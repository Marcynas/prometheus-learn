import http.server
from prometheus_client import start_http_server

APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>  It works :)! </body></html>","utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT),HandleRequests)
    server.serve_forever()
