import os
import sys
import logging
from http.server import HTTPServer
sys.path.insert(0, "/usr/local/share/microservice")
from functools import wraps
from Common.base_http_server import NCD_http_request_handler

logger = logging
logger.basicConfig(filename='{}/log_controler/app.log'.format(os.getcwd()),
                   level=logging.INFO,
                   filemode='w',
                   format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

def show_fucntion_name(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

hostName = "0.0.0.0"
serverPort = int(os.environ['PORT'])
class MyServer(NCD_http_request_handler):

    @show_fucntion_name
    def do_GET(self):
        logger.info("path: {}".format(self.path))

        if "/" == self.path:
            self.login_html_index()
            return
        elif "/" in self.path and "." in self.path:
            self.path = "/microservice/NCD_service/GUI/Login_v1" +self.path
            super().do_GET()
            return

        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

    def login_html_index(self):
        pat = '/usr/local/share/microservice/NCD_service/GUI/Login_v1/index.html'
        try:
            if pat != ".py":
                f = open(pat).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = pat + " - File Not Found"
                self.send_error(404,f)
                logger.error("{}".format(f))
        except:
            f = pat + " - File Not Found"
            self.send_error(404,f)
            logger.error("{}".format(f),exc_info=True)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    sa = webServer.socket.getsockname()
    url = "http://" + sa[0] + ":" + str(sa[1]) + "/"
    logger.info("Server started http://%s:%s" % (hostName, serverPort))
    logger.info("url: {}".format(url))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        logger.error("Server stopped",exc_info=True)
        webServer.server_close()
