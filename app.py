from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Вітаємо у простому веб-додатку!</h1><p>Перейдіть до <a href='/form'>форми</a>.</p>"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"<h1>Привіт, {name}!</h1><p><a href='/form'>Назад до форми</a></p>"
    return '''
        <h1>Форма</h1>
        <form method="POST">
            <label for="name">Введіть своє ім'я:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <input type="submit" value="Відправити">
        </form>
        <p><a href="/">На головну</a></p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
