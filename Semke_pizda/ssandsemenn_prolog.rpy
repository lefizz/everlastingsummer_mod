init:

    $ mods["ssandsemenn_prolog"]=u"Сёмке пизда"
    
    $ sa = Character (u'Саня', color="#778899", what_color="E2C777")
    
    $ ss = Character (u'Сергей Сергеевич', color="#008080", what_color="E2C778")
    
    image ss normal = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_normal.png'))
    
    image ss surprise = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_surprise.png'))
    
    image ss smile = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png', (0, 0), 'mods/Semke_pizda/image/sprites/semenn_smile.png'))
        
label ssandsemenn_prolog:
    play music music_list["a_promise_from_distant_days_v2"] 
    th "Охх ебааа... скоро на работу"
    "Семён только проснулся от будильника и открыл глаза."
    scene bg semen_room
    with dissolve2
    th "Сук, уже 6 часов вечера. Автобус в 7:15... ладно, надо собираться."
    "Семён работал в кафе неподалёку от центра города. Платили ему достаточно. На базовые потребности хватало с головой."
    "Семён умылся, сделал кофе и сел за комп."
    play sound sfx_keyboard_mouse_computer_noise
    message "В КС пойдём сегодня?"
    me "Бля, сори. Мне на работу нужно."
    message "Ок, труженник блин..."
    me "Я напишу как освобожусь. Я буквально на 4 часа и домой."
    message "Хорошо, жду."
    "Семён жил на окраине города в однушке. Но ему многое и не требовалось. Кровать, комп, интернет и еда - всё что ему нужно."
    "Время 7 часов."
    th "Так, нужно выходить."
    stop sound
    "Сёма накинул куртку и кеды. Он взял с собой полную пачку сигарет и направился на остановку."
    play ambience ambience_cold_wind_loop
    with dissolve
    scene bg bus_stop
    with dissolve2
    "Хоть и на дворе был апрель - на улице были большие сугробы, и из-за снега у Семёна быстро промокли ноги."
    th "Бля, ебучий снег."
    play sound sfx_alisa_lighter 
    "Семён пришёл на остановку и закурил."
    "Живёт он спокойно, так как он получил военный билет благодаря связям отца. Проживал он один в квартире которую снимали ему родители."
    "Сёма глянул в телефоне время. Было уже 7:16."
    th "И где этот ебаный автобус? Я так опоздать могу."
    "Через эту остановку ходил только один автобус под номером 46."
    play sound sfx_alisa_lighter 
    "Сёма достал ещё одну сигарету и прикурил."
    "Он начал думать о жизни."
    th "Бля, с одной стороны я живу по кайфу. Но с другой стороны как - то скучновато. Никаких интересных приключений, нигде не гуляю. Только старые друзья в кс зовут иногда."
    th "Да и девушки у меня нету. Вообще если подумать - жить одному классно. Хоть иногда и хочется найти тян."
    th "Да где этот сраный автобус?"
    "Сёма посмотрел на время и понял то что он уже опаздывает. Время было 7.32, а на работе надо быть уже в 8"
    th "Не дай бог меня за это оштрафуют. Я этого водилу отпизжу."
    "Спустя несколько минут подъехал какой то старый автобус."
    play sound sfx_intro_bus_engine_start
    th "Явление Христа народу ебать того рот!"
    stop ambience
    stop music
    with dissolve
    scene bg intro_xx
    with dissolve2
    play sound sfx_intro_bus_engine_loop
    play sound sfx_bus_interior_moving
    th "Бля, а чё он такой старый? Ладно, похуй."
    "В автобусе никого небыло за исключением водителя."
    "Сёма оплатил проезд у водителя."
    me "На ленинской разбудите пожалуйста, не выспался немного."
    "Водитель лишь слегка кивнул."
    "Сёма развалился на сидении и полез в карман за телефоном. Но он замети что на полу под его ногами лежит листик из календаря."
    "Там было обведено число 4 июля."
    th "Хмм, а восьмого у меня др. 18 исполниться, во всех магазах смогу пиво покупать с сигами, а не только у кента на районе."
    "Сёма закрыл глаза что бы поспать. Он сразу же уснул."
    stop sound
    jump semkayebivaet_d1