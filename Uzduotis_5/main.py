# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos:

import modules.num.ints as integers
from modules.mathematics.addition import add
from modules.mathematics.division import divide
from modules.mathematics.multiplication import multiply
from modules.mathematics.subtraction import subtract

# Kitų failų ir žemiau esančio kodo nekeiskite
a = add(integers.one, integers.four)
b = divide(integers.four, integers.two)
c = subtract(integers.three, integers.two)
d = multiply(integers.five, integers.two)

print(a);
print(b);
print(c);
print(d);
