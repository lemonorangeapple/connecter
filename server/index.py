import dns.resolver
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    add = request.values.get('get')
    if add is None:
        return '200 OK'
    try:
        return str(add + ' ' + dns.resolver.resolve(add, 'A')[0].to_text())
    except Exception as e:
        return str(e), 500
