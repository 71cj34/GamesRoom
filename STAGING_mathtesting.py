import random
import math

a = 9
b = 4
c = -12


# solutions = 0
# constant = c + a * b
# for factor1 in range(1, abs(constant) + 1):
#     if constant % factor1 == 0:
#         factor2 = constant // factor1
#         x = factor1 - b
#         y = factor2 - a
#         if (x * y + a * x + b * y == c):  # pos
#             solutions.append((x, y))  # use as 4
#         x = -factor1 - b
#         y = -factor2 - a
#         if (x * y + a * x + b * y) == c:  # neg
#             solutions.append((x, y))
# answer = solutions
# question = f"How many NEGATIVE solution pairs are there for the equation xy + {a}x + {b}y = {c}?"

solutions = 0
constant = c + a * b
for factor1 in range(1, abs(constant) + 1):
    if constant % factor1 == 0:
        factor2 = constant // factor1
        x = factor1 - b
        y = factor2 - a
        if x > 0 and y > 0:
            solutions += 1
answer = solutions
question = f"How many POSITIVE solution pairs are there for the equation xy + {a}x + {b}y = {c}?"

# solutions = []
# constant = c + a * b
# for factor1 in range(1, abs(constant) + 1):
#     if constant % factor1 == 0:
#         factor2 = constant // factor1
#         x = factor1 - b
#         y = factor2 - a
#         if (x * y + a * x + b * y == c):  # pos
#             solutions.append((x, y))  # use as 4
#         x = -factor1 - b
#         y = -factor2 - a
#         if (x * y + a * x + b * y) == c:  # neg
#             solutions.append((x, y))
# answer = len(solutions)
# question = f"How many solution pairs are there for the equation xy + {a}x + {b}y = {c}?"

print(question)
print(answer)

