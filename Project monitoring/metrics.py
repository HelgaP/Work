
def tight_lines_evaluator(project, all_lines, finished_projects):

    tight_lines = len(finished_projects.loc[(finished_projects['Название проекта'] == project) & (finished_projects['Контрактная дата отгрузки'] > finished_projects['Желаемая дата отгрузки'])].drop_duplicates(subset='Заказ клиента&Id строки EDI'))
    percent = round(tight_lines/all_lines*100)
    print(percent)

    if percent < 10:
        return 0
    elif 10 <= percent < 40:
        return 1
    elif 40 <= percent < 70:
        return 2
    else:
        return 3

def rare_refs_evaluator(project, all_lines, finished_projects):

    rare_groups = ['AR', 'BR', 'CF', 'CM', 'CR']
    rare_refs = len(finished_projects.loc[(finished_projects['Category'].isin(rare_groups)) & (finished_projects['Название проекта'] == project)].drop_duplicates(subset='Заказ клиента&Id строки EDI'))

    percent = round(rare_refs/all_lines*100)

    if percent < 10: return 0
    elif 10 <= percent < 40: return 1
    elif 40 <= percent < 70: return 2
    else: return 3

def el_orders_evaluator(project, all_lines, finished_projects):

    el_orders = len(finished_projects.loc[(finished_projects['Название проекта'] == project) & (finished_projects['Amu'] > finished_projects['Количество'])].drop_duplicates(subset='Заказ клиента&Id строки EDI'))
    percent = round(el_orders/all_lines*100)

    if percent < 10: return 0
    elif 10 <= percent < 40: return 1
    elif 40 <= percent < 70: return 2
    else: return 3

def lines_qty_evaluator(lines):

    if lines < 100: return 0
    elif 100 <= lines < 500: return 1
    else: return 2

def define_category(points):
    if points <= 6: return 'A'
    elif 7 <= points <= 13: return 'B'
    else: return 'C'

def suppliers_evaluator(qty):

    if qty == 1: return 0
    elif 2 <= qty <= 3: return 1
    else: return 2

def whs_evaluator(whs):

    if 'RU01-4000' in whs or 'RU06-4000' in whs:
        if 'RU01-5600' in whs or 'RU01-5602' in whs:
            if 'RU01-5600' in whs and 'RU01-5602' in whs:
                return 2
            return 1
        return 0
    else:
        return 3