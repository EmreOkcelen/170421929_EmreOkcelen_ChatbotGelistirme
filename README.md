# 🎮 Oyun Geliştirme Chatbot - LLM Tabanlı Oyun Geliştirme Asistanı

Bu proje, oyun geliştirme süreçlerine yönelik soruları hızlı ve doğru yanıtlayabilen, yapay zekâ destekli bir sohbet botu geliştirmeyi amaçlamaktadır.


# 📌 Projenin Amacı

Bu projenin temel amacı, belirli **intent** türlerine göre etiketlenmiş veri setiyle eğitilen ve farklı büyük dil modelleri (LLM) ile karşılaştırmalı olarak test edilen bir chatbot geliştirmektir. Chatbot, önceden belirlenmiş intent (niyet) kategorilerine göre kullanıcıdan gelen ifadeleri sınıflandırmakta ve uygun yanıtları üretmektedir.

Uygulama süreci aşağıdaki aşamaları kapsamaktadır:

- Intent tabanlı veri seti oluşturma

- LLM modelleri ile eğitme (BERT VE RoBERTa)

- Performans karşılaştırması (Precision, Recall, F1 Score, Confusion Matrix)

- Uygulama arayüzü geliştirme (Streamlit)


# 📁 Veri Seti Oluşturma

Bu proje kapsamında, oyun geliştirme alanına özgü farklı niyet türlerini (intent) kapsayan 1500 satırlık bir veri seti oluşturulmuştur. Her satırda bir intent ve bu intent’e karşılık gelen örnek kullanıcı cümlesi yer almaktadır. Veri seti, yapay zekâ tabanlı oyun geliştirme asistanının kullanıcı niyetlerini doğru anlaması için kullanılacaktır.


# 🎯 Intentler (Niyet Türleri)

Projede kullanılan başlıca intentler şunlardır:

• **Greeting** – Selamlama

• **Goodbye** – Vedalaşma

• **Reject** – Reddetme

• **GameEngineInfo** – Oyun motorları hakkında bilgi

• **BugFix** – Hata/bug bildirimleri

• **DesignAdvice** – Oyun tasarımı önerileri

• **PerformanceOptimize** – Performans optimizasyonu

• **PublishHelp** – Oyun yayınlama yardımı

• **AIHelp** – Yapay zeka/savaşçı yapımı desteği

• ControlScriptHelp – Kontrol ve input scriptleri yardımı

• AssetHelp – Oyun varlıkları (asset) yardımı


# 🔨 Veri Üretim Süreci

Veri seti, Python programlama dili kullanılarak otomatik bir yöntemle oluşturulmuştur. Her bir niyet (intent) türü için çeşitli örnek cümleler tanımlanmış ve bu cümlelerden rastgele seçimler yapılarak toplamda 1500 satırlık etiketli bir veri seti üretilmiştir. Elde edilen veri seti, analiz ve model eğitimi amaçlı olarak Kaggle platformuna yüklenmiştir.

🔗 Kaggle veri seti bağlantısı: https://www.kaggle.com/datasets/emreokelen/game-dev-buddy-dataset-1500-intent


# 🧠 Kullanılan LLM Modelleri

Proje kapsamında iki farklı büyük dil modeli (LLM) ile chatbot eğitimi gerçekleştirilmiştir:

**BERT**: Google tarafından geliştirilen ve doğal dil anlama görevlerinde yaygın şekilde kullanılan transformer tabanlı bir dil modelidir. Projenin ilk sürümünde temel performansın değerlendirilmesi amacıyla tercih edilmiştir.

**RoBERTa**: BERT modelinin optimize edilmiş ve daha geniş veri kümeleri üzerinde yeniden eğitilmiş bir varyantıdır. Niyet sınıflandırma doğruluğunu artırmak için, BERT modelinden sonra daha gelişmiş bir alternatif olarak projeye entegre edilmiştir.

Projenin erken aşamalarında, DistilBERT modeli denenmiş; ancak bu modelin niyet tahminlerinde yeterli doğruluk ve kararlılık sağlayamaması nedeniyle BERT ve RoBERTa modelleri kullanılmış ve başarılı sonuçlar elde edilmiştir.


# 📌 Kullanılan Teknolojiler

- Python
- OpenAI API
- Streamlit
- Kaggle
- Ngrok


# 🔑 Kullanılan API

- **OpenAI** **API** (GPT-3.5 ile yanıt üretimi)

- **🔐 OpenAI API Anahtarı ve Entegrasyonu**

1) OpenAI Python SDK’sı (openai modülü yerine openai paketinin yeni sürümü olan OpenAI sınıfı) kullanılarak API entegrasyonu sağlanmıştır.

2) API anahtarı doğrudan OpenAI sınıfının api_key parametresi olarak kod içerisinde güvenli şekilde tanımlanmıştır.

3) Chat tabanlı yanıt üretimi için client.chat.completions.create() fonksiyonu çağrılarak **GPT-3.5-turbo** modeli kullanılmıştır.

4) İstemci (client) uygulama içerisinde, kullanıcı niyeti (intent) ve kullanıcının sorusu sistem mesajı formatında modele iletilmiş, modelden kısa ve net yanıt alınmıştır.

5) Yanıt üretimi sırasında hata yönetimi try-except bloğu ile sağlanmıştır.


# 🛠️ Model Eğitimi

Model eğitimi, Hugging Face’in **transformers** kütüphanesi kullanılarak gerçekleştirilmiştir. Aşağıdaki adımlar izlenmiştir:

- **Veri Ön İşleme:**

  • Veri setindeki intent (niyet) etiketleri **LabelEncoder** ile sayısal sınıf etiketlerine dönüştürülmüştür.

  • Veri seti, **train_test_split** fonksiyonu ile %80 eğitim, %20 doğrulama olacak şekilde stratifikasyonlu olarak bölünmüştür.

- **Tokenizasyon:**

  • **AutoTokenizer** kullanılarak metin verileri token'lara dönüştürülmüştür.

  • Girdi dizileri, maksimum uzunluk 128 token olacak şekilde, **padding ve truncation** uygulanmıştır.

- **Dataset Hazırlama:**

  • Tokenize edilmiş veriler ve etiketler, PyTorch tabanlı özel bir Dataset sınıfı (IntentDataset) ile paketlenmiştir.

- **Model Yapılandırması:**

  • Eğitilmiş modeller **AutoModelForSequenceClassification** ile yüklenmiştir.

  • Model konfigürasyonunda sınıf sayısı (**num_labels**) güncellenmiş, ayrıca dropout oranları (hidden ve attention) 0.3 olarak belirlenmiştir.

- **Eğitim ve Değerlendirme:**

  • **Trainer ve TrainingArguments** kullanılarak model  eğitilmiştir.

  • Eğitim parametreleri arasında batch size, learning rate, erken durdurma (EarlyStoppingCallback), en iyi model kaydetme ve epoch bazlı değerlendirme stratejisi bulunmaktadır.

  • Performans metrikleri olarak **accuracy**, **precision**, **recall** ve **F1-score** hesaplanmıştır.

  • Eğitim ve doğrulama sonuçları konsola yazdırılmış, ayrıca doğrulama sonuçları için karışıklık matrisi (**confusion matrix**) görselleştirilmiştir.

- **Model Kaydetme ve Yükleme:**

  • Eğitim sonunda **model, tokenizer ve LabelEncoder** objesi belirlenen dizine kaydedilmiştir.

  • Modelin yeniden kullanımı için kaydedilen dosyalar yüklenmiş ve kullanılmaya hazır hale getirilmiştir.



# 🔓 Kullanım

 1) Gereksinimleri yükle -> pip install -r requirements.txt
    ![image](https://github.com/user-attachments/assets/d6efbf80-f3d4-4588-b96a-21cb08564c65)


 3) Modeli eğit -> Kodun ilgili kısmında model eğitimi yapılır. (Eğitilmiş model klasörü models/roberta_intent_model veya models/bert_intent_model olarak kaydedilmiştir.)

 4) Chatbot'u başlat

  - streamlit run app.py
  - Ngrok ile internete aç


📊 Sonuçlar

Modelin doğruluk ve F1 skoru gibi performans metrikleri Trainer.evaluate() ile hesaplanmış ve bir Confusion Matrix oluşturulmuştur.

BERT Modeli Değerlendirme Sonuçları:

image image

RoBERTa Modeli Değerlendirme Sonuçları:

image image

📊 Model Performansı Karşılaştırma Tablosu

image

🖥️ Chatbot Arayüzü

Streamlit ile geliştirilen arayüz sayesinde kullanıcılar metin giriş alanına üniversiteyle ilgili sorularını yazabilirler. Sistem, soru metnini RoBERTa veya BERT modeline gönderir ve niyeti tahmin eder. Bu niyeti GPT-3.5'e ileterek uygun yanıt üretilmesini sağlar. Kullanıcıya tahmin edilen niyet ve yanıtı gösterir.

Streamlit Ekran Görüntüleri

RoBERTa + GPT3.5 Destekli Chatbot Tasarımı

Greeting Intent

image

DormitoryInfo Intent

image

Registration Intent

image

EventInfo Intent

image

ContactInfo Intent

image

Goodbye Intent

image

ScholarshipInfo Intent

image

DepartmentInfo Intent

image

Reject Intent

image

BERT + GPT3.5 Destekli Chatbot Tasarımı

image
