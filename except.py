import pandas as pd
class DF_excepts:
    def __init__(self):
        try:
            self.df = pd.read_csv('var3.csv')
        except FileNotFoundError:
            print("Файл var3.csv отсутсвуют либо назавн иначе")
        except pd.errors.EmptyDataError:
            print("Файл var3.csv пуст")
        except pd.errors.ParserError:
            print("Файл var3.csv не соответствует структуре csv")
        
    def full_chek(self):
        self.column_names = self.df.columns.values
        self.column_example = ('Участники граждкого оборота' 'Тип операции' 'Сумма операции'
 'Вид расчета' 'Место оплаты' 'Терминал оплаты' 'Дата оплаты'
 'Время оплаты' 'Результат операции' 'Cash-back' 'Сумма cash-back')
        if self.column_names[0] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[1] != 'Тип операции':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[2] != 'Сумма операции':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[3] != 'Вид расчета':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[4] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[5] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[6] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[7] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[8] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[9] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')
        
        if self.column_names[10] != 'Участники гражданского оборота':
            print("Назвния столбцов не совпадают с ожидаемыми")
            print("Фактические названия",self.column_names)
            print("Ожидаемые названия",self.column_example)
            raise IndexError(f'Структура датафрейма var3.csv не соответсвует ожидаемой')

    def __del__(self):
        pass
