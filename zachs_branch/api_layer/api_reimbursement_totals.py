from flask import Flask, jsonify
from flask_cors import CORS

from zachs_branch.data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from zachs_branch.service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation

from zachs_branch.utilities.custom_exceptions.total_is_zero import TotalIsZero
from zachs_branch.utilities.custom_exceptions.no_history import NoHistory

app: Flask = Flask(__name__)
CORS(app)
data_implementation = ReimbursementTotalsDataImplementation()
service_implementation = ReimbursementTotalsServiceImplementation(data_implementation)

# Basic hello world test to ensure app is running and connected (for testing with Postman).
@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

# API point for getting just approved reimbursements.
@app.route("/employee/<employee_id>/reimbursements/approved", methods=["GET"])
def get_approved_reimbursements(employee_id: str):
    try:
        result = service_implementation.check_completed_reimbursement_total(employee_id)
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
        result = service_implementation.check_pending_reimbursement_total(employee_id)
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
        result = service_implementation.check_full_history(employee_id)
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