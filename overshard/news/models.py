from overshard.extensions import db

class Content(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.String(1000))
	def __init__(self,content):
		self.content=content


