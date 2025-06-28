# 🎮 Oyun Geliştirme Chatbot - LLM Tabanlı Oyun Geliştirme Asistanı

Bu proje, oyun geliştirme süreçlerine yönelik soruları hızlı ve doğru yanıtlayabilen, yapay zekâ destekli bir sohbet botu geliştirmeyi amaçlamaktadır.

# Proje Çalışmadığı noktada ulaşım sağlanabilecek Link:
- https://colab.research.google.com/drive/1gbwReNQc8yTv17k8ITfRXQ4c8NxhGaMi?usp=sharing

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

• **ControlScriptHelp** – Kontrol ve input scriptleri yardımı

• **AssetHelp** – Oyun varlıkları (asset) yardımı


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


 2) Modeli eğit -> Kodun ilgili kısmında model eğitimi yapılır. (Eğitilmiş model klasörü models/roberta_intent_model veya models/bert_intent_model olarak kaydedilmiştir.)

    ![image](https://github.com/user-attachments/assets/38c08a5a-2136-4c0e-aef1-7955f7b7a791)


 3) Modeli eğittikten sonra Niyet Modellerini, OpenAI Chatbot mesaj sistemini ve uygulama üzerinden güncel sonuçları görmek üzere değerlendirmeler Kod dizimini çalıştır

    ![image](https://github.com/user-attachments/assets/6da394b1-2dca-4aa2-a311-fc80a4587716)

    
 4) Chatbot'u başlat

  - streamlit run app.py
  - Ngrok ile internete aç

    ![image](https://github.com/user-attachments/assets/794be457-3650-4cbc-9025-e9638979e4b2)




# 📊 Sonuçlar

Modelin doğruluk ve F1 skoru gibi performans metrikleri **Trainer.evaluate()** ile hesaplanmış ve bir **Confusion Matrix** oluşturulmuştur.

 - **BERT Modeli Değerlendirme Sonuçları:**

    ![WhatsApp Görsel 2025-06-28 saat 16 22 12_0c001726](https://github.com/user-attachments/assets/3ad1f981-6714-410a-ace7-7b785d906650)

   ![WhatsApp Görsel 2025-06-28 saat 16 22 50_deabb03b](https://github.com/user-attachments/assets/ad8e1763-2e60-41ca-a1a7-725301ada222)


 - **RoBERTa Modeli Değerlendirme Sonuçları:**

    ![WhatsApp Görsel 2025-06-28 saat 16 42 19_acf0608f](https://github.com/user-attachments/assets/eff0a5fd-1da0-45f3-8caa-4d45111914c3)

  ![WhatsApp Görsel 2025-06-28 saat 16 42 07_5b8b9a8a](https://github.com/user-attachments/assets/5d40e308-9424-4c08-9adc-2c2208701309)


# 📊 Model Performansı Karşılaştırma Tablosu

![WhatsApp Görsel 2025-06-28 saat 16 50 09_1ef14a9f](https://github.com/user-attachments/assets/7b3a20c6-cbfe-40e4-ae9e-2d9db3aaf8bb)


# 🖥️ Chatbot Arayüzü

Proje kapsamında geliştirilen web tabanlı arayüz, **Streamlit** kullanılarak kullanıcı dostu bir etkileşim ortamı sunar. Arayüz, oyun geliştiricilere yönelik soruların otomatik olarak sınıflandırılmasını ve bu sınıflamaya uygun GPT-3.5 yanıtlarının üretilmesini sağlar.

 - **🎛️ Temel Özellikler:**
   1) **Niyet Sınıflandırması:** Kullanıcının yazdığı metin, seçilen modele (BERT veya RoBERTa) iletilerek niyeti (intent) tahmin edilir.

   2) **LLM Yanıtı (GPT-3.5):** Tahmin edilen niyet, kullanıcının girdisiyle birlikte OpenAI API'ye gönderilir ve kısa, konuya uygun bir yanıt üretilir.

      ![WhatsApp Görsel 2025-06-28 saat 16 21 23_7e72e988](https://github.com/user-attachments/assets/4382dd6b-6d48-461b-a5aa-3ffcc1146888)


   3) **Yanıt ve Niyet Görselleştirme:** Tahmin edilen niyet emojili olarak sunulur ve GPT yanıtı bilgilendirici kutuda gösterilir.

   4) **Geçmiş Görüntüleme:** Son 5 giriş, arayüzün sol panelinde zaman damgası ve model bilgisiyle birlikte görüntülenebilir.

      ![WhatsApp Görsel 2025-06-28 saat 15 58 05_a6e71454](https://github.com/user-attachments/assets/252d0b61-3109-47bb-a3f8-dea115b41cba)


   5) **Model Performans Karşılaştırması:** Ayrı bir sekmede Precision, Recall ve F1 metriklerine göre BERT ve RoBERTa modelleri kıyaslanabilir. Sonuçlar tablo, bar chart ve radar chart ile görselleştirilir.

      ![WhatsApp Görsel 2025-06-28 saat 16 47 30_8b790e44](https://github.com/user-attachments/assets/0d045fe3-9d88-4824-af17-8f1520e2fea2)


   6) **Confusion Matrix:** Üçüncü sekmede, her iki modelin sınıflandırma doğruluğu karışıklık matrisi üzerinden detaylı biçimde analiz edilebilir.

      ![WhatsApp Görsel 2025-06-28 saat 16 48 58_98ad2e3a](https://github.com/user-attachments/assets/135e1312-de82-492f-be20-1dca7f5505dc)



# 🖼️ Intent’lerin Ekran Görüntüleri


**👋 Greeting – Selamlama**

![WhatsApp Görsel 2025-06-28 saat 15 41 07_1007a24f](https://github.com/user-attachments/assets/d6349ed2-07eb-4210-89f6-f5260851a5f6)


**📴 Goodbye – Vedalaşma**

![WhatsApp Görsel 2025-06-28 saat 15 54 37_144d9c15](https://github.com/user-attachments/assets/c175c516-794d-42ea-882c-c5e845980b57)


**❓ Reject – Anlamama / Konu Dışı**

![WhatsApp Görsel 2025-06-28 saat 15 56 50_61bd63e5](https://github.com/user-attachments/assets/6ebc9e4e-d23e-4678-988d-44bfcc51c6e4)


**🛠️ GameEngineInfo – Oyun Motoru Bilgisi**

![WhatsApp Görsel 2025-06-28 saat 15 40 51_fa17c32b](https://github.com/user-attachments/assets/b8f484f5-0f94-460e-ad22-fbf9fa290a26)


**🐞 BugFix – Hata Giderme**

![WhatsApp Görsel 2025-06-28 saat 15 45 29_9b8f6152](https://github.com/user-attachments/assets/75e23c8d-946e-4f2a-8b2e-ab7fd153494f)


**🎨 DesignAdvice – Tasarım Tavsiyesi**

![WhatsApp Görsel 2025-06-28 saat 15 46 03_1fb77fec](https://github.com/user-attachments/assets/ae0e9648-7643-40aa-a560-aa072fd1a947)


**⚡ PerformanceOptimize – Performans Optimizasyonu**

![WhatsApp Görsel 2025-06-28 saat 16 02 56_5e9f8d61](https://github.com/user-attachments/assets/b4d997dd-edfe-487c-b1a1-f19eaa59ba36)


**🚀 PublishHelp – Yayınlama Yardımı**

![WhatsApp Görsel 2025-06-28 saat 16 03 46_e0d32949](https://github.com/user-attachments/assets/b0d37d02-7f87-46dc-8d93-4155e52a9931)


**🤖 AIHelp – Yapay Zeka Yardımı**

![WhatsApp Görsel 2025-06-28 saat 15 42 49_bf862ee9](https://github.com/user-attachments/assets/e66b754f-65da-4b4f-a6c3-a5c84cba3bcd)


**🎮 ControlScriptHelp – Kontroller ve Input**

![WhatsApp Görsel 2025-06-28 saat 16 00 21_4ef91056](https://github.com/user-attachments/assets/8dc9bc3d-1509-4bf4-8db8-7b6fced44435)


**📦 AssetHelp – Asset Yönetimi**

![WhatsApp Görsel 2025-06-28 saat 15 53 38_5fbbcfb1](https://github.com/user-attachments/assets/9ebf7d54-569b-4334-9727-086d9b522a7c)

