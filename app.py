import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", answer=None)

@app.route("/answer", methods=["POST"])
def answer():
    response = request.form.get("response")

    if response == "yes":
        message = "And Its a Yes! 💖 She said YES! Best Valentine ever!"
    else:
        message = "Oh nooo 😭 But I’ll keep trying!"

    return render_template("index.html", answer=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

