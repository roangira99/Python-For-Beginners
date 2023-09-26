# Collatz's hypothesis program
c0 = int(input("Please enter a number (should not be negative or zero): "))
steps = 0

while c0 <= 0:
    print("Invalid number! Please try again.")
    c0 = int(input("Please enter a number (should not be negative or zero): "))
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
            print(c0)
            steps += 1
        else:
            c0 = 3 * c0 + 1
            print(c0)
            steps += 1

print("steps =", steps)