# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/xml/full_person_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Full_Person_Info_Form(object):
    def setupUi(self, Full_Person_Info_Form):
        Full_Person_Info_Form.setObjectName("Full_Person_Info_Form")
        Full_Person_Info_Form.resize(926, 689)
        self.tabWidget = QtWidgets.QTabWidget(Full_Person_Info_Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 881, 71))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.perso_name_label_2 = QtWidgets.QLabel(self.tab_1)
        self.perso_name_label_2.setGeometry(QtCore.QRect(10, 0, 371, 41))
        self.perso_name_label_2.setObjectName("perso_name_label_2")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.perso_name_label = QtWidgets.QLabel(Full_Person_Info_Form)
        self.perso_name_label.setGeometry(QtCore.QRect(20, 30, 371, 41))
        self.perso_name_label.setObjectName("perso_name_label")
        self.update_rb = QtWidgets.QRadioButton(Full_Person_Info_Form)
        self.update_rb.setGeometry(QtCore.QRect(750, 50, 131, 20))
        self.update_rb.setObjectName("update_rb")
        self.pushButton_2 = QtWidgets.QPushButton(Full_Person_Info_Form)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 640, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Full_Person_Info_Form)
        self.pushButton.setGeometry(QtCore.QRect(680, 640, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Full_Person_Info_Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 851, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Full_Person_Info_Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Full_Person_Info_Form)

    def retranslateUi(self, Full_Person_Info_Form):
        _translate = QtCore.QCoreApplication.translate
        Full_Person_Info_Form.setWindowTitle(_translate("Full_Person_Info_Form", "Form"))
        self.perso_name_label_2.setText(_translate("Full_Person_Info_Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Full_Person_Info_Form", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Full_Person_Info_Form", "Страница"))
        self.perso_name_label.setText(_translate("Full_Person_Info_Form", "TextLabel"))
        self.update_rb.setText(_translate("Full_Person_Info_Form", "Изменять данные"))
        self.pushButton_2.setText(_translate("Full_Person_Info_Form", "Обновить"))
        self.pushButton.setText(_translate("Full_Person_Info_Form", "Сохранить"))