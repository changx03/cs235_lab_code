"""
The code is written for COMPSCI235 Lab 3 HTML and CSS. 
You do not need to alter this Python file in Lab 3.

Author: Luke Change (xcha011@aucklanduni.ac.nz) 
Date: 23/07/2022
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def show_main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
