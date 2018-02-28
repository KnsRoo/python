def swap(letter):
	a = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]
	b = ["я", "п", "ф", "к", "т", "э", "о", "ш", "с", "ы", "й", "г", "л", "м", "н", "ё", "б", "р", "з", "д", "ю", "в", "х", "ц", "щ", "ж", "ч", "ь", "и", "ъ", "е", "у", "а"]
	for i in range(len(a)):
		if letter == a[i]:
			return b[i]

if __name__ == "__main__":
	mas = []
	print("Введите строку")
	string = input()
	for i  in range(len(string)):
		mas.append(string[i])
	for i in range(len(mas)):
		mas[i] = swap(mas[i])
	string = ""
	for i in range(len(mas)):
		string+=str(mas[i])
	print(string)



