def is_valid_email(email):
    """
    Имэйл хаягийн зөв эсэхийг шалгах функц
    """
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    return True
