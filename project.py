import re


class HotelRoom:
    def __init__(self, room_number, is_booked=False, guest_name=None, key=None):
        self.room_number = room_number
        self.is_booked = is_booked
        self.guest_name = guest_name
        self.key = key

    def book_room(self, guest_name):
        if self.is_booked:
            print(f"\n❌ Room {self.room_number} is already booked.")
        else:
            self.is_booked = True
            self.guest_name = guest_name
            self.key = f"FAKE-{self.room_number}-{guest_name.split()[0].upper()[:3]}"
            print(f"\n✅ Room {self.room_number} successfully booked by {guest_name}.")
            print(f"🔑 Your room key: {self.key}")
            self.print_receipt(guest_name)
            print("\n✨ Thank you for choosing FAKE HOTEL! Enjoy your stay. ✨")
            exit()  # Exit after booking

    def print_receipt(self, guest_name):
        print("\n" + "=" * 40)
        print("                RECEIPT")
        print("=" * 40)
        print(f"Guest Name      : {guest_name}")
        print(f"Room Number     : {self.room_number}")
        print(f"Room Key        : {self.key}")
        print("=" * 40)


def welcome_message():
    print("\n" + "=" * 40)
    print("   🌟 WELCOME TO FAKE HOTEL 🌟   ")
    print("        Where luxury is a lie        ")
    print("=" * 40 + "\n")


def validate_phone(phone):
    if re.fullmatch(r"\d{10}$", phone):
        return True
    print("\n❌ Invalid phone number! It must be 10 digits.")
    return False


def validate_email(email):
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    print("\n❌ Invalid email address! Please enter a valid email.")
    return False


def validate_card_number(card_number):
    if re.fullmatch(r"\d{16}$", card_number):
        return True
    print("\n❌ Invalid card number! It must be 16 digits.")
    return False


def validate_card_type(card_type):
    if card_type.lower() in ["visa", "mastercard"]:
        return True
    print("\n❌ Invalid card type! Please enter 'Visa' or 'MasterCard'.")
    return False


def main():
    # Initialize rooms
    rooms = {101: HotelRoom(101), 102: HotelRoom(102), 103: HotelRoom(103)}

    welcome_message()

    # Take user's personal information
    print("Please provide the following details to book your stay:\n")

    first_name = input("Enter your First Name: ").strip()
    last_name = input("Enter your Last Name: ").strip()

    phone_number = input("Enter your Phone Number: ").strip()
    while not validate_phone(phone_number):
        phone_number = input("Enter your Phone Number (10 digits): ").strip()

    email = input("Enter your Email: ").strip()
    while not validate_email(email):
        email = input("Enter your Email: ").strip()

    city = input("Enter your City: ").strip()

    special_requests = input("Enter any Special Requests (optional): ").strip() or "None"

    card_type = input("Enter your Card Type (Visa, MasterCard): ").strip()
    while not validate_card_type(card_type):
        card_type = input("Enter your Card Type (Visa, MasterCard): ").strip()

    card_number = input("Enter your Card Number: ").strip()
    while not validate_card_number(card_number):
        card_number = input("Enter your Card Number: ").strip()

    print("\n🏨 Available Rooms:\n")
    for room_number, room in rooms.items():
        if not room.is_booked:
            print(f"Room {room_number}")

    # Booking process
    try:
        selected_room = int(input("\nEnter the room number you want to book: "))
        if selected_room in rooms:
            full_name = f"{first_name} {last_name}"
            rooms[selected_room].book_room(full_name)
        else:
            print("\n❌ Invalid room number. Please restart the booking process.")
            exit()
    except ValueError:
        print("\n❌ Invalid input! Please enter a valid room number.")
        exit()


if __name__ == "__main__":
    main()
