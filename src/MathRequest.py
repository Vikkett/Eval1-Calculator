class MathRequest:

    def __init__ (self, ope1, oper, ope2):
        self.ope1 = ope1
        self.oper = oper
        self.ope2 = ope2
<<<<<<< HEAD
=======
        self.res = None
>>>>>>> feature/MathLib

    def get_ope1(self):
        return self.ope1

    def get_oper(self):
<<<<<<< HEAD
        raise NotImplementedError

    def get_ope2(self):
        raise NotImplementedError

    def get_res(self):
        raise NotImplementedError

    def set_res(self, value):
        raise NotImplementedError
=======
        return self.oper

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return self.res

    def set_res(self, value):
        self.res = value
>>>>>>> feature/MathLib

    def to_string(self):
        raise NotImplementedError