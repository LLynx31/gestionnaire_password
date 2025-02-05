from functools import partial

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QPlainTextEdit, QDialog, QPushButton, QLabel,
                               QVBoxLayout, QHBoxLayout, QSpacerItem)
from mixbox.idgen import set_id_method

from cb import ajouterCarteBancaire, lireCarteBancaires, lireCarteBancaire, mettreAJourCarteBancaire, \
    supprimerCarteBancaire
from compte import *
from modelsData import *
from notes import *
from utilisateur import *
import secrets
import string


def clearLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clearLayout(item.layout())

def generer_mot_de_passe(longueur=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(secrets.choice(alphabet) for _ in range(longueur))
    return mot_de_passe

class Ui_DialogAjoutApp(QDialog):

    def __init__(self,vbox,id_):
        super().__init__()
        self.vbox = vbox
        self.setupUi(id_)
        self.exec()

    def setupUi(self,id_):
        self.resize(558, 386)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.id_ = id_

        self.labelTitreApp = QLabel(self)
        self.labelTitreApp.setObjectName(u"labelTitreApp")
        self.labelTitreApp.setGeometry(QRect(190, 20, 171, 19))

        self.labelNomApp = QLabel(self)
        self.labelNomApp.setObjectName(u"labelNomApp")
        self.labelNomApp.setGeometry(QRect(50, 70, 171, 19))

        self.lineEditNomApp = QLineEdit(self)
        self.lineEditNomApp.setObjectName(u"lineEditNomApp")
        self.lineEditNomApp.setGeometry(QRect(50, 100, 441, 40))

        self.labelUsernameApp = QLabel(self)
        self.labelUsernameApp.setObjectName(u"labelPassApp")
        self.labelUsernameApp.setGeometry(QRect(50, 150, 151, 19))
        self.labelUsernameApp.setText("Nom d'utilisateur")

        self.lineEditUsernameApp = QLineEdit(self)
        self.lineEditUsernameApp.setObjectName(u"lineEditPassApp")
        self.lineEditUsernameApp.setGeometry(QRect(50, 180, 441, 40))

        self.labelPassApp = QLabel(self)
        self.labelPassApp.setObjectName(u"labelPassApp")
        self.labelPassApp.setGeometry(QRect(50, 230, 151, 19))

        self.lineEditPassApp = QLineEdit(self)
        self.lineEditPassApp.setObjectName(u"lineEditPassApp")
        self.lineEditPassApp.setGeometry(QRect(50, 260, 441, 40))

        self.pushButtonAjoutApp = QPushButton(self)
        self.pushButtonAjoutApp.setObjectName(u"pushButtonAjoutApp")
        self.pushButtonAjoutApp.setGeometry(QRect(190, 320, 151, 41))
        self.pushButtonAjoutApp.clicked.connect(self.ajout)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, DialogAjoutApplication):
        DialogAjoutApplication.setWindowTitle(QCoreApplication.translate("DialogAjoutApplication", u"Dialog", None))
        self.labelTitreApp.setText(QCoreApplication.translate("DialogAjoutApplication", u"Ajout d'une application", None))
        self.labelNomApp.setText(QCoreApplication.translate("DialogAjoutApplication", u"Site Web ou application", None))
        self.labelPassApp.setText(QCoreApplication.translate("DialogAjoutApplication", u"Mot de passe", None))
        self.pushButtonAjoutApp.setText(QCoreApplication.translate("DialogAjoutApplication", u"Ajouter", None))
    # retranslateUi

    def ajout(self):
        try :
            app = ajouterApplication(self.lineEditNomApp.text(), self.lineEditUsernameApp.text(), self.lineEditPassApp.text(), self.id_)
        except Exception as e :
            Ui_DialogFailed(str(e))
        else:
            itemApp = dataAppPass(app[0], app[1], app[2])
            itemApp.clicked.connect(partial(self.lauchDialogModApp, itemApp.id_))
            self.vbox.insertWidget(0, itemApp)
            Ui_DialogSucces()


        self.lineEditNomApp.setText("")
        self.lineEditPassApp.setText("")
        self.lineEditUsernameApp.setText("")

    def lauchDialogModApp(self,id_):
        self.dialog = Ui_DialogModApp(id_)

        clearLayout(self.vbox,)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vbox.addItem(spacer)

        self.loadMyPasswordApp(self.vbox)

    def loadMyPasswordApp(self, vbox:QVBoxLayout):
        dataApp = lireApplications(self.id_)
        for data in dataApp:
            item = dataAppPass(data[0],data[1],data[2])
            item.clicked.connect(partial(self.lauchDialogModApp,item.id_,))
            vbox.insertWidget(vbox.count()-1,item)

class Ui_DialogAjoutCB(QDialog):
    def __init__(self,vbox,id_):
        super().__init__()
        self.vbox = vbox
        self.setupUi(id_)
        self.exec()
    def setupUi(self,id_):

        self.resize(701, 400)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.id_ = id_

        self.labelTitreaAddCB = QLabel(self)
        self.labelTitreaAddCB.setObjectName(u"labelTitreaAddCB")
        self.labelTitreaAddCB.setGeometry(QRect(260, 10, 171, 19))

        self.pushButtonAjoutCB = QPushButton(self)
        self.pushButtonAjoutCB.setObjectName(u"pushButtonAjoutCB")
        self.pushButtonAjoutCB.setGeometry(QRect(270, 286, 151, 41))
        self.pushButtonAjoutCB.clicked.connect(self.ajout)

        self.lineEditValiditeCB = QLineEdit(self)
        self.lineEditValiditeCB.setObjectName(u"lineEditValiditeCB")
        self.lineEditValiditeCB.setGeometry(QRect(120, 230, 101, 40))

        self.lineEditNumCB = QLineEdit(self)
        self.lineEditNumCB.setObjectName(u"lineEditNumCB")
        self.lineEditNumCB.setGeometry(QRect(120, 150, 441, 40))

        self.labelvaliditeCB = QLabel(self)
        self.labelvaliditeCB.setObjectName(u"labelvaliditeCB")
        self.labelvaliditeCB.setGeometry(QRect(120, 200, 120, 19))

        self.labelNumCB = QLabel(self)
        self.labelNumCB.setObjectName(u"labelNumCB")
        self.labelNumCB.setGeometry(QRect(120, 120, 171, 19))

        self.labelCVVCB = QLabel(self)
        self.labelCVVCB.setObjectName(u"labelCVVCB")
        self.labelCVVCB.setGeometry(QRect(260, 200, 101, 19))

        self.lineEditCVVCB = QLineEdit(self)
        self.lineEditCVVCB.setObjectName(u"lineEditCVVCB")
        self.lineEditCVVCB.setGeometry(QRect(260, 230, 101, 40))

        self.lineEditTitulaireCB = QLineEdit(self)
        self.lineEditTitulaireCB.setObjectName(u"lineEditTitulaireCB")
        self.lineEditTitulaireCB.setGeometry(QRect(120, 70, 441, 40))

        self.labelTitulaireCB = QLabel(self)
        self.labelTitulaireCB.setObjectName(u"labelTitulaireCB")
        self.labelTitulaireCB.setGeometry(QRect(120, 40, 61, 19))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitreaAddCB.setText(QCoreApplication.translate("Dialog", u"Ajout d'une carte bancaire", None))
        self.pushButtonAjoutCB.setText(QCoreApplication.translate("Dialog", u"Ajouter", None))
        self.labelvaliditeCB.setText(QCoreApplication.translate("Dialog", u"carte de validit\u00e9", None))
        self.labelNumCB.setText(QCoreApplication.translate("Dialog", u"Num\u00e9ro carte", None))
        self.labelCVVCB.setText(QCoreApplication.translate("Dialog", u"CVV", None))
        self.lineEditTitulaireCB.setText("")
        self.labelTitulaireCB.setText(QCoreApplication.translate("Dialog", u"Titulaire", None))
    # retranslateUi

    def ajout(self):
        try :
            app = ajouterCarteBancaire(self.lineEditNumCB.text(),self.lineEditValiditeCB.text(),self.lineEditTitulaireCB.text(),self.lineEditCVVCB.text(),self.id_)
        except Exception as e:
            Ui_DialogFailed(str(e))
        else:
            item = dataCB(app[0], app[1], app[3])
            item.clicked.connect(partial(self.lauchDialogModCB, item.id_))
            self.vbox.insertWidget(0, item)

            Ui_DialogSucces()

        self.lineEditTitulaireCB.setText("")
        self.lineEditNumCB.setText("")
        self.lineEditCVVCB.setText("")
        self.lineEditValiditeCB.setText("")

    def lauchDialogModCB(self, id_,):
        self.dialog = Ui_DialogModCB(id_)

        clearLayout(self.vbox)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vbox.addItem(spacer)

        self.loadDataCBs(self.vbox)


    def loadDataCBs(self, vbox:QVBoxLayout):
        dataCb = lireCarteBancaires(self.id_)
        for data in dataCb:
            item = dataCB(data[0],f"NUMERO DE LA CARTE: {data[1]}   ",f"TITULAURE: {data[3]}")
            item.clicked.connect(partial(self.lauchDialogModCB,item.id_))
            vbox.insertWidget(vbox.count()-1,item)

class Ui_DialogAjoutNot(QDialog):

    def __init__(self,vbox,id_):
        super().__init__()
        self.vbox = vbox
        self.setupUi(id_)
        self.exec()

    def setupUi(self,id_):
        self.resize(712, 364)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.id_ = id_

        self.labelTitreNote = QLabel(self)
        self.labelTitreNote.setObjectName(u"labelTitreNote")
        self.labelTitreNote.setGeometry(QRect(290, 30, 151, 19))

        self.pushButtonAjoutNote = QPushButton(self)
        self.pushButtonAjoutNote.setObjectName(u"pushButtonAjoutNote")
        self.pushButtonAjoutNote.setGeometry(QRect(270, 310, 151, 41))
        self.pushButtonAjoutNote.clicked.connect(self.ajout)

        self.labelContenuNote = QLabel(self)
        self.labelContenuNote.setObjectName(u"labelContenuNote")
        self.labelContenuNote.setGeometry(QRect(140, 70, 151, 19))

        self.plainTextEditContenuNote = QPlainTextEdit(self)
        self.plainTextEditContenuNote.setObjectName(u"plainTextEditContenuNote")
        self.plainTextEditContenuNote.setGeometry(QRect(140, 100, 441, 201))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitreNote.setText(QCoreApplication.translate("Dialog", u"Ajout d'une note", None))
        self.pushButtonAjoutNote.setText(QCoreApplication.translate("Dialog", u"Ajouter", None))
        self.labelContenuNote.setText(QCoreApplication.translate("Dialog", u"Contenu de la note", None))
    # retranslateUi

    def ajout(self):
        try :
            noteAjoute = ajouterNote(self.plainTextEditContenuNote.toPlainText(),self.id_,)
            Ui_DialogSucces()
        except Exception as e:
            Ui_DialogFailed(str(e))
        else:
            item = dataNotePass(noteAjoute[0],noteAjoute[1])
            item.clicked.connect(partial(self.lauchDialogModNote, item.id_,))
            self.vbox.insertWidget(0,item)



        self.plainTextEditContenuNote.setPlainText("")

    def lauchDialogModNote(self,id_):
        self.dialog = Ui_DialogModNote(id_)
        clearLayout(self.vbox)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vbox.addItem(spacer)

        self.loadDataNotes(self.vbox)

    def loadDataNotes(self, vbox:QVBoxLayout):
        dataNote = lireNotes(self.id_)
        for data in dataNote:
            item = dataNotePass(data[0],data[1])
            item.clicked.connect(partial(self.lauchDialogModNote,item.id_,item.noteText))
            vbox.insertWidget(vbox.count()-1,item)

class Ui_DialogFailed(QDialog):

    def __init__(self, message):
        super().__init__()
        self.setupUi(message)
        self.exec()

    def setupUi(self, message):
        self.resize(403, 150)
        self.setStyleSheet(u"QDialog {\n"
                           "    background-color: #627F91; /* Couleur de fond sombre */\n"
                           "    border-radius: 10px;\n"
                           "}\n"
                           "\n"
                           "QLineEdit {\n"
                           "    background-color: #2a2a3b; /* Fond des champs de texte */\n"
                           "    color: #ffffff; /* Couleur du texte */\n"
                           "    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
                           "    border-radius: 5px;\n"
                           "    padding: 8px;\n"
                           "    font-size: 14px;\n"
                           "}\n"
                           "\n"
                           "QLineEdit:focus {\n"
                           "    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QPlainTextEdit {\n"
                           "    background-color: #2a2a3b; /* Fond des champs de texte */\n"
                           "    color: #ffffff; /* Couleur du texte */\n"
                           "    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
                           "    border-radius: 5px;\n"
                           "    padding: 8px;\n"
                           "    font-size: 14px;\n"
                           "}\n"
                           "\n"
                           "QPlainTextEdit:focus {\n"
                           "    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QPushButton {\n"
                           "    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
                           "    color: white; /* Couleur du texte */\n"
                           "    border: none; /* Pas de bordure */\n"
                           "    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
                           "    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
                           "    font-size: 14px; /* Taille de la police */\n"
                           "    font-weight: bold; /* Texte en gras */\n"
                           "    margin: 5px 0; /* Espacement entre les boutons */\n"
                           "    height: 25px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover {\n"
                           "    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed {\n"
                           "    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QLabel {\n"
                           "    color: #ffffff; /* Couleur des labels */\n"
                           "    font-size: 14px;\n"
                           "    font-weight: bold;\n"
                           "}\n"
                           "")

        self.pushButtonOk = QPushButton(self)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: #8B0000; /* Rouge vif */\n"
                                        "    color: white; /* Texte en blanc */\n"
                                        "    border: none; /* Pas de bordure */\n"
                                        "    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
                                        "    padding: 10px 20px; /* Espacement int\u00e9rieur */\n"
                                        "    font-size: 14px; /* Taille de la police */\n"
                                        "    font-weight: bold; /* Texte en gras */\n"
                                        "    font-family: Arial, sans-serif; /* Police moderne */\n"
                                        "    transition: background-color 0.3s ease; /* Transition fluide pour les interactions */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #C0392B; /* Rouge plus fonc\u00e9 au survol */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #A93226; /* Rouge encore plus fonc\u00e9 */\n"
                                        "    padding-left: 22px; /* L\u00e9g\u00e8re modification pour l'effet d'appui */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:disabled {\n"
                                        "    background-color: #E6B0AA; /* Rouge p\u00e2le pour l'\u00e9tat d\u00e9sactiv\u00e9 */\n"
                                        "    color: #FDEDEC; /* Couleur de texte plus douce */\n"
                                        "    border: none; /* Pas de bordure */\n"
                                        "}\n"
                                        "")
        self.pushButtonOk.clicked.connect(self.close)

        self.labelEchec = QLabel(self)
        self.labelEchec.setObjectName(u"labelEchec")
        self.labelEchec.setStyleSheet(u"color: \"#8B0000\"")
        self.labelEchec.setText(message)
        self.labelEchec.setWordWrap(True)  # Permettre l'enveloppement du texte

        # Utilisation de QVBoxLayout pour organiser les widgets verticalement
        layout = QVBoxLayout()
        layout.addWidget(self.labelEchec)
        layout.addWidget(self.pushButtonOk)
        self.setLayout(layout)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))

class Ui_DialogGenPassword(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.exec()

    def setupUi(self):
        self.resize(676, 190)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.label = QLabel(self)
        self.label.setObjectName(u"labelNomApp")
        self.label.setGeometry(QRect(50, 150, 451, 19))

        self.lineEditPasswordGen = QLineEdit(self)
        self.lineEditPasswordGen.setObjectName(u"lineEditNomApp")
        self.lineEditPasswordGen.setGeometry(QRect(150, 140, 441, 40))

        self.labelTitreApp = QLabel(self)
        self.labelTitreApp.setObjectName(u"labelTitreApp")
        self.labelTitreApp.setGeometry(QRect(230, 20, 200, 19))

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 80, 231, 41))
        self.pushButton.clicked.connect(self.genPassword)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Mot de passe : ", None))
        self.labelTitreApp.setText(QCoreApplication.translate("Dialog", u"G\u00e9n\u00e9reration un mot de passe", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"G\u00e9n\u00e9rer", None))
    # retranslateUi



    def genPassword(self):
        password = generer_mot_de_passe()
        self.lineEditPasswordGen.setText(password)

class Ui_DialogModApp(QDialog):

    def __init__(self,id_,):
        super().__init__()
        self.id_ = id_
        self.setupUi()
        self.loadApp()
        self.exec()

    def setupUi(self):

        self.setModal(True)

        self.resize(556, 385)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.labelTitreApp = QLabel(self)
        self.labelTitreApp.setObjectName(u"labelTitreApp")
        self.labelTitreApp.setGeometry(QRect(180, 20, 211, 19))

        self.labelNomApp = QLabel(self)
        self.labelNomApp.setObjectName(u"labelNomApp")
        self.labelNomApp.setGeometry(QRect(50, 70, 241, 19))

        self.lineEditNomApp = QLineEdit(self)
        self.lineEditNomApp.setObjectName(u"lineEditNomApp")
        self.lineEditNomApp.setGeometry(QRect(50, 100, 441, 40))

        self.labelUsernameApp = QLabel(self)
        self.labelUsernameApp.setObjectName(u"labelPassApp")
        self.labelUsernameApp.setGeometry(QRect(50, 150, 151, 19))
        self.labelUsernameApp.setText("Nom d'utilisateur")

        self.lineEditUsernameApp = QLineEdit(self)
        self.lineEditUsernameApp.setObjectName(u"lineEditPassApp")
        self.lineEditUsernameApp.setGeometry(QRect(50, 180, 441, 40))

        self.labelPassApp = QLabel(self)
        self.labelPassApp.setObjectName(u"labelPassApp")
        self.labelPassApp.setGeometry(QRect(50, 230, 151, 19))

        self.lineEditPassApp = QLineEdit(self)
        self.lineEditPassApp.setObjectName(u"lineEditPassApp")
        self.lineEditPassApp.setGeometry(QRect(50, 260, 441, 40))

        self.pushButtonModApp = QPushButton(self)
        self.pushButtonModApp.setObjectName(u"pushButtonModApp")
        self.pushButtonModApp.setGeometry(QRect(110, 320, 151, 41))
        self.pushButtonModApp.clicked.connect(self.modApp)

        self.pushButtonSuppApp_2 = QPushButton(self)
        self.pushButtonSuppApp_2.setObjectName(u"pushButtonSuppApp_2")
        self.pushButtonSuppApp_2.setGeometry(QRect(290, 320, 151, 41))
        self.pushButtonSuppApp_2.setStyleSheet(u"/* Style g\u00e9n\u00e9ral du bouton */\n"
"QPushButton {\n"
"    background-color: #E74C3C; /* Rouge vif */\n"
"   color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet au survol */\n"
"QPushButton:hover {\n"
"    background-color: #C0392B; /* Rouge plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Effet au clic */\n"
"QPushButton:pressed {\n"
"    background-color: #A93226; /* Rouge encore plus fonc\u00e9 */\n"
"    padding-left: 22px; /* L\u00e9g\u00e8re modification pour l'effet d'appui */\n"
"}\n"
"\n"
"/* Bouton d\u00e9sactiv\u00e9 (facultatif) */\n"
"QPushButton:disabled {\n"
"    background-color: #E6B0AA; /* Rouge p\u00e2le pour l'\u00e9tat d\u00e9sactiv\u00e9"
                        " */\n"
"    color: #FDEDEC; /* Couleur de texte plus douce */\n"
"    border: none; /* Pas de bordure */\n"
"}\n"
"")
        self.pushButtonSuppApp_2.clicked.connect(self.suppApp)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitreApp.setText(QCoreApplication.translate("Dialog", u"Modification d'une application", None))
        self.pushButtonModApp.setText(QCoreApplication.translate("Dialog", u"Modifier", None))
        self.labelPassApp.setText(QCoreApplication.translate("Dialog", u"Mot de passe", None))
        self.labelNomApp.setText(QCoreApplication.translate("Dialog", u"Nom de l'application ou du site web", None))
        self.pushButtonSuppApp_2.setText(QCoreApplication.translate("Dialog", u"Supprimer", None))
    # retranslateUi

    def loadApp(self):
        try :
            application = lireApplication(self.id_)
        except Exception as e:
            Ui_DialogFailed(str(e))
        else :
            self.lineEditNomApp.setText(application[1])
            self.lineEditUsernameApp.setText(application[2])
            self.lineEditPassApp.setText(application[3])

    def modApp(self):
        try :
            mettreAJourApplication(self.id_,self.lineEditNomApp.text(),self.lineEditUsernameApp.text(),self.lineEditPassApp.text())
            Ui_DialogSucces()
        except Exception as e :
            Ui_DialogFailed(str(e))


    def suppApp(self):
        try :
            supprimerApplication(self.id_)
            Ui_DialogSucces()
            self.close()
        except Exception as e:
            Ui_DialogFailed(str(e))

class Ui_DialogModCB(QDialog):

    def __init__(self,id_):
        super().__init__()
        self.id_ = id_
        self.setupUi()
        self.laodCb()
        self.exec()


    def setupUi(self):
        self.resize(781, 400)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.labelTitreaAddCB = QLabel(self)
        self.labelTitreaAddCB.setObjectName(u"labelTitreaAddCB")
        self.labelTitreaAddCB.setGeometry(QRect(310, 20, 171, 19))

        self.lineEditValiditeCB = QLineEdit(self)
        self.lineEditValiditeCB.setObjectName(u"lineEditValiditeCB")
        self.lineEditValiditeCB.setGeometry(QRect(120, 230, 101, 40))

        self.lineEditNumCB = QLineEdit(self)
        self.lineEditNumCB.setObjectName(u"lineEditNumCB")
        self.lineEditNumCB.setGeometry(QRect(120, 150, 441, 40))
        self.lineEditNumCB.setDisabled(True)

        self.labelvaliditeCB = QLabel(self)
        self.labelvaliditeCB.setObjectName(u"labelvaliditeCB")
        self.labelvaliditeCB.setGeometry(QRect(120, 200, 120, 19))

        self.labelNumCB = QLabel(self)
        self.labelNumCB.setObjectName(u"labelNumCB")
        self.labelNumCB.setGeometry(QRect(120, 120, 171, 19))

        self.labelCVVCB = QLabel(self)
        self.labelCVVCB.setObjectName(u"labelCVVCB")
        self.labelCVVCB.setGeometry(QRect(260, 200, 101, 19))

        self.lineEditCVVCB = QLineEdit(self)
        self.lineEditCVVCB.setObjectName(u"lineEditCVVCB")
        self.lineEditCVVCB.setGeometry(QRect(260, 230, 101, 40))

        self.lineEditTitulaireCB = QLineEdit(self)
        self.lineEditTitulaireCB.setObjectName(u"lineEditTitulaireCB")
        self.lineEditTitulaireCB.setGeometry(QRect(120, 70, 441, 40))

        self.labelTitulaireCB = QLabel(self)
        self.labelTitulaireCB.setObjectName(u"labelTitulaireCB")
        self.labelTitulaireCB.setGeometry(QRect(120, 40, 61, 19))

        self.pushButtonModtCB = QPushButton(self)
        self.pushButtonModtCB.setObjectName(u"pushButtonModtCB")
        self.pushButtonModtCB.setGeometry(QRect(230, 286, 151, 41))
        self.pushButtonModtCB.clicked.connect(self.modCb)

        self.pushButtonSupptCB = QPushButton(self)
        self.pushButtonSupptCB.setObjectName(u"pushButtonSupptCB")
        self.pushButtonSupptCB.setGeometry(QRect(390, 286, 151, 41))
        self.pushButtonSupptCB.setStyleSheet(u"/* Style g\u00e9n\u00e9ral du bouton */\n"
                                                "QPushButton {\n"
                                                "    background-color: #E74C3C; /* Rouge vif */\n"
                                                "   color: white; /* Couleur du texte */\n"
                                                "    border: none; /* Pas de bordure */\n"
                                                "    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
                                                "    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
                                                "    font-size: 14px; /* Taille de la police */\n"
                                                "    font-weight: bold; /* Texte en gras */\n"
                                                "    margin: 5px 0; /* Espacement entre les boutons */\n"
                                                "	height : 25px\n"
                                                "}\n"
                                                "\n"
                                                "/* Effet au survol */\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #C0392B; /* Rouge plus fonc\u00e9 au survol */\n"
                                                "}\n"
                                                "\n"
                                                "/* Effet au clic */\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #A93226; /* Rouge encore plus fonc\u00e9 */\n"
                                                "    padding-left: 22px; /* L\u00e9g\u00e8re modification pour l'effet d'appui */\n"
                                                "}\n"
                                                "\n"
                                                "/* Bouton d\u00e9sactiv\u00e9 (facultatif) */\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #E6B0AA; /* Rouge p\u00e2le pour l'\u00e9tat d\u00e9sactiv\u00e9"
                                                                        " */\n"
                                                "    color: #FDEDEC; /* Couleur de texte plus douce */\n"
                                                "    border: none; /* Pas de bordure */\n"
                                                "}\n"
                                                "")
        self.pushButtonSupptCB.clicked.connect(self.supCb)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitreaAddCB.setText(QCoreApplication.translate("Dialog", u"Ajout d'une carte bancaire", None))
        self.labelvaliditeCB.setText(QCoreApplication.translate("Dialog", u"date de validit\u00e9", None))
        self.labelCVVCB.setText(QCoreApplication.translate("Dialog", u"CVV", None))
        self.labelTitulaireCB.setText(QCoreApplication.translate("Dialog", u"Titulaire", None))
        self.labelNumCB.setText(QCoreApplication.translate("Dialog", u"Num\u00e9ro carte", None))
        self.pushButtonModtCB.setText(QCoreApplication.translate("Dialog", u"Modifier", None))
        self.pushButtonSupptCB.setText(QCoreApplication.translate("Dialog", u"Supprimer", None))
    # retranslateUi*

    def laodCb(self):
        try :
            cb = lireCarteBancaire(self.id_)
        except Exception as e:
            Ui_DialogFailed(str(e))
        else:
            self.lineEditNumCB.setText(str(cb[1]))
            self.lineEditValiditeCB.setText(str(cb[2]))
            self.lineEditTitulaireCB.setText(str(cb[3]))
            self.lineEditCVVCB.setText(str(cb[4]))


    def modCb(self):
        try :
            mettreAJourCarteBancaire(self.id_,self.lineEditValiditeCB.text(),self.lineEditTitulaireCB.text(),self.lineEditCVVCB.text())
            Ui_DialogSucces()
        except Exception as e:
            Ui_DialogFailed(str(e))

    def supCb(self):
        try :
            supprimerCarteBancaire(self.id_)
            Ui_DialogSucces()
            self.close()
        except Exception as e:
            Ui_DialogFailed(str(e))

class Ui_DialogModCompte(QDialog):

    def __init__(self,id_):
        super().__init__()
        self.id_ = id_
        self.setupUi()
        self.loadInfoCompte()
        self.exec()

    def setupUi(self,):
        self.resize(750, 593)
        self.setStyleSheet(u"QDialog {\n"
                           "    background-color: #4A657A; /* Couleur de fond sombre */\n"
                           "    border-radius: 10px;\n"
                           "}\n"
                           "\n"
                           "QLineEdit {\n"
                           "    background-color: #2a2a3b; /* Fond des champs de texte */\n"
                           "    color: #ffffff; /* Couleur du texte */\n"
                           "    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
                           "    border-radius: 5px;\n"
                           "    padding: 8px;\n"
                           "    font-size: 14px;\n"
                           "}\n"
                           "\n"
                           "QLineEdit:focus {\n"
                           "    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QPlainTextEdit {\n"
                           "    background-color: #2a2a3b; /* Fond des champs de texte */\n"
                           "    color: #ffffff; /* Couleur du texte */\n"
                           "    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
                           "    border-radius: 5px;\n"
                           "    padding: 8px;\n"
                           "    font-size: 14px;\n"
                           "}\n"
                           "\n"
                           "QPlainTextEdit:focus {\n"
                           "    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QPushButton {\n"
                           "    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                           "s */\n"
                           "    color: white; /* Couleur du texte */\n"
                           "    border: none; /* Pas de bordure */\n"
                           "    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
                           "    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
                           "    font-size: 14px; /* Taille de la police */\n"
                           "    font-weight: bold; /* Texte en gras */\n"
                           "    margin: 5px 0; /* Espacement entre les boutons */\n"
                           "	height : 25px\n"
                           "}\n"
                           "\n"
                           "/* Effet hover pour les boutons */\n"
                           "QPushButton:hover {\n"
                           "    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
                           "}\n"
                           "\n"
                           "/* Effet clic pour les boutons */\n"
                           "QPushButton:pressed {\n"
                           "    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
                           "}\n"
                           "\n"
                           "QLabel {\n"
                           "    color: #ffffff; /* Couleur des labels */\n"
                           "    font-size: 14px;\n"
                           "    font-weight: bold;\n"
                           "}\n"
                           "")



        self.labelTitreaInfoCompte = QLabel(self)
        self.labelTitreaInfoCompte.setObjectName(u"labelTitreaInfoCompte")
        self.labelTitreaInfoCompte.setGeometry(QRect(320, 20, 101, 19))

        self.labelNomCompte = QLabel(self)
        self.labelNomCompte.setObjectName(u"labelNomCompte")
        self.labelNomCompte.setGeometry(QRect(140, 50, 61, 19))

        self.lineEditPrenomCompte = QLineEdit(self)
        self.lineEditPrenomCompte.setObjectName(u"lineEditPrenomCompte")
        self.lineEditPrenomCompte.setGeometry(QRect(140, 170, 441, 40))

        self.labelPrenomCompte = QLabel(self)
        self.labelPrenomCompte.setObjectName(u"labelPrenomCompte")
        self.labelPrenomCompte.setGeometry(QRect(140, 140, 171, 19))

        self.lineEditNomCompte = QLineEdit(self)
        self.lineEditNomCompte.setObjectName(u"lineEditNomCompte")
        self.lineEditNomCompte.setGeometry(QRect(140, 80, 441, 40))


        self.labelEmailCompte = QLabel(self)
        self.labelEmailCompte.setObjectName(u"labelEmailCompte")
        self.labelEmailCompte.setGeometry(QRect(140, 220, 171, 19))


        self.lineEditEmailCompte = QLineEdit(self)
        self.lineEditEmailCompte.setObjectName(u"lineEditEmailCompte")
        self.lineEditEmailCompte.setGeometry(QRect(140, 250, 441, 40))
        self.lineEditEmailCompte.setDisabled(True)

        self.labelPassCompte = QLabel(self)
        self.labelPassCompte.setObjectName(u"labelPassCompte")
        self.labelPassCompte.setGeometry(QRect(140, 300, 520, 19))
        self.labelPassCompte.setStyleSheet(u'color: \"#8B0000\"')

        self.lineEditPassCompte = QLineEdit(self)
        self.lineEditPassCompte.setObjectName(u"lineEditPassCompte")
        self.lineEditPassCompte.setGeometry(QRect(140, 330, 441, 40))

        self.labelNewPassCompte = QLabel(self)
        self.labelNewPassCompte.setObjectName(u"labelPassCompte")
        self.labelNewPassCompte.setGeometry(QRect(140, 380, 300, 19))

        self.lineEditNewPassCompte = QLineEdit(self)
        self.lineEditNewPassCompte.setObjectName(u"lineEditPassCompte")
        self.lineEditNewPassCompte.setGeometry(QRect(140, 410, 441, 40))

        self.labelNumCompte = QLabel(self)
        self.labelNumCompte.setObjectName(u"labelNumCompte")
        self.labelNumCompte.setGeometry(QRect(140, 460, 171, 19))

        self.lineEditNumCompte = QLineEdit(self)
        self.lineEditNumCompte.setObjectName(u"lineEditNumCompte")
        self.lineEditNumCompte.setGeometry(QRect(140, 490, 441, 40))
        self.lineEditNumCompte.setDisabled(True)

        self.pushButtonModInfoCompte = QPushButton(self)
        self.pushButtonModInfoCompte.setObjectName(u"pushButtonModInfoCompte")
        self.pushButtonModInfoCompte.setGeometry(QRect(300, 550, 151, 41))
        self.pushButtonModInfoCompte.clicked.connect(self.modifierInfo)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelTitreaInfoCompte.setText(QCoreApplication.translate("Dialog", u"Info du compte", None))
        self.labelNomCompte.setText(QCoreApplication.translate("Dialog", u"Nom", None))
        self.labelPrenomCompte.setText(QCoreApplication.translate("Dialog", u"Pr\u00e9nom", None))
        self.pushButtonModInfoCompte.setText(QCoreApplication.translate("Dialog", u"Modifier", None))
        self.labelEmailCompte.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.labelPassCompte.setText(QCoreApplication.translate("Dialog", u"Mot de passe* (Mot de passe réquis pour pouvoir changer une information)", None))
        self.labelNewPassCompte.setText(QCoreApplication.translate("Dialog", u"Entrez le nouvau mot de passe", None))
        self.labelNumCompte.setText(QCoreApplication.translate("Dialog", u"Num\u00e9ro de t\u00e9l\u00e9phone", None))
    # retranslateUi

    def modifierInfo(self):
        try :
            mettre_a_jour_utilisateur(self.id_,self.lineEditNomCompte.text(),self.lineEditPrenomCompte.text(),self.lineEditPassCompte.text(),self.lineEditNewPassCompte.text())
            Ui_DialogSucces()
            self.lineEditNewPassCompte.setText("")
            self.lineEditPassCompte.setText("")
        except Exception as e:
            Ui_DialogFailed(str(e))

    def loadInfoCompte(self):
        try:
            user = lire_utilisateur(self.id_)
        except Exception as e :
            Ui_DialogFailed(str(e))
        else:
            self.lineEditNomCompte.setText(user[1])
            self.lineEditPrenomCompte.setText(user[2])
            self.lineEditEmailCompte.setText(user[3])
            self.lineEditNumCompte.setText(user[5])

class Ui_DialogModNote(QDialog):
    def __init__(self,id_):
        super().__init__()
        self.id_ = id_
        self.setupUi()
        self.loadNote()
        self.exec()

    def setupUi(self,):
        self.resize(736, 365)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #4A657A; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.pushButtonModNote = QPushButton(self)
        self.pushButtonModNote.setObjectName(u"pushButtonModNote")
        self.pushButtonModNote.setGeometry(QRect(190, 310, 151, 41))
        self.pushButtonModNote.setStyleSheet(u"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"")
        self.pushButtonModNote.clicked.connect(self.modNote)

        self.labelContenuNote = QLabel(self)
        self.labelContenuNote.setObjectName(u"labelContenuNote")
        self.labelContenuNote.setGeometry(QRect(150, 60, 151, 19))

        self.plainTextEditContenuNote = QPlainTextEdit(self)
        self.plainTextEditContenuNote.setObjectName(u"plainTextEditContenuNote")
        self.plainTextEditContenuNote.setGeometry(QRect(150, 90, 441, 201))

        self.labelTitreModNote = QLabel(self)
        self.labelTitreModNote.setObjectName(u"labelTitreModNote")
        self.labelTitreModNote.setGeometry(QRect(310, 20, 111, 19))

        self.pushButtonSuppNote = QPushButton(self)
        self.pushButtonSuppNote.setObjectName(u"pushButtonSuppNote")
        self.pushButtonSuppNote.setGeometry(QRect(380, 310, 151, 41))
        self.pushButtonSuppNote.clicked.connect(self.supNote)
        self.pushButtonSuppNote.setStyleSheet(u"/* Style g\u00e9n\u00e9ral du bouton */\n"
"QPushButton {\n"
"    background-color: #E74C3C; /* Rouge vif */\n"
"   color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet au survol */\n"
"QPushButton:hover {\n"
"    background-color: #C0392B; /* Rouge plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Effet au clic */\n"
"QPushButton:pressed {\n"
"    background-color: #A93226; /* Rouge encore plus fonc\u00e9 */\n"
"    padding-left: 22px; /* L\u00e9g\u00e8re modification pour l'effet d'appui */\n"
"}\n"
"\n"
"/* Bouton d\u00e9sactiv\u00e9 (facultatif) */\n"
"QPushButton:disabled {\n"
"    background-color: #E6B0AA; /* Rouge p\u00e2le pour l'\u00e9tat d\u00e9sactiv\u00e9"
                        " */\n"
"    color: #FDEDEC; /* Couleur de texte plus douce */\n"
"    border: none; /* Pas de bordure */\n"
"}\n"
"")

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonModNote.setText(QCoreApplication.translate("Dialog", u"Modfier", None))
        self.labelContenuNote.setText(QCoreApplication.translate("Dialog", u"Contenu de la note", None))
        self.labelTitreModNote.setText(QCoreApplication.translate("Dialog", u"Modier une note", None))
        self.pushButtonSuppNote.setText(QCoreApplication.translate("Dialog", u"Supprimer", None))
    # retranslateUi

    def loadNote(self):
        try:
            note = lireNote(self.id_)
            print(note)
        except Exception as e:
            Ui_DialogFailed(str(e))
        else:
            self.plainTextEditContenuNote.setPlainText(note[1])

    def modNote(self):
        try:
            mettreAJourNote(self.id_,self.plainTextEditContenuNote.toPlainText())
            Ui_DialogSucces()
        except Exception as e:
            Ui_DialogFailed(str(e))

    def supNote(self):
        try:
            supprimerNote(self.id_)
            Ui_DialogSucces()
            self.close()
        except Exception as e:
            Ui_DialogFailed(str(e))

class Ui_DialogSucces(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.exec()


    def setupUi(self):

        self.resize(400, 111)
        self.setStyleSheet(u"QDialog {\n"
"    background-color: #627F91; /* Couleur de fond sombre */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2a2a3b; /* Fond des champs de texte */\n"
"    color: #ffffff; /* Couleur du texte */\n"
"    border: 1px solid #3a3a4a; /* Bord des champs de texte */\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #5a5aff; /* Bord bleu lorsque le champ est s\u00e9lectionn\u00e9 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les bouton"
                        "s */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    background-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff; /* Couleur des labels */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.labelSucces = QLabel(self)
        self.labelSucces.setObjectName(u"labelSucces")
        self.labelSucces.setGeometry(QRect(140, 30, 121, 19))

        self.pushButtonOk = QPushButton(self)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setGeometry(QRect(160, 56, 80, 41))
        self.pushButtonOk.clicked.connect(self.close)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelSucces.setText(QCoreApplication.translate("Dialog", u"Op\u00e9ration r\u00e9ussie", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi