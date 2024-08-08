import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import (
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
from enums import CourseType
from models import Course
from web_driver import driver


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

    @staticmethod
    def get_button_of_course_type(
        course: WebElement, course_type: CourseType
    ) -> WebElement | None:
        course_type_buttons = course.find_elements(By.TAG_NAME, "a")
        for button in course_type_buttons:
            if button.text == course_type.value:
                return button

    @staticmethod
    def update_course(course_name: str) -> WebElement:
        courses = driver.find_elements(By.CLASS_NAME, COURSES_CSS_SELECTOR)

        for course in courses:
            if course.find_element(By.TAG_NAME, "h3").text == course_name:
                return course

    def parse_course_with_types(self, course: WebElement) -> list[Course]:
        courses = []

        course_name = course.find_element(By.TAG_NAME, "h3").text
        course_description = course.find_element(By.CLASS_NAME, "mb-32").text

        for course_type in [CourseType.FLEX, CourseType.FULL_TIME]:
            button = self.get_button_of_course_type(
                course=course, course_type=course_type
            )

            if button is None:
                continue

            href = button.get_attribute("href")
            driver.get(href)

            num_of_modules = int(
                driver.find_element(
                    By.CLASS_NAME, MODULES_NUMBER_CSS_SELECTOR
                ).text.split()[0]
            )
            num_of_topics = int(
                driver.find_element(
                    By.CLASS_NAME, TOPICS_NUMBER_CSS_SELECTOR
                ).text.split()[0]
            )
            duration = driver.find_element(
                By.CLASS_NAME, COURSE_DURATION_CSS_SELECTOR
            ).text

            courses.append(
                self.create_course_model(
                    course_name=course_name,
                    course_description=course_description,
                    course_type=course_type,
                    num_of_modules=num_of_modules,
                    num_of_topics=num_of_topics,
                    duration=duration,
                )
            )

            driver.back()
            course = self.update_course(course_name=course_name)

        return courses

    def get_all_courses(self) -> list[Course]:
        driver.get(URL_TO_SCRAPE)
        self.change_language()

        all_courses = []
        courses = driver.find_elements(By.CLASS_NAME, COURSES_CSS_SELECTOR)

        for course_index in range(len(courses) - 1):
            course = self.parse_course_with_types(courses[course_index])
            all_courses.extend(course)
            courses = driver.find_elements(By.CLASS_NAME, COURSES_CSS_SELECTOR)

        return all_courses
