from django.shortcuts import render

def calculator(request):
    return render(request, "calculator.html")

def result(request):
    oper1 = int(request.GET['oper1'])
    operator = request.GET['operator']
    oper2 = int(request.GET['oper2'])
    if operator == "+":
        output = oper1 + oper2
    elif operator == "-":
        output = oper1 - oper2
    elif operator == "*":
        output = oper1 * oper2
    elif operator == "/" and oper2 != 0:
        output = oper1 / oper2
    else:
        output = "Division by zero"
    return render(request, "result.html", {'output' : output})