
# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# @app.route("/hello")
# def hello():
#     return "<h1>Hello World!!</h1>"

# @app.route("/about")
# def about():
#     return "<h1>About World!!</h1>"
    
# if __name__ =='__main__':
#     app.run(debug=True)

import sqlite3
conn=sqlite3.connect('em.db')