const employeeUsername = document.getElementById("username-input");
const employeePassword = document.getElementById("password-input");

let employeeInformation = {"employeeUsername":null, "employeePassword":null};

async function logIn() {
    let requestURL = `http://localhost:5000/employee/${employeeUsername.value}/${employeePassword.value}/`
    employeeInformation.employeeUsername = employeeUsername.value;
    employeeInformation.employeePassword = employeePassword.value;

    let config = {
        method:"GET"  
    }

    const response = await fetch(requestURL, config);
    if(response.status === 200){
        message = await response.text();
        let unpackedMessage = JSON.parse(message);
        let numberMessage = Number(unpackedMessage.message)
        window.sessionStorage.setItem("employee-id", numberMessage);
        window.location.href = "employee-home-page.html"
    } else {
        message = await response.text();
        let unpackedMessage2 = JSON.parse(message)

        alert(unpackedMessage2.message);
        }
}