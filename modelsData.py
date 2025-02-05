from PySide6.QtCore import QSize
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import (QSize, QTime, QUrl, Qt)
from PySide6.QtCore import Signal


class dataAppPass(QLabel):
    clicked = Signal()

    def __init__(self, id_, nomAppOrSite, username):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.nomAppOrSite = nomAppOrSite
        self.setText(f"{self.nomAppOrSite}, {username}")
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))
        self.setStyleSheet(u"QLabel{\n"
                           "    color: #ffffff; /* Couleur des labels */\n"
                           "    font-size: 14px;\n"
                           "    font-weight: bold;\n"
                           "}\n")

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class dataNotePass(QLabel):
    clicked = Signal()

    def __init__(self, id_, noteText):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.noteText = noteText
        self.setText(self.noteText)
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))
        self.setStyleSheet(u"QLabel{\n"
                           "    color: #ffffff; /* Couleur des labels */\n"
                           "    font-size: 14px;\n"
                           "    font-weight: bold;\n"
                           "}\n")

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class dataCB(QLabel):
    clicked = Signal()

    def __init__(self, id_, numCB, cbTitulaire):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.id_ = id_
        self.cbTitulaire = cbTitulaire
        self.numCB = numCB
        self.setText(f'carte n°: {self.numCB},   {self.cbTitulaire}' )
        self.setStyleSheet(u"QLabel {\n"
                            "    color: #ffffff; /* Couleur des labels */\n"
                            "    font-size: 14px;\n"
                            "    font-weight: bold;\n"
                            "}\n")
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(16777215, 80))

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)