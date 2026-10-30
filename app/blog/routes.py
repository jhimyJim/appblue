from flask import Blueprint, render_template

blog_bp = Blueprint(
    'blog',
    __name__,
    template_folder='templates'
)

@blog_bp.route('/entrada/<int:id>')
def entrada(id):

    titulo = "Mi primera entrada del blog"

    return render_template('entrada.html', titulo=titulo)