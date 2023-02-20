from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


USERS = {
    "Fairy": {
        "user_id": "1",
        "password": "password",
        "email": "mail@demo",
        "last_login": get_timestamp(),
        "creation_date": get_timestamp()
    },
    "Ruprecht": {
        "user_id": "2",
        "password": "password",
        "email": "mail@demo",
        "last_login": get_timestamp(),
        "creation_date": get_timestamp()
    },
    "Bunny": {
        "user_id": "3",
        "password": "password",
        "email": "mail@demo",
        "last_login": get_timestamp(),
        "creation_date": get_timestamp()
    },
}


def read_all():
    return list(USERS.values())


def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in USERS:
        USERS[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return USERS[lname], 201
    else:
        abort(406, f"Person with last name {lname} already exists")


def read_one(lname):
    if lname in USERS:
        return USERS[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


def update(lname, person):
    if lname in USERS:
        USERS[lname]["fname"] = person.get("fname", USERS[lname]["fname"])
        USERS[lname]["timestamp"] = get_timestamp()
        return USERS[lname]
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    if lname in USERS:
        del USERS[lname]
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
