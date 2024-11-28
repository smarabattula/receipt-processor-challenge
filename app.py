from connexion import FlaskApp
from connexion.resolver import RelativeResolver

app = FlaskApp(__name__, strict_validation=True, validate_responses=True)

# Import OpenAPI Spec file
app.add_api("./api.yml", resolver = RelativeResolver("receipt_processor.handlers.handler_code"), strict_validation=True, validate_responses=True)

# Run app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1777)
