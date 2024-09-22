from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the host and port to bind to
HOST = '0.0.0.0'  # Bind to all available network interfaces
PORT = 80  # Port number inside the container


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content=type', 'text/html')
        self.end_headers()
        self.write.write(b'Hello, Docker World!')

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on {HOST}:{PORT}")
    httpd.server_forever()

if __name__ == "__main__":
    run()
