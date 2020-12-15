import random
from tkinter import *
from tkinter.ttk import Combobox

#base data for reference
languages = ["Common", "Elvish", "Dwarvish", "Gnomish", "Halfling", "Orcish", "Giant", "Goblin", "Abyssal", "Draconic", "Celestial"]
abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature",
          "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]

#we define race here, then define the races
class race(object):
    def __init__(self, name, abils, speed, skills, langs, langs_2, racial):
        self.name = name
        self.abils = abils
        self.speed = speed
        self.skills = skills
        self.langs = langs
        self.langs_2 = langs_2
        self.racial = racial

dwarf_hill = race("Hill Dwarf", [0, 0, 2, 0, 1, 0], 25, [], ["Common", "Dwarvish"], 0,
                  ["Dwarven Resilience: Adv. on saves vs. poison", "Stonecunning: Add proficiency bonus to History checks concerning stone","Dwarves speed are not reduced by armour"])
dwarf_mountain = race("Mountain Dwarf", [2, 0, 2, 0, 0, 0], 25, [], ["Common", "Dwarvish"], 0,
                      ["Darkvision 60ft", "Dwarven Resilience: Adv. on saves vs. poison", "Stonecunning: Add proficiency bonus to History checks concerning stone","Dwarves speed are not reduced by armour"])
elf_high = race("High Elf", [0, 2, 0, 1, 0, 0], 30, ["Perception"], ["Common", "Elvish"], 0, ["Darkvision 60ft", "Fey Ancestry: Adv. vs saves against charm", "Trance: Elves have no need for sleep, and instead enter a trance-like state for 4 hours", "Add one cantrip from the wizard spell list to your spell list"])
elf_wood = race("Wood Elf", [0, 2, 0, 0, 1, 0], 35, ["Perception"], ["Common", "Elvish"], 1, ["Darkvision 60ft", "Fey Ancestry: Adv. vs saves against charm", "Trance: Elves have no need for sleep, and instead enter a trance-like state for 4 hours"])
human = race("Human", [1, 1, 1, 1, 1, 1], 30, [], ["Common"], 1, ["Basic human, consider variant"])
gnome_rock = race("Rock Gnome", [0, 0, 1, 2, 0, 0], 25, [], ["Common, Gnomish"], 0, ["Darkvision 60ft", "Gnome Cunning: Advantage on all mental saves vs magic",
                                                                                 "Tinker: Make a fun toy and it does dumb stuff"])
gnome_forest = race("Forest Gnome", [0, 1, 0, 2, 0, 0], 25, [], ["Common", "Gnomish"], 0, ["Darkvision 60ft", "Gnome Cunning: Advantage on all mental saves vs magic",
                                                                                           "Add the minor illusion cantrip to your spell list", "Speak with small beasts"])
half_orc = race("Half Orc", [2, 0, 1, 0, 0, 0], 30, ["Intimidation"], ["Common", "Orcish"], 0, ["Darkvision 60ft", "Relentless Endurance: Once per long rest, when you drop to 0 hit points, instead drop to 1",
                                                                                                "Savage Critical: When you score a critical hit with a melee attack, you can roll one of the damage die one more time than normal and add it to the damage of the critical hit"])

races = [dwarf_hill, elf_high, human, elf_wood, dwarf_mountain, gnome_rock, gnome_forest, half_orc]

#we define each class individually and add it to the list
class char_class(object):
    def __init__(self, name, abils, saves, no_prof, profs, armor, weapons, inv):
        self.name = name
        self.abils = abils
        self.saves = saves
        self.no_prof = no_prof
        self.profs = profs
        self.armor = armor
        self.weapons = weapons
        self.inv = inv

barbarian = char_class("Barbarian", ["CON", "STR"], ["STR", "CON"], 2, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
                       ["Shields"], ["Simple Weapons", "Martial Weapons"], [2, 4])
bard = char_class("Bard", ["CHA", "DEX"], ["DEX", "CHA"], 3, skills, ["Light Armor"], ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers",
                                                                                       "Shortswords", "Three musical instruments"], [5, 4])
cleric = char_class("Cleric", ["WIS", "CON"], ["INT", "WIS"], 2, ["History", "Insight", "Medicine", "Persuasion", "Religion"], ["Shields", "Light Armor", "Medium Armor"],
                    ["Simple Weapons"], [5, 4])
druid = char_class("Druid", ["WIS", "CON"], ["INT", "WIS"], 2, ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
                   ["Light armor", "Medium armor", "Shields", "Special - Druids cannot wear metal"], ["Clubs", "Daggers", "Darts", "Javelins", "Maces",
                    "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears", "Herbalism Kit"], [2, 4])
fighter = char_class("Fighter", ["CON", "STR", "DEX"], ["STR", "CON"], 2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation",
                    "Perception", "Survival"], ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"], ["Simple Weapons", "Martial Weapons"], [5, 4])
monk = char_class("Monk", ["WIS", "DEX", "CON"], ["STR", "DEX"], 2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], [],
                  ["Simple Weapons", "Shortswords", "One artisan's tool or musical instrument of choice"], [5, 4])
paladin = char_class("Paladin", ["CHA", "STR", "CON"], ["WIS", "CHA"], 2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
                     ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"], ["Simple Weapons", "Martial Weapons"], [5, 4])
ranger = char_class("Ranger", ["DEX", "WIS"], ["STR", "DEX"], 3, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
                    ["Light Armor", "Medium Armor", "Shields"], ["Simple Weapons", "Martial Weapons"], [5, 4])
rogue = char_class("Rogue", ["DEX", "INT"], ["DEX", "INT"], 4, ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception",
                    "Performance", "Persuasion", "Sleight of Hand", "Stealth"], ["Light Armor"], ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Thieve's Tools"], [4, 4])
sorceror = char_class("Sorceror", ["CHA", "DEX", "CON"], ["CHA", "CON"], 2, ["Arcana", "Deception", "Insight", "Persuasion", "Religion"], [],
                      ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"], [3, 4])
warlock = char_class("Warlock", ["CHA"], ["CHA", "WIS"], 2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], ["Light Armor"],
                     ["Simple Weapons"], [4, 4])
wizard = char_class("Wizard", ["INT", "CON", "DEX"], ["INT", "WIS"], 2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], [], ["Daggers", "Darts", "Slings",
                        "Quarterstaffs", "Light Crossbows"], [4, 4])

classes = [barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorceror, warlock, wizard]


#finally we do the same for backgrounds
class background(object):
    def __init__(self, name, prof, bonus, inv, gp_bg, langs):
        self.name = name
        self.prof = prof
        self.bonus = bonus
        self.inv = inv
        self.gp_bg = gp_bg
        self.langs = langs
        
acolyte = background("Acolyte", ["Insight", "Religion"], [], ["Holy Symbol", "Prayer Book"], 15, 2)
charlatan = background("Charlatan", ["Deception", "Sleight of Hand"], ["Disguise kit", "Forgery Kit"], ["Fine clothes", "Disguise kit", "Con tools"], 15, 0)
criminal = background("Criminal", ["Deception", "Stealth"], ["Thieve's tools", "Gaming set"], ["Crowbar"], 15, 0)
entertainer = background("Entertainer", ["Acrobatics", "Performance"], ["Disguise Kit", "One musical instrument"], ["A musical instrument of choice", "Costume"], 15, 0)
folk_hero = background("Folk Hero", ["Animal Handling", "Survival"], ["Artisan's tools", "Vehicles (Land)"], ["Artisan's tools of choice", "Shovel", "Iron Pot"], 15, 0)
guild_artisan = background("Guild Artisan", ["Insight", "Persuasion"], ["Artisan's tools"], ["Artisan's tools of choice", "Letter of introduction"], 15, 1)
hermit = background("Hermit", ["Medicine", "Religion"], ["Herbalism Kit"], ["Scroll case full of notes", "Winter Blanket", "Herbalism Kit"], 5, 1)
noble = background("Noble", ["History", "Persuasion"], ["One type of gaming set"], ["Fine clothes", "Signet Ring", "Scroll of Pedigree"], 25, 1)
outlander = background("Outlander", ["Athletics", "Survival"], ["One type of musical instrument"], ["Staff", "Hunting trap", "Trophy from hunted animal"], 10, 0)
sage = background("Sage", ["Arcana", "History"], [], ["Bottle of black ink", "Quill", "Small knife", "Letter from a dead colleague"], 10, 2)
sailor = background("Sailor", ["Athletics", "Perception"], ["Navigator's tools", "Vehicles (Water)"], ["Club", "Silk Rope", "Lucky Charm"], 10, 0)
soldier = background("Soldier", ["Athletics", "Intimidation"], ["One type of gaming set", "Vehicles (Land)"], ["Insignia of rank", "Trophy from a fallen enemy"], 10, 0)
urchin = background("Urchin", ["Sleight of Hand", "Stealth"], ["Disguise Kit", "Thieves Tools"], ["A small knife", "Map of home city", "Pet mouse"], 10, 0)

backgrounds = [acolyte, charlatan, criminal, entertainer, folk_hero, guild_artisan, hermit, noble, outlander, sage, sailor, soldier, urchin]

#a few functions we need for randomising things
def r(list_things):
    i = random.randint(0, len(list_things)-1)
    return list_things[i]

def d(size):
    i = random.randint(1, size)
    return i

#this will calculate a single score
def score():
    subs = []
    for i in range(1, 5):
        subs.append(d(6))
    subs.sort()
    final = sum(subs[1:])
    return final

#calculates many scores, keeping them within a playable range  
def abilities_get():
    abilities = [0, 7]
    while abilities[0] < 15 or abilities[-1] < 8:
        abilities = []
        for i in range(1, 7):
            abilities.append(score())
        abilities.sort()
        abilities.reverse()
    return abilities

#boring function for boring people
def race_get():
    race = r(races)
    return race

def name_this():
    one_syll = ["Po", "Tha", "To", "Ol", "Si", "Se", "Ka", "Te", "Go", "Re", "Tur", "Vu", "Foi", "Hor", "Dee", "Sca", "Bur", "Wil", "Fre", "Jeru", "Cas", "Ma"]
    two_syll = ["ra", "da", "in", "li", "man", "kin", "no", "un", "id", "ro", "ang", "mur", "neh", "zidl", "ough", "ster", "plir", "then"]
    three_syll = ["adir", "eodun", "ablin", "ameer", "adosh", "ari", " von Stammbank"]
    one = r(one_syll)
    two = r(two_syll)
    three = r(three_syll)
    val=d(10)
    if val>=7:
        name = one+two+three
    else:
        name = one+two
    return name

#grabs a class from the list, generates list of ability scores then correctly assigns the 'main' abilities to maximise playability. then randomises the rest
def abilities_assign():
    char_class = r(classes)
    favoured_abilities = char_class.abils
    unfavoured_abilities = [str(i) for i in abilities if i not in favoured_abilities]
    raw_scores = abilities_get()
    
    final_scores = {}
    for i, n in zip(favoured_abilities, raw_scores):
        final_scores[i] = n
    remaining_scores=raw_scores[len(favoured_abilities):]
    random.shuffle(remaining_scores)
    for i, n in zip(unfavoured_abilities, remaining_scores):
        final_scores[i] = n
    scores_ordered = {}
    for i, n in zip(abilities, final_scores):
        scores_ordered[i] = final_scores[i]

    return char_class, scores_ordered

def abilities_assign_nonrand(class_name):
    char_class = class_name
    favoured_abilities = char_class.abils
    unfavoured_abilities = [str(i) for i in abilities if i not in favoured_abilities]
    raw_scores = abilities_get()
    
    final_scores = {}
    for i, n in zip(favoured_abilities, raw_scores):
        final_scores[i] = n
    remaining_scores=raw_scores[len(favoured_abilities):]
    random.shuffle(remaining_scores)
    for i, n in zip(unfavoured_abilities, remaining_scores):
        final_scores[i] = n
    scores_ordered = {}
    for i, n in zip(abilities, final_scores):
        scores_ordered[i] = final_scores[i]

    return char_class, scores_ordered

#again,trash function for trash people
def bg_get():
    cb = r(backgrounds)
    return cb

def get_deets():
    
    rand_race_check=rand_race.get()
    rand_class_check=rand_class.get()
    rand_bg_check=rand_bg.get()
    
    if rand_name.get()==1:
        name = name_this()
    else:
        name=str(name_entered.get())+" "
    race = 0
    char_class = 0
    background = 0
    race_name=combo_races.get()
    
    for i in races:
        if race_name == i.name:
            race = i
    class_name=combo_class.get()
    for i in classes:
        if class_name==i.name:
            char_class=i
    if rand_class_check==1:
        char_class=r(classes)
        
    background_name=combo_background.get()
    for i in backgrounds:
        if background_name==i.name:
            background=i
        
    if rand_race_check == 1:
        race=r(races)
    
        
    skills = []
    profs = []
    inv = []
    langs = []
    languages_known = []
    remaining_languages = []
    remaining_skills = []
    x, y = 0, 0
    bg = 0

    #grabs the basic data from above classes/functions
    
    bg = background

    if rand_bg_check==1:
        bg=r(backgrounds)
    
    x, y = abilities_assign_nonrand(char_class)

    #print(y)
    #print(x)
    #we add racial bonuses to abilies
    for i, n in enumerate(abilities):
        y[n] = y[n]+race.abils[i]


    #we check racial skills here
    for i in range(1, len(race.skills)+1):
        if i not in skills:
            skills.append(race.skills[i-1])
            if i in remaining_skills:
                remaining_skills.remove(i)
        if i in remaining_skills:
            remaining_skills.remove(race.skills[i-1])

    #we add the background skills first because they're fixed and remove them from the possible skills
    for i in bg.prof:
        if i not in skills:
            skills.append(i)
    remaining_skills = [i for i in x.profs if i not in skills]
    
    #we add up that dolla' to keep it simple
    gp_calc = x.inv
    gp = 0
    for i in range(1, gp_calc[0]+1):
        gp += d(gp_calc[1])
        
    gp = gp*10
    gp += bg.gp_bg
    inv.append(str(gp)+" gp")

    #then we add the rest of the stuff given from backgrounds
    for i in bg.inv:
        inv.append(i)

    
    #we add in the class skills at random here
    for i in range(1, x.no_prof+1):
        k = (r(remaining_skills))
        skills.append(k)
        remaining_skills.remove(k)

    #we add weapon and armor proficiency
    for i in x.armor:
        profs.append(i)
    for i in x.weapons:
        profs.append(i)

    #we add the fun proficiencies from backgrounds
    for i in bg.bonus:
        profs.append(i)

    #languages used to cause a bug but it's fixed now - we start with some racial langs...
    for i in race.langs:
        languages_known.append(i)

    #remove the already known races
    remaining_languages = [i for i in languages if i not in languages_known]

    #and then we randomise and other languages we get
    total_bonus_lang = race.langs_2+bg.langs
    for i in range(1, total_bonus_lang+1):
        k = r(remaining_languages)
        languages_known.append(k)
        remaining_languages.remove(k)

    skills.sort()

    #then we print that shit out
    print("Name: "+str(name))
    print("Race: "+str(race.name))
    print("Class: "+str(x.name))

    print("Background: "+str(bg.name))
    print("Saves: "+str(x.saves[0])+", "+str(x.saves[1]))
    for i in y:
        print(str(i)+" "+str(y[i]))

    print("\nRacial Traits: ")
    for i in race.racial:
        print(i)

    print("\nSkill proficiencies: ")
    for i in skills:
        print(str(i))

    print("\nOther Proficiencies: ")
    for i in profs:
        print(str(i))

    print("\nLanguages: ")
    for i in languages_known:
        print(str(i))
    
    print("\nInventory: ")
    for i in inv:
        print(str(i))
    with open(str(name)+".txt", "w") as f:
        f.write("Name: "+str(name))
        f.write("\n\nRace: "+str(race.name))
        f.write("    Class: "+str(x.name))
        f.write("   Background: "+str(bg.name))
        f.write("\n\nSaves: "+str(x.saves[0])+", "+str(x.saves[1])+"\n")
        for i in y:
            f.write("\n"+str(i)+" "+str(y[i]))
        f.write("\n\nRacial Traits: ")
        for i in race.racial:
            f.write("\n"+i)

        f.write("\n\nSkill proficiencies: ")
        for i in skills:
            f.write("\n"+str(i))

        f.write("\n\nOther Proficiencies: ")
        for i in profs:
            f.write("\n"+str(i))

        f.write("\n\nLanguages: ")
        for i in languages_known:
            f.write("\n"+str(i))
    
        f.write("\n\nInventory: ")
        for i in inv:
            f.write("\n"+str(i))

window= Tk()

rand_race=IntVar()
rand_class=IntVar()
rand_bg=IntVar()
rand_name=IntVar()
name_entered=StringVar()

window.title("Character Generator")
window.geometry("290x190")

lbl_name=Label(window, text="Name:   ")
lbl_name.grid(row=1, column=1, sticky="w")

entry_name=Entry(window, text=name_entered, width=23).grid(row=1, column=2)

name_check=Checkbutton(window, text="Random", variable=rand_name).grid(row=1, column=3)

lbl_races = Label(window, text="Race:   ")
lbl_races.grid(row=2, column=1, sticky="w")

combo_races=Combobox(window)
combo_races["values"]=[i.name for i in races]
combo_races.grid(row=2, column=2)
combo_races.current(0)

race_check=Checkbutton(window, text="Random", variable=rand_race).grid(row=2, column=3)

lbl_class = Label(window, text="Class:")
lbl_class.grid(row=3, column=1, sticky="w")

combo_class=Combobox(window)
combo_class["values"]=[i.name for i in classes]
combo_class.grid(row=3, column=2)
combo_class.current(0)

class_check=Checkbutton(window, text="Random", variable=rand_class).grid(row=3, column=3)

lbl_background = Label(window, text="Background:", width=10, justify=LEFT)
lbl_background.grid(row=4, column=1, sticky="w")

combo_background=Combobox(window)
combo_background["values"]=[i.name for i in backgrounds]
combo_background.grid(row=4, column=2)
combo_background.current(0)

bg_check=Checkbutton(window, text="Random", variable=rand_bg).grid(row=4, column=3)

blank_1=Label(window).grid(row=6, column=2)

button_do = Button(window, text="Generate Character", command = get_deets, width=30)
button_do.grid(row=7, column =1, columnspan=3)




