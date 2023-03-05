import sys
import time
import pyautogui as df


text_write = None
recording_button = None
queue = []
# time_limit_array=[]Sound recorderSound recorder

sys.stdin = open("work\English_study\question\Description_question.txt")

while True:
    tmp = sys.stdin.readline().strip('\n')
    if tmp == 'end':
        break
    elif tmp =='':
        continue
    else:
        queue.append(tmp)
# print(queue)
while queue:
    question = queue.pop()
    print(question)
    # time_limit = time_limit_array.pop()
    if recording_button is None:
        df.press('winleft')
        df.write('Sound recorder')
        df.press('enter')
        time.sleep(1)
        df.hotkey('winleft','left')
        time.sleep(1)
        df.press('enter')
        time.sleep(1)
        recording_button = df.locateOnScreen("work\English_study\img\\recording_button.png",confidence =0.9)
        stop_button = df.locateOnScreen("work\English_study\img\stop_button.png",confidence =0.9)
        if recording_button is None:
            break
    if text_write is None:
        df.press('winleft')
        df.write('Chrome')
        df.press('enter')
        time.sleep(1)
        df.write('papago.naver.com')
        time.sleep(0.1)
        df.press('enter')
        time.sleep(1)
        df.hotkey('winleft','right')
        time.sleep(1)
        df.press('enter')
        time.sleep(1)
        text_write = df.locateOnScreen("work\English_study\img\papago.png",confidence =0.9)
        listen = df.locateOnScreen("work\English_study\img\listen.png",confidence =0.9)
        text_write = list(text_write)
        text_write[0] = text_write[0]
        text_write[1] = text_write[1]+150
        if text_write is None:
            break
    time.sleep(1)
    df.click(recording_button)
    df.click(text_write)
    df.hotkey('ctrl','a')
    df.press('delete')
    df.write(question)
    time.sleep(1)
    df.moveTo(listen)
    time.sleep(1)
    df.click(listen)
    time.sleep(60)
    df.click(stop_button)