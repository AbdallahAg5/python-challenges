def print_full_name(first, last):
    if len(first) <=10 and len(last) <= 10:
           print("Hello " + first + " " + last + "! You just delved into python.")
           return 'nice'

first_name = input()
last_name = input()
print_full_name(first_name, last_name)