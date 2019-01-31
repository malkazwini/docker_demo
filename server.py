#Requires Python 3.7 and above

import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello Docker world')


httpd = socketserver.TCPServer(('', 8011), Handler)
httpd.serve_forever()

