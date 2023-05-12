# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applikacija1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import csv

import numpy
import scipy
from PyQt5 import QtCore, QtGui, QtWidgets
import pyxdf
import pyqtgraph as pg
import numpy as np
from PyQt5.QtGui import QPixmap
from scipy import signal
import pyhrv

import mne


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 933)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(42, 42, 63);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vest_label = QtWidgets.QLabel(self.centralwidget)
        self.vest_label.setGeometry(QtCore.QRect(30, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vest_label.setFont(font)
        self.vest_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.vest_label.setObjectName("vest_label")
        self.vest = QtWidgets.QComboBox(self.centralwidget)
        self.vest.setGeometry(QtCore.QRect(100, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vest.setFont(font)
        self.vest.setAutoFillBackground(False)
        self.vest.setStyleSheet("background-color: rgb(90, 90, 135);\n"
"background-color: rgb(91, 91, 136);\n"
"color: rgb(170, 170, 255);")
        self.vest.setFrame(False)
        self.vest.setObjectName("vest")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.vest.addItem("")
        self.slika = QtWidgets.QLabel(self.centralwidget)
        self.slika.setGeometry(QtCore.QRect(30, 50, 441, 341))
        self.slika.setStyleSheet("")
        self.slika.setObjectName("slika")
        self.ispitanik_label = QtWidgets.QLabel(self.centralwidget)
        self.ispitanik_label.setGeometry(QtCore.QRect(30, 450, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ispitanik_label.setFont(font)
        self.ispitanik_label.setStyleSheet("color: rgb(202, 202, 202);\n"
"color: rgb(170, 170, 255);")
        self.ispitanik_label.setObjectName("ispitanik_label")
        self.ispitanik = QtWidgets.QComboBox(self.centralwidget)
        self.ispitanik.setGeometry(QtCore.QRect(120, 450, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 93, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.ispitanik.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ispitanik.setFont(font)
        self.ispitanik.setStyleSheet("color: rgb(170, 170, 255);\n"
"background-color: rgb(93, 93, 139);")
        self.ispitanik.setFrame(False)
        self.ispitanik.setObjectName("ispitanik")
        self.ispitanik.addItem("")
        self.ispitanik.addItem("")
        self.ispitanik.addItem("")
        self.ucitaj = QtWidgets.QPushButton(self.centralwidget)
        self.ucitaj.setGeometry(QtCore.QRect(30, 760, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ucitaj.setFont(font)
        self.ucitaj.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ucitaj.setStyleSheet("color: rgb(170, 170, 255);\n"
"background-color: rgb(93, 93, 139);\n"
"")
        self.ucitaj.setCheckable(False)
        self.ucitaj.setObjectName("ucitaj")
        self.obrisi = QtWidgets.QPushButton(self.centralwidget)
        self.obrisi.setGeometry(QtCore.QRect(190, 760, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.obrisi.setFont(font)
        self.obrisi.setMouseTracking(True)
        self.obrisi.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.obrisi.setAutoFillBackground(False)
        self.obrisi.setStyleSheet("background-color: rgb(93, 93, 139);\n"
"color: rgb(170, 170, 255);")
        self.obrisi.setAutoDefault(False)
        self.obrisi.setDefault(False)
        self.obrisi.setFlat(False)
        self.obrisi.setObjectName("obrisi")
        self.gsr = QtWidgets.QWidget(self.centralwidget)
        self.gsr.setGeometry(QtCore.QRect(560, 340, 751, 221))
        self.gsr.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.gsr.setObjectName("gsr")
        self.gsr_label = QtWidgets.QLabel(self.centralwidget)
        self.gsr_label.setGeometry(QtCore.QRect(560, 290, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gsr_label.setFont(font)
        self.gsr_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.gsr_label.setObjectName("gsr_label")
        self.eeg_label = QtWidgets.QLabel(self.centralwidget)
        self.eeg_label.setGeometry(QtCore.QRect(560, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eeg_label.setFont(font)
        self.eeg_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.eeg_label.setObjectName("eeg_label")
        self.podnaslov = QtWidgets.QLabel(self.centralwidget)
        self.podnaslov.setGeometry(QtCore.QRect(30, 520, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.podnaslov.setFont(font)
        self.podnaslov.setStyleSheet("color: rgb(170, 170, 255);")
        self.podnaslov.setObjectName("podnaslov")
        self.kanal_label = QtWidgets.QLabel(self.centralwidget)
        self.kanal_label.setGeometry(QtCore.QRect(30, 580, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kanal_label.setFont(font)
        self.kanal_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.kanal_label.setObjectName("kanal_label")
        self.talas_label = QtWidgets.QLabel(self.centralwidget)
        self.talas_label.setGeometry(QtCore.QRect(30, 640, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.talas_label.setFont(font)
        self.talas_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.talas_label.setObjectName("talas_label")
        self.kanal = QtWidgets.QComboBox(self.centralwidget)
        self.kanal.setGeometry(QtCore.QRect(120, 580, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kanal.setFont(font)
        self.kanal.setStyleSheet("background-color: rgb(93, 93, 139);\n"
"color: rgb(170, 170, 255);")
        self.kanal.setFrame(False)
        self.kanal.setObjectName("kanal")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.kanal.addItem("")
        self.talas = QtWidgets.QComboBox(self.centralwidget)
        self.talas.setGeometry(QtCore.QRect(120, 640, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.talas.setFont(font)
        self.talas.setStyleSheet("color: rgb(170, 170, 255);\n"
"background-color: rgb(93, 93, 139);")
        self.talas.setFrame(False)
        self.talas.setObjectName("talas")
        self.talas.addItem("")
        self.talas.addItem("")
        self.talas.addItem("")
        self.talas.addItem("")
        self.talas.addItem("")
        self.eeg = QtWidgets.QWidget(self.centralwidget)
        self.eeg.setGeometry(QtCore.QRect(560, 50, 751, 221))
        self.eeg.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.eeg.setObjectName("eeg")
        self.ecg = QtWidgets.QWidget(self.centralwidget)
        self.ecg.setGeometry(QtCore.QRect(560, 630, 751, 221))
        self.ecg.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.ecg.setObjectName("ecg")
        self.ecg_label = QtWidgets.QLabel(self.centralwidget)
        self.ecg_label.setGeometry(QtCore.QRect(560, 580, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ecg_label.setFont(font)
        self.ecg_label.setStyleSheet("color: rgb(170, 170, 255);")
        self.ecg_label.setObjectName("ecg_label")
        self.eksport = QtWidgets.QPushButton(self.centralwidget)
        self.eksport.setGeometry(QtCore.QRect(350, 760, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eksport.setFont(font)
        self.eksport.setMouseTracking(True)
        self.eksport.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.eksport.setAutoFillBackground(False)
        self.eksport.setStyleSheet("background-color: rgb(93, 93, 139);\n"
"color: rgb(170, 170, 255);")
        self.eksport.setAutoDefault(False)
        self.eksport.setDefault(False)
        self.eksport.setFlat(False)
        self.eksport.setObjectName("eksport")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1384, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

                                         # CUSTOM CODE
        self.t = 573  # 9.46 min
        self.fs = 5  # frekfencija odabiranja za GSR
        self.fs2 = 250  # frekfencija odabiranja za EKG
        self.total_samples = self.fs * self.t
        self.nyq = 0.5 * self.fs  # Nikvistova f
        self.nyq2 = 0.5 * self.fs2

        # Vremena u kojima se pojavljuje vest
        self.starts = [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553]
        self.ends = [23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573]

        # Algoritam za uskladjivanje ispitanika i slike
        self.m = [
            [2, 6, 1, 7, 3, 0, 10, 8, 5, 9, 4, 11],
            [5, 0, 9, 1, 6, 7, 2, 8, 4, 11, 10, 3],
            [9, 7, 5, 1, 3, 10, 4, 2, 6, 0, 11, 8]
        ]

        self.gsr_graph = pg.PlotWidget(self.gsr)
        self.gsr_graph.showGrid(x=True, y=True)
        self.gsr_graph.setGeometry(QtCore.QRect(0, 0, 671, 181))

        self.eeg_graph = pg.PlotWidget(self.eeg)
        self.eeg_graph.showGrid(x=True, y=True)
        self.eeg_graph.setGeometry(QtCore.QRect(0, 0, 671, 181))

        self.ecg_graph = pg.PlotWidget(self.ecg)
        self.ecg_graph.showGrid(x=True, y=True)
        self.ecg_graph.setGeometry(QtCore.QRect(0, 0, 671, 181))

        self.ucitaj.clicked.connect(lambda: self.render())
        self.obrisi.clicked.connect(lambda: self.clear())
        self.eksport.clicked.connect(lambda: self.eksport_ecg())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vest_label.setText(_translate("MainWindow", "Vest"))
        self.vest.setItemText(0, _translate("MainWindow", "1"))
        self.vest.setItemText(1, _translate("MainWindow", "2"))
        self.vest.setItemText(2, _translate("MainWindow", "3"))
        self.vest.setItemText(3, _translate("MainWindow", "4"))
        self.vest.setItemText(4, _translate("MainWindow", "5"))
        self.vest.setItemText(5, _translate("MainWindow", "6"))
        self.vest.setItemText(6, _translate("MainWindow", "7"))
        self.vest.setItemText(7, _translate("MainWindow", "8"))
        self.vest.setItemText(8, _translate("MainWindow", "9"))
        self.vest.setItemText(9, _translate("MainWindow", "10"))
        self.vest.setItemText(10, _translate("MainWindow", "11"))
        self.vest.setItemText(11, _translate("MainWindow", "12"))
        self.slika.setText(_translate("MainWindow", "slika"))
        self.ispitanik_label.setText(_translate("MainWindow", "Ispitanik"))
        self.ispitanik.setItemText(0, _translate("MainWindow", " 1"))
        self.ispitanik.setItemText(1, _translate("MainWindow", " 2"))
        self.ispitanik.setItemText(2, _translate("MainWindow", " 3"))
        self.ucitaj.setText(_translate("MainWindow", "Učitaj"))
        self.obrisi.setText(_translate("MainWindow", "Obriši"))
        self.gsr_label.setText(_translate("MainWindow", "GSR"))
        self.eeg_label.setText(_translate("MainWindow", "EEG"))
        self.podnaslov.setText(_translate("MainWindow", "EEG parametri"))
        self.kanal_label.setText(_translate("MainWindow", "Kanal"))
        self.talas_label.setText(_translate("MainWindow", "Talas"))
        self.kanal.setItemText(0, _translate("MainWindow", "1"))
        self.kanal.setItemText(1, _translate("MainWindow", "2"))
        self.kanal.setItemText(2, _translate("MainWindow", "3"))
        self.kanal.setItemText(3, _translate("MainWindow", "4"))
        self.kanal.setItemText(4, _translate("MainWindow", "5"))
        self.kanal.setItemText(5, _translate("MainWindow", "6"))
        self.kanal.setItemText(6, _translate("MainWindow", "7"))
        self.kanal.setItemText(7, _translate("MainWindow", "8"))
        self.kanal.setItemText(8, _translate("MainWindow", "9"))
        self.kanal.setItemText(9, _translate("MainWindow", "10"))
        self.kanal.setItemText(10, _translate("MainWindow", "11"))
        self.kanal.setItemText(11, _translate("MainWindow", "12"))
        self.kanal.setItemText(12, _translate("MainWindow", "13"))
        self.kanal.setItemText(13, _translate("MainWindow", "14"))
        self.kanal.setItemText(14, _translate("MainWindow", "15"))
        self.kanal.setItemText(15, _translate("MainWindow", "16"))
        self.kanal.setItemText(16, _translate("MainWindow", "17"))
        self.kanal.setItemText(17, _translate("MainWindow", "18"))
        self.kanal.setItemText(18, _translate("MainWindow", "19"))
        self.kanal.setItemText(19, _translate("MainWindow", "21"))
        self.kanal.setItemText(20, _translate("MainWindow", "22"))
        self.kanal.setItemText(21, _translate("MainWindow", "23"))
        self.kanal.setItemText(22, _translate("MainWindow", "24"))
        self.talas.setItemText(0, _translate("MainWindow", "Alfa"))
        self.talas.setItemText(1, _translate("MainWindow", "Beta"))
        self.talas.setItemText(2, _translate("MainWindow", "Gama"))
        self.talas.setItemText(3, _translate("MainWindow", "Delta"))
        self.talas.setItemText(4, _translate("MainWindow", "Teta"))
        self.ecg_label.setText(_translate("MainWindow", "ECG"))
        self.eksport.setText(_translate("MainWindow", "Export"))


                                           #Obrada signala
 # ucitavanje
    def load_data(self, ispitanik):
        file = 'data/vesti_id{}.xdf'.format(ispitanik + 1)
        data = pyxdf.load_xdf(file)
        return data

    def load_eeg(self, ispitanik):
        file = 'data/eeg_ica_id{}.txt.npy'.format(ispitanik+1)
        data = np.load(file)
        return data

                                                #GSR

    def ucitaj_gsr(self):
        ispitanik = int(self.ispitanik.currentText().strip()) - 1
        data = self.load_data(ispitanik)[0][1]['time_series']
        vest = int(self.vest.currentText()) - 1
        vest_index = self.m[ispitanik][vest]
        pocetni_odbirak = self.starts[vest_index] * self.fs
        krajni_odbirak = self.ends[vest_index] * self.fs
        isecak = data[pocetni_odbirak:krajni_odbirak]

        # Isecak raw
        isecak = np.reshape(isecak, -1)
        # Filtriranje iseckak
        # b2, a2 = scipy.signal.butter(2, 2.45 / self.nyq, 'lowpass')
        # filtrirani_isecak = scipy.signal.lfilter(b2, a2, isecak)
        return isecak, data.min(), data.max()

    def render_gsr(self):
        isecak, min, max = self.ucitaj_gsr()
        self.gsr_graph.plot(isecak)
        self.gsr_graph.setLabel('bottom', text="Vremenski odbirci (razmera:0.2s)")
        self.gsr_graph.setLabel('left', units='uS', text="Provodnost koze")
        self.gsr_graph.setYRange(min, max)

                                             # EEG
    def ucitaj_eeg(self):
        ispitanik = int(self.ispitanik.currentText().strip()) - 1
        kanal = int(self.kanal.currentText())
        data = self.load_eeg(ispitanik)[kanal] / 40e-9
        # [:, kanal - 1]

        vest = int(self.vest.currentText()) - 1
        vest_index = self.m[ispitanik][vest]
        pocetni_odbirak = self.starts[vest_index] * self.fs2
        krajni_odbirak = self.ends[vest_index] * self.fs2
        isecak = data[pocetni_odbirak:krajni_odbirak]

        talas = self.talas.currentText()
        if talas == 'Alfa':
            opseg_pocetak = 8
            opseg_kraj = 13
        elif talas == 'Beta':
            opseg_pocetak = 13
            opseg_kraj = 30
        elif talas == 'Gama':
            opseg_pocetak = 30
            opseg_kraj = 50
        elif talas == 'Delta':
            opseg_pocetak = 0.5
            opseg_kraj = 4
        else:  # Teta
            opseg_pocetak = 4
            opseg_kraj = 8

        # filtriranje
        b, a = scipy.signal.butter(3, [opseg_pocetak / self.nyq2, opseg_kraj / self.nyq2], 'band')
        filtriran_isecak = scipy.signal.filtfilt(b, a, isecak)
        # plot snage
        snaga = self.racunaj_snagu(filtriran_isecak)
        return snaga

    def render_eeg(self):
        snaga = self.ucitaj_eeg()
        #snaga = [x*1000 for x in snaga]
        self.eeg_graph.plot(snaga)
        self.eeg_graph.setLabel('bottom', text="Vremenski odbirci (razmera:4ms)")
        self.eeg_graph.setLabel('left', units = 'uV^2/Hz', text="Spektralna gustina snage") #Spektralna gustina snage"


                                                #ECG

    def ucitaj_ecg(self):
        ispitanik = int(self.ispitanik.currentText().strip()) - 1
        data = self.load_data(ispitanik)[0][0]['time_series'][:, 19]

        vest = int(self.vest.currentText()) - 1
        vest_index = self.m[ispitanik][vest]
        pocetni_odbirak = self.starts[vest_index] * self.fs2
        krajni_odbirak = self.ends[vest_index] * self.fs2
        isecak = data[pocetni_odbirak:krajni_odbirak]

        b, a = scipy.signal.butter(3, [2 / self.nyq2, 40 / self.nyq2], 'band')
        filteredBandPass = scipy.signal.filtfilt(b, a, isecak)

        #trazenje pikova
        differentiated = np.diff(filteredBandPass)
        invdiff = (-1) * differentiated
        peaks, _ = scipy.signal.find_peaks(invdiff, height=55, distance=50, prominence=50)
        last_num = peaks[0]
        novi_peaks = [last_num]

        for x in peaks[1:]:
            if x - last_num >= 150:
                novi_peaks.append(x)
                last_num = x

        peaks_x_values = novi_peaks
        peaks_y_values = filteredBandPass[novi_peaks]
        for znj in range(500):
            for x in peaks_x_values[0:]:
                if peaks_y_values[peaks_x_values.index(x)] < filteredBandPass[x - 1]:
                    peaks_y_values[peaks_x_values.index(x)] = filteredBandPass[x - 1]
                    peaks_x_values[peaks_x_values.index(x)] = x - 1
        return filteredBandPass, peaks_x_values, peaks_y_values

    def render_ecg(self):
        filteredBandPass, peaks_x_values, peaks_y_values = self.ucitaj_ecg()
        self.ecg_graph.plot(filteredBandPass)
        self.ecg_graph.setLabel('bottom', text="Vremenski odbirci (razmera 4ms)")
        self.ecg_graph.setLabel('left', units='mV*10^2', text="Amplituda")
        scatter = pg.ScatterPlotItem(
            size=10, brush=pg.mkBrush(255, 0, 111, 180))
        scatter.addPoints(peaks_x_values, peaks_y_values)
        self.ecg_graph.addItem(scatter)

    def eksport_ecg(self):
        filteredBandPass, peaks_x_values, peaks_y_values = self.ucitaj_ecg()
        RR_intervali = []
        for x, y in zip(peaks_x_values[0::], peaks_x_values[1::]):
            RR_intervali.append((y - x) / self.fs2)  # delimo sa 250Hz da bismo dobili int u sek
        results = pyhrv.hrv(RR_intervali, self.fs2)
        # print('a')
        csv_output = [[], []]

        for param_name, param_value in results.as_dict().items():
            if type(param_value) in [numpy.float64, numpy.int64, str]:
                csv_output[0].append(param_name)
                csv_output[1].append(param_value)

        # Eksport eeg
        snaga = self.ucitaj_eeg()
        mean_eeg = np.mean(snaga)
        csv_output[0].append("EEG")
        csv_output[1].append(mean_eeg)

        #Eksport gsr
        isecak, _, _= self.ucitaj_gsr()
        mean_gsr=np.mean(isecak)
        csv_output[0].append("GSR")
        csv_output[1].append(mean_gsr)

        # Eksport u fajl
        ispitanik = int(self.ispitanik.currentText().strip())
        vest = int(self.vest.currentText())
        file_name = 'data/hrv/ispitanik_{}_vest_{}.csv'.format(ispitanik, vest)
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(csv_output)


    # EEG- odredjivanje gustine sprektrane snage putem Welch metode
    def racunaj_snagu(self, filteredBandPass):
        srednja_snaga = []
        for i in range(10):
            f, Pxx_den = signal.welch(filteredBandPass[i * 500:(i + 1) * 500], 250)
            srednja_snaga.append(np.mean(Pxx_den))
        return srednja_snaga

    def render_image(self):
        vest = self.vest.currentText().strip()
        pixmap = QPixmap('data/images/{}.jpg'.format(vest))
        pixmap.scaled(self.slika.width(), self.slika.height())
        self.slika.setScaledContents(True)
        self.slika.setPixmap(pixmap)

    def render(self):
        self.clear()
        self.render_image()
        self.render_gsr()
        self.render_eeg()
        self.render_ecg()

    def clear(self):
        self.gsr_graph.clear()
        self.eeg_graph.clear()
        self.ecg_graph.clear()
        self.slika.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
