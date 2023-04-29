import re

def arithmetic_arranger(problems, doSum = False):
  final_str = ""
  #Error Check
  if(len(problems) > 5):
    return "Error: Too many problems."
    
  opndList = checkOperator(problems)
  if opndList == False:
    return "Error: Operator must be '+' or '-'."
      
  numList = checkNumber(problems)
  if isinstance(numList, str): return numList

  #Calculate Space and dash
  j = 0
  sum = []
  spaceBefore1 = []
  spaceBefore2 = []
  dash = []
  
  for i in range(0, len(numList), 2):
    dash.append(max(len(numList[i]), len(numList[i+1])) + 2)
    
    if(len(numList[i]) == len(numList[i+1])):
      spaceBefore1.append(2)
      spaceBefore2.append(1)
      
    if(len(numList[i]) > len(numList[i+1])):
      spaceBefore1.append(2)
      spaceBefore2.append(len(numList[i])+1 - len(numList[i+1]))
      
    if(len(numList[i]) < len(numList[i+1])):
      spaceBefore1.append(len(numList[i+1])+2 - len(numList[i]))
      spaceBefore2.append(1)

    if doSum == True:
      if(opndList[j] == "+"): sum.append(str(int(numList[i]) + int(numList[i+1])))
      if(opndList[j] == "-"): sum.append(str(int(numList[i]) - int(numList[i+1])))
      j  = j + 1

  #Print Line 1
  j = 0
  #print(spaceBefore1[j])
  for i in range(0, len(numList), 2):
    for k in range(spaceBefore1[j]):
      final_str = final_str + " "
      
    j = j + 1
    final_str = final_str + numList[i]
    if(i != len(numList) - 2):
        final_str = final_str + "    "
      
  final_str = final_str + "\n"  
  #Print Line 2
  j = 0
  for i in range(1, len(numList), 2):
    final_str = final_str + opndList[j]
    for k in range(spaceBefore2[j]):
      final_str = final_str + " "
      
    j = j + 1
    final_str = final_str + numList[i]
    if(i != len(numList) - 1):
        final_str = final_str + "    "
      
  #Print Dash
  final_str = final_str + "\n"  
  for i in range(len(dash)):
    for j in range(dash[i]):
      final_str = final_str + "-"
  
    if i != len(dash) - 1:
      final_str = final_str + "    "
      
  #Print Answer
  if doSum == True:
    final_str = final_str + "\n" 
    for i in range(len(dash)):
      for j in range(dash[i] - len(sum[i])):
        final_str = final_str + " "
        
      final_str = final_str + sum[i]
      if(i != len(dash) -1):
        final_str = final_str + "    "
        
  return final_str


def checkOperator(problems):
  x = []
  for eqn in problems:
    for i in eqn:
      if(i == "*" or i == "/"):
        return False
      if(i == "+" or i=="-"):
        x.append(i)
  return x
  
def checkNumber(problems):
  y = []
  for eqn in problems:
    z = re.findall("[^\s0-9+-]", eqn)
    if len(z):
      return "Error: Numbers must only contain digits."
    
    x = re.findall("[0-9]+", eqn)
    y = y + x
    
    for num in y:
      if len(num) > 4:
        return "Error: Numbers cannot be more than four digits."

  return y

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))