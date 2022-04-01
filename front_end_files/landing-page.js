const employeeID = document.getElementById("employee-id-test")

function transferToHome() {
    window.sessionStorage.setItem("employee-id", employeeID.value);
    window.location.href = "employee-home-page.html"
}