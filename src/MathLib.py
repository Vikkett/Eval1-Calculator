from src.MathRequest import MathRequest
class MathLib:

    @classmethod
    def execute(self, mathRequest):
        # Perform the operation based on the operator
        ope1 = mathRequest.get_ope1()
        oper = mathRequest.get_oper()
        ope2 = mathRequest.get_ope2()

        match oper:
            case 'add':
                mathRequest.set_res(ope1 + ope2)
            case 'sub':
                mathRequest.set_res(ope1 - ope2)
            case 'mul':
                mathRequest.set_res(ope1 * ope2)
            case 'div':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return
                mathRequest.set_res(ope1 / ope2)
            case 'pow':
                res = 1
                for count in range(int(ope1)):
                    mathRequest.set_res(ope1 ** ope2)
            case _:
                print("Invalid operator.")
                return
        return
