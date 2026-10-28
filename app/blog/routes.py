
from flask import Blueprint, render_template

blog_bp = Blueprint(
    'blog',
    __name__,
    url_prefix='/entrada',
    template_folder='templates'
)

@blog_bp.route('/')
def index():
    return render_template('blog.html')


@blog_bp.route('/<int:id>')
def mostrar_entrada(id):
    entradas = {
        1: 'Mi primera entrada',
        2: 'Aprendiendo Flask'
    }

    titulo = entradas.get(id)

    if titulo is None:
        return 'Entrada no encontrada', 404

    return render_template('blog.html', titulo=titulo)
