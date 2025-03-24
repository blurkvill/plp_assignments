
# Question 1: Creating a new file and writing in it
with open('/home/the_blurkville/Documents/PLP Assignments/python_week_4_assignment/file_handling.txt', 'w') as file:
    file.write('random content')

# Question 2: Handling exceptions
file_name = input("What is the name of the file you'd like to open? ")

if not file_name.endswith('.txt'):
    file_name += '.txt'

try:
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error. The file does not exist. Check file name again. ")
