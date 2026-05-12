# Inventory Management for Medical & Food Supplies
class PayloadAgent:
    def __init__(self):
        self.inventory = {
            "med_kits": 5,
            "water_bottles": 10,
            "rations": 10
        }

    def dispense_item(self, item_name):
        if self.inventory.get(item_name, 0) > 0:
            self.inventory[item_name] -= 1
            print(f"[PAYLOAD] Dispensed: {item_name}. Remaining: {self.inventory[item_name]}")
        else:
            print(f"[PAYLOAD] Error: {item_name} out of stock!")

    def auto_scan_wounds(self, thermal_data):
        # Logic: If blood/heat signature detected, prioritize med_kits
        pass
