from cardValidator.CardType import *


class CardValidator:

    def __init__(self, card_number):
        self.card_number = card_number
        self.card_length = 0
        self.is_card_valid = False
        self.card_status = "Invalid"
        self.card_type = "INVALID CARD TYPE"

    def __str__(self):
        return f"Card number is {self.card_number}"

    def get_card_number(self):
        return self.card_number

    def card_number_length(self):
        self.card_length = len(self.card_number)
        return self.card_length

    def card_number_validity(self):
        if 13 <= self.card_length <= 16:
            self.is_card_valid = True
        return self.is_card_valid

    def card_number_to_list(self):
        d_list = list(self.card_number)
        e = []
        for i in d_list:
            a = int(i)
            e.append(a)
        return e

    def validate_card_type(self):
        american_express_first_digit = int(CardType.AMERICAN_EXPRESS.value / 10)
        american_express_second_digit = CardType.AMERICAN_EXPRESS.value % 10
        american_express_second_digit_is_true = self.card_number_to_list()[0] == american_express_first_digit
        american_express_first_digit_is_true = self.card_number_to_list()[1] == american_express_second_digit

        if self.card_number_to_list()[0] == CardType.VISA.value:
            self.card_type = "VISA"

        elif self.card_number_to_list()[0] == CardType.MASTERCARD.value:
            self.card_type = "MASTERCARD"

        elif american_express_second_digit_is_true and american_express_first_digit_is_true:
            self.card_type = "AMERICAN EXPRESS"

        elif self.card_number_to_list()[0] == CardType.DISCOVER_CARD.value:
            self.card_type = "DISCOVER CARD"

        return self.card_type

    def sum_card_number(self):

        # DOUBLING CARD EVEN DIGIT FROM RIGHT TO LEFT
        # [4, 3, 5, 7, 6, 3, 7, 4, 3, 6, 5, 6, 8, 3, 2]
        even_num = 0
        odd_num = 0
        for i in range(-2, -len(self.card_number_to_list())-1, -2):
            # print(self.card_number_to_list()[i])
            doubling_result = self.card_number_to_list()[i] * 2
            if doubling_result > 9:
                f = doubling_result % 10
                s = int(doubling_result / 10)
                even_num += f + s
            else:
                even_num += doubling_result

        # ADDING CARD ODD DIGIT FROM RIGHT TO LEFT
        for i in range(-1, -len(self.card_number_to_list())-1, -2):
            # print(self.card_number_to_list()[i])
            odd_num += self.card_number_to_list()[i]

        # TOTAL OF BOTH VARIABLES
        total_result = even_num + odd_num

        # CHECK WHETHER CARD IS VALID THROUGH ITS DIGITS
        self.is_card_valid = total_result % 10 == 0
        return self.is_card_valid

    def set_card_status(self):
        if self.sum_card_number() and self.card_number_validity():
            self.card_status = "Valid"
        else:
            self.card_status = "Invalid"
        return self.card_status

    def validate_card(self):
        return f"""Credit Card Type: {self.validate_card_type()}
Credit CardNumber: {self.card_number}
Credit Card Digit Length: {self.card_number_length()}
Credit Card Validity Status: {self.set_card_status()}"""

