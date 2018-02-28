
def whatq(m, ret = "Ошибка"):
	if m > 0 and m < 4:
		ret = "1 Квартал"
	elif m > 3 and m < 7:
		ret = "2 Квартал"
	elif m > 6 and m < 10:
		ret = "3 Квартал"
	elif m > 9 and m < 13:
		ret = "4 Квартал"
	return ret


if __name__ == "__main__":
	print("Введите номер месяца:")
	x = input()
	print(whatq(int(x)))