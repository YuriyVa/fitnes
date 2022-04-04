class InfoMessage:
    """Информационное сообщение о тренировке."""
    def _int_(self, 
             training_type: str,
             duration: float,
             distance: float,
             speed: float,
             calories: float
             ) -> None:
             self.training_type = training_type
             self.duration = duration
             self.distance = distance
             self.speed = speed
             self.calories = calories


    def get_message(sself, 
             training_type: str,
             duration: float,
             distance: float,
             speed: float,
             calories: float) -> str:
             
             self.training_type = training_type
             self.duration = duration
             self.distance = distance
             self.speed = speed
             self.calories = calories
    
    pass


class Training:
    """Базовый класс тренировки."""
LEN_STEP = 0.65
M_IN_KM = 1000
TRANING_TYPE: str = 'Тренировка'
T_IN_M = 60
    
    def __init__(self,
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
        return self.action * (self.LEN_STEP / self.M_IN_KM)

        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance / self.duration
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        
        pass


class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20
    TTRANING_TYPE = "Running"

    def _init_(self, 
               weight: float) -> None:

        super().__init__(weight)

    def get_spent_calories(self ) -> float:
        
        return (self.COEFF_CALORIE_1 * self.get_mean_speed - self.COEFF_CALORIE_2) * self.weight / self.M_IN_KM * self.T_IN_M 
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEFF_CALORIE_3 = 0.035
    COEFF_CALORIE_4 = 0.029
    TTRANING_TYPE = "SportsWalking"
    
    def __init__(self,
                weight: float, 
                height: float,
                duration: float) -> None:
        super().__init__(weight, duration)
        self.height = height 

    def get_spent_calories(self) -> float:
        
           
        return (self.COEFF_CALORIE_3 * self.weight + (self.get_mean_speed**2 // self.height)
         * self.COEFF_CALORIE_4 * self.weight) * self.duration * self.T_IN_M 
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    COEFF_CALORIE_5 = 1.1
    COEFF_CALORIE_6 = 2
    TTRANING_TYPE = "Swimming"
    LEN_STEP = 1.38
    
    def __init__(self,
                weight: float,
                duration: float,
                length_pool: float, 
                count_pool: int) -> None:
        super().__init__(weight, duration)
        self.length_pool = length_pool
        self.count_pool = count_pool


    def get_mean_speed(self) -> float:
        return self.length_pool* self.count_pool / M_IN_KM / self.duration 


    def  get_spent_calories(self) -> float:  
        return (self.get_mean_speed + self.COEFF_CALORIE_5) * self.COEFF_CALORIE_6 * self.weight 

    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

