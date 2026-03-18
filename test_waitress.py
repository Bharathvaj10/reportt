from waitress import serve

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b"Hello world from Waitress!"]

def main():
    print("Starting minimal Waitress server on http://127.0.0.1:8001")
    serve(simple_app, host='127.0.0.1', port=8001)

if __name__ == "__main__":
    main()
