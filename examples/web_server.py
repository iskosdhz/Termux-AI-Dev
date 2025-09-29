#!/data/data/com.termux/files/usr/bin/python3
"""
🌐 Web Server for Termux Development
Author: iskosdhz
Description: Simple Flask web server to test web development environment
"""

from flask import Flask, render_template_string, jsonify, request
import socket
import threading
import time
import os

app = Flask(__name__)

# HTML Templates
HOME_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Termux Web Server</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        .container { 
            max-width: 800px; 
            margin: 0 auto;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .header { 
            text-align: center; 
            margin-bottom: 30px;
        }
        .header h1 { 
            font-size: 2.5em; 
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .status-card {
            background: rgba(255,255,255,0.2);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            border-left: 5px solid #4CAF50;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .feature {
            background: rgba(255,255,255,0.15);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }
        .btn {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 25px;
            margin: 10px 5px;
            transition: transform 0.3s;
        }
        .btn:hover {
            transform: translateY(-2px);
            background: #45a049;
        }
        .terminal {
            background: #1e1e1e;
            color: #00ff00;
            padding: 15px;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌐 Termux Web Server</h1>
            <p>Your Android device is now running a web server! 🚀</p>
        </div>

        <div class="status-card">
            <h2>📊 Server Status</h2>
            <p><strong>Platform:</strong> {{ platform }}</p>
            <p><strong>Python Version:</strong> {{ python_version }}</p>
            <p><strong>Server IP:</strong> {{ server_ip }}</p>
            <p><strong>Port:</strong> {{ port }}</p>
            <p><strong>Uptime:</strong> {{ uptime }}</p>
        </div>

        <div class="feature-grid">
            <div class="feature">
                <h3>🤖 AI Ready</h3>
                <p>TensorFlow, PyTorch, scikit-learn</p>
            </div>
            <div class="feature">
                <h3>🌐 Web Framework</h3>
                <p>Flask, APIs, Templates</p>
            </div>
            <div class="feature">
                <h3>📱 Mobile Optimized</h3>
                <p>Runs on Android Termux</p>
            </div>
            <div class="feature">
                <h3>🔧 Development</h3>
                <p>Full stack environment</p>
            </div>
        </div>

        <div style="text-align: center;">
            <a href="/api/status" class="btn">📡 API Status</a>
            <a href="/api/system" class="btn">⚙️ System Info</a>
            <a href="/demo" class="btn">🎯 Demo Page</a>
        </div>

        <div class="terminal">
            $ python examples/web_server.py<br>
            🚀 Server running on {{ server_ip }}:{{ port }}<br>
            ✅ Termux development environment active
        </div>

        <div style="text-align: center; margin-top: 20px;">
            <p><strong>🔧 Next Steps:</strong> Check the <code>projects/web/</code> directory for your web projects!</p>
        </div>
    </div>
</body>
</html>
'''

DEMO_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🎯 Demo Page - Termux</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }
        .demo-card { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>🎯 Termux Web Development Demo</h1>
    
    <div class="demo-card">
        <h3>🚀 Features Demonstrated</h3>
        <ul>
            <li>✅ Flask Web Framework</li>
            <li>✅ REST API Endpoints</li>
            <li>✅ HTML Templates</li>
            <li>✅ CSS Styling</li>
            <li>✅ JSON Responses</li>
            <li>✅ Mobile Responsive</li>
        </ul>
    </div>

    <div class="demo-card">
        <h3>🔧 Try These API Endpoints:</h3>
        <p><a href="/api/status">/api/status</a> - Server status</p>
        <p><a href="/api/system">/api/system</a> - System information</p>
        <p><a href="/api/time">/api/time</a> - Current time</p>
    </div>

    <a href="/">🏠 Back to Home</a>
</body>
</html>
'''

class ServerMonitor:
    def __init__(self):
        self.start_time = time.time()
    
    def get_uptime(self):
        uptime_seconds = time.time() - self.start_time
        hours = int(uptime_seconds // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Initialize monitor
monitor = ServerMonitor()

@app.route('/')
def home():
    """Main homepage"""
    try:
        # Get server IP
        hostname = socket.gethostname()
        server_ip = socket.gethostbyname(hostname)
    except:
        server_ip = "127.0.0.1"
    
    return render_template_string(HOME_TEMPLATE,
        platform="Termux on Android",
        python_version=sys.version.split()[0],
        server_ip=server_ip,
        port=5000,
        uptime=monitor.get_uptime()
    )

@app.route('/demo')
def demo():
    """Demo page"""
    return render_template_string(DEMO_TEMPLATE)

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        "status": "running",
        "service": "Termux Web Server",
        "platform": "Android Termux",
        "timestamp": time.time(),
        "uptime": monitor.get_uptime()
    })

@app.route('/api/system')
def api_system():
    """System information API"""
    return jsonify({
        "python_version": sys.version,
        "platform": sys.platform,
        "working_directory": os.getcwd(),
        "server_time": time.ctime()
    })

@app.route('/api/time')
def api_time():
    """Current time API"""
    return jsonify({
        "current_time": time.ctime(),
        "timestamp": time.time(),
        "timezone": time.tzname
    })

@app.route('/api/echo', methods=['POST'])
def api_echo():
    """Echo API for testing POST requests"""
    data = request.get_json() or {}
    return jsonify({
        "echo": data,
        "received_at": time.ctime()
    })

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def main():
    """Main function to start the server"""
    local_ip = get_local_ip()
    
    print("🚀 Starting Termux Web Server...")
    print("=" * 50)
    print(f"📱 Local:    http://127.0.0.1:5000")
    print(f"🌐 Network:  http://{local_ip}:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Start Flask server
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()
