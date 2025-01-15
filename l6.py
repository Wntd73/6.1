'''1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), 
сравнив по времени их выполнение.
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.'''

import timeit
import itertools

endings = {
    'Единственное': {
        'именительный': '',
        'родительный': 'а',
        'дательный': 'у',
        'винительный': '',
        'творительный': 'ом',
        'предложный': 'е'
    },
    'Множественное': {
        'именительный': 'ы',
        'родительный': 'ов',
        'дательный': 'ам',
        'винительный': 'ы',
        'творительный': 'ами',
        'предложный': 'ах'
    }
}

word = "компьютер"

def gen_lex_dict(word):
    lexs = []
    for _, cases in endings.items():
        for ending in cases.values():
            lexs.append(f"{word}{ending}")
    return lexs

def gen_lex_it(word):
    s_end = ['', 'а', 'у', '', 'ом', 'е']
    p_end = ['ы', 'ов', 'ам', 'ы', 'ами', 'ах']

    all_endings = itertools.chain(s_end, p_end)
    lexs = [f"{word}{ending}" for ending in all_endings]
    return lexs

t_d = timeit.timeit(lambda: gen_lex_dict(word), number=1)
r_d = gen_lex_dict(word)

t_i = timeit.timeit(lambda: gen_lex_it(word), number=1)
r_i = gen_lex_it(word)

print("Сгенерированные лексемы (словарь):")
print(r_d)
print(f"Время выполнения (словарь): {t_d:.5f} сек")

print("Сгенерированные лексемы (itertools):")
print(r_i)
print(f"Время выполнения (itertools): {t_i:.5f} сек")
