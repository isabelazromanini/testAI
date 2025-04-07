from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice.automationtesting.in/my-account/"
        
        # Localizadores dos elementos
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.NAME, "login")
    
    def open(self):
        """Abre a página de login."""
        self.driver.get(self.url)

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10) 
        
        """Realiza o login preenchendo os campos e clicando no botão."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        """Verifica se o login foi bem-sucedido."""
        return "dashboard" in self.driver.current_url.lower()
    
    def error_email_invalid(self):
        """Verifica se a mensagem de erro para e-mail inválido aparece na tela."""
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_message_locator)
            )
            return "A user could not be found with this email address." in error_message.text
        except:
            return False  # Retorna False caso a mensagem de erro não apareça