import pandas as pd


def add_function(number1, number2):
    return number1 + number2


number_calculated = 25

result_list = [add_function(number_calculated, x) for x in range(50, 125, 3)]
data = pd.DataFrame({'Result': result_list})

print(data)
data.to_csv(f'DATA/Result_for_{number_calculated}.csv', index=False)