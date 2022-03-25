from flask import Flask, jsonify, request

from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from service_layer.serl_login_implementation import LogInServiceLayerImplementation
from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword

app: Flask = Flask(__name__)

login_data_access_object = LogInDataAccessLayerImplementation()
login_service = LogInServiceLayerImplementation(login_data_access_object)


@app.route("/employee", methods=["GET"])
def select_employee_information():
    try:
        employee = request.get_json()
        employee_username = employee["employeeUsername"]
        employee_password = employee["employeePassword"]
        result = login_service.service_select_employee_information(employee_username, employee_password)
        result_dictionary = {
            "result": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 201

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