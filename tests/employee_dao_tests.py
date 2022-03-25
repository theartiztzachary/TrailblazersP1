from data_access_layer.employee_dao_imp import EmployeeDAOImp
from entities.reimbursement_data import ReimbursementData

employee_dao = EmployeeDAOImp()


def test_dao_submit_reimbursement():
    reimbursements = ReimbursementData(0, 1, 100.00, "Hotel", "stayed in HamptonInn", "pending")
    result = employee_dao.submit_reimbursement(reimbursements)
    assert result.reimbursement_id != 0


def test_dao_get_reimbursement_info_by_id_success():
    result = employee_dao.get_reimbursement_info_by_id(2)
    assert result.reimbursement_id == 2


def test_dao_get_reimbursement_info_by_non_existant_id():
    result = employee_dao.get_reimbursement_info_by_id(-100)
    assert result is None
