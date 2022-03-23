from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysecretkey' #used so session cookies can be encrypted
@app.route("/")
@app.route("/<name>")
def index(name):
    if name:
        return "Welcome " + name
    else:
        return "Hello everyone"

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host,port,debug=True)
