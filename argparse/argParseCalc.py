# importing argparse module  
import argparse  
parser = argparse.ArgumentParser()  
  
# creating two variables using the add_argument method  
parser.add_argument("num1", help = "first number")  
parser.add_argument("num2", help = "second number")  
parser.add_argument("operation", help = "operation")  
  
  
args = parser.parse_args()  
  
print(args.num1)  
print(args.num2)  
print(args.operation)  
  
n1 = int(args.num1)  
n2 = int(args.num2)  
  
  
if args.operation == "add":  
    result = n1 + n2  
    print("The Result is : ",result)  
  
elif args.operation == "sub":  
    result = n1 - n2  
  
elif args.operation == "mul":  
    result = n1 * n2  
elif args.operation == "div":  
    result = n1 / n2  
else:  
    print("Unmatched Argument")  
  
print("result is : ",result)  