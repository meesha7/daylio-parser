# -*- coding: utf-8 -*-
"""
Mood statistics
"""

import datetime
from typing import List

import numpy as np

from .parser import Entry


def average_moods(entries: List[Entry]):
    group_by_date = {}

    for entry in entries:
        date = datetime.date(
            entry.datetime.year,
            entry.datetime.month,
            entry.datetime.day
        )

        group_by_date.setdefault(date, [])
        group_by_date[date].append(entry.mood.level)

    result = []

    for date, moods in group_by_date.items():
        result.append((date, np.mean(moods)))

    return result