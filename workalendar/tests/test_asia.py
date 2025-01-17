from datetime import date
from workalendar.tests import GenericCalendarTest

from workalendar.asia import (
    HongKong, Japan, JapanBank, Qatar, Singapore,
    SouthKorea, Taiwan, Malaysia, China, Israel
)
from workalendar.asia.china import holidays as china_holidays
from workalendar.exceptions import CalendarError


class ChinaTest(GenericCalendarTest):

    cal_class = China

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)    # New year
        self.assertIn(date(2018, 2, 15), holidays)   # Spring Festival
        self.assertIn(date(2018, 2, 21), holidays)   # Spring Festival
        self.assertIn(date(2018, 10, 1), holidays)   # National Day
        self.assertIn(date(2018, 10, 7), holidays)   # National Day

        # Variable days
        self.assertIn(date(2018, 4, 5), holidays)    # Ching Ming Festival
        self.assertIn(date(2018, 4, 7), holidays)    # Ching Ming Festival
        self.assertIn(date(2018, 4, 29), holidays)   # Labour Day Holiday
        self.assertIn(date(2018, 5, 1), holidays)    # Labour Day Holiday
        self.assertIn(date(2018, 6, 18), holidays)   # Dragon Boat Festival
        self.assertIn(date(2018, 9, 24), holidays)   # Mid-Autumn Festival
        self.assertIn(date(2018, 12, 30), holidays)  # New year
        self.assertIn(date(2018, 12, 31), holidays)  # New year

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertNotIn(date(2019, 4, 28), holidays)  # Labour Day Shift
        self.assertIn(date(2019, 5, 1), holidays)  # Labour Day Holiday
        self.assertIn(date(2019, 5, 2), holidays)  # Labour Day Holiday
        self.assertIn(date(2019, 5, 3), holidays)  # Labour Day Holiday
        self.assertNotIn(date(2019, 5, 5), holidays)  # Labour Day Shift

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New Year
        self.assertIn(date(2020, 1, 25), holidays)  # Spring Festival
        self.assertIn(date(2020, 4, 4), holidays)  # Ching Ming Festival
        self.assertIn(date(2020, 4, 6), holidays)  # Ching Ming Festival
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day Holiday
        self.assertIn(date(2020, 5, 5), holidays)  # Labour Day Holiday
        self.assertIn(date(2020, 6, 25), holidays)  # Dragon Boat Festival
        self.assertIn(date(2020, 6, 27), holidays)  # Dragon Boat Festival
        self.assertIn(date(2020, 10, 1), holidays)  # National Day
        self.assertIn(date(2020, 10, 8), holidays)  # National Day

        self.assertNotIn(date(2020, 1, 19), holidays)  # Spring Festival Shift
        self.assertNotIn(date(2020, 2, 1), holidays)  # Spring Festival Shift
        self.assertNotIn(date(2020, 4, 26), holidays)  # Labour Day Shift
        self.assertNotIn(date(2020, 5, 9), holidays)  # Labour Day Shift
        self.assertNotIn(date(2020, 6, 28), holidays)  # Dragon Boat Shift
        self.assertNotIn(date(2020, 9, 27), holidays)  # National Day Shift
        self.assertNotIn(date(2020, 10, 10), holidays)  # National Day Shift

    def test_missing_holiday_year(self):
        save_2018 = china_holidays[2018]
        del china_holidays[2018]
        with self.assertRaises(CalendarError):
            self.cal.holidays_set(2018)
        china_holidays[2018] = save_2018

    def test_is_working_day(self):
        # It's a SAT, but it's a working day this year
        self.assertTrue(self.cal.is_working_day(date(2019, 2, 2)))
        # It's a SUN, but it's a working day this year
        self.assertTrue(self.cal.is_working_day(date(2019, 2, 3)))

    def test_add_working_days(self):
        # Normally, February 1st + 1 working day would be on February 4th
        # Because 2nd and 3rd are on SAT and SUN.
        self.assertEqual(
            self.cal.add_working_days(date(2019, 2, 1), 1),
            date(2019, 2, 2)
        )

    def test_sub_working_days(self):
        # Normally, February 4th - 1 working day would be on February 1st
        # Because 2nd and 3rd are on SAT and SUN.
        self.assertEqual(
            self.cal.sub_working_days(date(2019, 2, 4), 1),
            date(2019, 2, 3)
        )


class HongKongTest(GenericCalendarTest):

    cal_class = HongKong

    def test_year_2010(self):
        """ Interesting because Christmas fell on a Saturday and CNY fell
            on a Sunday, so didn't roll, and Ching Ming was on the same day
            as Easter Monday """
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 1, 1), holidays)    # New Year
        self.assertIn(date(2010, 2, 13), holidays)   # Chinese new year (shift)
        self.assertIn(date(2010, 2, 15), holidays)   # Chinese new year
        self.assertIn(date(2010, 2, 16), holidays)   # Chinese new year
        self.assertNotIn(date(2010, 2, 17), holidays)  # Not Chinese new year
        self.assertIn(date(2010, 4, 2), holidays)    # Good Friday
        self.assertIn(date(2010, 4, 3), holidays)    # Day after Good Friday
        self.assertIn(date(2010, 4, 5), holidays)    # Easter Monday
        self.assertIn(date(2010, 4, 6), holidays)    # Ching Ming (shifted)
        self.assertIn(date(2010, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2010, 5, 21), holidays)   # Buddha's Birthday
        self.assertIn(date(2010, 6, 16), holidays)   # Tuen Ng Festival
        self.assertIn(date(2010, 7, 1), holidays)    # HK SAR Establishment Day
        self.assertIn(date(2010, 9, 23), holidays)   # Day after Mid-Autumn
        self.assertIn(date(2010, 10, 1), holidays)   # National Day
        self.assertIn(date(2010, 10, 16), holidays)  # Chung Yeung Festival
        self.assertIn(date(2010, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2010, 12, 27), holidays)  # Boxing Day (shifted)

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # New Year
        self.assertIn(date(2013, 2, 11), holidays)   # Chinese new year
        self.assertIn(date(2013, 2, 12), holidays)   # Chinese new year
        self.assertIn(date(2013, 2, 13), holidays)   # Chinese new year
        self.assertIn(date(2013, 3, 29), holidays)   # Good Friday
        self.assertIn(date(2013, 3, 30), holidays)   # Day after Good Friday
        self.assertIn(date(2013, 4, 1), holidays)    # Easter Monday
        self.assertIn(date(2013, 4, 4), holidays)    # Ching Ming
        self.assertIn(date(2013, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2013, 5, 17), holidays)   # Buddha's Birthday
        self.assertIn(date(2013, 6, 12), holidays)   # Tuen Ng Festival
        self.assertIn(date(2013, 7, 1), holidays)    # HK SAR Establishment Day
        self.assertIn(date(2013, 9, 20), holidays)   # Day after Mid-Autumn
        self.assertIn(date(2013, 10, 1), holidays)   # National Day
        self.assertIn(date(2013, 10, 14), holidays)  # Chung Yeung Festival
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)    # New Year
        self.assertIn(date(2016, 2, 8), holidays)    # Chinese new year
        self.assertIn(date(2016, 2, 9), holidays)    # Chinese new year
        self.assertIn(date(2016, 2, 10), holidays)   # Chinese new year
        self.assertIn(date(2016, 3, 25), holidays)   # Good Friday
        self.assertIn(date(2016, 3, 26), holidays)   # Day after Good Friday
        self.assertIn(date(2016, 3, 28), holidays)   # Easter Monday
        self.assertIn(date(2016, 4, 4), holidays)    # Ching Ming
        self.assertIn(date(2016, 5, 2), holidays)    # Labour Day (shifted)
        self.assertIn(date(2016, 5, 14), holidays)   # Buddha's Birthday
        self.assertIn(date(2016, 6, 9), holidays)    # Tuen Ng Festival
        self.assertIn(date(2016, 7, 1), holidays)    # HK SAR Establishment Day
        self.assertIn(date(2016, 9, 16), holidays)   # Day after Mid-Autumn
        self.assertIn(date(2016, 10, 1), holidays)   # National Day
        self.assertIn(date(2016, 10, 10), holidays)  # Chung Yeung Festival
        self.assertIn(date(2016, 12, 26), holidays)  # Christmas Day (shifted)
        self.assertIn(date(2016, 12, 27), holidays)  # Boxing Day (shifted)

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 2), holidays)    # New Year (shifted)
        self.assertIn(date(2017, 1, 28), holidays)   # Chinese new year
        self.assertIn(date(2017, 1, 30), holidays)   # Chinese new year
        self.assertIn(date(2017, 1, 31), holidays)   # Chinese new year
        self.assertIn(date(2017, 4, 4), holidays)    # Ching Ming
        self.assertIn(date(2017, 4, 14), holidays)   # Good Friday
        self.assertIn(date(2017, 4, 15), holidays)   # Day after Good Friday
        self.assertIn(date(2017, 4, 17), holidays)   # Easter Monday
        self.assertIn(date(2017, 5, 1), holidays)    # Labour Day
        self.assertIn(date(2017, 5, 3), holidays)    # Buddha's Birthday
        self.assertIn(date(2017, 5, 30), holidays)   # Tuen Ng Festival
        self.assertIn(date(2017, 7, 1), holidays)    # HK SAR Establishment Day
        self.assertIn(date(2017, 10, 2), holidays)   # National Day (shifted)
        self.assertIn(date(2017, 10, 5), holidays)   # Day after Mid-Autumn
        self.assertIn(date(2017, 10, 28), holidays)  # Chung Yeung Festival
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2017, 12, 26), holidays)  # Boxing Day

    def test_chingming_festival(self):
        # This is the same as the Taiwan test, just different spelling
        # Could move this into a Core test
        self.assertIn(date(2005, 4, 5), self.cal.holidays_set(2005))
        self.assertIn(date(2006, 4, 5), self.cal.holidays_set(2006))
        self.assertIn(date(2007, 4, 5), self.cal.holidays_set(2007))
        self.assertIn(date(2008, 4, 4), self.cal.holidays_set(2008))
        self.assertIn(date(2010, 4, 5), self.cal.holidays_set(2010))
        self.assertIn(date(2011, 4, 5), self.cal.holidays_set(2011))
        self.assertIn(date(2012, 4, 4), self.cal.holidays_set(2012))
        self.assertIn(date(2013, 4, 4), self.cal.holidays_set(2013))
        self.assertIn(date(2014, 4, 5), self.cal.holidays_set(2014))
        self.assertIn(date(2015, 4, 4), self.cal.holidays_set(2015))
        self.assertIn(date(2016, 4, 4), self.cal.holidays_set(2016))
        self.assertIn(date(2017, 4, 4), self.cal.holidays_set(2017))
        self.assertIn(date(2018, 4, 5), self.cal.holidays_set(2018))


class JapanTest(GenericCalendarTest):

    cal_class = Japan

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # new year
        self.assertIn(date(2013, 2, 11), holidays)   # Foundation Day
        self.assertIn(date(2013, 3, 20), holidays)   # Vernal Equinox Day
        self.assertIn(date(2013, 4, 29), holidays)   # Showa Day
        self.assertIn(date(2013, 5, 3), holidays)  # Constitution Memorial Day
        self.assertIn(date(2013, 5, 4), holidays)    # Greenery Day
        self.assertIn(date(2013, 5, 5), holidays)    # Children's Day
        self.assertIn(date(2013, 9, 23), holidays)   # Autumnal Equinox Day
        self.assertIn(date(2013, 11, 3), holidays)   # Culture Day
        self.assertIn(date(2013, 11, 23), holidays)  # Labour Thanksgiving Day
        self.assertIn(date(2013, 12, 23), holidays)  # The Emperor's Birthday

        # Variable days
        self.assertIn(date(2013, 1, 14), holidays)   # Coming of Age Day
        self.assertIn(date(2013, 7, 15), holidays)   # Marine Day
        self.assertIn(date(2013, 9, 16), holidays)   # Respect-for-the-Aged Day
        self.assertIn(date(2013, 10, 14), holidays)  # Health and Sports Day

    def test_year_2016(self):
        # Before 2016, no Mountain Day
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(date(2014, 8, 11), holidays)   # Mountain Day
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 8, 11), holidays)   # Mountain Day
        # After 2016, yes
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 8, 11), holidays)   # Mountain Day
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 8, 11), holidays)   # Mountain Day

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 14), holidays)  # Coming of Age Day
        self.assertIn(date(2019, 5, 1), holidays)  # Coronation Day
        self.assertIn(date(2019, 5, 6), holidays)  # Children's Day
        self.assertIn(date(2019, 8, 12), holidays)  # Mountain Day Observed
        self.assertIn(date(2019, 11, 4), holidays)  # Culture Day Observed

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 7, 23), holidays)  # Marine Day
        self.assertIn(date(2020, 7, 24), holidays)  # Sports Day
        self.assertIn(date(2020, 8, 10), holidays)  # Mountain Day adjustment
        self.assertNotIn(date(2020, 8, 11), holidays)  # Mountain Day
        self.assertNotIn(date(2020, 12, 31), holidays)  # New Year's Bank Day


class JapanBankTest(GenericCalendarTest):
    cal_class = JapanBank

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 2), holidays)  # New Year's Bank Day
        self.assertIn(date(2019, 1, 3), holidays)  # New Year's Bank Day
        self.assertIn(date(2019, 1, 14), holidays)  # Coming of Age Day
        self.assertIn(date(2019, 5, 3), holidays)  # Constitution Memorial Day
        self.assertIn(date(2019, 11, 4), holidays)  # Culture Day Observed
        self.assertIn(date(2019, 12, 31), holidays)  # New Year's Bank Day

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 2), holidays)  # New Year's Bank Day
        self.assertIn(date(2020, 1, 3), holidays)  # New Year's Bank Day
        self.assertIn(date(2020, 12, 31), holidays)  # New Year's Bank Day
        self.assertIn(date(2020, 8, 10), holidays)  # Mountain Day adjustment
        self.assertNotIn(date(2020, 8, 11), holidays)  # Mountain Day
        self.assertIn(date(2020, 7, 23), holidays)  # Marine Day
        self.assertIn(date(2020, 7, 24), holidays)  # Sports Day


class MalaysiaTest(GenericCalendarTest):
    cal_class = Malaysia

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # New Year's Day
        self.assertIn(date(2013, 1, 28), holidays)   # Thaipusam
        self.assertIn(date(2013, 2, 1), holidays)    # Federal Territory Day
        self.assertIn(date(2013, 2, 11), holidays)   # 2nd day of Lunar NY
        self.assertIn(date(2013, 2, 12), holidays)   # 1st day (Sun lieu)
        self.assertIn(date(2013, 5, 1), holidays)    # Workers' Day
        self.assertIn(date(2013, 5, 24), holidays)   # Vesak Day
        self.assertIn(date(2013, 8, 8), holidays)    # 1st day eid-al-fitr
        self.assertIn(date(2013, 8, 9), holidays)    # 2nd day eid-al-fitr
        self.assertIn(date(2013, 8, 31), holidays)   # National Day
        self.assertIn(date(2013, 9, 16), holidays)   # Malaysia Day
        self.assertIn(date(2013, 10, 15), holidays)  # Hari Raya Haji
        self.assertIn(date(2013, 11, 2), holidays)   # Deepavali
        self.assertIn(date(2013, 11, 5), holidays)   # Islamic New Year
        self.assertIn(date(2013, 12, 25), holidays)  # Xmas

    def test_year_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)    # New Year's Day
        self.assertIn(date(2012, 1, 24), holidays)   # Federal Territory Day
        self.assertIn(date(2012, 2, 1), holidays)    # 2nd day of Lunar NY
        self.assertIn(date(2012, 5, 1), holidays)    # 1st day (Sun lieu)
        self.assertIn(date(2012, 5, 5), holidays)    # Workers' Day
        self.assertIn(date(2012, 8, 19), holidays)   # 1st day eid-al-fitr
        self.assertIn(date(2012, 8, 20), holidays)   # 2nd day eid-al-fitr
        self.assertIn(date(2012, 8, 31), holidays)   # National Day
        self.assertIn(date(2012, 9, 16), holidays)   # Malaysia Day
        self.assertIn(date(2012, 10, 26), holidays)  # Hari Raya Haji
        self.assertIn(date(2012, 11, 13), holidays)  # Islamic New Year
        self.assertIn(date(2012, 11, 15), holidays)  # Deepavali
        self.assertIn(date(2012, 12, 25), holidays)  # Xmas

    def test_nuzul_al_quran(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 6, 12), holidays)
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 6, 1), holidays)

    def test_fix_deepavali_2018(self):
        holidays = self.cal.holidays(2018)
        holidays = dict(holidays)
        deepavali = date(2018, 11, 6)
        self.assertIn(deepavali, holidays)
        self.assertEqual(holidays[deepavali], "Deepavali")

    def test_msia_thaipusam(self):
        years = self.cal.MSIA_THAIPUSAM.keys()
        # we only have them for years 2010-2020
        self.assertEqual(
            set(years),
            set(range(2010, 2021))
        )

    def test_missing_deepavali(self):
        save_2020 = self.cal.MSIA_DEEPAVALI[2020]
        del self.cal.MSIA_DEEPAVALI[2020]
        with self.assertRaises(KeyError):
            self.cal.holidays(2020)
        # Back to normal, to avoid breaking further tests
        self.cal.MSIA_DEEPAVALI[2020] = save_2020

    def test_missing_thaipusam(self):
        save_2020 = self.cal.MSIA_THAIPUSAM[2020]
        del self.cal.MSIA_THAIPUSAM[2020]
        with self.assertRaises(KeyError):
            self.cal.holidays(2020)
        # Back to normal, to avoid breaking further tests
        self.cal.MSIA_THAIPUSAM[2020] = save_2020


class QatarTest(GenericCalendarTest):
    cal_class = Qatar

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 7, 9), holidays)  # start ramadan
        # warning, the official date was (2013, 8, 10)
        self.assertIn(date(2013, 8, 8), holidays)  # eid al fitr
        # The official date was (2013, 10, 14)
        self.assertIn(date(2013, 10, 15), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 16), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 17), holidays)  # eid al adha
        self.assertIn(date(2013, 10, 18), holidays)  # eid al adha
        self.assertIn(date(2013, 12, 18), holidays)  # National Day

    def test_weekend(self):
        # In Qatar, Week-end days are Friday / Sunday.
        weekend_day = date(2017, 5, 12)  # This is a Friday
        non_weekend_day = date(2017, 5, 14)  # This is a Sunday
        self.assertFalse(self.cal.is_working_day(weekend_day))
        self.assertTrue(self.cal.is_working_day(non_weekend_day))


class SingaporeTest(GenericCalendarTest):

    cal_class = Singapore

    def test_CNY_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 2, 14), holidays)  # CNY1
        self.assertIn(date(2010, 2, 15), holidays)  # CNY2
        self.assertIn(date(2010, 2, 16), holidays)  # Rolled day for CNY

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New Year
        self.assertIn(date(2013, 2, 10), holidays)  # CNY1
        self.assertIn(date(2013, 2, 11), holidays)  # CNY2
        self.assertIn(date(2013, 2, 12), holidays)  # Rolled day for CNY
        self.assertIn(date(2013, 3, 29), holidays)  # Good Friday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2013, 5, 24), holidays)  # Vesak Day
        self.assertIn(date(2013, 8, 8), holidays)  # Hari Raya Puasa
        self.assertIn(date(2013, 8, 9), holidays)  # National Day
        self.assertIn(date(2013, 10, 15), holidays)  # Hari Raya Haji
        self.assertIn(date(2013, 11, 3), holidays)  # Deepavali
        self.assertIn(date(2013, 11, 4), holidays)  # Deepavali shift
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas Day

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)  # New Year
        self.assertIn(date(2018, 2, 16), holidays)  # CNY
        self.assertIn(date(2018, 2, 17), holidays)  # CNY
        self.assertIn(date(2018, 3, 30), holidays)  # Good Friday
        self.assertIn(date(2018, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2018, 5, 29), holidays)  # Vesak Day
        self.assertIn(date(2018, 6, 15), holidays)  # Hari Raya Puasa
        self.assertIn(date(2018, 8, 9), holidays)  # National Day
        self.assertIn(date(2018, 8, 22), holidays)  # Hari Raya Haji
        self.assertIn(date(2018, 11, 6), holidays)  # Deepavali
        self.assertIn(date(2018, 12, 25), holidays)  # Christmas Day

    def test_fixed_holiday_shift(self):
        # Labour Day was on a Sunday in 2016
        holidays = self.cal.holidays_set(2016)
        # Labour Day (sunday)
        self.assertIn(date(2016, 5, 1), holidays)
        # Shifted day (Monday)
        self.assertIn(date(2016, 5, 2), holidays)

    def test_deepavali(self):
        # At the moment, we have values for deepavali only until year 2020
        for year in range(2000, 2021):
            self.assertIn(year, self.cal.DEEPAVALI)

    def test_deepavali_current_year(self):
        # This is a regression test. We should be able to have the deepavali
        # value until this year and probably a few years in the future
        current_year = date.today().year
        self.assertIn(current_year, self.cal.DEEPAVALI)


class SouthKoreaTest(GenericCalendarTest):

    cal_class = SouthKorea

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # new year
        self.assertIn(date(2013, 3, 1), holidays)    # Independence day
        self.assertIn(date(2013, 5, 5), holidays)    # children's day
        self.assertIn(date(2013, 6, 6), holidays)    # Memorial day
        self.assertIn(date(2013, 8, 15), holidays)   # Liberation day
        self.assertIn(date(2013, 10, 3), holidays)   # National Foundation Day
        self.assertIn(date(2013, 10, 9), holidays)   # Hangul Day
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

        # Variable days
        self.assertIn(date(2013, 2, 9), holidays)
        self.assertIn(date(2013, 2, 10), holidays)
        self.assertIn(date(2013, 2, 11), holidays)
        self.assertIn(date(2013, 5, 17), holidays)
        self.assertIn(date(2013, 9, 18), holidays)
        self.assertIn(date(2013, 9, 19), holidays)
        self.assertIn(date(2013, 9, 20), holidays)


class TaiwanTest(GenericCalendarTest):

    cal_class = Taiwan

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # New Year
        self.assertIn(date(2013, 2, 9), holidays)    # Chinese new year's eve
        self.assertIn(date(2013, 2, 10), holidays)   # Chinese new year
        self.assertIn(date(2013, 2, 11), holidays)   # Spring Festival
        self.assertIn(date(2013, 2, 12), holidays)   # Spring Festival
        self.assertIn(date(2013, 2, 28), holidays)   # 228 Peace Memorial Day
        self.assertIn(date(2013, 4, 4), holidays)    # Children's Day
        self.assertIn(date(2013, 6, 12), holidays)   # Dragon Boat Festival
        self.assertIn(date(2013, 9, 19), holidays)   # Mid-Autumn Festival
        self.assertIn(date(2013, 10, 10), holidays)  # National Day

    def test_qingming_festival(self):
        self.assertIn(date(2001, 4, 5), self.cal.holidays_set(2001))
        self.assertIn(date(2002, 4, 5), self.cal.holidays_set(2002))
        self.assertIn(date(2005, 4, 5), self.cal.holidays_set(2005))
        self.assertIn(date(2006, 4, 5), self.cal.holidays_set(2006))
        self.assertIn(date(2007, 4, 5), self.cal.holidays_set(2007))
        self.assertIn(date(2008, 4, 4), self.cal.holidays_set(2008))
        self.assertIn(date(2010, 4, 5), self.cal.holidays_set(2010))
        self.assertIn(date(2011, 4, 5), self.cal.holidays_set(2011))
        self.assertIn(date(2012, 4, 4), self.cal.holidays_set(2012))
        self.assertIn(date(2013, 4, 4), self.cal.holidays_set(2013))
        self.assertIn(date(2014, 4, 4), self.cal.holidays_set(2014))


class IsraelTest(GenericCalendarTest):

    cal_class = Israel

    def test_holidays_2017(self):
        holidays = self.cal.holidays_set(2017)

        self.assertIn(date(2017, 4, 11), holidays)  # Passover (Pesach)
        self.assertIn(date(2017, 4, 17), holidays)  # Passover (Pesach)
        self.assertIn(
            date(2017, 5, 2), holidays
        )  # Independence Day (Yom Ha-Atzmaut), was early in 2017
        self.assertIn(date(2017, 5, 31), holidays)  # Shavuot
        self.assertIn(
            date(2017, 9, 21), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(
            date(2017, 9, 22), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(
            date(2017, 9, 30), holidays
        )  # Yom Kippur (already a Saturday - Shabbat, weekend day)
        self.assertIn(date(2017, 10, 5), holidays)  # Sukkot
        self.assertIn(date(2017, 10, 12), holidays)  # Sukkot

    def test_holidays_2018(self):
        holidays = self.cal.holidays_set(2018)

        self.assertIn(date(2018, 3, 31), holidays)  # Passover (Pesach)
        self.assertIn(date(2018, 4, 6), holidays)  # Passover (Pesach)
        self.assertIn(
            date(2018, 4, 19), holidays
        )  # Independence Day (Yom Ha-Atzmaut), was delayed in 2018
        self.assertIn(date(2018, 5, 20), holidays)  # Shavuot
        self.assertIn(
            date(2018, 9, 10), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(
            date(2018, 9, 11), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(date(2018, 9, 19), holidays)  # Yom Kippur
        self.assertIn(date(2018, 9, 24), holidays)  # Sukkot
        self.assertIn(date(2018, 9, 30), holidays)  # Sukkot

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)

        self.assertIn(date(2019, 4, 20), holidays)  # Passover (Pesach)
        self.assertIn(date(2019, 4, 26), holidays)  # Passover (Pesach)
        self.assertIn(
            date(2019, 5, 9), holidays
        )  # Independence Day (Yom Ha-Atzmaut), was delayed in 2019
        self.assertIn(date(2019, 6, 9), holidays)  # Shavuot
        self.assertIn(
            date(2019, 9, 30), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(
            date(2019, 10, 1), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(
            date(2019, 10, 2), holidays
        )  # Jewish New Year (Rosh Ha-Shana)
        self.assertIn(date(2019, 10, 9), holidays)  # Yom Kippur
        self.assertIn(date(2019, 10, 14), holidays)  # Sukkot
        self.assertIn(date(2019, 10, 20), holidays)  # Sukkot

        # Leap year Purim
        self.assertIn(date(2019, 3, 21), holidays)  # purim
        self.assertIn(date(2019, 3, 22), holidays)  # shushan purim
