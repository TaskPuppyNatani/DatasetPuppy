from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .dataset_processor import DatasetProcessor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.processor = DatasetProcessor()

        self.setWindowTitle("DatasetPuppy")
        self.resize(700, 500)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("DatasetPuppy")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = title.font()
        font.setPointSize(24)
        font.setBold(True)
        title.setFont(font)

        open_button = QPushButton("Open Dataset")
        open_button.clicked.connect(self.open_dataset)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(open_button)
        layout.addWidget(self.status_label)
        layout.addStretch()

        self.setCentralWidget(central_widget)
        self.statusBar().showMessage("Ready")

    def open_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Dataset",
            "",
            "Dataset Files (*.jsonl *.json);;All Files (*)",
        )

        if not file_path:
            return

        try:
            result = self.processor.inspect_dataset(file_path)

            self.status_label.setText(
                f"File: {result['file_name']}\n"
                f"Type: {result['file_type']}\n"
                f"Records: {result['records']}\n"
                f"Valid: {result['valid_records']}\n"
                f"Invalid: {result['invalid_records']}"
            )

            self.statusBar().showMessage("Dataset inspected")

        except Exception as error:
            self.status_label.setText(f"Error: {error}")
            self.statusBar().showMessage("Inspection failed")
