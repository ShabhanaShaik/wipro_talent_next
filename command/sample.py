"""import sys
print("Script name:",sys.argv[0])
print("all args:",sys.argv[1:])
print("no of items:",len(sys.argv))
print("include file name:",sys.argv)
if len(sys.argv)>1:
  print("first arg:",sys.argv[1])
else:
  print("no arguments provided")


import sys
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print(num1+num2+num3)

import sys
if len(sys.argv) != 3:
     print("usage:python sample.py l b")
else:
  l=float(sys.argv[1])
  b=float(sys.argv[2])
  print("calculated area:",int(l*b))


import sys
if len(sys.argv)<2:
      print("Usage:python sample.py n1,n2,....")
      sys.exit()
numbers=[int(arg) for arg in sys.argv[1:]]
total=sum(numbers)
print("Numbers:",numbers)
print("Sum:",total)

import argparse
parser=argparse.ArgumentParser(description="Add 2 numbers")
parser.add_argument('--x',type=int,required=True,help="First number")
parser.add_argument('--y',type=int,required=True,help="Second number")
args=parser.parse_args()
result=args.x+args.y
print("Sum is",result)



#calc 
import argparse
parser=argparse.ArgumentParser(description="Add 2 numbers")
parser.add_argument('--x',type=int,required=True,help="First number")
parser.add_argument('--y',type=int,required=True,help="Second number")
parser.add_argument('--opt',type=str,required=True, choices= ['add','sub','mul','div'],help="Operation")
args=parser.parse_args()
if args.opt=='add':
  result=args.x + args.y
elif args.opt=='sub':
  result=args.x - args.y
elif args.opt=='mul':
  result=args.x * args.y
elif args.opt=='div':
  result=args.x / args.y
print("Result is",result)

#os module

#read and list the files in that folder which contains sample.py file(folder)
import os
path="."   #reads all the files in that folder and provides list of folders present in that particular folder 
files=os.listdir(path)
print("files and folders in current directory:")
for f in files:
   print(f)



#creates new folder in the folder which contains the sample.py files
import os

folder="new_folder"
if not os.path.exists(folder):
   os.mkdir(folder)
   print(f"Folder '{folder}' created.")
else:
   print(f"Folder '{folder}' already exists.")




#delete a file
#create a file in the folder before deleting!!!
import os
file="deletingfile.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"{file} deleted.")
else:
    print("file not found")"""

import os
file="shift.py"
if os.path.exists(file):
   size=os.path.getsize(file)
   print(f"{file} size:{size} bytes.")
else:
   print("file not Found")
























































