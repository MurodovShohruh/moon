numbers = {"number1": 24,"number2": 56, "number3": 45, "number4": 34, "number5": 78, "number6": 67}
max_key=max(numbers,key=numbers.get)
max_value=numbers.pop(max_key)
print((f"({max_key} : {max_value})"))