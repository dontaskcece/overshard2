from flask import Blueprint ,render_template
frontend = Blueprint("frontend",__name__)
from overshard.frontend import views


frontend.add_url_rule('/', view_func=views.index)

frontend.add_url_rule('/about', view_func=views.about)


frontend.add_url_rule('/login', view_func=views.login,methods=['GET', 'POST'])

frontend.add_url_rule('/logout', view_func=views.logout)