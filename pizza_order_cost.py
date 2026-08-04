"""
    Program Requirements: 
    - Use Python's input() function to gather user data.    
    - Implement conditional statements (if-elif) to make decisions based on input.
    - Perform arithmetic calculations to determine costs.
    - Use f-strings for formatted output.
    - Apply problem-solving skills to create a functional program.

    Pricing rules: 
        Pizza sizes and base prices:
            - Small pizza: $8
            - Large pizza: $12

        Toppings: $1 for each additional topping
        
        Delivery fee:
            - $2 for the first 5 miles
            - $1 for each additional mile

"""
print("Hello! Welcome to Python Pizza Shop!")
pizza_size = int(input("Would you like to order a small or large pizza? Press 1 for small or 2 for large: "))
num_toppings = int(input("How many toppings would you like on your pizza? "))
delivery_distance = int(input("How far away do you live from the shop? "))

# Base cost of a large or small pizza
if pizza_size == 1: 
    pizza_size = "small"
    base_cost = 8
elif pizza_size == 2:
    pizza_size = "large"
    base_cost = 12
else:
    print("That's an invalid input please try again.")

# Calculate cost of toppings
cost_of_toppings = num_toppings * 1 # $1 per topping

# Calculate delivery fee
if delivery_distance <= 5:
    delivery_fee = 2 # $2 for first 5 miles
else:
    delivery_fee = 2 + ((delivery_distance - 5) * 1) # $1 for each additional mile after 5


# Calculate total cost
total_cost = base_cost + cost_of_toppings + delivery_fee

print(f"You ordered a {pizza_size} pizza with {num_toppings} topping(s). The total will be ${total_cost}.")



 