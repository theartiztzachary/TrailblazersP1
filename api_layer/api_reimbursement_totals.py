from flask import Flask, jsonify

from data_access_layer.dal_reimbursement_total import ReimbursementTotalsDataImplementation
from service_layer.serl_reimbursement_total import ReimbursementTotalsServiceImplementation

from utilities.custom_exceptions.total_is_zero import TotalIsZero

app: Flask = Flask(__name__)
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

app.run()