import mysql.connector

def db_conect():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'users'
    )
    
def cadastra_user(name, user, email, pwd):
    db = db_conect()
    cursor = db.cursor()
    query = "insert into users (name, user, email, pwd) values (%s, %s, %s, %s);"
    values = (name, user, email, pwd)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    


def busca_todos_users():
    db = db_conect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    busca = cursor.fetchall()
    cursor.close()
    db.close()
    return busca


def busca_users(email):
    db = db_conect()
    cursor = db.cursor()
    cursor.execute("SELECT id, user, email FROM users WHERE email = '"+email+"'")
    busca = cursor.fetchall()
    cursor.close()
    db.close()
    return busca

def busca_users_blog():
    db = db_conect()
    cursor = db.cursor()
    cursor.execute("select u.id, u.name, u.email, b.title, b.author, b.theme, b.content from users as u join bpost as b on u.id = b.fk_users_id")
    busca_tudo = cursor.fetchall()
    cursor.close()
    db.close()
    return busca_tudo

def busca_post(pesquisa):
    db = db_conect()
    cursor = db.cursor()
    cursor.execute(f"select u.id, u.name, u.email, b.title, b.author, b.theme, b.content from users as u join bpost as b on u.id = b.fk_users_id where u.name like '%{pesquisa}%'or b.title like '%{pesquisa}%' or b.author like '%{pesquisa}%' or b.theme like '%{pesquisa}%' or b.content like '%{pesquisa}%'")
    pesquisa_posts = cursor.fetchall()
    cursor.close()
    db.close()
    return pesquisa_posts

def cria_post(title, user, theme, content, id, image_paths=None, video_paths=None):
    db = db_conect()
    cursor = db.cursor()
    # Armazena os caminhos das imagens e vídeos como strings separadas por vírgulas
    image_paths_str = ','.join(image_paths) if image_paths else None
    video_paths_str = ','.join(video_paths) if video_paths else None
    query = """
        INSERT INTO bpost (title, author, theme, content, fk_users_id, image_path, video_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    values = (title, user, theme, content, id, image_paths_str, video_paths_str)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()

    