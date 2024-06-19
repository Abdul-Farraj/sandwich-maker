
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, resource in ingredients.items():
            if self.machine_resources[item] < resource:
                print(f"Sorry there is not enough {item}. ")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, resource in order_ingredients.items():
            self.machine_resources[item] -= resource
        print(f"\n<{sandwich_size} sandwich is ready. Bon appétit!>")