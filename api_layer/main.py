from flask import Flask, request, jsonify

app: Flask = Flask(__name__)


@app.route("/json", methods=["GET"])
def return_a_json():
    customer_id = 1
    first_name = "Ted"
    last_name = "Teddington"

    # because this will be converted to a JSON we should follow JSON naming conventions
    customer_as_dictionary = {
        "customerId": customer_id,
        "firstName": first_name,
        "lastName": last_name
    }

    # we use the jsonify method to convert our dictionary into a json
    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json, 200


@app.route("/cancel/employee_id/reimbursement_id", methods=["DELETE"])  # or /cancel/reimbursement_id"
def cancel_reimbursement_request():
    pass
