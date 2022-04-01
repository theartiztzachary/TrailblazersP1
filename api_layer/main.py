from flask import Flask, jsonify
from flask_cors import CORS

from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from service_layer.serl_login_implementation import LogInServiceLayerImplementation
from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword

app: Flask = Flask(__name__)
CORS(app)

login_data_access_object = LogInDataAccessLayerImplementation()
login_service = LogInServiceLayerImplementation(login_data_access_object)


@app.route("/employee/<employeeUsername>/<employeePassword>/", methods=["GET"])
def select_employee_information(employeeUsername: str, employeePassword: str):
    try:
        result = login_service.service_select_employee_information(employeeUsername, employeePassword)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        print("HELLO")
        return result_json, 200

    except EmployeeNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IncorrectPassword as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
