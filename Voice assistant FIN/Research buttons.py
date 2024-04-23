import pyautogui as pag
pag.FAILSAFE = False


def buttons_coordinates():
    global buttons_coord
    region = (385, 155, 915, 510) #  область для поиска кнопок на мониторе

    # где хранятся кнопки 
    accounts = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\accounts.png'
    autocompensation = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\autocompensation.png'
    fin_Y3 = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\fin_Y3.png'
    ip_fin = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\ip fin.png'
    ip_pay = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\ip_pay.png'
    card_pro = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\card_pro.png'
    cash = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\cash.png'
    low_prices = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\low prices.png'
    all_questions = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\all questions.png'
    cancel = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\cancel.png'
    drivers = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\drivers.png'
    info = 'D:\\Voice assistant\\SORT FIN\\buttons_fin\\info.png'

    # pyautogui сканирует экран, собирает координаты кнопок
    c_accounts = list(pag.locateCenterOnScreen(
        accounts, confidence=0.9, region=region))
    c_autocompensation = list(pag.locateCenterOnScreen(
        autocompensation, confidence=0.9, region=region))
    c_fin_Y3 = list(pag.locateCenterOnScreen(
        fin_Y3, confidence=0.9, region=region))
    c_ip_fin = list(pag.locateCenterOnScreen(
        ip_fin, confidence=0.9, region=region))
    c_ip_pay = list(pag.locateCenterOnScreen(
        ip_pay, confidence=0.9, region=region))
    c_card_pro = list(pag.locateCenterOnScreen(
        card_pro, confidence=0.9, region=region))
    c_cash = list(pag.locateCenterOnScreen(
        cash, confidence=0.9, region=region))
    c_low_prices = list(pag.locateCenterOnScreen(
        low_prices, confidence=0.9, region=region))
    c_all_questions = list(pag.locateCenterOnScreen(
        all_questions, confidence=0.9, region=region))
    c_cancel = list(pag.locateCenterOnScreen(
        cancel, confidence=0.9, region=region))
    c_drivers = list(pag.locateCenterOnScreen(
        drivers, confidence=0.9, region=region))
    c_info = list(pag.locateCenterOnScreen(
        info, confidence=0.9, region=region))

    # выводит координаты в виде словаря
    buttons_coord = {'accounts': c_accounts, 'autocompensation': c_autocompensation, 'fin_Y3': c_fin_Y3,
                     'ip_fin': c_ip_fin, 'ip_pay': c_ip_pay, 'card_pro': c_card_pro, 'cash': c_cash,
                     'low_prices': c_low_prices, 'all_questions': c_all_questions, 'cancel': c_cancel,
                     'drivers': c_drivers, 'info': c_info}
    return buttons_coord


print(buttons_coordinates())
