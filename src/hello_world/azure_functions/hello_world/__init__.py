import logging

import azure.functions as func

VOWELS = {"a", "e", "i", "o", "u"}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not name:
        return func.HttpResponse("Unknown name")
    else:
        return func.HttpResponse(f"Hello {name}. Your name contains {calculate_vowels_in_name(name)} vowels")


def calculate_vowels_in_name(name: str) -> int:
    nr_vowels = 0
    for char in name:
        if char.lower() in VOWELS:
            nr_vowels += 1
    return nr_vowels
