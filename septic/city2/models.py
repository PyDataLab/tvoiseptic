from django.db import models

class MetaContent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    keywords = models.TextField(verbose_name="Ключевые слова")

    class Meta:
        verbose_name = "01 Метатеги"
        verbose_name_plural = "01 Метатеги"

    def __str__(self):
        return self.title

class SideBar(models.Model):
    engineer_text = models.CharField(max_length=255, verbose_name="Текст кнопки вызова инженера")
    price_text = models.CharField(max_length=255, verbose_name="Текст кнопки скачивания прайса")
    whatsapp_text = models.CharField(max_length=255, verbose_name="Текст кнопки WhatsApp")

    price_link = models.URLField(verbose_name="Ссылка на прайс")
    whatsapp_link = models.URLField(verbose_name="Ссылка на WhatsApp")

    sidebar_image_1 = models.FileField(upload_to='sidebar/', verbose_name="Изображение кнопки вызова инженера")
    sidebar_image_2 = models.FileField(upload_to='sidebar/', verbose_name="Изображение кнопки скачивания прайса")
    sidebar_image_3 = models.FileField(upload_to='sidebar/', verbose_name="Изображение кнопки WhatsApp")
    sidebar_arrow = models.FileField(upload_to='sidebar/', verbose_name="Изображение стрелки")

    class Meta:
        verbose_name = "02 Сайдбар"
        verbose_name_plural = "02 Сайдбар"

    def __str__(self):
        return "Контент для бокового меню"

class Header(models.Model):
    bg_desktop = models.FileField(upload_to='header/', verbose_name="Фон desktop")
    bg_mobile = models.FileField(upload_to='header/', verbose_name="Фон mobile")
    logo_link = models.URLField(verbose_name="Ссылка логотипа")
    logo_image = models.FileField(upload_to='header/', verbose_name="Логотип")
    header_text1 = models.TextField(verbose_name="Текст1 в шапке")
    header_text2 = models.TextField(verbose_name="Текст2 в шапке")
    map_image = models.FileField(upload_to='header/', verbose_name="Изображение карты")
    map_address = models.TextField(verbose_name="Адрес на карте")
    map_link = models.URLField(verbose_name="Ссылка на карту")
    map_link_text = models.TextField(verbose_name="Текст ссылки на карту")
    catalog_link = models.URLField(verbose_name="Ссылка на каталог")
    catalog_link_text = models.TextField(verbose_name="Текст cсылки на каталог")
    tg_link = models.URLField(verbose_name="Ссылка на телеграм")
    tg_icon = models.FileField(upload_to='header/', verbose_name="Изображение телеграм")
    wa_link = models.URLField(verbose_name="Ссылка на whatsapp")
    wa_icon = models.FileField(upload_to='header/', verbose_name="Изображение whatsapp")
    working_hours = models.TextField(verbose_name="Часы работы")
    phone_link = models.CharField(max_length=20, verbose_name="Ссылка для звонка")
    phone_image = models.FileField(upload_to='header/', verbose_name="Изображение телефона")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    popup_text = models.CharField(max_length=100, verbose_name="Текст popup")

    class Meta:
        verbose_name = "03 Шапка"
        verbose_name_plural = "03 Шапка"

    def __str__(self):
        return "Контент для шапки"

class Menu(models.Model):
    main_link = models.URLField(verbose_name="Ссылка на главную")
    main_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на главную")
    quiz_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на акции")
    budget_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на budget")
    catalog_link = models.URLField(verbose_name="Ссылка на каталог")
    catalog_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на каталог")
    guarantees_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на гарантии")
    portfolio_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки на портфолио")
    about_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки о компании")
    quality_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки о quality")
    contacts_link_text = models.CharField(max_length=100, verbose_name="Текст ссылки о contacts")

    class Meta:
        verbose_name = "04 Меню"
        verbose_name_plural = "04 Меню"

    def __str__(self):
        return "Контент для меню"

class MainContent(models.Model):
    h1 = models.TextField(verbose_name="Заголовок")
    check_img = models.FileField(upload_to='main/', verbose_name="Изображение check")
    text_1 = models.TextField(verbose_name="Текст 1")
    text_2 = models.TextField(verbose_name="Текст 2")
    text_3 = models.TextField(verbose_name="Текст 3")
    text_4 = models.TextField(verbose_name="Текст 4")
    text_5 = models.TextField(verbose_name="Текст 5")
    button_text = models.TextField(verbose_name="Текст кнопки")
    touch_img = models.FileField(upload_to='main/', verbose_name="Изображение touch")
    text_6 = models.TextField(verbose_name="Текст 6")
    text_01 = models.TextField(verbose_name="Текст 01")
    text_02 = models.TextField(verbose_name="Текст 02")
    text_03 = models.TextField(verbose_name="Текст 03")
    text_04 = models.TextField(verbose_name="Текст 04")
    text_05 = models.TextField(verbose_name="Текст 05")
    text_06 = models.TextField(verbose_name="Текст 06")

    class Meta:
        verbose_name = "05 Первый экран"
        verbose_name_plural = "05 Первый экран"

    def __str__(self):
        return "Контент для первого экрана"

class Add(models.Model):
    add_text = models.TextField(verbose_name="Add текст")
    arrow_img = models.FileField(upload_to='add/', verbose_name="Изображение arrow")
    add_text1 = models.TextField(verbose_name="Add текст1")
    swipe_img = models.FileField(upload_to='add/', verbose_name="Изображение swipe")
    add1_img = models.FileField(upload_to='add/', verbose_name="Изображение add1")
    add1_title = models.TextField(verbose_name="Add1 title")
    add1_text = models.TextField(verbose_name="Add1 text")
    add2_img = models.FileField(upload_to='add/', verbose_name="Изображение add2")
    add2_title = models.TextField(verbose_name="Add2 title")
    add2_text = models.TextField(verbose_name="Add2 text")
    add3_img = models.FileField(upload_to='add/', verbose_name="Изображение add3")
    add3_title = models.TextField(verbose_name="Add3 title")
    add3_text = models.TextField(verbose_name="Add3 text")
    add5_img = models.FileField(upload_to='add/', verbose_name="Изображение add5")
    add5_title = models.TextField(verbose_name="Add5 title")
    add5_text = models.TextField(verbose_name="Add5 text")
    add6_img = models.FileField(upload_to='add/', verbose_name="Изображение add6")
    add6_title = models.TextField(verbose_name="Add6 title")
    add6_text = models.TextField(verbose_name="Add6 text")

    class Meta:
        verbose_name = "06 Дополнительные услуги"
        verbose_name_plural = "06 Дополнительные услуги"

    def __str__(self):
        return "Контент для дополнительных услуг"

class Quiz(models.Model):
    quiz_header = models.TextField(verbose_name="Quiz header")
    quiz_header_text1 = models.TextField(verbose_name="Quiz header текст1")
    quiz_header_text2 = models.TextField(verbose_name="Quiz header текст2")
    quiz_header_text3 = models.TextField(verbose_name="Quiz header текст3")
    quiz_line_text1 = models.TextField(verbose_name="Quiz line текст1")
    quiz_question1_title = models.TextField(verbose_name="Quiz question1 title")
    quiz_question1_1_img = models.FileField(upload_to='quiz/', verbose_name="Quiz первый вопрос первый вариант ответа изображение")
    quiz_question1_1_text = models.TextField(verbose_name="Quiz первый вопрос первый вариант ответа текст")
    quiz_question1_2_img = models.FileField(upload_to='quiz/', verbose_name="Quiz первый вопрос второй вариант ответа изображение")
    quiz_question1_2_text = models.TextField(verbose_name="Quiz первый вопрос второй вариант ответа текст")
    quiz_question1_3_img = models.FileField(upload_to='quiz/', verbose_name="Quiz первый вопрос третий вариант ответа изображение")
    quiz_question1_3_text = models.TextField(verbose_name="Quiz первый вопрос третий вариант ответа текст")
    quiz_question2_title = models.TextField(verbose_name="Quiz второй вопрос заголовок")
    quiz_question2_1 = models.TextField(verbose_name="Quiz второй вопрос первый вариант ответа")
    quiz_question2_2 = models.TextField(verbose_name="Quiz второй вопрос второй вариант ответа")
    quiz_question2_3 = models.TextField(verbose_name="Quiz второй вопрос третий вариант ответа")
    quiz_question2_4 = models.TextField(verbose_name="Quiz второй вопрос четвёртый вариант ответа")
    quiz_question3_title = models.TextField(verbose_name="Quiz третий вопрос заголовок")
    quiz_question3_1_text = models.TextField(verbose_name="Quiz третий вопрос первый вариант ответа текст")
    quiz_question3_1_hint = models.TextField(verbose_name="Quiz третий вопрос первый вариант ответа hint")
    quiz_question3_2_text = models.TextField(verbose_name="Quiz третий вопрос второй вариант ответа текст")
    quiz_question3_2_hint = models.TextField(verbose_name="Quiz третий вопрос второй вариант ответа hint")
    quiz_question3_3_text = models.TextField(verbose_name="Quiz третий вопрос третий вариант ответа текст")
    quiz_question3_3_hint = models.TextField(verbose_name="Quiz третий вопрос третий вариант ответа hint")
    quiz_question3_4_text = models.TextField(verbose_name="Quiz третий вопрос четвёртый вариант ответа текст")
    quiz_question3_4_hint = models.TextField(verbose_name="Quiz третий вопрос четвёртый вариант ответа hint")
    quiz_question4_title = models.TextField(verbose_name="Quiz четвёртый вопрос заголовок")
    quiz_question4_1 = models.TextField(verbose_name="Quiz четвёртый вопрос первый вариант ответа")
    quiz_question4_2 = models.TextField(verbose_name="Quiz четвёртый вопрос второй вариант ответа")
    touch_img = models.FileField(upload_to='quiz/', verbose_name="Изображение touch")
    touch_text = models.TextField(verbose_name="Текст touch")
    button_text1 = models.TextField(verbose_name="Текст кнопки1")
    button_text2 = models.TextField(verbose_name="Текст кнопки2")
    quiz_right_bg = models.FileField(upload_to='quiz/', verbose_name="Quiz right изображение bg")
    quiz_right_text1 = models.TextField(verbose_name="Quiz right текст 1")
    quiz_right_text2 = models.TextField(verbose_name="Quiz right текст 2")
    quiz_right_text3 = models.TextField(verbose_name="Quiz right текст 3")
    quiz_load_img = models.FileField(upload_to='quiz/', verbose_name="Quiz load изображение")
    quiz_load_text = models.TextField(verbose_name="Quiz load текст")
    quiz_result_bg = models.FileField(upload_to='quiz/', verbose_name="Quiz result изображение bg")
    quiz_result_title = models.TextField(verbose_name="Quiz result заголовок")
    quiz_result_subtitle = models.TextField(verbose_name="Quiz result subtitle")
    quiz_result_text = models.TextField(verbose_name="Quiz result text")
    quiz_result_wa = models.FileField(upload_to='quiz/', verbose_name="Quiz result изображение wa")
    quiz_result_tg = models.FileField(upload_to='quiz/', verbose_name="Quiz result изображение tg")
    quiz_result_btn_text = models.TextField(verbose_name="Quiz result btn text")
    quiz_result_wa_text = models.TextField(verbose_name="Quiz result wa text")
    quiz_result_tg_text = models.TextField(verbose_name="Quiz result tg text")
    quiz_result_btn_text2 = models.TextField(verbose_name="Quiz result btn text2")
    quiz_result_check = models.FileField(upload_to='quiz/', verbose_name="Quiz result изображение check")
    quiz_result_check_text = models.TextField(verbose_name="Quiz result check text")

    class Meta:
        verbose_name = "07 Квиз"
        verbose_name_plural = "07 Квиз"

    def __str__(self):
        return "Контент для квиза"

class Category(models.Model):
    header = models.TextField(verbose_name="Header")
    swipe_text = models.TextField(verbose_name="Swipe text")
    swipe_img = models.FileField(upload_to='categories/', verbose_name="Swipe изображение")
    arrow_img = models.FileField(upload_to='categories/', verbose_name="Arrow изображение")
    manufacturer2_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 2 изображение")
    manufacturer1_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 1 изображение")
    manufacturer3_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 3 изображение")
    manufacturer8_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 8 изображение")
    manufacturer6_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 6 изображение")
    manufacturer4_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 4 изображение")
    manufacturer5_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 5 изображение")
    manufacturer7_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 7 изображение")
    manufacturer9_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 9 изображение")
    manufacturer10_img = models.FileField(upload_to='categories/', verbose_name="Manufacturer 10 изображение")

    class Meta:
        verbose_name = "08 Производители"
        verbose_name_plural = "08 Производители"

    def __str__(self):
        return "Контент для производителей"

class ModelStatic(models.Model):
    title_description_s = models.TextField(verbose_name="Заголовок описания")
    title_char_s = models.TextField(verbose_name="Заголовок характеристик")
    text_btn_s = models.TextField(verbose_name="Текст кнопки")
    hint_key_s = models.TextField(verbose_name="Hint вопрос")
    hint_value_s = models.TextField(verbose_name="Hint ответ")
    installment_s = models.TextField(verbose_name="Рассрочка")
    delivery_s = models.TextField(verbose_name="Доставка")
    wa_text_s = models.TextField(verbose_name="Текст WhatsApp")
    wa_link_s = models.URLField(verbose_name="Ссылка WhatsApp")
    ya_map_title = models.TextField(verbose_name="Заголовок яндекс карт")
    ya_map_link = models.URLField(verbose_name="Ссылка яндекс карт")
    ya_map_btn = models.TextField(verbose_name="Кнопка яндекс карт")

    class Meta:
        verbose_name = "09 Модели статика"
        verbose_name_plural = "09 Модели статика"

    def __str__(self):
        return "Контент для модели статика"

class ModelDynamic(models.Model):
    manufacturer_number_d = models.IntegerField(verbose_name="Номер производителя")
    model_number_d = models.IntegerField(verbose_name="Номер модели")
    name_d = models.TextField(verbose_name="Название")
    image_d = models.FileField(upload_to='mod/', verbose_name="Изображение")
    description_d = models.TextField(verbose_name="Описание")
    char1_key_d = models.TextField(verbose_name="Характеристика 1 ключ")
    char1_value_d = models.TextField(verbose_name="Характеристика 1 значение")
    char2_key_d = models.TextField(verbose_name="Характеристика 2 ключ")
    char2_value_d = models.TextField(verbose_name="Характеристика 2 значение")
    char3_key_d = models.TextField(verbose_name="Характеристика 3 ключ")
    char3_value_d = models.TextField(verbose_name="Характеристика 3 значение")
    char4_key_d = models.TextField(verbose_name="Характеристика 4 ключ")
    char4_value_d = models.TextField(verbose_name="Характеристика 4 значение")
    available_d = models.TextField(verbose_name="Наличие")
    discount_d = models.TextField(verbose_name="Скидка")
    body_guarantee_d = models.TextField(verbose_name="Гарантия на корпус")
    installation_guarantee_d = models.TextField(verbose_name="Гарантия на монтаж")
    price_new_d = models.TextField(verbose_name="Новая цена")
    price_old_d = models.TextField(verbose_name="Старая цена")

    class Meta:
        verbose_name = "10 Модели"
        verbose_name_plural = "10 Модели"

    def __str__(self):
        return "Контент для моделей"

class Catalog(models.Model):
    image_bg_desktop = models.FileField(upload_to='catalog/', verbose_name="Изображение фона desktop")
    image_bg_mobile = models.FileField(upload_to='catalog/', verbose_name="Изображение фона mobile")
    title = models.TextField(verbose_name="Заголовок")
    title_h2 = models.TextField(verbose_name="Заголовок h2")
    update = models.TextField(verbose_name="Update")
    btn_wa = models.TextField(verbose_name="Кнопка wa")
    wa_text = models.TextField(verbose_name="Текст wa")
    tg_text = models.TextField(verbose_name="Текст tg")
    btn = models.TextField(verbose_name="Кнопка")
    politic = models.TextField(verbose_name="Политика конфиденциальности")

    class Meta:
        verbose_name = "11 Каталог"
        verbose_name_plural = "11 Каталог"

class Budget(models.Model):
    title_h2 = models.TextField(verbose_name="Заголовок h2")
    title = models.TextField(verbose_name="Заголовок")
    swipe_text = models.TextField(verbose_name="Swipe текст")
    img_1 = models.FileField(upload_to='budget/', verbose_name="Бюджет 1 изображение")
    title_1 = models.TextField(verbose_name="Бюджет 1 заголовок")
    btn_1 = models.TextField(verbose_name="Бюджет 1 кнопка")
    img_2 = models.FileField(upload_to='budget/', verbose_name="Бюджет 2 изображение")
    title_2 = models.TextField(verbose_name="Бюджет 2 заголовок")
    btn_2 = models.TextField(verbose_name="Бюджет 2 кнопка")
    img_3 = models.FileField(upload_to='budget/', verbose_name="Бюджет 3 изображение")
    title_3 = models.TextField(verbose_name="Бюджет 3 заголовок")
    btn_3 = models.TextField(verbose_name="Бюджет 3 кнопка")
    img_4 = models.FileField(upload_to='budget/', verbose_name="Бюджет 4 изображение")
    title_4 = models.TextField(verbose_name="Бюджет 4 заголовок")
    btn_4 = models.TextField(verbose_name="Бюджет 4 кнопка")

    class Meta:
        verbose_name = "12 Бюджет"
        verbose_name_plural = "12 Бюджет"

class Guarantees(models.Model):
    bg_1 = models.FileField(upload_to='guarantees/', verbose_name="Фон 1 изображение")
    number = models.FileField(upload_to='guarantees/', verbose_name="Число")
    text = models.TextField(verbose_name="Текст")
    bg_2 = models.FileField(upload_to='guarantees/', verbose_name="Фон 2 изображение")
    mobile = models.FileField(upload_to='guarantees/', verbose_name="Mobile изображение")
    h2 = models.TextField(verbose_name="Текст h2")

    class Meta:
        verbose_name = "13 Гарантии"
        verbose_name_plural = "13 Гарантии"

class More(models.Model):
    text1 = models.TextField(verbose_name="Текст 1")
    block1_title = models.TextField(verbose_name="Блок 1 заголовок")
    block1_text = models.TextField(verbose_name="Блок 1 текст")
    block2_title = models.TextField(verbose_name="Блок 2 заголовок")
    block2_text = models.TextField(verbose_name="Блок 2 текст")
    block3_title = models.TextField(verbose_name="Блок 3 заголовок")
    block3_text = models.TextField(verbose_name="Блок 3 текст")
    block4_title = models.TextField(verbose_name="Блок 4 заголовок")
    block4_text = models.TextField(verbose_name="Блок 4 текст")
    block5_title = models.TextField(verbose_name="Блок 5 заголовок")
    block5_text = models.TextField(verbose_name="Блок 5 текст")
    block6_title = models.TextField(verbose_name="Блок 6 заголовок")
    block6_text = models.TextField(verbose_name="Блок 6 текст")
    footer_img = models.FileField(upload_to='more/', verbose_name="Футер изображение")
    footer_text = models.TextField(verbose_name="Футер текст")

    class Meta:
        verbose_name = "14 Подробнее"
        verbose_name_plural = "14 Подробнее"

class Portfolio(models.Model):
    header_text = models.TextField(verbose_name="Текст шапки")
    swipe_text = models.TextField(verbose_name="Swipe текст")
    block1_img_main = models.FileField(upload_to='portfolio/', verbose_name="Блок 1 изображение главное")
    block1_img2 = models.FileField(upload_to='portfolio/', verbose_name="Блок 1 изображение 2")
    block1_img3 = models.FileField(upload_to='portfolio/', verbose_name="Блок 1 изображение 3")
    block1_img4 = models.FileField(upload_to='portfolio/', verbose_name="Блок 1 изображение 4")
    block1_img5 = models.FileField(upload_to='portfolio/', verbose_name="Блок 1 изображение 5")
    block1_title = models.TextField(verbose_name="Блок 1 заголовок")
    block1_address = models.TextField(verbose_name="Блок 1 адрес")
    block2_img_main = models.FileField(upload_to='portfolio/', verbose_name="Блок 2 изображение главное")
    block2_img2 = models.FileField(upload_to='portfolio/', verbose_name="Блок 2 изображение 2")
    block2_img3 = models.FileField(upload_to='portfolio/', verbose_name="Блок 2 изображение 3")
    block2_img4 = models.FileField(upload_to='portfolio/', verbose_name="Блок 2 изображение 4")
    block2_img5 = models.FileField(upload_to='portfolio/', verbose_name="Блок 2 изображение 5")
    block2_title = models.TextField(verbose_name="Блок 2 заголовок")
    block2_address = models.TextField(verbose_name="Блок 2 адрес")
    block3_img_main = models.FileField(upload_to='portfolio/', verbose_name="Блок 3 изображение главное")
    block3_img2 = models.FileField(upload_to='portfolio/', verbose_name="Блок 3 изображение 2")
    block3_img3 = models.FileField(upload_to='portfolio/', verbose_name="Блок 3 изображение 3")
    block3_img4 = models.FileField(upload_to='portfolio/', verbose_name="Блок 3 изображение 4")
    block3_img5 = models.FileField(upload_to='portfolio/', verbose_name="Блок 3 изображение 5")
    block3_title = models.TextField(verbose_name="Блок 3 заголовок")
    block3_address = models.TextField(verbose_name="Блок 3 адрес")
    block4_img_main = models.FileField(upload_to='portfolio/', verbose_name="Блок 4 изображение главное")
    block4_img2 = models.FileField(upload_to='portfolio/', verbose_name="Блок 4 изображение 2")
    block4_img3 = models.FileField(upload_to='portfolio/', verbose_name="Блок 4 изображение 3")
    block4_img4 = models.FileField(upload_to='portfolio/', verbose_name="Блок 4 изображение 4")
    block4_img5 = models.FileField(upload_to='portfolio/', verbose_name="Блок 4 изображение 5")
    block4_title = models.TextField(verbose_name="Блок 4 заголовок")
    block4_address = models.TextField(verbose_name="Блок 4 адрес")
    block5_img_main = models.FileField(upload_to='portfolio/', verbose_name="Блок 5 изображение главное")
    block5_img2 = models.FileField(upload_to='portfolio/', verbose_name="Блок 5 изображение 2")
    block5_img3 = models.FileField(upload_to='portfolio/', verbose_name="Блок 5 изображение 3")
    block5_img4 = models.FileField(upload_to='portfolio/', verbose_name="Блок 5 изображение 4")
    block5_img5 = models.FileField(upload_to='portfolio/', verbose_name="Блок 5 изображение 5")
    block5_title = models.TextField(verbose_name="Блок 5 заголовок")
    block5_address = models.TextField(verbose_name="Блок 5 адрес")

    class Meta:
        verbose_name = "15 Портфолио"
        verbose_name_plural = "15 Портфолио"

class Video(models.Model):
    header_text = models.TextField(verbose_name="Текст шапки")
    youtube_link1 = models.URLField(verbose_name="Ссылка youtube 1")
    youtube_link2 = models.URLField(verbose_name="Ссылка youtube 2")
    text = models.TextField(verbose_name="Текст")
    swipe_text = models.TextField(verbose_name="Swipe текст")
    youtube_shorts = models.URLField(verbose_name="Ссылка youtube shorts")
    img = models.FileField(upload_to='video/', verbose_name="Изображение")

    class Meta:
        verbose_name = "16 Видео"
        verbose_name_plural = "16 Видео"

class Reviews(models.Model):
    bg = models.FileField(upload_to='reviews/', verbose_name="Фон")
    header_text = models.TextField(verbose_name="Текст шапки")
    img1 = models.FileField(upload_to='reviews/', verbose_name="Изображение 1")
    img2 = models.FileField(upload_to='reviews/', verbose_name="Изображение 2")
    img3 = models.FileField(upload_to='reviews/', verbose_name="Изображение 3")
    img4 = models.FileField(upload_to='reviews/', verbose_name="Изображение 4")
    img5 = models.FileField(upload_to='reviews/', verbose_name="Изображение 5")
    img6 = models.FileField(upload_to='reviews/', verbose_name="Изображение 6")
    img7 = models.FileField(upload_to='reviews/', verbose_name="Изображение 7")
    rate = models.TextField(verbose_name="Рейтинг")
    text = models.TextField(verbose_name="Текст")
    ya_map_link = models.URLField(verbose_name="Ссылка на yandex карту")
    text2 = models.TextField(verbose_name="Текст 2")
    bg2 = models.FileField(upload_to='reviews/', verbose_name="Фон 2")
    bg_mobile = models.FileField(upload_to='reviews/', verbose_name="Фон mobile")
    header_text2 = models.TextField(verbose_name="Текст шапки 2")
    subtitle_text = models.TextField(verbose_name="Текст подзаголовок")
    text3 = models.TextField(verbose_name="Текст 3")
    wa_link = models.URLField(verbose_name="Ссылка на whatsapp")
    text4 = models.TextField(verbose_name="Текст 4")

    class Meta:
        verbose_name = "17 Отзывы"
        verbose_name_plural = "17 Отзывы"

class Install(models.Model):
    bg = models.FileField(upload_to='install/', verbose_name="Фон")
    bg_mobile = models.FileField(upload_to='install/', verbose_name="Фон mobile")
    header_text = models.TextField(verbose_name="Текст шапки")
    subtitle = models.TextField(verbose_name="Подзаголовок")
    swipe_text = models.TextField(verbose_name="Swipe текст")
    img1 = models.FileField(upload_to='install/', verbose_name="Изображение 1")
    text1 = models.TextField(verbose_name="Текст 1")
    img2 = models.FileField(upload_to='install/', verbose_name="Изображение 2")
    text2 = models.TextField(verbose_name="Текст 2")
    img3 = models.FileField(upload_to='install/', verbose_name="Изображение 3")
    text3 = models.TextField(verbose_name="Текст 3")
    img4 = models.FileField(upload_to='install/', verbose_name="Изображение 4")
    text4 = models.TextField(verbose_name="Текст 4")
    img5 = models.FileField(upload_to='install/', verbose_name="Изображение 5")
    text5 = models.TextField(verbose_name="Текст 5")
    img6 = models.FileField(upload_to='install/', verbose_name="Изображение 6")
    text6 = models.TextField(verbose_name="Текст 6")
    title_right1 = models.TextField(verbose_name="Заголовок справа 1")
    text_right1 = models.TextField(verbose_name="Текст справа 1")
    title_right2 = models.TextField(verbose_name="Заголовок справа 2")
    text_right2 = models.TextField(verbose_name="Текст справа 2")

    class Meta:
        verbose_name = "18 Установка"
        verbose_name_plural = "18 Установка"

class Numbers(models.Model):
    title1 = models.TextField(verbose_name="Заголовок 1")
    text1 = models.TextField(verbose_name="Текст 1")
    title2 = models.TextField(verbose_name="Заголовок 2")
    text2 = models.TextField(verbose_name="Текст 2")
    title3 = models.TextField(verbose_name="Заголовок 3")
    text3 = models.TextField(verbose_name="Текст 3")
    title4 = models.TextField(verbose_name="Заголовок 4")
    text4 = models.TextField(verbose_name="Текст 4")
    montage_img1 = models.FileField(upload_to='numbers/', verbose_name="Изображение 1")
    montage_header1 = models.TextField(verbose_name="Header 1")
    montage_number1 = models.TextField(verbose_name="Номер 1")
    montage_text1 = models.TextField(verbose_name="Текст 1")
    montage_img2 = models.FileField(upload_to='numbers/', verbose_name="Изображение 2")
    montage_header2 = models.TextField(verbose_name="Header 2")
    montage_number2 = models.TextField(verbose_name="Номер 2")
    montage_text2 = models.TextField(verbose_name="Текст 2")
    montage_img3 = models.FileField(upload_to='numbers/', verbose_name="Изображение 3")
    montage_header3 = models.TextField(verbose_name="Header 3")
    montage_number3 = models.TextField(verbose_name="Номер 3")
    montage_text3 = models.TextField(verbose_name="Текст 3")
    montage_img4 = models.FileField(upload_to='numbers/', verbose_name="Изображение 4")
    montage_header4 = models.TextField(verbose_name="Header 4")
    montage_number4 = models.TextField(verbose_name="Номер 4")
    montage_text4 = models.TextField(verbose_name="Текст 4")
    montage_img5 = models.FileField(upload_to='numbers/', verbose_name="Изображение 5")
    montage_header5 = models.TextField(verbose_name="Header 5")
    montage_number5 = models.TextField(verbose_name="Номер 5")
    montage_text5 = models.TextField(verbose_name="Текст 5")

    class Meta:
        verbose_name = "19 Цифры"
        verbose_name_plural = "19 Цифры"

class Quality(models.Model):
    bg = models.FileField(upload_to='quality/', verbose_name="Фон")
    header_text = models.TextField(verbose_name="Текст шапки")
    swipe_text = models.TextField(verbose_name="Swipe текст")
    number1 = models.TextField(verbose_name="Номер 1")
    title1 = models.TextField(verbose_name="Заголовок 1")
    text1_1 = models.TextField(verbose_name="Текст 1_1")
    text1_2 = models.TextField(verbose_name="Текст 1_2")
    title2 = models.TextField(verbose_name="Заголовок 2")
    text2_1 = models.TextField(verbose_name="Текст 2_1")
    text2_2 = models.TextField(verbose_name="Текст 2_2")
    title3 = models.TextField(verbose_name="Заголовок 3")
    text3_1 = models.TextField(verbose_name="Текст 3_1")
    text3_2 = models.TextField(verbose_name="Текст 3_2")
    bg2 = models.FileField(upload_to='quality/', verbose_name="Фон 2")
    bg_mobile = models.FileField(upload_to='quality/', verbose_name="Фон mobile")
    report_header = models.TextField(verbose_name="Текст шапки")
    report_text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "20 Качество"
        verbose_name_plural = "20 Качество"

class Faq(models.Model):
    header_text = models.TextField(verbose_name="Текст шапки")
    question1 = models.TextField(verbose_name="Вопрос 1")
    answer1 = models.TextField(verbose_name="Ответ 1")
    question2 = models.TextField(verbose_name="Вопрос 2")
    answer2 = models.TextField(verbose_name="Ответ 2")
    question3 = models.TextField(verbose_name="Вопрос 3")
    answer3 = models.TextField(verbose_name="Ответ 3")
    question4 = models.TextField(verbose_name="Вопрос 4")
    answer4 = models.TextField(verbose_name="Ответ 4")
    question5 = models.TextField(verbose_name="Вопрос 5")
    answer5 = models.TextField(verbose_name="Ответ 5")
    question6 = models.TextField(verbose_name="Вопрос 6")
    answer6 = models.TextField(verbose_name="Ответ 6")
    question7 = models.TextField(verbose_name="Вопрос 7")
    answer7 = models.TextField(verbose_name="Ответ 7")
    question8 = models.TextField(verbose_name="Вопрос 8")
    answer8 = models.TextField(verbose_name="Ответ 8")
    question9 = models.TextField(verbose_name="Вопрос 9")
    answer9 = models.TextField(verbose_name="Ответ 9")
    question10 = models.TextField(verbose_name="Вопрос 10")
    answer10 = models.TextField(verbose_name="Ответ 10")
    wa_link = models.URLField(verbose_name="Ссылка на whatsapp")
    wa_text = models.TextField(verbose_name="Текст whatsapp")

    class Meta:
        verbose_name = "21 Вопрос-ответ"
        verbose_name_plural = "21 Вопрос-ответ"

class Requisition(models.Model):
    header_text = models.TextField(verbose_name="Текст шапки")
    title = models.TextField(verbose_name="Заголовок")
    bg= models.FileField(upload_to='requisition/', verbose_name="Фон")
    bg_mobile = models.FileField(upload_to='requisition/', verbose_name="Фон mobile")
    title2 = models.TextField(verbose_name="Заголовок 2")
    text1 = models.TextField(verbose_name="Текст 1")
    text2 = models.TextField(verbose_name="Текст 2")
    text3 = models.TextField(verbose_name="Текст 3")
    text4 = models.TextField(verbose_name="Текст 4")
    text5 = models.TextField(verbose_name="Текст 5")
    text6 = models.TextField(verbose_name="Текст 6")
    title3 = models.TextField(verbose_name="Заголовок 3")
    btn = models.TextField(verbose_name="Кнопка текст")
    text7 = models.TextField(verbose_name="Текст 7")
    text8 = models.TextField(verbose_name="Текст 8")
    text9 = models.TextField(verbose_name="Текст 9")

    class Meta:
        verbose_name = "22 Заявка"
        verbose_name_plural = "22 Заявка"

class Contacts(models.Model):
    header_text = models.TextField(verbose_name="Текст шапки")
    title = models.TextField(verbose_name="Заголовок")
    ya_map_link = models.URLField(verbose_name="Ссылка на yandex карту")
    address = models.TextField(verbose_name="Адрес")
    title2 = models.TextField(verbose_name="Заголовок 2")
    phone_link = models.TextField(verbose_name="Ссылка на телефон")
    phone = models.TextField(verbose_name="Телефон")
    wa_link = models.URLField(verbose_name="Ссылка на whatsapp")
    tg_link = models.URLField(verbose_name="Ссылка на telegram")
    vk_link = models.URLField(verbose_name="Ссылка на vk")
    title3 = models.TextField(verbose_name="Заголовок 3")
    email_link = models.TextField(verbose_name="Ссылка email")
    email_text = models.TextField(verbose_name="Текст email")
    title4 = models.TextField(verbose_name="Заголовок 4")
    text = models.TextField(verbose_name="Текст")
    title5 = models.TextField(verbose_name="Заголовок 5")
    swipe_text = models.TextField(verbose_name="Swipe text")
    slider1_img1= models.FileField(upload_to='contacts/', verbose_name="Слайдер 1 изображение 1")
    slider1_text1 = models.TextField(verbose_name="Слайдер 1 текст 1")
    slider1_img2 = models.FileField(upload_to='contacts/', verbose_name="Слайдер 1 изображение 2")
    slider1_text2 = models.TextField(verbose_name="Слайдер 1 текст 2")
    slider1_img3 = models.FileField(upload_to='contacts/', verbose_name="Слайдер 1 изображение 3")
    slider1_text3 = models.TextField(verbose_name="Слайдер 1 текст 3")
    slider2_img1 = models.FileField(upload_to='contacts/', verbose_name="Слайдер 2 изображение 1")
    slider2_text1 = models.TextField(verbose_name="Слайдер 2 текст 1")
    slider2_img2 = models.FileField(upload_to='contacts/', verbose_name="Слайдер 2 изображение 2")
    slider2_text2 = models.TextField(verbose_name="Слайдер 2 текст 2")
    title6 = models.TextField(verbose_name="Заголовок 6")
    yandex_map = models.TextField(verbose_name="Яндекс карта")

    class Meta:
        verbose_name = "23 Контакты"
        verbose_name_plural = "23 Контакты"

class Footer(models.Model):
    logo_link = models.TextField(verbose_name="Ссылка на логотипе")
    logo_img = models.FileField(upload_to='footer/', verbose_name="Логотип изображение")
    text1 = models.TextField(verbose_name="Текст 1")
    text2 = models.TextField(verbose_name="Текст 2")
    text3 = models.TextField(verbose_name="Текст 3")

    class Meta:
        verbose_name = "24 Футер"
        verbose_name_plural = "24 Футер"

class PopupRequest(models.Model):
    bg = models.FileField(upload_to='popup_request/', verbose_name="Фон")
    title = models.TextField(verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    btn = models.TextField(verbose_name="Кнопка")
    text2 = models.TextField(verbose_name="Текст 2")

    class Meta:
        verbose_name = "25 Всплывающее окно заявка"
        verbose_name_plural = "25 Всплывающее окно заявка"

class PopupStock(models.Model):
    bg = models.FileField(upload_to='popup_stock/', verbose_name="Фон")
    header = models.TextField(verbose_name="Текст в шапке")
    title = models.TextField(verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    btn = models.TextField(verbose_name="Кнопка")
    text2 = models.TextField(verbose_name="Текст 2")

    class Meta:
        verbose_name = "26 Всплывающее окно акции"
        verbose_name_plural = "26 Всплывающее окно акции"

class PopupPolitic(models.Model):
    full_text = models.TextField(verbose_name="Текст полностью")

    class Meta:
        verbose_name = "27 Всплывающее окно политика"
        verbose_name_plural = "27 Всплывающее окно политика"

class PopupLeave(models.Model):
    bg = models.FileField(upload_to='popup_leave/', verbose_name="Фон")
    header = models.TextField(verbose_name="Текст в шапке")
    text = models.TextField(verbose_name="Текст")
    title = models.TextField(verbose_name="Заголовок")
    text2 = models.TextField(verbose_name="Текст 2")
    btn = models.TextField(verbose_name="Кнопка")
    wa_text = models.TextField(verbose_name="Whatsapp")
    tg_text = models.TextField(verbose_name="Telegram")
    btn2 = models.TextField(verbose_name="Кнопка 2")
    text3 = models.TextField(verbose_name="Текст 3")

    class Meta:
        verbose_name = "28 Всплывающее окно подождите"
        verbose_name_plural = "28 Всплывающее окно подождите"