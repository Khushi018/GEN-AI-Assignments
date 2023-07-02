class Snack:
        self.snack_name = snack_name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self): 
        self.inventory = []
        self.sales_record = []

    def add_snack(self, snack):
        self.inventory.append(snack)
        print("Snack added successfully.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed successfully.")
                break
        else:
            print("Snack not found in the inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated successfully.")
                break
        else:
            print("Snack not found in the inventory.")

    def record_sale(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == 'yes':
                    self.sales_record.append(snack)
                    snack.availability = 'no'
                    print("Sale recorded successfully.")
                    break
                else:
                    print("Snack is not available for sale.")
                    break
        else:
            print("Snack not found in the inventory.")

    def display_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("No snacks in the inventory.")
        else:
            for snack in self.inventory:
                print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, "
                      f"Availability: {snack.availability}")

    def display_sales_record(self):
        print("Sales Record:")
        if not self.sales_record:
            print("No snacks sold.")
        else:
            for snack in self.sales_record:
                print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")


def get_input(prompt):
    return input(prompt).strip()


def get_integer_input(prompt):
    while True:
        try:
