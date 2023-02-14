from cardValidator.card_validator import CardValidator

if __name__ == "__main__":
    user_input = input("Hello, Kindly Enter Card details to verify: ")
    card = CardValidator(user_input)

    print(card.validate_card())
