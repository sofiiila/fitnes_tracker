    #training_type, duration, distance, speed, calories(float до 3 знаков)
    #show_training_info(): 
    # собственный метод get_message() return f'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.'
class InfoMessage:
    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float) -> str:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> None:
        return(f'Тип тренировки: {self.training_type};
               fДлительность: {self.duration:.3f} ч;
               Дистанция: {self.distance:.3f} км;
               Ср. скорость: {self.speed:.3f} км/ч;
               Потрачено ккал: {self.calories:.3f}.') 

#формула расчета action * LEN_STEP / M_IN_KM  #action: int, duration: float, weight: float для всех дочерних      
class Training:
    M_IN_KM = 1000
    LEN_STEP = 0,65   

    def __init__(self, action: int, duration: float, weight: float) -> None:
            self.action = action
            self.duration = duration
            self.weight = weight 
    
    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM     
        
    def get_mean_speed(self) -> float:#преодоленная дистанция за тренировку / время_тренировки
        return self.get_distance() / self.duration
        
    def get_spent_calories(self) -> float:
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(  
            self.duration, 
            self.get_distance(), 
            self.get_mean_speed(), 
            self.get_spent_calories())  
      
class Running(Training):
    def get_spent_calories(self) -> float:
          return ((18 * self.get_mean_speed() + 1.79) * self.weight / self.M_IN_KM * self.duration)
    
class SportsWalking(Training):    # доп параметр height расчет калорий ф-ла ((0.035 * вес + (сред скорость в м/с**2/ рост в м)*0.029*вес)*время трен в мин)
    def __init__(self, action: int, duration: float, weight: float, height: float):
          super().__init__(action, duration, weight)
          self.height = height

    def get_spent_calories(self):
          return ((0.035 * self.weight + (self.get_mean_speed() ** 2 / self.height) * 0.029 * self.weight) * self.duration)

class Swimming(Training):# length_pool, count_pool доп парам  дл басс*count_pool / M_IN_KM / время трен(сред скор + 1.1)*2*вес*время трен (LEN_STROKE = 1,38)
    LEN_STROKE = 1.38
    
    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: float):
          super().__init__(action, duration, weight)
          self.length_pool = length_pool
          self.count_pool = count_pool
          
    def get_mean_speed(self) -> float:
          return (self.length_pool * self.count_pool / self.M_IN_KM / self.duration)

    def get_spent_calories(self):
          return (self.get_mean_speed() + 1.1) * 2 * self.weight

    def read_package(workout_type: str, data: list) -> Training:#словарь с кодами класс трен 'SWM' 'RUN' 'WLK'
        ...

        
        