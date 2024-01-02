## _Secure File Vault_

Developed a web application with Streamlit and Flask, allowing operational users to securely upload files that are encrypted using symmetric-key encryption. 
Users, categorized as either operators or clients, their data is stored in MongoDB(database). Client users can subsequently download the encrypted files,
ensuring a seamless and secure data exchange.


## Prerequisites
- python(3.x)
- pip(package manager)

## Installation
**clone the repo**
```sh
git clone https://github.com/ravsa0001/SecureFileTransfer.git
cd SecureFileTransfer
```

**Install the dependencies**
``` sh
pip install -r requirements.txt
```

After that you need to run the code given below to run the web application smoothly
``` sh
streamlit run main.py
```
