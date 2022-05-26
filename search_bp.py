from flask import Flask, request, Blueprint, render_template
from UseSqlite import InsertQuery, RiskQuery
from datetime import datetime
from PIL import Image

search_bp = Blueprint('site',__name__,)


@search_bp.route('/search')
def searchh():
    re="Christ Park"
    rq = RiskQuery('./static/RiskDB.db')

    #rq.instructions("SELECT * FROM photo where description='Christ Park'")

    rq.instructions("SELECT * FROM photo where description='%s'"%(re))
    rq.do()

    record = '<p>search photo</p>'
    for r in rq.format_results().split('\n\n'):
        record += '%s' % (make_html_paragraph(r))
    return record+'</table>\n'

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