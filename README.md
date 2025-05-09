
# Python HTTP Web Server with QR Code Generator

This Python-based web server allows you to serve files from your local machine over HTTP and generates a QR code containing the link to the server for easy access. The QR code is displayed automatically in the web browser. The server will continue to run until the user presses 'q' to shut it down.

## Features

- Starts a local HTTP server that serves files from your computer's user directory.
- Generates a QR code containing the local server link (`http://<ip_address>:<port>`) that you can scan with your mobile device.
- Gracefully shuts down the server when the user presses the 'q' key.

## Requirements

To run this application, you will need the following:

- Python 3.6 or above
- Python packages:
  - `pyqrcode`
  - `png`
  - `getpass`
  - `webbrowser`
  - `http.server`
  - `socket`
  - `socketserver`
  - `threading`

You can install the required packages using `pip`:

```bash
pip install pyqrcode pypng
```

## How to Run

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Vishnu-Yadav0/FileSharing.git
    cd FileSharing
    ```

2. Run the script:
    ```bash
    pip install -r requirements.txt
    python3 server.py
    ```

   This will:
   - Start a web server on port `8010`.
   - Generate a QR code that contains the URL to access the server from any device in the same local network.
   - Open the QR code image in your web browser.

3. Scan the QR code with your mobile device, or type the server link directly into your browser:
    ```
    http://<ip_address>:8010
    ```

4. Press `q` and hit **Enter** to stop the server.

## Notes

- The server will start in your user directory (`C:\Users\<your-username>` for Windows or `/home/<your-username>` for Linux/macOS).
- Make sure that both the **sender's** and **receiver's** laptops are connected to the **same local network** for the QR code to work correctly and the link to be accessible.

## Example Output

Upon successful execution, you will see output similar to the following:

```bash
Username: vishnu
[INFO] Serving files from: C:\Users\vishnu
[INFO] Local server link: http://192.168.1.100:8010
[INFO] QR Code saved at: C:\Users\vishnu\myqr.svg
[INFO] Serving at port 8010
[INFO] Type this in your browser: http://192.168.1.100:8010
[INFO] Or scan the QR code
[INFO] Press 'q' and Enter to quit.
```

The QR code will be automatically opened in your web browser for you to scan.

## Error Handling

The application handles the following errors:
- **FileNotFoundError**: Raised if the user's home directory cannot be found.
- **PermissionError**: Raised if the script does not have permission to access the required files or directories.
- **OSError**: Raised for any other operating system-related errors, such as network issues.
- **KeyboardInterrupt**: Gracefully handles the server stop command (Ctrl+C).
  
If any errors occur, they will be printed in the terminal or command prompt.

## Contributing

Feel free to fork this repository, contribute bug fixes, or improve the features. Open a pull request with your changes, and they will be reviewed.

### License

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

**Note:** Both the **sender's** and **receiver's** devices must be connected to the **same local network** for the QR code to work and the server to be accessible. If they are on different networks, the connection will not be established.
