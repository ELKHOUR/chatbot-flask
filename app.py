from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, url_for, request, jsonify
import os
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

bot = ChatBot('module', read_only=False, logic_adapters=[{
    'import_path': 'chatterbot.logic.BestMatch',
    'default_response': 'I am sorry rewrite what u wont ?'
}] )




list_to_train = [
    "привет",
    "Здравствуйте! Чем могу помочь?",

    "как тебя зовут",
    "Я УниБот, ваш помощник по университету.",

    "где находится библиотека",
    "Библиотека находится в главном корпусе, 2 этаж. Подробнее: https://university.ru/library",

    "как попасть в деканат",
    "Деканат находится в корпусе №1, кабинет 101. Часы работы: 9:00–17:00. Подробнее: https://university.ru/dean-office",

    "как посмотреть расписание",
    "Расписание занятий доступно на сайте: https://university.ru/schedule",

    "когда сессия",
    "График сессии опубликован на портале: https://university.ru/exams",

    "как связаться с преподавателем",
    "Вы можете написать преподавателю через университетскую почту. Список контактов: https://university.ru/contacts",

    "как восстановить студенческий билет",
    "Обратитесь в студенческий отдел (корпус №1, каб. 12). Информация: https://university.ru/student-card",

    "где находится столовая",
    "Столовая находится в корпусе №2, первый этаж. Меню: https://university.ru/cafeteria",

    "какие есть кружки и секции",
    "Список кружков и спортивных секций: https://university.ru/clubs",

    "как получить справку об обучении",
    "Справку можно заказать в деканате или через онлайн-портал: https://university.ru/documents",

    "как подключить wi-fi в университете",
    "Подробная инструкция по подключению Wi-Fi: https://university.ru/wi-fi",

    "сколько стоит общежитие",
    "Стоимость проживания в общежитии — от 2000 руб./мес. Подробнее: https://university.ru/dormitory",

    "как подать заявление на стипендию",
    "Заявления на стипендию подаются через деканат или портал: https://university.ru/scholarship",

    "где найти электронные учебники",
    "Электронные книги и материалы доступны в ЭБС: https://university.ru/ebooks",

    "как пройти практику",
    "Информация о практике доступна на сайте кафедры: https://university.ru/practice",

    "когда каникулы",
    "Учебный календарь можно посмотреть тут: https://university.ru/calendar",

    "как оплатить обучение",
    "Оплатить обучение можно через личный кабинет: https://university.ru/payments",

    "как получить диплом",
    "Информация о получении диплома и выдаче документов: https://university.ru/diploma"
]


ListTrainer(bot).train(list_to_train)


@app.route("/get")
def get_chatBot_response():
    user_input = request.args.get('user_input')
    return str(bot.get_response(user_input))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))