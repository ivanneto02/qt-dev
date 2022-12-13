from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow

def main():
    app = QApplication([])
    window = QMainWindow()
    window.show() # show the label
    app.exec()  # execute application

if __name__ == "__main__":
    main()