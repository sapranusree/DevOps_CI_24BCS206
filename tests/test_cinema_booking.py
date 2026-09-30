import unittest
from src.cinema_booking import CinemaBooking


class TestCinemaBooking(unittest.TestCase):

    def test_view_movies(self):
        cinema = CinemaBooking()

        movies = cinema.view_movies()

        self.assertIn("Leo", movies)
        self.assertIn("Interstellar", movies)

    def test_view_shows(self):
        cinema = CinemaBooking()

        shows = cinema.view_shows("Leo")

        self.assertIn("10:00 AM", shows)
        self.assertIn("6:00 PM", shows)

    def test_display_seats(self):
        cinema = CinemaBooking()

        seats = cinema.display_seats()

        self.assertIn("A1", seats)
        self.assertFalse(seats["A1"])

    def test_seat_availability(self):
        cinema = CinemaBooking()

        self.assertTrue(
            cinema.check_seat_availability("A1")
        )

    def test_invalid_empty_seat_validation(self):
        cinema = CinemaBooking()

        with self.assertRaisesRegex(
            ValueError,
            "Seat number cannot be empty"
        ):
            cinema.check_seat_availability("")

    def test_successful_booking(self):
        cinema = CinemaBooking()

        result = cinema.book_seat("A1")

        self.assertTrue(result)
        self.assertFalse(
            cinema.check_seat_availability("A1")
        )

    def test_duplicate_seat_prevention(self):
        cinema = CinemaBooking()

        cinema.book_seat("A1")

        with self.assertRaisesRegex(
            ValueError,
            "Duplicate booking prevented: A1 is already booked"
        ):
            cinema.book_seat("A1")

    def test_cancellation(self):
        cinema = CinemaBooking()

        cinema.book_seat("A1")
        cinema.cancel_booking("A1")

        self.assertTrue(
            cinema.check_seat_availability("A1")
        )

    def test_price_calculation(self):
        cinema = CinemaBooking(ticket_price=150)

        self.assertEqual(
            cinema.calculate_ticket_cost(2),
            300
        )

        self.assertEqual(
            cinema.calculate_ticket_cost(4),
            600
        )

    def test_confirm_booking(self):
        cinema = CinemaBooking()

        booking = cinema.confirm_booking(
            "Leo",
            "6:00 PM",
            ["A1", "A2"]
        )

        self.assertEqual(
            booking["status"],
            "Confirmed"
        )

        self.assertEqual(
            booking["movie"],
            "Leo"
        )

        self.assertEqual(
            booking["show_time"],
            "6:00 PM"
        )

        self.assertEqual(
            booking["seats"],
            ["A1", "A2"]
        )

        self.assertEqual(
            booking["total_cost"],
            300
        )

    def test_allocate_seat(self):
        cinema = CinemaBooking()

        result = cinema.allocate_seat("B2")

        self.assertTrue(result)

        self.assertNotIn(
            "B2",
            cinema.get_available_seats()
        )

    def test_display_available_seats(self):
        cinema = CinemaBooking()

        cinema.allocate_seat("A1")

        available_seats = (
            cinema.display_available_seats()
        )

        self.assertNotIn(
            "A1",
            available_seats
        )

        self.assertIn(
            "A2",
            available_seats
        )


if __name__ == "__main__":
    unittest.main()