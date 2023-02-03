class RecipeIngrediants:

    def __init__(self, ingrediant, value, size):
        self._ingrediant = ingrediant
        self._value = value
        self._size = size

    @property
    def ingrediant(self):
        return self._ingrediant()

    @property
    def value(self):
        return self._value()

    @property
    def size(self):
        return self._size()

    def list_ingrediants(self):
        for row in 