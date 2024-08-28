import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8080

DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def start_server():
    handler = CustomHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()


def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")


if __name__ == "__main__":
    threading.Thread(target=start_server).start()
    open_browser()
