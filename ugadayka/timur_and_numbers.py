"""Timur guessed a number from 1 to n. For what is the smallest number of questions (to which Timur answers "more" or "less") Ruslan can be guaranteed to guess Timur's number?

Input data format
The input of the program is a natural number n.

The output format
The program should print the minimum number of questions that are guaranteed to be enough for Ruslan to guess Timur's number.


###RUS###
Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше") Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура."""
from math import log2, ceil
a = int(input())
print(int(ceil(log2(a))))