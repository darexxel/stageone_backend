import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import is_armstrong, is_prime, is_perfect, get_digit_sum

@api_view(['GET'])
def root_view(request):
    return Response({
        "message": "Number Classification API",
        "example": "/api/classify-number?number=371",
        "documentation": "https://github.com/darexxel/stageone_backend"
    })

@api_view(['GET'])
def classify_number(request):
    try:
        if 'number' not in request.GET:
            return Response({
                "number": "alphabet",
                "error": True
            }, status=400)

        number = int(request.GET.get('number', ''))
        abs_number = abs(number)  # Use absolute value for calculations

        # Keep properties array compact
        properties = []
        if is_armstrong(abs_number):  # Check armstrong using absolute value
            properties.append("armstrong")
        properties.append("odd" if abs_number % 2 else "even")

        # Ensure exact fun fact format for Armstrong numbers
        if is_armstrong(abs_number):
            fun_fact = f"{number} is an Armstrong number because {' + '.join([f'{d}^3' for d in str(abs_number)])} = {abs_number}"
        else:
            try:
                response = requests.get(f'http://numbersapi.com/{number}/math')
                fun_fact = response.text if response.status_code == 200 else f"{number} is an unremarkable number"
            except:
                fun_fact = f"{number} is an unremarkable number"

        digit_sum = get_digit_sum(abs_number)
        if number < 0:
            digit_sum = -digit_sum  # Make digit sum negative for negative numbers

        return Response({
            "number": number,
            "is_prime": False if number < 0 else is_prime(abs_number),  # Negative numbers can't be prime
            "is_perfect": False if number < 0 else is_perfect(abs_number),  # Negative numbers can't be perfect
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })
    except ValueError:
        return Response({
            "number": "alphabet",
            "error": True
        }, status=400)