
def to_list(expression):
    expr_copy = expression.replace('x', ' ').replace('/', ' ').replace('+',
                                                                       ' ').replace('-', ' ').replace('(', ' ').replace(')', ' ').split()

    numbers = [int(x) for x in expr_copy]
    operators = [char for char in expression if not char.isdigit()]

    expr_final = []
    previous_was_digit = False
    for char in expression:
        if not char.isdigit():
            expr_final.append(operators[0])
            operators.pop(0)
            previous_was_digit = False
        elif not previous_was_digit:
            expr_final.append(numbers[0])
            numbers.pop(0)
            previous_was_digit = True
    return expr_final


def solve_times_div(expression):
    expr_copy = expression
    while expr_copy.count("x") > 0 or expr_copy.count("/") > 0:
        try:
            for index, item in enumerate(expr_copy):
                if (type(item) == int or type(item) == float) and expr_copy[index+1] == "x":
                    result = item * expr_copy[index+2]
                    expr_copy[index] = result
                    expr_copy.pop(index+1)
                    expr_copy.pop(index+1)
                    break
                elif (type(item) == int or type(item) == float) and expr_copy[index+1] == "/":
                    result = item / expr_copy[index+2]
                    expr_copy[index] = result
                    expr_copy.pop(index+1)
                    expr_copy.pop(index+1)
                    break
        except Exception as ex:
            print(Exception)
            break

    return expr_copy


def solve_plus_min(expression):
    expr_copy = expression
    while expr_copy.count("+") > 0 or expr_copy.count("-") > 0:
        try:
            for index, item in enumerate(expr_copy):
                if expr_copy[index+1] == "+":
                    result = item + expr_copy[index+2]
                    expr_copy[index] = result
                    expr_copy.pop(index+1)
                    expr_copy.pop(index+1)
                    break
                if expr_copy[index+1] == "-":
                    result = item - expr_copy[index+2]
                    expr_copy[index] = result
                    expr_copy.pop(index+1)
                    expr_copy.pop(index+1)
                    break
        except Exception as ex:
            print(ex)
            break

    return expr_copy


def solve_brackets_get_result(expression):
    expr_copy = expression
    while expr_copy.count("(") > 0:
        try:
            for index, item in enumerate(expr_copy):
                if item == "(":
                    if expr_copy[index+1:expr_copy.index(")")].count("(") == 0:
                        result = solve_plus_min(solve_times_div(
                            expr_copy[index+1:expr_copy.index(")")]))
                        result = result[0]
                        length = expr_copy.index(")") - index
                        expr_copy[index] = result
                        for i in range(length):
                            expr_copy.pop(index+1)
                        break
        except:
            raise Exception("Ooops! Something went wrong.")

    solve_plus_min(solve_times_div(expr_copy))
    return expr_copy[0]
