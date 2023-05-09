class Car:
    
    def __init__(self, make, model_name, top_speed, color):
        
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
        
        # Variables
        self._current_speed = 0
        
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
        
class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_load = max_load
        
    @property
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
        
    def accelerate(self, step=10):
        self.current_speed += step
        
    def decelerate(self, step=10):
        self.current_speed -= step
        
truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print(truck)  # Black Mercedes Actros

truck.accelerate(10)
print(truck.current_speed) # 10