from connexion import FlaskApp

app = FlaskApp(__name__, strict_validation=True, validate_responses=True)

app.add_api("./api.yml",  strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=5000)
