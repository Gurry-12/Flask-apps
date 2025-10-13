from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the create employee page')
def step_go_to_create_page(context):
    # Access the initialized driver
    context.driver.get('http://localhost:5000/create')

@when('I fill out the form with name "{name}", age "{age}", and department "{major}"')
def step_fill_out_form(context, name, age, major):
    # Fill out the form fields
    name_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'name'))
    )
    name_input.clear()
    name_input.send_keys(name)

    age_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'age'))
    )
    age_input.clear()
    age_input.send_keys(age)

    major_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'major'))
    )
    major_input.clear()
    major_input.send_keys(major)

@when('I submit the form')
def step_submit_form(context):
    # Using the updated selector
    submit_button = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > form:nth-child(2) > button:nth-child(13)'))
    )
    print("Submit button found. Clicking it...")
    submit_button.click()
    print("Form submitted successfully.")



@then('I should see "{student_name}" in the list of employee')
def step_see_student_in_list(context, student_name):
    context.driver.get('http://localhost:5000/')
    page_source = context.driver.page_source
    assert student_name in page_source, f"{student_name} not found in the list of employee"
