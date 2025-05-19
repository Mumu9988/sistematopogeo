from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("mensagem")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente técnico rural do sistema Topogeo. Fale de forma direta, clara e profissional sobre crédito rural, propostas e atendimento."},
            {"role": "user", "content": user_msg}
        ]
    )
    return jsonify({"resposta": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)
