from flask import Flask, redirect, url_for, render_template
from pivot import getSales
app = Flask(__name__)

@app.route('/')
def index():
  return redirect(url_for('hello'))

@app.route('/hello')
def hello():
  return getSales()

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404