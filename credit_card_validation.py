import re

def check_credit_card(card_number):
    # Remove hyphens
    card_number = card_number.replace("-", "")
    
    # Define the regular expression
    reg_exp = r'^[456]\d{3}(-?\d{4}){3}$'
    
    # Check for the starting digit, length and format
    if not re.match(reg_exp, card_number):
        return 'Invalid'
    
    # Check for repeated digits
    if re.search(r'(\d)\1{3,}', card_number):
        return 'Invalid'
    
    return 'Valid'
N = input('number of credit cards to test:')
N = int(N.strip())
for _ in range(N):
    card_number = input('credit card number:')
    card_number = card_number.strip()
    print(check_credit_card(card_number))
