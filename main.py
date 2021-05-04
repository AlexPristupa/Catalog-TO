import peewee
import json
from Models.models import *
# import Models/models


def add_mark(mark):
    prExist = False
    try:
        markExist = Marks.select().where(Marks.name
                                         == mark["name"]).get()
        prExist = True
    except DoesNotExist as de:
        prExcept = False

    if prExist == False:
        row = Marks(
            name=mark["name"].strip(),
            img=mark["img"]
        )
        row.save()


def add_modificator(markModificator):
    markName = markModificator["markName"]
    modificator = markModificator["modificator"]

    prExists = False

    try:
        modificatorExist = Modifications.select().where(
            Modifications.name == modificator["name"]).get()
        prExists = True
    except DoesNotExist as de:
        prExists = False

        if prExists == False:
            mark = Marks.select().where(Marks.name == markName).get()
            row = Modifications(
                name=modificator["name"],
                img=modificator["img"],
                marka=mark
            )
            row.save()

        for model in modificator["models"]:

            modificationModels = {
                "nameModification": modificator["name"],
                "model": model
            }
            add_models(modificationModels)


def add_models(modificationModels):
    prExists = False

    model = modificationModels["model"]
    arrPropertyModel = model["model"]
    arrDetailsModel = model["details"]

    try:
        Model = Models.select().where(
            Models.name == arrPropertyModel[0]).get()
        prExists = True
    except DoesNotExist as de:
        prExists = False

    if prExists == False:

        modification = Modifications.select().where(
            Modifications.name == modificationModels["nameModification"]).get()

        if(len(arrPropertyModel) == 4):
            row = Models(
                name=arrPropertyModel[0],
                power=arrPropertyModel[1],
                fuel=arrPropertyModel[2],
                year=arrPropertyModel[3],
                modification=modification
            )
        else:
            row = Models(
                name=arrPropertyModel[0],
                power=arrPropertyModel[1],
                fuel=arrPropertyModel[2],
                year="",
                modification=modification
            )

        row.save()

        modelDetails = {
            "nameModel": arrPropertyModel[0],
            "details": arrDetailsModel
        }

        add_details(modelDetails)


def add_details(modelDetails):
    prExists = False

    model = Models.select().where(
        Models.name == modelDetails["nameModel"]).get()

    arrDetails = modelDetails["details"]

    for detail in arrDetails:

        try:
            Detail = Details.select().where(
                Details.name == detail["name_detail"]).where(Details.model == model).get()
            prExists = True
        except DoesNotExist as de:
            prExists = False

        if prExists == False:

            row = Details(
                name=detail["name_detail"],
                code=detail["articul"],
                comment="",
                model=model,
            )
            row.save()


def load_json_data():
    with open("name_models_list.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for marka in data:
        if(marka["name_marka"]):
            print(marka["name_marka"])
            markAdd = {
                "name": marka["name_marka"],
                "img": marka["img_marka"]
            }
            add_mark(markAdd)

            for modification in marka["name_models_list"]:
                name_models_list = marka["name_models_list"]
                for obj_modificator in name_models_list:
                    modificator = {
                        "name":  obj_modificator["name_modification"],
                        "img": obj_modificator["img_modificsation"],
                        "models": obj_modificator["models"]
                    }

                    markModificator = {
                        "markName": marka["name_marka"],
                        "modificator": modificator}

                    add_modificator(markModificator)


if __name__ == '__main__':
    try:
        # dbhandle.connect()
        load_json_data()
    except peewee.InternalError as px:
        print(str(px))
