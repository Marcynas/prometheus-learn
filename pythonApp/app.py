import http.server
from prometheus_client import start_http_server, Counter, Gauge, Summary
import time

APP_PORT = 8000
METRICS_PORT = 8001

REQUEST_COUNT = Counter("app_requests_count", "total all http request count",['app_name','endpoint'])
REQUEST_INPROGRESS = Gauge("app_requests_inprogress","number of app  requests in progress", )
REQUEST_LAST_SERVED = Gauge("app_last_served","Time the application was last served")
REQUEST_RESPOND_TIME = Summary("app_response_latency_sec", "latency in seconds")

class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQUEST_RESPOND_TIME.time()
    @REQUEST_INPROGRESS.track_inprogress()
    def do_GET(self): 
        #start_time = time.time()
        REQUEST_COUNT.labels('homepage',self.path).inc()
        #REQUEST_INPROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>  It works :)! </body></html>","utf-8"))
        self.wfile.close()
        REQUEST_LAST_SERVED.set_to_current_time()
        #REQUEST_LAST_SERVED.set(time.time())
        #REQUEST_INPROGRESS.dec()
        #time_taken = time.time()-start_time
        #REQUEST_RESPOND_TIME.observe(time_taken)

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT),HandleRequests)
    print("It's ON!")
    server.serve_forever()
    