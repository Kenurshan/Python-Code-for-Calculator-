def select_op(choice):
    if choice == "+":
        answer = float(oprd1) + float(oprd2)
        print(float(oprd1), choice, float(oprd2), "=", answer)
    elif choice == "-":
        answer = float(oprd1) - float(oprd2)
        print(float(oprd1), choice, float(oprd2), "=", answer)
    elif choice == "*":
        answer = float(oprd1) * float(oprd2)
        print(float(oprd1), choice, float(oprd2), "=", answer)
    elif choice == "/":
        if oprd2 == "0":
            print("float division by zero")
            print(float(oprd1), choice, float(oprd2), "= None")
        else:
            answer = float(oprd1) / float(oprd2)
            print(float(oprd1), choice, float(oprd2), "=", answer)
    elif choice == "^":
        answer = float(oprd1) ** float(oprd2)
        print(float(oprd1), choice, float(oprd2), "=", answer)
    elif choice == "%":
        answer = float(oprd1) % float(oprd2)
        print(float(oprd1), choice, float(oprd2), "=", answer)
    else:
        print("Unrecognized operation")
    return

def ctrl(choice):
  if choice == "#":
        print("Done. Terminating")
        exit()
  elif choice == "$":
        main()
  return

def main():
  while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
  
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    ctrl(choice)
    
    global oprd1
    oprd1 = input("Enter first number: ")
    for i in oprd1:
      if i == "$":
        main()
      elif i == "#":
        print(oprd1)
        print("Done. Terminating")
        exit()
      else:
        print(oprd1)
        continue
    global oprd2
    oprd2 = input("Enter second number: ")
    for x in oprd2:
      if x == "$":
        main()
      elif x == "#":
        print(oprd2)
        print("Done. Terminating")
        exit()
      else:
        print(oprd2)
        continue
    select_op(choice)
    
main()



