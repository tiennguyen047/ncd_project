import os
import sys
from http.server import HTTPServer
sys.path.insert(0, "/usr/local/share/microservice")
from functools import wraps
from Common.base_http_server import NCD_http_request_handler

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
        print(self.path)

        if "/" == self.path:
            print("1")
            self.login_html_index()
            return
        elif "/" in self.path and "." in self.path:
            self.path = "/microservice/NCD_service/GUI/Login_v1" +self.path
            super().do_GET()
            return

        else:
            print("else")
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
        except:
            f = pat + " - File Not Found"
            self.send_error(404,f)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    sa = webServer.socket.getsockname()
    url = "http://" + sa[0] + ":" + str(sa[1]) + "/"
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
