from flask import Flask, render_template
app = Flask('__name__') #importar as bibliotecas do flask na aplicacao

@app.route('/') #quando a requesição do cliente terminar com '/' ele já vai entrar na funcao
def index ():  #criar a função index que vai ser chamada quando o servidor receber uma requisicao da raiz
    return render_template('index.html') # a funcao retornara o template que vai ser criado



f