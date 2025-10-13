import flet as ft
from time import sleep
# a={"МКТ":"молекулярно-кинетическая теория ",
#    "диффузия":"самопроизвольное проникновение веществ друг в друга",
#    "агрегатное состояние":"состояние в-ва в жидком, твёрдом или газообразном состоянии",
#    "аморфное состояние":"Вещества в аморфном состоянии, как и жидкости, текучи, только текут они очень медленно.",
#    "смачивание":"если притяжение между молекулами поверхности твёрдого тела и молекулами жидкости, находящейся н а этой поверхности, больше, чем притяжение молекул жидкости между собой, то жидкость смачивает по-верхность.",
#    "капилляр":"узкая трубка",
#    "капиллярные явления":"в смачивающих жидкостях чем уже трубка тем выше подымется жидкость, в несмачивающих жидкостях чем уже трубка тем меньше будет подыматься жидкость",
#    "тепловые явления":"явления у которых важной характеристикой является температура",
#    "тепловое равновесие":"если несколько тел различной температуры привести в соприкосновение друг с другом, то через некотороевремя температура всех тел станет одинаковой",
#    "С":"C=K-273",
#    "Внутреняя энергия тела":"сумма потенциальной и кинетической энергии тела",
#    "Теплопередача":"Процесс изменения внутренней энергии тела без совершения работы",
#    "теплопроводность":"процесс, при котором энергия передаётся от одного тела к другому или от одной части тела к другой за счёт теплового движения частиц и их взаимодействия между собой",
#    "конвекция":"Перенос энергии потоками жидкости и газа",
#    "Джоуль":"Кол-во теплоты",
#    "Удельная теплоёмкость в-ва":"(табличное значение)Удельная теплоёмкость в-ва=кол-во теплоты/масса*разность конечной и начальной температур тела(c=Q/m(t2-t1))",
#    "Охлаждение":"Q = cm(t1 - t2)",
#    "Нагревание":"Q = cm(t2 - t1)",
#    "Плавление":"Переход вещества из твёрдого состояния в жидкое",
#    "Температура плавления":"Температура, при которой вещество плавится",
#    "Отвердивание":"Переход вещества из жидкого состояния в твёрдое",
#    "Кристализация":"Переход вещества из жидкого состояния в твёрдое",
#    "Температура отвердивания(кристализации)":"Температуру, при которой вещество отвердевает(кристализуется)",
#    "Теплота плавления":"Количество теплоты, которое нужно сообщить 1 кг кристаллического вещества при температуре плавления, чтобы превратить его в жидкость",
#    "парообразование":"Процесс превращения жидкости в пар",
#    "испарение":"Процесс парообразования с поверхности жидкости",
#    "конденсация":"Процесс превращения пара в жидкость",
#    "насыщение":"Пар, находящийся в динамическом равновесии со своей жидкостью",
#    "динамическое равновесие":"число молекул, покидающих жидкость, равно числу молекул, возвращающихся в неё",
#    "Ненасыщенные пар":"Пар, не находящийся в динамическом равновесии со своей жидкостью",
#    "Относительная влажность воздуха":"отношение абсолютнойвлажности воздуха к плотности насыщенного водяного пара при той же температуре, выраженное в процентах",
#    "Точка росы":"Температуру, при которой находящийся в воздухе водяной пар становится насыщенным",
#    "кипение":"процесс парообразования, происходящий по всему объёму жидкости",
#    "температура кипения":"Температуру, при которой жидкость кипит",
#    "удельная теплота парообразования":"Количество теплоты, необходимое для превращения жидкости массой 1 кг в пар при температуре кипения",
#    "тепловой двигатель":"машина которая превращяет внутрюнюю энергию топлива в механическую",
#    "КПД":"коэфицент полезного действия",
#    "КПД теплового двигателя":"работа/кол-во теплоты выделившемуся при сгорании топлива(A/Q1)",
#    "Электризация":"это сообщение телу электрического заряда",
#    "Точечный заряд":"заряженное тело, размеры которого пренебрежимо малы по сравнению с расстояниями от него до других рассматриваемых тел.",
#    "Напряжённость электрического поля":"физическая величина, равная отношению электрической силы, действующей на помещённый в электрическое поле пробный заряд, к значению этого заряда.",
#    "Сила тока":"Физическая величина, равная отношению электрического заряда, прошедшего через поперечное сечение проводника, ко времени его прохожде-ния(I=q/t)",
#    "Напряжение тока":"Отношение работы электрического поля по перемещению электрического заряда между двумя точками цепи к этому заряду",
#    "Сопротевление":"Физическая величина, равная отношению напряжения U н а концах проводника к силе тока, проходящего по нему",
#    "Удельное сопротивление":"сопротивление*площадь поперечного сечения/длина проводника",
#    "Последовательное соединение":"бщее напряжение в последовательной цепи равно сумме напряжений на её отдельных участках, общее сопротивление нескольких последовательно соединённых проводников равно сумме сопротивлений каждого из них",
#    "паралленльное соединение":"сила тока в неразветвлённой части цепи равна сумме сил токов на её отдельных участках и R=1/R1+1/R2",
#    "работа тока":"произведению напряжения на концах этого участка, силы тока и времени прохождения тока",
#    "мощность тока":"произведению напряжения и силы тока в цепи",
#    "Закон Джоуля-Ленца":"Количество теплоты, выделяющееся при прохождении тока в проводнике, равно произведению квадрата силы тока, сопротивления проводникаи времени прохождения тока",
#    "Закон Джоуля":"Сопротивление проводника равно отношению напряжениею к силе тока",
#    "магнитные линии":"Линии, вдоль которых в магнитном поле располагаются оси маленьких магнитных стрелок",
#    "Электромагнит":"катушка с железным сердечником",
# }
txt={"/1/2":"Как вы знаете, одно и то же вещество в зависимости от внешних условий может находиться в одном из агрегатных состояний: жидком, твёрдом или газообразном. Как определить, что находится в стакане: вода или прозрачный лёд? Для этого необходимо использовать информацию о свойствах вещества в различных агрегатных состояниях. Вы же помните, что жидкости сохраняют объём, но не форму — они текучи и приобретают форму того сосуда, в который их переливают. Особенностью твёрдых тел является наличие собственного объёма и формы. Газы не обладают ни собственной формой, ни собственным объёмом. Они занимают весь предоставленный им объём, принимая форму сосуда. Газы легко сжать. Во всех трёх агрегатных состояниях вещество, например вода, образовано одинаковыми молекулами — молекулами воды. Почему же одно и то же вещество может быть и жидкостью, и твёрдым телом, и газом? Как вам известно, молекулы вещества взаимодействуют друг с другом, а также совершают непрерывное хаотическое движение. Можно предположить, что существование различных агрегатных состояний связано с особенностями взаимодействия и движения молекул вещества. Представим, что молекулы только беспорядочно движутся и при этом не взаимодействуют. Тогда они разлетались бы по всем направлениям, и вещество занимало бы весь предоставленный объём. Значит, единственно возможным состоянием вещества было бы газообразное состояние. А к чему приводит наличие взаимодействия между молекулами? Вы знаете, что молекулы взаимодействуют друг с другом силами притяжения и отталкивания, причём проявляется это взаимодействие на малых расстояниях. Так, если молекулы находятся на расстояниях, превышающих их размеры в несколько раз, то силы взаимодействия между ними уже почти не сказываются. Итак, существует некоторое равновесное расстояние между молекулами данного вещества, на котором силы отталкивания равны силам притяжения. Если расстояние между молекулами больше равновесного, то преобладают силы притяжения, если меньше — силы отталкивания. Представим, что хаотическое движение молекул отсутствует. Тогда все молекулы располагались бы в положениях равновесия и единственно возможным состоянием вещества было бы твёрдое состояние. Но молекулы взаимодействуют и движутся одновременно. Силы притяжения стремятся сблизить их, а хаотическое движение препятствует этому. Быть ли телу газообразным, жидким или твёрдым, зависит от соотношения этих факторов. В газах молекулы быстро движутся и почти не взаимодействуют, в твёрдых телах, наоборот, взаимодействие молекул велико, а движутся они медленно. Промежуточный случай соответствует жидкости. Опишем агрегатные состояния с молекулярной точки зрения более подробно и дадим объяснение их свойствам. В газах среднее расстояние между молекулами значительно больше их размеров. На таких расстояниях силы взаимодействия молекул почти отсутствуют. Поэтому вещество в газообразном состоянии не сохраняет ни форму, ни объём. Бо́льшую часть времени каждая молекула движется прямолинейно, затем меняет направление движения в результате столкновения с другой молекулой. В отличие от газов в жидкостях молекулы находятся близко друг к другу. Взаимодействие между молекулами достаточно велико для того, чтобы объём жидкости оставался постоянным, но не достаточно велико для сохранения жидкостью формы. Положения молекул жидкости относительно друг друга не фиксированы. Совершив несколько десятков—сотен колебаний около некоторого положения равновесия, молекула скачком меняет его на новое и колеблется рядом с новыми соседями. В твёрдых телах молекулы находятся друг от друга на расстояниях, близких к размерам молекул, и колеблются около положений равновесия. В случае попытки увеличить или уменьшить расстояние между молекулами возникают значительные силы их притяжения или отталкивания. Этим объясняется, что твёрдые тела сохраняют форму и объём. Молекулы и атомы большинства веществ в твёрдом состоянии расположены в строго определённом порядке, образующем повторяющуюся структуру — кристаллическую решётку. Такое состояние вещества называют кристаллическим. Места нахождения атомов называют узлами кристаллической решётки. Бывают решётки, «составленные» из кубиков, параллелепипедов и т. п. Кристаллическое строение имеют поваренная соль, лёд, алмаз, железо и т. д. Существует твёрдое состояние вещества, для которого характерно отсутствие кристаллической решётки и в целом беспорядочное расположение молекул (атомов). Это аморфное состояние. У вещества в аморфном состоянии порядок во взаимном расположении атомов наблюдается только в небольшой области вблизи каждого атома и с увеличением расстояния исчезает. В природе в аморфном состоянии могут находиться опал, янтарь, смолы и т. д. Вещества в аморфном состоянии, как и жидкости, текучи, только текут они очень медленно."}
anw={"/1/2/test":["твёрдое","жидкое","газообразное"]}
b={"/":"ОГЛАВЛЕНИЕ","/1":"Глава 1:ТЕПЛОВЫЕ ЯВЛЕНИЯ","/2":"Глава 2:ЭЛЕКТРИЧЕСКИЕ ЯВЛЕНИЯ",
   "/3":"Глава 3:ЭЛЕКТРОМАГНИТНЫЕ ЯВЛЕНИЯ",
   "/1/2":"Агрегатные состояния вещества ",
   "/1/3":"Смачивание и несмачивание. Капиллярные явления",
   "/1/4":"Температура",
   "/1/5":"Внутренняя энергия",
   "/1/6":"Способы изменения внутренней энергии тела ",
   "/1/7":"Теплопроводность","/1/8":"Конвекция",
   "/1/9":"Излучение",
   "/1/10":"Количество теплоты. Единицы количества теплоты",
   "/1/11":"Удельная теплоёмкость",
   "/1/12":"Расчёт количества теплоты. Уравнение теплового баланса",
   "/1/13":"Энергия топлива. Удельная теплота сгорания",
   "/1/14":"Закон сохранения и превращения энергии в механических и тепловых процессах",
   "/1/15":"Плавление и отвердевание кристаллических тел",
   "/1/16":"График плавления и отвердевания кристаллических тел",
   "/1/17":"Удельная теплота плавления",
   "/1/18":"Испарение. Конденсация. Насыщенный и ненасыщенный пар",
   "/1/19":"Поглощение энергии при испарении жидкости. Выделение энергии при конденсации пара",
   "/1/20":"Влажность воздуха. Способы определения влажности воздуха",
   "/1/21":"Кипение",
   "/1/22":"Удельная теплота парообразования",
   "/1/23":"Работа газа и пара при расширении",
   "/1/24":"Двигатель внутреннего сгорания",
   "/1/25":"Паровая турбина",
   "/1/26":"КПД теплового двигателя",
   "/2/27":"Электризация тел при соприкосновении. Взаимодействие заряженных тел",
   "/2/28":"Электроскоп. Проводники и непроводники электричества",
   "/2/29":"Закон Кулона. Электрическое поле ",
   "/2/30":"Делимость электрического заряда. Электрон",
   "/2/31":"Строение атома",
   "/2/32":"Объяснение электрических явлений. Закон сохранения электрического заряда",
   "/2/33":"Статическое электричество, его учёт и использованиев быту и технике",
   "/2/34":"Электрический ток. Источники электрического тока",
   "/2/35":"Электрическая цепь и её составные части",
   "/2/36":"Электрический ток в металлах",
   "/2/37":"Действия электрического тока",
   "/2/38":"Сила тока. Измерение силы тока",
   "/2/39":"Электрическое напряжение. Измерение напряжения",
   "/2/40":"Электрическое сопротивление проводника. Закон Ома для участка цепи ",
   "/2/41":"Расчёт сопротивления проводника. Удельное сопротивление ",
   "/2/42":"Примеры на расчёт сопротивления проводника, силы тока и напряжения ",
   "/2/43":"Реостаты",
   "/2/44":"Последовательное соединение проводников ",
   "/2/45":"Параллельное соединение проводников ",
   "/2/46":"Работа и мощность электрического тока",
   "/2/47":"Нагревание проводников электрическим током. Закон Джоуля —Ленца",
   "/2/48":"Лампа освещения. Электрические нагревательные приборы ",
   "/2/49":"Короткое замыкание. Предохранители",
   "/3/50":"Постоянные магниты ","/3/51":"Магнитное поле",
   "/3/52":"Магнитное поле проводников с током и постоянных магнитов. Магнитные линии",
   "/3/53":"Магнитное поле катушки с током","/3/54":"Магнитное поле Земли ",
   "/3/55":"Действие магнитного поля на проводник с током. Правило левой руки",
   "/3/56":"Индукция магнитного поля ",
   "/3/57":"Электрический двигатель","/3/58":"Магнитный поток",
   "/3/59":"Явление электромагнитной индукции ",
   "/3/60":"Направление индукционного тока. Правило Ленца",
   "/3/61":"Способы получения электрической энергии",
   "/3/62":"Передача электрической энергии"}

# def dropdown_changed(e):
#         page.update()
# dd=ft.DropdownM2(on_change=dropdown_changed,hint_text="Глава",options=[
#             ft.dropdownm2.Option("Глава 1:ТЕПЛОВЫЕ ЯВЛЕНИЯ"),
#             ft.dropdownm2.Option("Глава 2:ЭЛЕКТРИЧЕСКИЕ ЯВЛЕНИЯ"),
#             ft.dropdownm2.Option("Глава 3:ЭЛЕКТРОМАГНИТНЫЕ ЯВЛЕНИЯ"),
#         ],)



def main(pagew: ft.Page):
    def goto_pagew2(n):
        pagew.go(button2.data)
    def goto_pagew3(n):
        pagew.go(button3.data)
    def goto_pagew4(n):
        pagew.go(button4.data)
    def goto_pagew5(n):
        pagew.go(button5.data)
    def goto_pagew6(n):
        pagew.go(button6.data)
    def goto_pagew7(n):
        pagew.go(button7.data)
    def goto_pagew8(n):
        pagew.go(button8.data)
    def goto_pagew9(n):
        pagew.go(button9.data)
    def goto_pagew10(n):
        pagew.go(button10.data)
    def goto_pagew11(n):
        pagew.go(button11.data)
    def goto_pagew12(n):
        pagew.go(button12.data)
    def goto_pagew13(n):
        pagew.go(button13.data)
    def goto_pagew14(n):
        pagew.go(button14.data)
    def goto_pagew15(n):
        pagew.go(button15.data)
    def goto_pagew16(n):
        pagew.go(button16.data)
    def goto_pagew17(n):
        pagew.go(button17.data)
    def goto_pagew18(n):
        pagew.go(button18.data)
    def goto_pagew19(n):
        pagew.go(button19.data)
    def goto_pagew20(n):
        pagew.go(button20.data)
    def goto_pagew21(n):
        pagew.go(button21.data)
    def goto_pagew22(n):
        pagew.go(button22.data)
    def goto_pagew23(n):
        pagew.go(button23.data)
    def goto_pagew24(n):
        pagew.go(button24.data)
    def goto_pagew25(n):
        pagew.go(button25.data)
    def goto_pagew26(n):
        pagew.go(button26.data)
    def goto_pagew27(n):
        pagew.go(button27.data)
    def goto_pagew28(n):
        pagew.go(button28.data)
    def goto_pagew29(n):
        pagew.go(button29.data)
    def goto_pagew30(n):
        pagew.go(button30.data)
    def goto_pagew31(n):
        pagew.go(button31.data)
    def goto_pagew32(n):
        pagew.go(button32.data)
    def goto_pagew33(n):
        pagew.go(button33.data)
    def goto_pagew34(n):
        pagew.go(button34.data)
    def goto_pagew35(n):
        pagew.go(button35.data)
    def goto_pagew36(n):
        pagew.go(button36.data)
    def goto_pagew37(n):
        pagew.go(button37.data)
    def goto_pagew38(n):
        pagew.go(button38.data)
    def goto_pagew39(n):
        pagew.go(button39.data)
    def goto_pagew40(n):
        pagew.go(button40.data)
    def goto_pagew41(n):
        pagew.go(button41.data)
    def goto_pagew42(n):
        pagew.go(button42.data)
    def goto_pagew43(n):
        pagew.go(button43.data)
    def goto_pagew44(n):
        pagew.go(button44.data)
    def goto_pagew45(n):
        pagew.go(button45.data)
    def goto_pagew46(n):
        pagew.go(button46.data)
    def goto_pagew47(n):
        pagew.go(button47.data)
    def goto_pagew48(n):
        pagew.go(button48.data)
    def goto_pagew49(n):
        pagew.go(button49.data)
    def goto_pagew50(n):
        pagew.go(button50.data)
    def goto_pagew51(n):
        pagew.go(button51.data)
    def goto_pagew52(n):
        pagew.go(button52.data)
    def goto_pagew53(n):
        pagew.go(button53.data)
    def goto_pagew54(n):
        pagew.go(button54.data)
    def goto_pagew55(n):
        pagew.go(button55.data)
    def goto_pagew56(n):
        pagew.go(button56.data)
    def goto_pagew57(n):
        pagew.go(button57.data)
    def goto_pagew58(n):
        pagew.go(button58.data)
    def goto_pagew59(n):
        pagew.go(button59.data)
    def goto_pagew60(n):
        pagew.go(button60.data)
    def goto_pagew61(n):
        pagew.go(button61.data)
    def goto_pagew62(n):
        pagew.go(button62.data)
    def goto_test(n):
        pagew.go(pagew.route+"/test")
        pagew.update()
    def goto_test_end(n):
        if txtf.value.lower().split(",").sort() == anw[pagew.route].lower().split(",").sort() and txtf.value != "":
            
            print(txtf.value)
            print(anw[pagew.route].lower().replace(",","").split(" "))
            pagew.go("/")
    button2 = ft.TextButton(b["/1/2"],on_click=goto_pagew2,data="/1/2")
    button3 = ft.TextButton(b["/1/3"],on_click=goto_pagew3,data="/1/3")
    button4 = ft.TextButton(b["/1/4"],on_click=goto_pagew4,data="/1/4")
    button5 = ft.TextButton(b["/1/5"],on_click=goto_pagew5,data="/1/5")
    button6 = ft.TextButton(b["/1/6"],on_click=goto_pagew6,data="/1/6")
    button7 = ft.TextButton(b["/1/7"],on_click=goto_pagew7,data="/1/7")
    button8 = ft.TextButton(b["/1/8"],on_click=goto_pagew8,data="/1/8")
    button9 = ft.TextButton(b["/1/9"],on_click=goto_pagew9,data="/1/9")
    button10 = ft.TextButton(b["/1/10"],on_click=goto_pagew10,data="/1/10")
    button11 = ft.TextButton(b["/1/11"],on_click=goto_pagew11,data="/1/11")
    button12 = ft.TextButton(b["/1/12"],on_click=goto_pagew12,data="/1/12")
    button13 = ft.TextButton(b["/1/13"],on_click=goto_pagew13,data="/1/13")
    button14 = ft.TextButton(b["/1/14"],on_click=goto_pagew14,data="/1/14")
    button15 = ft.TextButton(b["/1/15"],on_click=goto_pagew15,data="/1/15")
    button16 = ft.TextButton(b["/1/16"],on_click=goto_pagew16,data="/1/16")
    button17 = ft.TextButton(b["/1/17"],on_click=goto_pagew17,data="/1/17")
    button18 = ft.TextButton(b["/1/18"],on_click=goto_pagew18,data="/1/18")
    button19 = ft.TextButton(b["/1/19"],on_click=goto_pagew19,data="/1/19")
    button20 = ft.TextButton(b["/1/20"],on_click=goto_pagew20,data="/1/20")
    button21 = ft.TextButton(b["/1/21"],on_click=goto_pagew21,data="/1/21")
    button22 = ft.TextButton(b["/1/22"],on_click=goto_pagew22,data="/1/22")
    button23 = ft.TextButton(b["/1/23"],on_click=goto_pagew23,data="/1/23")
    button24 = ft.TextButton(b["/1/24"],on_click=goto_pagew24,data="/1/24")
    button25 = ft.TextButton(b["/1/25"],on_click=goto_pagew25,data="/1/25")
    button26 = ft.TextButton(b["/1/26"],on_click=goto_pagew26,data="/1/26")
    button27 = ft.TextButton(b["/2/27"],on_click=goto_pagew27,data="/2/27")
    button28 = ft.TextButton(b["/2/28"],on_click=goto_pagew28,data="/2/28")
    button29 = ft.TextButton(b["/2/29"],on_click=goto_pagew29,data="/2/29")
    button30 = ft.TextButton(b["/2/30"],on_click=goto_pagew30,data="/2/30")
    button31 = ft.TextButton(b["/2/31"],on_click=goto_pagew31,data="/2/31")
    button32 = ft.TextButton(b["/2/32"],on_click=goto_pagew32,data="/2/32")
    button33 = ft.TextButton(b["/2/33"],on_click=goto_pagew33,data="/2/33")
    button34 = ft.TextButton(b["/2/34"],on_click=goto_pagew34,data="/2/34")
    button35 = ft.TextButton(b["/2/35"],on_click=goto_pagew35,data="/2/35")
    button36 = ft.TextButton(b["/2/36"],on_click=goto_pagew36,data="/2/36")
    button37 = ft.TextButton(b["/2/37"],on_click=goto_pagew37,data="/2/37")
    button38 = ft.TextButton(b["/2/38"],on_click=goto_pagew38,data="/2/38")
    button39 = ft.TextButton(b["/2/39"],on_click=goto_pagew39,data="/2/39")
    button40 = ft.TextButton(b["/2/40"],on_click=goto_pagew40,data="/2/40")
    button41 = ft.TextButton(b["/2/41"],on_click=goto_pagew41,data="/2/41")
    button42 = ft.TextButton(b["/2/42"],on_click=goto_pagew42,data="/2/42")
    button43 = ft.TextButton(b["/2/43"],on_click=goto_pagew43,data="/2/43")
    button44 = ft.TextButton(b["/2/44"],on_click=goto_pagew44,data="/2/44")
    button45 = ft.TextButton(b["/2/45"],on_click=goto_pagew45,data="/2/45")
    button46 = ft.TextButton(b["/2/46"],on_click=goto_pagew46,data="/2/46")
    button47 = ft.TextButton(b["/2/47"],on_click=goto_pagew47,data="/2/47")
    button48 = ft.TextButton(b["/2/48"],on_click=goto_pagew48,data="/2/48")
    button49 = ft.TextButton(b["/2/49"],on_click=goto_pagew49,data="/2/49")
    button50 = ft.TextButton(b["/3/50"],on_click=goto_pagew50,data="/3/50")
    button51 = ft.TextButton(b["/3/51"],on_click=goto_pagew51,data="/3/51")
    button52 = ft.TextButton(b["/3/52"],on_click=goto_pagew52,data="/3/52")
    button53 = ft.TextButton(b["/3/53"],on_click=goto_pagew53,data="/3/53")
    button54 = ft.TextButton(b["/3/54"],on_click=goto_pagew54,data="/3/54")
    button55 = ft.TextButton(b["/3/55"],on_click=goto_pagew55,data="/3/55")
    button56 = ft.TextButton(b["/3/56"],on_click=goto_pagew56,data="/3/56")
    button57 = ft.TextButton(b["/3/57"],on_click=goto_pagew57,data="/3/57")
    button58 = ft.TextButton(b["/3/58"],on_click=goto_pagew58,data="/3/58")
    button59 = ft.TextButton(b["/3/59"],on_click=goto_pagew59,data="/3/59")
    button60 = ft.TextButton(b["/3/60"],on_click=goto_pagew60,data="/3/60")
    button61 = ft.TextButton(b["/3/61"],on_click=goto_pagew61,data="/3/61")
    button62 = ft.TextButton(b["/3/62"],on_click=goto_pagew62,data="/3/62")
    txtf = ft.TextField(label="Ответ",border=ft.InputBorder.UNDERLINE,border_color=ft.Colors.BLUE_200,hint_text="Пишите только запятые без пробелов")
    buttons1 = [button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26]
    buttons2 = [button27,button28,button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,button39,button40,button41,button42,button43,button44,button45,button46,button47,button48,button49]
    buttons3 = [button50,button51,button52,button53,button54,button55,button56,button57,button58,button59,button60,button61]
    pagew.title = "Электронный учебник"

    print("Initial route:", pagew.route)
    tests={"/1/2":["Налейте в пластиковую бутылку немного холодной воды и поместите её в морозильную камеру на несколько часов, чтобы образовался лёд. Затем, вынув бутылку со льдом, добавьте в неё воды. Внутри будет находиться вода одновременно в трёх состояниях. Какие это состояния?"]}
    def route_change(e):
        print("Route change:", e.route)
        pagew.views.clear()
        pagew.views.append(
            ft.View(
                "/",
                [

                ft.AppBar(title=ft.Text(b["/"], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),
                ft.Row([
                    ft.Column([ft.ElevatedButton("Глава 1:ТЕПЛОВЫЕ ЯВЛЕНИЯ",on_click=open_1)]+buttons1),
                    ft.Column([ft.ElevatedButton("Глава 2:ЭЛЕКТРИЧЕСКИЕ ЯВЛЕНИЯ",on_click=open_2)]+buttons2),
                    ft.Column([ft.ElevatedButton("Глава 3:ЭЛЕКТРОМАГНИТНЫЕ ЯВЛЕНИЯ",on_click=open_3)]+buttons3)
                ]),
                ],
                )
        )
        if pagew.route == "/1" :
            pagew.views.append(
                ft.View(
                    "/1",
                    [   ft.AppBar(title=ft.Text(b["/1"], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),
                        ft.Column(buttons1)
                    ],
                )
            )
        if pagew.route == "/2":
            pagew.views.append(
                ft.View(
                    "/2",
                    [   ft.AppBar(title=ft.Text(b["/2"], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),
                        ft.Column(buttons2)
                    ],
                )
            )
        if pagew.route == "/3":
            pagew.views.append(
                ft.View(
                    "/3",
                    [   ft.AppBar(title=ft.Text(b["/3"], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),
                        ft.Column(buttons3)
                    ],
                )
            )
        for i in range(2,27):
            if pagew.route == "/1/"+str(i):
                pagew.views.append(
                    ft.View(
                    "/1/"+str(i),[ft.AppBar(title=ft.Text(b["/1/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),ft.Text(value=txt["/1/"+str(i-i+2)],theme_style=ft.TextThemeStyle.TITLE_MEDIUM,weight=300),ft.TextButton("Приступить к тестированию",on_click=goto_test)]
                    )
                )
        for i in range(27,50):
            if pagew.route == "/2/"+str(i):
                pagew.views.append(
                    ft.View(
                    "/2/"+str(i),[ft.AppBar(title=ft.Text(b["/2/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),]
                    )
                )
        for i in range(50,63):
            if pagew.route == "/3/"+str(i):
                pagew.views.append(
                    ft.View(
                    "/3/"+str(i),[ft.AppBar(title=ft.Text(b["/3/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),]
                    )
                )
        for i in range(2,27):
            if pagew.route == "/1/"+str(i)+"/test":
                pagew.views.append(
                    ft.View(
                    "/1/"+str(i)+"/test",[ft.AppBar(title=ft.Text("Тестирование по теме "+b["/1/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),ft.Text(value=tests["/1/"+str(i-i+2)][0],theme_style=ft.TextThemeStyle.HEADLINE_SMALL),txtf,ft.TextButton("Закончить тестирование",on_click=goto_test_end)]
                    )
                )
        for i in range(27,50):
            if pagew.route == "/2/"+str(i)+"/test":
                pagew.views.append(
                    ft.View(
                    "/2/"+str(i)+"/test",[ft.AppBar(title=ft.Text("Тестирование по теме "+b["/2/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),ft.TextButton("Закончить тестирование",on_click=goto_test_end)]
                    )
                )
        for i in range(50,63):
            if pagew.route == "/3/"+str(i)+"/test":
                pagew.views.append(
                    ft.View(
                    "/3/"+str(i)+"/test",[ft.AppBar(title=ft.Text("Тестирование по теме "+b["/3/"+str(i)], theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM),center_title=True),ft.TextButton("Закончить тестирование",on_click=goto_test_end)]
                    )
                )
        pagew.update()

    pagew.on_route_change = route_change


    def open_1(e):
        pagew.go("/1")

    def open_2(e):
        pagew.go("/2")

    def open_3(e):
        pagew.go("/3")



    pagew.go("/")
ft.app(target=main, view=ft.AppView.WEB_BROWSER)