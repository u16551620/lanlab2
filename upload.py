# -*- coding = utf-8 -*-
# @Time : 2022/5/22 21:20
# @Author : onion
# @File : upload.py
# @Software : PyCharm

from flask import Blueprint, request

import Lab
from UseSqlite import InsertQuery
from datetime import datetime

# 创建一个蓝图的对象
upload = Blueprint('upload', __name__)


# 利用蓝图对象定义具体的视图函数
@upload.route("/upload", methods=['POST', 'GET'])
def uploads():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        time_str = datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename = time_str + '.jpg'
        uploaded_file.save('./static/upload/' + new_filename)
        time_info = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        description = request.form['description']
        path = './static/upload/' + new_filename
        iq = InsertQuery('./static/RiskDB.db')
        iq.instructions("INSERT INTO photo Values('%s','%s','%s','%s')" % (time_info, description, path, new_filename))
        iq.do()
        return '<p>You have uploaded %s.<br/> <a href="/upload">Return</a>.' % uploaded_file.filename
    else:
        page = '''<form action="/upload"method="post"enctype="multipart/form-data">
        <input type="file"name="file"><input name="description"><input type="submit"value="Upload"></form>'''
        page += Lab.get_database_photos()
        return page
