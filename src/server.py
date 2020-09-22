from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    page_title = 'Home'
    title = 'Home Pagina Inicial'
    return render_template('index.html', page_title=page_title, title= title)



if __name__ == "__main__":
    app.run(debug = True)