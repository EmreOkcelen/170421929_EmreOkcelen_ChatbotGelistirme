import pandas as pd
import random
from itertools import cycle
from pathlib import Path

# Türkçe ve oyun temalı, birbirinden bağımsız intentler
intent_examples = {
    "Greeting": [
        "Selam!", "Merhaba, yardım edebilir misin?", "Hey orada!", "Nasılsın?"
    ],
    "Goodbye": [
        "Teşekkürler, görüşürüz!", "Hoşçakal!", "Çok sağ ol, bay bay"
    ],
        "Reject": [
        "Bunun oyunla ne ilgisi var?",
        "Ne dediğini anlamadım.",
        "Bu konu dışı, geçelim.",
        "Bununla ilgilenmiyorum.",
        "Ne demek istiyorsun tam olarak?",
        "Bu sistem bunu cevaplayamaz.",
        "Bu bir hata olabilir mi?"
    ],
    "GameEngineInfo": [
        "Unity mi Unreal mı önerirsin?", "Unreal Engine hakkında ne düşünüyorsun?",
        "Unity ile mobil oyun yapılır mı?", "En iyi oyun motoru hangisi?"
    ],
"BugFix": [
    "Karakter yere gömülüyor, bu bir bug olabilir mi?",
    "Platforma temas ettiğinde oyun çöküyor.",
    "Trigger collider'lar çalışmıyor.",
    "Play tuşuna bastığımda hiç bir şey olmuyor.",
    "Jump fonksiyonum çağrılıyor ama karakter tepki vermiyor.",
    "Animator parametreleri değişiyor ama animasyon başlamıyor.",
    "Scene yüklenince inputlar çalışmaz hale geliyor.",
    "Script hata veriyor ama hatayı çözemiyorum.",
    "Prefab'da yaptığım değişiklik oyuna yansımıyor.",
    "Build aldıktan sonra UI bozuluyor."
],
    "DesignAdvice": [
        "Yeni başlayanlar için oyun tasarımı nasıl olmalı?",
        "İyi bir seviye tasarımı nasıl yapılır?",
        "Oyunum çok sıkıcı oldu, ne önerirsin?",
        "Kullanıcıyı oyunda tutmak için ne yapmalıyım?"
    ],
"PerformanceOptimize": [
    "Build boyutu çok büyük, nasıl küçültebilirim?",
    "Oyunu oynarken FPS 15'e düşüyor, ne yapmalıyım?",
    "Profiler'da CPU usage çok yüksek görünüyor.",
    "Optimize etmeden önce neleri kontrol etmeliyim?",
    "Batching ile draw call sayısını düşürmek istiyorum.",
    "LOD sistemi performansı nasıl etkiler?",
    "Mobil cihazlarda kasıyor ama PC'de akıcı, neden?",
    "Işıklandırma performansı kötü etkiliyor olabilir mi?",
    "Asset import ayarları FPS'yi etkiler mi?",
    "Garbage collection oyun sırasında donma yapıyor."
],
    "PublishHelp": [
        "Oyunu Android'e nasıl export ederim?",
        "İlk defa oyunu yayınlıyorum, yardım edebilir misin?",
        "Google Play'e yüklemek zor mu?",
        "WebGL için nelere dikkat etmeliyim?"
    ],
    "AIHelp": [
        "Düşman AI’ı nasıl yapabilirim?",
        "Patrolling sistemi kurmak istiyorum.",
        "AI karakter neden oyuncuyu takip etmiyor?",
        "Basit bir saldırı algoritması lazım."
    ],
    "ControlScriptHelp": [
        "Karakterim tuşa basınca yürümüyor.",
        "Joystick input'u nasıl ayarlayabilirim?",
        "Kamera hareketini mouse ile kontrol etmek istiyorum.",
        "Input System 2.0 kullanmalı mıyım?"
    ],
    "AssetHelp": [
        "Ücretsiz ses efektleri nereden bulabilirim?",
        "Animasyonlar Unity'de neden bozuluyor?",
        "Sprite’ları nasıl sıkıştırmalıyım?",
        "3D assetleri nereden indirebilirim?"
    ]
}

# Hedef satır sayısı
target_size = 1500
data = []

# Verileri oluştur
while len(data) < target_size:
    for intent, examples in intent_examples.items():
        example = random.choice(examples)
        data.append({"Intent": intent, "Example": example})
        if len(data) >= target_size:
            break

# DataFrame oluştur ve dışa aktar
df = pd.DataFrame(data)
df.to_excel("test_intents_1000.xlsx", index=False)

print("Veri seti başarıyla oluşturuldu ve kaydedildi.")
