import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
#sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = Cashier()



def main():
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
            if sandwich_maker_instance.check_resources(sandwich_recipe["ingredients"]):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich_recipe["cost"]):
                    sandwich_maker_instance.make_sandwich(response, sandwich_recipe["ingredients"])
        else:
            print("Invalid response")

if __name__=="__main__":
    main()
