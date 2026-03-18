import subprocess
import time
import sys

def main():
    print("Starting Loop Server (Auto-Restart Mode)...")
    cmd = [sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload', '--nothreading']
    while True:
        try:
            print("Server process started.")
            # Run the server and wait for it to exit
            process = subprocess.Popen(cmd)
            process.wait()
            
            # If it exits with an error code, wait a bit and restart
            if process.returncode != 0:
                print(f"Server crashed with exit code {process.returncode}. Restarting in 2 seconds...")
                time.sleep(2)
            else:
                print("Server stopped cleanly. Restarting...")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping loop server.")
            break
        except Exception as e:
            print(f"Loop error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
