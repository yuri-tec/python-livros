from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
    {
        'id': 1,
        'livros': 'senhor dos aneis',
        'autor': 'j.r.r'
    },

    {
        'id': 2,
        'livros': 'hobbit',
        'autor': 'j.r.r'
    },

    {
        'id': 1,
        'livros': 'bilbia',
        'autor': 'senhor'
    }

]


@app.route('/livros')
def obter_livro():
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
