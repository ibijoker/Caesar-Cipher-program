# 🔐 Interactive Caesar Cipher

A simple, interactive command-line application built in Python that encrypts and decrypts text using the classic Caesar Cipher algorithm. 

This project was built to explore the fundamentals of data protection, symmetric encryption, and algorithm visualization.

## 🚀 Features
- **Two-way processing:** Easily switch between `Encrypt` and `Decrypt` modes.
- **Smart character handling:** Shifts alphabetic characters while perfectly preserving spaces, numbers, and punctuation.
- **Dynamic wrapping:** Uses modulo arithmetic to seamlessly wrap around the alphabet (e.g., shifting past 'Z' loops back to 'A').
- **User-friendly:** Interactive prompts in the terminal for seamless user experience.

## 📸 See it in Action
<img width="1535" height="863" alt="screenshot" src="https://github.com/user-attachments/assets/b8e8f8e0-ff81-4b55-83d2-e6ce9881d27d" />

## 💻 Example Output

As seen in the project demo, encrypting and then decrypting restores the original text:

**Encryption:**
```text
--- Interactive Caesar Cipher ---
Do you want to (E)ncrypt or (D)ecrypt? e
Enter the text to encrypt: this is project 2 at decode
Enter the shift key (e.g., 3): 3

--- Result ---
Original: this is project 2 at decode
Output:   wklv lv surmhfw 2 dw ghfrgh
