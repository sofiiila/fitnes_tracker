from dataclasses import dataclass

@dataclass
class InfoMessage:
    """Класс содержит информационное сообщение
       о результатах тренировки.  
    """
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (           
            f'Тип тренировки: {self.training_type}; ' 
            f'Длительность: {self.duration:.3f} ч.; ' 
            f'Дистанция: {self.distance:.3f} км; ' 
            f'Ср. скорость: {self.speed:.3f} км/ч; ' 
            f'Потрачено ккал: {self.calories:.3f}.') 

@dataclass     
class Training:
    """Базовый класс тренировки"""
    M_IN_KM = 1000
    LEN_STEP = 0.65   

    def __init__(
            self, 
            action: int, 
            duration: float, 
            weight: float) -> None: 
        self.action = action 
        self.duration = duration 
        self.weight = weight

    @property
    def get_distance(self) -> float:
        """Вычисление пройденной дистанции в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM     

    @property    
    def get_mean_speed(self) -> float:
        """Вычисление средней скорости."""
        return self.get_distance / self.duration
        
    def get_spent_calories(self) -> float:
        """ВЫчисление затраченных калорий"""
        pass

    def show_training_info(self) -> InfoMessage:
        """Возврат сообщения о результатах тренировки"""
        return InfoMessage( 
            type(self).__name__,  
            self.duration, 
            self.get_distance, 
            self.get_mean_speed, 
            self.get_spent_calories)  
      
class Running(Training):
    """Вид тренировки: бег."""
    first_coef: int = 18 
    second_coef: int = 20
  
    @property
    def get_spent_calories(self) -> float: 
        return ((self.first_coef 
                * self.get_mean_speed() 
                - self.second_coef) 
                * self.weight 
                / self.M_IN_KM 
                * self.duration 
                * self.MIN_IN_H)
    
class SportsWalking(Training):  
    """Вид тренировки: спортивная ходьба."""
    first_coef: float = 0.035 
    second_coef: int = 2 
    thrid_coef: float = 0.029

    def __init__(
            self, 
            action: int,
            duration: float, 
            weight: float, 
            height: float):
          super().__init__(action, duration, weight)
          self.height = height

    @property
    def get_spent_calories(self) -> float: 
        return ((self.first_coef 
                * self.weight 
                + (self.get_mean_speed() 
                    ** self.second_coef 
                    // self.height) 
                * self.thrid_coef 
                * self.weight) 
                * self.duration 
                * self.MIN_IN_H)

class Swimming(Training):
    """Вид тренировки: плавание."""
    LEN_STEP = 1.38
    first_coef: float = 1.1 
    second_coef: int = 2 
    
    def __init__(
            self, 
            action: int, 
            duration: float,
            weight: float, 
            length_pool: float, 
            count_pool: float):
          super().__init__(action, duration, weight)
          self.length_pool = length_pool
          self.count_pool = count_pool

    @property      
    def get_mean_speed(self) -> float:
          return (self.length_pool * self.count_pool / self.M_IN_KM / self.duration)

    @property 
    def get_spent_calories(self):
          return ( 
            (self.get_mean_speed() 
                + self.first_coef) 
            * self.second_coef 
            * self.weight)

def read_package(workout_type: str, data: list) -> Training: 
    """Прочитать данные полученные от датчиков.""" 
    parameters_train = { 
        'RUN': Running,
        'SWM': Swimming,          
        'WLK': SportsWalking} 
    if workout_type not in parameters_train: 
        raise ValueError("Unknown workout type")
    
    if workout_type == "RUN":
        return parameters_train[workout_type](*data[:3])  
    elif workout_type == "SWM":
        return parameters_train[workout_type](*data[:5])  
    elif workout_type == "WLK":
        return parameters_train[workout_type](*data[:4])

def main(training: Training) -> None:
    """Главная функция"""
    try:
        message_train = training.show_training_info()
        print(message_train.get_message())
    except AttributeError:
        print("Данный тип тренировки неизвестен")
    pass

if __name__ == "__main__":
    packages = [        
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:       
        if data[0] > 0:
            training = read_package(workout_type, data)
            main(training)
        else:
            print('Вы еще не начали тренироваться=)')
    else:
        print('Не определен тип тренировки или датчики неисправны')
                

        
        