############
# Lire le fichier
#############
import pandas as pd

CULVERT_FILE_PATH = "culvert_logfile.txt"

print("starting...")

culvert_data = {
    "branch": [],
    "name": [],
    "type": [],
    "diameter": [],
    "length": [],
    "manning": [],
    "upstream_chainage": [],
    "upstream_invert": []
    }


with open(CULVERT_FILE_PATH, "r", encoding="utf-8") as f:
    
    culvert_count = 0
    
    for line in f:
        if "START CULVERT" in line:
            culvert_count +=1
        if line.startswith("Culvert_branch"):
            branch = line.strip().split("=")[1].strip("")
            culvert_data["branch"].append(branch)
        if line.startswith("Culvert_name"):
            name = line.strip().split("=")[1].strip("")
            culvert_data["name"].append(name)
        if line.startswith("Culvert_params"):
            params = line.strip().split(" = ")[1].split(",")            
            t,d,l,m,uc,ui = params
            
            culvert_data["type"].append(t)
            culvert_data["diameter"].append(d)
            culvert_data["length"].append(l)
            culvert_data["manning"].append(m)
            culvert_data["upstream_chainage"].append(uc)
            culvert_data["upstream_invert"].append(ui)
print(f"{culvert_count} culverts ont été trouvés!")

df = pd.DataFrame(culvert_data)

print(df)

df.to_csv("culvert_data.csv", index=False)

print("Done")
            
        









