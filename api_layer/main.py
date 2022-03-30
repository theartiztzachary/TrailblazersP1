from flask import Flask, request, jsonify

from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.reimbursement_service_imp import ReimbursementServiceImp

app: Flask = Flask(__name__)

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


@app.route("/cancel/employee_id/reimbursement_id", methods=["PATCH"])  # or /cancel/reimbursement_id"
def cancel_reimbursement_request():
    try:
        pass
    except IdNotFound as e:
        error_message = {
            "message": str(e)
        }
        error_json = jsonify(error_message)
        return error_json, 404
