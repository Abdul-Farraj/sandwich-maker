class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coin_total = 0.0
        dollar = float(input("how many large dollars?: "))
        half = float(input("how many half dollars?: "))
        quarters = float(input("how many quarters?: "))
        nickels = float(input("how many nickels?: "))
        coin_total = dollar * 1.0 + half * 0.50 + quarters * 0.25 + nickels * 0.10
        return coin_total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = coins - cost
            print(f"Here is your change: ${change:.2f} ")
        return True
