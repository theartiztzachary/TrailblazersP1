from flask import Flask, jsonify
from flask_cors import CORS

from data_access_layer.dal_login_implementation import LogInDataAccessLayerImplementation
from service_layer.serl_login_implementation import LogInServiceLayerImplementation
from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation

from utilities.custom_exceptions.employee_not_found import EmployeeNotFound
from utilities.custom_exceptions.incorrect_password import IncorrectPassword
from utilities.custom_exceptions.total_is_zero import TotalIsZero
from utilities.custom_exceptions.no_history import NoHistory

app: Flask = Flask(__name__)
CORS(app)

login_data_access_object = LogInDataAccessLayerImplementation()
login_service = LogInServiceLayerImplementation(login_data_access_object)
totals_data_implementation = ReimbursementTotalsDataImplementation()
totals_service_implementation = ReimbursementTotalsServiceImplementation(totals_data_implementation)

# Basic hello world test to ensure app is running and connected (for testing with Postman).
@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

@app.route("/employee/<employeeUsername>/<employeePassword>/", methods=["GET"])
def select_employee_information(employeeUsername: str, employeePassword: str):
    try:
        result = login_service.service_select_employee_information(employeeUsername, employeePassword)

        result_dictionary = {
            "message": result
        }
        result_json = jsonify(result_dictionary)
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


# API point for getting just approved reimbursements.
@app.route("/employee/<employee_id>/reimbursements/approved", methods=["GET"])
def get_approved_reimbursements(employee_id: str):
    try:
        result = totals_service_implementation.check_completed_reimbursement_total(employee_id)
        result_dictionary = {"Approved Total:": result}
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except TotalIsZero as exception:
        message = {"Error Message:": str(exception)}
        return jsonify(message), 400

# API point for getting just pending reimbursements.
@app.route("/employee/<employee_id>/reimbursements/pending", methods=["GET"])
def get_pending_reimbursements(employee_id: str):
    try:
        result = totals_service_implementation.check_pending_reimbursement_total(employee_id)
        result_dictionary = {"Pending Total:": result}
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except TotalIsZero as exception:
        message = {"Error Message:": str(exception)}
        return jsonify(message), 400

# API point for getting the full reimbursement history.
@app.route("/employee/<employee_id>/reimbursements/all", methods=["GET"])
def get_all_reimbursements(employee_id: str):
    try:
        result = totals_service_implementation.check_full_history(employee_id)
        result_dictionary = {}
        for i in range(len(result)):
            current_dictionary = {
                "reimbursementID": result[i].reimbursement_id,
                "employeeID": result[i].employee_id,
                "amount": result[i].amount,
                "reason": result[i].reason,
                "reimbursementComment": result[i].reimbursement_comment,
                "statusCode": result[i].status_code
            }
            dictionary_index = f"Entry {i+1}"
            result_dictionary[dictionary_index] = current_dictionary
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except NoHistory as exception:
        message = {"Error Message:": str(exception)}
        return jsonify(message), 400

app.run()