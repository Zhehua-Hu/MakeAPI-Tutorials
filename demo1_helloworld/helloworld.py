#!newpy/bin/python
# coding=utf-8
"""

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	# return "Hello, World!"
    return "<h1 style='color:black'>Hello, World!</h1>"


if __name__ == '__main__':
	app.run(debug=True)