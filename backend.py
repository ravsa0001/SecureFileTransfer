from flask import Flask, request, jsonify, url_for
from pymongo import MongoClient
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
import uuid
import base64

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
                                "user": data["user"]})
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
                return jsonify({"text":"Successfully loged In", "user": email["user"]})
            return jsonify({"text":"Incorrect Password"})
        return jsonify({"text":"Email doesn't exists"})
    
    
    
@app.route("/upload", methods=["GET", "POST"])
def upload():

    data = request.json
    file = data["file_name"]
    
    path = "/home/vo1d/Desktop/VS_Code/ez/uploads/"
    uploaded_file = data["uploaded_file"]

    data = bytes(uploaded_file, "utf-8")
    file_path = f"{path}{file}"
    
    with open(file_path, 'wb') as f:
        f.write(data)

    unique_key = str(uuid.uuid4())[:8]
    file_storage.insert_one({
        "file name": file, 
        "file link": file_path,
        "download key": unique_key,
    })
    return jsonify({"message": "File uploaded successfully"})
        
 

if __name__ == "__main__":
    app.run(debug = True)
    
    
    
