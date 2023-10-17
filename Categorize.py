

def categorizeAircraft(aircraft_list):

    helicopter_list = []
    combat_list = []
    transport_list = []
    trainer_list = []
    surveillance_list = []

    for aircraft in aircraft_list:

        if "helicopter" in aircraft:
            aircraft.remove("helicopter")
            helicopter_list.append(aircraft.pop())    
        elif "combat aircraft" in aircraft:
            aircraft.remove("combat aircraft")
            combat_list.append(aircraft.pop())
        elif "transport aircraft" in aircraft:
            aircraft.remove("transport aircraft")
            transport_list.append(aircraft.pop())
        elif "trainer aircraft" in aircraft:
            aircraft.remove("trainer aircraft")
            trainer_list.append(aircraft.pop())
    
    print(helicopter_list)
    print(combat_list)
    print(transport_list)
    print(trainer_list)

    return [combat_list, transport_list, surveillance_list, helicopter_list, trainer_list]

def categorizeVehicle(vehicle_list):

    tank_list = []
    artillery_list = []
    recon_list = []
    support_list = []

    for vehicle in vehicle_list:
        if "Tank" in vehicle:
            vehicle.remove("Tank")
            tank_list.append(vehicle.pop())    
        elif "Self-Propelled Artillery" in vehicle:
            vehicle.remove("Self-Propelled Artillery")
            artillery_list.append(vehicle.pop())
        elif "Recon" in vehicle:
            vehicle.remove("Recon")
            recon_list.append(vehicle.pop())
        elif "Support" in vehicle:
            vehicle.remove("Support")
            support_list.append(vehicle)

    print(tank_list)
    print(artillery_list)

    return [tank_list, artillery_list, recon_list, support_list]
            

def categorizeVessel(vessel_list):
    return 