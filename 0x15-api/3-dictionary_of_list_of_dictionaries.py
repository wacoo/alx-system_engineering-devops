#!/usr/bin/python3

""" show employee todo list progress and export all users to JSON """

if __name__ == "__main__":
    import json
    import urllib.request

    emp_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    emp = urllib.request.urlopen(emp_url)
    todos = urllib.request.urlopen(todos_url)
    d_emp = json.loads(emp.read())
    d_todos = json.loads(todos.read())
    t_title = []
    t_count = 0
    t_owned = {}
    det = []
    idd = 0
    done_count = 0
    for em in d_emp:
        for td in d_todos:
            if td["userId"] == em["id"]:
                if td["completed"]:
                    done_count += 1
                    t_title.append(td["title"])
                t_count += 1
                tsks = {"username": em["username"], "task": td["title"],
                        "completed": td["completed"]}
                idd = td["userId"]

                det.append(tsks)
        t_owned[idd] = det
        print("Employee {} is done with tasks({}/{}):".format(em["name"],
              done_count, t_count))
        t_count = 0
        done_count = 0
        det = []
        for i in t_title:
            print("\t {}".format(i))
        t_title = []

    with open("todo_all_employees.json".format(idd), 'w') as f:
        json.dump(t_owned, f)
