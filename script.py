from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def test_registration_form(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Влад")
        
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Кардаев")
        
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("test@example.com")
        

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return "Congratulations! You have successfully registered!" in welcome_text
        
    except NoSuchElementException as e:
        print(f"Элемент не найден: {e}")
        return False
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    print("Тест для registration1.html:", 
          "УСПЕХ" if test_registration_form("http://suninjuly.github.io/registration1.html") else "ПРОВАЛ")
    
    print("Тест для registration2.html:", 
          "УСПЕХ" if test_registration_form("http://suninjuly.github.io/registration2.html") else "ПРОВАЛ (как и ожидалось)")