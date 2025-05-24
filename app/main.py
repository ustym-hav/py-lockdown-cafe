from typing import List

from app.errors import VaccineError, NotWearingMaskError

from app.cafe import Cafe


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    check_vaccine = None
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            check_vaccine = True
        except NotWearingMaskError:
            masks_to_buy += 1
    if check_vaccine:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
