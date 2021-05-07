from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    operand1 = int(request.GET["operand1"])
    operand2 = int(request.GET["operand2"])
    operator = request.GET["operator"]
    
    result = 0
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            result = "division by zero ＼（〇_ｏ）／"
        else:
            result = operand1 / operand2
    
    return render(request, "result.html", {"result":result})