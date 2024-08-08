from app.config import CSV_PATH
from app.scraper import MateScraper


def parse_mate_academy_courses() -> None:
    scraper = MateScraper()
    all_courses = scraper.get_all_courses()
    write_courses_to_csv(csv_path=CSV_PATH, all_courses=all_courses)


if __name__ == "__main__":
    parse_mate_academy_courses()
