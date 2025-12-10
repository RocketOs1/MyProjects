import random



class Game():
	def __init__(self):
		print('Это игра "Угадай число"!\nДиапозон чисел: 1-10')


	def main(self):
		b = random.randint(1, 10)
		while True:
			a = int(input('Введите число:\t'))
			if a == b:
				print('Ты угадал! :)')
				break
				
			elif a > b:
				print('Загаданое число меньше. :)')
				continue
			
			elif a < b:
				print('Загаданное число больше. :)')
				continue
					
		answer = input('Ты хочешь продолжить? (Да/Нет)\t')

		if answer.split()[0].lower() == 'да':
			self.main()

		elif answer.split()[0].lower() == 'нет':
			print('Пока! :)')
				


if __name__ == '__main__':
	try:
		game = Game()
		game.main()
	except KeyboardInterrupt:
		print('Программа прекращена комбинацией клавиш CTRL + C.')
	except ValueError:
		print('Введена буква, а не число!')