from flask import Flask, render_template, request , redirect

app = Flask (__name__)

app.route('/', methods =['GET', 'POST'])

def index():
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")
        return f"Nome:{nome}<br>Email:{email}<br>Mensagem:{mensagem}"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)