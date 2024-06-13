# Sandstorm - GPG Encryption app

This is a small local application to write messages and encrypt text or files using GPG, making it easy to copy and paste the encrypted content into Gmail for sending. Gmail does not have native support for sending encrypted emails via GPG tools. While services like ProtonMail or some browser/mail app plugins offer similar features, I prefer a local and self-contained application for a little extra privacy and security.

## Features

- Encrypt text messages and copy the encrypted text to the clipboard
- Encrypt files and save the encrypted version
- Select recipient from known GPG keys
- User-friendly interface built with PyQt (☠️)

## Installation

### Prerequisites

- Python 3.x
- GPG (GnuPG)
- `gnupg` Python package
- `PyQt5` Python package
- `pyperclip` Python package
- Astral's [uv](https://github.com/astral-sh/uv) for python package management - optional

### Install Dependencies

```bash
uv venv
uv pip install python-gnupg PyQt5 pyperclip
```

## Usage
Clone the repository:

```bash
git clone https://github.com/jwalker/gpg-sandstorm.git
cd gpg-sandstorm
```

Run the application:

```bash
python sandstorm.py
```

Encrypt Text:

- Select recipients GPG key ID from the dropdown.
- Click "Encrypt Text" to encrypt the message.
- The encrypted message will be copied to your clipboard for easy pasting into Gmail.


Encrypt File:

- Select recipients GPG key ID from the dropdown.
- Click "Encrypt File" to select a file and encrypt it.
- The encrypted file will be saved with a .gpg extension.

### Signing Public Keys

If you encounter an error stating "Failed to encrypt message. Status: invalid recipient," you may need to sign the recipient's public key to verify the key owner:

```bash
gpg --sign-key [KEY_ID]
```

### Additional Information

This tool provides an extra layer of privacy and security by being a local and self-contained application. It ensures that the encryption process happens on your machine without relying on external services or plugins.

### Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
