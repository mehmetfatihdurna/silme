import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Spss Survey")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Yazı Yazayrom")
    button = QtWidgets.QPushButton(pencere)
    button.setText("Button")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(button)
    h_box.addWidget(etiket1)
    h_box.addStretch()
    pencere.setLayout(h_box)
    pencere.setGeometry(100,100,620,872)
    pencere.show()
    sys.exit(app.exec_())

Pencere()