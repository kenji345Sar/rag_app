from flask import Flask, request, render_template
from rag_core import get_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = get_answer(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
