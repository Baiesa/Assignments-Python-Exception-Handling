'''
Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, 
regardless of the outcome of the calculation.


'''

def calculate_adjustment_factor(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
        return None
    except ArithmeticError:
        print("Arithmetic error occurred during calculation.")
        return None

def main():
    try:
        original_servings = float(input("Enter the number of servings the recipe is originally for: "))
        desired_servings = float(input("Enter the number of servings you wish to make: "))
    except ValueError:
        print("Please enter valid numerical values for servings.")
        return

    adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
    if adjustment_factor is not None:
        print("Adjusted recipe quantities:")
        # Assuming there's a list of ingredients and quantities, adjust each quantity
        # and print the adjusted quantities to the user
        print("- Adjusted quantities based on {:.2f} servings:".format(desired_servings))
        # Adjust quantities here
    else:
        print("Failed to calculate adjustment factor.")

  

if __name__ == "__main__":
    main()