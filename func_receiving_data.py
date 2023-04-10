import json


def load_canditates():
    """
    Function, которая load
     data from json.file
    :param filename:
    :return: file_json
    """
    with open("canditates.json","r",encoding="UTF 8") as file:
      file_json = json.load(file)
    return file_json


def get_all():
    """
    function которая выводит всех canditates
    :param canditates:
    :return: instance
    """
    return load_canditates()


def get_by_pk(pk):
    for c in load_canditates():
        if c["pk"] == pk:
            return c

    return "Not found"

def get_by_skill(skill):
    result = []
    for candidate in load_canditates():
        if skill.lower() in candidate['skills'].lower().split(','):
            result.append(candidate)
    return result
















