# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/xml/add_person.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 404)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setWhatsThis("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 331, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 80, 201, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 201, 22))
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 201, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 200, 331, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.birth_date = QtWidgets.QDateEdit(self.groupBox_3)
        self.birth_date.setGeometry(QtCore.QRect(10, 70, 110, 22))
        self.birth_date.setObjectName("birth_date")
        self.dead_date = QtWidgets.QDateEdit(self.groupBox_3)
        self.dead_date.setGeometry(QtCore.QRect(210, 70, 110, 22))
        self.dead_date.setObjectName("dead_date")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(210, 20, 121, 41))
        self.radioButton.setObjectName("radioButton")
        self.birth_day_label = QtWidgets.QLabel(self.groupBox_3)
        self.birth_day_label.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.birth_day_label.setObjectName("birth_day_label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 140, 331, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(120, 20, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление человека"))
        self.groupBox.setTitle(_translate("Form", "Основная информация"))
        self.groupBox_2.setTitle(_translate("Form", "ФИО"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Отчество"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Фамилия"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Имя"))
        self.groupBox_3.setTitle(_translate("Form", "Даты"))
        self.radioButton.setText(_translate("Form", "Дата смерти"))
        self.birth_day_label.setText(_translate("Form", "Дата рождения"))
        self.groupBox_4.setTitle(_translate("Form", "Пол"))
        self.radioButton_2.setText(_translate("Form", "Мужской"))
        self.radioButton_3.setText(_translate("Form", "Женский"))