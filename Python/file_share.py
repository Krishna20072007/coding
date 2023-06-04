import http.server
import socket
import socketserver
import os


PORT = 2000
IP = "http://localhost:" + str(PORT)
print(f"Serving on {IP}")

file_path = "c:/Users/krish/Desktop/Krishna-Files"
Handler = http.server.SimpleHTTPRequestHandler
os.chdir(file_path)

httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
