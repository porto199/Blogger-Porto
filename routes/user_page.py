from imports.imports import *
from __main__ import app
from imports.form_class import *
from imports.db_query import *

SECRET_KEY = '12345678'
app.config[SECRET_KEY] = SECRET_KEY

IMAGE_UPLOAD_FOLDER = 'C:/Users/Porto/Documents/MEGA/Dev/Python/Flask/Blogger-Porto/static/image'  # Substitua pelo caminho real do diretório de upload de imagens
VIDEO_UPLOAD_FOLDER = 'C:/Users/Porto/Documents/MEGA/Dev/Python/Flask/Blogger-Porto/static/video'  # Substitua pelo caminho real do diretório de upload de vídeos
THUMBNAIL_UPLOAD_FOLDER = 'C:/Users/Porto/Documents/MEGA/Dev/Python/Flask/Blogger-Porto/static/thumbnails'
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov'}


app.config['THUMBNAIL_UPLOAD_FOLDER'] = THUMBNAIL_UPLOAD_FOLDER
app.config['IMAGE_UPLOAD_FOLDER'] = IMAGE_UPLOAD_FOLDER
app.config['VIDEO_UPLOAD_FOLDER'] = VIDEO_UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

def save_thumbnail(image_path, thumbnail_path, thumbnail_size=(100, 100)):
    try:
        image = Image.open(image_path)
        image.thumbnail(thumbnail_size)
        image.save(thumbnail_path)
        return True
    except Exception as e:
        print(f"Erro ao salvar miniatura: {e}")
        return False

def allowed_image_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

def allowed_video_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


@app.route('/user_page', methods=['GET', 'POST'])
def user_page():
    busca_posts = busca_users_blog()
    u_id = request.args.get('u_id')
    u_user = request.args.get('u_user')
    u_email = request.args.get('u_email')
    pesquisa = request.form.get('pesquisa')

    if request.method == 'POST' and pesquisa:
        resultados = busca_post(pesquisa)
        if not resultados:
            flash('Sua busca não retornou resultados!')
        return render_template('search_results.html', resultados=resultados)
    
    blog = Blog_Post()
    if blog.validate_on_submit():
        title = blog.title.data
        theme = blog.theme.data
        content = blog.content.data
        u_id = request.form.get('u_id')
        u_user = request.form.get('u_user')
        print(title, u_user, theme, content, u_id)

        # Processar arquivos de imagens
        image_filenames = []
        if 'images' in request.files:
            images = request.files.getlist('images')
            for image in images:
                if image and allowed_image_file(image.filename):
                    image_filename = secure_filename(image.filename)
                    image.save(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], image_filename))
                    image_filenames.append(image_filename)
                    
                    # Salvar miniatura
                    thumbnail_filename = 'thumb_' + secure_filename(image.filename)
                    thumbnail_path = os.path.join(app.config['THUMBNAIL_UPLOAD_FOLDER'], thumbnail_filename)
                    save_thumbnail(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], image_filename), thumbnail_path)
        
        # Processar arquivos de vídeos
        video_filenames = []
        if 'videos' in request.files:
            videos = request.files.getlist('videos')
            for video in videos:
                if video and allowed_video_file(video.filename):
                    video_filename = secure_filename(video.filename)
                    video.save(os.path.join(app.config['VIDEO_UPLOAD_FOLDER'], video_filename))
                    video_filenames.append(video_filename)

        cria_post(title, u_user, theme, content, u_id, image_filenames, video_filenames)

    return render_template('content_user.html', id=u_id, user=u_user, email=u_email, blog=blog, busca_posts=busca_posts, image_filenames=image_filenames, video_filenames=video_filenames)