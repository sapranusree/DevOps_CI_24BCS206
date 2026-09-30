class CinemaBooking:
    def __init__(self, ticket_price=150):
        self.ticket_price = ticket_price

        self.movies = [
            "Leo",
            "Interstellar",
            "Avengers: Endgame"
        ]

        self.shows = {
            "Leo": ["10:00 AM", "2:00 PM", "6:00 PM"],
            "Interstellar": ["11:00 AM", "3:00 PM", "7:00 PM"],
            "Avengers: Endgame": ["12:00 PM", "4:00 PM", "8:00 PM"]
        }

        # Seats: A1-A5, B1-B5, C1-C5
        self.seats = {
            f"{chr(65 + row)}{seat}": False
            for row in range(3)
            for seat in range(1, 6)
        }

    def view_movies(self):
        return self.movies

    def view_shows(self, movie):
        if movie not in self.shows:
            raise ValueError("Movie not found.")

        return self.shows[movie]

    def display_seats(self):
        return self.seats.copy()

    def display_available_seats(self):
        return [
            seat
            for seat, booked in self.seats.items()
            if not booked
        ]

    def check_seat_availability(self, seat):
        if not isinstance(seat, str) or not seat.strip():
            raise ValueError("Seat number cannot be empty.")

        if seat not in self.seats:
            raise ValueError("Invalid seat number.")

        return not self.seats[seat]

    def allocate_seat(self, seat):
        if seat not in self.seats:
            raise ValueError("Invalid seat number.")

        if self.seats[seat]:
            raise ValueError(
                f"Duplicate booking prevented: {seat} is already booked"
            )

        self.seats[seat] = True
        return True

    def book_seat(self, seat):
        return self.allocate_seat(seat)

    def cancel_booking(self, seat):
        if seat not in self.seats:
            raise ValueError("Invalid seat number.")

        if not self.seats[seat]:
            raise ValueError("Seat is not booked.")

        self.seats[seat] = False
        return True

    def calculate_ticket_cost(self, number_of_tickets):
        if number_of_tickets <= 0:
            raise ValueError(
                "Number of tickets must be greater than zero."
            )

        return number_of_tickets * self.ticket_price

    def calculate_price(self, number_of_tickets):
        return self.calculate_ticket_cost(number_of_tickets)

    def confirm_booking(self, movie, show_time, seats):
        if movie not in self.movies:
            raise ValueError("Movie not found.")

        if show_time not in self.shows[movie]:
            raise ValueError("Invalid show time.")

        for seat in seats:
            if seat not in self.seats:
                raise ValueError(
                    f"Invalid seat number: {seat}"
                )

            if self.seats[seat]:
                raise ValueError(
                    f"Seat {seat} is already booked."
                )

        for seat in seats:
            self.seats[seat] = True

        total_cost = self.calculate_ticket_cost(len(seats))

        return {
            "movie": movie,
            "show_time": show_time,
            "seats": seats,
            "total_cost": total_cost,
            "status": "Confirmed"
        }

    def get_available_seats(self):
        return [
            seat
            for seat, booked in self.seats.items()
            if not booked
        ]