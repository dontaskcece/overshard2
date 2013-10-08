from flask import Blueprint ,render_template
errantdb = Blueprint("errantdb",__name__)
from overshard.errantdb import views


errantdb.add_url_rule('/', view_func=views.index)


