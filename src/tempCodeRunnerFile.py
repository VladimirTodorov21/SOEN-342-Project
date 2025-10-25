if isinstance(connectionChoice, tuple):
            connection_1, connection_2 = connectionChoice
            print(f"Multi-stop Trip from {connection_1.getDepartureCity()} to {connection_2.getArrivalCity()} has been booked for {numTravelers} travelers!\n")
          else:
            print(f"Direct Trip from {connectionChoice.getDepartureCity()} to {connectionChoice.getArrivalCity()} has been booked for {numTravelers} travelers!\n")