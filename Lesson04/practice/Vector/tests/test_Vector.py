# test_vector.py
import pytest
from ... import Vector  # Импортируем наш класс Vector


def test_vector_init_valid():
    """Тест инициализации вектора с корректными числовыми значениями."""
    v = Vector(1, 2)
    assert v.x == 1
    assert v.y == 2
    assert v.dimension == 2


def test_vector_init_float_values():
    """Тест инициализации вектора с корректными значениями с плавающей точкой."""
    v = Vector(1.5, -2.7)
    assert v.x == 1.5
    assert v.y == -2.7


def test_vector_init_invalid_x_type():
    """Тест инициализации вектора с некорректным типом x."""
    with pytest.raises(TypeError, match="Координаты x и y должны быть числами."):
        Vector("a", 2)


def test_vector_init_invalid_y_type():
    """Тест инициализации вектора с некорректным типом y."""
    with pytest.raises(TypeError, match="Координаты x и y должны быть числами."):
        Vector(1, "b")


def test_vector_str():
    """Тест строкового представления вектора."""
    v = Vector(1, 2)
    assert str(v) == "Vector(x=1, y=2)"


def test_vector_repr():
    """Тест представления вектора для отладки."""
    v = Vector(1.0, -2.0)
    assert repr(v) == "Vector(1.0, -2.0)"


def test_vector_add():
    """Тест сложения двух векторов."""
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v_sum = v1 + v2
    assert v_sum.x == 4
    assert v_sum.y == 6
    assert v_sum == Vector(4, 6)  # Проверка через __eq__


def test_vector_add_negative_coords():
    """Тест сложения векторов с отрицательными координатами."""
    v1 = Vector(-1, -2)
    v2 = Vector(3, 4)
    v_sum = v1 + v2
    assert v_sum == Vector(2, 2)


def test_vector_add_type_error():
    """Тест сложения вектора с некорректным типом."""
    v1 = Vector(1, 2)
    with pytest.raises(TypeError, match="Можно складывать только объекты класса Vector."):
        v1 + [1, 2]


def test_vector_sub():
    """Тест вычитания двух векторов."""
    v1 = Vector(5, 7)
    v2 = Vector(3, 2)
    v_diff = v1 - v2
    assert v_diff.x == 2
    assert v_diff.y == 5
    assert v_diff == Vector(2, 5)


def test_vector_sub_negative_result():
    """Тест вычитания, приводящего к отрицательным координатам."""
    v1 = Vector(1, 1)
    v2 = Vector(3, 3)
    v_diff = v1 - v2
    assert v_diff == Vector(-2, -2)


def test_vector_sub_type_error():
    """Тест вычитания вектора с некорректным типом."""
    v1 = Vector(1, 2)
    with pytest.raises(TypeError, match="Можно вычитать только объекты класса Vector."):
        v1 - (1, 2)


def test_vector_mul_scalar():
    """Тест умножения вектора на скаляр (целое число)."""
    v = Vector(2, 3)
    scalar = 5
    v_scaled = v * scalar
    assert v_scaled.x == 10
    assert v_scaled.y == 15
    assert v_scaled == Vector(10, 15)


def test_vector_mul_float_scalar():
    """Тест умножения вектора на скаляр (число с плавающей точкой)."""
    v = Vector(2, 3)
    scalar = 2.5
    v_scaled = v * scalar
    assert v_scaled == Vector(5.0, 7.5)


def test_vector_mul_zero_scalar():
    """Тест умножения вектора на ноль."""
    v = Vector(10, 20)
    scalar = 0
    v_scaled = v * scalar
    assert v_scaled == Vector(0, 0)


def test_vector_rmul_scalar():
    """Тест обратного умножения скаляра на вектор (скаляр * вектор)."""
    v = Vector(2, 3)
    scalar = 4
    v_scaled = scalar * v
    assert v_scaled.x == 8
    assert v_scaled.y == 12
    assert v_scaled == Vector(8, 12)


def test_vector_mul_type_error():
    """Тест умножения вектора на некорректный тип скаляра."""
    v = Vector(1, 2)
    with pytest.raises(TypeError, match="Можно умножать только на числовой скаляр"):
        v * "abc"


def test_vector_eq_true():
    """Тест проверки равенства двух одинаковых векторов."""
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    assert v1 == v2


def test_vector_eq_false_x():
    """Тест проверки равенства для векторов с разными x."""
    v1 = Vector(1, 2)
    v2 = Vector(3, 2)
    assert not (v1 == v2)


def test_vector_eq_false_y():
    """Тест проверки равенства для векторов с разными y."""
    v1 = Vector(1, 2)
    v2 = Vector(1, 4)
    assert not (v1 == v2)


def test_vector_eq_different_type():
    """Тест проверки равенства с другим типом объекта."""
    v = Vector(1, 2)
    assert not (v == [1, 2])  # Должен вернуть False, а не TypeError благодаря NotImplemented


def test_vector_len():
    """Тест возврата размерности вектора."""
    v = Vector(1, 2)
    assert len(v) == 2


def test_vector_getitem_x():
    """Тест доступа к координате x по индексу 0."""
    v = Vector(10, 20)
    assert v[0] == 10


def test_vector_getitem_y():
    """Тест доступа к координате y по индексу 1."""
    v = Vector(10, 20)
    assert v[1] == 20


def test_vector_getitem_invalid_index():
    """Тест доступа по некорректному индексу."""
    v = Vector(10, 20)
    with pytest.raises(IndexError, match="Индекс вне диапазона для 2D вектора"):
        v[2]


def test_vector_setitem_x():
    """Тест изменения координаты x по индексу 0."""
    v = Vector(1, 2)
    v[0] = 5
    assert v.x == 5
    assert v == Vector(5, 2)


def test_vector_setitem_y():
    """Тест изменения координаты y по индексу 1."""
    v = Vector(1, 2)
    v[1] = 10.5
    assert v.y == 10.5
    assert v == Vector(1, 10.5)


def test_vector_setitem_invalid_index():
    """Тест изменения координаты по некорректному индексу."""
    v = Vector(1, 2)
    with pytest.raises(IndexError, match="Индекс вне диапазона для 2D вектора"):
        v[2] = 7


def test_vector_setitem_invalid_value_type():
    """Тест изменения координаты на значение некорректного типа."""
    v = Vector(1, 2)
    with pytest.raises(ValueError, match="Координата должна быть числом."):
        v[0] = "error"
