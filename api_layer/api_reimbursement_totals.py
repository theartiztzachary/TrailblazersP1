from flask import Flask, request, jsonify

app: Flask = Flask(__name__)

#Basic hello world test to ensure app is running and connected (for testing with Postman).
@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

@app.route("/employee/<employee_id>/reimbursements")
def return_reimbursements():
    pass