class MathLib:

def calculate(math_request):
    # Perform the operation based on the operator
    ope1 = math_request.get_ope1()
    oper = math_request.get_oper()
    ope2 = math_request.get_ope2()

    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope1 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case '^':
            res = 1
            for count in range(int(ope1)):
                res = res * ope2
        case _:
            print("Invalid operator.")
            return
    return res