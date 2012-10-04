from decimal        import Decimal
from exceptions     import ValueError



class Temperature(object):
    """
    A class for working with temperatures. It provides helpers for converting
    between Kelvin, Celsius, Fahrenheit, and Rankine. Internally, the
    temperature is stored as Kelvin in a Decimal. All of the conversions are
    returned in Decimal form, for the sake of .

    Access each conversion by using the corresponding attribute:

        >>> t = Temperature(1.0)
        >>> t
        Temperature(1)
        >>> t.k
        Decimal('1')
        >>> t.c
        Decimal('-272.15')
        >>> t.f
        Decimal('-457.870')
        >>> t.r
        Decimal('1.80')
        >>> str(t)
        '1 K'

    Temperatures can be generally treated like a number, using various
    operators like <, >, +, -, *. If operating on two Temperatures, their
    Kelvin value will be used.

        >>> t1 = Temperature(k=40)
        >>> t2 = Temperature(f=212)
        >>> t2 - t1
        Temperature(333.15)
        >>> (t2 - t1).f
        Decimal('140.000')
        >>> t1 * 2
        Temperature(80)

    To operate on a temperature without creating another Temperature instance,
    simply operate on the unit attribute, and the other operand will be used as
    that unit:

        >>> t = Temperature(0)
        >>> t.f += 100
        >>> t
        Temperature(55.5556)

    If the specified temperature is less than 0 Kelvin, a `ValueError` will be
    raised.

        >>> t = Temperature(-5)
        [...traceback omitted...]
        Exception: Temperature Kelvin value (-4) cannot be less than 0
        >>> t1 = Temperature(100)
        >>> t2 = Temperature(200)
        >>> t1 - t2
        [...traceback omitted...]
        Exception: Temperature Kelvin value (-4) cannot be less than 0


    Derived from http://code.activestate.com/recipes/286226-temperature-class/
    with some operadtor overloading and sanity checks (eg prevent temperatures
    less than 0 K).
    """

    equations = {
        'c': ( Decimal('1.0'), Decimal('0.0')     , Decimal('-273.15') ),
        'f': ( Decimal('1.8'), Decimal('-273.15') , Decimal('32.0') ),
        'r': ( Decimal('1.8'), Decimal('0.0')     , Decimal('0.0') ),
    }

    def __init__(self, k=0.0, **kwargs):
        self.k = k
        for key in kwargs:
            if key in ('c', 'f', 'r'):
                setattr(self, key, kwargs[key])
                break

    def __getattr__(self, name):
        if name in self.equations:
            eq = self.equations[name]
            return (self.k + eq[1]) * eq[0] + eq[2]
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        value = Decimal(value)
        if name in self.equations:
            eq = self.equations[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        else:
            object.__setattr__(self, name, value)
        if self.k < 0:
            k = self.k
            self.k = 0
            raise ValueError('Temperature Kelvin value (%s) cannot be less than 0' % (k,))



    def __str__(self):
        return "%g K" % self.k

    def __repr__(self):
        return "Temperature(%g)" % self.k

    def __lt__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k < other
    
    def __le__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k <= other
    
    def __gt__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k > other
    
    def __ge__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k >= other
    
    def __eq__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k == other
    
    def __ne__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return self.k != other
    
    def __add__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return Temperature(self.k + other)
    
    def __sub__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return Temperature(self.k - other)
    
    def __mul__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return Temperature(self.k * other)
    
    def __div__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        return Temperature(self.k / other)

    def __iadd__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        self.k = self.k + other
        return self
    
    def __isub__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        self.k = self.k - other
        return self
    
    def __imul__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        self.k = self.k * other
        return self
    
    def __idiv__(self, other):
        if hasattr(other, 'k'):
            other = other.k
        self.k = self.k / other
        return self

    def __int__(self):
        return int(self.k)

    def __long__(self):
        return long(self.k)

    def __float__(self):
        return float(self.k)

    def __complex__(self):
        return complex(self.k)

    def __oct__(self):
        return oct(self.k)

    def __hex__(self):
        return hex(self.k)