def create_app(config_filename):
	from flask import Flask
	app = Flask(__name__)
	app.config.from_pyfile(config_filename)
	from overshard.extensions import db
	db.init_app(app)
	from overshard.frontend import frontend
	from overshard.news import news
	from overshard.errantdb import errantdb
	app.register_blueprint(frontend)
	app.register_blueprint(news,url_prefix="/news")
	app.register_blueprint(errantdb,url_prefix="/errantdb")
	return app








