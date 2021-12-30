# data types
#numbers(int, float, complex)
#srinigs
#Booleans( True  or False)
# List, Set, Tuple, Dictionary 

#Builtin fucntion we use to check 
#Numbers
print(type(10))
print(type('10'))

# Strings 
# As short as a single character or as long as many pages 

letter = 'a'
word = 'love'

print(word)
print(len(word))
print(word[0])
print(word[1])

last_index = len(word)-1

sentence ='I love python'
print(sentence)
print(sentence.upper()) #method should be attached with something
print(sentence.lower())
#print(sentence.count())

dna = '''gtggcgctgcagagtagaactccgttgttagaccagtaatatctgggggcggaagatggc
ctcggagcgaggctgaaggaactcagtatctaaaagttaattgatgagcatttctaccgg
ggagcgccgtagatggcagtgagccgtttaaagctcatcatctcagcaccgcgaagagtc
ctctgtgggggtccgggcacaccccgagtagtatcctgcacccaacacaggcatcccgtc
gagtatagtataaagaaggtctgcggttatttggtcctgttttctctttacgatacaacg
tataaaccgcgggcttgcagaagccatctcaatttaccttaccttcttcggtatattctt
tataggctggtcaacaacaatcaacattgggggtcgcgaaattcgtgacgccttaggccc
ttgcgtacaggacgttgttcttaccataattacaggctgacttgtgcgaaaagtccgatt
tgccacatgacactcctaccgagcagcttgcgttaggacagttcgcaaattccctaacaa
aggtagcgtttcggaagatacccaaagcggcgcaggtcttcccgaagcaaagtgtggccg
tgtggtgtacatggccacatgggaacagtcgagacgacgtctctcataagtagacggata
tgctatacttgcggcaggcaccagggttctattccggtatctttccgtgggggtgcattc
cgtccataggcctcgtcgccggggattaacggcggcttcgcccaccgttccattaagtgc
gcctatcggcatagaaggtcgtttcctagaaccgggtgctccctagttttacggactcca
tggatttgtatgggccacttgctattcgcgtaagggatcacatatggtttagagacccac
cggtgcaccaaaactcggccttcaagagcctgacaatttacatggctcacccttgtgacg
gtctagccgtagggctgaataacctcttttgcctaaacac'''

print(dna)
print(len(dna))

total_count = len(dna)
a = dna.count('a')
c = dna.count('c')
t = dna.count('t')
g = dna.count('g')
print(a, c,t, g)
print('proporation', 'a nucotide:',  round(a / total_count * 100, 2), '%')
print('proporation','c nucotide:',round(c / total_count * 100, 2), '%')
print('proporation', 't nucotide:', round(t/total_count * 100, 2), '%')
print('proporation',  'g nucotide:', round(g/total_count * 100, 2), '%')

'''sentence = 'I love python and I love Javascript'

print(sentence.count('I'))
print(sentence.title())
print(sentence.swapcase())
print(sentence.startswith('I'))
print(sentence.find('o'))'''

#string formating 
country = 'Ethiopia'
city = 'Addis Ababa'
print('{} is in africa. The capital is {}.'.format(country, city))

a = 4
b = 3
print(f'The sum of {a} and {b} is {a+b}')
a = 4
b = 3
print(f'The sum of {a} and {b} is {a + b}.')
print(f'The difference of {a} and {b} is {a - b}.')
print(f'The product of {a} and {b} is {a * b}.')

""" I am Asabeneh Yetayeh. 
I live in Helsinki, Finland. 
I teach Python. My skills are HTML, CSS, JS, and Python. 
I am 250 years old. """

first_name = 'Eyasu'
country = 'USA'
city = 'Seattle'
skills = ['3d prinitng', 'NMR', 'Laser cutting']
age = 31
tech_lang = 'Python'

#print(f'My name is {first_name}.I live in {country} and my city is {city} and I am {age}. I am currently learning {tech_lang}.')

print(f'I am {first_name}. I live in {country}, {city}. My skills are {skills[0]}, {skills[1]}, {skills[2]}. I am {age} years old.')
nums = [1, 2, 3, 4, 5]
print(nums[:])
print(nums[3:])
print(nums[3:-1])

