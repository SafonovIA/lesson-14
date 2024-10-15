from atf.ui import *


class AuthPage(Region):
    """Страница авторизации онлайн"""
    login = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"] [inputmode="text"]', 'Пароль')

    def auth(self):
        self.browser.open(self.config.get('SITE'))
        self.login.type_in(self.config.get('LOGIN') + Keys.ENTER)
        self.password.type_in(self.config.get('PASSWORD') + Keys.ENTER)
        self.check_page_load_wasaby()

