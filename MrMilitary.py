
import discord
from discord import app_commands
from DataCaller import getAllPlanes
from DataCaller import getAllVehicles
from DataCaller import callDataPlane
from DataCaller import callDataShip
from DataCaller import callDataVehicle
from Categorize import categorizeAircraft
from Categorize import categorizeVehicle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_ids = [1030746627113230367, ]

def sendError(parameter):
     
    embed = discord.Embed(
        title="Oh no! A miscalculation",
        description=f"Sorry commander, looks like we don't have the desired unit you are searching for. We can't find {parameter} in our catalog",
        color=discord.Color.dark_red()
    )
    
    return embed
     
#List of Planes
@tree.command(name = "plane-list", description = "Get a list of available planes", guild=discord.Object(id=1030746627113230367))
async def acquire_planes(interaction):
   
    await interaction.response.send_message("The list has been relayed")
    aircraft_list = getAllPlanes()
    categorized_aircraft_list = categorizeAircraft(aircraft_list)
    categorized_combat = '\n'.join(categorized_aircraft_list[0])
    categorized_transport = '\n'.join(categorized_aircraft_list[1])
    categorized_surveillance = '\n'.join(categorized_aircraft_list[2])
    categorized_helicopter =  '\n'.join(categorized_aircraft_list[3])
    categorized_trainer = '\n'.join(categorized_aircraft_list[4])
    
    embed = discord.Embed(
        title="Aircraft List",
        description="List of available aircraft with information!",
        color=discord.Color.dark_green()
    )
    embed.add_field(name="Combat Aircraft", value=categorized_combat, inline=False)
    embed.add_field(name="Transport/Utility Aircraft", value=categorized_transport, inline=False)
    embed.add_field(name="Surveillance Aircraft", value=categorized_surveillance, inline=False)
    embed.add_field(name="Helicopters", value=categorized_helicopter, inline=False)
    embed.add_field(name="Trainer Aircraft", value=categorized_trainer, inline=False)
    embed.set_footer(text="Learn and Adapt")
    await interaction.followup.send(embed=embed)

@tree.command(name = "vehicle-list", description = "Get a list of available land vehicles", guild=discord.Object(id=1030746627113230367))
async def acquire_vehicles(interaction):
   
    await interaction.response.send_message("The list has been relayed")
    vehicle_list = getAllVehicles()
    categorized_vehicle_list = categorizeVehicle(vehicle_list)
    categorized_tank = '\n'.join(categorized_vehicle_list[0])
    categorized_artillery = '\n'.join(categorized_vehicle_list[1])
    categorized_recon = '\n'.join(categorized_vehicle_list[2])

    embed = discord.Embed(
        title="Vehicle List",
        description="List of available land vehicles!",
        color=discord.Color.dark_green()
    )
    embed.add_field(name="Tanks", value=categorized_tank, inline=False)
    embed.add_field(name="Artillery", value=categorized_artillery, inline=False)
    embed.add_field(name="Recon", value=categorized_recon, inline=False)

    await interaction.followup.send(embed=embed)
    
#Request aircraft command (Helicopters included)
@tree.command(name = "requestplane", description = "Get an aircraft's information! Bombers, Fighters...", guild=discord.Object(id=1030746627113230367))
async def get_plane(interaction, aircraft: str):

    await interaction.response.send_message(f"An aircraft {aircraft} has been dispatched")
    result = callDataPlane(aircraft)

    #handling errors
    if result == (f"The {aircraft} cannot be found within our catalog."):
        embed = sendError(aircraft)
    else:
        result_image = result.get("image")
        result_class = result.get("_class")
        result_manu = result.get("manufacturer")
        result_status = result.get("status")

        embed = discord.Embed(
            title= aircraft,
            description=f"One of Switzerland's {result_class}",
            color=discord.Color.dark_green()
        )
        embed.add_field(name="Current status", value=result_status)
        embed.add_field(name="Type", value=result_class)
        embed.add_field(name="Manufactured by", value=result_manu)
        embed.set_image(url=result_image)

    await interaction.followup.send(embed=embed)


## Request vehicles command
@tree.command(name = "requestvehicle", description = "Get a vehicle's information! Tanks, Artilleries...", guild=discord.Object(id=1030746627113230367))
async def get_vehicle(interaction, vehicle: str):
    
    await interaction.response.send_message(f"A vehicle {vehicle} has been dispatched")
    result = callDataVehicle(vehicle)

    if result == (f"The {vehicle} cannot be found within our catalog."):
        embed = sendError(vehicle)
    else:
        result_image = result.get("image")
        result_class = result.get("_class")
        result_manu = result.get("manufacturer")
        result_status = result.get("status")

        embed = discord.Embed(
            title= vehicle,
            description=f"One of Switzerland's {result_class}",
            color=discord.Color.dark_green()
        )
        embed.add_field(name="Current status", value=result_status)
        embed.add_field(name="Type", value=result_class)
        embed.add_field(name="Manufactured by", value=result_manu)
        embed.set_image(url=result_image)

    await interaction.followup.send(embed=embed)

#Request Vessel
@tree.command(name="requestvessel", description="Get a vessel's information! Destroyers, Carriers, Battleships, Submarines...", guild=discord.Object(id=1030746627113230367))
async def get_ship(interaction, vessel: str):
    await interaction.response.send_message(f"the vessel {vessel} has been dispatched")
    result = callDataShip(vessel)   

@client.event   
async def on_ready():
        for guild_id in guild_ids:
            await tree.sync(guild=discord.Object(id=guild_id))
        print(f'Logged on as {client.user}!')


client.run("") #Token here

