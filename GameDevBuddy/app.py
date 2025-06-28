import sys
import os
import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix
from sklearn.model_selection import train_test_split
sys.path.append("/content/drive/MyDrive/Colab Notebooks/GameDevBuddy")


# app.py'nin bulunduğu dizin
current_dir = os.path.dirname(os.path.abspath(__file__))

# Proje ana dizini
project_root = current_dir

# Proje ana dizinini python path'e ekle
if project_root not in sys.path:
    sys.path.append(project_root)

from models.bert_intent_model import bert_intent_predict
from models.roberta_intent_model import roberta_intent_predict
from utils.openai_utils import generate_gpt_response  # ✅ GPT entegrasyonu

# Streamlit sayfa ayarları
st.set_page_config(page_title="🎮 Game Dev Buddy", page_icon="🎮", layout="wide")

# Karanlık tema
st.markdown(
    """
    <style>
    .main { background-color: #0f111a; color: #cfd8dc; font-family: 'Segoe UI'; }
    h1, h2, h3 { color: #61dafb; text-shadow: 0 0 5px #61dafb; }
    div.stButton > button {
        background-color: #1e88e5; color: white; border-radius: 8px;
        font-weight: bold; padding: 8px 20px;
    }
    div.stButton > button:hover { background-color: #42a5f5; }
    section[data-testid="stSidebar"] { background-color: #121826; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎮 Game Dev Buddy")


intent_emojis = {
    "Greeting": "👋 Merhaba",
    "Goodbye": "📴 Hoşçakal",
    "Reject": "❓ Anlamadım",
    "GameEngineInfo": "🛠️ Motor Bilgisi",
    "BugFix": "🐞 Hata Giderme",
    "DesignAdvice": "🎨 Tasarım Tavsiyesi",
    "PerformanceOptimize": "⚡ Performans",
    "PublishHelp": "🚀 Yayınlama Yardımı",
    "AIHelp": "🤖 Yapay Zeka",
    "ControlScriptHelp": "🎮 Kontroller",
    "AssetHelp": "📦 Asset Yardımı"
}


# Tabs
tab1, tab2, tab3 = st.tabs(["💬 Chatbot", "📈 Performance", "🧩 Confusion Matrix"])

with tab1:
    with st.sidebar:
        st.header("ℹ️ Bu Uygulama Hakkında")
        st.markdown("""
Bu asistan, **kullanıcının niyetini (intent)** tahmin eder (BERT veya RoBERTa ile) ve uygun şekilde **GPT-3.5 cevabı üretir**.

**💡 Intentler:**
- 👋 Greeting: Sohbet başlatma
- 📴 Goodbye: Sohbet sonlandırma
- ❓ Reject: Konu dışı mesajlar
- 🛠️ GameEngineInfo: Oyun motoru soruları
- 🐞 BugFix: Kod hatası yardımı
- 🎨 DesignAdvice: Tasarım tavsiyesi
- ⚡ PerformanceOptimize: Performans sorunları
- 🚀 PublishHelp: Yayınlama soruları
- 🤖 AIHelp: Yapay zeka yardımı
- 🎮 ControlScriptHelp: Kontrol ve hareket scriptleri
- 📦 AssetHelp: Asset kaynakları
        """)

        if 'history' in st.session_state and st.session_state.history:
            st.subheader("📜 Son 5 Tahmin")
            for ts, question, model, predicted, gpt_reply in reversed(st.session_state.history[-5:]):
                emoji = intent_emojis.get(predicted, "❓")
                with st.expander(f"{ts} - {model}: {question}"):
                    st.markdown(f"- **Intent:** {emoji} `{predicted}`")
                    st.markdown(f"- **ChatGPT Cevabı:** {gpt_reply}")

    model_choice = st.selectbox("🧠 Model Seç:", ["BERT", "RoBERTa"])
    user_input = st.text_input("✏️ Bir şey sor:")

    if 'history' not in st.session_state:
        st.session_state.history = []

    if st.button("🧪 Tahmin Et"):
        if not user_input.strip():
            st.warning("⚠️ Lütfen bir soru girin.")
        else:
            intent = (
                bert_intent_predict(user_input)
                if model_choice == "BERT"
                else roberta_intent_predict(user_input)
            )
            gpt_response = generate_gpt_response(intent, user_input)
            emoji = intent_emojis.get(intent, "❓")
            timestamp = datetime.now().strftime('%H:%M:%S')
            st.session_state.history.append((timestamp, user_input, model_choice, intent, gpt_response))

            st.markdown("### 🎯 Tahmin Edilen Intent")
            st.markdown(f"**{emoji} `{intent}`**")

            st.markdown("### 🤖 ChatGPT Yanıtı")
            st.info(gpt_response)

with tab2:
    st.header("📈 Model Performance Comparison")

    @st.cache_data
    def evaluate_models():
        df = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/GameDevBuddy/data/test_intents_1500.xlsx")
        train, test = train_test_split(df, test_size=0.2, stratify=df['Intent'], random_state=42)
        X_test = test['Example'].tolist()
        y_test = test['Intent'].tolist()

        def run_eval(predict_fn):
            preds = [predict_fn(x) for x in X_test]
            precision, recall, f1, _ = precision_recall_fscore_support(y_test, preds, average='weighted')
            return y_test, preds, precision, recall, f1

        y_test, bert_preds, p1, r1, f1 = run_eval(bert_intent_predict)
        _, roberta_preds, p2, r2, f2 = run_eval(roberta_intent_predict)

        return {
            "BERT": (p1, r1, f1, y_test, bert_preds),
            "RoBERTa": (p2, r2, f2, y_test, roberta_preds)
        }

    results = evaluate_models()

    # Performans metriklerini DataFrame'e aktar
    metrics = ["Precision", "Recall", "F1"]
    df_metrics = pd.DataFrame({
        "Metric": metrics,
        "BERT": results["BERT"][:3],
        "RoBERTa": results["RoBERTa"][:3]
    })

    # Dropdown filtre
    selected_metric = st.selectbox("🔍 Choose Metric to View:", metrics + ["All"])

    if selected_metric != "All":
        filtered_df = df_metrics[df_metrics["Metric"] == selected_metric]
    else:
        filtered_df = df_metrics

    # Tablo görünümü
    st.dataframe(filtered_df.set_index("Metric"), use_container_width=True)

    # CSV dışa aktarma
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name='model_metrics.csv',
        mime='text/csv'
    )

    # Bar ve radar grafiklerini yan yana
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Bar Chart")
        st.bar_chart(filtered_df.set_index("Metric"))

    with col2:
        st.subheader("🕸️ Radar Chart")
        if selected_metric == "All":
            def radar_plot(data_dict):
                angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
                angles += angles[:1]
                fig, ax = plt.subplots(figsize=(4.5, 4.5), subplot_kw=dict(polar=True))
                for name, vals in data_dict.items():
                    vals += vals[:1]
                    ax.plot(angles, vals, label=name)
                    ax.fill(angles, vals, alpha=0.25)
                ax.set_theta_offset(np.pi / 2)
                ax.set_theta_direction(-1)
                ax.set_thetagrids(np.degrees(angles[:-1]), metrics)
                ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
                st.pyplot(fig)

            radar_plot({
                "BERT": list(results["BERT"][:3]),
                "RoBERTa": list(results["RoBERTa"][:3])
            })
        else:
            st.info("Radar chart only available when 'All' is selected.")

with tab3:
    st.header("🧩 Confusion Matrix")
    selected_model = st.selectbox("Choose Model:", ["BERT", "RoBERTa"], key="matrix_select")
    _, _, _, y_true, y_pred = results[selected_model]

    labels = sorted(set(y_true))
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=labels, yticklabels=labels, cmap='Blues')
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Actual")
    ax.set_title(f"{selected_model} Confusion Matrix")
    st.pyplot(fig)