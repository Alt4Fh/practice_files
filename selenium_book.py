

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    text = message.text

    driver.quit()
    return


if __name__ == "__main__":
    app.run()
