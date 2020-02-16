from areaCalculator import AreaCalculator, AreaCalculationError


class AreaCalculatorLibrary(object):
    """Test library for testing *AreaCalculator* logic.

    Interacts with the calculator directly using its ``push`` method.
    """

    def __init__(self):
        self._calc = AreaCalculator()
        self._result = ''

    def push_argument(self, arg):
        """Pushes the argument.
        The given value is passed to the calculator directly.

        Examples:
        | Push Argument | r   |
        | Push Argument | 1.0 |
        """
        self._result = self._calc.push(arg)

    def push_arguments(self, args):
        """Pushes the arguments.

        Uses `Push Argument` to push all the arguments that must be given as
        a single string. Possible spaces are ignored.

        Example:
        | Push Arguments | r 1.0 2.0 |
        """
        args=args.replace('C','C ')

        #remove multiple spaces
        while "  " in args:
            args.replace('  ',' ')
        
        args_splitted=args.split(" ")

        for arg in args_splitted:
            self.push_argument(arg)

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Arguments   | r 1.0 2.0 |
        | Result Should Be | 2.0       |
        """
        if self._result != float(expected):
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_cause_error(self, expression):
        """Verifies that calculating the given ``expression`` causes an error.
        """
        try:
            self.push_arguments(expression)
        except AreaCalculationError as err:
            return str(err)
        else:
            raise AssertionError("'%s' should have caused an error."
                                 % expression)
