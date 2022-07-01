class Car:
    def __init__(self, make, model, max_speed, name, brake_rate, accelerate_rate):
        self.name = name
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.brake_rate = brake_rate
        self.accelerate_rate = accelerate_rate
        self.speed = 0

    def accelerate(self):
        if self.speed + self.accelerate_rate > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.accelerate_rate

    def decelerate(self, rate):
        if self.speed - rate < 0:
            self.speed = 0
        else:
            self.speed -= rate

    def brake(self):
        self.decelerate(self.brake_rate)
