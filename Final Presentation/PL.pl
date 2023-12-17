

% Propositional logic

P: Socrates is a philosopher.
Q: Plato is a philosopher.
R: Aristotle is a philosopher.
S: Socrates is human.
T: Plato is human.
U: Aristotle is human.
V: Suman is human.
W: Socrates is wise.
X: Plato is wise.
Y: Aristotle is wise.

P is symbol and the comment is semantics
# Define propositions
P = True  # Socrates is a philosopher.
Q = False  # Plato is a philosopher.
R = True  # Aristotle is a philosopher.
S = True  # Socrates is human.
T = False  # Plato is human.
U = True  # Aristotle is human.
V = True  # Suman is human.
W = True  # Socrates is wise.
X = False  # Plato is wise.
Y = True  # Aristotle is wise.

# Apply AND operation
result = P and Q and R and S and T and U and V and W and X and Y

# Print result
print("The result of the AND operation is:", result)
