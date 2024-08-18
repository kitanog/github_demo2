from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class InsecureHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_components = parse_qs(urlparse(self.path).query)
        
        # Get the 'name' parameter from the query string
        name = query_components.get('name', [''])[0]

        # Insecure: Reflect the 'name' parameter directly in the response without sanitizing it
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f"<h1>Hello, {name}</h1>", "utf-8"))

def run(server_class=HTTPServer, handler_class=InsecureHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
