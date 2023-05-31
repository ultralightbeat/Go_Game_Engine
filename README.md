# Go_Game_Engine
Go_Game_Engine - это движок для Sabaki GUI(https://github.com/SabakiHQ/Sabaki) созданный на языке Python для игры в древнюю китайскую игру Го.
# Правила игры
1)	Игра начинается с пустой доски. Затем два партнера по очереди ставят на нее камни своего цвета. У одного они белые, у другого - черные.
2)	Побеждает тот, кто окружит больше территории.
3)	Камень или группа камней противника, которые вы окружили своими камнями, снимается с доски.
4)	Во время игры на доске появляются пункты куда нельзя ходить: запрещенные пункты.
5)	Запрещается повторять позицию: правило ко
# Скриншоты графического интерфейса
Благодаря графическому интерфейсу Sabaki я могу продемонстрировать какую логику смог прописать для своего движка.
По ссылке вы можете ознакомиться с геймплеем игры(https://rutube.ru/video/6b2540eac14b974a4372b476dd5cd350/)

Представляю вам некоторые фотографии интерфейса и способ установки движка

![Скриншот установки](https://github.com/ultralightbeat/Go_Game_Engine/blob/master/images/engine_dowload_1.png)

Далее в меню нужно указать путь к испольнуемому файлу и необходимые аргументы как показано на скриншоте(путь нужно указывать на место на диске где у вас распакован скачанный архив) 

![Скриншот определения пути и аргументов](https://github.com/ultralightbeat/Go_Game_Engine/blob/master/images/engine_dowload.png)


После добавления движка его следует выбрать в меню терминала и определить какими камнями компьютер будет играть
После добавления движка в терминале должна отобразиться версия, имя движка и версия протокола. Через главное меню сверху следует нажать File > New. Далее перед пользователем будет представлено меню настройки доски, следует указать размеры доски которые используются в настоящей игре Го.
Чтобы начать играть против движка, на боковой панели терминала следует выбрать ранее указанный движок и выбрать каким цветом камней он будет играть. В игре Го первым ходит игрок с черными камнями, поэтому если вы выбрали движок за черные камни следует навестись на него курсором и отдать команду сгенерировать первый ход – Generate Move. 
![Скриншот выбора какими камнями будет играть движок](https://github.com/ultralightbeat/Go_Game_Engine/blob/master/images/engine_dowload.png)

Дальнейшие ходы осуществляются кликом курсора по доске, если ход невозможен программа предупредит вас об этом.
Ниже представлена скришот игрового поля в процессе игры

![Скриншот игрового поля](https://github.com/ultralightbeat/Go_Game_Engine/blob/master/images/ban.png)

Число набранных очков отображается в нижней части под игровой доской. Для подробного отображения захваченной территории игроком следует перейти в меню доски в нижнем правом углу и выбрать Score.

![Скриншот таблицы очков](https://github.com/ultralightbeat/Go_Game_Engine/blob/master/images/score.png)

# Особенности движка
В отличие от рандомной генерации ходов движок анализирует текущую ситуацию на доске и методом исключения выбирает лучший ход в данной ситуации. Это делает игру интереснее и сложнее по сравнению с рандомной генерации. Реализованный движок составляет конкуренцию игроку уровня новичка - любителя. Также можно добавить уже созданные движки и понаблюдать за схваткой двух алгоритмов. 






