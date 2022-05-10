from typing import Type, Dict, List
from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    INFO_MESSAGE = (
        "Тип тренировки: {self.training_type};"
        "Длительность: {self.duration:.3f}ч.; "
        "Дистанция: {self.distance:.3f}; "
        "Ср. скорость: {self.speed:.3f}км/ч; "
        "Потрачено ккал: {self.calories:.3f}."
    )

    def get_message(self):
        return self.INFO_MESSAGE.format(*asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    M_IN_H: float = 60

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, 
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""

    coef_calorie_1: float = 18
    coef_calorie_2: float = 20

    def get_spent_calories(self) -> float:
        return (
            (self.coef_calorie_1 * self.get_mean_speed() - self.coef_calorie_2)
            * self.weight
            / self.M_IN_KM
            * self.duration
            * self.M_IN_H
        )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coef_calorie_3: float = 0.035
    coef_calorie_4: float = 2
    coef_calorie_5: float = 0.029

    def __init__(
        self, action: int, duration: float, weight: float, height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return (
            (
                self.coef_calorie_3 * self.weight
                + (self.get_mean_speed() ** self.coef_calorie_4 // self.height)
                * self.coef_calorie_5
                * self.weight
            )
            * self.duration
            * self.M_IN_H
        )


class Swimming(Training):
    """Тренировка: плавание."""

    coef_calorie_6: float = 1.1
    coef_calorie_7: float = 2
    LEN_STEP: float = 1.38

    def __init__(
        self,
        action: float,
        duration: float,
        weight: float,
        length_pool: float,
        count_pool: float,
    ) -> None:
        super().__init__(action, duration, weight)
        self.len_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return self.len_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (
            (self.get_mean_speed() + self.coef_calorie_6)
            * self.coef_calorie_7
            * self.weight
        )


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pack = {"SWM": Swimming, "RUN": Running, "WLK": SportsWalking}
    if workout_type in pack:
        return pack[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    message_trainig = training.show_training_info()
    info = message_trainig.get_message()
    print(info)


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
