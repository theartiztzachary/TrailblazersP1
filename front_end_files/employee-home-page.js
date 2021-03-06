const historyTable = document.getElementById("history-table")
const pendingTotal = document.getElementById("pending-total")
const approvedTotal = document.getElementById("approved-total")

let generatedID = 0

async function populatePage() {
    requestHistory();
    requestPending();
    requestApproved();
}

async function requestHistory() {
    let requestURL = `http://localhost:5000/employee/${window.sessionStorage.getItem("employee-id")}/reimbursements/all`;
    let response = await fetch(requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populateHistory(data);
    }
}

function populateHistory(data) {
    historyTable.innerHTML = "";
    for (let key in data) {
        const row = document.createElement("tr");
        historyTable.appendChild(row);

        const reimbursementID = data[key].reimbursementID;
        const amount = data[key].amount;
        const reason = data[key].reason;
        const note = data[key].reimbursementComment;
        const statusCode = data[key].statusCode

        dataList = [reimbursementID, amount, reason, note, statusCode]
        for (let element of dataList) {
            const square = document.createElement("td");
            square.textContent = element;
            row.appendChild(square);
            square.id = generatedID;
            generatedID ++
        }
    }
}

async function requestPending() {
    let requestURL = `http://localhost:5000/employee/${window.sessionStorage.getItem("employee-id")}/reimbursements/pending`;
    let response = await fetch(requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populatePending(data);
    }
}

function populatePending(data) {
    pendingTotal.textContent = data["Pending Total:"];
}

async function requestApproved() {
    let requestURL = `http://localhost:5000/employee/${window.sessionStorage.getItem("employee-id")}/reimbursements/approved`;
    let response = await fetch (requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populateApproved(data);
    }
}

function populateApproved(data) {
    approvedTotal.textContent = data["Approved Total:"];
}

function logoutFunction() {
    window.sessionStorage.clear;
    window.location.href = "landing-page.html";
}

function toSubmitPage() {
    window.location.href = "submit-reimbursement.html";
}

function toCancelPage() {
    window.location.href = "cancel-reimbursement.html";
}