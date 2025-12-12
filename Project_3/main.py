import random


def main() -> str:
	length = int(input('Какой длины пароль вам нужен:\t'))
	list_1 = list('QWERTYUIOPASDFGHJKLZXCVBNM')
	list_2 = list('qwertyuiopasdfghjklzxcvbnm')
	list_3 = list('1234567890')
	list_4 = [list_1, list_2, list_3]
	s = ''
	for i in range(length):
		ran_list = random.choice(list_4)
		ran_char = random.choice(ran_list)
		s += ran_char

	return s



if __name__ == '__main__':
	try:
		print(f'Вот сгенерированный пароль:\t{main()}')
	except ValueError:
		print('Ошибка в вводе длины пароля.')
	except KeyboardInterrupt:
		print('\nПрограмма прекращена комбинацией клавиш CTRL + C.')