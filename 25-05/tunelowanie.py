# serwer9000.py
import http.server
import socketserver

PORT = 9000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Forwarding dziala! (Port 9000 lokalnie)")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serwer HTTP dziala na porcie {PORT}")
    httpd.serve_forever()