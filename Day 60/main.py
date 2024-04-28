from flask import Flask, render_template, request
import requests
from twilio.rest import Client

posts = requests.get("https://api.npoint.io/a69f759d40f59c052c50").json()
account_sid = ""
auth_token = ""

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_message(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_message(name, email, phone, message):
    message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    client = Client(account_sid, auth_token)
    client.messages.create(from_="", body=message, to="")


if __name__ == "__main__":
    app.run(debug=True)
