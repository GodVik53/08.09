#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два 
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
#произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

from math import sqrt
# s, p = map( int, input('s, p = ').split() )
z = sqrt( (s/2)**2 - p )
print( int( s/2 - z ), int( s/2 + z ) )

