### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, resource in ingredients.items():
            if self.machine_resources[item] < resource:
                print(f"Sorry there is not enough {item}. ")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = coins-cost
            print(f"Here is your change: ${change:.2f} ")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, resource in order_ingredients.items():
            self.machine_resources[item] -= resource
        print(f"\n<{sandwich_size} sandwich is ready. Bon appétit!>")



sandwich = SandwichMachine(resources)
while True:
    response = input("What would you like? (small/medium/large/off/report): ").strip().lower()
    if response == "off":
        print("Turning off machine!")
        break
    elif response == "report":
        for item, resource in resources.items():
            print(f"{item}: {resource}")
    elif response == "small" or response == "medium" or response == "large":
        sandwich_recipe = recipes[response]
        if sandwich.check_resources(sandwich_recipe["ingredients"]):
            coins_inserted = sandwich.process_coins()
            if sandwich.transaction_result(coins_inserted, sandwich_recipe["cost"]):
                sandwich.make_sandwich(response, sandwich_recipe["ingredients"])
    else:
        print("Invalid response")

