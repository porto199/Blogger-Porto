from __main__ import app
from imports.imports import *
from imports.form_class import *
from imports.db_query import *

SECRET_KEY = '1234567'
app.config['SECRET_KEY'] = SECRET_KEY

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWD']  = '1234'
app.config['MYSQL_DB'] = 'users'
mysql = MySQL(app)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     login = LoginForm()
#     reset = ResetPwdForm()
#     register = RegisterForm()
#     active_modal = None  # Para manter o controle do modal ativo

#     if login.validate_on_submit():
#         email = login.name.data
#         pwd = login.pwd.data
#         result = busca_users(email)
#         if result:
#             u_id = result[0][0]
#             u_user = result[0][1]
#             u_email = result[0][2]
#             login.name.data = ''
#             print(u_id, u_user, u_email)
#             return redirect(url_for('user_page', u_id=u_id, u_user=u_user, u_email=u_email))
#         else:
#             flash(f'User {email} not found!', 'danger')
#         active_modal = 'loginModal'

#     if reset.validate_on_submit():
#         email = reset.email.data
#         pwd = reset.pwd.data
#         pwd_2 = reset.pwd_2.data
#         if pwd == pwd_2:
#             print(f'Email: {email} - Passwd: {pwd} - Passwd_2: {pwd_2}')
#             flash('Password reset requested!', 'success')
#             active_modal = 'resetModal'
#         else:
#             flash('Passwords not match!', 'danger')
#         active_modal = 'resetModal'

#     if register.validate_on_submit():
#         name = register.name.data
#         user = register.user.data
#         email = register.email.data
#         pwd = register.pwd.data
#         pwd_2 = register.pwd_2.data
#         result = busca_users(email)
#         if result:
#             u_id = result[0][0]
#             u_user = result[0][1]
#             u_email = result[0][2]
#         if pwd == pwd_2:
#             print(f'Name: {name} - User: {user} - Email: {email} - Passwd: {pwd} - Passwd_2: {pwd_2}')
#             flash('Registration successful!', 'success')
#             active_modal = 'registerModal'
#         else:
#             flash('Registration failled! Wrong Password', 'danger')
#         active_modal = 'registerModal'

#     return render_template('home.html', login=login, reset=reset, register=register, active_modal=active_modal)

@app.route('/', methods=['GET', 'POST'])
def home():
    login = LoginForm()
    reset = ResetPwdForm()
    register = RegisterForm()
    active_modal = None  # Para manter o controle do modal ativo

    if login.validate_on_submit():
        email = login.name.data
        pwd = login.pwd.data
        result = busca_users(email)
        if result:
            u_id = result[0][0]
            u_user = result[0][1]
            u_email = result[0][2]
            login.name.data = ''
            return redirect(url_for('user_page', u_id=u_id, u_user=u_user, u_email=u_email))
        else:
            flash(f'User {email} not found!', 'login-danger')
            active_modal = 'loginModal'

    if reset.validate_on_submit():
        email = reset.email.data
        pwd = reset.pwd.data
        pwd_2 = reset.pwd_2.data
        if pwd == pwd_2:
            flash('Password reset requested!', 'reset-success')
        else:
            flash('Passwords not match!', 'reset-danger')
        active_modal = 'resetModal'

    if register.validate_on_submit():
        name = register.name.data
        user = register.user.data
        email = register.email.data
        pwd = register.pwd.data
        pwd_2 = register.pwd_2.data
        if pwd == pwd_2:
            cadastra_user(name, user, email, pwd)
            flash('Registration successful!', 'register-success')
        else:
            flash('Registration failed! Wrong Password', 'register-danger')
        active_modal = 'registerModal'

    return render_template('home.html', login=login, reset=reset, register=register, active_modal=active_modal)