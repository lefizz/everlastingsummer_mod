label semkayebivaet_d1:
    $ backdrop = "days"
    $ new_chapter(1, u"День 1")
    
    play music music_list["no_tresspassing"]
    scene bg int_bus
    with dissolve
    
    "Семённу в глаза ударил яркий солнечный свет."
    th "Да Сука! Просил же разбудить на Ленинской. {w}И какого хуя так светло?"
    "семён оглянулся и понял..."
    th "Ёпта! Это ж другой автобус! Какого хуя!?"
    "Сказать то что Семён {b}АХУЕЛ{/b} это ничего не сказать."
    th "Лаааааандо, и где тут вы... а вот он."
    "Он направился к открытой двери возле водительского места."
    "Сёма окинул взглядом место водителя и увидел пачку <Столичных> сигарет и зажигалку."
    "Он пошарился по своим карман и понял что его сигареты и зажигалка пропала. Остался только телефон."
    th "бля, если бы меня хотели ограбить - забрали бы ещё и телефон. Пиздец какой-то."
    "Он взял сигареты и зажигалку. {w}Сигарет осталось 5 штук."
    th "Не густо, но на первое время сойдёт."
    "Сёма вышел из автобуса"
    
    scene bg ext_bus
    play ambience ambience_ext_road_day
    with dissolve
    
    me "ЕЕЕБААААТЬ!!!"
    th "Пиздец, {b}ЧЕГО НАХУЙ?!{/b}"
    "Семён конкретно ахуел."
    th "Я ложился спать... весной. С хуя ли сейчас лето? {w}А я то думаю - бля а чё так жарко?"
    
    play sound sfx_alisa_lighter
    
    "Семён достал одну <Столичную> и прикурил."
    th "Я в ахуе."
    "С этой мыслью он скурил сигарету."
    th "А как я сюда попал? И что это за место?"
    
    show bg ext_camp_entrance_day
    with dissolve
    
    "Семён развернулся в другую сторону и увидел длинный забор с воротами."
    "Он увидел надпись <Совёнок> над воротами"
    th "Хмм... что-то знакомое. Друзья что то рассказывали, но конечно же я нихуя не помню."
    play sound sfx_alisa_lighter 
    "Он скурил ещё одну сигарету. У него осталось 3 штуки." 
    "Сёма посмотрел на ворота."
    th "Ну хули терять? Погнали нахуй!"
    "Он выкинул окурок в кусты и решительно направился к воротам."
    "Как только до ворот оставалось примерно метра 3... {w}От туда вышла девушка... красивая девушка."
    
    $ persistent.sprite_time = "day"
    
    show sl smile pioneer at center
    with dissolve
    
    slp "Привет, ты Семён?"
    th "бля, ты кто? Я первый раз тебя вижу! Хотя она вроде бы добрая."
    me "Ну да, я Семён, но можешь звать меня просто Сёма."
    slp "А я Славяна, но все зовут Славя."
    me "Приятно познакомиться, Славя."
    th "бля, Еб@#ь у неё глаза красивые, да и в целом она ничего такая."
    me "А где мы?"
    
    show sl surprise pioneer close at center
    with dissolve
    
    sl "В смысле?"
    me "В прямом. Где мы сейчас?"
    sl "На остановке, где же ещё?"  
    "Славя удивлённо посмотрела на Семёна"
    th "Она тупая, или реально не понимает что произошло?"
    me "Ладно, поставлю вопрос по другому. Мы находимся в <Совёнке>. Что такое совёнок?"
    sl "А ты разве не знаешь? Это пионерлагерь, <Совёнок> называется."
    th "Так, нихуя пока не понял."
    me "Ага, и чё мне тут делать?"
    
    show sl happy pioneer close at center
    with dissolve
    
    sl "Отдыхать и веселиться, что же ещё тут можно делать?"
    me "Ага, понял. {w}И куда мне надо идти?"
    sl "А, тебе к вожатому надо. Иди за ворота, прямо до площади, потом в сторону памятника и чуть левее, потом влево, и вправо, там только одна такая дорожка, а затем ещё раз вправо и самый крайний домик слева. там вожатый."
    me "С...Спасибо."
    "Сёма растерялся и нихуя не запомнил"
    "Спустя примерно полминуты славя задала вопрос."
    
    show sl surprise pioneer close at center
    with dissolve
    
    sl "А ты чего в куртке?"
    me "Ах да..."
    th "бля чё бы ей ответить? {w}А, во, придумал!"
    me "Да я когда ехал в автобусе спал несколько раз. Я куртку надевал что бы не продуло. Вот только проснулся, голова вообще не варит. По этому и спрашивал про лагерь."
    sl "Умно, воспользуюсь как нибудь твоим методом."
    
    show sl happy pioneer close at center
    with dissolve
    
    sl "Ладно, мне надо идти. И ты ступай к вожатому."
    me "Хорошо."
    
    hide sl happy pioneer
    
    th "Так бля, это что сейчас вообще было?"
    th "Какая то двечёнка спросила я ли тот самый Семён? Вопрос - откуда она знает как меня зовут?"
    th "Ответов с нихуя я не получу. {w}Так, она сказала что нужно идти к вожатому. Следовательно лагерь живой."
    th "Так. {w}СТАПЭ НАХУЙ. Она сказала что это пионер лагерь. Значит я где то между 1922 и 1991 годом. {w}Но если учесть тот факт что я вышел из 255 икаруса - я где-то в 70-ых - 80-ых годах."
    th "ЁПТА, у меня же есть теллефон!"
    
    play sound sfx_home_phone_take
    
    "Семён открыл календарь и ахуел в очередной раз!"
    me "Твою мать..."
    "Он увидел дату 4 июля 1983"
    th "ахуеть не встать. {w}Это чё, я почти на 40 лет назад откинулся? Еб@#ь!"
    "Семён стоял в шоке ещё пару минут, но потом решил пойти к вожатому"
    th "АХУЕТЬ. 39 лет..."
    
    scene bg ext_square_day
    with dissolve2
    
    "с этой мыслью он шёл до площади"
    th "ладно, нужно не подовать виду что что-то не так."
    
    show un normal pioneer far at center
    with dissolve 
    
    "Семён заметил красивую девушку на площади и решил подойти к ней."
    
    show un normal pioneer close at center
    with dissolve
    
    me "Привет, не подскажешь как к домику вожатого пройти?"
    
    show un surprise pioneer close at center
    with dissolve
    
    unp "П..Привет, а тут не далеко."
    "Пионерка рассказала как дойти до домика вожатого"
    me "Я кстати Семён"
    unp "А я Лена."
    "бля, они все тут такие красивые?"
    me "Приятно познакомиться. Ладно, я к вожатому. До скорых встреч."
    un "Пока."
    th "Боиться меня что ли? Или я ей понравился? Ладно, есть проблемы и поважнее."
    "Сёма подошёл к домику вожатого."
    
    scene bg ext_house_of_mt_day
    with dissolve
    play ambience ambience_camp_center_day
    
    th "А тут довольно мило."
    th "Ну, была не была!"
    "Семён постучал в дверь"
    voice "Открыто!"
    
    $ ss = Character (u'Сергей Сергеевич', color="#008080", what_color="E2C778")
    image ss normal = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'))
    image ss surprise = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'))
    image ss smile = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'))
    play sound sfx_close_door_clubs_nextroom
    scene bg int_house_of_mt_day
    with dissolve
    show ss normal at center
    
    "Семён зашёлл в домик и увидел вожатого. на вид лет 19-20"
    "Он увидел вожатого {w}Он читал какую то книгу."
    th "Хмм... что за книга?"
    me "Здравствуйте, вы вожатый?"
    ss "Здравстуй, да, я вожатый Сергей Сеогеевич. А ты семён?"
    me "Тот самый."
    th "хмм... норм мужик вроде. Может даже сиги получится стрельнуть."
    ss "У тебя есть форма пионера?"
    me "Не-а."
    ss "Ладно, у меня в шкафу есть форма какая-то."
    "Он порылся в шкафу и нашёл рубашку с шортами и туфлями."
    me "Извините, можно я в своей обуви похожу? у меня плоскостопие просто."
    ss "Да на здоровье."
    th "бля, форма есть, а где переодеться?"
    me "Сергей Сергеевич, а где мне переодеться?"
    ss "Да я вот как раз собирался сходить кое-куда, так что можешь тут переодеться. {w}И кстати, после обеда скажу куда тебя заселю.{w}"
    me "А на сколько заселите?"
    
    show ss surprise close at center
    
    "Вожатый удивлённо посмотрел на Сёму."
    ss "Всмысле <На сколько?>"
    th "Так нахуй, что то тут не чисто. Но раз уж начал - иди до конца."
    me "В прямом, сколько мне тут жить надо?"
    
    show ss smile close at center
    
    ss "А, ты про это? До конца смены."
    me "А конец смены когда?"
    ss "Ровно через 7 дней. Ни больше ни меньше."
    "Семён резко переменился в лице."
    th "Ахуеть! {w}Да что же это за день то такой?{w} Мало того что я попал в эту залупу хуй знает как, так теперь ещё 7 дней торчать здесь."
    th "{b}Ахуеть.{/b} {w}Просто ахуеть."
    
    show ss surprise closee at center
    
    ss "Ты в порядке? Может тебе к Виоле нужно?"
    me "К кому?"
    ss "Ну... к Виоле, в медпункте работает."
    me "Да не, просто не выспался."
    ss "Ну ладно. Ты смотри, чуть что - сразу в медпункт. {w}Давай, переодевайся и иди на обед."
    me "Понял."
    
    hide ss surprise
    
    "Вожатый вышел из домика."
    th "Так нахуй. Что это сейчас было?"
    th "Это пионерлагерь, я тут на 7 дней, я не ебу как я сюда попал. Ладно, попробую выяснить что да как."
    "Он увидел книгу которую вожатый оставил на столе."
    th "Джеймс Ален. <Как мыслит человек>. психология значит. {w}И как эта книга попала в савок? Она же явно написана не советским писателем."
    "Сёма переоделся и вышел на улицу"
    
    scene bg ext_house_of_mt_day
    play ambience ambience_camp_center_day
    with dissolve
    play sound sfx_alisa_lighter
    
    "Сёма достал сигарету и прикурил."
    th "бля, какого хуя тут происходит? Я собирался на ебучую работу. Хотел отработать и приехать домой."
    
    play sound sfx_dinner_jingle_speaker
    
    "Звук горна вывел семёна из раздумий."
    th "Так, вожатый сказал что нужно идти обедать. По идее этот Горн обозначает время приёма пищи."
    th "Стапэ, а где столовая? Хотя если подумать логически... пионеры пойдут на обед. {w}А значит, надо идти за ними."
    
    scene bg ext_square_day
    with dissolve
    
    "Сёма вышел на площадь и увидел как толпа пионеров направлялась куда-то"
    th "Так, если они куда-то целенаправленно идут - значит моё предположение становится верным."
    
    scene bg ext_dining_hall_away_day
    with dissolve
    play ambience ambience_camp_center_day
    with dissolve
    
    "И вправду, семён увидел как пионеры заходят в здание, которое похоже на столовую."
    
    scene bg ext_dining_hall_near_day
    
    show sl normal pioneer at center
    
    with dissolve
    
    show un normal pioneer at left
    
    with dissolve
    
    show us normal pioneer at right
    
    with dissolve
    
    "на крыльце стояли Славя, Лена и какая то мелкая пионерка."
    "Они о чём то оживлённо разговаривали до подхода Семёна."
    me "Всем привет."
    sl "Уже здоровались."
    un "Привет."
    usp "Привет, это же ты Семён?"
    me "Да, я. А тебя как звать?"
    
    show us smile pioneer at right
    
    with dissolve_fast
    
    usp "Я Ульянка."
    me "Приятно познакомиться."
    th "Ну и хули вы молчите?"
    me "Чего вы ещё не пошли есть?"
    sl "Да мы просто болтаем о своих делах."
    me "Понятно, пойдём есть?"
    us "Да, пойдёмте, а то сейчас прям тут кого-нибудь съем!"
    
    scene bg int_dining_hall_people_day
    show sl normal pioneer at center
    show un normal pioneer at left
    show us smile pioneer at right
    with dissolve
    play ambience ambience_dining_hall_full
    
    "Сёма направился за пионерками и взял поднос с едой."
    th "Хм, борщ, пюрешка с котлетой и чай. Надеюсь, будет вкусно."
    sl "С нами сядешь, или за другой столик пойдёшь?"
    me "Я наверное сяду с вами."
    th "может получится попиздеть."
    "Семён, Славя, Лена и Ульяна сели за один стол."
    me "А как часто вы сюда приезжаете?"
    sl "Я каждое лето сюда приезжаю. Я помощница у вожатого. {w}Надеюсь что стану вожатой в будущем."
    un "А я 3 раз уже приезжаю сюда."
    us "А я в первый раз тут. Так что есть что поисследовать, ха."
    me "Я тоже первый раз тут."
    "Сёма съел борщ и пюре."
    th "бля, наелся от души, от чая что то сверхъестественное ждать не стоит."
    "Сёма развалился на стуле и принялся пить чай."
    me "Лена, чего ты грустишь?"
    
    show un surprise pioneer at left
    
    un "С чего ты взял?"
    me "У тебя такое выражение лица, что может показаться что ты грустишь."
    un "Просто настроения нету."
    me "А чего настроения нету?"
    un "Не знаю. {w}Просто нету настроения."
    th "бля, жиза. Я в таких случаях кентам пишу, либо музыку врубаю."
    me "А ты н..."
    th "Сука!"
    un "Что?"
    me "Не пробовала говорить с кем-то когда у тебя настроения нету?"
    un "Мне не хочется."
    me "Ну, как знаешь. Мне помогает."
    un "Ага."
    th "Что за хуйня с ней твориться? Почему просто не побазарить с кем нибудь?"
    th "Ладно, хуй с ней. Допью чай и пойду к вожатому. Интересно, а где я буду жить?"
    "Сёма допил чай."
    me "Ладно, я пойду. Нужно узнать куда меня вожатый заселит. До встречи."
    all "До встречи!"
    
    scene bg ext_dining_hall_near_day
    
    with dissolve
    
    show ss normal close at center
    
    with dissolve
    
    ss "О, Семён, а я тебя ищу. {w}В общем, домиков свободных нету."
    th "бля, почему я нихуя не удивлён? {w}И где мне жить? На скамейке на площади?"
    me "И где мне жить тогда?"
    ss "Ну смотри, вариантов у тебя не много, первый - жить у меня в домике."
    me "СОГЛАСЕН!"
    
    show ss smile close at center
    
    ss "Хах, а ты второй не выслушал же. может есть кое-что для тебя."
    me "Ну давайте, удивляйте."
    ss "На одной из скамеек лагеря. хахаха!"
    th "Прочитан нахуй!"
    ss "Ладно, держи ключи от моего домика. Твоя кровать слева от входа."
    me "Благодарю вас, Сергей Сергеевич."
    me "Ладно, я пойду посплю немного."
    ss "Да, конечно. И да, шкафчиком тоже можешь пользоваться. В общем - будь как у себя дома. {w}Только никого туда не приводи, хах!"
    me "Да я и не собирался в принципе..."
    ss "Мало ли. Ладно, ступай."
    
    scene bg ext_square_day
    
    with dissolve
    
    th "Так, По закону Архимеда после сытного обеда, чтобы жиром не заплыть, нужно срочно покурить."
    
    scene ext_house_of_mt_day
    
    with dissolve2
    
    "Сёма подашёл к домику вожатого. Он лёг на шезлонг возле домика и прикурил сигарету."
    
    play sound sfx_alisa_lighter
    
    "У него осталась 1 штука."
    th "Так, если сделать вид что всё происходит как обычно, то всё в порядке {w}{b}НО ВСЁ НИХУЯ НЕ НОРМАЛЬНО!{/b}"
    th "Каким хуем я оказался тут? что меня сюда принесло или привезло? Хотя ответ очевиден {w}- автобус."
    th "Ладно, пойду спать. чем быстрее скипну эти дни - тем лучше."
    "Семён докурил сигарету и выкинул окурок в кусты."
    
    scene int_house_of_mt_day
    
    with dissolve
    
    "Сёма зашёл в домик и лёг спать."
    
    show blink
    
    voice "Ёбаный замкнутый круг. Это временная петля? Если да - то её не разорвать?"
    voice "Ещё этот новенький странный... ладно, позже с ним разберусь."
    
    show unblink
    
    with dissolve
    
    scene int_house_of_mt_sunset
    
    th "Эээээээ... Сука... какого хуя так быстро? И что это было нахуй?"
    "Сёма взгляну за окно и понял то что уже вечер."
    th "Ладно, уже вечереет, значит поспал больше двух часов. Когда ложился спать было примерно 12 часов, может час."
    th "И что это за параша? Хуйня а не сон."
    
    scene bg ext_house_of_mt_sunset
    
    with dissolve
    
    play ambience ambience_camp_center_evening
    
    "Сёма вышел на улицу и хотел закурить, но вспомнил что у него только одна сигарета."
    th "Скурю когда узнаю где достать новые."
    
    play sound sfx_dinner_jingle_speaker
    
    th "Опа, а вот и хавчик."
    "Сёма пошёл в столовую"
    
    scene bg ext_square_sunset
    with dissolve_fast
    
    scene bg ext_dining_hall_away_sunset
    with dissolve_fast
    
    scene bg ext_dining_hall_near_sunset
    with dissolve_fast
    
    scene int_dining_hall_sunset
    with dissolve_fast
    
    "Сёма зашёл в столовую один из первых и взял поднос с едой."
    "На подносе были макароны, овощи и яблочный сок."
    th "Лёгкая пища вечером это самое то для хорошего сна. Не зря же я работаю в кафе. {w}СТАПЭ, А работаю ли я до сих пор?"
    th "Ладно, пока я тут - бессмысленно гадать. Выберусь - узнаю"
    "Семён съел всё и принлся пить сок."
    th "Ох, сейчас бы пивка..."
    th "Ладно, пойду прогуляюсь, осмотрю лагерь до конца."
    "Сёма вышел из столовой и пошёл прогуливаться."
    
    $ persistent.sprite_time = "sunset"
    
    scene bg ext_square_sunset
    with dissolve2
    show un normal pioneer far at center
    play ambience ambience_camp_center_evening
    
    "Сёма увидел сидящую на скамейке Лену. Она что-читала."
    th "Подойти и поговорить с ней может?"
    "Семён решил подойти к ней."
    
    show un normal pioneer close at center
    
    me "Ещё раз привет."
    un "Привет."
    me "Что читаешь?"
    un "Унесённые ветром. Маргарет Митчелл."
    me "Романы любишь?"
    un "Ага."
    me "Можно присесть?"
    un "Да."
    th "О чём бы с ней поговорить?"
    me "А какая твоя любимая книга? У меня вот... Книга Джеймса Алена <Как мыслит человек>. Психологию люблю."
    un "А мне нравится <Мастер и Маргарита>. Классика всё-таки."
    th "И чё дальше?"
    me "Лен."
    un "Что?"
    me "Ты красивая."
    
    play music music_list["lets_be_friends"]
    show un surprise pioneer close at center
    with dissolve
    
    th "Ёпт. Ну и нахуя я это сказал?"
    un "С..Спасибо..."
    me "Я серьёзно."
    
    show un smile pioneer close at center
    with dissolve
    
    un "Это мило."
    me "Это факт, ты красивая, и я тебе об этом сказал."
    un "Ладно, я в домик пойду. До встречи."
    me "Пока, до встречи."
    
    stop music
    hide un smile pioneer close at cecnter
    
    th "бля, она реально красивая. Может попробовать замутить с ней? Всё равно я тут на 7 дней. {w}А что после этих ссеми днней будет?"
    th "Ладно, прогуляюсь ещё немного..."
    
    scene bg ext_houses_sunset
    play ambience ambience_camp_center_night 
    
    th "Ахуенный закат..."
    th "Сейчас бы закурить."
    "Семён прогуливался между домиков как вдруг..."
    "УДАР!"
    play music music_list["pile"]
    th "Какого..."
    
    show dv guilty pioneer2 close at center
    
    "Сёма обернулся и увидел пионерку."
    me "Ты какого хуя делаешь?"
    dvp "Прости, я просто..."
    me "Что просто? Просто я мог пиздануться и сломать что нибудь!"
    me "Как же у вас, девушек, всё просто!"
    
    stop music
    play music music_list["i_dont_blame_you"]
    show dv cry pioneer2 close at center
    with dissolve_fast
    
    dvp "Прости, я не хотела."
    me "Тогда объясни мне зачем ты меня толкнула в спину?"
    dvp "Я не знаю..."
    me "Ладно, я человек не злопамятный, вытри слёзы и успокойся."
    th "Я тебе это припомню ещё, Сука. Просто так ты не отделаешься у меня, падла."
    dvp "Я больше не буду так."
    me "Верю. Успокойся уже"
    
    show dv guilty pioneer2 close at center
    
    dvp "Просто Ульяна видела тебя с Леной на скамейке на площади, потом она пришла в домик и мне рассказала."
    th "Ёпта, я тебя вообще первый раз вижу, какое нахуй?"
    me "Да ладно тебе, мы с ней о книгах разговаривали."
    dvp "Понятно."
    me "Ладно, успокаивайся, мне надо идти в домик."
    dvp "Хорошо. {w}Тебя же Семён зовут?"
    me "Да."
    dvp "А я Алиса."
    me "Понял. Пока, Алиса."
    
    stop music
    hide dv guilty pioneer2 close at cecnter
    
    "Сёма пошёл к домику вожатого."
    th "Это какой то пиздец. Что блять происходит в последние 2 дня?"
    th "Я блять хотел просто поехать на ссаную работу! А оказаллся в каком-то милом... {w}{b}АДУ НАХУЙ!{/b}"
    
    scene bg ext_house_of_mt_night_without_light
    with dissolve2
    play ambience ambience_camp_entrance_night
    
    "Сёма лёг на шезлонг и понял что он хочет курить."
    th "бля, сейчас бы пыхнуть... но надо потерпеть. У меня чуйка нна сиги, я чувствую что они рядом."
    th "Ладно, найду - заебись. Не найду - будет хуёво."
    
    play sound sfx_alisa_lighter
    
    "Сёма подкурил последнюю сигарету."
    th "Как же ахуеееенно."
    "Сёма скурил сигарету и выкинул окурок в кусты."
    "спустя пару минут бездумного нахождения на шезлонге пришёл вожатый."
    
    $ persistent.sprite_time = "night"
    
    show ss normal at center
    
    ss "А ты чего тут лежишь? У тебя же есть ключи от домика."
    me "Я устал. вообще понятия не имею почему, но я очень устал."
    ss "Понимаю тебя. Ладно, пошли в домик."
    me "Пойдёмте."
    
    scene bg int_house_of_mt_night2
    with dissolve
    show ss normal
    
    "Сёма разделся и лёг на свою кровать."
    ss "Как первый день?"
    me "Честно?"
    ss "Ну я не просто так спросил."
    me "Вообще жесть какая-то."
    ss "Почему?"
    me "Простите что не по теме. Вы курите?"
    ss "Допустим курю. Тебе то что?"
    th "Опа, вот это уже интереснее."
    me "Просто я сегодня последнюю сигарету скурил, а больше у меня нету."
    ss "Фух бля, нормальный пацан попался."
    th "Джекпот ёбана!"
    ss "Просто понимаешь, эти два мудака типа зожники, а с пионерками курить не круто. Я же как приер для пионеров."
    me "Это верно."
    ss "Покурим?"
    me "Можно."
    
    scene bg ext_house_of_mt_night
    with dissolve
    show ss smile close at center
    play ambience ambience_camp_center_night 
    play ambience ambience_camp_entrance_night
    
    ss "Только один ньюанс, у меня не сигареты, а папиросы. Беломорканал, не откажешься?"
    me "Не поверите, всегда хотел попробовать. Я только вот столичные выкурил."
    ss "Держи."
    "Сергей Сергеевич протянул Семёну папиросу."
    
    play sound sfx_alisa_lighter
    
    play music music_list["smooth_machine"]
    
    "Сёма подкурилл её."
    me "Нормально в голову дают."
    ss "А то. Крепкие Сука."
    me "А как давно вы тут работаете?"
    ss "Слушай, давай на едине на ты. просто меня напрягает когда я к человеку, которого считаю равным себе, обращаюсь на ты, а он ко мне на вы."
    me "Понял."
    ss "Работаю... года три, может четыре. Я раньше сюда ездил, когда было 14. Потом моя вожатая уволилась. Была ещё одна, Ольга Дмитриевна зовут, но она плохо справлялась со своими задачами. Из-за этого её уволили."
    "До меня дошла эта новость и я решил попробовать себя в роли вожатого."
    me "Круто, вам нравится тут работать?"
    ss "Ну я же сказал, давай на ты."
    me "Прости. Тебе нравится тут работать?"
    ss "Да, пионерки тут иногда интересные бывают."
    "Сергей Сергеевич затянулся."
    ss "А у тебя как с пионерками?"
    "Сёма с грустным лицом затянулся."
    me "Ну смотри, одна ебанутая толкнула меня в спину так, что я чуть не сломал себе что-нибудь, Алиса по-моему. Другая замкнутая в себе что-ли... это Лена. А третья... А что третья? Обычная пионерка. Красивая."
    ss "Ты про славю что-ли?"
    me "Ага. Она прикольная. И глаза у неё красивые."
    ss "Это да... в её глазах утонуть можно, хах."
    "Они докурили папиросы."
    me "Слушай, ты психологией увлекаешься?"
    ss "да, а как ты узнал?"
    me "Да вот, книгу утром видел."
    ss "А, как думает человек?"
    me "Именно."
    ss "А, я её только вчера в библиотеке взял."
    me "Понятно. Пойдём спать?"
    ss "Пошли."
    scene bg int_house_of_mt_night2
    with dissolve
    
    th "Еб@#ь он классный чувак. Я уж думал мудак какой то. Шутить он явно не уммеет. Хотя... кто его знает?"
    
    show blink
    "Семён закрыл глаза и погрузился в сон."
    
    jump ssandsemenn_d_2