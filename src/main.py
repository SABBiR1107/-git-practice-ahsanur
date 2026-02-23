import datetime

from utils import add, subtract, multiply, divide

name = "Ahsanur Rahman"
print("My Name:", name)


today = datetime.date.today()
print("Today’s Date:", today)

print("Addition:", add(10, 20))
print("Subtraction:", subtract(10, 20))
print("Multiplication:", multiply(10, 20))
print("Division:", divide(10, 20))
