from PyQt5 import QtWidgets
import sys

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):

        


        self.radio_yazi = QtWidgets.QLabel("Hangi dili daha çok seviyorsunuz")
        self.java = QtWidgets.QRadioButton("Java")
        self.python = QtWidgets.QRadioButton("Python")
        self.php = QtWidgets.QRadioButton("PHP")
        self.text_area = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("Gönder")
        self.button.clicked.connect(lambda: self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.text_area))

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle('RadioButton')

        self.show()
    
    def click(self,python,java,php,text_area):
        if python:
            self.text_area.setText("python")
        elif java:
            self.text_area.setText("java")
        elif php:
            self.text_area.setText("php")




app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()


sys.exit(app.exec_())



