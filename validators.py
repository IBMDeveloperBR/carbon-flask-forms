import re

def dropsqlsyntax(input: str) -> str:
    sqlsyntax = ['SELECT', 'DELETE', 'CREATE', 'DROP', 'UPDATE', 'TABLE',
                 'select', 'delete', 'create', 'drop', 'update', 'table']
    # Eliminates SQL syntax words from the input str
    for str_to_be_replaced in sqlsyntax:
        input = input.replace(str_to_be_replaced, '')
    return input

def drophtmltags(input: str) -> str:
    # Eliminates HTML tags from the input str
    input = re.sub('<.*?>', '', input)
    return input

def validate_email(email: str) -> bool:
    # Check email syntax with a simple regex
    rgx = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    if re.match(rgx, email) == None:
        return False
    # Check input size
    elif len(email) < 1 or len(email) > 110:
        return False
    # SMTP ping input email
    else:
        # TODO
        return True

def validate_name(name: str) -> bool:
    # Cleansing user input
    name = re.sub(r'[^a-zA-Z àèìòùáéíóúäëïöüãõâêîôûç]', '',
                  re.sub(' +', ' ', name.strip()))
    # Validating input size and if surname was provided
    if len(name) < 1 or len(name) > 110 or ' ' not in name:
        return False
    return True

def validate_cpf(cpf: str) -> bool:
    # Limpeza da input
    cpf = re.sub(r'[^0-9]', '', cpf.strip())
    numbers = [int(digit) for digit in cpf]
    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False
    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    return True