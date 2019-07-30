from flask import Flask, request, current_app
from flask_bluestatic import BlueStatic

app = Flask(__name__)
app.register_blueprint(BlueStatic(name ="bluestaticOne", path='./test/html'))
app.register_blueprint(BlueStatic(name ="bluestaticTwo",path='./test/html', url_prefix="/static"))

if __name__ == "__main__":
    app.run(port=8080)
