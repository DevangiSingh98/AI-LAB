from itertools import product

class Symbol:
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        return model[self.name]

    def symbols(self):
        return {self.name}

    def __repr__(self):
        return self.name


class Not:
    def __init__(self, a):
        self.a = a

    def evaluate(self, model):
        return not self.a.evaluate(model)

    def symbols(self):
        return self.a.symbols()


class And:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self, model):
        return self.a.evaluate(model) and self.b.evaluate(model)

    def symbols(self):
        return self.a.symbols() | self.b.symbols()


class Or:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self, model):
        return self.a.evaluate(model) or self.b.evaluate(model)

    def symbols(self):
        return self.a.symbols() | self.b.symbols()


class If:  # conditional ->
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self, model):
        return (not self.a.evaluate(model)) or self.b.evaluate(model)

    def symbols(self):
        return self.a.symbols() | self.b.symbols()


class Iff:  # biconditional <->
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self, model):
        return self.a.evaluate(model) == self.b.evaluate(model)

    def symbols(self):
        return self.a.symbols() | self.b.symbols()


def tf(val):
    return 'T' if val else 'F'


def truth_table(label, expr):
    syms = sorted(expr.symbols())
    print(f"\n--- {label} ---")
    header = "  ".join(syms) + "  | Result"
    print(header)
    print("-" * len(header))
    for vals in product([False, True], repeat=len(syms)):
        model = dict(zip(syms, vals))
        result = expr.evaluate(model)
        row = "  ".join(tf(v) for v in vals) + "  |  " + tf(result)
        print(row)


# define symbols
P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')

# 1. ~P -> Q
e1 = If(Not(P), Q)
truth_table("1. ~P -> Q", e1)

# 2. ~P and ~Q
e2 = And(Not(P), Not(Q))
truth_table("2. ~P ^ ~Q", e2)

# 3. ~P or ~Q
e3 = Or(Not(P), Not(Q))
truth_table("3. ~P v ~Q", e3)

# 4. ~P -> ~Q
e4 = If(Not(P), Not(Q))
truth_table("4. ~P -> ~Q", e4)

# 5. ~P <-> ~Q
e5 = Iff(Not(P), Not(Q))
truth_table("5. ~P <-> ~Q", e5)

# 6. (P v Q) ^ (~P -> Q)
e6 = And(Or(P, Q), If(Not(P), Q))
truth_table("6. (P v Q) ^ (~P -> Q)", e6)

# 7. (P v Q) -> ~R
e7 = If(Or(P, Q), Not(R))
truth_table("7. (P v Q) -> ~R", e7)

# 8. ((P v Q) -> ~R) <-> ((~P ^ ~Q) -> ~R)
e8 = Iff(If(Or(P, Q), Not(R)), If(And(Not(P), Not(Q)), Not(R)))
truth_table("8. ((P v Q)->~R) <-> ((~P^~Q)->~R)", e8)

# 9. ((P->Q) ^ (Q->R)) -> (Q->R)
e9 = If(And(If(P, Q), If(Q, R)), If(Q, R))
truth_table("9. ((P->Q)^(Q->R))->(Q->R)", e9)

# 10. (((P->(QvR)) -> (~P^~Q^~R)))
e10 = If(If(P, Or(Q, R)), And(And(Not(P), Not(Q)), Not(R)))
truth_table("10. ((P->(QvR))->(~P^~Q^~R))", e10)