import math

def makeChange(cents):
    coins = {};
    if cents/100 >= 1:
        coins["dollars"] = math.floor(cents/100);
        cents = cents % 100
    if cents/50 >= 1:
        coins["half-dollars"] = math.floor(cents/50);
        cents = cents % 50
    if cents/25 >= 1:
        coins["quarters"] = math.floor(cents/25);
        cents = cents % 25
    if cents/10 >= 1:
        coins["dimes"] = math.floor(cents/10);
        cents = cents % 10
    if cents/5 >= 1:
        coins["nickels"] = math.floor(cents/5);
        cents = cents % 5
    if cents/1 >= 1:
        coins["pennies"] = math.floor(cents/1);
        cents = cents % 1

    return coins


print(makeChange(45))
print(makeChange(1231233))
print(makeChange(65423567))
print(makeChange(10000))
