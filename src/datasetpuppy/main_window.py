from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DatasetPuppy")
        self.resize(700, 500)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("DatasetPuppy")
        title.setAlignment(Qt.AlignCenter)

        font = title.font()
        font.setPointSize(24)
        font.setBold(True)
        title.setFont(font)

        open_button = QPushButton("Open Dataset")

        status_label = QLabel("")
        status_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(open_button)
        layout.addWidget(status_label)
        layout.addStretch()

        self.setCentralWidget(central_widget)
        self.statusBar().showMessage("Ready")
