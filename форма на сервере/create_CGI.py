from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

server_address = ("localhost", 8000) #иногда хочет пустые кавычки
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()