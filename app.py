from flask import Flask
from flask_cors import CORS  # Importa a extensão CORS
from controllers.template_controllers import template_blueprint
from controllers.dashboard_controller import dashboard_blueprint


app = Flask(__name__)
CORS(app)  # Aplica CORS à aplicação Flask
app.register_blueprint(template_blueprint)
app.register_blueprint(dashboard_blueprint)

if __name__ == '__main__':
    app.run(debug=True)