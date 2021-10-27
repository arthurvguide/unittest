from datetime import date, timedelta
import requests

class Student:
    """ A Student class as base method for testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    def email(self) :
        return f"{self._first_name}.{self._last_name}@email.com".lower() 

    def apply_extension(self, extension):
     self.end_date = self.end_date + timedelta(days=extension)

    def course_schedule(self):
        response = requests.get(f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")
        
        if response.ok:
            return response.text
        else:
            return "Something went wrong"   