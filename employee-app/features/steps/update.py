from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import app

@given('I visit the employee management page for updating')
def step_visit_student_management(context):
    context.driver.get('http://127.0.0.1:5000/')

@when('I locate the top-most student')
def step_locate_top_most_student(context):
    # Locate the first student in the list
    context.top_student_row = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody tr:first-child'))
    )

@when('I update the employee\'s details with name "{name}", age "{age}", and department "{major}"')
def step_update_student_details(context, name, age, major):
    # Click the update link/button for the top-most student
    update_button = context.driver.find_element(By.CSS_SELECTOR, 'body > table:nth-child(5) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)')
    update_button.click()

    # Fill out the update form
    name_input = context.driver.find_element(By.NAME, 'name')
    age_input = context.driver.find_element(By.NAME, 'age')
    major_input = context.driver.find_element(By.NAME, 'major')

    name_input.clear()
    name_input.send_keys(name)
    age_input.clear()
    age_input.send_keys(age)
    major_input.clear()
    major_input.send_keys(major)

    # Use the new selector for the submit button
    submit_button = context.driver.find_element(By.CSS_SELECTOR, 'body > form:nth-child(2) > button:nth-child(13)')
    submit_button.click()


@then('I should see "{name}" in the list of employee after the update')
def step_see_updated_student(context, name):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, f"//td[text()='{name}']"))
    )
