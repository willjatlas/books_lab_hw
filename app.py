from flask import Flask, render_template
from controllers.books_controller import books_blueprint

# TODO: import books blueprint here

app = Flask(__name__)

app.register_blueprint(books_blueprint)

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)



