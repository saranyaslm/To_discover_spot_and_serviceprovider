import phonenumbers
from phonenumbers import geocoder, carrier

while True:
    number = input("Enter a PhoneNumber with the country code (or 'exit' to quit): ")

    if number == 'exit':
        break

    try:
        phoneNumber = phonenumbers.parse(number, None)
        if not phonenumbers.is_valid_number(phoneNumber):
            print("Invalid phone number. Please try again.")
            continue
    except phonenumbers.phonenumberutil.NumberFormatException:
        print("Invalid phone number. Please try again.")
        continue

    yourLocation = geocoder.description_for_number(phoneNumber, "en")
    yourServiceProvider = phonenumbers.carrier.name_for_number(phoneNumber, "en")

    print("Phone Number:", number)
    print("Location:", yourLocation)
    print("Service Provider:", yourServiceProvider)

    # Additional functionality
    while True:
        choice = input("Do you want to do more with this number? (y/n): ").strip().lower()
        if choice == 'n':
            break
        elif choice != 'y':
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

        # Additional options can be added here
        if choice == 'y':
            # Add more options or functionality here
            pass

print("Exiting the program.")


