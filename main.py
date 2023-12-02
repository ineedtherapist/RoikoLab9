import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["library"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
collection = db["books"]

# Додавання документів (еквівалент записів в таблиці)
data1 = {"Назва книжки": "Відьмак", "Автор": "Анджей Сапковській", "Арендував": "Віктор"}
data2 = {"Назва книжки": "Гра престолів", "Автор": "Джордж Мартін", "Арендував": "Антон"}
data3 = {"Назва книжки": "Володар Перстнів", "Автор": "Джон Р.Р. Толкін", "Арендував": "Леонід"}

# Вставка документів
inserted_data1 = collection.insert_one(data1)
inserted_data2 = collection.insert_one(data2)
inserted_data3 = collection.insert_one(data3)

# Видалення документа
delete_query = {"Назва книжки": "Володар Перстнів"}
collection.delete_one(delete_query)

#Пошук документа
search_query = {"Назва книжки": "Гра престолів"}
print("Знайдено книжку:")
for document in collection.find(search_query):
    print(document)

# Оновлення документа
query = {"Назва книжки": "Відьмак"}
new_data = {"$set": {"Арендував": "Назар"}}
collection.update_one(query, new_data)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in collection.find():
    print(document)

# Закриття підключення
client.close()