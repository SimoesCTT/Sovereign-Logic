from flask import Flask, jsonify, render_template_string
import json
import os

app = Flask(__name__)
VAULT_PATH = "sovereign_vault.json"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sovereign Logic - Lattice Monitor</title>
    <style>
        body { background: #0d1117; color: #58a6ff; font-family: monospace; padding: 40px; }
        .vault-card { border: 1px solid #30363d; padding: 20px; border-radius: 6px; background: #161b22; }
        .delta { color: #3fb950; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #30363d; }
        h1 { color: #c9d1d9; border-bottom: 2px solid #238636; padding-bottom: 10px; }
    </style>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <h1>SINGAPORE ZENITH | v2.0.0-Omega</h1>
    <div class="vault-card">
        <p>Status: <span class="delta">ONLINE / COHERENT</span></p>
        <p>Anchor: 4A32...E5A8 | Delta: <span class="delta">0.00000000</span></p>
        <table>
            <tr><th>NODE_ID</th><th>STATUS/VALUE</th></tr>
            {% for key, val in data.items() %}
            <tr><td>{{ key }}</td><td>{{ val }}</td></tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    if os.path.exists(VAULT_PATH):
        with open(VAULT_PATH, 'r') as f:
            data = json.load(f)
    else:
        data = {"System": "Waiting for first resonance..."}
    return render_template_string(HTML_TEMPLATE, data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
