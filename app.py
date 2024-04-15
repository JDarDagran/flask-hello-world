from __future__ import annotations

import sys
import time

from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    time.sleep(2)
    if request.is_json:
        print(request.json, file=sys.stderr)
    
    return Response('You want path: %s' % path, status=200)

if __name__ == '__main__':
    app.run()
