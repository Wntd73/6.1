'''1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), 
сравнив по времени их выполнение.
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.

2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

Усложнение: ограничение на длину слова от n1 до n2.
Целевая функция: нахождение самой короткой лексемы.'''

import timeit
import itertools

mainword = 'компьютер'
filename = 'words.txt'

def fileop(filename):
    with open(filename, "r", encoding="utf8") as f:
        line = f.readline()
        words = list(map(str, line.split()))
    return words


def generate_combinations(word):
    def generate_subsets(current, remaining):
        if len(current) >= 2:
            subsets.append(current)
        for i in range(len(remaining)):
            generate_subsets(current + remaining[i], remaining[:i] + remaining[i+1:])
    subsets = []
    generate_subsets("", word)
    return subsets

def generate_combinations_itertools(word):
    result = []
    for length in range(2, len(word) + 1):
        for perm in itertools.permutations(word, length):
            result.append(''.join(perm))
    return result


def find_matching_words(words, combinations, n1, n2):
    matches = []
    for word in words:
        if word in combinations and n1 <= len(word) <= n2:
            matches.append(word)
    return matches

while True:
    try:
        n1 = int(input("Введите минимальную длину слова (n1): "))
        n2 = int(input("Введите максимальную длину слова (n2): "))
        if n1 < 2 or n2 < n1:
            raise ValueError
        break
    except ValueError:
        print("Ошибка: введите корректные числа (n1 >= 2 и n2 >= n1).")

words = fileop(filename)

start_algo = timeit.default_timer()
result_algo = generate_combinations(mainword)
matches_algo = find_matching_words(words, result_algo, n1, n2)
end_algo = timeit.default_timer()
print("\nАлгоритмический способ:")
print("Совпадения:", " ".join(matches_algo))
print(f"Время: {end_algo - start_algo:.4f} секунд")

start_itertools = timeit.default_timer()
result_itertools = generate_combinations_itertools(mainword)
matches_itertools = find_matching_words(words, result_itertools, n1, n2)
end_itertools = timeit.default_timer()
print("\nСпособ с itertools:")
print("Совпадения:", " ".join(matches_itertools))
print(f"Время: {end_itertools - start_itertools:.4f} секунд")
