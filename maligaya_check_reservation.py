from models import MaligayaCourtReservationList


def check_reservation(day, time_slot):
    day = day.capitalize()
    time_slot = time_slot.lower()

    reservation = MaligayaCourtReservationList.query.filter_by(reservation_date=day, reservation_time=time_slot).first()

    return True if reservation else False
