def ochka(name):
    glasnye = 'ёуеыаоэяию'
    take_o = 'уеыао'
    list_name = list(name)
    while list_name[-1] in glasnye:
        list_name.pop(-1)
    return ''.join(list_name) + ('Очка' if name[-1] in take_o else 'Ечка')
