'''
 _            __   __          _          _
| |           \ \ / /         | |        (_)
| |__  _   _   \ V /__ _ _ __ | |     ___ _
| '_ \| | | |   \ // _` | '_ \| |    / _ \ |
| |_) | |_| |   | | (_| | | | | |___|  __/ |
|_.__/ \__, |   \_/\__,_|_| |_\_____/\___|_|
       __/ |
      |___/
@FileName   : show.py
@Descript   : 
@Version    : 1.0
@Author     : YanLei
@CreateTm   : 2022/05/25 22:28:37
@Specific   : 
'''
from flask import Flask, request, Blueprint, render_template
from UseSqlite import InsertQuery, RiskQuery
from datetime import datetime
from PIL import Image

show_bp = Blueprint(
    'site',
    __name__,
)


def make_html_paragraph(s):
    if s.strip() == '':
        return ''
    lst = s.split(',')
    picture_path = lst[2].strip()
    picture_name = lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'jpeg')
    result = '<p>'
    result += '<i>%s</i><br/>' % (lst[0])
    result += '<i>%s</i><br/>' % (lst[1])
    result += '<a href="%s"><img src="./static/figure/%s"alt="风景图"></a>' % (
        picture_path, picture_name)
    return result+'</p>'


@show_bp.route('/show')
def show():
    rq = RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    record = '<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record += '%s' % (make_html_paragraph(r))
    return record+'</table>\n'
