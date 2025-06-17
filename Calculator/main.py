from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2


def calculator():
    print(logo)
    cont = "y"
    result = 0
    a=float(input("What's the first number?: "))
    while cont=="y":

        op=input("""+
-
*
/
Pick an operation: """)
        b=float(input("What's the second number?: "))

        operations={"+":add(a,b),
                    "-":sub(a,b),
                    "*":mul(a,b),
                    "/":div(a,b),}

        for opr in operations:
            if op==opr:
                result=(operations[opr])
                print(f"{a}{op}{b}={result}")

        cont=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if cont=="y":
            a=result
        else:
            print("\n"*20)
            calculator()

calculator()

