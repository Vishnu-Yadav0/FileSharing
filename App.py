import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os
import getpass
import sys
import threading

# Constants
PORT = 8010

def run_server():
    try:
        # Get current username
        username = getpass.getuser()
        home_path = os.environ.get('USERPROFILE') or os.path.expanduser("~")

        # Verify directory
        if not os.path.exists(home_path):
            raise FileNotFoundError(f"Directory not found: {home_path}")

        os.chdir(home_path)
        print(f"Username: {username}")
        print(f"[INFO] Serving files from: {home_path}")

        # Set up handler
        Handler = http.server.SimpleHTTPRequestHandler

        # Get local IP
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                ip_address = s.getsockname()[0]
        except OSError as e:
            print(f"[ERROR] Could not retrieve IP address: {e}")
            return

        link = f"http://{ip_address}:{PORT}"
        print(f"[INFO] Local server link: {link}")

        # Generate QR Code
        try:
            qr = pyqrcode.create(link)
            qr_file = os.path.join(home_path, "myqr.svg")
            qr.svg(qr_file, scale=8)
            print(f"[INFO] QR Code saved at: {qr_file}")
            webbrowser.open(qr_file)
        except Exception as e:
            print(f"[ERROR] Could not generate or open QR code: {e}")

        # Start server with shutdown support
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"[INFO] Serving at port {PORT}")
            print(f"[INFO] Type this in your browser: {link}")
            print(f"[INFO] Or scan the QR code")
            print("[INFO] Press 'q' and Enter to quit.\n")

            # Background thread to watch for 'q'
            def watch_quit():
                while True:
                    if input().strip().lower() == 'q':
                        print("[INFO] Shutting down server...")
                        httpd.shutdown()
                        break

            threading.Thread(target=watch_quit, daemon=True).start()

            httpd.serve_forever()

    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
    except PermissionError:
        print("[ERROR] Permission denied. Try running with appropriate access rights.")
    except OSError as e:
        print(f"[ERROR] OS error: {e}")
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped by user.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
    finally:
        sys.exit(0)

# Run it
if __name__ == "__main__":
    run_server()
