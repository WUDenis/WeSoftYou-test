'''
    Перебрать ниже приведенную структуру до тех пор, пока ключу 'boxes' будет соответствовать числовое значение.  
    Вывести достигнутый уровень вложенности в виде целого числа.
'''
boxes = [
    {
        'boxes': [
            {
                'boxes': [
                    {
                        'boxes': 42
                    },
                ],
            }, 
            {},
        ],
    },
]