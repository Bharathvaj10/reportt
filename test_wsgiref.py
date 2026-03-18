from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b"Hello world from wsgiref!"]

def main():
    print("Starting wsgiref server on http://127.0.0.1:8006")
    with make_server('127.0.0.1', 8006, simple_app) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
