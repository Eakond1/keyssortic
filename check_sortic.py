from sortic import *

number1 = []
number2 = []
sortirovka = []
num = 0
into = ""


while (num != '!'):
    num = input()
    if num != '!':
        int(num)
        number1.append(num)
sortirovka = number1.sort()
while (into != '*'):
    into = str(input())
    if into != '*':
        if into == "sa":
            sa(number1)
        elif into == "sb":
            sb(number2)
        elif into == "ss":
            ss(number1, number2)
        elif into == "pa":
            pa(number1, number2)
        elif into == "pb":
            pb(number1, number2)
        elif into == "ra":
            ra(number1)
        elif into == "rb":
            rb(number2)
        elif into == "rr":
            rr(number1, number2)
        elif into == "rra":
            rra(number1)
        elif into == "rrb":
            rrb(number2)
        elif into == "rrr":
            rrr(number1, number2)


if sortirovka == number1:
    print("OK")
else:
    print("KO")