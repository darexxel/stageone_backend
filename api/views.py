# views.py

import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .utils import is_prime, is_perfect, is_armstrong, digit_sum

@require_GET
def classify_number(request):
    # Get the 'number' query parameter.
    number_param = request.GET.get('number')
    try:
        number = int(number_param)
    except (ValueError, TypeError):
        # If conversion fails, return a 400 Bad Request with error info.
        response_data = {
            "number": number_param,
            "error": True
        }
        return JsonResponse(response_data, status=400)
    
    # Determine mathematical properties.
    prime_flag = is_prime(number)
    perfect_flag = is_perfect(number)
    armstrong_flag = is_armstrong(number)
    
    # Determine the properties field based on the requirements:
    # If the number is an Armstrong number, include "armstrong" and then "odd" or "even" based on its parity.
    # Otherwise, include only the parity.
    if armstrong_flag:
        properties = ["armstrong", "odd" if number % 2 != 0 else "even"]
    else:
        properties = ["odd" if number % 2 != 0 else "even"]
    
    # Compute digit sum.
    ds = digit_sum(number)
    
    # Get a fun fact using the Numbers API (math type).
    try:
        api_url = f"http://numbersapi.com/{number}/math"
        fun_fact_response = requests.get(api_url, timeout=2)
        # Use the returned text if the API call was successful.
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else ""
    except Exception:
        fun_fact = ""
    
    # Build the response data.
    response_data = {
        "number": number,
        "is_prime": prime_flag,
        "is_perfect": perfect_flag,
        "properties": properties,
        "digit_sum": ds,
        "fun_fact": fun_fact
    }
    
    # Create the JsonResponse and add CORS header.
    response = JsonResponse(response_data)
    response["Access-Control-Allow-Origin"] = "*"
    return response
