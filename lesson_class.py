import db_les
from flask import Response
from encoder import JSONEncoder
from bson.objectid import ObjectId
import pprint
import json



class json_lessons:

    def __init__(self):
        super().__init__()
        self.les = db_les.lessons.get_instance()
        self.json_ayt_data = {}
        self.json_tyt_data = {}
        self.response_data = {}
        self.ayt_list = []
        self.tyt_list = []
        self._id = None
        self.json_ayt_matematik = json_ayt_matematik_class
        self.json_ayt_geometri = json_ayt_geometri_class
        self.json_ayt_edebiyat = json_ayt_edebiyat_class
        self.json_ayt_fizik = json_ayt_fizik_class
        self.json_ayt_kimya = json_ayt_kimya_class
        self.json_ayt_biyoloji = json_ayt_biyoloji_class
        self.json_ayt_tarih = json_ayt_tarih_class
        self.json_ayt_cografya = json_ayt_cografya_class
        self.json_ayt_felsefe = json_ayt_felsefe_class

        self.json_tyt_matematik = json_tyt_matematik_class
        self.json_tyt_geometri = json_tyt_geometri_class
        self.json_tyt_turkce = json_tyt_turkce_class
        self.json_tyt_fizik = json_tyt_fizik_class
        self.json_tyt_kimya = json_tyt_kimya_class
        self.json_tyt_biyoloji = json_tyt_biyoloji_class
        self.json_tyt_tarih = json_tyt_tarih_class
        self.json_tyt_cografya = json_tyt_cografya_class
        self.json_tyt_felsefe = json_tyt_felsefe_class

    def send_response(self,object_id):
        self.set_objectId(object_id)
        return Response(JSONEncoder().encode(self.response_data),mimetype='application/json')

    def set_objectId(self,object_id):
        self._id = object_id
        self.get_json_data()
    
    def get_json_data(self):
        json_data = self.les.get_json_from_database(self._id)
        self.json_ayt_data = json_data.get("ayt")
        self.json_tyt_data = json_data.get("tyt")
        self.set_response_data()

    def set_response_data(self):
       self.set_ayt_subjects()
       self.set_tyt_subjects()
       self.set_ayt_list()
       self.set_tyt_list()
       self.response_data["_id"] = self._id
       self.response_data["ayt"] = self.ayt_list
       self.response_data["tyt"] = self.tyt_list


    def set_ayt_subjects(self):
        self.json_ayt_matematik["subject_state"] = self.json_ayt_data.get("matematik")
        self.json_ayt_geometri["subject_state"] = self.json_ayt_data.get("geometri")
        self.json_ayt_edebiyat["subject_state"] = self.json_ayt_data.get("edebiyat")
        self.json_ayt_fizik["subject_state"] = self.json_ayt_data.get("fizik")
        self.json_ayt_kimya["subject_state"] = self.json_ayt_data.get("kimya")
        self.json_ayt_biyoloji["subject_state"] = self.json_ayt_data.get("biyoloji")
        self.json_ayt_tarih["subject_state"] = self.json_ayt_data.get("tarih")
        self.json_ayt_cografya["subject_state"] = self.json_ayt_data.get("cografya")
        self.json_ayt_felsefe["subject_state"] = self.json_ayt_data.get("felsefe & din kültürü")

    def set_tyt_subjects(self):
        self.json_tyt_matematik["subject_state"] = self.json_tyt_data.get("matematik")
        self.json_tyt_geometri["subject_state"] = self.json_tyt_data.get("geometri")
        self.json_tyt_turkce["subject_state"] = self.json_tyt_data.get("turkce")
        self.json_tyt_fizik["subject_state"] = self.json_tyt_data.get("fizik")
        self.json_tyt_kimya["subject_state"] = self.json_tyt_data.get("kimya")
        self.json_tyt_biyoloji["subject_state"] = self.json_tyt_data.get("biyoloji")
        self.json_tyt_tarih["subject_state"] = self.json_tyt_data.get("tarih")
        self.json_tyt_cografya["subject_state"] = self.json_tyt_data.get("cografya")
        self.json_tyt_felsefe["subject_state"] = self.json_tyt_data.get("felsefe & din kültürü")
    
    def set_ayt_list(self):
        self.ayt_list.append(self.json_ayt_matematik)
        self.ayt_list.append(self.json_ayt_geometri)
        self.ayt_list.append(self.json_ayt_edebiyat)
        self.ayt_list.append(self.json_ayt_fizik)
        self.ayt_list.append(self.json_ayt_kimya)
        self.ayt_list.append(self.json_ayt_biyoloji)
        self.ayt_list.append(self.json_ayt_tarih)
        self.ayt_list.append(self.json_ayt_cografya)
        self.ayt_list.append(self.json_ayt_felsefe)

    def set_tyt_list(self):
        self.tyt_list.append(self.json_tyt_matematik)
        self.tyt_list.append(self.json_tyt_geometri)
        self.tyt_list.append(self.json_tyt_turkce)
        self.tyt_list.append(self.json_tyt_fizik)
        self.tyt_list.append(self.json_tyt_kimya)
        self.tyt_list.append(self.json_tyt_biyoloji)
        self.tyt_list.append(self.json_tyt_tarih)
        self.tyt_list.append(self.json_tyt_cografya)
        self.tyt_list.append(self.json_tyt_felsefe)

    def new_user(self,object_id):
        json_data = {
            "_id":ObjectId(object_id),
            "ayt":{
                "matematik":"0000000000000000000000000000000",
                "geometri":"0000000000000000000000000000000",
                "edebiyat":"0000000000000000000",
                "fizik":"000000000000000000000000000000000",
                "kimya":"000000000000000000000",
                "biyoloji":"0000000000000000000000000000",
                "tarih":"0000000000000000000000000000",
                "cografya":"0000000000000000000000000000000000",
                "felsefe & din kültürü":"00000000000000000000000000000000"
            },
            "tyt":{
                "matematik":"0000000000000000000000",
                "geometri":"000000000000000000000000",
                "turkce":"00000000000000000000000000",
                "fizik":"000000000000",
                "kimya":"0000000000",
                "biyoloji":"0000000000",
                "tarih":"000000000000000000000",
                "cografya":"0000000000000000000",
                "felsefe & din kültürü":"000000000000000000"
            }        
        }
        return self.les.set_new_user(json_data) 

json_ayt_matematik_class = {
    "lesson_name": "matematik",
    "subjects":[
        "Temel Kavramlar","Sayı Basamakları","Bölme ve Bölünebilme","EBOB – EKOK","Rasyonel Sayılar","Basit Eşitsizlikler","Mutlak Değer",
        "Üslü Sayılar","Köklü Sayılar","Çarpanlara Ayırma","Oran Orantı","Denklem Çözme","Problemler",
        "Kümeler","Kartezyen Çarpım","Mantık","Fonskiyonlar","Polinomlar","2.Dereceden Denklemler","Permütasyon ve Kombinasyon",
        "Olasılık","İstatistik","Karmaşık Sayılar","2.Dereceden Eşitsizlikler","Parabol","Trigonometri","Logaritma","Diziler","Limit","Türev","İntegral",
    ],
    "subject_state": "0000000000000000000000000000000"
}

json_tyt_matematik_class = {
    "lesson_name":"matematik",
    "subjects":[
        "Temel Kavramlar","Sayı Basamakları","Bölme ve Bölünebilme","EBOB – EKOK","Rasyonel Sayılar","Basit Eşitsizlikler","Mutlak Değer",
        "Üslü Sayılar","Köklü Sayılar","Çarpanlara Ayırma","Oran Orantı","Denklem Çözme","Problemler",
        "Kümeler","Kartezyen Çarpım","Mantık","Fonskiyonlar","Polinomlar","2.Dereceden Denklemler","Permütasyon ve Kombinasyon",
        "Olasılık","İstatistik"
        ],
        "subject_state":"0000000000000000000000"
}

json_ayt_geometri_class = {
    "lesson_name": "geometri",
    "subjects": [
        "Temel Kavramlar","Doğruda Açılar","Üçgende Açılar","Özel Üçgenler","Dik Üçgen","İkizkenar Üçgen",
        "Eşkenar Üçgen","Açıortay","Kenarortay","Üçgende Alan","Üçgende Benzerlik","Açı Kenar Bağıntıları","Çokgenler",
        "Dörtgenler","Deltoid","Paralelkenar","Eşkenar Dörtgen","Dikdörtgen","Kare","İkizkenar","Yamuk","Noktanın Analitiği",
        "Prizmalar","Piramitler","Doğrunun Analitiği","Çember ve Daire","Silindir","Koni","Küre","Dönüşüm Geometrisi","Çemberin Analitiği"
        ],
    "subject_state": "0000000000000000000000000000000"
}

json_tyt_geometri_class = {
    "lesson_name": "geometri",
    "subjects": [
        "Temel Kavramlar","Doğruda Açılar","Üçgende Açılar","Özel Üçgenler","Dik Üçgen","İkizkenar Üçgen",
        "Eşkenar Üçgen","Açıortay","Kenarortay","Üçgende Alan","Üçgende Benzerlik","Açı Kenar Bağıntıları","Çokgenler",
        "Dörtgenler","Deltoid","Paralelkenar","Eşkenar Dörtgen","Dikdörtgen","Kare","İkizkenar","Yamuk","Noktanın Analitiği",
        "Prizmalar","Piramitler"
        ],
    "subject_state":"000000000000000000000000"
}

json_ayt_edebiyat_class = {
    "lesson_name": "edebiyat",
    "subjects": [
        "Anlam Bilgisi","Dil Bilgisi","Güzel Sanatlar ve Edebiyat","Metinlerin Sınıflandırılması","Şiir Bilgisi",
        "Edebi Sanatlar","Türk Edebiyatı Dönemleri","İslamiyet Öncesi Türk Edebiyatı ve Geçiş Dönemi","Halk Edebiyatı","Divan Edebiyatı",
        "Tanzimat Edebiyatı","Servet-i Fünun Edebiyatı","Fecr-i Ati Edebiyatı"," Milli Edebiyat","Cumhuriyet Şiiri","Cumhuriyet Romanı",
        "Cumhuriyet Dönemi","Edebiyat Akımları","Dünya Edebiyatı"
        ],
    "subject_state": "0000000000000000000",
    "lesson_name": "edebiyat",
    "subjects": [
        "Anlam Bilgisi","Dil Bilgisi","Güzel Sanatlar ve Edebiyat","Metinlerin Sınıflandırılması","Şiir Bilgisi",
        "Edebi Sanatlar","Türk Edebiyatı Dönemleri","İslamiyet Öncesi Türk Edebiyatı ve Geçiş Dönemi","Halk Edebiyatı","Divan Edebiyatı",
        "Tanzimat Edebiyatı","Servet-i Fünun Edebiyatı","Fecr-i Ati Edebiyatı"," Milli Edebiyat","Cumhuriyet Şiiri","Cumhuriyet Romanı",
        "Cumhuriyet Dönemi","Edebiyat Akımları","Dünya Edebiyatı"
        ],
}

json_tyt_turkce_class = {
    "lesson_name": "turkce",
    "subjects": [
        "Sözcükte Anlam","Söz Yorumu","Deyim ve Atasözü","Cümlede Anlam","Paragrafta Anlam","Paragrafta Anlatım Teknikleri","Paragrafta Konu-Ana Düşünce",
        "Paragrafta Yapı","Paragrafta Yardımcı Düşünce","Ses Bilgisi","Yazım Kuralları","Noktalama İşaretleri","Sözcükte Yapı","Sözcük Türleri","İsimler",
        "Zamirler","Sıfatlar","Zarflar","Edat - Bağlaç - Ünlem","Fiil, Ek Fiil, Fiilimsi","Sözcük Grupları","Cümlenin Öğeleri","Cümle Türleri","Anlatım Bozukluğu"
    ],
    "subject_state":"00000000000000000000000000"
}

json_ayt_fizik_class = {
    "lesson_name":"fizik",
    "subjects":[
        "Fizik Bilimine Giriş","Madde ve Özellikleri","Sıvıların Kaldırma Kuvveti","Basınç","Isı, Sıcaklık ve Genleşme","Hareket",
        "Dinamik","İş, Güç ve Enerji","Elektrik","Optik","Manyetizma","Dalgalar","Vektörler","Kuvvet, Tork ve Denge","Kütle Merkezi",
        "Basit Makineler","Hareket","Newton’un Hareket Yasaları","İş, Güç ve Enerji II","Atışlar","İtme ve Momentum","Elektrik Alan ve Potansiyel",
        "Paralel Levhalar ve Sığa","Manyetik Alan ve Manyetik Kuvvet","İndüksiyon, Alternatif Akım ve Transformatörler","Çembersel Hareket",
        "Kütle Çekim ve Kepler Yasaları","Basit Harmonik Hareket","Dalga Mekaniği ve Elektromanyetik Dalgalar","Atom Modelleri","Büyük Patlama ve Radyoaktivite",
        "Modern Fizik","Modern Fiziğin Teknolojideki Uygulamaları"
        ],
    "subject_state":"000000000000000000000000000000000"
}

json_tyt_fizik_class = {
    "lesson_name":"fizik",
    "subjects":[
        "Fizik Bilimine Giriş","Madde ve Özellikleri","Sıvıların Kaldırma Kuvveti","Basınç","Isı, Sıcaklık ve Genleşme","Hareket",
        "Dinamik","İş, Güç ve Enerji","Elektrik","Optik","Manyetizma","Dalgalar"
    ],
    "subject_state":"000000000000"
}

json_ayt_kimya_class = {
    "lesson_name":"kimya",
    "subjects":[
        "Kimya Bilimi","Atom ve Periyodik Sistem","Kimyasal Türler Arası Etkileşimler","Kimyasal Hesaplamalar","Kimyanın Temel Kanunları",
        "Asit, Baz ve Tuz","Maddenin Halleri","Karışımlar","Doğa ve Kimya","Kimya Her Yerde","Modern Atom Teorisi","Gazlar","Çözeltiler",
        "Kimyasal Tepkimelerde Enerji","Kimyasal Tepkimelerde Hız","Kimyasal Tepkimelerde Denge","Asit-Baz Dengesi","Çözünürlük Dengesi",
        "Kimya ve Elektrik","Karbon Kimyasına Giriş","Organik Kimya"
        ],
    "subject_state":"000000000000000000000"
}

json_tyt_kimya_class = {
    "lesson_name":"kimya",
    "subjects":[
        "Kimya Bilimi","Atom ve Periyodik Sistem","Kimyasal Türler Arası Etkileşimler","Kimyasal Hesaplamalar","Kimyanın Temel Kanunları",
        "Asit, Baz ve Tuz","Maddenin Halleri","Karışımlar","Doğa ve Kimya","Kimya Her Yerde"
    ],
    "subject_state":"0000000000"
}

json_ayt_biyoloji_class = {
    "lesson_name":"biyoloji",
    "subjects":[
            "Canlıların Ortak Özellikleri","Canlıların Temel Bileşenleri","Hücre ve Organelleri","Hücre Zarından Madde Geçişi","Canlıların Sınıflandırılması",
            "Mitoz ve Eşeysiz Üreme","Mayoz ve Eşeyli Üreme","Kalıtım","Ekosistem Ekolojisi","Güncel Çevre Sorunları","Sinir Sistemi","Endokrin Sistem",
            "Duyu Organları","Destek ve Hareket Sistemi","Sindirim Sistemi","Dolaşım ve Bağışıklık Sistemi","Solunum Sistemi","Boşaltım Sistemi","Üriner Sistem",
            "Üreme Sistemi ve Embriyonik Gelişim","Komünite ve Popülasyon Ekolojisi","Nükleik Asitler","Genetik Şifre ve Protein Sentezi","Canlılık ve Enerji",
            "Fotosentez ve Kemosentez","Hücresel Solunum","Bitki Biyolojisi","Canlılar ve Çevre"
            ],
    "subject_state":"0000000000000000000000000000"
}

json_tyt_biyoloji_class = {
    "lesson_name":"biyoloji",
    "subjects":[
            "Canlıların Ortak Özellikleri","Canlıların Temel Bileşenleri","Hücre ve Organelleri","Hücre Zarından Madde Geçişi","Canlıların Sınıflandırılması",
            "Mitoz ve Eşeysiz Üreme","Mayoz ve Eşeyli Üreme","Kalıtım","Ekosistem Ekolojisi","Güncel Çevre Sorunları"
    ],
    "subject_state":"0000000000"
}

json_ayt_tarih_class = {
    "lesson_name":"tarih",
    "subjects":[
        "Tarih Bilimi","İlk Uygarlıklar","İlk Türk Devletleri","İslam Tarihi ve Uygarlığı","Türk-İslam Devletleri","Orta Çağ ve Avrupa Tarihi",
        "Türkiye Tarihi","Beylikten Devlete (1300-1453)","Dünya Gücü: Osmanlı Devleti (1453-1600)","Osmanlı Kültür ve Medeniyeti","Yeni ve Yakın Çağda Avrupa Tarihi",
        "Arayış Yılları (17. Yüzyıl)","Yeni Çağda Avrupa","En Uzun Yüzyıl (1800-1922)","20. Yüzyıl Başlarında Osmanlı Devleti",
        "1. Dünya Savaşı – Milli Mücadeleye Hazırlık Dönemi","Kurtuluş Savaşı ve Antlaşmalar","I. TBMM Dönemi","Türk İnkılabı","Atatürkçülük ve Atatürk İlkeleri",
        "Türk Dış Politikası","Atatürk’ün Ölümü","20. yy Başlarında Dünya","İkinci Dünya Savaşı","Soğuk Savaş Dönemi","Yumuşama Dönemi ve Sonrası","Küreselleşen Dünya",
        "XXI. Yüzyılın Eşiğinde Türkiye ve Dünya"
        ],
    "subject_state":"0000000000000000000000000000"
}

json_tyt_tarih_class = {
    "lesson_name":"tarih",
    "subjects":[
        "Tarih Bilimi","İlk Uygarlıklar","İlk Türk Devletleri","İslam Tarihi ve Uygarlığı","Türk-İslam Devletleri","Orta Çağ ve Avrupa Tarihi",
        "Türkiye Tarihi","Beylikten Devlete (1300-1453)","Dünya Gücü: Osmanlı Devleti (1453-1600)","Osmanlı Kültür ve Medeniyeti","Yeni ve Yakın Çağda Avrupa Tarihi",
        "Arayış Yılları (17. Yüzyıl)","Yeni Çağda Avrupa","En Uzun Yüzyıl (1800-1922)","20. Yüzyıl Başlarında Osmanlı Devleti",
        "1. Dünya Savaşı – Milli Mücadeleye Hazırlık Dönemi","Kurtuluş Savaşı ve Antlaşmalar","I. TBMM Dönemi","Türk İnkılabı","Atatürkçülük ve Atatürk İlkeleri",
        "Türk Dış Politikası"
        ],
    "subject_state":"000000000000000000000"
}

json_ayt_cografya_class = {
    "lesson_name":"cografya",
    "subjects":[
        "Doğa ve İnsan","Dünya’nın Şekli ve Hareketleri","Coğrafi Konum","Harita Bilgisi","Atmosfer ve Sıcaklık","İklimler",
        "Basınç ve Rüzgarlar","Nem, Yağış ve Buharlaşma","İç Kuvvetler / Dış Kuvvetler","Su – Toprak ve Bitkiler","Nüfus","Göç","Yerleşme",
        "Türkiye’nin Yer Şekilleri","Ekonomik Faaliyetler","Bölgeler","Uluslararası Ulaşım Hatları","Çevre ve Toplum","Doğal Afetler","Ekosistem",
        "Doğadaki Ekstrem Olaylar","İlk Medeniyet ve Şehirler","Nüfus Politikaları"," Türkiye’de Nüfus ve Yerleşme","Ekonomik Faaliyetler","Göç ve Şehirleşme",
        "Türkiye Ekonomisi","Türkiye’nin Jeopolitik Konumu","Bölgesel Kalkınma Projeleri","İklim ve Yer şekilleri","Ülkeler Arası Etkileşim","Küresel ve Bölgesel Örgütler",
        "Üretim Alanları ve Ulaşım Ağları","Bölgeler ve Ülkeler"
        ],
    "subject_state":"0000000000000000000000000000000000"
}

json_tyt_cografya_class = {
    "lesson_name":"cografya",
    "subjects":[
        "Doğa ve İnsan","Dünya’nın Şekli ve Hareketleri","Coğrafi Konum","Harita Bilgisi","Atmosfer ve Sıcaklık","İklimler",
        "Basınç ve Rüzgarlar","Nem, Yağış ve Buharlaşma","İç Kuvvetler / Dış Kuvvetler","Su – Toprak ve Bitkiler","Nüfus","Göç","Yerleşme",
        "Türkiye’nin Yer Şekilleri","Ekonomik Faaliyetler","Bölgeler","Uluslararası Ulaşım Hatları","Çevre ve Toplum","Doğal Afetler"
    ],
    "subject_state":"0000000000000000000"
}

json_ayt_felsefe_class = {
    "lesson_name":"felsefe & din kültürü",
    "subjects":[
        "Felsefe’nin Konusu","Bilgi Felsefesi","Varlık Felsefesi","Ahlak Felsefesi","Sanat Felsefesi","Din Felsefesi","Siyaset Felsefesi","Bilim Felsefesi",
        "Mantığa Giriş","Klasik Mantık","Mantık ve Dil","Sembolik Mantık","Psikoloji Bilimini Tanıyalım","Psikolojinin Temel Süreçleri","Öğrenme Bellek Düşünme",
        "Ruh Sağlığının Temelleri","Sosyolojiye Giriş","Birey ve Toplum","Toplumsal Yapı","Toplumsal Değişme ve Gelişme","Toplum ve Kültür","Toplumsal Kurumlar",
        "Bilgi ve İnanç","İslam ve İbadet","Ahlak ve Değerler","Allah İnsan İlişkisi","Hz. Muhammed (S.A.V.)","Vahiy ve Akıl","İslam Düşüncesinde Yorumlar, Mezhepler",
        "Din, Kültür ve Medeniyet","İslam ve Bilim, Estetik, Barış","Yaşayan Dinler"
        ],
    	"subject_state":"00000000000000000000000000000000"
}

json_tyt_felsefe_class = {
    "lesson_name":"felsefe & din kültürü",
    "subjects":[
        "Felsefe’nin Konusu","Bilgi Felsefesi","Varlık Felsefesi","Ahlak Felsefesi","Sanat Felsefesi","Din Felsefesi","Siyaset Felsefesi","Bilim Felsefesi",
        "Bilgi ve İnanç","İslam ve İbadet","Ahlak ve Değerler","Allah İnsan İlişkisi","Hz. Muhammed (S.A.V.)","Vahiy ve Akıl","İslam Düşüncesinde Yorumlar, Mezhepler",
        "Din, Kültür ve Medeniyet","İslam ve Bilim, Estetik, Barış","Yaşayan Dinler"
        ],
        "subject_state":"000000000000000000"
}




