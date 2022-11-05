"""
Equivalent de main.sh en python avec un fichier .json pour la configuration
"""
from time import sleep
import os, json

def record(file_path):
    with open(file_path) as jsonFile:
        config = json.load(jsonFile)
        arg = ""
        for key, val in config.items():
            arg += " --" + key + " "
            if key == "angle" or key == "town":
                arg += "{" + key + "}"
            elif key == "dimension":
                arg += str(config[key][0]) + " " + str(config[key][1])
            else:
                arg += str(val)

    for town in config["town"]:
        for angle in config["angle"]:
            os.system(f"gnome-terminal --tab --title \"Server on {town}\" -- /opt/carla-simulator/CarlaUE4.sh -opengl -RenderOffScreen")

            sleep(2)
            os.system("python3 simulation.py" + arg.format(town=town, angle=angle))

            carlaPID = os.popen("ps -a | grep Carla | awk '{print $1}'").read()[:-1]
            os.kill(int(carlaPID), 9)

    return config["dbname"]


if __name__ == "__main__":
    file_path = "conf.json"
    db_folder = record(file_path)
    os.system(f"python3 extra/evaluation_DB.py --dbname {db_folder}")
