import random
majus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minus = "abcdefghijklmnopqrstuvwxyz"
numb = "123456789"
symbol = "&é(-è_çà)=~#{[|\+@]}*$^ù!:;µ£%§/?¤"
ch = ""
all = majus + minus + numb + symbol
normal_text = minus + majus
minus_majus_numbers = minus + majus + numb
majus_numbers = majus + numb
minus_numbers = minus + numb
text_symbol = minus + majus + symbol
majus_symbol = majus + symbol
minus_symbol = minus + symbol
numb_symbol = numb + symbol


n = int(input("\033[91m{}\033[00m".format("type the length of your password: ")))

print("all (1)")
print("minus(2)")
print("majus (3)")
print("numb (4)")
print("symbol (5)")
print("normal_text(6)")
print("minus_majus_numbers (7)")
print("majus_numbers (8)")
print("minus_numbers (9)")
print("text_symbol (10)")
print("majus_symbol (11)")
print("minus_symbol (12)")
print("numb_symbol (13)")
while True:
    type = int(input("give the type of your password: "))
    if type <= 13 and type != 0:
        break

if type == 1:
    for i in range(0, n - 1):
        ch = ch + all[random.randint(0, len(all) - 1)]

if type == 2:
    for i in range(0, n - 1):
        ch = ch + minus[random.randint(0, len(minus) - 1)]

if type == 3:
    for i in range(0, n - 1):
        ch = ch + majus[random.randint(0, len(majus) - 1)]

if type == 4:
    for i in range(0, n - 1):
        ch = ch + numb[random.randint(0, len(numb) - 1)]

if type == 5:
    for i in range(0, n - 1):
        ch = ch + symbol[random.randint(0, len(symbol) - 1)]

if type == 6:
    for i in range(0, n - 1):
        ch = ch + normal_text[random.randint(0, len(normal_text) - 1)]

if type == 7:
    for i in range(0, n - 1):
        ch = ch + minus_majus_numbers[random.randint(0, len(minus_majus_numbers) - 1)]

if type == 8:
    for i in range(0, n - 1):
        ch = ch + majus_numbers[random.randint(0, len(majus_numbers) - 1)]

if type == 9:
    for i in range(0, n - 1):
        ch = ch + minus_numbers[random.randint(0, len(minus_numbers) - 1)]

if type == 10:
    for i in range(0, n - 1):
        ch = ch + text_symbol[random.randint(0, len(text_symbol) - 1)]

if type == 11:
    for i in range(0, n - 1):
        ch = ch + majus_symbol[random.randint(0, len(majus_symbol) - 1)]

if type == 12:
    for i in range(0, n - 1):
        ch = ch + minus_symbol[random.randint(0, len(minus_symbol) - 1)]

if type == 13:
    for i in range(0, n - 1):
        ch = ch + numb_symbol[random.randint(0, len(numb_symbol) - 1)]

print("The Password is: ", ch)
print("Hope you enjoy the bot By malek maghraoui ;)")


