import sys

from PyQt6.QtWidgets import QApplication, Qlabel, QWidget

app = QApplication([])

window + QWidget()
window.setwindowtitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>What's up?</h1>", parent = window)
helloMsg.move(60, 15)
window.show()
sys.exit(app.exec())