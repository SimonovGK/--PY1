from pprint import pprint
num = 15
# TODO решить с помощью list comprehension и распечатать его
pprint([{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(num+1)])
