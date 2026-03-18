import socket

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
        s.bind(('127.0.0.1', 9001))
        print("Socket bound to 9001")
        s.listen(1)
        print("Socket listening")
        s.close()
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
