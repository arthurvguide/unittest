import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Jhon", "Doe")

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "Jhon Doe")

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        email = self.student.email()
        self.assertEqual(email, "jhon.doe@email.com")
    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(10)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=10))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
    
    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")
            
if __name__ == "__main__":
    unittest.main()