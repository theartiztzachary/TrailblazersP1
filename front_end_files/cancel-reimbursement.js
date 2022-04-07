const cancelReimbursement = document.getElementById("reimbursement_id")

let requestId = {1:"Reimbursement ID"}; 
let input = 1;

function addReimbursementId()
{
requestId[input] = cancelReimbursement.value;
console.log(cancelReimbursement.value);
cancelReimbursement.value ="";
}

async function submit_cancel_reimbursement_button()
{

    let response = await fetch(
        `http://localhost:5000/cancel/${cancelReimbursement.value}`,
        {
            method:"GET"
        }
    );
    if(response.status == 200)
    {
        message = await response.text();
        alert(`Cancel successful for reimbursement ID number ${cancelReimbursement.value}`);
        
        window.location.href = "employee-home-page.html";
    } 
    else 
    {
        alert("Something went wrong, please try again");
    }


}