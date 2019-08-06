import os
import json
from flask import Flask,abort,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/study'
db = SQLAlchemy(app)

class File(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	categroy_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	content = db.Column(db.Text)

	def __repr__(self):
		return "<User %r>" % self.title

class Category(db.Model):
	id = db.Column(db.Integer,primary_key=True,)
	name = db.Column(db.String(80))

	def __repr__(self):
		return "<User %r>"% self.name	

@app.route('/')
def index():
	# 显示文章名称的列表
	# 页面中需要显示所有文章的标题（title）列表，此外每个标题都需要使用 '<a href=></a>'链接到对应的文章内容页面
	titles = []
	ids = []
	for f in session.query(File).all():
		titles.append(f.title)
		ids.append(f.id)
	return render_template('index.html',titles=titles,ids=ids)

@app.route('/files/<file_id>')
def file(filename):
	# file_id 为 File 表中的文章 ID
	try:
		f=session.query(File).filter(File.id==file_id).first()
		return render_template('file.html',datas=f)
	except:
		abort(404)
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename="helloshiyanlou"的时候显示helloshiyanlou.json中的内容
    # 如果 filename 不存在，则显示包含字符串 "shiyanlou 404"404 错误页面

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404

if __name__=="__main__":
    app.run()
