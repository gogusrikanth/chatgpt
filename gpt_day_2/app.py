from flask import Flask, request, render_template, jsonify
import json
from prompt_processing import tokenizer
from knowledge_classification import classify
from knowledge_classification import extract,tokenizer as tk

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    prompt = data["prompt"]
    result = tokenizer(prompt)
    return jsonify(result)

@app.route("/classify", methods=["GET","POST"])
def cls():
    data = request.get_json()
    prompt = data["prompt"]
    most_similar_sentence,most_similar_index,similarities = classify(prompt)
    result = {
        "Most similar sentence": most_similar_sentence[0],
        "Intent": most_similar_sentence[1],
        "Cosine Similarity": similarities[most_similar_index]
    }
    return jsonify(result)

@app.route("/extract",methods=["POST"])
def ext():
    data = request.get_json()
    prompt = data["prompt"]
    kwds = extract(set(tk(prompt)))
    result = {
        "Keywords":kwds
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)