# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/xml/sort.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sort(object):
    def setupUi(self, Sort):
        Sort.setObjectName("Sort")
        Sort.resize(400, 300)

        self.retranslateUi(Sort)
        QtCore.QMetaObject.connectSlotsByName(Sort)

    def retranslateUi(self, Sort):
        _translate = QtCore.QCoreApplication.translate
        Sort.setWindowTitle(_translate("Sort", "Параметры сортировки"))