class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            sorted_list = sorted(
                self.students,
                key=lambda x: float(x['final_exam_score']),
                reverse=True
            )[:10]

            top_10_json = []
            for i, s in enumerate(sorted_list):
                top_10_json.append({
                    "rank": i + 1,
                    "student_id": s['student_id'],
                    "country": s['country'],
                    "major": s['major'],
                    "final_exam_score": float(s['final_exam_score']),
                    "GPA": float(s['GPA'])
                })

            self.result = {
                "analysis": "Top 10 Students by Exam Score",
                "total_students": len(self.students),
                "top_10": top_10_json
            }
            return self.result
        except Exception as e:
            print(f"Analysis error: {e}")
            return {}

    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)
        for key, value in self.result.items():
            if key != "top_10":
                print(f"{key}: {value}")
        if "top_10" in self.result:
            print("-" * 30)
            for s in self.result["top_10"]:
                print(f"{s['rank']}. {s['student_id']} | {s['country']} | "
                      f"{s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top 10 by Exam Score, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            country_counts = {}
            for s in self.students:
                country = s['country']
                if country in country_counts:
                    country_counts[country] += 1
                else:
                    country_counts[country] = 1

            top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

            self.result = {
                "analysis": "Country Analysis",
                "total_students": len(self.students),
                "total_countries": len(country_counts),
                "top_3": top_3,
                "all_countries": country_counts
            }
            return self.result
        except Exception as e:
            print(f"Analysis error: {e}")
            return {}

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        for key, value in self.result.items():
            if key not in ("top_3", "all_countries"):
                print(f"{key}: {value}")
        if "top_3" in self.result:
            print("top_3:", self.result["top_3"])
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
