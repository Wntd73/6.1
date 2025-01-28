'''1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), 
сравнив по времени их выполнение.
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.'''

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

def find_matching_words(words, combinations):
    matches = []
    for word in words:
        if word in combinations:
            matches.append(word)
    return matches


words = fileop(filename)

start_algo = timeit.default_timer()
result_algo = generate_combinations(mainword)
matches_algo = find_matching_words(words, result_algo)
end_algo = timeit.default_timer()
print("\nАлгоритмисески:")
print("Совпадения:", " ".join(matches_algo))
print(f"Время: {end_algo - start_algo:.4f} секунд")


start_itertools = timeit.default_timer()
result_itertools = generate_combinations_itertools(mainword)
matches_itertools = find_matching_words(words, result_itertools)
end_itertools = timeit.default_timer()
print("\nItertools:")
print("Совпадения:", " ".join(matches_itertools))
print(f"Время: {end_itertools - start_itertools:.4f} секунд")