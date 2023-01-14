import numbers
class SomadorError(Exception):
    pass

class Somador:
    def soma(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 + op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral):
            raise SomadorError(f"{op} n eh inteiro!!!!")


