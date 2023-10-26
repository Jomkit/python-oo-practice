"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes
    ---------------
    start: int starting value (default = 0)
    a: int the variable that increments when executing generate()
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        
        self.start = start
        self.a = start

    def __repr__(self):
        return f"<serialGenerator start={self.start} next={self.generate()}>"

    def generate(self):
        """increments a by 1 every time it is called"""
        self.a += 1
        return self.a

    def reset(self):
        """resets a to start value"""
        self.a = self.start