# This program will query a user for their phone number, SSN, and zip code.
# Using regular expression, it will validate the inputs of each, mathing them with common patterns.
# accepting both spaces and hyphens between digit blocks.


# imports the regular-expression package for future use.
import re

# Checks if the phone number is valid, accepting formats with and without minus sign.
def validate_phone(phone_number):
    # Regular expression pattern for phone number, accepting formats of ###-###-#### and ### ### ####.
    pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d'

    # Checks if the phone number string fully matches the pattern
    if re.fullmatch(pattern, phone_number):

        # Returns true if it matches
        return True

    else:

        # Returns false if it doesnt match
        return False

# Checks if the SSN is valid, accepting formats with and without minus sign.
def validate_ssn(ssn):

    # Regular expression pattern for SSN, accepting formats of ###-##-#### and ### ## ####.
    pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d'

    # Checks if the ssn string fully matches the pattern
    if re.fullmatch(pattern, ssn):

        # Returns true if it matches
        return True

    else:

        # Returns false if it doesnt match
        return False

# Checks if the zip code is valid, accepting only one format.
def validate_zip(zip_code):
    # Regular expression pattern for zip, only accepting format of #####.
    pattern = r'\d\d\d\d\d'

    # Checks if the zip code string fully matches the pattern
    if re.fullmatch(pattern, zip_code):

        # Returns true if it matches
        return True

    else:

        # Returns false if it doesnt match
        return False


# Main function that query's user for input, and sends it to the other function to later receive true or false values.
def main():
    # Asks the user for their phone number
    phone_number = input('Enter your phone number (###-###-####): ')

    # Asks the user for their SSN
    ssn = input('Enter your social security number (###-##-####): ')

    # Asks the user for their zip code
    zip_code = input('Enter your zip code (#####): ')

    # Validates phone number, prints whether it is valid or invalid.
    if validate_phone(phone_number):
        print('Phone number is valid')
    else:
        print('Phone number is invalid')

    # Validates SSN, prints whether it is valid or invalid.
    if validate_ssn(ssn):
        print('Social security number is valid')
    else:
        print('Social security number is invalid')


    # Validates zip code, prints whether it is valid or invalid.
    if validate_zip(zip_code):
        print('Zip code is valid')
    else:
        print('Zip code is invalid')


# Run the program
main()