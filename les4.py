
# Write a function that checks whether a passed string is palindrome or not
import pi as pi


def is_palindrome(s):
  if len(s) == 0:
    return True
  else:
    if s[0] == s[-1]:
      return is_palindrome(s[1:len(s)-1])
    else:
      return False

s = "minim"
if is_palindrome(s) == 1:
  print(s, 'is a palindrome')
else:
  print(s, 'is not a palindrome')

#Write a function that computes the volume of a sphere given its radius.
#The volume of the sphere = V
pi = 3.14
radius = 2
V = (4/3)*pi*(radius**3)
print("The Volume of the sphere is:", V)

#
def show_employee_basic_data( name , age):
  print(name, "is a", age)
  name = "Hayk"
  show_employee_basic_data("Hayk" , 23)

#
  def show_employee(name, salary=9000):
    print(name)
    print(salary)


    

