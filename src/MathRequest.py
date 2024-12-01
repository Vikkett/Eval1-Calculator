class MathRequest():
    def __init__ (self, ope1, oper, op2):
        raise NotImplementedError

    def get_ope1(self):
        raise NotImplementedError

    def get_oper(self):
        raise NotImplementedError

    def get_op2(self):
        raise NotImplementedError

    def get_res(self):
        raise NotImplementedError

    def set_res(self, value):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError