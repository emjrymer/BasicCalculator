from django.shortcuts import render

# Create your views here.


def index_view(request):
    try:
        if request.method == "POST":
            operator = request.POST.get('operator')
            first = float(request.POST.get('input_number_1'))
            second = float(request.POST.get('input_number_2'))
            answer = 0
            if first and second:
                if operator == '+':
                    answer = first + second
                elif operator == '-':
                    answer = first - second
                elif operator == '*':
                    answer = first * second
                elif operator == '/':
                    if second == 0:
                        answer = "Can't divide by zero"
                    else:
                        answer = first / second
                elif operator == 'squared':
                    answer = first ** second
            return render(request, 'index.html', {'answer': answer, 'first': first, 'second': second, 'operator': operator})
        else:
            return render(request, 'index.html')
    except (ValueError, TypeError):
        answer = "Invalid Input"
        return render(request, 'index.html', {'answer': answer})

