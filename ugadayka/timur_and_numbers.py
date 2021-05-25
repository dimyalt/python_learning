"""Timur guessed a number from 1 to n. For what is the smallest number of questions (to which Timur answers "more" or "less") Ruslan can be guaranteed to guess Timur's number?

Input data format
The input of the program is a natural number n.

The output format
The program should print the minimum number of questions that are guaranteed to be enough for Ruslan to guess Timur's number.


###RUS###
����� ������� ����� �� 1 �� n. �� ����� ���������� ���������� �������� (�� ������� ����� �������� "������" ��� "������") ������ ����� �������������� ������� ����� ������?

������ ������� ������
�� ���� ��������� �������� ����������� ����� n.

������ �������� ������
��������� ������ ������� ���������� ���������� ��������, ������� �������������� ������ �������, ����� ������� ����� ������."""
from math import log2, ceil
a = int(input())
print(int(ceil(log2(a))))