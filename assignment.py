# Number Guessing Game

def number_guessing_game():
    import random
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()

# List Manipulation Example

def list_operations():
    # Create an empty list
    my_list = []

    # Append elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # Insert 15 at the second position
    my_list.insert(1, 15)

    # Extend the list with [50, 60, 70]
    my_list.extend([50, 60, 70])

    # Remove the last element
    my_list.pop()

    # Sort the list in ascending order
    my_list.sort()

    # Find and print the index of the value 30
    index_of_30 = my_list.index(30)
    print(f"The index of 30 in my_list is: {index_of_30}")

if __name__ == "__main__":
    list_operations()

# Discount Calculation Example

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

if __name__ == "__main__":
    try:
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)

        if discount_percentage >= 20:
            print(f"The final price after applying the discount is: {final_price}")
        else:
            print(f"No discount applied. The original price is: {original_price}")

    except ValueError:
        print("Error: Please enter valid numeric values for price and discount percentage.")

# File Read & Write Challenge

def file_read_write():
    """
    Reads content from an input file, modifies it, and writes the modified content to a new file.
    """
    try:
        input_file = input("Enter the name of the file to read from: ").strip()
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        output_file = input("Enter the name of the file to write to: ").strip()
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to {output_file}.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to the file.")

if __name__ == "__main__":
    file_read_write()
