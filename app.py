from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # Estado inicial do jogo
    etapa = request.form.get("etapa", "inicio")
    resposta = request.form.get("resposta", "").strip().lower()

    resultado = ""
    erro = ""
    proxima_etapa = etapa

    if request.method == "POST":
        # Fase 1: Binário
        if etapa == "inicio":
            if resposta in ["binario", "binário"]:
                resultado = "Resultado: WOI GSOUK"
                proxima_etapa = "fase2"
            else:
                erro = "Erro 333: Cifra incorreta. Tente novamente."

        # Fase 2: Atbash
        elif etapa == "fase2":
            if resposta == "atbash":
                resultado = "Resultado: GOU WKOIS"
                proxima_etapa = "fase3"
            else:
                erro = "Erro 303: Atbash não detectado."

        # Fase 3: César
        elif etapa == "fase3":
            if resposta in ["cesar", "césar"]:
                resultado = "Resultado: DLR THLFP"
                proxima_etapa = "final"
            else:
                erro = "Erro 404: Cifra de César incorreta."

        # Fase 4: Tradução
        elif etapa == "final":
            if resposta == "sim":
                resultado = "Criptografia é divertida!"
                proxima_etapa = "venceu"
            else:
                erro = "Erro 309: Tradução recusada."

    return render_template("index.html",
                           etapa=proxima_etapa,
                           resultado=resultado,
                           erro=erro)


if __name__ == "__main__":
    app.run(debug=True)
