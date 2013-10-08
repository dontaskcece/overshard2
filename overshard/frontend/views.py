from flask import render_template,request,session,redirect,url_for
from overshard.frontend.forms import MyForm



def index():
	return render_template("frontend/index.html")


def about():
	return render_template("frontend/about.html")

def login():
	form=MyForm()
	if request.method=="POST":
		username=form.username.data 
		session["username"]=username
		session["logged"]=True
		return redirect(url_for("frontend.index"))
	return render_template("frontend/login.html",form=form)



def logout():
	session.pop("username",None)
	session["logged"]=False
	return redirect(url_for("frontend.index"))