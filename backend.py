from flask import Flask, render_template, request, flash, jsonify, url_for, session, redirect, send_file
from pymongo import MongoClient
import uuid

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017") 

ez = client["ez"]
users_data = ez["users_data"]
file_storage = ez["files_ storage"]

@app.route("/")
def home():
    return "Hello there!"
        
        
@app.route("/signup", methods = ["GET","POST"])
def index():
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
    
    
    
@app.route("/uploads", methods=["GET", "POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "File type not selected"})

    file = request.files["file"]
    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    data = request.json()
    file_name = data["file"]

    # file.save("uploads" + '/' + file.filename)
    # return jsonify({"message": "HOTx"}) 

    unique_key = str(uuid.uuid4())[:8]  
    file_link =  file.save("uploads" + '/' + file.filename)
    file_storage.insert_one({
        "file name": file_name, 
        "file link": file_link,
        "download key": unique_key,
    })
    return jsonify({"message": "File uploaded successfully"})
    

    # db = get_db()
    # cursor = db.cursor()
    # cursor.execute("INSERT INTO files (filename, file_link, download_key) VALUES (?, ?, ?)", (file.filename, os.path.join(UPLOAD_FOLDER, file.filename), unique_key))
    # db.commit()
    # cursor.close()

    # file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    # return jsonify({'message': 'File uploaded successfully', 'download_key': unique_key}), 200
    
    
     
@app.route("/uploaded-files", methods=["GET", "POST"])
def uploaded():

    # if file:
    #     files = file_storage.find_one(file)
    #     file_path = files["download key"]
    #     return send_file(file_path, as_attachment = True)
    # return jsonify({"message": "File not found"})
    pass
         
        
 

if __name__ == "__main__":
    app.run(debug = True)
    
    
    
