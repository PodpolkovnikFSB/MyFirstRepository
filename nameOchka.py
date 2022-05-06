# Анюта -> АнютОчка
# Алина -> АлинОчка
# Оливия -> ОливОчка

def ochka(name):
    glasnye = 'ёуеыаоэяию'
    list_name = list(name)
    while list_name[-1] in glasnye:
        list_name.pop(-1)
    return ''.join(list_name) + 'Очка'
