from imports.imports import *
from imports.db_query import *
from __main__ import app

@app.route('/admin')
def admin():
    busca = busca_users_blog()
    return render_template('admin.html', busca=busca)