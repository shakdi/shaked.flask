from flask import Flask, redirect, url_for

app = Flask(_name_)

@app.route('/')
def MyPage():
    return "welcome to my page"

@app.route('/HomePage')
def HomePage():
    return redirect(url_for('MyPage'))

@app.route('/Home')
def Home():
    return redirect('/')

if _name_ == '_main_':
    app.run()
