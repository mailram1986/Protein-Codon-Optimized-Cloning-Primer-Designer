from PyQt5 import QtWidgets
import sys

class PrimerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Protein → Primer Designer")
        self.resize(600, 400)

        layout = QtWidgets.QVBoxLayout()

        self.input = QtWidgets.QTextEdit()
        self.input.setPlaceholderText("Paste Protein Sequence")

        self.run = QtWidgets.QPushButton("Generate Primers")
        self.output = QtWidgets.QTextEdit()

        self.run.clicked.connect(self.process)

        layout.addWidget(self.input)
        layout.addWidget(self.run)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def process(self):
        protein = self.input.toPlainText()
        self.output.setText("Connect same backend logic here")

app = QtWidgets.QApplication(sys.argv)
window = PrimerApp()
window.show()
sys.exit(app.exec_())
