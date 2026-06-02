"""Exercises 22-30: Flask routes, templates, forms, sessions, JSON POST, and deployment."""

try:
    from flask import Flask, jsonify, redirect, render_template, request, session, url_for
except ImportError:  # Keeps the file import-safe before dependencies are installed.
    Flask = None


if Flask:
    app = Flask(__name__)
    app.secret_key = "internship-demo-secret"

    @app.route("/")
    def home():
        return "Welcome to the Home Page"

    @app.route("/hello")
    def hello():
        return "Hello, Flask!"

    @app.route("/about")
    def about():
        return "This is the About Page"

    @app.route("/contact")
    def contact():
        return "Contact us at contact@example.com"

    @app.route("/greet")
    def greet():
        name = request.args.get("name", "Guest")
        return f"Hello, {name}!"

    @app.route("/profile")
    def profile():
        person = {"name": "Alice", "age": 25}
        return render_template("profile.html", person=person)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "").strip()
            return f"Submitted username: {username}, password length: {len(password)}"
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            session["username"] = request.form.get("username", "student")
            return redirect(url_for("dashboard"))
        return render_template("login.html")

    @app.route("/dashboard")
    def dashboard():
        username = session.get("username")
        if not username:
            return redirect(url_for("login"))
        return f"Welcome, {username}!"

    @app.route("/submit", methods=["POST"])
    def submit():
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        age = data.get("age")
        if not isinstance(name, str) or not name.strip() or not isinstance(age, int) or age <= 0:
            return jsonify(status="error", message="Invalid input"), 400
        return jsonify(status="success", message="Data received", data={"name": name.strip(), "age": age})


if __name__ == "__main__":
    if not Flask:
        print("Install Flask first: pip install flask")
    else:
        app.run(debug=True)
