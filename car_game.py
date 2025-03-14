key=""
move=0 #used like a flag to determine whether the car is moving(1) or not(0)
while True:
    key=input(">").lower()
    if key=='help':
        print("start-to start the car\nstop-to stop the car\nquit-to exit")
    elif key=="start":
        if move==1:
            print("car is already started...")
        else:
            print("car is started vrommm vrommm")
            move=1
    elif key=="stop":
        if move==0:
            print("car is already stopped...")
        else:
            print("car is stopped ")
            move=0
    elif key=='quit':
        break
    else:
        print("nah , i cant understand u mannn")

