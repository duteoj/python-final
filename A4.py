import sys
import sys
from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.result_saver import ResultSaver
from analytics.report import Report
from analytics.analyser import TopStudentsAnalyser, CountryAnalyser, DataAnalyser


def main():
    input_filename = 'global_university_students_performance_habits_10000.csv'
    output_filename = 'output/result.json'

    fm = FileManager(input_filename)
    if not fm.check_file():
        print('Stopping program.')
        sys.exit()
    fm.create_output_folder()

    dl = DataLoader(input_filename)
    dl.load()
    dl.preview_data()

    base = DataAnalyser(dl.students)
    print()
    print(base)
    base.analyse()

    analysers = [
        TopStudentsAnalyser(dl.students),
        CountryAnalyser(dl.students)
    ]

    print()
    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()
        print()

    saver = ResultSaver(analysers[0].result, output_filename)
    report = Report(analysers[0], saver)
    report.generate()


if __name__ == "__main__":
    main()
