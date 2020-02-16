class AreaCalculator(object):
    #SHAPES:
    #r = rectangle
    #e = ellipse
    #t = triangle

    def __init__(self):
        self._shape = ''
        self._width = 0.0
        self._height = 0.0


    def push(self, arg):
        if arg=="C":
            self._shape = ''
            self._width = 0.0
            self._height = 0.0
        elif arg in ["r","e","t"] and not self._shape:
            self._shape = arg
        elif self._shape and not self._width:
            try:
                w=float(arg)
                if w<=0.0:
                    w=0.0
                    raise AreaCalculationError("Invalid width argument: "+arg)
                self._width = w
            except:
                raise AreaCalculationError("Invalid width argument: "+arg)
        elif self._shape and self._width>0.0:
            try:
                h=float(arg)
                if h<=0.0:
                    h=0.0
                    raise AreaCalculationError("Invalid height argument: "+arg)
                self._height = h
            except:
                raise AreaCalculationError("Invalid height argument: "+arg)
        else:
            raise AreaCalculationError("Invalid expression.")

        if self._shape and self._width>0.0 and self._height>0.0:
            return self._calculate()


    def _calculate(self):
        if self._shape == "r":
            return round(self._width*self._height,2)
        elif self._shape == "e":
            return round(3.14*self._width*self._height,2)
        elif self._shape == "t":
            return round(self._width*self._height/2.0,2)


class AreaCalculationError(Exception):
    pass
