import pytest
from src.cinema_booking import CinemaBooking


def test_view_movies():
    cinema = CinemaBooking()

    movies = cinema.view_movies()

    assert "Leo" in movies
    assert "Interstellar" in movies


def test_view_shows():
    cinema = CinemaBooking()

    shows = cinema.view_shows("Leo")

    assert "10:00 AM" in shows
    assert "6:00 PM" in shows


def test_display_seats():
    cinema = CinemaBooking()

    seats = cinema.display_seats()

    assert "A1" in seats
    assert seats["A1"] is False


def test_seat_availability():
    cinema = CinemaBooking()

    assert cinema.check_seat_availability("A1") is True


def test_successful_booking():
    cinema = CinemaBooking()

    assert cinema.book_seat("A1") is True
    assert cinema.check_seat_availability("A1") is False


def test_duplicate_seat_prevention():
    cinema = CinemaBooking()

    cinema.book_seat("A1")

    with pytest.raises(
        ValueError,
        match="Cannot allocate A1: seat is already booked"
    ):
        cinema.book_seat("A1")


def test_cancellation():
    cinema = CinemaBooking()

    cinema.book_seat("A1")
    cinema.cancel_booking("A1")

    assert cinema.check_seat_availability("A1") is True


def test_price_calculation():
    cinema = CinemaBooking(ticket_price=150)

    assert cinema.calculate_ticket_cost(2) == 300
    assert cinema.calculate_ticket_cost(4) == 600


def test_confirm_booking():
    cinema = CinemaBooking()

    booking = cinema.confirm_booking(
        "Leo",
        "6:00 PM",
        ["A1", "A2"]
    )

    assert booking["status"] == "Confirmed"
    assert booking["movie"] == "Leo"
    assert booking["show_time"] == "6:00 PM"
    assert booking["seats"] == ["A1", "A2"]
    assert booking["total_cost"] == 300


def test_allocate_seat():
    cinema = CinemaBooking()

    assert cinema.allocate_seat("B2") is True
    assert "B2" not in cinema.get_available_seats()


def test_display_available_seats():
    cinema = CinemaBooking()

    cinema.allocate_seat("A1")

    available_seats = cinema.display_available_seats()

    assert "A1" not in available_seats
    assert "A2" in available_seats