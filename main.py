
# task 1
cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    for l in file:
        recipe_name = l.strip()
        rec = {'name': recipe_name, 'ingredients': []}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            rec['ingredients'].append({'ingredient_name': ingredient_name,
                                       'quantity': int(quantity),
                                       'measure': measure})
        blank_line = file.readline()
        cook_book[recipe_name] = rec['ingredients']
print(cook_book)


# task 2
def get_shop_list_by_dishes(dishes, person_count): # Функция принимает в себя лист с названиями блюд и количество персон
    shop_list = {} # Создаём словарь - список продуктов
    for dish in dishes: # Проходимся по переданным блюдам
        for ing in cook_book[dish]: # Проходимся по ингредиентам каждого блюда
            mult_quantity = ing['quantity'] * person_count # Увеличиваем количество ингредиентов для соответствия кол-ву персон

            includes = False # Тут будем смотреть, был ли уже такой ингредиент до этого, поэтому создаём переменную - флаг для индикации
            for entry in shop_list: # Проходимся по уже выписанным ингредиентам
                if entry == ing['ingredient_name']: # Если текущий ингредиент совпадает с каким-либо уже имеющимся, прибавляем к выписанному дополнительное кол-во
                    shop_list[entry]['quantity'] += mult_quantity
                    includes = True # Ставим флаг true, чтобы знать, что этот ингредиент мы уже записали
                    break # Выходим, потому что точно знаем, что больше повторов быть не может

            if not includes: # Если не нашли вхождения, записываем новый ингредиент
                shop_list[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': mult_quantity}

    return shop_list # Возвращаем список

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)


# task 3
def combine(files, combined='combined.txt'): # Функция принимает лист с названиями файлов и название конечного файла, по-умолчанию combined.txt
    contains = [] # Лист для хранения внутренностей всех файлов, откуда мы позже будем выписывать всё в новый
    for f in files: # Проходимся по каждому названию
        lines = open(f, encoding='utf-8').read().splitlines() # Открываем файл, читаем его как единую строку и далее делим, чтобы в строках не было '\n', которые возникают при использовании readlines()
        contains.append({'title': f, 'length': len(lines), 'lines': lines}) # Записываем информацию о файле

    contains = sorted(contains, key=lambda d: d['length']) # Сортируем лист по количеству строк

    fw = open(combined, 'w', encoding='utf-8') # Открываем файл на запись
    for f in contains: # Проходимся по всем записанным файлам
        fw.write(f['title'] + '\n') # Пишем Название файла

        fw.write(str(f['length']) + '\n') # Пишем длину файла

        for line in f['lines']:
            fw.write(line + '\n') # Записываем каждую строку файла

combine(['1.txt', '2.txt']) # Вызываем для файлов 1.txt и 2.txt






