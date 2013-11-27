class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))    


# R-2.4 (combined with R-2.5 and R-2.6)
class Flower:

    def __init__ (self, name, petals, price):
        self._name = name
        if not isinstance(petals, int) or petals < 0:
            raise ValueError("Number of petals must be a nonnegative integer.")
        self._petals =  petals
        if price < 0:
            raise ValueError("Price must be nonnegative.")
        else:
            self._price = price

    def getName(self):
        return self._name

    

# R-2.9
class Vector:
    def __init__ (self, l):
        self._dim = len(l)
        self._l = l

    def __sub__ (self, v):
        l = []

        try:
            for i in range(self._dim):
                l.append(self._l[i] - v[i])
        except IndexError:
            raise IndexError("Dimension mismatch.")
##        except TypeError:
##            raise TypeError

        return Vector(l)

    def __getitem__ (self, k):
        return self._l[k]

    def print(self):
        print(self._l)

    def __neg__ (self):
        l = []
        for i in range(self._dim):
            l.append(-self._l[i])
        return Vector(l)

    def __add__ (self, v):
        return -(-self - v)

    # from C-2.24
    def __mul__(self, a):
        if isinstance(a, Vector) or isinstance(a, list):
            try:
                return sum([self[i]*a[i] for i in range(self._dim)])
            except IndexError:
                raise IndexError("Dimension mismatch.")

        else:
            try:
                l=[]
                for i in range(self._dim):
                    l.append(self[i]*a)
                return Vector(l)
            except TypeError:
                raise TypeError("Cannot multiply these two objects.")


### C-2.37
##class Animal:
##    def __init__(self, species, gender, strength):
##        self._species = species
##        self._gender = gender
##        self._strength = strength
##
##class Bear(Animal):
##    def __init__(self, gender, strength):
##        super().__init__('bear', gender, strength)
##
##class Fish(Animal):
##    def __init__(self, gender, strength):
##        super().__init__('fish', gender, strength)
##
##class Ecosystem:
##    def __init__(self, size):
##        import random
##        
##        self._size=size
##        self._l=[]
##        
##        for i in range(size):
##            gender = 'M' if random.randint(0,1) else 'F'    
##            strength = random.randint(1,10)
##            animal = random.choice(range(3))
##            animal = Bear(gender, strength) if animal == 0 else (Fish(gender, strength) if animal == 1 else None)
##            self._l.append(animal)
##
##    def evolve(self):
##        import random
##        movement = [random.choice([-1,0,1]) for i in range(self._size-2)]
##        movement.insert(0, random.randint([0,1]))
##        movement.append(random.randint([-1,0]))
##        
        
