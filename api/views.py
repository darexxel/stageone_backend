import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import is_armstrong, is_prime, is_perfect, get_digit_sum

@api_view(['GET'])
def classify_number(request):
    try:
        number = int(request.GET.get('number', ''))
    except ValueError:
        return Response({
            "number": request.GET.get('number', ''),
            "error": True
        }, status=status.HTTP_400_BAD_REQUEST)

    # Get fun fact from Numbers API
    response = requests.get(f'http://numbersapi.com/{number}/math')
    fun_fact = response.text if response.status_code == 200 else f"{number} is an interesting number"

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": get_digit_sum(number),
        "fun_fact": fun_fact
    }

    return Response(result)
