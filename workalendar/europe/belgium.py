# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Belgium(WesternCalendar, ChristianMixin):
    "Belgium"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Labour Day"),
        (7, 21, "National Day"),
        (11, 11, "Armistice of 1918"),
    )

    include_easter_monday = True
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True