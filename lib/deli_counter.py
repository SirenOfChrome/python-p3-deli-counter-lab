# lib/deli_counter.py

# define an empty list to represent the line
katz_deli = []

def line(line):
    if not line:
        print("The line is currently empty.")
    else:
        line_text = "The line is currently:"
        for i, name in enumerate(line):
            line_text += f" {i+1}. {name}"
        print(line_text)

def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(line):
    if not line:
        print("There is nobody waiting to be served!")
    else:
        next_customer = line.pop(0)
        print(f"Currently serving {next_customer}.")
#GDC8