from flask import Flask, render_template, request
from app import app
from . import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = forms.ContactForm()

    if request.method == 'POST':
        return 'Form posted'
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.context_processor
def inject_variables():
    return dict(
        user={'name': 'Damian'},
    )
