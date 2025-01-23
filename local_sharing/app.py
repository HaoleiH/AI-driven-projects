from flask import Flask, request, jsonify, send_from_directory, abort
import os
import json
from werkzeug.utils import secure_filename
import ipaddress

app = Flask(__name__, static_folder="public")
UPLOAD_FOLDER = "uploads"
DATA_FILE = "data.json"

# this is the password. change 2887 to any password you want.
PASSWORD = "2887"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# uncomment this code block to only allow access to the website from certain ip addresses.
#------------
'''
def is_allowed_ip(ip):
    # Define the allowed subnet
    allowed_subnet = ipaddress.ip_network("10.84.0.0/16", strict=False)
    return ipaddress.ip_address(ip) in allowed_subnet

@app.before_request
def restrict_to_local_network():
    client_ip = request.remote_addr
    if not is_allowed_ip(client_ip):
        abort(403)  # Forbidden

'''
#-------------

# Serve the index.html file
@app.route("/")
def serve_index():
    return send_from_directory("public", "index.html")

# Serve static files
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("public", path)

# Serve uploaded images
@app.route("/uploads/<filename>")
def serve_uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Authenticate user
@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.get_json()
    if data.get("password") == PASSWORD:
        return jsonify(success=True), 200
    return jsonify(success=False), 403

# Save chat data
@app.route("/save", methods=["POST"])
def save_data():
    data = request.get_json()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    return jsonify(success=True), 200

# Load chat data
@app.route("/load", methods=["GET"])
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return jsonify(json.load(f)), 200
    return jsonify([]), 200

# Handle image uploads
@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return jsonify(success=True, url=f"/uploads/{filename}"), 200
    return jsonify(success=False), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #app.run(port=5000, debug=True)