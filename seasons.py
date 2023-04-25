From datetime import date, datetime
Import sys


Def main():
    Dob = input(“Please enter your date of birth (YYYY-MM-DD): “)
    Try:
        Birthdate = datetime.strptime(dob, “%Y-%m-%d”).date()
    Except ValueError:
        Print(“Invalid date format. Please enter in YYYY-MM-DD format.”)
        Sys.exit(1)

    Today = date.today()
    Age_in_years = today.year – birthdate.year – ((today.month, today.day) < (birthdate.month, birthdate.day))
    Age_in_minutes = age_in_years * 365 * 24 * 60

    Print(format_age_in_minutes(age_in_minutes))


Def format_age_in_minutes(age_in_minutes):
    Units = [
        (60 * 24 * 365, “year”),
        (60 * 24 * 30, “month”),
        (60 * 24 * 7, “week”),
        (60 * 24, “day”),
        (60, “hour”),
        (1, “minute”),
    ]

    Parts = []
    For unit, label in units:
        Count = age_in_minutes // unit
        Age_in_minutes -= count * unit
        If count:
            If count > 1:
                Label += “s”
            Parts.append(f”{count} {label}”)

    If len(parts) == 1:
        Return parts[0]
    Else:
        Return “, “.join(parts[:-1]) + “ and “ + parts[-1]


If __name__ == “__main__”:
    Main()
