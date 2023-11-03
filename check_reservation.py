from models import MaligayaCourtReservationList, CountrysideCourtReservationList, TennisCourtReservationList


def check_reservation_maligaya(day, time_slot):
    day = day.capitalize()
    time_slot = time_slot.lower()

    reservation = MaligayaCourtReservationList.query.filter_by(reservation_date=day, reservation_time=time_slot).first()

    return True if reservation else False


def check_reservation_countryside(day, time_slot):
    day = day.capitalize()
    time_slot = time_slot.lower()

    reservation = CountrysideCourtReservationList.query.filter_by(reservation_date=day, reservation_time=time_slot).first()

    return True if reservation else False


def check_reservation_tennis(day, time_slot):
    day = day.capitalize()
    time_slot = time_slot.lower()

    reservation = TennisCourtReservationList.query.filter_by(reservation_date=day, reservation_time=time_slot).first()

    return True if reservation else False
