class DiscountModule:
    def apply_student_discount(self, card_id):
        if int(card_id) > 0 and len(str(card_id)) == 8:
            return 15.0
        return 0.0
