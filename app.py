from flask import Flask
from flask_cors import CORS  # Importa a extensão CORS
from controllers.template_controllers import template_blueprint

app = Flask(__name__)
CORS(app)  # Aplica CORS à aplicação Flask
app.register_blueprint(template_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
