def validator(phone):
    if len(phone) >= 9 or len(phone) == 14:
        return True
    else:
        raise ValueError("Telefon raqam noto'g'ri kiritilgan!!!")