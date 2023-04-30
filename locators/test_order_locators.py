from selenium.webdriver.common.by import By


class OrderLocators:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    LOGO_YANDEX = [By.CSS_SELECTOR, "[alt = 'Yandex']"]

    LOCATOR_TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка заказа(верхняя)

    LOCATOR_DOWN_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM") # Кнопка заказа(нижняя)

    LOCATOR_NAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u div."
                                          "Input_InputContainer__3NykH:nth-child(1) > input.Input_Input__1iN_Z."
                                          "Input_Responsible__1jDKN")  # Поле для ввода имени
    LOCATOR_LASTNAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u"
                                              " div.Input_InputContainer__3NykH:nth-child(2) > "
                                              "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Поле для ввода
    # фамилии
    LOCATOR_ADDRESS_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                             "div.Input_InputContainer__3NykH:nth-child(3) > "
                                             "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Поле для ввода
    # адреса
    LOCATOR_METRO_FORM_BUTTON = (By.CLASS_NAME, "select-search__input")  # Кнопка указания метро
    LOCATOR_METRO_SQUARE_BUTTON = (
        By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button")  # Выбор метро
    LOCATOR_PHONE_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                           "div.Input_InputContainer__3NykH:nth-child(5) > "
                                           "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Кнопка для ввода
    # номера телефона
    LOCATOR_CONTINUE_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")  # Кнопка 'Далее'

    # продолжить(форма заказа)
    LOCATOR_DATE_BRING_SCOOTER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")  # Поле для ввода даты
    LOCATOR_DATE_BRING_SCOOTER_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                          "div.Order_Form__17u6u div.Order_MixedDatePicker__3qiay "
                                                          "div.react-datepicker__tab-loop div.react-datepicker-popper "
                                                          "div.react-datepicker "
                                                          "div.react-datepicker__month-container:nth-child(4) "
                                                          "div.react-datepicker__month "
                                                          "div.react-datepicker__week:nth-child(3) > "
                                                          "div.react-datepicker__day.react-datepicker__day--018.react"
                                                          "-datepicker__day--weekend:nth-child(7)")
    # Подтверждение# даты в datepicker
    LOCATOR_RENTAL_PERIOD_BUTTON = (
        By.XPATH, "//div[@class='Dropdown-control']")  # Кнопка выбора периода времени катания
    LOCATOR_RENTAL_PERIOD_CHOICE = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)")  # Выбираем период времени
    LOCATOR_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")  # Выбираем цвет самоката
    LOCATOR_COMMENTARY = (By.XPATH, "//div[@class='Order_Form__17u6u']//div["
                                    "@class='Input_InputContainer__3NykH']//input[@type='text']")
    # Поле для ввода комментария
    LOCATOR_ORDER_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__15LM- div.Order_Content__bmtHS "
                                             "div.Order_Buttons__1xGrp > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")
    # Кнопка заказать в форме "заказа"
    LOCATOR_CONFIRM_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                               "div.Order_Buttons__1xGrp > "
                                               "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")
    # Кнопка подтверждения заказа
    LOCATOR_CHECK_STATUS = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                             "div.Order_NextButton__1_rCA > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM")
    # Кнопка проверить статус
    LOCATOR_YANDEX_BUTTON = (By.XPATH, "//a [@href = '//yandex.ru']")


    LOCATOR_SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Кнопка "Самокаты"
    LOCATOR_SHOW_STATUS = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                            "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                            "button.Button_Button__ra12g.Button_Middle__1CSJM")
    LOCATOR_UP_BOTTOM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                          "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                          "button.Button_Button__ra12g.Button_Middle__1CSJM")

    LOCATOR_DOWN_BUTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")

    LOCATOR_TEXT_ARENDA = (By.CLASS_NAME, "Order_Header__BZXOb")

