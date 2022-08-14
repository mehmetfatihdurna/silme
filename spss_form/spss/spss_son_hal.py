from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,QButtonGroup,QRadioButton,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import os
import spss_func


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):

        #soru1
        self.question1 = QLabel("1-Cinsiyetiniz:")
        self.bg1 = QButtonGroup()
        self.answer11 = QRadioButton("1-Kadın")
        self.answer12 = QRadioButton("2-Erkek")
        self.bg1.addButton(self.answer11)
        self.bg1.addButton(self.answer12)

        #soru2
        self.question2 = QLabel("2-Yaşınız:")
        self.answer21 = QLineEdit()

        #soru3
        self.question3 = QLabel("3-Medeni Durumunuz:")
        self.bg3 = QButtonGroup(self)
        self.answer31 = QRadioButton("1-Evli",self)
        self.answer32 = QRadioButton("2-Bekar",self)
        self.bg3.addButton(self.answer31)
        self.bg3.addButton(self.answer32)

        #soru4
        self.question4 = QLabel("4-Mezuniyet durumunuz:")
        self.bg4 = QButtonGroup(self)
        self.answer41 = QRadioButton("1-Ortaöğğretim",self)
        self.answer42 = QRadioButton("2-Ön Lisans",self)
        self.answer43 = QRadioButton("3-Lisans",self)
        self.answer44 = QRadioButton("4-Lisansüstü",self)
        self.bg4.addButton(self.answer41)
        self.bg4.addButton(self.answer42)
        self.bg4.addButton(self.answer43)
        self.bg4.addButton(self.answer44)

        #soru5
        self.question5 = QLabel("5-Uzun süredir yaşadığınız yer:")
        self.bg5 = QButtonGroup(self)
        self.answer51 = QRadioButton("1-Köy-kasaba",self)
        self.answer52 = QRadioButton("2-İlçe",self)
        self.answer53 = QRadioButton("3-İl",self)
        self.answer54 = QRadioButton("4-Yurtdışı",self)
        self.bg5.addButton(self.answer51)
        self.bg5.addButton(self.answer52)
        self.bg5.addButton(self.answer53)
        self.bg5.addButton(self.answer54)

        #soru6
        self.question6 = QLabel("6-Uzun süredir yaşadığınız yer:")
        self.bg6 = QButtonGroup(self)
        self.answer61 = QRadioButton("1-Karadeniz Bölgesi",self)
        self.answer62 = QRadioButton("2-İç Anadolu Bölgesi",self)
        self.answer63 = QRadioButton("3-Ege-Marmara Bölgesi",self)
        self.answer64 = QRadioButton("4-Akdeniz Bölgesi",self)
        self.answer65 = QRadioButton("5-Doğu Anadolu-Güneydoğu Anadolu Bölgesi",self)
        self.bg6.addButton(self.answer61)
        self.bg6.addButton(self.answer62)
        self.bg6.addButton(self.answer63)
        self.bg6.addButton(self.answer64)
        self.bg6.addButton(self.answer65)

        #soru7
        self.question7 = QLabel("7-Hemşirelik mesleğini seçme nedeniniz nedir:")
        self.bg7 = QButtonGroup(self)
        self.answer71 = QRadioButton("1-Kolay iş bulma(ekonomik nedenler)",self)
        self.answer72 = QRadioButton("2-İstediğim meslek olması",self)
        self.answer73 = QRadioButton("3-Ailemin isteği",self)
        self.answer74 = QRadioButton("4-Diğer",self)
        self.bg7.addButton(self.answer71)
        self.bg7.addButton(self.answer72)
        self.bg7.addButton(self.answer73)
        self.bg7.addButton(self.answer74)

        #soru8
        self.question8 = QLabel("8-Mesleki deneyim süreniz:")
        self.bg8 = QButtonGroup(self)
        self.answer81 = QRadioButton("1- (0-2) yıl",self)
        self.answer82 = QRadioButton("2- (3-5) yıl",self)
        self.answer83 = QRadioButton("3- (6-10) yıl",self)
        self.answer84 = QRadioButton("4- 11 yıl ve üzeri",self)
        self.bg8.addButton(self.answer81)
        self.bg8.addButton(self.answer82)
        self.bg8.addButton(self.answer83)
        self.bg8.addButton(self.answer84)

        #soru9
        self.question9 = QLabel("9-Yaşadığınız deneyimler sonucu hemşirelik mesleğine bakış açınız nedir:")
        self.bg9 = QButtonGroup(self)
        self.answer91 = QRadioButton("1-Olumlu değişti",self)
        self.answer92 = QRadioButton("2-Olumsuz değişti",self)
        self.answer93 = QRadioButton("3-Değişmedi",self)
        self.bg9.addButton(self.answer91)
        self.bg9.addButton(self.answer92)
        self.bg9.addButton(self.answer93)

        #soru10
        self.question10 = QLabel("10-Yaşamınız boyunca yurt dışında bulundunuz mu:")
        self.bg10 = QButtonGroup(self)
        self.answer101 = QRadioButton("1-Evet",self)
        self.answer102 = QRadioButton("2-Hayır",self)
        self.bg10.addButton(self.answer101)
        self.bg10.addButton(self.answer102)

        #soru11
        self.question11 = QLabel("11-Farklı kültürlerden bireylere bakım verdiniz mi:")
        self.bg11 = QButtonGroup(self)
        self.answer111 = QRadioButton("1-Evet",self)
        self.answer112 = QRadioButton("2-Hayır",self)
        self.bg11.addButton(self.answer111)
        self.bg11.addButton(self.answer112)

        #soru12
        self.question12 = QLabel("12-Farklı kültürlerden bireylere bakım vermek ister misiniz:")
        self.bg12 = QButtonGroup(self)
        self.answer121 = QRadioButton("1-Evet",self)
        self.answer122 = QRadioButton("2-Hayır",self)
        self.bg12.addButton(self.answer121)
        self.bg12.addButton(self.answer122)

        #soru13
        self.question13 = QLabel("13-Yabancı dil biliyor musunuz:")
        self.bg13 = QButtonGroup(self)
        self.answer131 = QRadioButton("1-Evet",self)
        self.answer132 = QRadioButton("2-Hayır",self)
        self.bg13.addButton(self.answer131)
        self.bg13.addButton(self.answer132)

        #soru14
        self.question14 = QLabel("14-Kültür konusunda eğitim aldınız mı:")
        self.bg14 = QButtonGroup(self)
        self.answer141 = QRadioButton("1-Evet",self)
        self.answer142 = QRadioButton("2-Hayır",self)
        self.bg14.addButton(self.answer141)
        self.bg14.addButton(self.answer142)

        #soru15
        self.question15 = QLabel("15-Yurt dışında çalışmayı ister misiniz:")
        self.bg15 = QButtonGroup(self)
        self.answer151 = QRadioButton("1-Evet",self)
        self.answer152 = QRadioButton("2-Hayır",self)
        self.bg15.addButton(self.answer151)
        self.bg15.addButton(self.answer152)

        #soru16
        self.question16 = QLabel("16-Kültürlerarası hemşirelikle ilgili sempozyum, kongre, seminer gibi etkinliklere katıldınız mı:")
        self.bg16 = QButtonGroup(self)
        self.answer161 = QRadioButton("1-Evet",self)
        self.answer162 = QRadioButton("2-Hayır",self)
        self.bg16.addButton(self.answer161)
        self.bg16.addButton(self.answer162)

        #soru17
        self.question17 = QLabel("17-Farklı kültürel geçmişe sahip insanlarlaetkileşim kurarken kullandığım kültürel bilgilerin farkındayım:")
        self.bg17 = QButtonGroup(self)
        self.answer171 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer172 = QRadioButton("2-Katılmıyorum",self)
        self.answer173 = QRadioButton("3-Kararsızım",self)
        self.answer174 = QRadioButton("4-Katılıyorum",self)
        self.answer175 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg17.addButton(self.answer171)
        self.bg17.addButton(self.answer172)
        self.bg17.addButton(self.answer173)
        self.bg17.addButton(self.answer174)
        self.bg17.addButton(self.answer175)
        
        #soru18
        self.question18 = QLabel("18-Bana yabancı bir kültürden gelen insanlarla etkileşim kurarken kültürel bilgilerimi ayarlarım:")
        self.bg18 = QButtonGroup(self)
        self.answer181 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer182 = QRadioButton("2-Katılmıyorum",self)
        self.answer183 = QRadioButton("3-Kararsızım",self)
        self.answer184 = QRadioButton("4-Katılıyorum",self)
        self.answer185 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg18.addButton(self.answer181)
        self.bg18.addButton(self.answer182)
        self.bg18.addButton(self.answer183)
        self.bg18.addButton(self.answer184)
        self.bg18.addButton(self.answer185)

        #soru19
        self.question19 = QLabel("19-Kültürlerarası etkileşimlerde kullandığım kültürel bilgimin farkındayım:")
        self.bg19 = QButtonGroup(self)
        self.answer191 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer192 = QRadioButton("2-Katılmıyorum",self)
        self.answer193 = QRadioButton("3-Kararsızım",self)
        self.answer194 = QRadioButton("4-Katılıyorum",self)
        self.answer195 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg19.addButton(self.answer191)
        self.bg19.addButton(self.answer192)
        self.bg19.addButton(self.answer193)
        self.bg19.addButton(self.answer194)
        self.bg19.addButton(self.answer195)

        #soru20
        self.question20 = QLabel("20-Farklı kültürlere sahip insanlarla etkileşim halindeyken, kültürel bilgilerimin doğruluğunu kontrol ederim:")
        self.bg20 = QButtonGroup(self)
        self.answer201 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer202 = QRadioButton("2-Katılmıyorum",self)
        self.answer203 = QRadioButton("3-Kararsızım",self)
        self.answer204 = QRadioButton("4-Katılıyorum",self)
        self.answer205 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg20.addButton(self.answer201)
        self.bg20.addButton(self.answer202)
        self.bg20.addButton(self.answer203)
        self.bg20.addButton(self.answer204)
        self.bg20.addButton(self.answer205)

        #soru21
        self.question21 = QLabel("21-Diğer kültürlerin yasal ve ekonomik sistemlerini bilirim:")
        self.bg21 = QButtonGroup(self)
        self.answer211 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer212 = QRadioButton("2-Katılmıyorum",self)
        self.answer213 = QRadioButton("3-Kararsızım",self)
        self.answer214 = QRadioButton("4-Katılıyorum",self)
        self.answer215 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg21.addButton(self.answer211)
        self.bg21.addButton(self.answer212)
        self.bg21.addButton(self.answer213)
        self.bg21.addButton(self.answer214)
        self.bg21.addButton(self.answer215)

        #soru22
        self.question22 = QLabel("21-Diğer dillerin kurallarını(örneğin;kelime bilgisi,dil bilgisi) bilirim:")
        self.bg22 = QButtonGroup(self)
        self.answer221 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer222 = QRadioButton("2-Katılmıyorum",self)
        self.answer223 = QRadioButton("3-Kararsızım",self)
        self.answer224 = QRadioButton("4-Katılıyorum",self)
        self.answer225 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg22.addButton(self.answer221)
        self.bg22.addButton(self.answer222)
        self.bg22.addButton(self.answer223)
        self.bg22.addButton(self.answer224)
        self.bg22.addButton(self.answer225)

        #soru23
        self.question23 = QLabel("23-Diğer kültürlerin dini inançlarını ve kültürel değerlerini bilirim:")
        self.bg23 = QButtonGroup(self)
        self.answer231 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer232 = QRadioButton("2-Katılmıyorum",self)
        self.answer233 = QRadioButton("3-Kararsızım",self)
        self.answer234 = QRadioButton("4-Katılıyorum",self)
        self.answer235 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg23.addButton(self.answer231)
        self.bg23.addButton(self.answer232)
        self.bg23.addButton(self.answer233)
        self.bg23.addButton(self.answer234)
        self.bg23.addButton(self.answer235)

        
        #soru24
        self.question24 = QLabel("24-Diğer kültürlerin evlilik yapılarını bilirim:")
        self.bg24 = QButtonGroup(self)
        self.answer241 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer242 = QRadioButton("2-Katılmıyorum",self)
        self.answer243 = QRadioButton("3-Kararsızım",self)
        self.answer244 = QRadioButton("4-Katılıyorum",self)
        self.answer245 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg24.addButton(self.answer241)
        self.bg24.addButton(self.answer242)
        self.bg24.addButton(self.answer243)
        self.bg24.addButton(self.answer244)
        self.bg24.addButton(self.answer245)

        #soru25
        self.question25 = QLabel("25-Diğer kültürlerin sanat ve zanaatlarını bilirim:")
        self.bg25 = QButtonGroup(self)
        self.answer251 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer252 = QRadioButton("2-Katılmıyorum",self)
        self.answer253 = QRadioButton("3-Kararsızım",self)
        self.answer254 = QRadioButton("4-Katılıyorum",self)
        self.answer255 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg25.addButton(self.answer251)
        self.bg25.addButton(self.answer252)
        self.bg25.addButton(self.answer253)
        self.bg25.addButton(self.answer254)
        self.bg25.addButton(self.answer255)

        #soru26
        self.question26 = QLabel("26-Diğer kültürlerin sözel olmayan davranışları ifade etme şekillerini bilirim:")
        self.bg26 = QButtonGroup(self)
        self.answer261 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer262 = QRadioButton("2-Katılmıyorum",self)
        self.answer263 = QRadioButton("3-Kararsızım",self)
        self.answer264 = QRadioButton("4-Katılıyorum",self)
        self.answer265 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg26.addButton(self.answer261)
        self.bg26.addButton(self.answer262)
        self.bg26.addButton(self.answer263)
        self.bg26.addButton(self.answer264)
        self.bg26.addButton(self.answer265)

        #soru27
        self.question27 = QLabel("27-Farklı kültürden insanlarla etkileşim kurmaktan zevk alırım:")
        self.bg27 = QButtonGroup(self)
        self.answer271 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer272 = QRadioButton("2-Katılmıyorum",self)
        self.answer273 = QRadioButton("3-Kararsızım",self)
        self.answer274 = QRadioButton("4-Katılıyorum",self)
        self.answer275 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg27.addButton(self.answer271)
        self.bg27.addButton(self.answer272)
        self.bg27.addButton(self.answer273)
        self.bg27.addButton(self.answer274)
        self.bg27.addButton(self.answer275)

        #soru28
        self.question28 = QLabel("28-Ben yabancı bir kültürün halkı ile karşılaştığımda onlarla kaynaşabilme konusunda kendime güvenirim:")
        self.bg28 = QButtonGroup(self)
        self.answer281 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer282 = QRadioButton("2-Katılmıyorum",self)
        self.answer283 = QRadioButton("3-Kararsızım",self)
        self.answer284 = QRadioButton("4-Katılıyorum",self)
        self.answer285 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg28.addButton(self.answer281)
        self.bg28.addButton(self.answer282)
        self.bg28.addButton(self.answer283)
        self.bg28.addButton(self.answer284)
        self.bg28.addButton(self.answer285)

        #soru29
        self.question29 = QLabel("29-Yeni bir kültüre uyum sağlama sürecinde yaşayacağım stres ile başa çıkabilme konusunda kendime güvenirim:")
        self.bg29 = QButtonGroup(self)
        self.answer291 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer292 = QRadioButton("2-Katılmıyorum",self)
        self.answer293 = QRadioButton("3-Kararsızım",self)
        self.answer294 = QRadioButton("4-Katılıyorum",self)
        self.answer295 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg29.addButton(self.answer291)
        self.bg29.addButton(self.answer292)
        self.bg29.addButton(self.answer293)
        self.bg29.addButton(self.answer294)
        self.bg29.addButton(self.answer295)

        #soru30
        self.question30 = QLabel("30-Yabancısı olduğum bir kültürde yaşamaktan hoşlanırım:")
        self.bg30 = QButtonGroup(self)
        self.answer301 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer302 = QRadioButton("2-Katılmıyorum",self)
        self.answer303 = QRadioButton("3-Kararsızım",self)
        self.answer304 = QRadioButton("4-Katılıyorum",self)
        self.answer305 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg30.addButton(self.answer301)
        self.bg30.addButton(self.answer302)
        self.bg30.addButton(self.answer303)
        self.bg30.addButton(self.answer304)
        self.bg30.addButton(self.answer305)

        #soru31
        self.question31 = QLabel("31-Farklı bir kültürdeki alışveriş koşullarına alışabilme konusunda kendime güvenirim:")
        self.bg31 = QButtonGroup(self)
        self.answer311 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer312 = QRadioButton("2-Katılmıyorum",self)
        self.answer313 = QRadioButton("3-Kararsızım",self)
        self.answer314 = QRadioButton("4-Katılıyorum",self)
        self.answer315 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg31.addButton(self.answer311)
        self.bg31.addButton(self.answer312)
        self.bg31.addButton(self.answer313)
        self.bg31.addButton(self.answer314)
        self.bg31.addButton(self.answer315)

        #soru32
        self.question32 = QLabel("32-Konuşma davranışlarımı(örneğin; ses tonu, aksan vb.) kültürlerarası iletişimin gereklerine göre ayarlarım:")
        self.bg32 = QButtonGroup(self)
        self.answer321 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer322 = QRadioButton("2-Katılmıyorum",self)
        self.answer323 = QRadioButton("3-Kararsızım",self)
        self.answer324 = QRadioButton("4-Katılıyorum",self)
        self.answer325 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg32.addButton(self.answer321)
        self.bg32.addButton(self.answer322)
        self.bg32.addButton(self.answer323)
        self.bg32.addButton(self.answer324)
        self.bg32.addButton(self.answer325)

        #soru33
        self.question33 = QLabel("33-Farklı kültürlerarası durumlara uyum sağlamak duruma göre duraksar ya da sessiz kalırım:")
        self.bg33 = QButtonGroup(self)
        self.answer331 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer332 = QRadioButton("2-Katılmıyorum",self)
        self.answer333 = QRadioButton("3-Kararsızım",self)
        self.answer334 = QRadioButton("4-Katılıyorum",self)
        self.answer335 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg33.addButton(self.answer331)
        self.bg33.addButton(self.answer332)
        self.bg33.addButton(self.answer333)
        self.bg33.addButton(self.answer334)
        self.bg33.addButton(self.answer335)

        #soru34
        self.question34 = QLabel("34-Konuşma hızımı kültürlerarası etkileşimin gereklerine göre değiştirebilrim:")
        self.bg34 = QButtonGroup(self)
        self.answer341 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer342 = QRadioButton("2-Katılmıyorum",self)
        self.answer343 = QRadioButton("3-Kararsızım",self)
        self.answer344 = QRadioButton("4-Katılıyorum",self)
        self.answer345 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg34.addButton(self.answer341)
        self.bg34.addButton(self.answer342)
        self.bg34.addButton(self.answer343)
        self.bg34.addButton(self.answer344)
        self.bg34.addButton(self.answer345)

        #soru35
        self.question35 = QLabel("35-Sözel olmayan davranışlarımı kültürlerarası etkileşimin gereklerine göre değiştirebilirim:")
        self.bg35 = QButtonGroup(self)
        self.answer351 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer352 = QRadioButton("2-Katılmıyorum",self)
        self.answer353 = QRadioButton("3-Kararsızım",self)
        self.answer354 = QRadioButton("4-Katılıyorum",self)
        self.answer355 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg35.addButton(self.answer351)
        self.bg35.addButton(self.answer352)
        self.bg35.addButton(self.answer353)
        self.bg35.addButton(self.answer354)
        self.bg35.addButton(self.answer355)

        #soru36
        self.question36 = QLabel("36-Yüz ifadelerimi kültürlerarsı etkileşimin gereklerine göre değiştirebilirim:")
        self.bg36 = QButtonGroup(self)
        self.answer361 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer362 = QRadioButton("2-Katılmıyorum",self)
        self.answer363 = QRadioButton("3-Kararsızım",self)
        self.answer364 = QRadioButton("4-Katılıyorum",self)
        self.answer365 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg36.addButton(self.answer361)
        self.bg36.addButton(self.answer362)
        self.bg36.addButton(self.answer363)
        self.bg36.addButton(self.answer364)
        self.bg36.addButton(self.answer365)

        #soru37
        self.question37 = QLabel("37-Farklı kültürlerden olan insanlarla iletişimde bulunmaktan hoşlanırım:")
        self.bg37 = QButtonGroup(self)
        self.answer371 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer372 = QRadioButton("2-Katılmıyorum",self)
        self.answer373 = QRadioButton("3-Kararsızım",self)
        self.answer374 = QRadioButton("4-Katılıyorum",self)
        self.answer375 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg37.addButton(self.answer371)
        self.bg37.addButton(self.answer372)
        self.bg37.addButton(self.answer373)
        self.bg37.addButton(self.answer374)
        self.bg37.addButton(self.answer375)

        #soru38
        self.question38 = QLabel("38-Diğer görüşlerden olan insanların dar görüşlü olduğunu düşünürüm:")
        self.bg38 = QButtonGroup(self)
        self.answer381 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer382 = QRadioButton("2-Katılmıyorum",self)
        self.answer383 = QRadioButton("3-Kararsızım",self)
        self.answer384 = QRadioButton("4-Katılıyorum",self)
        self.answer385 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg38.addButton(self.answer381)
        self.bg38.addButton(self.answer382)
        self.bg38.addButton(self.answer383)
        self.bg38.addButton(self.answer384)
        self.bg38.addButton(self.answer385)

        #soru39
        self.question39 = QLabel("39-Farklı kültürlerden insanlarla iletişim kurarken kendimden oldukça eminimdir:")
        self.bg39 = QButtonGroup(self)
        self.answer391 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer392 = QRadioButton("2-Katılmıyorum",self)
        self.answer393 = QRadioButton("3-Kararsızım",self)
        self.answer394 = QRadioButton("4-Katılıyorum",self)
        self.answer395 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg39.addButton(self.answer391)
        self.bg39.addButton(self.answer392)
        self.bg39.addButton(self.answer393)
        self.bg39.addButton(self.answer394)
        self.bg39.addButton(self.answer395)

        #soru40
        self.question40 = QLabel("40-Farklı kültürlerden olan insanların karşısında konuşmakta çok zorlanırım:")
        self.bg40 = QButtonGroup(self)
        self.answer401 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer402 = QRadioButton("2-Katılmıyorum",self)
        self.answer403 = QRadioButton("3-Kararsızım",self)
        self.answer404 = QRadioButton("4-Katılıyorum",self)
        self.answer405 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg40.addButton(self.answer401)
        self.bg40.addButton(self.answer402)
        self.bg40.addButton(self.answer403)
        self.bg40.addButton(self.answer404)
        self.bg40.addButton(self.answer405)

        #soru41
        self.question41 = QLabel("41-Farklı kültürlerden olan insanlarla iletişim kurarken her zaman ne söyleyeceğimi bilirim:")
        self.bg41 = QButtonGroup(self)
        self.answer411 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer412 = QRadioButton("2-Katılmıyorum",self)
        self.answer413 = QRadioButton("3-Kararsızım",self)
        self.answer414 = QRadioButton("4-Katılıyorum",self)
        self.answer415 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg41.addButton(self.answer411)
        self.bg41.addButton(self.answer412)
        self.bg41.addButton(self.answer413)
        self.bg41.addButton(self.answer414)
        self.bg41.addButton(self.answer415)

        #soru42
        self.question42 = QLabel("42-Farklı kültürlerden olan insanlarla iletişim kurarken oldukça sosyal olabilirim:")
        self.bg42 = QButtonGroup(self)
        self.answer421 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer422 = QRadioButton("2-Katılmıyorum",self)
        self.answer423 = QRadioButton("3-Kararsızım",self)
        self.answer424 = QRadioButton("4-Katılıyorum",self)
        self.answer425 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg42.addButton(self.answer421)
        self.bg42.addButton(self.answer422)
        self.bg42.addButton(self.answer423)
        self.bg42.addButton(self.answer424)
        self.bg42.addButton(self.answer425)

        #soru43
        self.question43 = QLabel("43-Farklı kültürlerden olan insanlarla birlikte olmaktan hoşlanmam:")
        self.bg43 = QButtonGroup(self)
        self.answer431 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer432 = QRadioButton("2-Katılmıyorum",self)
        self.answer433 = QRadioButton("3-Kararsızım",self)
        self.answer434 = QRadioButton("4-Katılıyorum",self)
        self.answer435 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg43.addButton(self.answer431)
        self.bg43.addButton(self.answer432)
        self.bg43.addButton(self.answer433)
        self.bg43.addButton(self.answer434)
        self.bg43.addButton(self.answer435)

        #soru44
        self.question44 = QLabel("44-Farklı kültürlerden olan insanların değerlerine saygı duyarım:")
        self.bg44 = QButtonGroup(self)
        self.answer441 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer442 = QRadioButton("2-Katılmıyorum",self)
        self.answer443 = QRadioButton("3-Kararsızım",self)
        self.answer444 = QRadioButton("4-Katılıyorum",self)
        self.answer445 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg44.addButton(self.answer441)
        self.bg44.addButton(self.answer442)
        self.bg44.addButton(self.answer443)
        self.bg44.addButton(self.answer444)
        self.bg44.addButton(self.answer445)

        #soru45
        self.question45 = QLabel("45-Farklı kültürlerden olan insanlarla iletişim kurarken kolayca telaşlanırım:")
        self.bg45 = QButtonGroup(self)
        self.answer451 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer452 = QRadioButton("2-Katılmıyorum",self)
        self.answer453 = QRadioButton("3-Kararsızım",self)
        self.answer454 = QRadioButton("4-Katılıyorum",self)
        self.answer455 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg45.addButton(self.answer451)
        self.bg45.addButton(self.answer452)
        self.bg45.addButton(self.answer453)
        self.bg45.addButton(self.answer454)
        self.bg45.addButton(self.answer455)

        #soru46
        self.question46 = QLabel("46-Farklı kültürlerden olan insanlarla iletişim kurarken kendime güvenirim:")
        self.bg46 = QButtonGroup(self)
        self.answer461 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer462 = QRadioButton("2-Katılmıyorum",self)
        self.answer463 = QRadioButton("3-Kararsızım",self)
        self.answer464 = QRadioButton("4-Katılıyorum",self)
        self.answer465 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg46.addButton(self.answer461)
        self.bg46.addButton(self.answer462)
        self.bg46.addButton(self.answer463)
        self.bg46.addButton(self.answer464)
        self.bg46.addButton(self.answer465)

        #soru47
        self.question47 = QLabel("47-Farklı kültürdeki akranlarım hakkında bir kanıya varmadan önce beklemeyi tercih ederim:")
        self.bg47 = QButtonGroup(self)
        self.answer471 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer472 = QRadioButton("2-Katılmıyorum",self)
        self.answer473 = QRadioButton("3-Kararsızım",self)
        self.answer474 = QRadioButton("4-Katılıyorum",self)
        self.answer475 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg47.addButton(self.answer471)
        self.bg47.addButton(self.answer472)
        self.bg47.addButton(self.answer473)
        self.bg47.addButton(self.answer474)
        self.bg47.addButton(self.answer475)

        #soru48
        self.question48 = QLabel("48-Farklı kültürlerden olan insanlarla birlikteyken genellikle cesaretim kırılır:")
        self.bg48 = QButtonGroup(self)
        self.answer481 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer482 = QRadioButton("2-Katılmıyorum",self)
        self.answer483 = QRadioButton("3-Kararsızım",self)
        self.answer484 = QRadioButton("4-Katılıyorum",self)
        self.answer485 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg48.addButton(self.answer481)
        self.bg48.addButton(self.answer482)
        self.bg48.addButton(self.answer483)
        self.bg48.addButton(self.answer484)
        self.bg48.addButton(self.answer485)

        #soru49
        self.question49 = QLabel("49-Farklı kültürlerden olan insanlara karşı açık fikirliyimdir:")
        self.bg49 = QButtonGroup(self)
        self.answer491 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer492 = QRadioButton("2-Katılmıyorum",self)
        self.answer493 = QRadioButton("3-Kararsızım",self)
        self.answer494 = QRadioButton("4-Katılıyorum",self)
        self.answer495 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg49.addButton(self.answer491)
        self.bg49.addButton(self.answer492)
        self.bg49.addButton(self.answer493)
        self.bg49.addButton(self.answer494)
        self.bg49.addButton(self.answer495)

        #soru50
        self.question50 = QLabel("50-Farklı kültürlerden olan insanlarla iletişim kurarken nezaket kurallarına daha dikkat ederim:")
        self.bg50 = QButtonGroup(self)
        self.answer501 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer502 = QRadioButton("2-Katılmıyorum",self)
        self.answer503 = QRadioButton("3-Kararsızım",self)
        self.answer504 = QRadioButton("4-Katılıyorum",self)
        self.answer505 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg50.addButton(self.answer501)
        self.bg50.addButton(self.answer502)
        self.bg50.addButton(self.answer503)
        self.bg50.addButton(self.answer504)
        self.bg50.addButton(self.answer505)

        #soru51
        self.question51 = QLabel("51-Farklı kültürlerden olan insanlarla iletişim kurarken genellikle kendimi yararsız hissederim:")
        self.bg51 = QButtonGroup(self)
        self.answer511 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer512 = QRadioButton("2-Katılmıyorum",self)
        self.answer513 = QRadioButton("3-Kararsızım",self)
        self.answer514 = QRadioButton("4-Katılıyorum",self)
        self.answer515 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg51.addButton(self.answer511)
        self.bg51.addButton(self.answer512)
        self.bg51.addButton(self.answer513)
        self.bg51.addButton(self.answer514)
        self.bg51.addButton(self.answer515)

        #soru52
        self.question52 = QLabel("52-Farklı kültürlerden olan insanların davranış biçimlerine saygı duyarım:")
        self.bg52 = QButtonGroup(self)
        self.answer521 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer522 = QRadioButton("2-Katılmıyorum",self)
        self.answer523 = QRadioButton("3-Kararsızım",self)
        self.answer524 = QRadioButton("4-Katılıyorum",self)
        self.answer525 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg52.addButton(self.answer521)
        self.bg52.addButton(self.answer522)
        self.bg52.addButton(self.answer523)
        self.bg52.addButton(self.answer524)
        self.bg52.addButton(self.answer525)

        #soru53
        self.question53 = QLabel("53-Farklı kültürlerden olan insanlarla iletişim kurarken olabildiğince çok bilgi edinmeye çalışırım:")
        self.bg53 = QButtonGroup(self)
        self.answer531 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer532 = QRadioButton("2-Katılmıyorum",self)
        self.answer533 = QRadioButton("3-Kararsızım",self)
        self.answer534 = QRadioButton("4-Katılıyorum",self)
        self.answer535 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg53.addButton(self.answer531)
        self.bg53.addButton(self.answer532)
        self.bg53.addButton(self.answer533)
        self.bg53.addButton(self.answer534)
        self.bg53.addButton(self.answer535)

        #soru54
        self.question54 = QLabel("54-Farklı kültürlerden olan insanların görüşlerini kabul edemem:")
        self.bg54 = QButtonGroup(self)
        self.answer541 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer542 = QRadioButton("2-Katılmıyorum",self)
        self.answer543 = QRadioButton("3-Kararsızım",self)
        self.answer544 = QRadioButton("4-Katılıyorum",self)
        self.answer545 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg54.addButton(self.answer541)
        self.bg54.addButton(self.answer542)
        self.bg54.addButton(self.answer543)
        self.bg54.addButton(self.answer544)
        self.bg54.addButton(self.answer545)

        #soru55
        self.question55 = QLabel("55-İletişimimiz boyunca kültürel olarak farklı olan akranlarımın imalı yorumlarına karşı hassasımdır:")
        self.bg55 = QButtonGroup(self)
        self.answer551 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer552 = QRadioButton("2-Katılmıyorum",self)
        self.answer553 = QRadioButton("3-Kararsızım",self)
        self.answer554 = QRadioButton("4-Katılıyorum",self)
        self.answer555 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg55.addButton(self.answer551)
        self.bg55.addButton(self.answer552)
        self.bg55.addButton(self.answer553)
        self.bg55.addButton(self.answer554)
        self.bg55.addButton(self.answer555)

        #soru56
        self.question56 = QLabel("56-Kendi kültürümün diğer kültürlerden daha iyi olduğunu düşünürüm:")
        self.bg56 = QButtonGroup(self)
        self.answer561 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer562 = QRadioButton("2-Katılmıyorum",self)
        self.answer563 = QRadioButton("3-Kararsızım",self)
        self.answer564 = QRadioButton("4-Katılıyorum",self)
        self.answer565 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg56.addButton(self.answer561)
        self.bg56.addButton(self.answer562)
        self.bg56.addButton(self.answer563)
        self.bg56.addButton(self.answer564)
        self.bg56.addButton(self.answer565)

        #soru57
        self.question57 = QLabel("57-İletişimiz boyunca kültürel olarak farklı olan akranlarıma genellikle olumlu yaklaşırım:")
        self.bg57 = QButtonGroup(self)
        self.answer571 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer572 = QRadioButton("2-Katılmıyorum",self)
        self.answer573 = QRadioButton("3-Kararsızım",self)
        self.answer574 = QRadioButton("4-Katılıyorum",self)
        self.answer575 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg57.addButton(self.answer571)
        self.bg57.addButton(self.answer572)
        self.bg57.addButton(self.answer573)
        self.bg57.addButton(self.answer574)
        self.bg57.addButton(self.answer575)

        #soru58
        self.question58 = QLabel("58-Kültürel olarak farklı olan insanlarla uğraşmak zorunda kalacağım durumlardan kaçınırım:")
        self.bg58 = QButtonGroup(self)
        self.answer581 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer582 = QRadioButton("2-Katılmıyorum",self)
        self.answer583 = QRadioButton("3-Kararsızım",self)
        self.answer584 = QRadioButton("4-Katılıyorum",self)
        self.answer585 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg58.addButton(self.answer581)
        self.bg58.addButton(self.answer582)
        self.bg58.addButton(self.answer583)
        self.bg58.addButton(self.answer584)
        self.bg58.addButton(self.answer585)

        #soru59
        self.question59 = QLabel("59-Kültürel olarak farklı olan akranlarım akarşı anlayışımı, genellikle sözlü/sözsüz iletişim ile belli ederim:")
        self.bg59 = QButtonGroup(self)
        self.answer591 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer592 = QRadioButton("2-Katılmıyorum",self)
        self.answer593 = QRadioButton("3-Kararsızım",self)
        self.answer594 = QRadioButton("4-Katılıyorum",self)
        self.answer595 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg59.addButton(self.answer591)
        self.bg59.addButton(self.answer592)
        self.bg59.addButton(self.answer593)
        self.bg59.addButton(self.answer594)
        self.bg59.addButton(self.answer595)

        #soru60
        self.question60 = QLabel("60-Kültürel olarak farklı olan akranlarımla aramızdaki farklılıktan keyif alırım:")
        self.bg60 = QButtonGroup(self)
        self.answer601 = QRadioButton("1-Kesinlikle Katılmıyorum",self)
        self.answer602 = QRadioButton("2-Katılmıyorum",self)
        self.answer603 = QRadioButton("3-Kararsızım",self)
        self.answer604 = QRadioButton("4-Katılıyorum",self)
        self.answer605 = QRadioButton("5-Kesinlikle Katılıyorum",self)
        self.bg60.addButton(self.answer601)
        self.bg60.addButton(self.answer602)
        self.bg60.addButton(self.answer603)
        self.bg60.addButton(self.answer604)
        self.bg60.addButton(self.answer605)










        #Tamamm butonu
        self.button = QPushButton("TAMAM")
        self.button.clicked.connect(lambda : self.click(self.answer11.isChecked(),self.answer12.isChecked(),
        self.answer21,
        self.answer31.isChecked(),self.answer32.isChecked(),
        self.answer41.isChecked(),self.answer42.isChecked(),self.answer43.isChecked(),self.answer44.isChecked(),
        self.answer51.isChecked(),self.answer52.isChecked(),self.answer53.isChecked(),self.answer54.isChecked(),
        self.answer61.isChecked(),self.answer62.isChecked(),self.answer63.isChecked(),self.answer64.isChecked(),self.answer65.isChecked(),
        self.answer71.isChecked(),self.answer72.isChecked(),self.answer73.isChecked(),self.answer74.isChecked(),
        self.answer81.isChecked(),self.answer82.isChecked(),self.answer83.isChecked(),self.answer84.isChecked(),
        self.answer91.isChecked(),self.answer92.isChecked(),self.answer93.isChecked(),
        self.answer101.isChecked(),self.answer102.isChecked(),
        self.answer111.isChecked(),self.answer112.isChecked(),
        self.answer121.isChecked(),self.answer122.isChecked(),
        self.answer131.isChecked(),self.answer132.isChecked(),
        self.answer141.isChecked(),self.answer142.isChecked(),
        self.answer151.isChecked(),self.answer152.isChecked(),
        self.answer161.isChecked(),self.answer162.isChecked(),
        self.answer171.isChecked(),self.answer172.isChecked(),self.answer173.isChecked(),self.answer174.isChecked(),self.answer175.isChecked(),
        self.answer181.isChecked(),self.answer182.isChecked(),self.answer183.isChecked(),self.answer184.isChecked(),self.answer185.isChecked(),
        self.answer191.isChecked(),self.answer192.isChecked(),self.answer193.isChecked(),self.answer194.isChecked(),self.answer195.isChecked(),
        self.answer201.isChecked(),self.answer202.isChecked(),self.answer203.isChecked(),self.answer204.isChecked(),self.answer205.isChecked(),
        self.answer211.isChecked(),self.answer212.isChecked(),self.answer213.isChecked(),self.answer214.isChecked(),self.answer215.isChecked(),
        self.answer221.isChecked(),self.answer222.isChecked(),self.answer223.isChecked(),self.answer224.isChecked(),self.answer225.isChecked(),
        self.answer231.isChecked(),self.answer232.isChecked(),self.answer233.isChecked(),self.answer234.isChecked(),self.answer235.isChecked(),
        self.answer241.isChecked(),self.answer242.isChecked(),self.answer243.isChecked(),self.answer244.isChecked(),self.answer245.isChecked(),
        self.answer251.isChecked(),self.answer252.isChecked(),self.answer253.isChecked(),self.answer254.isChecked(),self.answer255.isChecked(),
        self.answer261.isChecked(),self.answer262.isChecked(),self.answer263.isChecked(),self.answer264.isChecked(),self.answer265.isChecked(),
        self.answer271.isChecked(),self.answer272.isChecked(),self.answer273.isChecked(),self.answer274.isChecked(),self.answer275.isChecked(),
        self.answer281.isChecked(),self.answer282.isChecked(),self.answer283.isChecked(),self.answer284.isChecked(),self.answer285.isChecked(),
        self.answer291.isChecked(),self.answer292.isChecked(),self.answer293.isChecked(),self.answer294.isChecked(),self.answer295.isChecked(),
        self.answer301.isChecked(),self.answer302.isChecked(),self.answer303.isChecked(),self.answer304.isChecked(),self.answer305.isChecked(),
        self.answer311.isChecked(),self.answer312.isChecked(),self.answer313.isChecked(),self.answer314.isChecked(),self.answer315.isChecked(),
        self.answer321.isChecked(),self.answer322.isChecked(),self.answer323.isChecked(),self.answer324.isChecked(),self.answer325.isChecked(),
        self.answer331.isChecked(),self.answer332.isChecked(),self.answer333.isChecked(),self.answer334.isChecked(),self.answer335.isChecked(),
        self.answer341.isChecked(),self.answer342.isChecked(),self.answer343.isChecked(),self.answer344.isChecked(),self.answer345.isChecked(),
        self.answer351.isChecked(),self.answer352.isChecked(),self.answer353.isChecked(),self.answer354.isChecked(),self.answer355.isChecked(),
        self.answer361.isChecked(),self.answer362.isChecked(),self.answer363.isChecked(),self.answer364.isChecked(),self.answer365.isChecked(),
        self.answer371.isChecked(),self.answer372.isChecked(),self.answer373.isChecked(),self.answer374.isChecked(),self.answer375.isChecked(),
        self.answer381.isChecked(),self.answer382.isChecked(),self.answer383.isChecked(),self.answer384.isChecked(),self.answer385.isChecked(),
        self.answer391.isChecked(),self.answer392.isChecked(),self.answer393.isChecked(),self.answer394.isChecked(),self.answer395.isChecked(),
        self.answer401.isChecked(),self.answer402.isChecked(),self.answer403.isChecked(),self.answer404.isChecked(),self.answer405.isChecked(),
        self.answer411.isChecked(),self.answer412.isChecked(),self.answer413.isChecked(),self.answer414.isChecked(),self.answer415.isChecked(),
        self.answer421.isChecked(),self.answer422.isChecked(),self.answer423.isChecked(),self.answer424.isChecked(),self.answer425.isChecked(),
        self.answer431.isChecked(),self.answer432.isChecked(),self.answer433.isChecked(),self.answer434.isChecked(),self.answer435.isChecked(),
        self.answer441.isChecked(),self.answer442.isChecked(),self.answer443.isChecked(),self.answer444.isChecked(),self.answer445.isChecked(),
        self.answer451.isChecked(),self.answer452.isChecked(),self.answer453.isChecked(),self.answer454.isChecked(),self.answer455.isChecked(),
        self.answer461.isChecked(),self.answer462.isChecked(),self.answer463.isChecked(),self.answer464.isChecked(),self.answer465.isChecked(),
        self.answer471.isChecked(),self.answer472.isChecked(),self.answer473.isChecked(),self.answer474.isChecked(),self.answer475.isChecked(),
        self.answer481.isChecked(),self.answer482.isChecked(),self.answer483.isChecked(),self.answer484.isChecked(),self.answer485.isChecked(),
        self.answer491.isChecked(),self.answer492.isChecked(),self.answer493.isChecked(),self.answer494.isChecked(),self.answer495.isChecked(),
        self.answer501.isChecked(),self.answer502.isChecked(),self.answer503.isChecked(),self.answer504.isChecked(),self.answer505.isChecked(),
        self.answer511.isChecked(),self.answer512.isChecked(),self.answer513.isChecked(),self.answer514.isChecked(),self.answer515.isChecked(),
        self.answer521.isChecked(),self.answer522.isChecked(),self.answer523.isChecked(),self.answer524.isChecked(),self.answer525.isChecked(),
        self.answer531.isChecked(),self.answer532.isChecked(),self.answer533.isChecked(),self.answer534.isChecked(),self.answer535.isChecked(),
        self.answer541.isChecked(),self.answer542.isChecked(),self.answer543.isChecked(),self.answer544.isChecked(),self.answer545.isChecked(),
        self.answer551.isChecked(),self.answer552.isChecked(),self.answer553.isChecked(),self.answer554.isChecked(),self.answer555.isChecked(),
        self.answer561.isChecked(),self.answer562.isChecked(),self.answer563.isChecked(),self.answer564.isChecked(),self.answer565.isChecked(),
        self.answer571.isChecked(),self.answer572.isChecked(),self.answer573.isChecked(),self.answer574.isChecked(),self.answer575.isChecked(),
        self.answer581.isChecked(),self.answer582.isChecked(),self.answer583.isChecked(),self.answer584.isChecked(),self.answer585.isChecked(),
        self.answer591.isChecked(),self.answer592.isChecked(),self.answer593.isChecked(),self.answer594.isChecked(),self.answer595.isChecked(),
        self.answer601.isChecked(),self.answer602.isChecked(),self.answer603.isChecked(),self.answer604.isChecked(),self.answer605.isChecked()))


        #▓son ayarlar
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.v_box = QVBoxLayout()

        self.v_box.addWidget(self.question1)
        self.v_box.addWidget(self.answer11)
        self.v_box.addWidget(self.answer12)
        self.v_box.addWidget(self.question2)
        self.v_box.addWidget(self.answer21)
        self.v_box.addWidget(self.question3)
        self.v_box.addWidget(self.answer31)
        self.v_box.addWidget(self.answer32)
        self.v_box.addWidget(self.question4)
        self.v_box.addWidget(self.answer41)
        self.v_box.addWidget(self.answer42)
        self.v_box.addWidget(self.answer43)
        self.v_box.addWidget(self.answer44)
        self.v_box.addWidget(self.question5)
        self.v_box.addWidget(self.answer51)
        self.v_box.addWidget(self.answer52)
        self.v_box.addWidget(self.answer53)
        self.v_box.addWidget(self.answer54)
        self.v_box.addWidget(self.question6)
        self.v_box.addWidget(self.answer61)
        self.v_box.addWidget(self.answer62)
        self.v_box.addWidget(self.answer63)
        self.v_box.addWidget(self.answer64)
        self.v_box.addWidget(self.answer65)
        self.v_box.addWidget(self.question7)
        self.v_box.addWidget(self.answer71)
        self.v_box.addWidget(self.answer72)
        self.v_box.addWidget(self.answer73)
        self.v_box.addWidget(self.answer74)
        self.v_box.addWidget(self.question8)
        self.v_box.addWidget(self.answer81)
        self.v_box.addWidget(self.answer82)
        self.v_box.addWidget(self.answer83)
        self.v_box.addWidget(self.answer84)
        self.v_box.addWidget(self.question9)
        self.v_box.addWidget(self.answer91)
        self.v_box.addWidget(self.answer92)
        self.v_box.addWidget(self.answer93)
        self.v_box.addWidget(self.question10)
        self.v_box.addWidget(self.answer101)
        self.v_box.addWidget(self.answer102)
        self.v_box.addWidget(self.question11)
        self.v_box.addWidget(self.answer111)
        self.v_box.addWidget(self.answer112)
        self.v_box.addWidget(self.question12)
        self.v_box.addWidget(self.answer121)
        self.v_box.addWidget(self.answer122)
        self.v_box.addWidget(self.question13)
        self.v_box.addWidget(self.answer131)
        self.v_box.addWidget(self.answer132)
        self.v_box.addWidget(self.question14)
        self.v_box.addWidget(self.answer141)
        self.v_box.addWidget(self.answer142)
        self.v_box.addWidget(self.question15)
        self.v_box.addWidget(self.answer151)
        self.v_box.addWidget(self.answer152)
        self.v_box.addWidget(self.question16)
        self.v_box.addWidget(self.answer161)
        self.v_box.addWidget(self.answer162)
        self.v_box.addWidget(self.question17)
        self.v_box.addWidget(self.answer171)
        self.v_box.addWidget(self.answer172)
        self.v_box.addWidget(self.answer173)
        self.v_box.addWidget(self.answer174)
        self.v_box.addWidget(self.answer175)
        self.v_box.addWidget(self.question18)
        self.v_box.addWidget(self.answer181)
        self.v_box.addWidget(self.answer182)
        self.v_box.addWidget(self.answer183)
        self.v_box.addWidget(self.answer184)
        self.v_box.addWidget(self.answer185)
        self.v_box.addWidget(self.question19)
        self.v_box.addWidget(self.answer191)
        self.v_box.addWidget(self.answer192)
        self.v_box.addWidget(self.answer193)
        self.v_box.addWidget(self.answer194)
        self.v_box.addWidget(self.answer194)
        self.v_box.addWidget(self.answer195)
        self.v_box.addWidget(self.question20)
        self.v_box.addWidget(self.answer201)
        self.v_box.addWidget(self.answer202)
        self.v_box.addWidget(self.answer203)
        self.v_box.addWidget(self.answer204)
        self.v_box.addWidget(self.answer205)
        self.v_box.addWidget(self.question21)
        self.v_box.addWidget(self.answer211)
        self.v_box.addWidget(self.answer212)
        self.v_box.addWidget(self.answer213)
        self.v_box.addWidget(self.answer214)
        self.v_box.addWidget(self.answer215)
        self.v_box.addWidget(self.question22)
        self.v_box.addWidget(self.answer221)
        self.v_box.addWidget(self.answer222)
        self.v_box.addWidget(self.answer223)
        self.v_box.addWidget(self.answer224)
        self.v_box.addWidget(self.answer225)
        self.v_box.addWidget(self.question23)
        self.v_box.addWidget(self.answer231)
        self.v_box.addWidget(self.answer232)
        self.v_box.addWidget(self.answer233)
        self.v_box.addWidget(self.answer234)
        self.v_box.addWidget(self.answer235)
        self.v_box.addWidget(self.question24)
        self.v_box.addWidget(self.answer241)
        self.v_box.addWidget(self.answer242)
        self.v_box.addWidget(self.answer243)
        self.v_box.addWidget(self.answer244)
        self.v_box.addWidget(self.answer245)
        self.v_box.addWidget(self.question25)
        self.v_box.addWidget(self.answer251)
        self.v_box.addWidget(self.answer252)
        self.v_box.addWidget(self.answer253)
        self.v_box.addWidget(self.answer254)
        self.v_box.addWidget(self.answer255)
        self.v_box.addWidget(self.question26)
        self.v_box.addWidget(self.answer261)
        self.v_box.addWidget(self.answer262)
        self.v_box.addWidget(self.answer263)
        self.v_box.addWidget(self.answer264)
        self.v_box.addWidget(self.answer265)
        self.v_box.addWidget(self.question27)
        self.v_box.addWidget(self.answer271)
        self.v_box.addWidget(self.answer272)
        self.v_box.addWidget(self.answer273)
        self.v_box.addWidget(self.answer274)
        self.v_box.addWidget(self.answer275)
        self.v_box.addWidget(self.question28)
        self.v_box.addWidget(self.answer281)
        self.v_box.addWidget(self.answer282)
        self.v_box.addWidget(self.answer283)
        self.v_box.addWidget(self.answer284)
        self.v_box.addWidget(self.answer285)
        self.v_box.addWidget(self.question29)
        self.v_box.addWidget(self.answer291)
        self.v_box.addWidget(self.answer292)
        self.v_box.addWidget(self.answer293)
        self.v_box.addWidget(self.answer294)
        self.v_box.addWidget(self.answer295)
        self.v_box.addWidget(self.question30)
        self.v_box.addWidget(self.answer301)
        self.v_box.addWidget(self.answer302)
        self.v_box.addWidget(self.answer303)
        self.v_box.addWidget(self.answer304)
        self.v_box.addWidget(self.answer305)
        self.v_box.addWidget(self.question31)
        self.v_box.addWidget(self.answer311)
        self.v_box.addWidget(self.answer312)
        self.v_box.addWidget(self.answer313)
        self.v_box.addWidget(self.answer314)
        self.v_box.addWidget(self.answer315)
        self.v_box.addWidget(self.question32)
        self.v_box.addWidget(self.answer321)
        self.v_box.addWidget(self.answer322)
        self.v_box.addWidget(self.answer323)
        self.v_box.addWidget(self.answer324)
        self.v_box.addWidget(self.answer325)
        self.v_box.addWidget(self.question33)
        self.v_box.addWidget(self.answer331)
        self.v_box.addWidget(self.answer332)
        self.v_box.addWidget(self.answer333)
        self.v_box.addWidget(self.answer334)
        self.v_box.addWidget(self.answer335)
        self.v_box.addWidget(self.question34)
        self.v_box.addWidget(self.answer341)
        self.v_box.addWidget(self.answer342)
        self.v_box.addWidget(self.answer343)
        self.v_box.addWidget(self.answer344)
        self.v_box.addWidget(self.answer345)
        self.v_box.addWidget(self.question35)
        self.v_box.addWidget(self.answer351)
        self.v_box.addWidget(self.answer352)
        self.v_box.addWidget(self.answer353)
        self.v_box.addWidget(self.answer354)
        self.v_box.addWidget(self.answer355)
        self.v_box.addWidget(self.question36)
        self.v_box.addWidget(self.answer361)
        self.v_box.addWidget(self.answer362)
        self.v_box.addWidget(self.answer363)
        self.v_box.addWidget(self.answer364)
        self.v_box.addWidget(self.answer365)
        self.v_box.addWidget(self.question37)
        self.v_box.addWidget(self.answer371)
        self.v_box.addWidget(self.answer372)
        self.v_box.addWidget(self.answer373)
        self.v_box.addWidget(self.answer374)
        self.v_box.addWidget(self.answer375)
        self.v_box.addWidget(self.question38)
        self.v_box.addWidget(self.answer381)
        self.v_box.addWidget(self.answer382)
        self.v_box.addWidget(self.answer383)
        self.v_box.addWidget(self.answer384)
        self.v_box.addWidget(self.answer385)
        self.v_box.addWidget(self.question39)
        self.v_box.addWidget(self.answer391)
        self.v_box.addWidget(self.answer392)
        self.v_box.addWidget(self.answer393)
        self.v_box.addWidget(self.answer394)
        self.v_box.addWidget(self.answer395)
        self.v_box.addWidget(self.question40)
        self.v_box.addWidget(self.answer401)
        self.v_box.addWidget(self.answer402)
        self.v_box.addWidget(self.answer403)
        self.v_box.addWidget(self.answer404)
        self.v_box.addWidget(self.answer405)
        self.v_box.addWidget(self.question41)
        self.v_box.addWidget(self.answer411)
        self.v_box.addWidget(self.answer412)
        self.v_box.addWidget(self.answer413)
        self.v_box.addWidget(self.answer414)
        self.v_box.addWidget(self.answer415)
        self.v_box.addWidget(self.question42)
        self.v_box.addWidget(self.answer421)
        self.v_box.addWidget(self.answer422)
        self.v_box.addWidget(self.answer423)
        self.v_box.addWidget(self.answer424)
        self.v_box.addWidget(self.answer425)
        self.v_box.addWidget(self.question43)
        self.v_box.addWidget(self.answer431)
        self.v_box.addWidget(self.answer432)
        self.v_box.addWidget(self.answer433)
        self.v_box.addWidget(self.answer434)
        self.v_box.addWidget(self.answer435)
        self.v_box.addWidget(self.question44)
        self.v_box.addWidget(self.answer441)
        self.v_box.addWidget(self.answer442)
        self.v_box.addWidget(self.answer443)
        self.v_box.addWidget(self.answer444)
        self.v_box.addWidget(self.answer445)
        self.v_box.addWidget(self.question45)
        self.v_box.addWidget(self.answer451)
        self.v_box.addWidget(self.answer452)
        self.v_box.addWidget(self.answer453)
        self.v_box.addWidget(self.answer454)
        self.v_box.addWidget(self.answer455)
        self.v_box.addWidget(self.question46)
        self.v_box.addWidget(self.answer461)
        self.v_box.addWidget(self.answer462)
        self.v_box.addWidget(self.answer463)
        self.v_box.addWidget(self.answer464)
        self.v_box.addWidget(self.answer465)
        self.v_box.addWidget(self.question47)
        self.v_box.addWidget(self.answer471)
        self.v_box.addWidget(self.answer472)
        self.v_box.addWidget(self.answer473)
        self.v_box.addWidget(self.answer474)
        self.v_box.addWidget(self.answer475)
        self.v_box.addWidget(self.question48)
        self.v_box.addWidget(self.answer481)
        self.v_box.addWidget(self.answer482)
        self.v_box.addWidget(self.answer483)
        self.v_box.addWidget(self.answer484)
        self.v_box.addWidget(self.answer485)
        self.v_box.addWidget(self.question49)
        self.v_box.addWidget(self.answer491)
        self.v_box.addWidget(self.answer492)
        self.v_box.addWidget(self.answer493)
        self.v_box.addWidget(self.answer494)
        self.v_box.addWidget(self.answer495)
        self.v_box.addWidget(self.question50)
        self.v_box.addWidget(self.answer501)
        self.v_box.addWidget(self.answer502)
        self.v_box.addWidget(self.answer503)
        self.v_box.addWidget(self.answer504)
        self.v_box.addWidget(self.answer505)
        self.v_box.addWidget(self.question51)
        self.v_box.addWidget(self.answer511)
        self.v_box.addWidget(self.answer512)
        self.v_box.addWidget(self.answer513)
        self.v_box.addWidget(self.answer514)
        self.v_box.addWidget(self.answer515)
        self.v_box.addWidget(self.question52)
        self.v_box.addWidget(self.answer521)
        self.v_box.addWidget(self.answer522)
        self.v_box.addWidget(self.answer523)
        self.v_box.addWidget(self.answer524)
        self.v_box.addWidget(self.answer525)
        self.v_box.addWidget(self.question53)
        self.v_box.addWidget(self.answer531)
        self.v_box.addWidget(self.answer532)
        self.v_box.addWidget(self.answer533)
        self.v_box.addWidget(self.answer534)
        self.v_box.addWidget(self.answer535)
        self.v_box.addWidget(self.question54)
        self.v_box.addWidget(self.answer541)
        self.v_box.addWidget(self.answer542)
        self.v_box.addWidget(self.answer543)
        self.v_box.addWidget(self.answer544)
        self.v_box.addWidget(self.answer545)
        self.v_box.addWidget(self.question55)
        self.v_box.addWidget(self.answer551)
        self.v_box.addWidget(self.answer552)
        self.v_box.addWidget(self.answer553)
        self.v_box.addWidget(self.answer554)
        self.v_box.addWidget(self.answer555)
        self.v_box.addWidget(self.question56)
        self.v_box.addWidget(self.answer561)
        self.v_box.addWidget(self.answer562)
        self.v_box.addWidget(self.answer563)
        self.v_box.addWidget(self.answer564)
        self.v_box.addWidget(self.answer565)
        self.v_box.addWidget(self.question57)
        self.v_box.addWidget(self.answer571)
        self.v_box.addWidget(self.answer572)
        self.v_box.addWidget(self.answer573)
        self.v_box.addWidget(self.answer574)
        self.v_box.addWidget(self.answer575)
        self.v_box.addWidget(self.question58)
        self.v_box.addWidget(self.answer581)
        self.v_box.addWidget(self.answer582)
        self.v_box.addWidget(self.answer583)
        self.v_box.addWidget(self.answer584)
        self.v_box.addWidget(self.answer585)
        self.v_box.addWidget(self.question59)
        self.v_box.addWidget(self.answer591)
        self.v_box.addWidget(self.answer592)
        self.v_box.addWidget(self.answer593)
        self.v_box.addWidget(self.answer594)
        self.v_box.addWidget(self.answer595)
        self.v_box.addWidget(self.question60)
        self.v_box.addWidget(self.answer601)
        self.v_box.addWidget(self.answer602)
        self.v_box.addWidget(self.answer603)
        self.v_box.addWidget(self.answer604)
        self.v_box.addWidget(self.answer605)






        self.v_box.addWidget(self.button)

        

        self.widget.setLayout(self.v_box)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("SPSS FORMS")
        self.show()
    
    def click(self,answer11,answer12,
    answer21,
    answer31,answer32,
    answer41,answer42,answer43,answer44,
    answer51,answer52,answer53,answer54,
    answer61,answer62,answer63,answer64,answer65,
    answer71,answer72,answer73,answer74,
    answer81,answer82,answer83,answer84,
    answer91,answer92,answer93,
    answer101,answer102,
    answer111,answer112,
    answer121,answer122,
    answer131,answer132,
    answer141,answer142,
    answer151,answer152,
    answer161,answer162,
    answer171,answer172,answer173,answer174,answer175,
    answer181,answer182,answer183,answer184,answer185,
    answer191,answer192,answer193,answer194,answer195,
    answer201,answer202,answer203,answer204,answer205,
    answer211,answer212,answer213,answer214,answer215,
    answer221,answer222,answer223,answer224,answer225,
    answer231,answer232,answer233,answer234,answer235,
    answer241,answer242,answer243,answer244,answer245,
    answer251,answer252,answer253,answer254,answer255,
    answer261,answer262,answer263,answer264,answer265,
    answer271,answer272,answer273,answer274,answer275,
    answer281,answer282,answer283,answer284,answer285,
    answer291,answer292,answer293,answer294,answer295,
    answer301,answer302,answer303,answer304,answer305,
    answer311,answer312,answer313,answer314,answer315,
    answer321,answer322,answer323,answer324,answer325,
    answer331,answer332,answer333,answer334,answer335,
    answer341,answer342,answer343,answer344,answer345,
    answer351,answer352,answer353,answer354,answer355,
    answer361,answer362,answer363,answer364,answer365,
    answer371,answer372,answer373,answer374,answer375,
    answer381,answer382,answer383,answer384,answer385,
    answer391,answer392,answer393,answer394,answer395,
    answer401,answer402,answer403,answer404,answer405,
    answer411,answer412,answer413,answer414,answer415,
    answer421,answer422,answer423,answer424,answer425,
    answer431,answer432,answer433,answer434,answer435,
    answer441,answer442,answer443,answer444,answer445,
    answer451,answer452,answer453,answer454,answer455,
    answer461,answer462,answer463,answer464,answer465,
    answer471,answer472,answer473,answer474,answer475,
    answer481,answer482,answer483,answer484,answer485,
    answer491,answer492,answer493,answer494,answer495,
    answer501,answer502,answer503,answer504,answer505,
    answer511,answer512,answer513,answer514,answer515,
    answer521,answer522,answer523,answer524,answer525,
    answer531,answer532,answer533,answer534,answer535,
    answer541,answer542,answer543,answer544,answer545,
    answer551,answer552,answer553,answer554,answer555,
    answer561,answer562,answer563,answer564,answer565,
    answer571,answer572,answer573,answer574,answer575,
    answer581,answer582,answer583,answer584,answer585,
    answer591,answer592,answer593,answer594,answer595,
    answer601,answer602,answer603,answer604,answer605):

        liste = []
        if answer11:
            liste.append(self.answer11.text()[0])
        elif answer12:
            liste.append(self.answer12.text()[0])
        
        liste.append(self.answer21.text())

        if answer31:
            liste.append(self.answer31.text()[0])
        elif answer32:
            liste.append(self.answer32.text()[0])

        if answer41:
            liste.append(self.answer41.text()[0])
        elif answer42:
            liste.append(self.answer42.text()[0])

        elif answer43:
            liste.append(self.answer43.text()[0])

        elif answer44:
            liste.append(self.answer44.text()[0])
        
        if answer51:
            liste.append(self.answer51.text()[0])
        elif answer52:
            liste.append(self.answer52.text()[0])
        elif answer53:
            liste.append(self.answer53.text()[0])
        elif answer54:
            liste.append(self.answer54.text()[0])
        
        if answer61:
            liste.append(self.answer61.text()[0])
        elif answer62:
            liste.append(self.answer62.text()[0])
        elif answer63:
            liste.append(self.answer63.text()[0])
        elif answer64:
            liste.append(self.answer64.text()[0])
        elif answer65:
            liste.append(self.answer65.text()[0])
        
        if answer71:
            liste.append(self.answer71.text()[0])
        elif answer72:
            liste.append(self.answer72.text()[0])
        elif answer73:
            liste.append(self.answer73.text()[0])
        elif answer74:
            liste.append(self.answer74.text()[0])
        
        if answer81:
            liste.append(self.answer81.text()[0])
        elif answer82:
            liste.append(self.answer82.text()[0])
        elif answer83:
            liste.append(self.answer83.text()[0])
        elif answer84:
            liste.append(self.answer84.text()[0])

        if answer91:
            liste.append(self.answer91.text()[0])
        elif answer92:
            liste.append(self.answer92.text()[0])
        elif answer93:
            liste.append(self.answer93.text()[0])
        
        if answer101:
            liste.append(self.answer101.text()[0])
        elif answer102:
            liste.append(self.answer102.text()[0])
        
        if answer111:
            liste.append(self.answer111.text()[0])
        elif answer112:
            liste.append(self.answer112.text()[0])

        if answer121:
            liste.append(self.answer121.text()[0])
        elif answer122:
            liste.append(self.answer122.text()[0])
        
        if answer131:
            liste.append(self.answer131.text()[0])
        elif answer132:
            liste.append(self.answer132.text()[0])
        
        if answer141:
            liste.append(self.answer141.text()[0])
        elif answer142:
            liste.append(self.answer142.text()[0])
        
        if answer151:
            liste.append(self.answer151.text()[0])
        elif answer152:
            liste.append(self.answer152.text()[0])
        
        if answer161:
            liste.append(self.answer161.text()[0])
        elif answer162:
            liste.append(self.answer162.text()[0])

        if answer171:
            liste.append(self.answer171.text()[0])
        elif answer172:
            liste.append(self.answer172.text()[0])
        elif answer173:
            liste.append(self.answer173.text()[0])
        elif answer174:
            liste.append(self.answer174.text()[0])
        elif answer175:
            liste.append(self.answer175.text()[0])
        
        if answer181:
            liste.append(self.answer181.text()[0])
        elif answer182:
            liste.append(self.answer182.text()[0])
        elif answer183:
            liste.append(self.answer183.text()[0])
        elif answer184:
            liste.append(self.answer184.text()[0])
        elif answer185:
            liste.append(self.answer185.text()[0])

        if answer191:
            liste.append(self.answer191.text()[0])
        elif answer192:
            liste.append(self.answer192.text()[0])
        elif answer193:
            liste.append(self.answer193.text()[0])
        elif answer194:
            liste.append(self.answer194.text()[0])
        elif answer195:
            liste.append(self.answer195.text()[0])

        if answer201:
            liste.append(self.answer201.text()[0])
        elif answer202:
            liste.append(self.answer202.text()[0])
        elif answer203:
            liste.append(self.answer203.text()[0])
        elif answer204:
            liste.append(self.answer204.text()[0])
        elif answer205:
            liste.append(self.answer205.text()[0])

        if answer211:
            liste.append(self.answer211.text()[0])
        elif answer212:
            liste.append(self.answer212.text()[0])
        elif answer213:
            liste.append(self.answer213.text()[0])
        elif answer214:
            liste.append(self.answer214.text()[0])
        elif answer215:
            liste.append(self.answer215.text()[0])

        if answer221:
            liste.append(self.answer221.text()[0])
        elif answer222:
            liste.append(self.answer222.text()[0])
        elif answer223:
            liste.append(self.answer223.text()[0])
        elif answer224:
            liste.append(self.answer224.text()[0])
        elif answer225:
            liste.append(self.answer225.text()[0])

        if answer231:
            liste.append(self.answer231.text()[0])
        elif answer232:
            liste.append(self.answer232.text()[0])
        elif answer233:
            liste.append(self.answer233.text()[0])
        elif answer234:
            liste.append(self.answer234.text()[0])
        elif answer235:
            liste.append(self.answer235.text()[0])

        if answer241:
            liste.append(self.answer241.text()[0])
        elif answer242:
            liste.append(self.answer242.text()[0])
        elif answer243:
            liste.append(self.answer243.text()[0])
        elif answer244:
            liste.append(self.answer244.text()[0])
        elif answer245:
            liste.append(self.answer245.text()[0])

        if answer251:
            liste.append(self.answer251.text()[0])
        elif answer252:
            liste.append(self.answer252.text()[0])
        elif answer253:
            liste.append(self.answer253.text()[0])
        elif answer254:
            liste.append(self.answer254.text()[0])
        elif answer255:
            liste.append(self.answer255.text()[0])

        if answer261:
            liste.append(self.answer261.text()[0])
        elif answer262:
            liste.append(self.answer262.text()[0])
        elif answer263:
            liste.append(self.answer263.text()[0])
        elif answer264:
            liste.append(self.answer264.text()[0])
        elif answer265:
            liste.append(self.answer265.text()[0])

        if answer271:
            liste.append(self.answer271.text()[0])
        elif answer272:
            liste.append(self.answer272.text()[0])
        elif answer273:
            liste.append(self.answer273.text()[0])
        elif answer274:
            liste.append(self.answer274.text()[0])
        elif answer275:
            liste.append(self.answer275.text()[0])

        if answer281:
            liste.append(self.answer281.text()[0])
        elif answer282:
            liste.append(self.answer282.text()[0])
        elif answer283:
            liste.append(self.answer283.text()[0])
        elif answer284:
            liste.append(self.answer284.text()[0])
        elif answer285:
            liste.append(self.answer285.text()[0])

        if answer291:
            liste.append(self.answer291.text()[0])
        elif answer292:
            liste.append(self.answer292.text()[0])
        elif answer293:
            liste.append(self.answer293.text()[0])
        elif answer294:
            liste.append(self.answer294.text()[0])
        elif answer295:
            liste.append(self.answer295.text()[0])

        if answer301:
            liste.append(self.answer301.text()[0])
        elif answer302:
            liste.append(self.answer302.text()[0])
        elif answer303:
            liste.append(self.answer303.text()[0])
        elif answer304:
            liste.append(self.answer304.text()[0])
        elif answer305:
            liste.append(self.answer305.text()[0])

        if answer311:
            liste.append(self.answer311.text()[0])
        elif answer312:
            liste.append(self.answer312.text()[0])
        elif answer313:
            liste.append(self.answer313.text()[0])
        elif answer314:
            liste.append(self.answer314.text()[0])
        elif answer315:
            liste.append(self.answer315.text()[0])

        if answer321:
            liste.append(self.answer321.text()[0])
        elif answer322:
            liste.append(self.answer322.text()[0])
        elif answer323:
            liste.append(self.answer323.text()[0])
        elif answer324:
            liste.append(self.answer324.text()[0])
        elif answer325:
            liste.append(self.answer325.text()[0])

        if answer331:
            liste.append(self.answer331.text()[0])
        elif answer332:
            liste.append(self.answer332.text()[0])
        elif answer333:
            liste.append(self.answer333.text()[0])
        elif answer334:
            liste.append(self.answer334.text()[0])
        elif answer335:
            liste.append(self.answer335.text()[0])

        if answer341:
            liste.append(self.answer341.text()[0])
        elif answer342:
            liste.append(self.answer342.text()[0])
        elif answer343:
            liste.append(self.answer343.text()[0])
        elif answer344:
            liste.append(self.answer344.text()[0])
        elif answer345:
            liste.append(self.answer345.text()[0])

        if answer351:
            liste.append(self.answer351.text()[0])
        elif answer352:
            liste.append(self.answer352.text()[0])
        elif answer353:
            liste.append(self.answer353.text()[0])
        elif answer354:
            liste.append(self.answer354.text()[0])
        elif answer355:
            liste.append(self.answer355.text()[0])

        if answer361:
            liste.append(self.answer361.text()[0])
        elif answer362:
            liste.append(self.answer362.text()[0])
        elif answer363:
            liste.append(self.answer363.text()[0])
        elif answer364:
            liste.append(self.answer364.text()[0])
        elif answer365:
            liste.append(self.answer365.text()[0])

        if answer371:
            liste.append(self.answer371.text()[0])
        elif answer372:
            liste.append(self.answer372.text()[0])
        elif answer373:
            liste.append(self.answer373.text()[0])
        elif answer374:
            liste.append(self.answer374.text()[0])
        elif answer375:
            liste.append(self.answer375.text()[0])

        if answer381:
            liste.append(self.answer381.text()[0])
        elif answer382:
            liste.append(self.answer382.text()[0])
        elif answer383:
            liste.append(self.answer383.text()[0])
        elif answer384:
            liste.append(self.answer384.text()[0])
        elif answer385:
            liste.append(self.answer385.text()[0])

        if answer391:
            liste.append(self.answer391.text()[0])
        elif answer392:
            liste.append(self.answer392.text()[0])
        elif answer393:
            liste.append(self.answer393.text()[0])
        elif answer394:
            liste.append(self.answer394.text()[0])
        elif answer395:
            liste.append(self.answer395.text()[0])

        if answer401:
            liste.append(self.answer401.text()[0])
        elif answer402:
            liste.append(self.answer402.text()[0])
        elif answer403:
            liste.append(self.answer403.text()[0])
        elif answer404:
            liste.append(self.answer404.text()[0])
        elif answer405:
            liste.append(self.answer405.text()[0])

        if answer411:
            liste.append(self.answer411.text()[0])
        elif answer412:
            liste.append(self.answer412.text()[0])
        elif answer413:
            liste.append(self.answer413.text()[0])
        elif answer414:
            liste.append(self.answer414.text()[0])
        elif answer415:
            liste.append(self.answer415.text()[0])

        if answer421:
            liste.append(self.answer421.text()[0])
        elif answer422:
            liste.append(self.answer422.text()[0])
        elif answer423:
            liste.append(self.answer423.text()[0])
        elif answer424:
            liste.append(self.answer424.text()[0])
        elif answer425:
            liste.append(self.answer425.text()[0])

        if answer431:
            liste.append(self.answer431.text()[0])
        elif answer432:
            liste.append(self.answer432.text()[0])
        elif answer433:
            liste.append(self.answer433.text()[0])
        elif answer434:
            liste.append(self.answer434.text()[0])
        elif answer435:
            liste.append(self.answer435.text()[0])

        if answer441:
            liste.append(self.answer441.text()[0])
        elif answer442:
            liste.append(self.answer442.text()[0])
        elif answer443:
            liste.append(self.answer443.text()[0])
        elif answer444:
            liste.append(self.answer444.text()[0])
        elif answer445:
            liste.append(self.answer445.text()[0])

        if answer451:
            liste.append(self.answer451.text()[0])
        elif answer452:
            liste.append(self.answer452.text()[0])
        elif answer453:
            liste.append(self.answer453.text()[0])
        elif answer454:
            liste.append(self.answer454.text()[0])
        elif answer455:
            liste.append(self.answer455.text()[0])

        if answer461:
            liste.append(self.answer461.text()[0])
        elif answer462:
            liste.append(self.answer462.text()[0])
        elif answer463:
            liste.append(self.answer463.text()[0])
        elif answer464:
            liste.append(self.answer464.text()[0])
        elif answer465:
            liste.append(self.answer465.text()[0])

        if answer471:
            liste.append(self.answer471.text()[0])
        elif answer472:
            liste.append(self.answer472.text()[0])
        elif answer473:
            liste.append(self.answer473.text()[0])
        elif answer474:
            liste.append(self.answer474.text()[0])
        elif answer475:
            liste.append(self.answer475.text()[0])

        if answer481:
            liste.append(self.answer481.text()[0])
        elif answer482:
            liste.append(self.answer482.text()[0])
        elif answer483:
            liste.append(self.answer483.text()[0])
        elif answer484:
            liste.append(self.answer484.text()[0])
        elif answer485:
            liste.append(self.answer485.text()[0])

        if answer491:
            liste.append(self.answer491.text()[0])
        elif answer492:
            liste.append(self.answer492.text()[0])
        elif answer493:
            liste.append(self.answer493.text()[0])
        elif answer494:
            liste.append(self.answer494.text()[0])
        elif answer495:
            liste.append(self.answer495.text()[0])

        if answer501:
            liste.append(self.answer501.text()[0])
        elif answer502:
            liste.append(self.answer502.text()[0])
        elif answer503:
            liste.append(self.answer503.text()[0])
        elif answer504:
            liste.append(self.answer504.text()[0])
        elif answer505:
            liste.append(self.answer505.text()[0])

        if answer511:
            liste.append(self.answer511.text()[0])
        elif answer512:
            liste.append(self.answer512.text()[0])
        elif answer513:
            liste.append(self.answer513.text()[0])
        elif answer514:
            liste.append(self.answer514.text()[0])
        elif answer515:
            liste.append(self.answer515.text()[0])

        if answer521:
            liste.append(self.answer521.text()[0])
        elif answer522:
            liste.append(self.answer522.text()[0])
        elif answer523:
            liste.append(self.answer523.text()[0])
        elif answer524:
            liste.append(self.answer524.text()[0])
        elif answer525:
            liste.append(self.answer525.text()[0])

        if answer531:
            liste.append(self.answer531.text()[0])
        elif answer532:
            liste.append(self.answer532.text()[0])
        elif answer533:
            liste.append(self.answer533.text()[0])
        elif answer534:
            liste.append(self.answer534.text()[0])
        elif answer535:
            liste.append(self.answer535.text()[0])

        if answer541:
            liste.append(self.answer541.text()[0])
        elif answer542:
            liste.append(self.answer542.text()[0])
        elif answer543:
            liste.append(self.answer543.text()[0])
        elif answer544:
            liste.append(self.answer544.text()[0])
        elif answer545:
            liste.append(self.answer545.text()[0])

        if answer551:
            liste.append(self.answer551.text()[0])
        elif answer552:
            liste.append(self.answer552.text()[0])
        elif answer553:
            liste.append(self.answer553.text()[0])
        elif answer554:
            liste.append(self.answer554.text()[0])
        elif answer555:
            liste.append(self.answer555.text()[0])

        if answer561:
            liste.append(self.answer561.text()[0])
        elif answer562:
            liste.append(self.answer562.text()[0])
        elif answer563:
            liste.append(self.answer563.text()[0])
        elif answer564:
            liste.append(self.answer564.text()[0])
        elif answer565:
            liste.append(self.answer565.text()[0])

        if answer571:
            liste.append(self.answer571.text()[0])
        elif answer572:
            liste.append(self.answer572.text()[0])
        elif answer573:
            liste.append(self.answer573.text()[0])
        elif answer574:
            liste.append(self.answer574.text()[0])
        elif answer575:
            liste.append(self.answer575.text()[0])

        if answer581:
            liste.append(self.answer581.text()[0])
        elif answer582:
            liste.append(self.answer582.text()[0])
        elif answer583:
            liste.append(self.answer583.text()[0])
        elif answer584:
            liste.append(self.answer584.text()[0])
        elif answer585:
            liste.append(self.answer585.text()[0])

        if answer591:
            liste.append(self.answer591.text()[0])
        elif answer592:
            liste.append(self.answer592.text()[0])
        elif answer593:
            liste.append(self.answer593.text()[0])
        elif answer594:
            liste.append(self.answer594.text()[0])
        elif answer595:
            liste.append(self.answer595.text()[0])

        if answer601:
            liste.append(self.answer601.text()[0])
        elif answer602:
            liste.append(self.answer602.text()[0])
        elif answer603:
            liste.append(self.answer603.text()[0])
        elif answer604:
            liste.append(self.answer604.text()[0])
        elif answer605:
            liste.append(self.answer605.text()[0])
        
        print(liste)
        spss_func.write_spss_data(liste)
        os.system("python C:/Users/m-dur/OneDrive/Masaüstü/spss_form/spss/spss_son_hal.py")
        sys.exit()

        QCoreApplication.instance().quit()


        


def main():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
