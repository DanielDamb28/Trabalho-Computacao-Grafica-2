from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse


class LogRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/log':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8') if length else ''
            try:
                print(f"[BROWSER LOG] {body}")
            except Exception:
                print('[BROWSER LOG] (could not decode body)')
            self.send_response(204)
            self.end_headers()
        else:
            self.send_error(404, 'Not Found')


def main():
    parser = argparse.ArgumentParser(description='Simple static server that prints browser logs')
    parser.add_argument('port', nargs='?', type=int, default=8000, help='Port to serve on (default 8000)')
    args = parser.parse_args()

    addr = ('', args.port)
    with ThreadingHTTPServer(addr, LogRequestHandler) as httpd:
        sa = httpd.socket.getsockname()
        print(f"Serving HTTP on {sa[0]} port {sa[1]} (http://localhost:{sa[1]}/) ...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nShutting down server')


if __name__ == '__main__':
    main()
