import lab2.bmi as bmi

def test_bmi_normal_weight():
    BMI = bmi.calculate_bmi(1.73,57)
    num = 0
    assert (BMI == num)
def test_bmi_over_weight():
    BMI = bmi.calculate_bmi(1.70,65)
    num = 1
    assert (BMI == num) 
def test_bmi_under_weight():
    BMI = bmi.calculate_bmi(175,53)
    num = -1
    assert (BMI == num)