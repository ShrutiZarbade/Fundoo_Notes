from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socketserver
import templates


PORT = 8000

#
# class ServerHandler(SimpleHTTPRequestHandler):
#
#     def do_POST(self):
#       content_len = int(self.headers.getheader('content-length', 0))
#       post_body = self.rfile.read(content_len)
#       print(post_body)
# Handler = ServerHandler
#
# httpd = socketserver.TCPServer(("", PORT), Handler)


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi</h1></body></html>")
    #     <form action="" method="post">
    # <div class="container">
    # <h3> Login Page </h3>
    # <label for="uname"><b>Username</b></label>
    # <input type="text" placeholder=" " name="uname" required>
    # <br>   </br>
    # <label for="psw"><b>Password</b></label>
    # <input type="password" placeholder=" " name="psw" required>
    # <br>  </br>
    # <button type="submit">Login</button>
    # </div>
    # </form>

    # .encode("utf-8")
    #    self.wfile.write(registration.html)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data)  # <-- Print post data
        self.wfile.write("<html><body><h1>POST!</h1><pre>" + post_data + "</prev></body></html>")
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(HTTPServer, S)