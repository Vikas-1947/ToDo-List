from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo")
    todos.append({"name": todo, "completed": False})
    return redirect("/")

@app.route("/complete/<index>")
def complete(index):
    index = int(index)
    todos[index]["completed"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
