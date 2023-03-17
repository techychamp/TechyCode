import socket

HOST = '74.82.60.89'  # The server's hostname or IP address
PORT = 443        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"""
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\n
accept-encoding: gzip, deflate\n
accept-language: en-US,en;q=0.9\n
cache-control: max-age=0\n
cookie: _ga=GA1.2.1528753803.1567001682; __unam=707d966-16cd8941c3e-5548e403-6\n
upgrade-insecure-requests: 1\n
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36""")
    data = s.recv(1024)

print('Received', repr(data))
