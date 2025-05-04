import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QProcess
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background
        self.Bg = QtWidgets.QLabel(self.centralwidget)
        self.Bg.setGeometry(QtCore.QRect(-30, -20, 1131, 601))
        self.Bg.setStyleSheet("background-color: #0A192F;")

        # Border
        self.bg_border = QtWidgets.QLabel(self.centralwidget)
        self.bg_border.setGeometry(QtCore.QRect(0, 0, 1051, 561))
        self.bg_border.setStyleSheet("border: 2px solid white;")

        # Buttons
        self.pushButton = QtWidgets.QPushButton("START", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 510, 131, 41))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #000;
                color: #0ef;
                border: 2px solid #0ef;
                font: bold 14pt;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #0ef;
                color: black;
            }
        """)

        self.pushButton_2 = QtWidgets.QPushButton("CLOSE", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 510, 131, 41))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #000;
                color: #f55;
                border: 2px solid #f55;
                font: bold 14pt;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #f55;
                color: black;
            }
        """)

        # Status Label
        self.label_status = QtWidgets.QLabel("🔴 Offline", self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(20, 510, 200, 30))
        self.label_status.setStyleSheet("color: red; font: 12pt 'Consolas';")

        # Clock Label
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(850, 10, 180, 30))
        self.label_time.setStyleSheet("color: cyan; font: 12pt Consolas;")
        self.timer_clock = QTimer()
        self.timer_clock.timeout.connect(self.show_time)
        self.timer_clock.start(1000)
        self.show_time()

        # JARVIS Main GIF
        self.Gif = QtWidgets.QLabel(self.centralwidget)
        self.Gif.setGeometry(QtCore.QRect(10, 10, 601, 381))
        self.movie = QMovie("JarvisMain.gif")
        self.Gif.setMovie(self.movie)
        self.movie.start()

        # Voice Wave GIF
        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(620, 10, 421, 201))
        self.movie2 = QMovie("VoiceWave.gif")
        self.Gif_2.setMovie(self.movie2)
        self.movie2.start()

        # Avatar GIF
        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(620, 220, 421, 171))
        self.movie3 = QMovie("AvatarIdle.gif")
        self.Gif_3.setMovie(self.movie3)
        self.movie3.start()

        # Terminal Look TextBrowser
        self.textBrowser_terminal = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_terminal.setGeometry(QtCore.QRect(10, 400, 761, 151))
        self.textBrowser_terminal.setStyleSheet("""
            background-color: black;
            border: 2px solid white;
            color: #39FF14;
            font: 14pt Courier;
        """)

        # Output TextBrowser (Auto Typing)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(780, 450, 256, 51))
        self.textBrowser.setStyleSheet("""
            background-color: black;
            border: 2px solid white;
            color: white;
            font: 20pt;
        """)

        # User Input LineEdit (Command Box)
        self.inputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(780, 410, 256, 30))
        self.inputBox.setPlaceholderText("Type a command...")
        self.inputBox.setStyleSheet("""
            QLineEdit {
                background-color: black;
                color: white;
                border: 2px solid #0ef;
                font: 12pt;
                border-radius: 5px;
                padding-left: 5px;
            }
        """)
        self.inputBox.returnPressed.connect(self.process_input_command)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Sound
        self.sound = QSound("Jarvisstart.wav")
        self.sound.play()

        # Events
        self.pushButton.clicked.connect(self.start_jarvis)
        self.pushButton_2.clicked.connect(sys.exit)

        # QProcess
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("JARVIS")

    def show_time(self):
        current_time = QtCore.QTime.currentTime().toString('hh:mm:ss AP')
        self.label_time.setText(f"🕒 {current_time}")

    def start_jarvis(self):
        self.type_text("Hello Sir, I am Online...")
        self.label_status.setText("🟢 Online")
        self.label_status.setStyleSheet("color: lime; font: 12pt 'Consolas';")
        self.process.start("python", ["-u", "ai_0.1.py"])
        QtCore.QTimer.singleShot(3000, self.idle_avatar)

    def idle_avatar(self):
        self.movie3.stop()
        self.movie3.setFileName("AvatarIdle.gif")
        self.movie3.start()

    def type_text(self, text):
        self.textBrowser.clear()
        self.current_text = ""
        self.text_to_type = text
        self.text_index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(80)

    def update_text(self):
        if self.text_index < len(self.text_to_type):
            self.current_text += self.text_to_type[self.text_index]
            self.textBrowser.setText(self.current_text)
            self.text_index += 1
        else:
            self.timer.stop()

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.textBrowser_terminal.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser_terminal.insertPlainText(data)
        self.textBrowser_terminal.verticalScrollBar().setValue(
            self.textBrowser_terminal.verticalScrollBar().maximum())

        if "Jarvis:" in data:
            reply = data.strip().split("Jarvis:")[-1].strip()
            self.type_text(reply)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.textBrowser_terminal.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser_terminal.insertPlainText(data)
        self.textBrowser_terminal.verticalScrollBar().setValue(
            self.textBrowser_terminal.verticalScrollBar().maximum())

    def process_input_command(self):
        command = self.inputBox.text().strip()
        if command:
            self.textBrowser_terminal.append(f">> {command}")
            self.inputBox.clear()

            if "hello" in command.lower():
                self.type_text("Hi there! How can I assist you?")
            elif "time" in command.lower():
                current_time = QtCore.QTime.currentTime().toString('hh:mm:ss AP')
                self.type_text(f"The current time is {current_time}")
            else:
                self.type_text("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())