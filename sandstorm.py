import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QComboBox
import gnupg
import pyperclip

# Initialize GPG
gpg = gnupg.GPG()

class GPGEncryptor(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.load_keys()
        
    def initUI(self):
        self.setWindowTitle('GPG - Sandstorm')
        
        layout = QVBoxLayout()
        
        self.recipient_label = QLabel('Recipient GPG Key:')
        layout.addWidget(self.recipient_label)
        
        self.recipient_dropdown = QComboBox()
        layout.addWidget(self.recipient_dropdown)
        
        self.text_label = QLabel('Message:')
        layout.addWidget(self.text_label)
        
        self.text_entry = QTextEdit()
        layout.addWidget(self.text_entry)
        
        self.encrypt_text_button = QPushButton('Encrypt Text')
        self.encrypt_text_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_text_button)
        
        self.encrypt_file_button = QPushButton('Encrypt File')
        self.encrypt_file_button.clicked.connect(self.encrypt_file)
        layout.addWidget(self.encrypt_file_button)
        
        self.setLayout(layout)
    
    def load_keys(self):
        keys = gpg.list_keys()
        for key in keys:
            for uid in key['uids']:
                self.recipient_dropdown.addItem(f"{uid} ({key['keyid']})")
    
    def encrypt_text(self):
        recipient = self.recipient_dropdown.currentText().split()[-1].strip('()')
        message = self.text_entry.toPlainText()
        if not recipient or not message.strip():
            QMessageBox.critical(self, "Error", "Recipient and message cannot be empty.")
            return
        encrypted_data = gpg.encrypt(message, recipient)
        if encrypted_data.ok:
            pyperclip.copy(str(encrypted_data))
            QMessageBox.information(self, "Success", "Message encrypted and copied to clipboard.")
        else:
            error_message = f"Failed to encrypt message. Status: {encrypted_data.status}, Stderr: {encrypted_data.stderr}"
            QMessageBox.critical(self, "Error", error_message)
            print(error_message)

    
    def encrypt_file(self):
        recipient = self.recipient_dropdown.currentText().split()[-1].strip('()')
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'All Files (*)')
        if not recipient or not file_path:
            QMessageBox.critical(self, "Error", "Recipient and file cannot be empty.")
            return
        with open(file_path, 'rb') as f:
            encrypted_data = gpg.encrypt_file(f, recipients=[recipient], output=f"{file_path}.gpg")
        if encrypted_data.ok:
            QMessageBox.information(self, "Success", f"File encrypted and saved as {file_path}.gpg")
        else:
            QMessageBox.critical(self, "Error", "Failed to encrypt file.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GPGEncryptor()
    ex.show()
    sys.exit(app.exec_())
