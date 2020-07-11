def checklist(x,list1):
	tf = False
	for n in list1:
		if x % n == 0:
			tf = True
		if x % n != 0:
			pass
	return tf


def checkfactor(x, list1):
	tf = False
	for n in list1:
		if x % n == 0:
			tf = True
			break
		else:
			pass
	return tf



def isprime():
	try:
		x = input('Enter a positive integer to see if it is a prime number!\n')
		x = int(x)
		if x == 2:
			print('2 is prime')
		elif x % 2 == 0:
			print('%s is even! It is not prime!' % x)
		else:
			if x > 2:
				list1 = []
				prime = True
				maximum = 2
				count = 0 
				for n in range(1, round((x+1)/maximum), 2):
					count += 1
					if list1 != []:
						maximum = max(list1)
					if x % n != 0:
						if checklist(n, list1) == True:
							pass
						else:
							list1.append(n)
					else:
						if count == 1:
							pass
						else:
							prime = False
							break
				length = len(list1)
				if prime:
					print('%d is a prime number!' % x)
					print('Count:', count)
					print('Length:', length)
				else:
					print('%d is not a prime number!' % x)
					print('Count:', count)
					print('Length:', length)
			else:
				print('Please enter a valid positive integer!')
	except: 
		print('Something\'s wrong! Try again!')


if __name__ == '__main__':
	isprime()




