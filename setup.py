import os.path
print("Setting up..")

options = {"DEBUG": None}

print("Creating common.py")
if(not os.path.exists("common.py")):
    with open("common.py", "w") as f:
        f.write("DEBUG = "+options["DEBUG"])
print("Setup complete\n Run python3.6 routes.py to start server")