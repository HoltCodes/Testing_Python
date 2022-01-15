from os import name
from timeit import repeat


def be_cheerful(name= '', repeat=2):
  print(f"Good morning {name}\n" * repeat)

be_cheerful("Rogan")
be_cheerful("River")
be_cheerful(name="Rachel")
be_cheerful(repeat=6)
be_cheerful(name="Nala", repeat=8)