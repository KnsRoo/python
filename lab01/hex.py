def convert_base(num, to_base=10, from_base=10):
	if isinstance(num, str):
		n = int(num, from_base)
	else:
		n = int(num)
	alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if n < to_base:
		return alphabet[n]
	else:
		return convert_base(n // to_base, to_base) + alphabet[n % to_base]

if __name__ == "__main__":
	print("Введите дату рождения в формате DD.MM.YYYY")
	dob = input().split('.')
	sum = 0
	for item in dob:
		item.strip()
		if (item.isdigit()):
			sum+=int(item)
		else:
			print("Ошибка")
	print("8 - "+convert_base(sum, from_base=10, to_base=8)+"\n16 - "+convert_base(sum, from_base=10, to_base=16)+"\n32 - "+convert_base(sum, from_base=10, to_base=32))