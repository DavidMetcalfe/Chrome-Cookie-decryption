# Chrome Cookie decryption

## Description

This tool will fetch and decrypt the local database that cookies are stored in by Chrome. Currently only built to work for Windows, and not all OS versions. 

## Installation

Open a Command Prompt window in the script's directory, and paste the following to install the required modules:

**pip install -r requirements.txt**

## Usage

1. Open a Command prompt in the script's directory.
2. Type "python application.py"
3. Hit Enter
3. Review the `export.txt` file created in the same directory.

## Notes
Creation and expiration dates of cookies are in UTC and not formatted into readable stamps.
