numeric_string = "75"
non_numeric_string = "hello"

number_int = int(numeric_string)
number_float = float(numeric_string)

print(number_int)
print(number_float)


# bad_number = int(non_numeric_string)

amount = "70.00"

try:
    amount_float = float(amount)
except ValueError:
    pass
    # raise custom error or however you want to do it