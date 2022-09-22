import datetime
import time

now = datetime.datetime.now()

print(now.time())


if now.weekday() == 0:
    print("Панядзелак ")
elif now.weekday() == 1:
    print("Аўторак ")
elif now.weekday() == 2:
    print("Серада ")
elif now.weekday() == 3:
    print("Чацвер ")
elif now.weekday() == 4:
    print("Пятніца ")
elif now.weekday() == 5:
    print("Субота ")
elif now.weekday() == 6:
    print("Нядзеля ")

print("""

1.	08:30 – 09:15	англ. мова (Англ. мова (м-а)))   313
                    фізіка (фізіка(ф-м))

2.	09:30 – 10:15	хімія                            213

3.	10:30 – 11:15	англ. мова (Англ.мова(ф-м))      226
                    фізіка (фізіка(м-а))             313

4.	11:30 – 12:15	бел. літ                         332

5.	12:30 – 13:15	чарчэнне                         235

6.	13:30 – 14:15	матэматыка                       325""")