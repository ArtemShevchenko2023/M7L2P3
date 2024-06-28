import pytest
from calculate.calculator_program import calculate
def test_calculate_addition():
    assert calculate(1, 1, '+') == 2
def test_calculate_division():
    assert calculate(8, 2, '/') == 4
def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."
def test_calculate_minus():
    assert calculate(5, 3, '-') == 2
def test_calculate_dupl():
    assert calculate(5, 85, '*') == 425
def test_calculate_diviszero():
    assert calculate(5, 0, '/') == "Деление на ноль."
def test_calculate_additio():
    assert calculate(1, -1, '+') == 0
def test_calculate_divisio():
    assert calculate(8, -2, '/') == -4
def test_calculate_minu():
    assert calculate(5, -3, '-') == 8
def test_calculate_dupli():
    assert calculate(5, -5, '*') == -25
def test_calculate_umn():
    assert calculate(5, "a", '*') == 'Числа должны быть введены корректно.'
def test_calculate_umno():
    assert calculate("a", 5, '*') == 'Числа должны быть введены корректно.'
'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
