from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.jinja2')

    return app