import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# ---------- booking_cost ----------
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000

def test_unknown_room():
    with pytest.raises(ValueError):
        booking_cost("penthouse", 2, 2, False)

def test_invalid_nights():
    with pytest.raises(ValueError):
        booking_cost("standard", 0, 2, False)

def test_peak_season():
    assert booking_cost("standard", 1, 2, True) == 2500

def test_extra_guests():
    assert booking_cost("standard", 1, 4, False) == 3000

def test_long_stay_discount():
    assert booking_cost("standard", 7, 2, False) == 12600


# ---------- cancellation_refund ----------
def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

def test_partial_refund():
    assert cancellation_refund(1000, 3, False) == 500

def test_no_refund():
    assert cancellation_refund(1000, 1, False) == 0

def test_member_bonus_refund():
    assert cancellation_refund(1000, 1, True) == 250

def test_member_partial_refund():
    assert cancellation_refund(1000, 3, True) == 750

def test_member_full_refund():
    assert cancellation_refund(1000, 10, True) == 1000


# ---------- room_upgrade ----------
def test_upgrade_no_rooms_free():
    assert room_upgrade("standard", True, 0) == "standard"

def test_upgrade_standard_member():
    assert room_upgrade("standard", True, 5) == "deluxe"

def test_upgrade_deluxe_member():
    assert room_upgrade("deluxe", True, 5) == "suite"

def test_standard_non_member():
    assert room_upgrade("standard", False, 5) == "standard"

def test_deluxe_non_member():
    assert room_upgrade("deluxe", False, 5) == "deluxe"

def test_suite_member():
    assert room_upgrade("suite", True, 5) == "suite"