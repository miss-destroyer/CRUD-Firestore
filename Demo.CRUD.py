import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from PyQt5 import QtCore, QtGui, QtWidgets

cred = credentials.Certificate(r"C:\Users\hp\Desktop\New project\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(810, 575)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 571))
        self.label.setMouseTracking(True)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 311, 31))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 87 20pt \"Segoe UI Black\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 111, 21))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 81, 31))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 270, 111, 21))
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 340, 71, 21))
        self.label_6.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 87 16pt \"Segoe UI Black\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 400, 81, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"font: 16pt \"Javanese Text\";\n"
"border-radius:8px;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(160, 240, 240)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 400, 81, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"font: 16pt \"Javanese Text\";\n"
"border-radius:8px;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(160, 240, 240)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 400, 81, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"font: 16pt \"Javanese Text\";\n"
"border-radius:8px;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(160, 240, 240)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 400, 81, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"font: 16pt \"Javanese Text\";\n"
"border-radius:8px;\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:rgb(160, 240, 240)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(250, 110, 371, 41))
        self.lineEdit.setStyleSheet("color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 320, 371, 41))
        self.lineEdit_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 250, 371, 41))
        self.lineEdit_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(250, 180, 371, 41))
        self.spinBox.setStyleSheet("color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setObjectName("spinBox")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(180, 480, 461, 31))
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell\";")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.read)
        self.pushButton_4.clicked.connect(self.delete)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Demo CRUD Operation"))
        self.label_3.setText(_translate("Form", "Full Name"))
        self.label_4.setText(_translate("Form", "Age"))
        self.label_5.setText(_translate("Form", "Phone No."))
        self.label_6.setText(_translate("Form", "Email"))
        self.pushButton.setText(_translate("Form", "Create"))
        self.pushButton_2.setText(_translate("Form", "Update"))
        self.pushButton_3.setText(_translate("Form", "Read"))
        self.pushButton_4.setText(_translate("Form", "Delete"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Enter Your Name ..."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Your Email Address ..."))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Enter Your Phone Number ..."))

    def create(self):
        name = self.lineEdit.text()
        age = self.spinBox.value()
        phone = self.lineEdit_3.text()
        email = self.lineEdit_2.text()
        data = {
            'name': name,
            'age': age,
            'phone': phone,
            'email': email
        }
        doc_ref = db.collection('user').document()
        doc_ref.set(data)
        self.label_7.setText("Successfully Created. Your ID is : " + doc_ref.id)


    def read(self):
        doc_id, ok = QtWidgets.QInputDialog.getText(None, 'Read Document', 'Enter Your ID:')
        if ok and doc_id:
            doc_ref = db.collection('user').document(doc_id)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                QtWidgets.QMessageBox.information(None, 'Document Data', str(data))
            else:
                QtWidgets.QMessageBox.warning(None, 'Error', 'This ID not found')

    def update(self):
        doc_id, ok = QtWidgets.QInputDialog.getText(None, 'Update Document', 'Enter Your ID:')
        if ok and doc_id:
            name = self.lineEdit.text()
            age = self.spinBox.value()
            phone = self.lineEdit_3.text()
            email = self.lineEdit_2.text()
            data = {
                'name': name,
                'age': age,
                'phone': phone,
                'email': email
            }
            doc_ref = db.collection('user').document(doc_id)
            doc_ref.update(data)
            QtWidgets.QMessageBox.information(None, 'Success', 'Your Document updated')

    def delete(self):
        doc_id, ok = QtWidgets.QInputDialog.getText(None, 'Delete Document', 'Enter Your ID:')
        if ok and doc_id:
            doc_ref = db.collection('user').document(doc_id)
            doc_ref.delete()
            QtWidgets.QMessageBox.information(None, 'Success', 'Ypur Document deleted')  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
