from flask import Flask, render_template
import random
import datetime
import requests

# Store data in JSON and we can get using API :  https://www.npoint.io/    ------------>

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 100)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, current_year=year)


@app.route("/guess/<name>")
def guess_age(name):
    gender_API_response = requests.get(f"https://api.genderize.io?name={name}").json()
    age_API_response = requests.get(f"https://api.agify.io?name={name}").json()
    gender = gender_API_response["gender"]
    age = age_API_response["age"]
    return render_template("guess_age.html", person_name=name, gender=gender, age=age)


@app.route("/blogs/<num>")
def get_blogs(num):
    print(num)
    response = requests.get("https://api.npoint.io/a69f759d40f59c052c50").json()
    return render_template("blog.html", all_blogs=response)


if __name__ == "__main__":
    app.run(debug=True)
