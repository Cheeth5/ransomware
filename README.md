Ransomware Project
Overview

This project demonstrates a basic ransomware implementation in Python, designed for educational and experimental purposes only. It encrypts files in a specified directory using symmetric encryption and demands a password for decryption. The ransomware also includes features to notify the user via email upon encryption and to execute predefined actions upon exceeding incorrect decryption attempts.
Features

    File Encryption: Encrypts files in a specified directory using the Fernet symmetric encryption scheme from the cryptography library.
    Password Protection: Requires a password for file decryption, with a limited number of incorrect attempts allowed before triggering additional actions.
    Email Notification: Sends an email containing the decryption password upon successful encryption.
    System Lockdown: Executes system actions (shutdown or lock) upon exceeding the maximum allowed incorrect decryption attempts.
    Platform Compatibility: Designed to work on Linux, Windows, and macOS platforms.

Disclaimer

This ransomware implementation is for educational purposes only. It should not be used for malicious intent or deployed on systems without explicit permission. The author assumes no liability for misuse or damage caused by this software.
Usage

    Clone the repository.
    Customize the encryption directory and password file path in ransomware.py.
    Run ransomware.py and follow on-screen instructions.
    Refer to the README file for further details and customization options.

Notes

    Ensure all usage complies with local laws and regulations.
    Use responsibly and ethically, respecting privacy and data security.


![Screenshot from 2024-07-17 17-34-00](https://github.com/user-attachments/assets/a899166a-3853-45d5-8cbe-f0e4cba4d166)

