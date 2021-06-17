# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import math

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender =  input('\nWhat is your gender?(F/M) ')
    birthday =  input('Enter your birthdate(YYYY-MM-DD): ')
    weight =  float(input('Enter your weight(lbs): '))
    height =  float(input('What is your height?(inches) '))
    

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    age_years = compute_age(birthday)
    weight_kg = kg_from_lb(weight)
    height_cm = cm_from_in(height)
    bmi = body_mass_index(weight_kg, height_cm)
    

    # and basal_metabolic_rate functions as needed.
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age_years)

    # Print the results for the user to see.
    print(f'\nAge (years): {age_years}\nWeight (kg): {weight_kg:.3f}\nHeight (cm): {height_cm:.3f}')
    print(f'\nYour body mass index is: {bmi:.3f}\nYour body metabolic rate is: {bmr:.3f}')


def compute_age(birthday):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(weight):
    """Convert a mass in pounds to kilograms."""
    return  weight * .453592


def cm_from_in(height):
    """Convert a length in inches to centimeters."""
    return height * 2.54


def body_mass_index(weight_kg, height_cm):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    return (10000 * weight_kg) / height_cm**2


def basal_metabolic_rate(gender, weight_kg, height_cm, age_years):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * age_years
    elif gender.lower() == 'm':
        bmr = 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age_years
    
    return bmr

main()