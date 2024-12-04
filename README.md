
FAKE HOTEL ROOM BOOKING SYSTEM

Video Demo: [www.youtube.com/your-video-url](https://youtu.be/dL3j-fo-pUA)

=============================

Overview

The **FAKE HOTEL ROOM BOOKING SYSTEM** is a Python-based command-line application designed to facilitate the booking of hotel rooms. This project is aimed at creating an interactive and user-friendly booking system that handles personal details, validates input, and manages the booking process for a hotel room. The program ensures users provide valid information, generates a room key, and prints a receipt. Upon successful booking, the program exits to enhance the user experience.

This project demonstrates key Python concepts such as classes, functions, input validation, and error handling. It also provides an example of implementing a simple booking system for educational purposes.

Features

- **User-friendly Interface**: The system starts by welcoming the user with an attractive and clear message, making the process smooth and easy to follow.

- **Personal Information Input**: The system collects basic user information including:
  - First Name
  - Last Name
  - Phone Number (validated)
  - Email Address (validated)
  - City

- **Room Booking**: Users can select from available rooms (the system checks for availability). Once the user selects a room, it’s marked as booked.

- **Room Key Generation**: After a successful booking, a unique room key is generated, combining the room number and the guest’s name.

- **Card Details Validation**: The system ensures that the user enters a valid credit card number (16 digits) and allows only Visa or MasterCard types.

- **Receipt Generation**: Once the room is booked, the system prints a receipt containing all the booking details including the guest's name, room number, room key, and booking status.

- **Error Handling**: Clear error messages are provided if any input is invalid, such as incorrect phone number formats, invalid email addresses, or unsupported card types.

- **Exit After Booking**: After the booking is completed and the receipt is generated, the system automatically exits to prevent any further actions from the user.

## How to Use

1. **Run the Program**: Start by running the program with the Python interpreter.
2. **Input Personal Information**: The system will prompt you to enter your first name, last name, phone number, email, and city.
3. **Special Requests**: You’ll be asked to provide any special requests you may have for your stay. This step is optional.
4. **Card Details**: Enter your card type (Visa or MasterCard) and your 16-digit card number.
5. **Room Selection**: After entering your details, the program will display a list of available rooms.
6. **Booking the Room**: Choose the room number you’d like to book.
7. **Receipt**: The system will generate a receipt with all your details and show a unique room key.
8. **Exit**: The program will exit automatically after booking the room.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your machine.
- **Basic Knowledge of Python**: This program can be run in any environment that supports Python, with minimal setup required.

## Installation

1. **Download or Clone the Repository**: Download the project files or clone the repository from GitHub to your local machine.
2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the folder where the files are stored.
3. **Run the Script**: Execute the following command in your terminal:
    ```bash
    python fakehotel.py
    ```

## Code Description

- **HotelRoom Class**: This class represents individual rooms. It contains methods to book a room and generate a room key. Each room has an associated room number, booking status, and guest name.

  - The `book_room` method handles the booking process by marking the room as booked and assigning the guest name and a unique room key.

- **Validation Functions**:
  - **validate_phone**: Checks if the phone number entered is 10 digits.
  - **validate_email**: Ensures the email entered matches the correct email format.
  - **validate_card_number**: Validates that the entered card number is exactly 16 digits.
  - **validate_card_type**: Ensures the card is either Visa or MasterCard.

- **Main Function**: This function orchestrates the entire booking process:
  - Collects user input.
  - Validates the input.
  - Displays available rooms.
  - Handles room booking and receipt generation.

## Design Choices

- **Error Handling**: I chose to implement detailed error handling for user inputs to ensure the user provides correct information, such as a valid phone number, email, and credit card details. This prevents errors and ensures smooth operation.

- **Card Type Validation**: To simplify the card validation process, I limited the card types to Visa and MasterCard, making the code more manageable while still ensuring realistic functionality.

- **Room Availability**: The program only shows available rooms to the user, ensuring that each room is only booked once, avoiding overbooking.

- **Exiting the Program**: After successfully booking a room, the program exits to give the user a clear end to the process, enhancing usability.

## Future Improvements

- **More Room Types**: I could add additional room types and prices for a more realistic simulation.
- **User Interface**: The current system is a command-line interface (CLI), but adding a graphical user interface (GUI) could improve the user experience.
- **Extended Card Validation**: I could expand the card validation to check if the card number is valid through a real payment gateway.

---
