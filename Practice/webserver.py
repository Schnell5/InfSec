import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80
os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
