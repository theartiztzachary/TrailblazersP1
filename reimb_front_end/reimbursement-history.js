const numberInput = document.getElementById("number-input")
const historyTable = document.getElementById("history-table")
const pendingTotal = document.getElementById("pending-total")
const approvedTotal = document.getElementById("approved-total")

async function requestHistory() {
    let requestURL = `http://localhost:5000/employee/${numberInput.value}/reimbursements/all`;
    let response = await fetch(requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populateHistory(data)
    } else {
        alert('Something went wrong :/');
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
            square.textContent = element
            row.appendChild(square)
        }
    }
}

async function requestPending() {
    let requestURL = `http://localhost:5000/employee/${numberInput.value}/reimbursements/pending`;
    let response = await fetch(requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populatePending(data);
    } else {
        alert('Something went wrong :/');
    }
}

function populatePending(data) {
    pendingTotal.textContent = data["Pending Total:"];
}

async function requestApproved() {
    let requestURL = `http://localhost:5000/employee/${numberInput.value}/reimbursements/approved`;
    let response = await fetch (requestURL, {method:"GET"});
    if (response.status === 200) {
        const data = await response.json();
        populateApproved(data);
    } else {
        alert('Something went wrong :/');
    }
}

function populateApproved(data) {
    approvedTotal.textContent = data ["Approved Total:"];
}