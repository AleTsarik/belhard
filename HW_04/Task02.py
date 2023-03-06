# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy: bool = False


class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if not car.is_busy:
                if count_passengers <= car.count_passenger_seats:
                    if is_baby:
                        if car.is_baby_seat:
                            car.is_busy = True
                            return f'Order: {count_passengers} passengers, baby ({is_baby}).\nSelected car is {car.color}, passenger seats: {car.count_passenger_seats}, baby seats: {car.is_baby_seat}, is busy: {car.is_busy}'
                    else:
                        car.is_busy = True
                        return f'Order: {count_passengers} passengers, baby ({is_baby}).\nSelected car is {car.color}, passenger seats: {car.count_passenger_seats}, baby seats: {car.is_baby_seat}, is busy: {car.is_busy}'
            else:
                return None


car1 = Car('blue', 3, True)
car2 = Car('green', 4, False)
car3 = Car('red', 7, False)
car4 = Car('silver', 8, True)

all_taxi = Taxi([car1, car2, car3, car4])
order = all_taxi.find_car(3, False)

print(order)
