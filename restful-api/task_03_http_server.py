#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class simpleHTTPServer(BaseHTTPRequestHandler):
    """Use the http.server module to set up a simple HTTP server. Start by
    creating a subclass of http.server.BaseHTTPRequestHandler."""

    def do_GET(self):
        """Serve a GET request."""

        # method to handle GET requests
        if self.path == "/":
            # status code: success
            self.send_response(200)

            # tell client what format sending back with header
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            # simple text response back to the client and convert into bytes
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        # serve a sample JSON data when endpoint /data is accessed.
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}

            json_response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json_response.encode('utf-8'))

        # /status endpoint to check the API status.
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "plain/text")
            self.end_headers()

            self.wfile.write("OK".encode('utf-8'))

        # Implement error handling
        else:
            self.send_response(404)
            self.send_header("Content-Type", "plain/text")
            self.end_headers()

            self.wfile.write("Endpoint not found".encode('utf-8'))


def run(server_class=HTTPServer, handler_class=simpleHTTPServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()