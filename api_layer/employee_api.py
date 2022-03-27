from flask import Flask, request, jsonify

from data_access_layer.employee_dao_imp import EmployeeDAOImp
from service_layer.employee_serl_imp import EmployeeServiceLayerImp
from utilities.custom_exceptions.bad_reimbursement_request import BadReimbursementRequest

app: Flask = Flask(__name__)

employee_dao = EmployeeDAOImp()
employee_serl = EmployeeServiceLayerImp(employee_dao)

@app.route("/reimbursements", methods=["POST"])
def submit_reimbursement_record():
    try:
        reimbursement_data_info = request.get_json()
        reimbursement = Reimbursement(
            reimbursement_data_info["reimbursementId"],
            reimbursement_data_info["employeeID"],
            reimbursement_data_info["amount"],
            reimbursement_data_info["reason"],
            reimbursement_data_info["reimbursementComment"],
            reimbursement_data_info["statusCode"]
        )
        result = employee_serl.serl_submit_reimbursement(reimbursement)
        dictionary_reimbursement = result.reimbursementdata_to_dictionary()
        reimbursement_json = jsonify(dictionary_reimbursement)
        return reimbursement_json, 201
    except BadReimbursementRequest as e:
        return_message = {
            "message": str(e)
        }
return jsonify(return_message), 404

app.run()

