"""
Модуль для расчета репутации персонажа после серии поединков.

Содержит функции для обработки результатов боев с учетом бонусов/антибонусов.
Основная функция main() принимает список поединков
и возвращает итоговую репутацию.
"""
from typing import List, Tuple

TEST_DATA: List[Tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """
    Добавляет очки репутации с учетом бонусного эффекта.
    Args:
        current_rep (float): Текущее значение репутации
        rep_points (int): Очки для добавления
        buf_effect (bool): Флаг бонусного эффекта
    Returns:
        float: Новая репутация с учетом бонуса (если применен)
    """
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(
            current_rep: float,
            rep_points: int,
            debuf_effect: bool
            ) -> float:
    """
    Уменьшает репутацию с учетом антибонуса.

    Args:
        current_rep: Текущая репутация
        rep_points: Очки для вычета
        debuf_effect: Флаг штрафного эффекта

    Returns:
        float: Новая репутация с учетом антибонуса
    """

    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: List[Tuple[int, str, bool]]) -> str:
    """
    Обрабатывает список поединков и вычисляет итоговую репутацию.
    Args:
        duel_res (list): Список кортежей (очки, результат, эффект)
    Returns:
        str: Форматированная строка с результатом
    """
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        elif result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, репутация персонажа '
            f'- {current_rep:.3f} очков.')


# Тестовый вызов функции main.
if __name__ == '__main__':
    print(main(TEST_DATA))
