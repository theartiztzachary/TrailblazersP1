from flask import Flask, request, jsonify
from flask_cors import CORS

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest

app: Flask = Flask(__name__)
CORS(app)
employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp(employee_dao)


@app.route("/reimbursements/", methods=["POST"])
def submit_reimbursement_record():
    try:
        reimbursement_data_info = request.get_json()
        reimbursement = ReimbursementData(
            "0",
            reimbursement_data_info["employeeId"],
            reimbursement_data_info["amount"],
            reimbursement_data_info["reason"],
            reimbursement_data_info["reimbursementComment"],
            "Pending"
        )
        result = employee_serl.serl_submit_reimbursement(reimbursement)
        dictionary_reimbursement = result.reimbursementdata_to_dictionary()
        reimbursement_json = jsonify(dictionary_reimbursement)
        return reimbursement_json, 201
    except BadReimbursementRequest as e:
        error_message = {
            "message": str(e)
        }
        error_json = jsonify(error_message)
        return error_json, 404


app.run()
