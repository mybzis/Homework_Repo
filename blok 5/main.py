# -*- coding: utf-8 -*-

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_owner_by_document_number(documents, doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return f"Владелец документа: {document['name']}"
    return "Документ не найден в базе"

def find_shelf_by_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return f"Книга находится на полке: {shelf}"
    return "Документ не найден в базе"

def show_all():
  # Выводим полную информацию по всем документам
  for document in documents:
      doc_number = document['number']
      doc_type = document['type']
      doc_owner = document['name']
      shelf = ""
      for shelf_number, docs in directories.items():
          if doc_number in docs:
              shelf = shelf_number
              break
      print(f"№: {doc_number}, тип: {doc_type}, владелец: {doc_owner}, полка хранения: {shelf}")
  
def add_shelf():
  shelf_number = input("Введите номер полки: ")
  if shelf_number in directories:
      print(f"Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())}")
  else:
      directories[shelf_number] = []
      print(f"Полка добавлена. Текущий перечень полок: {', '.join(directories.keys())}")

def delete_shelf():
  shelf_number = input("Введите номер полки: ")

  # Проверяем, существует ли полка
  if shelf_number not in directories:
      print(f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}")
      return

  # Проверяем, пустая ли полка
  if directories[shelf_number]:
      print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {', '.join(directories.keys())}")
  else:
      del directories[shelf_number]
      print(f"Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}")


while True:
    user_input = input("Введите команду: ")
    if user_input == "p":
        doc_number = input("Введите номер документа: ")
        result = find_owner_by_document_number(documents, doc_number)
        print(result)
    elif user_input == "s":
        doc_number = input("Введите номер документа: ")
        result = find_shelf_by_number(doc_number)
        print(result)
    elif user_input == "l":
      show_all()
    elif user_input == "ads":
      add_shelf()
    elif user_input == "ds":
      delete_shelf()
    elif user_input == "q":
        break
