const reimbursementId = 0;
const amountInput = document.getElementById("amount");
const reasonInput = document.getElementById("reason");
const reimbursementReasonInput = document.getElementById("reimbursementComment");

let reimburesementRequest = {
    "employeeId": null,
    "amount": null,
    "reason": null,
    "reimbursementComment": null
}

async function submitReimbursement(){
    reimburesementRequest.employeeId = window.sessionStorage.getItem("employee-id")
    reimburesementRequest.amount = amountInput.value;
    reimburesementRequest.reason = reasonInput.value;
    reimburesementRequest.reimbursementComment = reimbursementReasonInput.value;
    
    let config = {
            method:"POST",
            headers:{'Content-Type':"application/json"},
            body: JSON.stringify(reimburesementRequest)
        }

        const submit = await fetch("http://localhost:5000/reimbursements/", config);
        if(submit.status === 201){
            let reimbursement = await submit.text();
            alert(reimbursement);
            toHomePage()
        } else {
            alert("Oops Something went wrong");
        }
}

function toHomePage() {
    window.location.href = "employee-home-page.html";
}