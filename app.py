from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")  # Usa o que já tiver no seu templates/

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("mensagem")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente técnico rural do sistema Topogeo, especializado em crédito, propostas e atendimento."},
            {"role": "user", "content": user_msg}
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({"resposta": reply})

if __name__ == "__main__":
    app.run(debug=True)
