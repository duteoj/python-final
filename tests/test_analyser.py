import unittest
from analytics.analyser import TopStudentsAnalyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"student_id": "S001", "country": "USA",    "major": "Engineering",
             "GPA": "3.8", "sleep_hours": "7", "final_exam_score": "95",
             "study_hours_per_day": "4"},
            {"student_id": "S002", "country": "India",  "major": "Medicine",
             "GPA": "2.5", "sleep_hours": "5", "final_exam_score": "72",
             "study_hours_per_day": "2"},
            {"student_id": "S003", "country": "USA",    "major": "Biology",
             "GPA": "3.9", "sleep_hours": "8", "final_exam_score": "98",
             "study_hours_per_day": "5"},
            {"student_id": "S004", "country": "Canada", "major": "Law",
             "GPA": "1.8", "sleep_hours": "4", "final_exam_score": "55",
             "study_hours_per_day": "1"},
            {"student_id": "S005", "country": "India",  "major": "Physics",
             "GPA": "3.5", "sleep_hours": "6", "final_exam_score": "88",
             "study_hours_per_day": "3"},
        ]

    def test_result_is_not_empty(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("top_10", analyser.result)

    def test_analyse_twice(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == '__main__':
    unittest.main()
