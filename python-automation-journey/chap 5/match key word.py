#simple command automation 
command = input("enter a commant:(start/stop/restart)")

match command:
    case "start":
        print("system starting......")
    case "stop":
        print("system is shutting down......")
    case "restart":
        print("system restarting......")
    case _:
        print("unkown command")