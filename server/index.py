import dns.resolver
from flask import *
dns.resolver.name = ['1.0.0.1', '8.8.4.4']
app = Flask(__name__)

@app.route('/')
def index():
    add = request.values.get('get')
    if add is None:
        return '200 OK'
    add = add.split(';')
    try:
        res = ''
        for i in add:
            res += str(dns.resolver.resolve(i, 'A')[0].to_text() + ' ' + i)
            res += '\n'
        rsp = make_response(res)
        rsp.headers['Content-Type']= 'text/plain'
        return rsp
    except Exception as e:
        return str(e), 500
