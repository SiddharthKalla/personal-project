from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", answer=None)

@app.route("/answer", methods=["POST"])
def answer():
    response = request.form.get("response")

    if response == "yes":
        message = "YAYYYYY 💖 She said YES! Best Valentine ever!"
    else:
        message = "Oh nooo 😭 But I’ll keep trying!"

    return render_template("index.html", answer=message)

if __name__ == "__main__":
    app.run(debug=True)
