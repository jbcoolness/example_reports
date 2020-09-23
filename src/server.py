from flask import Flask, render_template

from config import DevelopmentConfig
from models import db
from models import capita_poblaciones


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    page_title = 'Home'
    title = 'Home Pagina Inicial'
    return render_template('index.html', page_title=page_title, title= title)



if __name__ == "__main__":    
    db.init_app(app)

    with app.app_context():
        db.create_all()
      
    app.run()