from discount_v1_buggy import DiscountModule
m = DiscountModule()
for name, v in [("ok","12345678"),("text","ABC-123"),("None",None),("empty",""),("spaces"," 12345678 "),("long","1"*5000),("neg","-1234567"),("float",12345678.0),("zeros","00000000"),("plus","+1234567"),("unicode","١٢٣٤٥٦٧٨")]:
    try: print(name, repr(m.apply_student_discount(v))[:60])
    except Exception as e: print(name, "EXC", type(e).__name__, str(e)[:50])
