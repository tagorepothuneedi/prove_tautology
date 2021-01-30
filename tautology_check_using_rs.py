# Enter the input in variables of either a,b,c,d,p,q,r,s
# Reference for Propositional formula elements
# 'and' == &
# 'or' == |
# '-> == >>
# 'not' == ~
# <-> ('Iff') == <<


#Input - This programs expects a propositional formula.
#Output - The expected output is whether the propositional formula is a tautology or not.

#Tautology - Tautologies are a key concept in propositional logic, where a tautology is defined as a propositional formula
#            that is true under any possible Boolean valuation of its propositional variables.


# This expression runs the formula and sub formula that is obtained after decomposition
class Convert_To_Expression:
    def __invert__(self):
        return Not(self)

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __rshift__(self, other):
        return Implies(self, other)

    def __lshift__(self, other):
        return Iff(self, other)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.eq(other)

    def driver_function(self, left, right):
        while True:
            found = True
            for item in left:
                if item in right:
                    return None
                if not isinstance(item, Prop_Var):
                    left.remove(item)
                    tup = item._tleft(left, right)
                    left, right = tup[0]
                    if len(tup) > 1:
                        v = self.driver_function(*tup[1])
                        if v is not None:
                            return v
                    found = False
                    break
            for item in right:
                if item in left:
                    return None
                if not isinstance(item, Prop_Var):
                    right.remove(item)
                    tup = item._tright(left, right)
                    left, right = tup[0]
                    if len(tup) > 1:
                        v = self.driver_function(*tup[1])
                        if v is not None:
                            return v
                    found = False
                    break
            if found:                
                return "The Given Propositional Formula is not a Tautology"

    def _driver_function(self):
        return self.driver_function([], [self])    


# This is a class that converts the given logic with proper braces and indentation
class Bin_Op(Convert_To_Expression):
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '(' + str(self.left_child) + ' ' + self.op + ' ' + str(self.right_child) + ')'

    def eq(self, other):
        return self.left_child == other.left_child and self.right_child == other.right_child


# This class resolves the "and" condition between propositional variables
class And(Bin_Op):
    op = '^'
    st = ''
    def _tleft(self, left, right):
        print("Result of AND function", self.left_child, self.right_child)        
        return (left + [self.left_child, self.right_child], right),

    def _tright(self, left, right):
        print("Result of AND function", self.left_child, self.right_child)        
        return (left, right + [self.left_child]), (left, right + [self.right_child])


# This class resolves the "Implies" condition between propositional variables
class Implies(Bin_Op):
    op = '->'

    def _tleft(self, left, right):
        print("Result of Implies function", self.left_child, self.right_child)
        return (left + [self.right_child], right), (left, right + [self.left_child])

    def _tright(self, left, right):
        print("Result of Implies function", self.left_child, self.right_child)
        return (left + [self.left_child], right + [self.right_child]),


# This class resolves the "Iff" condition between propositional variables
class Iff(Bin_Op):
    op = '<->'

    def _tleft(self, left, right):
        print("Result of Iff function", self.left_child, self.right_child)
        return (left + [self.left_child, self.right_child], right), (left, right + [self.left_child, self.right_child])

    def _tright(self, left, right):
        print("Result of Iff function", self.left_child, self.right_child)
        return (left + [self.left_child], right + [self.right_child]), (left + [self.right_child], right + [self.left_child])


# This class resolves the "not" condition between propositional variables
class Not(Convert_To_Expression):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return '~' + str(self.child)

    def eq(self, other):
        return self.child == other.child

    def _tleft(self, left, right):
        return (left, right + [self.child]),

    def _tright(self, left, right):
        return (left + [self.child], right),


# This class resolves the "or" condition between propositional variables
class Or(Bin_Op):
    op = 'v'

    def _tleft(self, left, right):
        print("Result of Or function", self.left_child, self.right_child)
        return (left + [self.left_child], right), (left + [self.right_child], right)

    def _tright(self, left, right):
        print("Result of Or function", self.left_child, self.right_child)
        return (left, right + [self.left_child, self.right_child]),


# This is a class that takes in the propositional variables that are involved to identify whether it's a tautology or not
class Prop_Var(Convert_To_Expression):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return str(self.name)

    __repr__ = __str__

    def eq(self, other):
        return self.name == other.name



a = Prop_Var('a')
b = Prop_Var('b')
c = Prop_Var('c')
d = Prop_Var('d')
p = Prop_Var('p')
q = Prop_Var('q')
r = Prop_Var('r')
s = Prop_Var('s')
treestruct = []

#This is the main method which runs the given expression
def rs_method(e):
    print("The given input in actual propositional formula terms ", e)
    result = e._driver_function() # This function break down the given formula to evaluate if it's a tautology or not
    #print(treestruct)
    if result == None:
        print("The Given Propositional Formula is a Tautology")
    else:
        print("The Given Propositional Formula is not a Tautology")


while(True):    
    inputString = input("Please enter the Propositional Formula. Press Ctrl + C to terminate:")
    #treestruct.clear()

    try:
        inputString = inputString.lower()
        e = eval(inputString)
        rs_method(e)
    except NameError:
        print("Invalid Propositional Formual. Please enter a valid one")
        
