from flask import Flask, request, jsonify
from .plagiarism import may_be_plagiarism_of

app = Flask(__name__)


@app.route("/plagiarism/possibility", methods=["POST"])
def may_be_plagiarism():
    # Parseo entrada
    json_data = request.json
    original_text = json_data['original_text']
    suspicious_text = json_data['suspicious_text']

    # Obtengo resultado
    result = may_be_plagiarism_of(suspicious_text, original_text)

    # Armo respuesta
    json_data['result'] = result

    return jsonify(json_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
