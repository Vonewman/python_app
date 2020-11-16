class Pair:
    # We want to change the output produced by printitng or viewing
    # instances to something more sensible.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
