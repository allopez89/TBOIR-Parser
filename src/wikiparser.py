from mediawiki import MediaWiki
import json
import sys
import Titles
import Images
import Descriptions

tboi = MediaWiki(url="https://bindingofisaacrebirth.fandom.com/api.php", user_agent="TBOIR-WikiParser/0.2.0 (axellpz89@hotmail.com) pymediawiki/0.7.0")

def SerializeActives():  
    try:
        Actives = Titles.GetActiveItems()
        result = []
        for i in range(0, len(Actives)):
            data = {}
            data["Name"] = Actives[i]
            data["Quote"] = Descriptions.GetQuote(Actives[i])
            sections = Descriptions.GetSections(Actives[i])
            
            for j in range(0, len(sections)):
                data[sections[j]] = tboi.page(Actives[i]).section(sections[j])
            activelist1 = ["Bag of Crafting", "Best Friend", "Broken Shovel", "Dad's Key", "Wait What?", "Yum Heart"]
            if Actives[i] in activelist1:
                ActivesImg = Images.GetActiveImages2(Actives[i].replace(" ", "_"))
            else:
                ActivesImg = Images.GetActiveImages(Actives[i].replace(" ", "_"))
            
            active2 = Actives[i].replace("!", "%21").replace("?", "").replace("'", "%27")
            if "Broken Shovel" in Actives[i]: active2 = "Broken Shovel 1"
            data["Images"] = []
            data["Images"].append({
                "Icon": next((x for x in ActivesImg if "Collectible_{}_icon".format(active2.replace(" ", "_")) in x), None), 
                "Altar": next((x for x in ActivesImg if "Item_altar".format(active2.replace(" ", "_")) in x), None), 
                "Appearance": next((x for x in ActivesImg if "Collectible_{}_appearance".format(active2.replace(" ", "_")) in x), None),
                "Tears": next((x for x in ActivesImg if "Collectible_{}_tears".format(active2.replace(" ", "_")) in x), None),
                "Recharge Time": next((x for x in ActivesImg if "Recharge_".format(active2.replace(" ", "_")) in x), None)})
            result.append(data)

            print("Done with {}".format(data["Name"]))

        with open("actives.json", "w") as acfile:
            json.dump(result, acfile, indent=4)

    except:
        print("An exception occurred on {} for {}, ".format(data["Name"], sys.exc_info()[0]))

def SerializePassives():  
    try:
        Passives = ["???'s Only Friend"]#Titles.GetPassiveItems()
        result = []
        for i in range(0, len(Passives)):
            data = {}
            data["Name"] = Passives[i]
            data["Quote"] = Descriptions.GetQuote(Passives[i])
            sections = Descriptions.GetSections(Passives[i])
            for j in range(0, len(sections)):
                data[sections[j]] = tboi.page(Passives[i]).section(sections[j])
            passinvelist1 = ["1up"]
            passive2 = Passives[i].replace("!", "%21").replace("?", "").replace("'", "%27")
            if Passives[i] in passinvelist1:
                PassivesImg = Images.GetPassiveImages2(Passives[i].replace(" ", "_"))
            else:
                PassivesImg = Images.GetPassiveImages(Passives[i].replace(" ", "_"))
            if "Broken Shovel" in Passives[i]: passive2 = "Broken Shovel 2"
            
            data["Images"] = []
            data["Images"].append({
                "Icon": next((x for x in PassivesImg if "Collectible_{}_icon".format(passive2.replace(" ", "_")) in x), None), 
                "Altar": next((x for x in PassivesImg if "Item_altar".format(passive2.replace(" ", "_")) in x), None), 
                "Appearance": next((x for x in PassivesImg if "Collectible_{}_appearance".format(passive2.replace(" ", "_")) in x), None),
                "Tears": next((x for x in PassivesImg if "Collectible_{}_tears".format(passive2.replace(" ", "_")) in x), None),
                "Recharge Time": next((x for x in PassivesImg if "Recharge_".format(passive2.replace(" ", "_")) in x), None)})
            result.append(data)

            print("Done with {}".format(data["Name"]))

        with open("passives.json", "w") as acfile:
            json.dump(result, acfile, indent=4)

    except:
        print("An exception occurred on {} for {}, ".format(data["Name"], sys.exc_info()[1]))

#SerializeActives()
SerializePassives()