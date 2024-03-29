LEXICON: dict[str, str] = {
    '/start': 'Откуда будем собирать конкурентов? 😎',
    '/help': 'Это бот, для сбора конкурентов в Яндексе\n\n'
             '<u>Доступные команды:</u>\n'
             '/start - запуск сбора конкурентов по вашему ключевому слову\n'
             '/help - краткая инструкция к боту\n'
             '/help_region - помощь по локациям\n\n'
             'Для того, чтобы узнать ваших конкурентов, пройдите 4 простых шага:\n'
             '1. Выберите необходимые данные (Реклама, SEO или Реклама + SEO)\n'
             '2. Введите ключевое слово, по которому искать конкурентов (например: купить забор)\n'
             '3. Укажите регион или город, в котором собираем конкурентов (например: Вологда)\n'
             '4. Скачайте файл в формате xlsx, где будет находиться список ваших конкурентов.\n\n'
             'Важно: Бот собирает информацию в режиме инкогнито. Бот собирает информацию с поиска Яндекса.',
    '/help_region': 'Воспользуйтесь базой регионов ⬇',
    'channel_left': 'Сервис доступен для подписчиков канала\n'
                    '<a href="t.me/ppc_expert_1">КОНТЕКСТНАЯ РЕКЛАМА</a>\n'
                    'Этот сервис собирает информацию о ваших конкурентах в контекстной рекламе Яндекс Директа и '
                    'органической выдаче (SEO) Яндекса. Бот умеет собирать сайты конкурентов, объявления конкурентов '
                    'на поиске. Узнайте ваших конкурентов меньше чем за 1 минуту, без регистраций и оплаты.',
    '^collect^': 'Введите ключевую фразу, по которой будем собирать конкурентов\n'
                 'Перед фразой необходимо поставить знак вопроса, <u>например:</u>\n'
                 '<b>? заборы для дачи</b>',
    'region': 'Укажите город, область или регион для сбора конкурентов.\n\n'
              '<code>Например город:\n'
              'Москва\n'
              'Екатеринбург\n'
              'Астрахань\n\n'
              'Например область:\n'
              'Москва и область\n'
              'Ленинградская область\n'
              'Псковская область\n\n'
              'Например регион:\n'
              'Центр\n'
              'Поволжье\n'
              'Сибирь\n\n</code>'
              'Названия локаций соответствуют локациям Яндекс вордстата. Если вы не знаете, как указать нужную локацию, '
              'загляните в меню бота в раздел помощь по локациям',
    'wait': 'Ожидайте, ваш запрос обрабатывается',
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Узнать конкурентов',
    '/help': 'Помощь',
    '/help_region': 'Помощь по локациям'
}
