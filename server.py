#!/usr/bin/env python
from operator import itemgetter
from flask import Flask, redirect, url_for, render_template, send_from_directory, request, send_file
from parser import parser


app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET','POST'])
def input():
    if request.method == "POST":
        texto = request.form['texto']
        lista = parser(texto)
        output =  '\n'.join(map(str, lista))
        print(output)
        return render_template("input.html", title = 'Index', t=output,i=texto)
    if request.method == "GET":
        texto = ''
        output = ''
        return render_template("input.html", title = 'Index', t=output, i=texto)

if __name__ == '__main__':
    app.run(debug=True)