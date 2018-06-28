import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

if len(sys.argv) > 1:
    webdir = sys.argv[1]
if len(sys.argv) > 2:
    port = sys.argv[2]

os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
