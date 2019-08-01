import os
import json
from flask import Flask,abort,render_template

app = Flask(__name__)

@app.route('/')
def index():
    files_path ="/home/shiyanlou/files/"
    files_list = os.listdir(files_path) 
    titles = []
    for the_file in files_list:
        file_name = os.path.join(files_path,the_file)
        with open(file_name,'r') as f :
            data = json.load(f)
            titles.append(data['title']) 
    return render_template('index.html',titles=titles)
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有json文件中的 title 信息列表

@app.route('/files/<filename>')
def file(filename):
    the_file_path = os.path.join("/home/shiyanlou/files",filename+'.json')
    try:
        with open(the_file_path,"r") as f:
            datas = json.load(f)
        return render_template('file.html',datas=datas)
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
