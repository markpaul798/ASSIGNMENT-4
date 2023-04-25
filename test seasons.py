From seasons import format_age_in_minutes


Def test_format_age_in_minutes():
    Assert format_age_in_minutes(0) == “0 minutes”
    Assert format_age_in_minutes(1) == “1 minute”
    Assert format_age_in_minutes(60) == “1 hour”
    Assert format_age_in_minutes(61) == “1 hour and 1 minute”
    Assert format_age_in_minutes(1440) == “1 day”
    Assert format_age_in_minutes(1501) == “1 day, 1 hour and 1 minute”
    Assert format_age_in_minutes(527040) == “1 year, 1 month and 1 day”
    Assert format_age_in_minutes(31622400) == “60 years and 1 day”
