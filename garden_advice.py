"""
garden_advice.py

This script provides gardening tips and advice based on the month and season.

Functions:
    get_gardening_advice(month): Returns gardening advice for the given month.

Usage:
    Run the script and enter the current month when prompted to receive gardening tips.
"""

def get_gardening_advice(month):
    """
    Returns gardening advice based on the provided month.

    Args:
        month (str): The name of the month (e.g., 'January').

    Returns:
        str: Gardening advice for the given month/season.
    """
    # Normalize the input to lowercase and remove extra spaces
    month = month.strip().lower()
    # Winter advice
    if month in ["december", "january", "february"]:
        return "It's winter. Protect your plants from frost and avoid overwatering."
    # Spring advice
    elif month in ["march", "april", "may"]:
        return "It's spring. Time to plant new seeds and prune shrubs."
    # Summer advice
    elif month in ["june", "july", "august"]:
        return "It's summer. Water your garden regularly and watch for pests."
    # Autumn advice
    elif month in ["september", "october", "november"]:
        return "It's autumn. Rake leaves and prepare your garden for winter."
    # Invalid input
    else:
        return "Invalid month entered. Please try again."

# Prompt the user for the current month
month = input("Enter the current month: ")
# Get gardening advice for the entered month
advice = get_gardening_advice(month)
# Display the advice to the user
print(advice)
