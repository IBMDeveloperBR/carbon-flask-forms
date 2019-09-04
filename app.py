import gunicorn_config
import validators as vld

from os import urandom, getenv
import datetime as dt

from flask import Flask, render_template, request, url_for, redirect
from flask_sslify import SSLify
from flask_wtf.csrf import CSRFProtect


# Flask config
app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(16)
app.config['WTF_CSRF_SECRET_KEY'] = urandom(16)
sslify = SSLify(app) # Comment out this line if you are running flask locally, in development mode
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def root():
    """ Example usage of `validators.py`
    email_error = False
    email_error_msg = ''
    name_error = False
    name_error_msg = ''
    cpf_error = False
    cpf_error_msg = ''
    """
    now = dt.datetime.utcnow() - dt.timedelta(hours=3)
    now_str = dt.datetime.strftime(now, "%H:%M:%S - %d/%m/%Y")
    if request.method == 'POST':
        # Capture User Input
        field1 = request.form['field1']
        field2 = request.form['field2']
        field3 = request.form['field3']
        """ Example usage of `validators.py`
        # Capturing user inputs
        email = vld.drophtmltags(vld.dropsqlsyntax(request.form['usr_email'])).lower()
        name = vld.drophtmltags(vld.dropsqlsyntax(request.form['usr_name'])).title()
        cpf = vld.drophtmltags(vld.dropsqlsyntax(request.form['usr_cpf']))
        # Validating user inputs
        if vld.validate_email(email) == False:
            email_error = True
            email_error_msg = 'Falha na verificação de e-mail.'
        if vld.validate_name(name) == False:
            name_error = True
            name_error_msg = 'Sintaxe de nome inválida.'
        if vld.validate_cpf(cpf) == False:
            cpf_error = True
            cpf_error_msg = 'CPF inválido.'
        if email_error==False and name_error==False and cpf_error==False:
            return render_template('result.html', now_str=now_str, 
                field1=field1, field2=field2, field3=field3
            )
        """
        return render_template('result.html', now_str=now_str, 
           field1=field1, field2=field2, field3=field3
        )
    else:
        """ Example usage of `validators.py`
        return render_template('form.html', 
            email_error=email_error, email_error_msg=email_error_msg,
            cpf_error=cpf_error, cpf_error_msg=cpf_error_msg,
            name_error=name_error, name_error_msg=name_error_msg,
            timestamp=now_str
        )
        """
        return render_template('form.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=gunicorn_config.PORT, debug=False)