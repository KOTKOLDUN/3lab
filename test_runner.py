from discount_module import DiscountModule

m = DiscountModule()
passed = failed = 0


def check(name, card_id, expected_valid):
    global passed, failed
    try:
        r = m.apply_student_discount(card_id)
        ok = r["valid"] == expected_valid and (r["discount_percent"] == 15.0) == expected_valid
        status = "PASS" if ok else "FAIL"
        info = r["message"]
    except Exception as e:  # модуль не должен падать
        ok, status, info = False, "FAIL", f"ИСКЛЮЧЕНИЕ {type(e).__name__}"
    passed += ok
    failed += (not ok)
    print(f"[{status}] {name}: {info}")


print("== Позитивные ==")
check("Валидный билет", "12345678", True)
check("Пробелы по краям", " 12345678 ", True)
check("Ведущие нули", "00000001", True)

print("== Граничные ==")
check("Пустая строка", "", False)
check("Только пробелы", "   ", False)
check("7 цифр", "1234567", False)
check("9 цифр", "123456789", False)
check("Нулевой билет", "00000000", False)

print("== Стресс-тест ==")
check("Текст вместо цифр (BUG-01)", "ABC-123", False)
check("None (BUG-02)", None, False)
check("Строка 5000 символов (BUG-03)", "1" * 5000, False)
check("Число вместо строки", 12345678, False)
check("Знак + (BUG-04)", "+1234567", False)
check("Арабо-индийские цифры (BUG-05)", "١٢٣٤٥٦٧٨", False)
check("SQL-инъекция", "1; DROP TABLE", False)
check("Отрицательное", "-1234567", False)

print(f"\nИтого: {passed} PASS, {failed} FAIL")
assert failed == 0
