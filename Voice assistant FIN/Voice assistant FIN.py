import vosk
import sys
import sounddevice as sd
import queue
import json
import pyautogui as pag
import keyboard as keyb
import time

pag.FAILSAFE = False
# подключаем языковую модель
model = vosk.Model('D:\\Voice assistant\\small_model')
samplerate = 16000
device = 1
q = queue.Queue()

# настройки прослушивания
def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# функция для прослушивания голоса
def listen():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16', channels=1, callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if not rec.AcceptWaveform(data):
                a = rec.PartialResult()
                a_dict = json.loads(a)
                partial_text = a_dict.get("partial")
                yield partial_text
            else:
                rec.Result()


examination = ''
for text in listen(): # каждое новое слово кладем в переменную text, если есть сопадения, ассистент отправляет тикет в нужню линию или вставляет макрос
    print(text)
    if text != examination:
        if text in ['стоп', 'стоп стоп']:
            break
        if text in ['водителя', 'водителем', 'водитель', 'руководителя']:  # Водители
            pag.leftClick(558, 189)
            time.sleep(0.2)
        if text in ['цены', 'низкие цены', 'цена', 'низкие', 'диски', 'низки', 'нитки']:  # Низкие цены
            pag.leftClick(667, 187)
            time.sleep(0.5)
        if text in ['первая линия', 'первая', 'первую']:  # ИП Фин
            pag.leftClick(772, 187)
            time.sleep(0.5)
        if text in ['компенсация', 'компенкин', 'компенсацию', 'капитан', 'компенсация', 'комплекс', 'автор', 'конденсация']:  # Вод. Автокомпенс
            pag.leftClick(477, 236)
            time.sleep(0.5)
        if text in ['наличие', 'наличные', 'кэш', 'кашу', 'наличка', 'нал', 'конечно', 'наличную', 'на лично']:  # Оплата наличными
            pag.leftClick(678, 236)
            time.sleep(0.5)
        if text in ['общая', 'общие', 'общие вопросы', 'общего', 'вопроса', 'общий', 'общем', 'общее', 'общую']:  # Общие вопросы
            pag.leftClick(510, 283)
            time.sleep(0.5)
        if text in ['третий', 'третьего', 'третий уровень', 'третьей', 'третья линия', 'третья', 'бонус','бонусы', 'бонуса']:  # Финансы У3
            pag.leftClick(695, 283)
            time.sleep(0.5)
        if text in ['карта про', 'карту', 'карта', 'про карта']:  # ИП Карта Про
            pag.leftClick(681, 332)
            time.sleep(0.5)
        if text in ['выплата', 'выплаты', 'вы потом', 'выработана', 'это выплата', 'это выплаты', 'выплату']:  # ИП Выплаты
            pag.leftClick(513, 379)
            time.sleep(0.5)
        if text in ['аккаунта', 'аккаунты', 'аки', 'это аккаунта', 'аккаунт', 'сортировка']:  # Аккаунты
            pag.leftClick(723, 380)
            time.sleep(0.5)
        if text in ['отмена', 'отмены', 'отмена', 'отмену', 'отмена заказа', 'отмена заказам']:  # Отмены\пропуски
            pag.leftClick(699, 426)
            time.sleep(0.5)
        if text in ['инфо', 'нимфа']:  # Финансы Инфо
            pag.leftClick(530, 427)
            time.sleep(0.5)
        if text in ['повтор', 'повторять', 'поиск', 'повторять ещё', 'повторять ещё минуту', 'поиска', 'поисками']:  # Повторять еще минуту
            pag.leftClick(646, 600)
            time.sleep(0.5)
        if text in ['сорта', 'магнус', 'макрон', 'макс']:  # Макрос СОРТ
            pag.leftClick(586, 538)
            keyb.write('Сорт')
            time.sleep(0.5)
        if text in ['типа', 'тип', 'типа плат', 'тип оплаты', 'типа платан']:  # Макрос СОРТ
            pag.leftClick(1468, 165)
            pag.typewrite(['enter'])
            time.sleep(0.5)

    examination = text
