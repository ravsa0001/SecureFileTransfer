from flask import Flask, request, jsonify, url_for
from pymongo import MongoClient
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
from cryptography.fernet import Fernet
import uuid

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017") 

ez = client["ez"]
users_data = ez["users_data"]
file_storage = ez["files_storage"]

app.config.from_pyfile('config.py')

mail = Mail(app)

@app.route("/")
def home():
    return "Hello there!"
        
        
@app.route("/signup_operation", methods = ["GET","POST"])
def signUpOp():
    if request.method == "POST":
        data = request.json  
        mail = data["email"]
        email = users_data.find_one({"email": mail})
        
        if email:
            return jsonify({"text": "email already exists"})
        else:
            if data["password"] == data["password2"]:
                users_data.insert_one({"username": data["username"], 
                                "email": data["email"], 
                                "password":data["password"], 
                                "user": data["user"],
                                "key": data["key"]})
            else:
                return jsonify({"text": "Passwords must be same"})         
            return jsonify({"text": "Regsitered Successfully" })
    return jsonify({"text": "Insert Data"})


s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def send_verification_email(all_info):
    email = all_info['email']
    token = s.dumps(all_info, salt="verificaion")
    msg = Message('Confirm Email', recipients=[email])
    link = url_for('verify', token=token, _external=True)
    msg.body = f'Your verification link is {link}'
    mail.send(msg)

@app.route("/signup_client", methods = ["GET", "POST"])
def signUpCL():
    if request.method == "POST":
        data = request.json
        # all_info = data["info"]
        send_verification_email(data)
        
        return jsonify({"message": "Verification link is sent to your Email"})
    
@app.route("/verify/<token>", methods=["GET", "POST"])
def verify(token):
    try:
        all_info = s.loads(token, salt="verificaion", max_age = 180)
        users_data.insert_one(all_info)
        
        return jsonify({"message": "You have Successfully Registered"})
    except SignatureExpired:
        return jsonify({"message": "Your token is expired"})




@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        temail = data["email"]
        
        email = users_data.find_one({"email": temail})
        
        passwod = data["password"]
        # return f"{passwod}"
        print(email)
        if email:
            confirm = email["password"]
            if passwod == confirm:
                return jsonify({"text":"Successfully loged In", 
                                "user": email["user"], 
                                "user_name": email["username"]})
            return jsonify({"text":"Incorrect Password"})
        return jsonify({"text":"Email doesn't exists"})
    
    
    
@app.route("/upload", methods=["GET", "POST"])
def upload():

    data = request.json
    file = data["file_name"]

    uploaded_file = data["uploaded_file"]
    # filedata = bytes(uploaded_file, "utf-8")
    
    user_name = data["user_name"]
    userdata = users_data.find_one({"username": user_name})
    # print(userdata, user_name)
    keykey = userdata["key"]
    byte_key = bytes(keykey, "utf-8")
    fernet = Fernet(byte_key)
    enfile = fernet.encrypt(uploaded_file.encode())
    print("********************************88")
    print(type(enfile))
    
    
    unique_name = str(uuid.uuid4())[:8]+'.txt'
    path = "/home/vo1d/Desktop/VS_Code/ez/uploads/"
    file_path = f"{path}{unique_name}"
    with open(file_path, 'wb') as f:
        f.write(enfile)

    file_storage.insert_one({
        "file name": file, 
        "file data": file_path,
        "upuser": user_name,
        "key": keykey
        # "download key": unique_key,
    })
    return jsonify({"message": "File uploaded successfully"})




@app.route("/uploaded_files", methods = ["GET", "POST"])
def uploaded():
    data = request.json
    index = data["index"]
    name_list = []
    for files in file_storage.find():
        names = files["file name"]
        name_list.append(names)
        
    file_name = name_list[index]
    
    file_data = file_storage.find_one({"file name": file_name})
    # print("$$$$$$$$$$$$$$$$$$$$$$4")
    # print(file_data)
    path = file_data["file data"]
    with open(path, "rb") as f:
        filedata = f.read()
    keykey = file_data["key"]
    print(type(keykey))
    byte_key = bytes(keykey, "utf-8")
    print(type(byte_key))
    fernet = Fernet(byte_key)
    
    file_decrypt = fernet.decrypt(filedata).decode()
    return jsonify({"filedata": file_decrypt, "file_name": file_name})

    # for files in file_storage.find():
    #     file_name = files["file name"]
    #     path = files["file data"]
        
    #     with open(path, "rb") as f:
    #         filedata = f.load()
        
    #     keykey = files["key"]
    #     byte_key = bytes(keykey, "utf-8")
    #     fernet = Fernet(byte_key)
        
    #     file_decrypt = fernet.decrypt(filedata).decode()
        
    #     # file_ka_data = bytes(file_decrypt, "utf-8")
    #     return jsonify({"filedata": file_decrypt, "file_name": file_name})
        
        
 


if __name__ == "__main__":
    app.run(debug = True)