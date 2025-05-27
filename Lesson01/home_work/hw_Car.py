## Автомобиль
class Car:
    def __init__(self, capacity, gas_per_km, gas=0):
        if gas > capacity:
            self.gas = capacity
            print("Излишек топлива ...")
        else:
            self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km

    def fill(self, fuel) -> None:
        if self.gas + fuel > self.capacity:
            extra_fuel = self.gas + fuel - self.capacity
            self.gas = self.capacity
            print(f"Лишний бензин: {extra_fuel}")
        else:
            self.gas += fuel

    def ride(self, distance) -> None:
        max_distance = self.gas / self.gas_per_km
        if distance > max_distance:
            self.gas = 0
        else:
            self.gas -= distance * self.gas_per_km


# Shift + F6