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
        return(f'Тип тренировки: {self.training_type};
               fДлительность: {self.duration:.3f} ч;
               Дистанция: {self.distance:.3f} км;
               Ср. скорость: {self.speed:.3f} км/ч;
               Потрачено ккал: {self.calories:.3f}.')

@dataclass     
class Training:
    """Базовый класс тренировки"""
    M_IN_KM = 1000
    LEN_STEP = 0,65   

    action: int
    duration: float
    weight: float 

    @property
    def get_distance(self) -> float:
        """Вычисление пройденной дистанции в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM     

    @property    
    def get_mean_speed(self) -> float:
        """Вычисление средней скорости."""
        return self.get_distance() / self.duration
        
    def get_spent_calories(self) -> float:
        """ВЫчисление затраченных калорий"""
        pass

    def show_training_info(self) -> InfoMessage:
        """Возврат сообщения о результатах тренировки"""
        return InfoMessage( 
            type(self).__name__,  
            self.duration, 
            self.get_distance(), 
            self.get_mean_speed(), 
            self.get_spent_calories())  
      
class Running(Training):
    """Вид тренировки: бег."""
  
    @property
    def get_spent_calories(self) -> float:
          return ((18 * self.get_mean_speed() + 1.79) * self.weight / self.M_IN_KM * self.duration)
    
class SportsWalking(Training):  
    """Вид тренировки: спортивная ходьба."""  
    def __init__(self, action: int, duration: float, weight: float, height: float):
          super().__init__(action, duration, weight)
          self.height = height

    @property
    def get_spent_calories(self):
          return ((0.035 * self.weight + (self.get_mean_speed() ** 2 / self.height) * 0.029 * self.weight) * self.duration)

class Swimming(Training):
    """Вид тренировки: плавание."""
    LEN_STROKE = 1.38
    
    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: float):
          super().__init__(action, duration, weight)
          self.length_pool = length_pool
          self.count_pool = count_pool

    @property      
    def get_mean_speed(self) -> float:
          return (self.length_pool * self.count_pool / self.M_IN_KM / self.duration)

    @property 
    def get_spent_calories(self):
          return (self.get_mean_speed() + 1.1) * 2 * self.weight

    def read_package(workout_type: str, data: list) -> Training:
        """Получение данных от датчиков."""
        try:
             if workout_type == "SWM":
                  return Swimming(
                       data[0],
                       data[1],
                       data[2],
                       data[3],
                       data[4])
             elif workout_type == "RUN":
                  return Running(
                       data[0],
                       data[1],
                       data[2])
             elif workout_type == "WLK":
                  return SportsWalking(
                       data[0],
                       data[1],
                       data[2],
                       data[3])
        except IndexError:
             print("Ошибка чтения с датчиков")

    def main(Training) -> None:
        """Главная функция"""
        try:
            message_train = Training.show_training_info()
            print(message_train.get_message())
        except AttributeError:
            print("Данный тип тренировки неизвестен")
        pass

    if __name__ == "__main__":
         packages = [
              ("SWM", [720, 1, 80, 25, 40]),
              ("RUN", [15000, 1, 75]),
              ("WLK", [9000, 1, 75, 180]),
              ('WRK', [9000, 1, 75, 180]),
              ('WLK', [0, 1, 75, 180]),
              ([9000, 1, 75, 180]),
              ('WLK', [1, 75, 180])
         ]

    for i in range(len(packages)):
        if len(packages[i]) == 2:
            workout_type = packages[i][0] 
            data = packages[i][1] 
            if packages[i][1][0] > 0: 
                training = read_package(workout_type, data) 
                main(training) 
            else: 
                print('Вы еще не начали тренироваться=)') 
        else: 
            print('Не определен тип тренировки или датчики неисправны') 
                

        
        