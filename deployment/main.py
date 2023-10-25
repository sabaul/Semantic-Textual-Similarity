import os
import json
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('./all-MiniLM-L6-v2')

app = Flask(__name__)

@app.route("/similarity", methods=["POST"])
def make_prediction():
    if request.method == "POST":
        try:
            input_sentences = request.json
            sentence1 = input_sentences.get('text1', '')
            sentence2 = input_sentences.get('text2', '')

            embeddings1 = model.encode(sentence1, convert_to_tensor=True)
            embeddings2 = model.encode(sentence2, convert_to_tensor=True)

            cosine_score = util.pytorch_cos_sim(embeddings1, embeddings2)[0][0]
            if cosine_score > 0:
                return jsonify({"Similarity Score": float(cosine_score)})
            else:
                return jsonify({"Similarity Score": 0})
        except Exception as err:
            return jsonify({"Error": str(err)})
    return "OK"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))