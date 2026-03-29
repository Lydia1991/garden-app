"""
garden_advice.py
A simple script to provide gardening tips based on the month and season.

TODO: Add docstrings and comments for clarity.
TODO: Replace hardcoded tips with a data structure.
"""

def get_gardening_advice(month):
    month = month.strip().lower()
    if month in ["december", "january", "february"]:
        return "It's winter. Protect your plants from frost and avoid overwatering."
    elif month in ["march", "april", "may"]:
        return "It's spring. Time to plant new seeds and prune shrubs."
    elif month in ["june", "july", "august"]:
        return "It's summer. Water your garden regularly and watch for pests."
    elif month in ["september", "october", "november"]:
        return "It's autumn. Rake leaves and prepare your garden for winter."
    else:
        return "Invalid month entered. Please try again."

month = input("Enter the current month: ")
advice = get_gardening_advice(month)
print(advice)
