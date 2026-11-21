"""
app.py - Flask Server for Quantum Gravity Presentation Project
Serves presentation interface, scientific assets, numerical calculation data,
and provides live MATLAB execution triggers.
"""

import os
import sys
import json
import subprocess
from flask import Flask, render_template, send_from_directory, jsonify, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, 'static'),
    template_folder=os.path.join(BASE_DIR, 'templates')
)

@app.route('/')
def index():
    return render_template('index.html', has_flask=True)

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'data'), filename)

@app.route('/results/<path:filename>')
def serve_results(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'results'), filename)

@app.route('/api/scenes')
def api_scenes():
    scenes_path = os.path.join(BASE_DIR, 'data', 'scenes.json')
    if os.path.exists(scenes_path):
        with open(scenes_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "scenes.json not found"}), 404

@app.route('/api/data')
def api_data():
    data_path = os.path.join(BASE_DIR, 'results', 'quantum_gravity_data.json')
    if not os.path.exists(data_path):
        data_path = os.path.join(BASE_DIR, 'data', 'quantum_gravity_data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "quantum_gravity_data.json not found"}), 404

@app.route('/api/run-matlab', methods=['POST'])
def api_run_matlab():
    """Trigger matlab_runner.py to re-evaluate calculations."""
    try:
        runner_path = os.path.join(BASE_DIR, 'matlab_runner.py')
        res = subprocess.run([sys.executable, runner_path], cwd=BASE_DIR, capture_output=True, text=True, timeout=60)
        return jsonify({
            "status": "success" if res.returncode == 0 else "error",
            "returncode": res.returncode,
            "stdout": res.stdout,
            "stderr": res.stderr
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("=========================================================================")
    print(" QUANTUM GRAVITY: Unifying the Universe and the Future of Technology")
    print(" Starting Flask local server on http://127.0.0.1:5000/")
    print("=========================================================================")
    app.run(host='127.0.0.1', port=5000, debug=False)
