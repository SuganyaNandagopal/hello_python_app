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
    app.run(debug=True)