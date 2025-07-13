from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Get request to render the hello world page
# This route is used to demonstrate a simple text response
@app.route("/helloWorld")
def hello_world():
    return "Hello, World!"


# Get request to render the home page
# This route serves the home page of the application
@app.route("/")
def home_page():
    return render_template("home.html")


# Get request to render the about page
@app.route("/about", methods=["GET"])
def about_page():
    return render_template("about.html")


# Post request to handle form submission
# This route handles both GET and POST requests
# If the request method is POST, it processes the form data
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form["email"]
        return f"Hello, {name}! , your email is {email}."
    return render_template("form.html")


# Get request to render the success page
# This route is used to display the result of an exam score
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam."
    else:
        res = "You have failed the exam."

    return render_template("result.html", result=res, score=score)


# This route is used to show all the results
@app.route("/results", methods=["GET"])
def results():
    results = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 45},
        {"name": "Charlie", "score": 70},
        {"name": "David", "score": 90},
        {"name": "Eve", "score": 60},
        {"name": "Frank", "score": 30},
        {"name": "Grace", "score": 95},
        {"name": "Hannah", "score": 55},
        {"name": "Ian", "score": 80},
        {"name": "Jack", "score": 40},
        {"name": "Kathy", "score": 75},
        {"name": "Leo", "score": 65},
        {"name": "Mia", "score": 50},
        {"name": "Nina", "score": 20},
        {"name": "Oscar", "score": 100},
        {"name": "Paul", "score": 30},
        {"name": "Quinn", "score": 85},
        {"name": "Rita", "score": 45},
        {"name": "Sam", "score": 70},
        {"name": "Tina", "score": 90},
    ]
    return render_template("allResults.html", results=results)


# redirect route to redirect to the home page
@app.route("/toBecomeSuccess", methods=["GET"])
def redirect_to_success():
    return redirect(url_for("success", score=75))


if __name__ == "__main__":
    app.run(debug=True)
