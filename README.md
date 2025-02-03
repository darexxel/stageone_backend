
# Number Classification API

## Overview

This API takes a number and returns interesting mathematical properties about it, along with a fun fact. It is built using Django and Django REST framework and deployed on Vercel.

## Features

- Accepts GET requests with a number parameter.
- Returns JSON responses with mathematical properties and a fun fact.
- Handles CORS (Cross-Origin Resource Sharing).
- Provides appropriate HTTP status codes.

## API Specification

### Endpoint

`GET /api/classify-number?number=<number>`

### Response Format

#### Success (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}

```

## Example Usage

### Valid Request

```bash
curl "https://backendhngzero.vercel.app/api/classify-number?number=371"
```

### Error Response

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Invalid Request

```bash
curl "https://backendhngzero.vercel.app/api/classify-number?number=abc"
```

### Response

```json
{
    "number": "abc",
    "error": true
}
```

## Local Development

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- django-cors-headers
- requests

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/darexxel/stageone_backend
    cd stageone_backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server:

    ```bash
    python manage.py runserver
    ```

5. Access the API at:

    ```plaintext
    http://localhost:8000/api/classify-number?number=371
    ```

## Deployment

### Vercel

1. Install Vercel CLI:

    ```bash
    npm i -g vercel
    ```

2. Deploy:

    ```bash
    vercel
    ```

## License

This project is licensed under the MIT License.
