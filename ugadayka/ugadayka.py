# -*- coding: utf-8 -*-
"""�������� �������: ��������� ���������� ��������� ����� � ��������� �� 11 �� 100100 � ������ ������������ ������� ��� �����. ���� ������� ������������ ������ ���������� �����, �� ��������� ������ ������� ��������� '������� �����, ���������� ��� ���'. ���� ������� ������ ���������� �����, �� ��������� ������ ������� ��������� '������� ����, ���������� ��� ���'. ���� ������������ ��������� �����, �� ��������� ������ ���������� ��� � ������� ��������� '�� �������, �����������!'."""

from random import randint
x = randint(1, 100)
print('�������� ����� �� 1 �� 100, �������� ��� �������.')
y = -1
while True:
    y = int(input())
    if x < y:
        print('������� �����, ���������� ��� ���!')
        continue
    elif x > y:
        print('������� ����, ���������� ��� ���!')
        continue
    else:    
        print('�� �������, �����������!')
        break        
        