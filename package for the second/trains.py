class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def __str__(self):
        return f"Поезд номер {self.train_number} с пунктом назначения {self.destination} отправляется в {self.departure_time}"
