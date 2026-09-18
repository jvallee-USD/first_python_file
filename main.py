# Prompt user for their name

name_input =str(input("Hello, and welcome to my first python program. \n\n Please state your name\n >>"))


# Prompt user for their favorite color 

print("\n Thank you for entering you name.\nNow, please enter a color \n")
print("- blue\n" \
"- red\n" \
"- orange\n" \
"- green\n" \
"- yellow\n" \
"")
color_input = str(input(">> "))

# Return name and favorite color, with the color applied to text
print(f"Hello, {name_input}! Your favorite color is {color_input}.")
