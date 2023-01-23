#-----------------------------------------------------
# Homework: Debugging
# Debug the following Python script
# 25 points total (1 point = 4% of grade)

# For each correction, use the comment symbol (#) to explain the debug.
# No comments, no credit.
#-----------------------------------------------------

# 1: Solving simple math:
# (1 point)
x = 2
y = 5
z = x + y
prnit(z)

# 2: Strings and data
# (2 points)
w = input("enter any number")
u = input("enter another number")
answer = w+u;
print(answer)

#--------------
# ignore this:
del w,u,z,y,x
#--------------

# 3: IF Statements
# (5 points)

price = input("What is the most you would pay for a pizza topping?: ")
if price = 1.5
print(That's about right)
elif price>1.5
print("That's too much")
else
print("Less than $1.50 would be great")

# 4: Loops
# (7 points)

# Below is a code to calculate the sum of any number, n, from 0 to n with all integers between.
# Example: if n= 10, the answer = 10+9+8+7+6+...+1+0 = 55

n = input("For what number would you like to find the cumulative sum?: ")
anwser = 0
for i in range(1, n+1)
answer = answer + 1
print("the answer is:" + answer)

#--------------
# ignore this:
del answer
#--------------

# 5: Function
# (10 points)

# Fix this code to calculate the area of a triangle.
# Also add code that gives a "DNE" (does not exist) message if the input to base or height is negative.
def trianglearea(x,y)
return(0.5*x*y)

base = input("what is the base of your triangle?: ")
height = input("what is the height of your triangle?: ")

result = trianglearae(x,y)
print("The area of the triangle is: " + result)

#--------------------------------------------------------
# End of assignment
#--------------------------------------------------------
