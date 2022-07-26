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

def get_user_info(rollno):
    f = open("./data/user_info.bin", "rb")
    content = dict(pickle.load(f))
    f.close()
    return content[str(rollno)]

init()