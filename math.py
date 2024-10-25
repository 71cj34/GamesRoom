# heyyyy 1p13 ta grading this lol
# i spent way too much time on this
# hint: i would collapse the generatequestion(topic) function if I were you
# :D

import math
import random
import time

class cl:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"

    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

q = []
a = []
points = 0

topics = ["add", "sub", "mult", "div", "pow", "sqrt", "percent", "gcd", "lcm",
          "factor", "roots", "dist", "log", "remainder",
          "chngbase", "crt", "diophantine", "vieta", "brahmagupta",
          "factoroffactorials", "", "burnside", "stewart", "chickenmcnuggettheorem"] # 'difficulty' is by obscurity not difficulty
                                                                                     # except the nugget one
                                                                                     # its there because its funny

def generatequestion(topic):
    if topic == 0:
        num1, num2 = random.randint(1, 5000), random.randint(1, 5000)
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif topic == 1:
        num1, num2 = random.randint(1, 5000), random.randint(1, 5000)
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif topic == 2:
        num1, num2 = random.randint(2, 25), random.randint(2, 25)
        question = f"{num1} * {num2}"
        answer = num1 * num2
    elif topic == 3:
        num1, num2 = random.randint(50, 500), random.randint(2, 20)
        question = f"{num1} / {num2}"
        answer = f"{num1 / num2:.2f}"
    elif topic == 4:
        num1, num2 = random.randint(1, 15), random.randint(2, 10)
        question = f"{num1} ^ {num2}"
        answer = num1 ** num2
    elif topic == 5:
        num1 = random.randint(2, 50) ** 2
        question = f"Square root of {num1}"
        answer = num1 ** 0.5
    elif topic == 6:
        num1, num2 = random.randint(5, 5000) // 5, random.randint(100, 5000) // 5
        question = f"{num1}% of {num2}"
        answer = (num2 / 100) * num1
    elif topic == 7:
        num1, num2 = random.randint(30, 500), random.randint(30, 500)
        question = f"GCD of {num1} and {num2}"
        answer = math.gcd(num1, num2)
    elif topic == 8:
        num1, num2 = random.randint(30, 500), random.randint(30, 500)
        question = f"LCM of {num1} and {num2}"
        answer = math.lcm(num1, num2)
    elif topic == 9:
        variation = random.randint(1, 5)
        if variation == 1:
            i, j, k, l = [random.randint(1, 10) for _ in range(4)]
            x, y, z = i * j, i * l + j * k, k * l
            question = f"Factorize {x}a^2 + {y}ab + {z}b^2. Input the coefficients of (?a + ?b)(?a + ?b)."
            answer = [i, k, j, l]
        elif variation == 2:
            r1, r2 = random.randint(-10, 10), random.randint(-10, 10)
            a = random.randint(-10, 10)
            while a == 0:
                a = random.randint(-10, 10)
            b = a * -(r1 + r2)
            c = a * (r1 * r2)
            question = f"Find all solutions for {a}x^2 + {b}x + {c} = 0. 1-2 integers expected."
            answer = [r1, r2]
        elif variation == 3:
            if random.random() > 0.5:
                a, b = random.randint(-20, 20), random.randint(-20, 20)
                question = f"Simplify ({a}x + {b})({a}x - {b}). "
                answer = [a ** 2, b ** 2]
            else:
                a, b = random.randint(-20, 20), random.randint(-20, 20)
                question = f"Factor {a ** 2}x^2 - {b ** 2}. "
                answer = [a, b]
        elif variation == 4:
            if random.random() > 0.5:
                if random.random() > 0.5:
                    a, b = random.randint(-20, 20), random.randint(-20, 20)
                    question = f"Factor {a ** 3}x^3 + {b ** 3}. "
                    answer = [a + b, a ** 2 - a * b + b ** 2]
                else:
                    a, b = random.randint(-20, 20), random.randint(-20, 20)
                    question = f"Factor {a ** 3}x^3 - {b ** 3}. "
                    answer = [a - b, a ** 2 + a * b + b ** 2]
        else:
            if random.random() > 0.5:
                a, b = random.randint(-20, 20), random.randint(-20, 20)
                question = f"Expand ({a} + {b})({a ** 2}x^2 - {a * b}x + {b ** 2}). "
                answer = [a ** 3, b ** 3]
            else:
                a, b = random.randint(-20, 20), random.randint(-20, 20)
                question = f"Expand ({a} - {b})({a ** 2}x^2 + {a * b}x + {b ** 2}). "
                answer = [a ** 3, -b ** 3]
    elif topic == 10:
        while True:
            a, b, c = random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)
            discriminant = b ** 2 - 4 * a * c
            if discriminant >= 0:
                break
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        question = f"Find the roots of this function: {a}x^2 + {b}x + {c}"
        answer = [root1, root2]
    elif topic == 11:
        a = (round(random.uniform(-20, 20), 1), round(random.uniform(-20, 20), 1))
        b = (round(random.uniform(-20, 20), 1), round(random.uniform(-20, 20), 1))
        question = f"Find the distance between {a} and {b}."
        answer = math.dist(a, b)
    elif topic == 12:
        b = random.randint(1, 20)
        a = b ** 0.5 if b in [1, 4, 9, 16] and random.random() > 0.75 else b ** random.randint(-2, 4)
        answer = math.log(a, b)
        question = f"Evaluate log_{b} ({a})."
    elif topic == 13:
        if random.random() > 0.5:
            a, e, d = random.randint(10, 60), random.randint(10, 40), random.randint(3, 9)
            simplified = a % d
            answer = pow(simplified, e, d)
            question = f"What is the remainder of {a}^{e} / {d}?"
        else:
            a, b, c, d = random.randint(10, 200), random.randint(10, 200), random.randint(10, 200), random.randint(2,
                                                                                                                   20)
            answer = (a * b * c) % d
            question = f"What is the remainder of ({a} * {b} * {c}) / {d}?"
    elif topic == 14:
        digits = "0123456789"
        a, b, c = random.randint(10, 100), random.randint(2, 10), random.randint(2, 10)
        while b == c:
            c = random.randint(2, 10)
        f = sum(int(digit) * (b ** e) for e, digit in enumerate(reversed(str(a))))
        answer = ""
        while f > 0:
            remainder = f % c
            answer = digits[remainder] + answer
            f = f // c
        question = f"Convert {a} (base {b}) to base {c}."
    elif topic == 15:
        m = [random.randint(2, 10) for _ in range(3)]
        while not all(math.gcd(m[i], m[j]) == 1 for i in range(len(m)) for j in range(i + 1, len(m))):
            m = [random.randint(2, 10) for _ in range(3)]
        remainders = [random.randint(0, m[i] - 1) for i in range(len(m))]
        M = 1
        for modulus in m:
            M *= modulus
        answer = 0
        for i in range(len(m)):
            Mi = M // m[i]
            Mi_inv = pow(Mi, -1, m[i])
            answer += remainders[i] * Mi * Mi_inv
        answer = (answer % M, M)
        question = f"Solve the system x ≡ {remainders[0]} (mod {m[0]}), x ≡ {remainders[1]} (mod {m[1]}), x ≡ {remainders[2]} (mod {m[2]})"
    elif topic == 16:
        variation = random.randint(1, 3)
        if (variation == 1):
            a = random.randint(-16, 16)
            b = random.randint(-16, 16)
            c = random.randint(-40, 40)
            solutions = []
            constant = c + a * b
            for factor1 in range(1, abs(constant) + 1):
                if constant % factor1 == 0:
                    factor2 = constant // factor1
                    x = factor1 - b
                    y = factor2 - a
                    if (x * y + a * x + b * y == c):  #pos
                        solutions.append((x, y))  # use as 4
                    x = -factor1 - b
                    y = -factor2 - a
                    if (x * y + a * x + b * y) == c:  #neg
                        solutions.append((x, y))
            answer = len(solutions)
            question = f"How many solution pairs are there for the equation xy + {a}x + {b}y = {c}?"
        elif (variation == 2):
            a = random.randint(-16, 16)
            b = random.randint(-16, 16)
            c = random.randint(-40, 40)
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
        elif (variation == 3):
            a = random.randint(-16, 16)
            b = random.randint(-16, 16)
            c = random.randint(-40, 40)
            solutions = []
            constant = c + a * b
            for factor1 in range(1, abs(constant) + 1):
                if constant % factor1 == 0:
                    factor2 = constant // factor1
                    x = factor1 - b
                    y = factor2 - a
                    if (x * y + a * x + b * y == c):  #pos
                        solutions.append((x, y))  # use as 4
                    x = -factor1 - b
                    y = -factor2 - a
                    if (x * y + a * x + b * y) == c:  #neg
                        solutions.append((x, y))
            answer = solutions
            question = f"Type in one solution pair for the equation xy + {a}x + {b}y = {c}. If there are none, press Enter."
    elif topic == 17:
        while True:
            a, b, c = random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)
            discriminant = b ** 2 - 4 * a * c
            if discriminant >= 0:
                break
        if(random.randint(1, 4) == 1):
            question = f"Suppose x1 and x2 are the roots of {a}x^2 + {b}x + {c}.\nFind the value of x1^2*x2 + x1*x2^2."
            answer = (c/a) * (-b/a)
        if(random.randint(1, 4) == 2):
            question = f"Suppose x1 and x2 are the roots of {a}x^2 + {b}x + {c}.\nFind the value of (x1-x2)^2."
            answer = (-b/a)**2 - 4*(c/a)
        if(random.randint(1, 4) == 3):
            question = f"Suppose x1 and x2 are the roots of {a}x^2 + {b}x + {c}.\nFind the value of (x1+x2)^(x1*x2)."
            answer = (-b/a)**(c/a)
        if(random.randint(1, 4) == 4):
            question = f"Suppose x1 and x2 are the roots of {a}x^2 + {b}x + {c}.\nFind the value of 1/x1 + 1/x2."
            answer = (-b/a) / (c/a)
    elif topic == 18:
        ab = random.randint(1, 25)
        bc = random.randint(1, 25)
        cd = random.randint(1, 25)
        ad = random.randint(1, 25)
        question = f"Find the area of the cyclic quadrilateral ABCD where AB = {ab}, BC = {bc}, CD = {cd}, AD = {ad}"
        s = (ab + bc + cd + ad) / 2
        answer = math.sqrt((s - ab) * (s - bc) * (s - cd) * (s - ad))
    elif topic == 19:
        a = random.randint(40, 99)
        b = random.randint(4, 10)
        k = 1
        answer = 0
        while b ** k <= a:
            answer += a // b ** k
            k += 1
        question = f"Given n ∈ Z and ({a}!)/{b}^n ∈ Z, what is the maximum value of n?"
    elif topic == 21:
        sides = random.randint(3, 10)
        colors = random.randint(2, 5)
        question = (f"Consider a regular {sides}-gon. How many distinct ways can you color the vertices of the {sides}-"
                    f"gon using {colors} colors if two colorings are considered the same if one can be obtained from "
                    f"the other by a rotation?") #add more variations ts is boring af
        totalc = 0
        for i in range(sides):
            # Rotato by k*(360/sides) deg
            if sides % (i + 1) == 0:
                cycles = sides // (i + 1)
                fixed_colorings = colors ** cycles
                totalc += fixed_colorings
            else:
                fixed_colorings = 0
                totalc += fixed_colorings
        answer = totalc // sides
    elif topic == 22:
        if(random.random() > 0.5):
            bd = random.randint(1, 15)
            dc = random.randint(1, 15)
            ad = random.randint(1, 15)
            ac = random.randint(1, 15)
            bc = bd + dc
            try:
                answer = (ad**2 * bc + bd * dc * bc - ac**2 * bd) / dc
            except:
                answer = ""
            question = f"In triangle ABC, D is a point on BC such that BD = {bd} and DC = {dc}. If AD = {ad} and AC = {ac}, find the length of AB.\nIf AB does not exist, press Enter."
        else:
            bd = random.randint(1, 15)
            dc = random.randint(1, 15)
            ad = random.randint(1, 15)
            ab = random.randint(1, 15)
            bc = bd + dc
            try:
                answer = (ad**2 * bc + bd * dc * bc - ab**2 * dc) / bd
            except:
                answer = ""
            question = f"In triangle ABC, D is a point on BC such that BD = {bd} and DC = {dc}. If AD = {ad} and AB = {ab}, find the length of AC.\nIf AC does not exist, press Enter."
    elif topic == 23:
        if(random.random() > 0.5):
            while True:
                m = random.randint(5, 30)
                n = random.randint(5, 30)
                if math.gcd(m, n) == 1:
                    break
            question = (f"A fast-food restaurant sells Chicken McNuggets in boxes of {m} and {n}.\n"
                        f"What is the largest number of Chicken McNuggets that cannot be bought exactly\n"
                        f"using a combination of these two boxes?")
            answer = m * n - m - n
        else:
            while True:
                m = random.randint(5, 30)
                n = random.randint(5, 30)
                if math.gcd(m, n) == 1:
                    break
            limit = random.randint(40, 200)
            question = (f"A fast-food restaurant sells Chicken McNuggets in boxes of {m} and {n}.\n"
                        f"How many different quantities of Chicken McNuggets can be bought exactly \n"
                        f"using a combination of these two box sizes, if you are allowed to buy at\n"
                        f"most {limit} Chicken McNuggets?")
    else:
        print(cl.RED + "Well, this is awkward." + cl.END)
        print("Something went wrong here. Tell Jason he made a fucky-wucky.")
        question = ""
        answer = 0

    return question, answer

def loadlevel(level, points=points):
    if 1 <= level < 4:
        index = 8
    elif 5 <= level < 7:
        index = 13
    elif 8 <= level < 10:
        index = 18
    elif 11 <= level <= 15:
        index = 23
    else:
        raise ValueError("Invalid level")

    print("Successfully loaded Level " + str(level) + "!")
    print("This level has " + cl.BOLD + f"{10 + (level * 1) // 3}" + cl.END + " questions.")
    asd = input("Ready to begin? ")
    for i in range(10 + (level * 1) // 3 if level < 11 else 20 + 2*(level-10)):
        correct = 0
        topicindex = random.randint(0, index)
        if level > 4 and topicindex < index // 2:
            topicindex = random.randint(level - 1, index)
        if level > 10 and topicindex < 18:
            topicindex = random.randint(12, index)

        timer = round(((index**2)/8 - 6) + 9, 1)
        print(f"Question {i + 1}")
        print(cl.LIGHT_GRAY + f"Topic code: {topics[topicindex]}" + cl.END)
        q = generatequestion(topicindex)
        print("\n" + q[0])
        time.sleep(3)
        print("\n Your three seconds of grace time has ended! The timer (" + str(timer) + "s) has started now.")
        start = time.time()
        response = input()
        end = time.time()
        if type(q[1]) == int or type(q[1]) == float:
            if abs(float(response) - q[1]) < 0.01:
                points += 5
                correct = 1
                print(cl.GREEN + "CORRECT! (5 points)" + cl.END)
                print(f"Difficulty multiplier: {20 / (1 + math.exp(-0.7 * (level - 9)))} extra points added for level {level}!")
                points += 20 / (1 + math.exp(-0.7 * (level - 9)))
            else:
                print(cl.RED + "INCORRECT! (0 points)" + cl.END)
        elif response == str(q[1]):
            points += 5
            correct = 1
            print(cl.GREEN + "CORRECT! (5 points)" + cl.END)
            time.sleep(1)
            print(f"Difficulty multiplier: {20 / (1 + math.exp(-0.7 * (level - 9))):.0f} extra points added for level {level}!\n")
            points += round(20 / (1 + math.exp(-0.7 * (level - 9))), 0)
        else:
            print(cl.RED + "INCORRECT! (0 points)" + cl.END)
        if end - start < timer and correct == 1:
            print("TIME BONUS! Bonus points being calculated....")
            time.sleep(1.5)
            if 0.6 * timer > end - start:
                print(cl.YELLOW + "Lightning!" + cl.END + f"You finished in {end - start:.2f} seconds. 5 points!")
                points += 5
            elif 0.8 * timer > end - start:
                print(cl.YELLOW + "Speedy!" + cl.END + f"You finished in {end - start:.2f} seconds. 3 points!")
                points += 3
            else:
                print(f"Fast! You finished in {end - start:.2f} seconds. 1 point!")
                points += 1

        input(f"Press Enter to begin the next question. You have finished {i + 1} question(s).")

def play_math():
    print("WELCOME TO MATH MANIA!\n")
    time.sleep(1)
    print("There are 15 levels of math-ness,")
    print("24 topics of varying difficulty,")
    print("and INFINITE randomly-generated problems!\n")
    time.sleep(3)
    while True:
        choice = input("Type a math level, 1-15, or type \"score\" to view your points! Type \"quit\" to exit. ")
        print("\n\n" + cl.LIGHT_GREEN + "Levels 1-3" + cl.END + " are for those who want to relax.")
        print(cl.BLUE + "Levels 4-6" + cl.END + " are for those who want to play a little harder.")
        print(cl.YELLOW + "Levels 7-10" + cl.END + " are for those who want a challenge.")
        print(cl.RED + cl.BOLD + "Levels 11-15 are reserved for those who dare." + cl.END)

        try:
            choice = int(choice)
            loadlevel(choice)
        except:
            if(choice == "score"):
                print("You currently have " + str(points) + " points. Get out there and get some more! (Enter to return to menu)")
                asd = input()
            elif(choice == "quit"):
                print(cl.YELLOW + cl.END + "\nThanks for playing!" + cl.END)
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    play_math()




