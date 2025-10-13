from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I visit the employee management page')
def step_visit_management_page(context):
    context.driver.get('http://127.0.0.1:5000/')

@when('I locate the delete button for the top-most employee')
def step_locate_delete_button(context):
    context.delete_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table:nth-child(5) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > form:nth-child(2) > button:nth-child(1)'))
    )

@when('I click the delete button')
def step_click_delete_button(context):
    context.delete_button.click()

@then('I should not see the top-most employee in the list of employee')
def step_not_see_top_most_student(context):
    student_name = "John Smith"  # Replace with the actual name of the top-most student if needed
    WebDriverWait(context.driver, 10).until_not(
        EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{student_name}')]"))
    )
