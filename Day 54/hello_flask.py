# for run : flask --app <file_name> run (Note: write only file name, not .py extension)
from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Hello!"


# if we write this porsion we not need to use command $$flask --app <file_name> run$$ for running
if __name__ == "__main__":
    app.run()
