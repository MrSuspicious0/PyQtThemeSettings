# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_settingswindow.ui'
##
# Created by: Qt User Interface Compiler version 6.4.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout, QLabel,
                               QPushButton, QVBoxLayout)


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.setWindowModality(Qt.ApplicationModal)
        SettingsWindow.resize(239, 126)
        SettingsWindow.setMinimumSize(QSize(239, 126))
        SettingsWindow.setMaximumSize(QSize(239, 126))
        self.gridLayout = QGridLayout(SettingsWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblDesc_Theme = QLabel(SettingsWindow)
        self.lblDesc_Theme.setObjectName(u"lblDesc_Theme")

        self.horizontalLayout.addWidget(self.lblDesc_Theme)

        self.comboxTheme = QComboBox(SettingsWindow)
        self.comboxTheme.setObjectName(u"comboxTheme")

        self.horizontalLayout.addWidget(self.comboxTheme)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblDesc_Accent = QLabel(SettingsWindow)
        self.lblDesc_Accent.setObjectName(u"lblDesc_Accent")

        self.verticalLayout.addWidget(self.lblDesc_Accent)

        self.lblColourPreview = QLabel(SettingsWindow)
        self.lblColourPreview.setObjectName(u"lblColourPreview")

        self.verticalLayout.addWidget(self.lblColourPreview)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btnChangeAccent = QPushButton(SettingsWindow)
        self.btnChangeAccent.setObjectName(u"btnChangeAccent")

        self.verticalLayout_2.addWidget(self.btnChangeAccent)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnApply = QPushButton(SettingsWindow)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_3.addWidget(self.btnApply)

        self.btnCancel = QPushButton(SettingsWindow)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_3.addWidget(self.btnCancel)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate(
            "SettingsWindow", u"Settings", None))
        self.lblDesc_Theme.setText(QCoreApplication.translate(
            "SettingsWindow", u"Theme", None))
        self.lblDesc_Accent.setText(QCoreApplication.translate(
            "SettingsWindow", u"   Accent Colour   ", None))
        self.lblColourPreview.setText("")
        self.btnChangeAccent.setText(QCoreApplication.translate(
            "SettingsWindow", u"Change Accent Colour", None))
        self.btnApply.setText(QCoreApplication.translate(
            "SettingsWindow", u"Apply", None))
        self.btnCancel.setText(QCoreApplication.translate(
            "SettingsWindow", u"Cancel", None))
    # retranslateUi
