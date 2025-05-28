import employee_info as EMPI
from employee_info import employee_data as data

def test_calc_average_salary():
    expected_result=60166.67
    test_result=EMPI.calculate_average_salary()
    assert (test_result==expected_result)

def test_get_employee_by_dept():
    expected_result =[ data[1], data[2]]
    test_result = EMPI.get_employees_by_dept('Marketing')
    assert (test_result==expected_result)

def test_get_employee_by_dept():
    expected_result=[data[0], data[-1]]
    test_result = EMPI.get_employees_by_dept("Sales")
    assert (test_result == expected_result)

def test_get_employees_by_age_range():
    expected_result=[data[0], data[4]]
    age_lower_limit =26
    age_upper_limit =33
    test_result =EMPI.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    assert (test_result == expected_result)
