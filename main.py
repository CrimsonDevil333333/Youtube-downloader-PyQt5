import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon,QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5 import QtCore
import youtube_dl
import os
import shutil
from os import system
import sip
import time
TIME_LIMIT = 100
import threading

w = 500
h = 300

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Youtube Downloader'
        self.left = 600
        self.top = 400  
        self.width = w
        self.height = h
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMaximumSize(QtCore.QSize(w, h))
        oImage = QImage("images/test.jpg")
        sImage = oImage.scaled(QSize(w,h))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage)) 
        self.setPalette(palette) 
    
        # Create textbox
        self.URL = QLineEdit(self)
        self.URL.setGeometry(QtCore.QRect(70, 70, 282, 31))
        self.URL.setObjectName("URL")
        
        # Create a button in the window
        self.check = QPushButton('Check', self)
        self.check.setGeometry(QtCore.QRect(380, 70, 66, 31))
        self.check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check.clicked.connect(self.on_click)

        self.mp3 = QPushButton("MP3",self)
        self.mp3.setGeometry(QtCore.QRect(50, 140, 56, 31))
        self.mp3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mp3.clicked.connect(self.mp3_format)

        self.mkv = QPushButton("MKV",self)
        self.mkv.setGeometry(QtCore.QRect(225, 140, 56, 31))
        self.mkv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mkv.clicked.connect(self.mkv_format)

        self.K2 = QPushButton("360p",self)
        self.K2.setGeometry(QtCore.QRect(420, 140, 56, 31))
        self.K2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.K2.clicked.connect(self.k2_format_360p)


        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(40, 230, 451, 31))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        
        self.show()
    

    @pyqtSlot()
    def on_click(self):
        self.progressBar.setValue(0)
        textboxValue = self.URL.text()
        QMessageBox.question(self, 'Your URL', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.URL.setText(textboxValue)
        self.progressBar.setValue(0)


    @pyqtSlot()
    def k2_format_360p(self):
        self.progressBar.setValue(10)
        url = self.URL.text()
        time.sleep(.5)
        self.progressBar.setValue(30)
        ydl_opts = {
            'format': '18',  
        }        
        time.sleep(.5)
        self.progressBar.setValue(49)
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading video in 360p now\n")
                self.progressBar.setValue(50)
                ydl.download([url])
                time.sleep(.5)
                self.progressBar.setValue(85)
                time.sleep(.5)
                self.progressBar.setValue(100)
        except:
            textboxValue = "Cant able to download your video pls check your Link or Net Connection"
            QMessageBox.question(self, 'Error', textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            print("Cant able to download your video pls check your Link or Net Connection")
            self.progressBar.setValue(100)

    

    @pyqtSlot()
    def mkv_format(self):
        self.progressBar.setValue(10)
        time.sleep(.5)
        url = self.URL.text()
        self.progressBar.setValue(20)
        time.sleep(.5)
        ydl_opts = {}
        ydl_opts['quiet'] = True
        ydl_opts['merge_output_format'] = 'mkv'
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio'
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                self.progressBar.setValue(40)
                time.sleep(.5)
                print("Downloading mkv hd video now\n")
                ydl.download([url])
                result = ydl.extract_info(url, download=False)
                self.progressBar.setValue(70)
                time.sleep(.5)
                self.progressBar.setValue(100)
        except:
            textboxValue = "Cant able to download your video pls check your Link or Net Connection"
            QMessageBox.question(self, 'Error', textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            print("Cant able to download your video pls check your Link or Net Connection")
            self.progressBar.setValue(100)


    @pyqtSlot()
    def mp3_format(self):
        self.progressBar.setValue(9)
        time.sleep(.5)
        url = self.URL.text()
        self.progressBar.setValue(26)
        ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        time.sleep(.5)
        self.progressBar.setValue(40)
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading audio file now\n")
                self.progressBar.setValue(56)
                t1 = threading.Thread(target=ydl.download([url]))
                t1.start()
                t1.join()
                self.progressBar.setValue(70)
                time.sleep(.5)
                for i in range (1,31,1):
                    self.progressBar.setValue(70+i)
        except:
            textboxValue = "Cant able to download your video pls check your Link or Net Connection"
            QMessageBox.question(self, 'Error', textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            print("Cant able to download your video pls check your Link or Net Connection")
            self.progressBar.setValue(100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

