from flask import Flask, request, render_template, redirect

# Configure app
app = Flask(__name__)

# Ensures templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("sign.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/main")
    else:
        return render_template("register.html")

if __name__ == "__main__":
    app.run()