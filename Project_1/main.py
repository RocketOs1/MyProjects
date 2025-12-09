

class Calculator():
	def __init__(self):
		print('Это простой консольный калькулятор.')

	def main(self):
		while True:
			try:
				a = float(input('Введите 1 число:\t'))
				b = float(input('Введите 2 число:\t'))
			except ValueError:
				break
				print('Ошибка в вводе чисел.')
			operation = input('Введите опрерацию: (+; -; *; /)\t')

			try:
				if operation.split()[0] == '+':
					print(f'Вот сумма: {a + b}.')

				elif operation.split()[0] == '-':
					print(f'Вот разность: {a - b}.')

				elif operation.split()[0] == '*':
					print(f'Вот произведение: {a * b}.')

				elif operation.split()[0] == '/':
					print(f'Вот частное: {a / b}.')

				else:
					print('Нет такой операции.')
			except IndexError:
				print('Ошибка в отсутствии операции.')
			cont = input('Продолжаем: (ДА/НЕТ)\t')
			if cont.lower().split()[0] == 'да':
				continue
			elif cont.lower().split()[0] == 'нет':
				print(f'До свидания!')
				break
			else:
				print('Я подумал, что ты захотел прекратить, поэтому пока!')
				break




if __name__ == '__main__':
	try:
		calc = Calculator()
		calc.main()
	except KeyboardInterrupt:
		print('Программа прекращена комбинацией клавиш CTRL + C.')
