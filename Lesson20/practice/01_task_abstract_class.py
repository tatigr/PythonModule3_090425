from abc import ABC, abstractmethod
from typing import Optional


# --- 1. Абстрактный класс SmartDevice ---
class SmartDevice(ABC):
    """
    Абстрактный базовый класс для умных устройств.
    Определяет общий интерфейс для включения/выключения и проверки состояния.
    """

    @property
    @abstractmethod
    def device_id(self) -> str:
        """Обязательное свойство: уникальный идентификатор устройства."""
        pass

    @abstractmethod
    def turn_on(self) -> None:
        """Включает устройство."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """Выключает устройство."""
        pass

    @abstractmethod
    def is_on(self) -> bool:
        """Возвращает True, если устройство включено, False в противном случае."""
        pass

    def get_status_report(self) -> str:
        """
        Возвращает строку с текущим статусом устройства.
        Это неабстрактный метод.
        """
        if self.is_on():
            return f"Device {self.device_id} is ON."
        else:
            return f"Device {self.device_id} is OFF."


# --- 2. Конкретные реализации SmartDevice ---

class SmartLight(SmartDevice):
    def __init__(self, light_id: str):
        self._light_id = light_id
        self._is_powered_on: bool = False  # Внутреннее состояние лампочки

    @property
    def device_id(self) -> str:
        # TODO: Реализуйте геттер для абстрактного свойства device_id
        ...

    def turn_on(self) -> None:
        # TODO: Реализуйте метод включения лампочки
        ...

    def turn_off(self) -> None:
        # TODO: Реализуйте метод выключения лампочки
        ...

    def is_on(self) -> bool:
        # TODO: Реализуйте метод проверки состояния лампочки
        ...


class SmartThermostat(SmartDevice):
    def __init__(self, thermostat_id: str, initial_temp: int = 20):
        self._thermostat_id = thermostat_id
        self._current_temp = initial_temp
        self._is_active: bool = False  # Внутреннее состояние термостата

    @property
    def device_id(self) -> str:
        # TODO: Реализуйте геттер для абстрактного свойства device_id
        ...

    def turn_on(self) -> None:
        # TODO: Реализуйте метод включения термостата
        ...

    def turn_off(self) -> None:
        # TODO: Реализуйте метод выключения термостата
        # Ваша реализация здесь:
        ...

    def is_on(self) -> bool:
        # TODO: Реализуйте метод проверки состояния термостата
        ...

    def set_temperature(self, temp: int) -> None:
        """Устанавливает температуру, если термостат включен."""
        # TODO: Реализуйте этот дополнительный метод.
        # Если термостат включен, обновите _current_temp и выведите сообщение.
        # Если выключен, выведите сообщение, что сначала нужно включить.
        # Ваша реализация здесь:
        ...


# --- 3. Использование в клиентском коде ---

def operate_device(device: SmartDevice) -> None:
    """
    Принимает любое умное устройство и выполняет на нем последовательность операций.
    """
    print(f"\n--- Операция с устройством {device.device_id} ({type(device).__name__}) ---")
    print(device.get_status_report())
    device.turn_on()
    print(device.get_status_report())
    if isinstance(device, SmartThermostat):  # Дополнительная логика для термостата
        device.set_temperature(22)
    device.turn_off()
    print(device.get_status_report())


# --- Код для тестирования (не менять, использовать для проверки) ---
if __name__ == "__main__":
    # 1. Создаем экземпляры различных умных устройств
    light1 = SmartLight("light-001")
    thermostat1 = SmartThermostat("thermo-001", 21)

    # 2. Демонстрируем работу с ними через общую функцию
    operate_device(light1)
    operate_device(thermostat1)

    print("\n--- Попытка создать некорректное устройство (без реализации абстрактных членов) ---")


    class IncompleteDevice(SmartDevice):
        # Отсутствует реализация device_id, turn_on, turn_off, is_on
        pass


    try:
        incomplete_d = IncompleteDevice()
    except TypeError as e:
        print(f"Ошибка: {e}")
        print("Это ожидаемое поведение, так как IncompleteDevice не реализовал все абстрактные члены SmartDevice.")

    print("\n--- Проверка состояния после отдельной установки температуры ---")
    thermostat2 = SmartThermostat("thermo-002", 18)
    thermostat2.set_temperature(25)  # Термостат выключен, должна быть ошибка
    thermostat2.turn_on()
    thermostat2.set_temperature(25)  # Теперь должен сработать
