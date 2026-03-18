import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 9005))
    s.listen(1)
    print("Listening on 9005...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        print(f"Received: {data}")
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello World!!")
    
    print("Connection closed. Success!")
    s.close()

if __name__ == "__main__":
    main()
