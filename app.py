from flask import Flask, render_template_string
import socket
import os
import platform
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    uptime = round(time.time() - start_time)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App Deployed with Docker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                text-align: center;
                padding-top: 80px;
            }
            h1 {
                color: #007bff;
            }
            p {
                color: #333;
                font-size: 18px;
            }
            .card {
                background-color: white;
                border-radius: 12px;
                padding: 20px;
                width: 60%;
                margin: 0 auto;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello from Ashwin Premani's Flask App!</h1>
            <p><strong>IP Address:</strong> {{ ip }}</p>
            <p><strong>Host:</strong> {{ host }}</p>
            <p><strong>System:</strong> {{ system }}</p>
            <p><strong>Uptime:</strong> {{ uptime }} seconds</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, ip=ip_address, host=hostname, system=platform.system(), uptime=uptime)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
