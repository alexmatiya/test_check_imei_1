class IMEIValidator:
    @staticmethod
    def is_valid(imei: str) -> bool:
        # Проверка на пустую строку
        if not imei:
            return False

        # Проверка длины и что строка состоит только из цифр
        if not imei.isdigit() or len(imei) != 15:
            return False

        # Проверка что IMEI не состоит только из нулей
        if imei == "0" * 15:
            return False

        # Проверка контрольной суммы по алгоритму Луна
        checksum = 0
        for i in range(14):
            digit = int(imei[i])
            if i % 2 == 0:
                checksum += digit
            else:
                doubled = digit * 2
                checksum += doubled if doubled < 10 else doubled - 9

        check_digit = (10 - (checksum % 10)) % 10
        return check_digit == int(imei[-1])
