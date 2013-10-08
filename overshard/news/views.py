from flask import render_template,redirect,url_for,request
from overshard.news.forms import WriteForm
from overshard.news.models import Content
from overshard.extensions import db
def index():
	content=get_all_posts()
	return render_template("news/index.html",content=content)


def news():
	pass
	

def write():
	form=WriteForm()
	if request.method=="POST":
		content=form.content.data
		db.session.add(Content(content))
		db.session.commit()
		return redirect(url_for("news.index"))
	return render_template("news/write.html",form=form)




def delete(id):
	db.session.delete(Content.query.get(id))
	db.session.commit()
	return redirect(url_for("news.index"))


def get_all_posts():
	posts=Content.query.order_by("id desc").all()
	return posts 


