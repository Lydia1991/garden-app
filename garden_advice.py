"""
garden_advice.py
A simple script to provide gardening tips based on the month and season.

TODO: Refactor repeated code into functions.
TODO: Add docstrings and comments for clarity.
TODO: Replace hardcoded tips with a data structure.
"""

# Hardcoded gardening tips by month
month = input("Enter the current month: ").strip().lower()

if month in ["december", "january", "february"]:
    print("It's winter. Protect your plants from frost and avoid overwatering.")
elif month in ["march", "april", "may"]:
    print("It's spring. Time to plant new seeds and prune shrubs.")
elif month in ["june", "july", "august"]:
    print("It's summer. Water your garden regularly and watch for pests.")
elif month in ["september", "october", "november"]:
    print("It's autumn. Rake leaves and prepare your garden for winter.")
else:
    print("Invalid month entered. Please try again.")
