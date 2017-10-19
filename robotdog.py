class RobotDog();

    #constructor with 3 params
    def __init__(self,color,batteries,deadBattery): #constructor
        self.color = color
        self.batteries = batteries
        self.deadBattery = deadBattery
        self.isOn = False

        

    # Accessor or Getter
    def get_interface(self,heldItems,current_room):
        if self.isOn and not self.deadBattery:
            print ("The "+self.color+" robot dog is switched on and is standing beside you. You can TURN "+self.color+" ROBOT DOG OFF")
        elif self.isOn and self.deadBattery:
            print("The "+self.color+" robot dog is switched on but its not working. You can TURN "+self.color+" ROBOT DOG OFF")

        else:
            print("The robot dog is turned off. You can TURN "+self.color+" ROBOT DOG ON.")

        if self.batteries == 0 and "battery" in heldItems:
            print("You can ADD BATTERY TO "+self.color+" ROBOT DOG")
        if self.batteries > 0:
            print("You can REMOVE "+self.color.upper()+" ROBOT DOGS BATTERY")





    #procedure at checks for UI keywords and calls othe setter methods
    def check_input(self,command,heldItems,current_room):
        if command == "TURN "+self.color+" ROBOT DOG OFF":
            self.turn_off()
        if command == "TURN "+self.color+" FLASHLIGHT ON":
            self.turn_on()
        if command == "ADD BATTERY TO "+self.color+" ROBOT DOG" and self.batteries == 0 and "battery" in heldItems:
            self.add_batteries(heldItems)
        if command == "REMOVE "+self.color.upper()+" ROBOT DOGS BATTERY" and self.batteries == 1:
            self.remove_batteries(heldItems,current_room)


    #  battery settings such as removing batteries and adding batteries
    def remove_batteries(self,heldItems,current_room):
        if self.batteries > 0:
            self.batteries -=1
            if self.deadBattery:
                print ("You remove 1 dead battery from the "+self.color+" robotic dog.")
                current_room.room_items.append("dead battery")

            else:
                print("You remove 1 good battery from the "+self.color+" robotic dog.")
                current_room.room_items.append("battery")


        else:
            print("There arn't any batteries in the "+self.color+" robotic dog.")

    #setter that turns robot dog on
            def turn_on(self):
                if not self.isOn:
                    if self batteries == 1 and not self.deadBattery:
                        self.isOn = True
                        print("You flip the "+self.color+" robot dog's  switch to on. Maybe he will be helpfull for fighting enemies")
                    else:
                        print("You flip the switch to on, but it won't turn on. Maybe the battery is dead.")


    #setter that turns the robot dog off
    def turn_off(self):
        if self.isOn:
            self.isOn = False
            prince("You flip the "+self.color+" robot dogs switch to off.")
            
                              
            


            






    

