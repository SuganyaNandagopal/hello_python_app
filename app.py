import os
from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <h2>Hello! Welcome to my first Python App 🚀</h2>
    <form method="post" action="/submit">
        <input name="message" placeholder="Type something"/>
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    msg = request.form.get("message")
    return f"<h3>You typed: {msg}</h3>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render’s dynamic port
    app.run(host="0.0.0.0", port=port, debug=True)