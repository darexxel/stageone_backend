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

        # Keep properties array compact
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 else "even")

        # Ensure exact fun fact format for Armstrong numbers
        if is_armstrong(number):
            fun_fact = f"{number} is an Armstrong number because {' + '.join([f'{d}^3' for d in str(number)])} = {number}"
        else:
            response = requests.get(f'http://numbersapi.com/{number}/math')
            fun_fact = response.text if response.status_code == 200 else f"{number} is an interesting number"

        # Return exact JSON structure
        return Response({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": get_digit_sum(number),
            "fun_fact": fun_fact
        })
    except ValueError:
        return Response({
            "number": "alphabet",
            "error": True
        }, status=400)