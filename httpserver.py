from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/webapps':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(str(datetime.now()), "utf-8"))
        else:
            m = "Unsupported URI: " + self.path
            self.send_error(400, m)


httpd = HTTPServer(('localhost', 10000), HttpServer)
httpd.serve_forever()
'content-type header field'
'discover what user-agent is sending the request'
'exercise 4 lab1'
'import requests'
'resp = '
import requests
url = "https://postman-echo.com/basic-auth"
header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(url, headers=header)
print(response.status_code)
print(response.json())
