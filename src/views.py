
import discord
import _defines as File

class hunts(discord.ui.View):

    def readHunts(self, userlvl:int):
        global options
        options = []
        
        for h in File.ReadFile("data/resource/Hunts.json"):

            if h["LVL"] <= userlvl:

                label = h["name"]
                descr = h["description"]

                options.append(discord.SelectOption(label=label, description=descr))


    @discord.ui.select(

        placeholder = "사냥할 사냥터를 골라주세요.",
        min_values = 1,
        max_values = 1,
        options = options

    )

    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"선택한 서비스 : {select.values[0]}", ephemeral=True)