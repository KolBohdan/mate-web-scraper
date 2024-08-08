import csv
from dataclasses import astuple

from config import CSV_PATH
from models import COURSE_FIELDS, Course
from scraper import MateScraper


def write_courses_to_csv(csv_path: str, all_courses: list[Course]) -> None:
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(COURSE_FIELDS)
        writer.writerows([astuple(cour) for cour in all_courses])


def parse_mate_academy_courses() -> None:
    scraper = MateScraper()
    all_courses = scraper.get_all_courses()
    write_courses_to_csv(csv_path=CSV_PATH, all_courses=all_courses)


if __name__ == "__main__":
    parse_mate_academy_courses()
