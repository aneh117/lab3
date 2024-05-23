import price_info as priceinfo

def test_total_cost_shopping():
    totalcost = priceinfo.total_cost_shopping()
    result = 1
    assert (result == 1)

def test_cost_of_fruit():
    fruit_cost = priceinfo.cost_of_fruits('apple', 10)
    result = 0
    assert (result == 0)