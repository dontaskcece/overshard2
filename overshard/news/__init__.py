from flask import Blueprint ,render_template
news = Blueprint("news",__name__)
from overshard.news import views


news.add_url_rule('/', view_func=views.index)

news.add_url_rule("/write",view_func=views.write,methods=['GET', 'POST'])

news.add_url_rule("/del/<int:id>",view_func=views.delete)

