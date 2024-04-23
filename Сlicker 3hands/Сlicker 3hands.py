import pyautogui as pag
import keyboard as keyb
import time

pag.FAILSAFE = False

while True:
    if keyb.is_pressed('1'):  # клик в Фин
        pag.leftClick(570, 186)
        time.sleep(0.5)

    if keyb.is_pressed('2'):  # клик в Акк
        pag.leftClick(772, 329)
        time.sleep(0.5)

    if keyb.is_pressed('3'):  # клик логистика
        pag.leftClick(675, 234)
        time.sleep(0.5)

    if keyb.is_pressed('4'):  # клик в центр
        pag.leftClick(641, 596)
        time.sleep(0.5)

    if keyb.is_pressed('e'):  # шаблон Сорт
        pag.leftClick(607, 484)
        keyb.write('Сорт')
        time.sleep(0.5)

    if keyb.is_pressed('r'):  # шаблон Сорт с плашкой
        pag.leftClick(643, 563)
        keyb.write('Сорт')
        time.sleep(0.5)

    if keyb.is_pressed('6'):  # шаблон Лин
        pag.leftClick(607, 484)
        keyb.write('Лин')
        time.sleep(0.5)

    if keyb.is_pressed('7'):  # шаблон Лин с плашкой
        pag.leftClick(643, 563)
        keyb.write('Лин')
        time.sleep(0.5)

    if keyb.is_pressed('8'):  # шаблон Ург
        pag.typewrite(['backspace'])
        keyb.write('Ург')
        time.sleep(0.5)

    if keyb.is_pressed('9'):  # шаблон Уточ
        pag.typewrite(['backspace'])
        keyb.write('Уточ')
        time.sleep(0.5)

    if keyb.is_pressed('esc'):  # конец
        break
