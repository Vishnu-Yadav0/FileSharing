import http.server
import socket
import socketserver
import pyqrcode
import os
import getpass
import sys
import threading

PORT = 8010

def run_server():
    try:
        username = getpass.getuser()
        home_path = os.path.expanduser("~")

        if not os.path.exists(home_path):
            raise FileNotFoundError(f"Directory not found: {home_path}")

        os.chdir(home_path)
        print(f"Username: {username}")
        print(f"[INFO] Serving files from: {home_path}")

        Handler = http.server.SimpleHTTPRequestHandler

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                ip_address = s.getsockname()[0]
        except OSError as e:
            print(f"[ERROR] Could not retrieve IP address: {e}")
            return

        link = f"http://{ip_address}:{PORT}"
        print(f"[INFO] Local server link: {link}")

        try:
            qr = pyqrcode.create(link)
            qr_file = os.path.join(home_path, "myqr.svg")
            qr.svg(qr_file, scale=8)
            print(f"[INFO] QR Code saved at: {qr_file}")
        except Exception as e:
            print(f"[ERROR] Could not generate QR code: {e}")

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"[INFO] Serving at port {PORT}")
            print(f"[INFO] Access it at: {link}")
            print("[INFO] Press 'q' and Enter to quit.\n")

            def watch_quit():
                while True:
                    if input().strip().lower() == 'q':
                        print("[INFO] Shutting down server...")
                        httpd.shutdown()
                        break

            threading.Thread(target=watch_quit, daemon=True).start()
            httpd.serve_forever()

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    run_server()
