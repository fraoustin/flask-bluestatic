Flask-bluestatic
=================

Flask-logsocketio generate on socketio "log"  log of your application

It use flask-bluestatic module

Installation
------------

::

    pip install flask-bluestatic
        
Or

::

    git clone https://github.com/fraoustin/bluestatic.git
    cd bluestatic
    python setup.py install

Usage
-----

::
    
    from flask import Flask
    from flask_bluestatic import BlueStatic

    app = Flask(__name__)
    app.register_blueprint(BlueStatic(path='./html'))

    if __name__ == "__main__":
        app.run(port=8080)
