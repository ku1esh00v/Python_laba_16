def find_trains_by_destination(trains, destination):
    destination_trains = [train for train in trains if train.destination == destination]
    return destination_trains
