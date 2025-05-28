import price_info as PInfo

def total_cost_of_fruits():
    fruits_name = 'watermelon'
    fruit_quantity = 5
    expected_result = 32.50
    test_result = PInfo.cost_of_fruits(fruits_name, fruit_quantity)
    assert (test_result == expected_result)


    assert (PInfo.cost_of_fruits('watermelon', 5)==32.50)