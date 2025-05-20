import pandas as pd
from pandas.errors import EmptyDataError

class Processing:

    def __init__(self, name, name2, name3): 
        self.name = name
        self.name2 = name2
        self.name3 = name3
     
    def data(self):
        try:
            df = pd.read_csv(self.name3)
            print(f"Файл {self.name3} успешно загружен.")
            return df
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")
        except EmptyDataError:
            print(f"Файл {self.name3} пуст. Нет данных для загрузки.")

    def open(self): 
        try:
            df = pd.read_csv(self.name2)
            print(f"Файл {self.name2} успешно загружен.")
            return df
        except EmptyDataError:
            print(f"Возникла следующая ошибка: Датафрейм {self.name2} пуст.")
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")

    def false(self):
        df1 = pd.read_csv(self.name3)
        df2 = pd.read_csv(self.name2)
        
        res1 = list(df1.columns)
        res2 = list(df2.columns)

        if res1 == res2:
            print("Чтение датафрейма завершено успешно. Структура совпадает.") 
        else:
            print("Структура датафрейма не соответствует ожидаемой:")
            print(f"- Названия столбцов не совпадают")
            print(f"Ожидаемые: {res1}")
            print(f"Фактические: {res2}")
            
            common_columns = df1.columns.intersection(df2.columns)

            for col in common_columns:
                dtype1 = df1[col].dtype
                dtype2 = df2[col].dtype
                if dtype1 != dtype2:
                    print(f"- в столбце '{col}' тип данных не соответствует ожидаемому.")
                    print(f"Ожидается: {dtype1}, Фактически: {dtype2}")

            print("Проверка завершена.")

def main():
    file_path = "var.csv"
    file_path2 = "var1.csv"
    file_path3 = "var3.csv"
    processor = Processing(file_path, file_path2, file_path3)
    df3 = processor.data()
    df2 = processor.open()
    
    if df3 is not None and df2 is not None:
        processor.false()

if __name__ == "__main__":
    main()