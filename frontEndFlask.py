import os
from flask import Flask, Response, request, redirect, url_for, render_template
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/ping_test', methods=['GET', 'POST'])
def ping_test():
    google = False
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('ping.html', google=google)

@app.route('/do_ping_test', methods=['GET', 'POST'])
def do_ping_test():
    if request.method == 'POST':
        google = True if os.system("ping -c 1 google.com") == 0 else False
        return render_template('ping.html', google=google)
    return render_template('ping.html')
