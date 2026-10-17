"""DiscountModule — проект FoodCampus. User Story: льготная скидка 15% по студбилету."""

STUDENT_DISCOUNT_PERCENT = 15.0
CARD_LENGTH = 8  # номер студбилета: ровно 8 цифр (ASCII)


class DiscountModule:
    def apply_student_discount(self, card_id):
        """Возвращает dict: {"valid": bool, "discount_percent": float, "message": str}.
        Никогда не бросает исключений наружу — ошибки возвращаются в message."""
        if card_id is None:
            return self._fail("Номер билета не указан")
        if not isinstance(card_id, str):
            return self._fail("Номер билета должен быть строкой")

        card_id = card_id.strip()
        if not card_id:
            return self._fail("Номер билета пуст")
        if len(card_id) != CARD_LENGTH:
            return self._fail(f"Номер билета должен содержать {CARD_LENGTH} цифр")
        if not (card_id.isascii() and card_id.isdigit()):
            return self._fail("Неверный формат: допустимы только цифры 0-9")
        if card_id == "0" * CARD_LENGTH:
            return self._fail("Недействительный номер билета")

        return {"valid": True, "discount_percent": STUDENT_DISCOUNT_PERCENT,
                "message": "Скидка применена"}

    @staticmethod
    def _fail(msg):
        return {"valid": False, "discount_percent": 0.0, "message": msg}
