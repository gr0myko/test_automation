from pages.menu_items import MenuItems
from framework.elements.button import Button
from selenium.webdriver.common.by import By


class MainMenu:
    @staticmethod
    def select_item(menu_item: MenuItems):
        menu_item_locator = f"//*[text()='{menu_item}']" \
                            f"//parent::a[@class='left_row']"
        menu_item_button = Button((By.XPATH, menu_item_locator))
        menu_item_button.wait_and_click()
