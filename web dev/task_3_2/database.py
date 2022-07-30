from webbrowser import get
from cryptography.fernet import Fernet
import pickle
import csv


def init():
    f = open("./data/login_info.bin", "wb")
    content = {
        "106121116":encry("madhumitha"),
        "110121111":encry("password")
    }
    pickle.dump(content, f)
    f.close()
    f = open("./data/user_info.bin", "wb")
    content = {
        "106121116" : {
            "name" : "sanjiv kannaa jeganathan",
            "gender" : "MALE",
            "programme" : "B.TECH",
            "branch" : "CSE",
            "section" : "B",
            "username" : "sanjiv_kannaa_jeganathan",
            "hostel" : "zircon b"
        },
        "110121111" : {
            "name" : "madhumitha t e",
            "gender" : "FEMALE",
            "programme" : "B.TECH",
            "branch" : "ICE",
            "section" : "A",
            "username" : "madhuxmitha",
            "hostel" : "opal C"
        }
    }
    pickle.dump(content, f)
    f.close()

def encry(data):
    file = "./data/encryption_key.bin"
    f = open(file, "rb")
    key = pickle.load(f)
    f.close()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decry(data):
    file = "./data/encryption_key.bin"
    f = open(file, "rb")
    key = pickle.load(f)
    f.close()
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()


def put_login_info(rollno, password):
    try:
        f = open("./data/login_info.bin", "rb")
        content = dict(pickle.load(f))
        f.close()
        content[str(rollno)] = encry(password)
        f = open("./data/login_info.bin", "wb")
        pickle.dump(content, f)
        f.close()
    except:
        f = open("./data/login_info.bin", "wb")
        content = {str(rollno) : encry(password)}
        pickle.dump(content, f)
        f.close()


def get_login_info():
    f = open("./data/login_info.bin", "rb")
    content = dict(pickle.load(f))
    f.close()
    content2 = {}
    for i in content:
        content2[i] = decry(content[i])
    return content2


def get_all_user_info():
    f = open("./data/user_info.bin", "rb")
    content = dict(pickle.load(f))
    f.close()
    return content

def put_user_info(name, rollno, gender, programme, branch, section, username, hostel):
    f = open("./data/user_info.bin", "rb")
    content = dict(pickle.load(f))
    f.close()
    content[str(rollno)] = {
        "name" : name,
        "gender" : gender,
        "programme" : programme,
        "branch" : branch,
        "section" : section,
        "username" : username,
        "hostel" : hostel
    }
    f = open("./data/user_info.bin", "wb")
    pickle.dump(content, f)
    f.close()

def get_user_info(rollno):
    f = open("./data/user_info.bin", "rb")
    content = dict(pickle.load(f))
    f.close()
    return content[str(rollno)]

def check_signup(name, rollno, password1, password2, gender, programme, branch, section, username, hostel):
    login_content = get_login_info()
    user_content = get_all_user_info()
    if password1 != password2:
        return [False, "passwords are not same"]
    for i in user_content.keys():
        if user_content[i]["username"] == username:
            return [False, "username already exists"]
    if rollno in login_content.keys():
        return [False, "password already exists"]
    try:
        put_login_info(rollno, password1)
        put_user_info(name, rollno, gender, programme, branch, section, username, hostel)
        return [True, True]
    except:
        return [False, "error uploading"]

