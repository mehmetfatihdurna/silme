import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QWaitCondition

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):

        #soru1
        self.question1 = QtWidgets.QLabel("1-Cinsiyetiniz:")
        self.bg1 = QtWidgets.QButtonGroup()
        self.answer11 = QtWidgets.QRadioButton("1-Kadın")
        self.answer12 = QtWidgets.QRadioButton("2-Erkek")
        self.bg1.addButton(self.answer11)
        self.bg1.addButton(self.answer12)
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addStretch()
        v_box1.addWidget(self.question1)
        v_box1.addWidget(self.answer11)
        v_box1.addWidget(self.answer12)
        v_box1.addStretch()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addLayout(v_box1)
        h_box1.addStretch()

        #soru2
        self.question2 = QtWidgets.QLabel("2-Yaşınız:")
        self.answer21 = QtWidgets.QLineEdit()
        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addStretch()
        v_box2.addWidget(self.question2)
        v_box2.addWidget(self.answer21)
        v_box2.addStretch()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addLayout(v_box2)
        h_box2.addStretch()

        #soru3
        self.question3 = QtWidgets.QLabel("3-Medeni Durumunuz:")
        self.bg3 = QtWidgets.QButtonGroup(self)
        self.answer31 = QtWidgets.QRadioButton("1-Evli",self)
        self.answer32 = QtWidgets.QRadioButton("2-Bekar",self)
        self.bg3.addButton(self.answer31)
        self.bg3.addButton(self.answer32)
        v_box3 = QtWidgets.QVBoxLayout()
        v_box3.addStretch()
        v_box3.addWidget(self.question3)
        v_box3.addWidget(self.answer31)
        v_box3.addWidget(self.answer32)
        v_box3.addStretch()
        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addLayout(v_box3)
        h_box3.addStretch()


        #soru4
        self.question4 = QtWidgets.QLabel("4-Mezuniyet durumunuz:")
        self.bg4 = QtWidgets.QButtonGroup(self)
        self.answer41 = QtWidgets.QRadioButton("1-Ortaöğğretim",self)
        self.answer42 = QtWidgets.QRadioButton("2-Ön Lisans",self)
        self.answer43 = QtWidgets.QRadioButton("3-Lisans",self)
        self.answer44 = QtWidgets.QRadioButton("4-Lisansüstü",self)
        self.bg4.addButton(self.answer41)
        self.bg4.addButton(self.answer42)
        self.bg4.addButton(self.answer43)
        self.bg4.addButton(self.answer44)
        v_box4 = QtWidgets.QVBoxLayout()
        v_box4.addStretch()
        v_box4.addWidget(self.question4)
        v_box4.addWidget(self.answer41)
        v_box4.addWidget(self.answer42)
        v_box4.addWidget(self.answer43)
        v_box4.addWidget(self.answer44)
        v_box4.addStretch()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addLayout(v_box4)
        h_box4.addStretch()



        #soru5
        self.question5 = QtWidgets.QLabel("5-Uzun süredir yaşadığınız yer:")
        self.bg5 = QtWidgets.QButtonGroup(self)
        self.answer51 = QtWidgets.QRadioButton("1-Köy-kasaba",self)
        self.answer52 = QtWidgets.QRadioButton("2-İlçe",self)
        self.answer53 = QtWidgets.QRadioButton("3-İl",self)
        self.answer54 = QtWidgets.QRadioButton("4-Yurtdışı",self)
        self.bg5.addButton(self.answer51)
        self.bg5.addButton(self.answer52)
        self.bg5.addButton(self.answer53)
        self.bg5.addButton(self.answer54)
        v_box5 = QtWidgets.QVBoxLayout()
        v_box5.addStretch()
        v_box5.addWidget(self.question5)
        v_box5.addWidget(self.answer51)
        v_box5.addWidget(self.answer52)
        v_box5.addWidget(self.answer53)
        v_box5.addWidget(self.answer54)
        v_box5.addStretch()
        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addLayout(v_box5)
        h_box5.addStretch()



        #soru6
        self.question6 = QtWidgets.QLabel("5-Uzun süredir yaşadığınız yer:")
        self.bg6 = QtWidgets.QButtonGroup(self)
        self.answer61 = QtWidgets.QRadioButton("1-Karadeniz Bölgesi",self)
        self.answer62 = QtWidgets.QRadioButton("2-İç Anadolu Bölgesi",self)
        self.answer63 = QtWidgets.QRadioButton("3-Ege-Marmara Bölgesi",self)
        self.answer64 = QtWidgets.QRadioButton("4-Akdeniz Bölgesi",self)
        self.answer65 = QtWidgets.QRadioButton("5-Doğu Anadolu-Güneydoğu Anadolu Bölgesi",self)
        self.bg6.addButton(self.answer61)
        self.bg6.addButton(self.answer62)
        self.bg6.addButton(self.answer63)
        self.bg6.addButton(self.answer64)
        self.bg6.addButton(self.answer65)
        v_box6 = QtWidgets.QVBoxLayout()
        v_box6.addStretch()
        v_box6.addWidget(self.question6)
        v_box6.addWidget(self.answer61)
        v_box6.addWidget(self.answer62)
        v_box6.addWidget(self.answer63)
        v_box6.addWidget(self.answer64)
        v_box6.addStretch()
        h_box6 = QtWidgets.QHBoxLayout()
        h_box6.addStretch()
        h_box6.addLayout(v_box6)
        h_box6.addStretch()



        #Tamamm butonu
        self.button = QtWidgets.QPushButton("TAMAM")
        self.button.clicked.connect(lambda : self.click(self.answer11.isChecked(),self.answer12.isChecked(),self.answer21,self.answer31.isChecked(),self.answer32.isChecked()))
        buttonlayout = QtWidgets.QHBoxLayout()
        buttonlayout.addStretch()
        buttonlayout.addWidget(self.button)
        buttonlayout.addStretch()




        #▓son ayarlar
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box6)

        v_box.addLayout(buttonlayout)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("SPSS FORMS")
        self.show()
    
    def click(self,answer11,answer12,answer21,answer31,answer32):
        if answer11:
            print(self.answer11.text())
        elif answer12:
            print(self.answer12.text())
        
        print(self.answer21.text())

        if answer31:
            print(self.answer31.text())
        elif answer32:
            print(self.answer32.text())

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())