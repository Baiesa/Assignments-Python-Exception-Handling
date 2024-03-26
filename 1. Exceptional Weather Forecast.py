'''
Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message if the user
 enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. 
Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, 
such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.

Add a finally block that thanks the user for using the weather forecast application, 
ensuring that this message is displayed regardless of whether an exception was caught or not.

'''
# # task 1 
# while True:
#     try:
#         tempreture_faranhite = float(input("enter the tempreture in faranhite."))
#         break
#     except ValueError:
#         print("please enter a numerical value for a tempreture. ")


# task 2

# def fahrenheit_to_celsius(fahrenheit):
#     try:
#         celsius = (fahrenheit - 32) * 5/9
#         return celsius
#     except ZeroDivisionError:
#         print("Error: Division by zero occurred.")
#     except OverflowError:
#         print("Error: Overflow occurred.")
#     except Exception as e:
#         print("An error occurred:", e)

# try:
#     fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print("Temperature in Celsius:", celsius)
# except ValueError:
#     print("Please enter a valid numerical value for the temperature.")

# task 3
def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except Exception as e:
        print("An error occurred during temperature conversion:", e)
        return None

def main():
    while True:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            break
        except ValueError:
            print("Please enter a numerical value for temperature.")

    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        print("The temperature in Celsius is {:.2f}°C".format(celsius))
    else:
        print("Temperature conversion failed.")

if __name__ == "__main__":
    main()

