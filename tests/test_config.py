# -*- coding: utf-8 -*-
"""
Test config.py
"""

from unittest import TestCase
from daylio_parser.config import MoodConfig


class TestConfig(TestCase):
    def test_default_mood_list(self):
        m = MoodConfig()

        self.assertEqual(m.moods[0].name, 'awful')
        self.assertEqual(m.moods[0].level, 1)
        self.assertEqual(m.moods[0].boundaries, (1, 1.5))

        self.assertEqual(m.moods[1].name, 'bad')
        self.assertEqual(m.moods[1].level, 2)
        self.assertEqual(m.moods[1].boundaries, (1.5, 2.5))

        self.assertEqual(m.moods[2].name, 'meh')
        self.assertEqual(m.moods[2].level, 3)
        self.assertEqual(m.moods[2].boundaries, (2.5, 3.5))

        self.assertEqual(m.moods[3].name, 'good')
        self.assertEqual(m.moods[3].level, 4)
        self.assertEqual(m.moods[3].boundaries, (3.5, 4.5))

        self.assertEqual(m.moods[4].name, 'rad')
        self.assertEqual(m.moods[4].level, 5)
        self.assertEqual(m.moods[4].boundaries, (4.5, 5.01))

    def test_custom_moods(self):
        moods = [
            ('bad', 'red'),
            ('neutral', 'orange'),
            ('good', 'green'),
        ]

        m = MoodConfig(moods)

        self.assertEqual(m.moods[0].name, 'bad')
        self.assertEqual(m.moods[0].level, 1)
        self.assertEqual(m.moods[0].boundaries, (1, 1.5))

        self.assertEqual(m.moods[1].name, 'neutral')
        self.assertEqual(m.moods[1].level, 2)
        self.assertEqual(m.moods[1].boundaries, (1.5, 2.5))

        self.assertEqual(m.moods[2].name, 'good')
        self.assertEqual(m.moods[2].level, 3)
        self.assertEqual(m.moods[2].boundaries, (2.5, 3.01))