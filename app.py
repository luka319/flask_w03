from flask import Flask, render_template, request

app = Flask(__name__)

import json
import calendar
import os
import locale
import pathlib

with open("teachers.json", "r", encoding="utf-8") as f:
    te = json.load(f)  #

@app.route('/')
def main():
    # print(f"{te=}")
    import random
    te_rand = random.sample(list(te), 6)
    # print(f"{te_rand =}")
    return render_template("index.html",te=te_rand)

@app.route('/all/')
def main_all():

    return render_template("all.html", te=te)

@app.route('/goals/<goal>/')
def main_goals(goal):
    # en_goals = ["travel", "study", "work", "relocate"]
    # ru_goals = ["путешествий", "школы", "работы", "переезда"]
    # goals = dict(zip(en_goals, ru_goals))
    # goal02 = goals[goal]
    # print(f"{goal02 =}")
    # print(f"{goal =}")
    with open("goals.json", "r", encoding="utf-8") as f:
        goals = json.load(f)  #

    for zz, kk in goals.items():
        # print(f'{zz =}')
        # print(f'{kk =}')
        pass
    # goal02 = goals[goal][3:]

    """
    for z in te:
        if goal in z['goals']:
            # print(f"{z['goals'] =}")
            name = z["name"]
            # print(f"{name =}")
            picture = z["picture"]
            about = z["about"]
            rating = z["rating"]
            price = z["price"]
            id_ = z["id"]
    """

    return render_template("goal.html", goal=goal, te=te, goals=goals)

@app.route('/profiles/<int:id_teacher>/') # 4. Выведите страницу преподавателя
def main_profiles(id_teacher):

    name = "pass"
    for z in te:
         if z["id"] == id_teacher:
            # z = id_teacher
            # print(f'{z["name"] =}')
            name = z["name"]
            picture = z["picture"]
            about = z["about"]
            rating = z["rating"]
            price = z["price"]
            free = z["free"]

    with open("goals.json", "r", encoding="utf-8") as f:
        goals = json.load(f)  #

    for zz, kk in goals.items():
        # print(f'{zz =}')
        # print(f'{kk =}')
        pass

    # =======================================
    # calendar
    engl_full_day = []
    for day2 in calendar.day_name:
        da2 = day2
        # print(da.title())
        engl_full_day.append(da2)

    if os.name == 'nt':
        locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")
    else:
        locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

    engl_day = []
    for k in free.keys():
         engl_day.append(k)

    ru_day = []
    for day in calendar.day_name:
        da = day
        # print(da.title())
        ru_day.append(da.title())
        # day_name[da.title()] = engl_day[zz]
    week_ = dict(zip(ru_day, engl_day))

    # print(
    #     list(calendar.day_name))  # ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

    # free = z["free"] # там выше оно есть, здеесь для напоминания

    day_false = []
    for ke, va in free.items():  # free ={'mon': {'8:00': False, '10:00': False,

        # print(f'{ke =}') # OK!!!
        # print(f'{va =}') # OK!!!
        va2_net = []
        for ke2, va2 in va.items():
            va2_net.append(va2)
        if any(va2_net)==False: # если оно False
                day_false.append(ke)

    # print(f"{day_false =}")
    # print(f"{id_teacher =}")
    id_te = id_teacher

    return render_template("profile.html", name=name, picture=picture, about=about,
                           rating=rating, price=price, goals=goals, free=free,
                           week_=week_,day_false=day_false,
                           id_te=id_te, engl_full_day=engl_full_day)

@app.route('/request/')
def main_request():
    return render_template("request.html",)

@app.route('/request_done/', methods=['POST'])
def main_request_done():
    if request.method == 'POST':
            goal = request.form['goal']
            # print(f"{goal=}")
            time_ = request.form['time']
            # print(f"{time_=}")
            name_ = request.form['name']
            # print(f"{name_ =}")
            phone = request.form['phone']
            # print(f"{phone=}")

            # сохраняю в request.json
            path = pathlib.Path('request.json')
            if path.exists():
                if path.is_file():
                    with open('request.json', 'r', encoding='utf-8') as f:
                        data_in = json.load(f)
                    count = len(data_in)
                else:
                    print("request.json не является файлом")
                    exit()
            else:
                print("== request.json doesn't exists. It will be created! ==")
                # exit()
                count = 0
                data_in = {}

            data = {count + 1: [goal, time_,
                            name_,
                            phone]
                    }
            data_in.update(data)
            data_out = data_in
            with open('request.json', 'w', encoding='utf-8') as f:
                json.dump(data_out, f, ensure_ascii=False)

    en_goals = ["travel","learn","work", "move"]
    ru_goals = ["Для путешествий", "Для школы", "Для работы", "Для переезда"]
    goals = dict(zip(en_goals, ru_goals))
    goal02 = goals[goal]
    # print(f"{goal02 =}")

    return render_template("request_done.html", goal=goal02, time_=time_,
                            name_=name_, phone=phone)

@app.route('/booking/<int:id_teacher>/<day_of_week>/<time>/')
def main_booking(id_teacher, day_of_week, time):
    free = {}
    with open("teachers.json", "r", encoding="utf-8") as f:
        te2 = json.load(f)  #
    # print(f"{te2=}")
    for z in te2:
         if z["id"] == id_teacher:
            free = z["free"]
            name = z["name"]
            picture = z["picture"]
            # print(f"{free =}")
    # =======================================
    # calendar


    if os.name == 'nt':
        locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")
    else:
        locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

    engl_day = []
    for k in free.keys():
        engl_day.append(k)

    ru_day = []
    for day in calendar.day_name:
        da = day
        # print(da.title())
        ru_day.append(da.title())
        # day_name[da.title()] = engl_day[zz]
    week_2 = dict(zip(engl_day, ru_day))
    # print(f"{week_2 =}")
    dweek = week_2[day_of_week]

    return render_template("booking.html", id_teacher=id_teacher,
                           dweek=dweek, time=time, name=name,
                           picture=picture,
                           )

# @app.route('/booking_done/<clientWeekday>/<clientTime>/<clientTeacher>/<clientName>/<clientPhone>/',
#            methods=['POST'])
@app.route('/booking_done/', methods=['GET', 'POST'])
# def main_booking_done(clientWeekday, clientTime, clientTeacher,
#                        clientName,  clientPhone):
def main_booking_done():
     if request.method == 'POST':
         clientWeekday = request.form['clientWeekday']
         # print(f"{clientWeekday=}")
         clientTime = request.form['clientTime']
         # print(f"{clientTime=}")
         clientTeacher = request.form['clientTeacher']
         # print(f"{clientTeacher=}")
         clientName = request.form['clientName']
         # print(f"{clientName=}")
         clientPhone = request.form['clientPhone']
         # print(f"{clientPhone=}")

     # сохраняю в booking.json
     path = pathlib.Path('booking.json')
     if path.exists():
         if path.is_file():
             with open('booking.json', 'r', encoding='utf-8') as f:
                 data_in = json.load(f)
             count = len(data_in)
         else:
             print("booking.json не является файлом")
             exit()
     else:
         print("booking.json не существует")
         # exit()
         count = 0
         data_in = {}

     data = {count + 1: [clientWeekday, clientTime,
                    clientTeacher, clientName,
                    clientPhone]
              }
     data_in.update(data)
     data_out = data_in
     with open('booking.json', 'w', encoding='utf-8') as f:
        json.dump(data_out, f, ensure_ascii=False)


     # return f'Был получен {request.method} запрос.'
     return render_template("booking_done.html", clientWeekday=clientWeekday,
                            clientTime=clientTime, clientTeacher=clientTeacher,
                            clientName=clientName, clientPhone=clientPhone)

if __name__ == '__main__':
    app.run()
"""
---> 1. Распишите роуты, выведите текст:

"""