from sqlite3 import connect
from wsgiref.simple_server import make_server
from flask import Flask, jsonify, make_response, render_template, request, request_started
import database

app = Flask(__name__)




@app.route('/')
def function():
    if  request.cookies.get('loginstatus') == 'True':
        return 'feed for user : '+request.cookies.get('login_username')
        #return render_template('feed.html')
        # feed()
    else:
        return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/developer')
def developer_information():
    return render_template('developer.html')

@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login_validation():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        content = database.get_login_info()
        rollno = str(request.form.get('rollno'))
        password = str(request.form.get('password'))
        #print('\n\n\n\n{}\n\n{}\n\n\n\n'.format(len(rollno), len(password)))
        #return "username = {} password = {}".format(rollno, password)
        if content[rollno] == password:
            res = make_response(render_template('login_success.html'))
            username = database.get_user_info(rollno)['username']
            res.set_cookie('loginstatus', 'True')
            res.set_cookie('login_rollno', rollno)
            res.set_cookie('login_username', username)
            return res
        else:
            return make_response(render_template("login.html"))


@app.route('/logout', methods=["POST", "GET"])
def logout():
    if request.method == 'GET':
        res = make_response(render_template('login.html'))
        res.set_cookie('loginstatus', "false")
        res.set_cookie('login_rollno', '')
        res.set_cookie('login_username', '')
        return res

@app.route('/forgot_password', methods=["GET", "POST"])
def forgot_password():
    if request.method == "GET":
        pass
    else:
        pass


@app.route('/feed', methods=["GET"])
def feed():
    if  request.cookies.get('loginstatus') == 'True':
        return render_template('feed.html')
    else:
        return render_template('login.html')



'''
@app.route('/login_bypass', methods = ['POST', 'GET'])
def login_bypass():
    if True: #request.method == 'POST':
        user = 'True'   # request.form['login_status']
        resp = make_response(render_template('login_success.html'))
        resp.set_cookie('login_status', user)
        return resp
    return "cookie not found"
'''



   
if __name__ == '__main__':
    app.run()