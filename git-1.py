side_a = 10
side_b = 5
hypotenuse = (side_a**2 + side_b**2)**0.5
S = side_a * side_b // 2
print(hypotenuse)
print(S) 
a = {1, 2, 3}
b = {3, 4, 5}
print(b.difference(a))  # {1, 2}
print(b - a)  # {1, 2}

s = "Hello, World!"
first_five = s[:6]
print(first_five)  # Виведе 'Hello'

money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

fruit = 'apple'
for char in fruit:
    print(char)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
