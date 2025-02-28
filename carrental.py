class CarRentalSystem:
    def __init__(self):
        self.cars = {
            "5-seater": ["Maruti Suzuki Baleno", "Swift", "Vitara Brezza", "i20", "Volkswagen Polo"],
            "7-seater": ["Ertiga", "Innova", "XL6", "XUV 700"]
        }
        self.available_cars = {car: True for category in self.cars.values() for car in category}
        self.pricing = {
            "5-seater": {"12 hours": 1500, "24 hours": 3000, "3 days": 6500, "1 week": 14000},
            "7-seater": {"12 hours": 2000, "24 hours": 4000, "3 days": 8500, "1 week": 16500}
        }
        self.admin_password = "admin123"  # Simple admin authentication

    def admin_login(self):
        password = input("Enter admin password: ")
        return password == self.admin_password

    def add_car(self):
        if self.admin_login():
            category = input("Enter category (5-seater/7-seater): ")
            if category in self.cars:
                car_name = input("Enter car name: ")
                self.cars[category].append(car_name)
                self.available_cars[car_name] = True
                print(f"{car_name} added to {category} category.")
            else:
                print("Invalid category.")
        else:
            print("Access denied! Incorrect admin password.")

    def remove_car(self):
        if self.admin_login():
            category = input("Enter category (5-seater/7-seater): ")
            car_name = input("Enter car name: ")
            if category in self.cars and car_name in self.cars[category]:
                self.cars[category].remove(car_name)
                del self.available_cars[car_name]
                print(f"{car_name} removed from {category} category.")
            else:
                print("Car not found.")
        else:
            print("Access denied! Incorrect admin password.")

    def rent_car(self):
        self.show_available_cars()
        car_name = input("Enter car name to rent: ")
        category = None
        for cat, cars in self.cars.items():
            if car_name in cars:
                category = cat
                break

        if car_name in self.available_cars and self.available_cars[car_name]:
            print("Available rent durations and prices:")
            for duration, price in self.pricing[category].items():
                print(f"{duration}: ₹{price}")

            rent_duration = input("Enter rent duration: ")
            if rent_duration not in self.pricing[category]:
                print("Invalid duration selected.")
                return

            total_amount = self.pricing[category][rent_duration]
            deposit = input("Enter deposit (ID proof or personal item): ")
            payment_mode = input("Enter payment mode (Cash/UPI/Card): ")
            
            self.available_cars[car_name] = False
            print("\n--- Rental Receipt ---")
            print(f"Car: {car_name}")
            print(f"Duration: {rent_duration}")
            print(f"Total Amount: ₹{total_amount}")
            print(f"Deposit: {deposit}")
            print(f"Payment Mode: {payment_mode}")
            print("Car has been successfully rented out.")
        else:
            print(f"{car_name} is not available for rent.")

    def show_available_cars(self):
        print("Available cars:")
        for category, cars in self.cars.items():
            print(f"{category}:")
            for car in cars:
                status = "Available" if self.available_cars[car] else "Not Available"
                print(f"  - {car} ({status})")


# Example Usage
rental_system = CarRentalSystem()
while True:
    print("\n1. Show Available Cars\n2. Rent a Car\n3. Add Car (Admin)\n4. Remove Car (Admin)\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        rental_system.show_available_cars()
    elif choice == "2":
        rental_system.rent_car()
    elif choice == "3":
        rental_system.add_car()
    elif choice == "4":
        rental_system.remove_car()
    elif choice == "5":
        break
    else:
        print("Invalid choice, try again!")