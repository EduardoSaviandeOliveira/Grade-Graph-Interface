import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from WindowLogin import WindowLogin

app = QApplication(sys.argv)
window = WindowLogin()

window.show()
sys.exit(app.exec())