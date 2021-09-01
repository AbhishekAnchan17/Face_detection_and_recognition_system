# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage , QPixmap
import cv2 as cv
import os
from PyQt5.QtWidgets import QMessageBox
class Ui_Form1(object):
    def Save(self):
        try:
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv.CascadeClassifier(cascPath)
            cap = cv.VideoCapture(0)
            if not cap.isOpened():
                QMessageBox.warning(QMessageBox(), 'Error', 'Cannot Open Camera')
                exit()
            while True:
                ret, frame = cap.read()
                imgS = cv.cvtColor(frame, cv.IMREAD_ANYCOLOR)
                faces = faceCascade.detectMultiScale(imgS,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),)
                for (x, y, w, h) in faces:
                    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                qformat = QtGui.QImage.Format_Indexed8
                img = QImage(frame,frame.shape[1],frame.shape[0],qformat)
                self.imgLabel.setPixmap(QPixmap.fromImage(img))
                self.displayImage(frame,1)
                if cv.waitKey(1) == ord('q'):
                    break
            cap.release()
            cv.destroyAllWindows()
        except Exception:
            pass
            #QMessageBox.information(QMessageBox(), 'Info', 'Image Saved')
    
    def capture(self):
        try:
            cap = cv.VideoCapture(0)
            ret, frame = cap.read()
            save=self.lineEdit.text()
            if len(save)==0 or save.isdigit():
                QMessageBox.information(QMessageBox(), 'Error', 'Please give a valid name')
                
            else:
                filename="D:/pjt/training_images"
                cv.imwrite(os.path.join(filename,str(save)+".jpg"),frame)
                QMessageBox.information(QMessageBox(), 'Saved', ' Image Registered.')
                QMessageBox.information(QMessageBox(), 'Welcome', 'Welcome!  {} you are a authorised user now.'.format(save))
                cap.release()
        except Exception:
            pass
            #QMessageBox.information(QMessageBox(), 'Saved', ' Image saved.')

    def displayImage(self,img,window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 636)
        self.imgLabel = QtWidgets.QLabel(Form)
        self.imgLabel.setGeometry(QtCore.QRect(110, 50, 381, 391))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 560, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 560, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 560, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 490, 131, 20))
        self.label.setObjectName("label")
        self.Label1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label1.setFont(font)
        self.Label1.setLineWidth(1)
        self.Label1.setTextFormat(QtCore.Qt.AutoText)
        self.Label1.setObjectName("Label1")
        self.Label1.setGeometry(QtCore.QRect(170,6,520,40))
        self.Label1.setObjectName("Label1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 490, 201, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.Save)
        self.pushButton_3.clicked.connect(self.capture)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Face Register"))
        self.Label1.setText(_translate("Form", "REGISTRATION SYSTEM"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.pushButton_2.setText(_translate("Form", "Register"))
        self.pushButton_3.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "ENTER YOUR NAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
