'''
Author: y3s
LastEditors: y3s
email: y3sss@foxmail.com
Date: 2022-05-20 11:57:37
LastEditTime: 2022-05-20 15:24:39
motto: keep learning makes u strong
'''
#encoding = 'utf-8'
from flask import Blueprint, jsonify
from sympy import true
from UseSqlite import RiskQuery
from datetime import date, datetime
import os
import json
api = Blueprint(
    'site',
    __name__,
)

@api.route('/api/json')
def get_json():
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    # result='<p>'
    i = 1
    key = ('id', 'date', 'Size', 'description')
    l = []
    for r in rq.format_results().split('\n\n'):
        if r.strip()=='':
            return ''
        lst=r.split(',')
        # l.append(lst)
        path = "E:\\PhotoString_by_ChenXintao\\"+lst[2].strip(' ./')
        true_path = path.replace('/', '\\')
        fileSize = os.path.getsize(true_path)
        fileSize = fileSize/(1024 * 1024)
        # str1 = [i, lst[0], fileSize, lst[1].strip()]
        str = {"id": i, "date": lst[0], "Size": fileSize, "description": lst[1]}
        l.append(str)
        i += 1
    # d = [dict(zip(key,value) for value in l)]
    # res_json = json.dumps(i for i in l)
    json1 = jsonify(l) 
    print(json1)
    return json1
