import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.config import (
    URL_TO_SCRAPE,
    LANGUAGE_BUTTON_CSS_SELECTOR,
    LANGUAGES_CSS_SELECTOR,
    LANGUAGE,
    SUBMIT_LANGUAGE_BUTTON_CSS_SELECTOR,
    COURSES_CSS_SELECTOR,
    MODULES_NUMBER_CSS_SELECTOR,
    TOPICS_NUMBER_CSS_SELECTOR,
    COURSE_DURATION_CSS_SELECTOR,
)
from app.enums import CourseType
from app.models import Course
from app.web_driver import driver


class MateScraper:
    @staticmethod
    def change_language() -> None:
        language_button = driver.find_element(
            By.CSS_SELECTOR, LANGUAGE_BUTTON_CSS_SELECTOR
        )

        language_button.click()
        time.sleep(3)
        languages = driver.find_elements(By.CLASS_NAME, LANGUAGES_CSS_SELECTOR)

        for language in languages:
            if language.text == LANGUAGE:
                language.click()

        submit_button = driver.find_element(
            By.CSS_SELECTOR, SUBMIT_LANGUAGE_BUTTON_CSS_SELECTOR
        )
        submit_button.click()

    @staticmethod
    def create_course_model(
        course_name: str,
        course_description: str,
        course_type: CourseType,
        num_of_modules: int,
        num_of_topics: int,
        duration: str,
    ) -> Course:
        return Course(
            name=course_name,
            short_description=course_description,
            course_type=course_type.value,
            num_of_modules=num_of_modules,
            num_of_topics=num_of_topics,
            duration=duration,
        )
