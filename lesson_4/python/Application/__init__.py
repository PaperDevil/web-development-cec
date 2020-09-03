from flask import Flask, redirect, flash, render_template, request

from Application.forms import UserInput

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "some string"

    @app.route('/')
    def index():
        return 'Hello World!'

    # Нативыне веб формы

    @app.route('/native-form', methods=['GET', 'POST'])
    def native_form():
        if request.method == 'POST':
            flash("Активация пользователя {} с почтовым адресом {}".format(
                request.form['username'],
                request.form['email']
            ))
            return redirect('/')
        else:
            return render_template('native_form.jinja2', bootstrap=True)

    # Flask WTF

    @app.route('/wtf-form', methods=['GET', 'POST'])
    def wtf_form():
        form = UserInput(request.form)
        if request.method == 'POST':
            flash(f'Активация пользователя {form.username.data} с почтовым адресом {form.email.data}')
            return redirect('/')
        return render_template('wtf_form.jinja2', bootstrap=True, form=form)

    return app
