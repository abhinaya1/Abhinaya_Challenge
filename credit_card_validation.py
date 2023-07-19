import re

def validate_credit_card(card_number):
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

n = int(input().strip())
for _ in range(n):
    card_number = input().strip()
    print(validate_credit_card(card_number))
