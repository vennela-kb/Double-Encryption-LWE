# 🔐 Double Encryption using LWE and AES

## 📌 Overview
This project implements a **double encryption mechanism** combining **Learning With Errors (LWE)** and **AES encryption** to enhance data security. The system ensures robustness against quantum attacks while maintaining efficiency through symmetric encryption.

### 🔑 Why Double Encryption?
- **Quantum Security**: LWE offers resistance against quantum decryption attacks.
- **Speed and Efficiency**: AES ensures fast encryption for large datasets.
- **Layered Security**: Combining AES and LWE prevents single-point vulnerabilities.
- **Data Confidentiality**: Protects both textual and image data from unauthorized access.

---

## 🚀 Features

✅ **LWE-based Encryption**
   - A post-quantum encryption method leveraging the Learning With Errors problem to provide secure cryptographic operations.

✅ **AES Encryption**
   - Symmetric encryption method used to enhance security and efficiency.

✅ **Hybrid Security Model**
   - Combination of classical and post-quantum encryption provides enhanced security.

✅ **Image & Text Encryption**
   - Encrypts and reconstructs images securely using both AES and LWE encryption.
   - Securely encrypts and decrypts textual data to ensure confidentiality.

✅ **User Interface**
   - UI implemented using Qt framework for ease of use.

✅ **Cross-Platform Compatibility**
   - Can be executed on Linux, macOS, and Windows.

✅ **Efficient Key Management**
   - Secure handling of cryptographic keys to prevent unauthorized access.

✅ **Integrity Checks**
   - Ensures that decrypted data remains unaltered from the original input.

---

## 📂 Project Structure

```
Double-Encryption-LWE/
│── AESCipher.py              # AES encryption module
│── lwe.py                    # Learning With Errors encryption module
│── Encrypter.py              # Handles encryption process
│── Decrypter.py              # Handles decryption process
│── main.py                   # Main execution file
│── cipher.txt                # Encrypted text output
│── cipher_aes.txt            # AES-encrypted output
│── reconstructed_image.png   # Decrypted image output
│── ui.ui                     # UI configuration file (Qt based)
│── README.md                 # Project documentation
│── requirements.txt          # List of dependencies
│── tests/                    # Unit tests for encryption and decryption
│── docs/                     # Additional documentation files
│── samples/                  # Sample encrypted/decrypted files
│── keys/                     # Directory for storing encryption keys securely
```

---

## 🔧 Installation

Before running the project, install the required dependencies:

```sh
pip install -r requirements.txt
```

---

## 🏃 How to Run

1. **Encrypt a Text File**
```sh
python Encrypter.py --input input.txt --output cipher.txt --method lwe
```

2. **Decrypt a Text File**
```sh
python Decrypter.py --input cipher.txt --output output.txt --method lwe
```

3. **Encrypt an Image**
```sh
python Encrypter.py --input image.png --output cipher_image.dat --method aes
```

4. **Decrypt an Image**
```sh
python Decrypter.py --input cipher_image.dat --output decrypted_image.png --method aes
```

5. **Launch the UI**
```sh
python main.py
```

---

## 🔒 Encryption Mechanism

### 🔹 **AES Encryption:**
   - Uses a symmetric key to encrypt data securely.
   - Ensures fast and efficient encryption.
   - Commonly used for encrypting images and large datasets.

### 🔹 **LWE Encryption:**
   - Provides a post-quantum cryptographic layer.
   - Protects against attacks leveraging quantum computing.
   - More computationally intensive than AES but ensures long-term security.

### 🔹 **Hybrid Model:**
   - AES ensures fast encryption, while LWE enhances quantum security.
   - Users can choose between AES, LWE, or a combination of both.

---

## 📊 Testing
To ensure that the encryption and decryption functions work as expected, unit tests are available. Run the following command:

```sh
python -m unittest discover tests/
```

---

## 📈 Example Output

```
Encrypting file: input.txt using LWE...
Encryption complete. Output: cipher.txt
Decrypting file: cipher.txt...
Decryption complete. Output: output.txt
```

---

## 🛡️ Security Considerations

- **Key Storage:** Ensure encryption keys are stored securely in the `keys/` directory.
- **Avoid Reusing Keys:** Using the same key multiple times reduces security.
- **Quantum Security:** LWE encryption protects against future quantum attacks.
- **Performance Trade-offs:** AES is fast but less secure than LWE, which is computationally expensive.
- **Hash Validation:** Implement hash integrity checks for encrypted files.

---

## 🛠️ Contribution Guidelines

We welcome contributions to improve this project. To contribute:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ✉️ Contact
For any questions, reach out to:
- **Vennela Kothakonda** - Developer & Researcher

---

## 📚 Future Enhancements

🔹 **Enhance UI for better encryption visualization.**  
🔹 **Optimize LWE encryption speed using parallel processing.**  
🔹 **Develop an Android/iOS app for mobile encryption needs.**  
🔹 **Integrate cloud storage encryption and decryption features.**
