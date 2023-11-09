from flask import Flask
from controllers.template_controllers import template_blueprint

app = Flask(__name__)
app.register_blueprint(template_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
