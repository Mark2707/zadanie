# Программа рассчитывает сколько будет стоить поездка в такси

# Константы
price = 0
coef_dem = 1
hend_price = 60
folks_price = 70
oct_price = 120
jet_price = 130
camr_price = 250
son_price = 230

# Программа узнает детали поездки
klass = input('На какой категории такси Вы планируете поездку?'
              ' (эконом, комфорт, бизнес)\n').lower().strip()
km = float(input('Сколько километров Вам нужно проехать?\n'))
time, m = map(int, input('Во сколько Вы планируете поездку?\n').split(':'))

# Программа анализирует время поездки для получения значения коэффицента спроса
if 8 <= time <= 10 or 17 < time < 20:
    coef_dem = 2
    print('Высокий спрос')
if 12 <= time <= 14:
    coef_dem = 1.5
    print('Высокий спрос')

# Клиент выбирает машину для поездки в тарифе 'эконом'
if klass == 'эконом':
    car_econ = input('На какой машине Вы предпочтете поездку?'
                     ' (Х. Солярис, Ф. Поло)\n').lower().strip()
    # Рассчет стоимости поездки
    if car_econ == 'х. солярис':
        price = round(coef_dem * hend_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')
    elif car_econ == 'ф. поло':
        price = round(coef_dem * folks_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')
# Клиент выбирает машину для поездки в тарифе 'комфорт'
elif klass == 'комфорт':
    car_comf = input('На какой машине Вы предпочтете поездку?'
                     ' (Ш. Октавия, Ф. Джетта)\n').lower().strip()
    # Рассчет стоимости поездки
    if car_comf == 'ш. октавия':
        price = round(coef_dem * oct_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')
    elif car_comf == 'ф. джетта':
        price = round(coef_dem * jet_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')
# Клиент выбирает машину для поездки в тарифе 'бизнес'
elif klass == 'бизнес':
    car_biz = input('На какой машине Вы предпочтете поездку?'
                    ' (Т. Камри, Х. Соната)\n').lower().strip()
    # Рассчет стоимости поездки
    if car_biz == 'т. камри':
        price = round(coef_dem * camr_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')
    elif car_biz == 'х. соната':
        price = round(coef_dem * son_price * km, 2)
        print('Цена поездки составит:', price, 'руб.')