# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_GUI_main(object):
    def setupUi(self, GUI_main):
        if not GUI_main.objectName():
            GUI_main.setObjectName(u"GUI_main")
        GUI_main.resize(800, 500)
        GUI_main.setStyleSheet(u"E:/others/others/GUI/GUIimage/BackGround.jpg")
        self.label = QLabel(GUI_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 221, 101))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"E:/others/others/GUI/GUIimage/logo.jpg"))
        self.label.setScaledContents(True)
        self.pushButton = QPushButton(GUI_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 150, 131, 51))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-image: url(E:/others/others/GUI/GUIimage/Start.png);\n"
"background-color: transparent;")
        self.pushButton_2 = QPushButton(GUI_main)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 230, 131, 51))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-image: url(E:/others/others/GUI/GUIimage/Login.png);\n"
"background-color: transparent;")
        self.pushButton_3 = QPushButton(GUI_main)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 320, 131, 51))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border-image: url(E:/others/others/GUI/GUIimage/Exit.png);\n"
"background-color: transparent;")

        self.retranslateUi(GUI_main)

        QMetaObject.connectSlotsByName(GUI_main)
    # setupUi

    def retranslateUi(self, GUI_main):
        GUI_main.setWindowTitle(QCoreApplication.translate("GUI_main", u"GUI_main", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

