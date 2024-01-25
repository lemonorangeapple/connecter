import dns.resolver
from flask import *
dns.resolver.name = ['1.0.0.1', '8.8.4.4']
app = Flask(__name__)

@app.route('/')
def index():
    add = request.values.get('get')
    add = add.split(';')
    if add is None:
        return '200 OK'
    try:
        res = ''
        for i in add:
            res += str(i + ' ' + dns.resolver.resolve(i, 'A')[0].to_text()) + '\n'
        return res
    except Exception as e:
        return str(e), 500
