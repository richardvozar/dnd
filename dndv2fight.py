import tkinter
import tkinter.scrolledtext as tkst
import sqlite3


def main_win():
    main_window = tkinter.Tk()
    main_window.title('D&D Helping Tool')
    main_window.geometry("520x440")
    main_window.resizable(0, 0)
    main_window.iconbitmap('icon.ico')

    welcome = tkinter.Label(main_window, text="Welcome to the D&D helper!")
    welcome.config(font=("Arial", 30))
    welcome.grid(row=1, column=1)

    instructions = tkinter.Label(main_window, text="By the following buttons you can add monsters or npcs to the database, or generate a fight.", fg="blue")
    instructions2 = tkinter.Label(main_window, text="First you should add your monsters and npcs to the database, and than they can join a fight.", fg="blue")
    instructions.grid(row=2, column=1)
    instructions2.grid(row=3, column=1)
    # empty row
    tkinter.Label(main_window, text=" ").grid(row=4, column=1)

    button1 = tkinter.Button(main_window, text="Add monster", height=5, width=25, command=add_monster_win)
    button1.grid(row=5, column=1)




    button2 = tkinter.Button(main_window, text="Add NPC", height=5, width=25, command=add_npc_win)
    button2.grid(row=6, column=1)

    button3 = tkinter.Button(main_window, text="Generate Fight", height=5, width=25, command=generate_fight_window)
    button3.grid(row=7, column=1)

    for i in range(10):
        tkinter.Label(main_window, text=' '*10).grid(row=10+i, column=1, rowspan=5)
    tkinter.Label(main_window, text='Version 1.1').grid(row=20, column=1, sticky=tkinter.E)


    main_window.mainloop()

def add_npc_win():
    #declare all f*cking variables as global.........
    global add_npc_window
    global w2_txt1
    global w2_txt2_input
    global w2_txt3
    global w2_txt4_input
    global w2_txt5
    global w2_txt6_input
    global w2_txt7
    global w2_txt8_input
    global w2_txt9
    global w2_txt10_input
    global w2_txt11
    global w2_txt12_input
    global w2_txt13
    global w2_txt14_input
    global w2_txt15
    global w2_txt16_input
    global w2_txt17
    global w2_txt18_input
    global w2_txt19
    global w2_txt20_input
    global w2_txt21
    global w2_txt22_input
    global w2_txt23
    global w2_txt24_input
    global homebrew_txt
    global homebrew_listbox
    global ch_rating_txt
    global ch_rating_scale
    global add_monster_btn
    global add_monster_creature_type_txt
    global add_monster_creature_type

    #window stats
    add_npc_window = tkinter.Tk()
    add_npc_window.title("Add NPC")
    add_npc_window.geometry("700x800")
    add_npc_window.resizable(1, 1)

    #add monster stats
    w2_txt1 = tkinter.Label(add_npc_window, text="Name:")
    w2_txt1.grid(row=1, column=1, sticky=tkinter.E)
    w2_txt2_input = tkinter.Entry(add_npc_window)
    w2_txt2_input.grid(row=1, column=2, sticky=tkinter.W)

    w2_txt3 = tkinter.Label(add_npc_window, text="Armor Class:")
    w2_txt3.grid(row=2, column=1, sticky=tkinter.E)
    w2_txt4_input = tkinter.Entry(add_npc_window)
    w2_txt4_input.grid(row=2, column=2, sticky=tkinter.W)

    w2_txt5 = tkinter.Label(add_npc_window, text="Hit Points:")
    w2_txt5.grid(row=3, column=1, sticky=tkinter.E)
    w2_txt6_input = tkinter.Entry(add_npc_window)
    w2_txt6_input.grid(row=3, column=2, sticky=tkinter.W)

    w2_txt7 = tkinter.Label(add_npc_window, text="Speed:")
    w2_txt7.grid(row=4, column=1, sticky=tkinter.E)
    w2_txt8_input = tkinter.Entry(add_npc_window)
    w2_txt8_input.grid(row=4, column=2, sticky=tkinter.W)

    w2_txt9 = tkinter.Label(add_npc_window, text="STR:")
    w2_txt9.grid(row=5, column=1, sticky=tkinter.E)
    w2_txt10_input = tkinter.Entry(add_npc_window)
    w2_txt10_input.grid(row=5, column=2, sticky=tkinter.W)

    w2_txt11 = tkinter.Label(add_npc_window, text="DEX:")
    w2_txt11.grid(row=6, column=1, sticky=tkinter.E)
    w2_txt12_input = tkinter.Entry(add_npc_window)
    w2_txt12_input.grid(row=6, column=2, sticky=tkinter.W)

    w2_txt13 = tkinter.Label(add_npc_window, text="CON:")
    w2_txt13.grid(row=7, column=1, sticky=tkinter.E)
    w2_txt14_input = tkinter.Entry(add_npc_window)
    w2_txt14_input.grid(row=7, column=2, sticky=tkinter.W)

    w2_txt15 = tkinter.Label(add_npc_window, text="INT:")
    w2_txt15.grid(row=8, column=1, sticky=tkinter.E)
    w2_txt16_input = tkinter.Entry(add_npc_window)
    w2_txt16_input.grid(row=8, column=2, sticky=tkinter.W)

    w2_txt17 = tkinter.Label(add_npc_window, text="WIS:")
    w2_txt17.grid(row=9, column=1, sticky=tkinter.E)
    w2_txt18_input = tkinter.Entry(add_npc_window)
    w2_txt18_input.grid(row=9, column=2, sticky=tkinter.W)

    w2_txt19 = tkinter.Label(add_npc_window, text="CHA:")
    w2_txt19.grid(row=10, column=1, sticky=tkinter.E)
    w2_txt20_input = tkinter.Entry(add_npc_window)
    w2_txt20_input.grid(row=10, column=2, sticky=tkinter.W)


    # this is the two long text box
    w2_txt21 = tkinter.Label(add_npc_window, text="Skills:")
    w2_txt21.grid(row=11, column=1, sticky=tkinter.W)
    w2_txt22_input = tkinter.Text(add_npc_window, height=17, width=50)

    # scrollbar
    w2_txt22_sb = tkinter.Scrollbar(add_npc_window)
    w2_txt22_sb.config(command=w2_txt22_input.yview)
    w2_txt22_input.config(yscrollcommand=w2_txt22_sb.set)
    w2_txt22_input.grid(row=11, column=2, sticky=tkinter.W)
    w2_txt22_sb.grid(row=11, column=3, sticky="ns")


    w2_txt23 = tkinter.Label(add_npc_window, text="Actions:")
    w2_txt23.grid(row=12, column=1, sticky=tkinter.W)
    w2_txt24_input = tkinter.Text(add_npc_window, height=10, width=50)


    # scrollbar
    w2_txt24_sb = tkinter.Scrollbar(add_npc_window)
    w2_txt24_sb.config(command=w2_txt24_input.yview)
    w2_txt24_input.config(yscrollcommand=w2_txt24_sb.set)
    w2_txt24_input.grid(row=12, column=2, sticky=tkinter.W)
    w2_txt24_sb.grid(row=12, column=3, sticky="ns")




    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=13)

    #listbox : homebrew or book

    homebrew_listbox = tkinter.Listbox(add_npc_window, height=2)
    for item in ["Homebrew", "Book"]:
        homebrew_listbox.insert(tkinter.END, item)
    homebrew_listbox.grid(row=12, column=4, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)

    #Challange rating rows
    ch_rating_txt = tkinter.Label(add_npc_window, text="Challenge rating:")
    ch_rating_txt.grid(row=17, column=1, sticky=tkinter.W)

    ch_rating_scale = tkinter.Scale(add_npc_window, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    ch_rating_scale.grid(row=17, column=2, sticky=tkinter.W, columnspan=4)

    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)
    # EMPTY ROW
    empty_row = tkinter.Label(add_npc_window, text="")
    empty_row.grid(row=16)

    #CONFRIM BUTTON

    add_monster_btn = tkinter.Button(add_npc_window, text="Add", command=add_npc_to_db)
    add_monster_btn.grid(row=20, column=2)

    # Creature Type Listbox
    add_monster_creature_type_txt = tkinter.Label(add_npc_window, text="Creature Type")
    add_monster_creature_type_txt.grid(row=10, column=4)

    add_monster_creature_type = tkinter.Listbox(add_npc_window, height=17)
    add_monster_creature_type.grid(row=11, column=4)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        add_monster_creature_type.insert(tkinter.END, item)




    add_npc_window.mainloop()


def add_monster_win():
    #declare all f*cking variables as global.........
    global add_monster_window
    global w2_txt1
    global w2_txt2_input
    global w2_txt3
    global w2_txt4_input
    global w2_txt5
    global w2_txt6_input
    global w2_txt7
    global w2_txt8_input
    global w2_txt9
    global w2_txt10_input
    global w2_txt11
    global w2_txt12_input
    global w2_txt13
    global w2_txt14_input
    global w2_txt15
    global w2_txt16_input
    global w2_txt17
    global w2_txt18_input
    global w2_txt19
    global w2_txt20_input
    global w2_txt21
    global w2_txt22_input
    global w2_txt23
    global w2_txt24_input
    global homebrew_txt
    global homebrew_listbox
    global ch_rating_txt
    global ch_rating_scale
    global add_monster_btn
    global add_monster_creature_type_txt
    global add_monster_creature_type

    #window stats
    add_monster_window = tkinter.Tk()
    add_monster_window.title("Add Monster")
    add_monster_window.geometry("700x800")
    add_monster_window.resizable(1, 1)
    add_monster_window.iconbitmap('icon.ico')

    #add monster stats
    w2_txt1 = tkinter.Label(add_monster_window, text="Name:")
    w2_txt1.grid(row=1, column=1, sticky=tkinter.E)
    w2_txt2_input = tkinter.Entry(add_monster_window)
    w2_txt2_input.grid(row=1, column=2, sticky=tkinter.W)

    w2_txt3 = tkinter.Label(add_monster_window, text="Armor Class:")
    w2_txt3.grid(row=2, column=1, sticky=tkinter.E)
    w2_txt4_input = tkinter.Entry(add_monster_window)
    w2_txt4_input.grid(row=2, column=2, sticky=tkinter.W)

    w2_txt5 = tkinter.Label(add_monster_window, text="Hit Points:")
    w2_txt5.grid(row=3, column=1, sticky=tkinter.E)
    w2_txt6_input = tkinter.Entry(add_monster_window)
    w2_txt6_input.grid(row=3, column=2, sticky=tkinter.W)

    w2_txt7 = tkinter.Label(add_monster_window, text="Speed:")
    w2_txt7.grid(row=4, column=1, sticky=tkinter.E)
    w2_txt8_input = tkinter.Entry(add_monster_window)
    w2_txt8_input.grid(row=4, column=2, sticky=tkinter.W)

    w2_txt9 = tkinter.Label(add_monster_window, text="STR:")
    w2_txt9.grid(row=5, column=1, sticky=tkinter.E)
    w2_txt10_input = tkinter.Entry(add_monster_window)
    w2_txt10_input.grid(row=5, column=2, sticky=tkinter.W)

    w2_txt11 = tkinter.Label(add_monster_window, text="DEX:")
    w2_txt11.grid(row=6, column=1, sticky=tkinter.E)
    w2_txt12_input = tkinter.Entry(add_monster_window)
    w2_txt12_input.grid(row=6, column=2, sticky=tkinter.W)

    w2_txt13 = tkinter.Label(add_monster_window, text="CON:")
    w2_txt13.grid(row=7, column=1, sticky=tkinter.E)
    w2_txt14_input = tkinter.Entry(add_monster_window)
    w2_txt14_input.grid(row=7, column=2, sticky=tkinter.W)

    w2_txt15 = tkinter.Label(add_monster_window, text="INT:")
    w2_txt15.grid(row=8, column=1, sticky=tkinter.E)
    w2_txt16_input = tkinter.Entry(add_monster_window)
    w2_txt16_input.grid(row=8, column=2, sticky=tkinter.W)

    w2_txt17 = tkinter.Label(add_monster_window, text="WIS:")
    w2_txt17.grid(row=9, column=1, sticky=tkinter.E)
    w2_txt18_input = tkinter.Entry(add_monster_window)
    w2_txt18_input.grid(row=9, column=2, sticky=tkinter.W)

    w2_txt19 = tkinter.Label(add_monster_window, text="CHA:")
    w2_txt19.grid(row=10, column=1, sticky=tkinter.E)
    w2_txt20_input = tkinter.Entry(add_monster_window)
    w2_txt20_input.grid(row=10, column=2, sticky=tkinter.W)

    #this is the two long text box
    w2_txt21 = tkinter.Label(add_monster_window, text="Skills:")
    w2_txt21.grid(row=11, column=1, sticky=tkinter.W)
    w2_txt22_input = tkinter.Text(add_monster_window, height=17, width=50)

    # scrollbar
    w2_txt22_sb = tkinter.Scrollbar(add_monster_window)
    w2_txt22_sb.config(command=w2_txt22_input.yview)
    w2_txt22_input.config(yscrollcommand=w2_txt22_sb.set)
    w2_txt22_input.grid(row=11, column=2, sticky=tkinter.W)
    w2_txt22_sb.grid(row=11, column=3, sticky="ns")


    w2_txt23 = tkinter.Label(add_monster_window, text="Actions:")
    w2_txt23.grid(row=12, column=1, sticky=tkinter.W)
    w2_txt24_input = tkinter.Text(add_monster_window, height=10, width=50)


    #scrollbar
    w2_txt24_sb = tkinter.Scrollbar(add_monster_window)
    w2_txt24_sb.config(command=w2_txt24_input.yview)
    w2_txt24_input.config(yscrollcommand=w2_txt24_sb.set)
    w2_txt24_input.grid(row=12, column=2, sticky=tkinter.W)
    w2_txt24_sb.grid(row=12, column=3, sticky="ns")


    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=13)

    #listbox : homebrew or book

    homebrew_listbox = tkinter.Listbox(add_monster_window, height=2)
    for item in ["Homebrew", "Book"]:
        homebrew_listbox.insert(tkinter.END, item)
    homebrew_listbox.grid(row=12, column=4, sticky=tkinter.W)

    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)

    #Challange rating rows
    ch_rating_txt = tkinter.Label(add_monster_window, text="Challenge rating:")
    ch_rating_txt.grid(row=17, column=1, sticky=tkinter.W)

    ch_rating_scale = tkinter.Scale(add_monster_window, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    ch_rating_scale.grid(row=17, column=2, sticky=tkinter.W, columnspan=3)

    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)
    # EMPTY ROW
    empty_row = tkinter.Label(add_monster_window, text="")
    empty_row.grid(row=16)

    #CONFRIM BUTTON

    add_monster_btn = tkinter.Button(add_monster_window, text="Add", command=add_monster_to_db)
    add_monster_btn.grid(row=20, column=2)

    # Creature Type Listbox
    add_monster_creature_type_txt = tkinter.Label(add_monster_window, text="Creature Type")
    add_monster_creature_type_txt.grid(row=10, column=4)

    add_monster_creature_type = tkinter.Listbox(add_monster_window, height=17)
    add_monster_creature_type.grid(row=11, column=4)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        add_monster_creature_type.insert(tkinter.END, item)



    add_monster_window.mainloop()

#function for button
def add_monster_to_db():
    #globalling everything...............
    global get_monster_name
    global get_monster_ac
    global get_monster_hp
    global get_monster_speed
    global get_monster_str
    global get_monster_str
    global get_monster_dex
    global get_monster_con
    global get_monster_int
    global get_monster_wis
    global get_monster_cha
    global get_monster_skills
    global get_monster_actions
    global get_monster_homebrew
    global get_monster_challange_rating
    global get_monster_creature_type

    # adding the input values to variables
    get_monster_name = w2_txt2_input.get()
    get_monster_ac = w2_txt4_input.get()
    get_monster_hp = w2_txt6_input.get()
    get_monster_speed = w2_txt8_input.get()
    get_monster_str = w2_txt10_input.get()
    get_monster_dex = w2_txt12_input.get()
    get_monster_con = w2_txt14_input.get()
    get_monster_int = w2_txt16_input.get()
    get_monster_wis = w2_txt18_input.get()
    get_monster_cha = w2_txt20_input.get()
    get_monster_skills = w2_txt22_input.get("1.0",tkinter.END)
    get_monster_actions = w2_txt24_input.get("1.0",tkinter.END)
    get_monster_homebrew = homebrew_listbox.get(tkinter.ACTIVE)
    get_monster_challange_rating = ch_rating_scale.get()
    get_monster_creature_type = add_monster_creature_type.get(tkinter.ACTIVE)

    #connecting to database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()


    c.execute("INSERT INTO monsters (name, ac, hp, speed, str, dex, con, int, wis, cha, skills, actions, challenge_rating, creature_type, homebrew) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (get_monster_name, get_monster_ac, get_monster_hp, get_monster_speed, get_monster_str, get_monster_dex,
         get_monster_con, get_monster_int, get_monster_wis, get_monster_cha, get_monster_skills, get_monster_actions,
         get_monster_challange_rating, get_monster_creature_type, get_monster_homebrew))

    #save and close database
    conn.commit()
    conn.close()

    # printing out that adding was successfully
    add_monster_successfully = tkinter.Label(add_monster_window, text="Adding %s was success." % get_monster_name, fg="red")
    add_monster_successfully.grid(row=21, column=2)


#function for button
def add_npc_to_db():
    # adding the input values to variables
    get_monster_name = w2_txt2_input.get()
    get_monster_ac = w2_txt4_input.get()
    get_monster_hp = w2_txt6_input.get()
    get_monster_speed = w2_txt8_input.get()
    get_monster_str = w2_txt10_input.get()
    get_monster_dex = w2_txt12_input.get()
    get_monster_con = w2_txt14_input.get()
    get_monster_int = w2_txt16_input.get()
    get_monster_wis = w2_txt18_input.get()
    get_monster_cha = w2_txt20_input.get()
    get_monster_skills = w2_txt22_input.get("1.0", tkinter.END)
    get_monster_actions = w2_txt24_input.get("1.0", tkinter.END)
    get_monster_homebrew = homebrew_listbox.get(tkinter.ACTIVE)
    get_monster_challange_rating = ch_rating_scale.get()
    get_monster_creature_type = add_monster_creature_type.get(tkinter.ACTIVE)

    #connecting to database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    # creating table...
    #c.execute("""CREATE TABLE npc (name, ac, hp, speed, str, dex, con, int, wis,
                #cha, skills, actions, challenge_rating, creature_type, homebrew)""")

    c.execute("INSERT INTO npc (name, ac, hp, speed, str, dex, con, int, wis, cha, skills, actions, challenge_rating, creature_type, homebrew) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (get_monster_name, get_monster_ac, get_monster_hp, get_monster_speed, get_monster_str, get_monster_dex,
         get_monster_con, get_monster_int, get_monster_wis, get_monster_cha, get_monster_skills, get_monster_actions,
         get_monster_challange_rating, get_monster_creature_type, get_monster_homebrew))

    for row in c.execute("SELECT rowid, name, speed FROM monsters WHERE homebrew = 'Homebrew'"):
        print(row)

    #save and close database
    conn.commit()
    conn.close()

    # printing out that adding was successfully
    add_monster_successfully = tkinter.Label(add_npc_window, text="Adding %s was success." % get_monster_name,
                                             fg="red")
    add_monster_successfully.grid(row=21, column=2)


    #print(get_monster_name,get_monster_ac,get_monster_hp,get_monster_speed,
    #      get_monster_str, get_monster_dex, get_monster_con, get_monster_int,
    #      get_monster_wis, get_monster_cha)
    #print()
    #print(get_monster_skills, get_monster_actions)
    #
    #print(str(type(get_monster_name))+"("+get_monster_name+")")
    #
    #print("homebrew: "+ str(get_monster_homebrew))
    #print("challange rating: "+str(get_monster_challange_rating))
    #print("creature type: "+str(get_monster_creature_type))



#-------------------------------------------- GENERATE FIGHT ------------------------------------------------

#GENERATE FIGHT ---> BUTTON FUNCTIONS

#---------ADD CHARACTER BUTTON
def gen_fight_char_button_f():
    global generate_fight_character
    generate_fight_character = tkinter.Tk()
    generate_fight_character.title("Add Character")
    generate_fight_character.iconbitmap('icon.ico')

    gen_fight_char_top = tkinter.Label(generate_fight_character, text="Choose one of the following opportunities, than click -Add-")
    gen_fight_char_top.grid(row=1, column=1)

    #connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    #make the table empty:
    c.execute("DELETE FROM fighting_char WHERE rowid > 0")
    #save and close database
    conn.commit()
    conn.close()

    #create the listbox of characters:
    global gen_fight_char_listbox
    gen_fight_char_listbox = tkinter.Listbox(generate_fight_character, height=6, selectbackground="purple")
    gen_fight_char_listbox.grid(row=3, column=1)

    #fill the listbox
    for item in ["Putukas", "Shadow Fury", "Farvizes Sallango", "Ped Ophelia", "Stickee", "Crag Stone"]:
        gen_fight_char_listbox.insert(tkinter.END, item)



    #ADD ALL button
    gen_fight_char_addall_button = tkinter.Button(generate_fight_character, text="ADD ALL", bg="blue", fg="white", command=gen_fight_char_add_all_button_f)
    gen_fight_char_addall_button.grid(row=5, column=1)
    #ADD button
    gen_fight_char_add_button = tkinter.Button(generate_fight_character, text="ADD active", bg="green", fg="black", command=gen_fight_char_add_button_f)
    gen_fight_char_add_button.grid(row=4, column=1)

    #instructions for adding characters

    add_char_instructions = tkinter.Label(generate_fight_character, text="Add characters to the fight one by one, or add all of them in one click. If you fail, just destroy this window and reopen it.", fg="red")
    add_char_instructions.grid(row=2, column=1)

#function for the "ADD ALL" button in the add character window
def gen_fight_char_add_all_button_f():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    for all_fight in ["Putukas", "Shadow Fury", "Farvizes Sallango", "Ped Ophelia", "Stickee", "Crag Stone"]:
        c.execute("INSERT OR IGNORE INTO fighting_char (name) VALUES (?)", (all_fight,))
    # save and close database
    conn.commit()
    conn.close()

    adding_all_was_success1 = tkinter.Label(generate_fight_character, text="Adding all from list was success. You can destroy this window.", fg="green")
    adding_all_was_success1.grid(row=6, column=1)

#function for the "ADD" button in the add character window
def gen_fight_char_add_button_f():
    #get the value:
    global gen_fight_char_value
    gen_fight_char_value = gen_fight_char_listbox.get(tkinter.ACTIVE)
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO fighting_char (name) VALUES (?)", (gen_fight_char_value,))
    #save and close database
    conn.commit()
    conn.close()

    adding_char_was_success = tkinter.Label(generate_fight_character, text="Adding %s was success." % gen_fight_char_value, fg="green")
    adding_char_was_success.grid(row=7, column=1)
# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz
#---------ADD MONSTER BUTTON
def gen_fight_monster_button_f():
    generate_fight_monster = tkinter.Tk()
    generate_fight_monster.title("Add monster to the fight")
    generate_fight_monster.geometry("1600x900")
    generate_fight_monster.iconbitmap('icon.ico')

    gen_fight_monster_search = tkinter.Label(generate_fight_monster, text="Search for monsters!")
    gen_fight_monster_search.grid(row=1, column=1)

    # clearing the database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("DELETE FROM fighting_mon WHERE rowid > 0")
    conn.commit()
    conn.close()

    #searching by name:
    gen_fight_monster_search_name = tkinter.Label(generate_fight_monster, text="Name")
    gen_fight_monster_search_name.grid(row=2, column=1)
    global gen_fight_monster_search_name_entry
    gen_fight_monster_search_name_entry = tkinter.Entry(generate_fight_monster)
    gen_fight_monster_search_name_entry.grid(row=2, column=2)
    gen_fight_monster_search_name_button = tkinter.Button(generate_fight_monster, text="Search by name", command=gen_fight_search_name_button_f)
    gen_fight_monster_search_name_button.grid(row=2, column=3)

    #empty row:
    gen_fight_monster_empty = tkinter.Label(generate_fight_monster)
    gen_fight_monster_empty.grid(row=3, column=1)

    #searching by challange rating:
    global gen_fight_monster_search_cr_scale
    gen_fight_monster_search_cr = tkinter.Label(generate_fight_monster, text="Challange Rating")
    gen_fight_monster_search_cr.grid(row=4, column=1)
    gen_fight_monster_search_cr_scale = tkinter.Scale(generate_fight_monster, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    gen_fight_monster_search_cr_scale.grid(row=4, column=2, sticky=tkinter.W)
    gen_fight_monster_search_cr_button = tkinter.Button(generate_fight_monster, text="Search by CR", command=gen_fight_search_cr_button_f)
    gen_fight_monster_search_cr_button.grid(row=4, column=3)


    #searching by creature type
    gen_fight_monster_search_ct = tkinter.Label(generate_fight_monster, text="Creature Type")
    gen_fight_monster_search_ct.grid(row=6, column=1)
    global gen_fight_monster_search_ct_listbox
    gen_fight_monster_search_ct_listbox = tkinter.Listbox(generate_fight_monster, height=17)
    gen_fight_monster_search_ct_listbox.grid(row=6, column=2)
    gen_fight_monster_search_ct_button = tkinter.Button(generate_fight_monster, text="Search by CT", command=gen_fight_search_ct_button_f)
    gen_fight_monster_search_ct_button.grid(row=6, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        gen_fight_monster_search_ct_listbox.insert(tkinter.END, item)

#function for the "search by name" button
def gen_fight_search_name_button_f():

    global gen_fight_search_name_value
    gen_fight_search_name_value = gen_fight_monster_search_name_entry.get()

    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE name LIKE (? || '%')", (gen_fight_search_name_value,))


    monsters_name_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_name_list.append(to_the_list[0])

    global search_mon_byname
    search_mon_byname = tkinter.Tk()
    search_mon_byname.title("Search Monster by NAME")
    search_mon_byname.geometry("400x400")
    search_mon_byname.iconbitmap('icon.ico')

    global searched_monsters_name
    searched_monsters_name = tkinter.Listbox(search_mon_byname, height=len(monsters_name_list))
    searched_monsters_name.grid(row=1, column=1)
    for item in monsters_name_list:
        searched_monsters_name.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_byname, text="ADD", command=add_monster_to_fight_by_name)
    searched_monsters_add_button.grid(row=2, column=2)


# function to the ADD button in search monsters by name window
def add_monster_to_fight_by_name():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_name.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_byname, text="Adding %s to the fight was success." % searched_monster_todb, fg="blue").grid(row=4, column=1)




#function for the "search by challange rating" button
def gen_fight_search_cr_button_f():
    global gen_fight_monster_search_cr_value
    gen_fight_monster_search_cr_value = gen_fight_monster_search_cr_scale.get()
    #connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE challenge_rating=?", (gen_fight_monster_search_cr_value,))

    monsters_cr_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_cr_list.append(to_the_list[0])

    global search_mon_bycr
    search_mon_bycr = tkinter.Tk()
    search_mon_bycr.title("Search Monster by Challange Rating")
    search_mon_bycr.geometry("400x400")
    search_mon_bycr.iconbitmap('icon.ico')

    global searched_monsters_cr
    searched_monsters_cr = tkinter.Listbox(search_mon_bycr, height=len(monsters_cr_list))
    searched_monsters_cr.grid(row=1, column=1)
    for item in monsters_cr_list:
        searched_monsters_cr.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_bycr, text="ADD", command=add_monster_to_fight_by_cr)
    searched_monsters_add_button.grid(row=2, column=2)


# function to the ADD button in monsters searching by challange rating
def add_monster_to_fight_by_cr():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_cr.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_bycr, text= "Adding %s to the fight was success." %searched_monster_todb, fg="blue").grid(row=4, column=1)


# function for the "search by creature type" button
def gen_fight_search_ct_button_f():
    global gen_fight_monster_search_ct_value
    gen_fight_monster_search_ct_value = gen_fight_monster_search_ct_listbox.get(tkinter.ACTIVE)


    # connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM monsters WHERE creature_type=?", (gen_fight_monster_search_ct_value,))

    monsters_ct_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        monsters_ct_list.append(to_the_list[0])

    global search_mon_byct
    search_mon_byct = tkinter.Tk()
    search_mon_byct.title("Search Monster by Challange Rating")
    search_mon_byct.geometry("400x400")
    search_mon_byct.iconbitmap('icon.ico')

    global searched_monsters_ct
    searched_monsters_ct = tkinter.Listbox(search_mon_byct, height=len(monsters_ct_list))
    searched_monsters_ct.grid(row=1, column=1)
    for item in monsters_ct_list:
        searched_monsters_ct.insert(tkinter.END, item)

    searched_monsters_add_button = tkinter.Button(search_mon_byct, text="ADD", command=add_monster_to_fight_by_ct)
    searched_monsters_add_button.grid(row=2, column=2)


def add_monster_to_fight_by_ct():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_monster_todb = searched_monsters_ct.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_mon (name) VALUES (?)", (searched_monster_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_mon_byct, text="Adding %s to the fight was success." % searched_monster_todb, fg="blue").grid(row=4, column=1)

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz
#---------ADD NPC BUTTON
def gen_fight_npc_button_f():
    generate_fight_npc = tkinter.Tk()
    generate_fight_npc.title("Add NPC to the fight")
    generate_fight_npc.geometry("1600x900")
    generate_fight_npc.iconbitmap('icon.ico')

    gen_fight_npc_search = tkinter.Label(generate_fight_npc, text="Search for NPC!")
    gen_fight_npc_search.grid(row=1, column=1)

    # clearing the database
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("DELETE FROM fighting_npc WHERE rowid > 0")
    conn.commit()
    conn.close()

    #searching by name:
    gen_fight_npc_search_name = tkinter.Label(generate_fight_npc, text="Name")
    gen_fight_npc_search_name.grid(row=2, column=1)
    global gen_fight_npc_search_name_entry
    gen_fight_npc_search_name_entry = tkinter.Entry(generate_fight_npc)
    gen_fight_npc_search_name_entry.grid(row=2, column=2)
    gen_fight_npc_search_name_button = tkinter.Button(generate_fight_npc, text="Search by name", command=gen_fight_search_name_button_f_npc)
    gen_fight_npc_search_name_button.grid(row=2, column=3)

    #empty row:
    gen_fight_npc_empty = tkinter.Label(generate_fight_npc)
    gen_fight_npc_empty.grid(row=3, column=1)

    #searching by challange rating:
    global gen_fight_npc_search_cr_scale
    gen_fight_npc_search_cr = tkinter.Label(generate_fight_npc, text="Challange Rating")
    gen_fight_npc_search_cr.grid(row=4, column=1)
    gen_fight_npc_search_cr_scale = tkinter.Scale(generate_fight_npc, from_=1, to=30, tickinterval=1, orient=tkinter.HORIZONTAL, length=550)
    gen_fight_npc_search_cr_scale.grid(row=4, column=2, sticky=tkinter.W)
    gen_fight_npc_search_cr_button = tkinter.Button(generate_fight_npc, text="Search by CR", command=gen_fight_search_cr_button_f_npc)
    gen_fight_npc_search_cr_button.grid(row=4, column=3)


    #searching by creature type
    gen_fight_npc_search_ct = tkinter.Label(generate_fight_npc, text="Creature Type")
    gen_fight_npc_search_ct.grid(row=6, column=1)
    global gen_fight_npc_search_ct_listbox
    gen_fight_npc_search_ct_listbox = tkinter.Listbox(generate_fight_npc, height=17)
    gen_fight_npc_search_ct_listbox.grid(row=6, column=2)
    gen_fight_npc_search_ct_button = tkinter.Button(generate_fight_npc, text="Search by CT", command=gen_fight_search_ct_button_f_npc)
    gen_fight_npc_search_ct_button.grid(row=6, column=3)
    for item in ["Aberration", "Animal", "Celestial", "Construct", "Dragon",
                 "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Magical Beast",
                 "Monstrous Humanoid", "Ooze", "Outsider", "Plant", "Undead", "Vermin"]:
        gen_fight_npc_search_ct_listbox.insert(tkinter.END, item)

#function for the "search by name" button
def gen_fight_search_name_button_f_npc():

    global gen_fight_search_name_value
    gen_fight_search_name_value = gen_fight_npc_search_name_entry.get()

    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE name LIKE (? || '%')", (gen_fight_search_name_value,))


    npc_name_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_name_list.append(to_the_list[0])

    global search_npc_byname
    search_npc_byname = tkinter.Tk()
    search_npc_byname.title("Search NPC by NAME")
    search_npc_byname.geometry("400x400")
    search_npc_byname.iconbitmap('icon.ico')

    global searched_npc_name
    searched_npc_name = tkinter.Listbox(search_npc_byname, height=len(npc_name_list))
    searched_npc_name.grid(row=1, column=1)
    for item in npc_name_list:
        searched_npc_name.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_byname, text="ADD", command=add_npc_to_fight_by_name)
    searched_npc_add_button.grid(row=2, column=2)


# function to the ADD button in search monsters by name window
def add_npc_to_fight_by_name():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_name.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_byname, text="Adding %s to the fight was success." % searched_npc_todb, fg="blue").grid(row=4, column=1)




#function for the "search by challange rating" button
def gen_fight_search_cr_button_f_npc():
    global gen_fight_npc_search_cr_value
    gen_fight_npc_search_cr_value = gen_fight_npc_search_cr_scale.get()
    #connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE challenge_rating=?", (gen_fight_npc_search_cr_value,))

    npc_cr_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_cr_list.append(to_the_list[0])

    global search_npc_bycr
    search_npc_bycr = tkinter.Tk()
    search_npc_bycr.title("Search NPC by Challange Rating")
    search_npc_bycr.geometry("400x400")
    search_npc_bycr.iconbitmap('icon.ico')

    global searched_npc_cr
    searched_npc_cr = tkinter.Listbox(search_npc_bycr, height=len(npc_cr_list))
    searched_npc_cr.grid(row=1, column=1)
    for item in npc_cr_list:
        searched_npc_cr.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_bycr, text="ADD", command=add_npc_to_fight_by_cr)
    searched_npc_add_button.grid(row=2, column=2)


# function to the ADD button in monsters searching by challange rating
def add_npc_to_fight_by_cr():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_cr.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_bycr, text= "Adding %s to the fight was success." %searched_npc_todb, fg="blue").grid(row=4, column=1)


# function for the "search by creature type" button
def gen_fight_search_ct_button_f_npc():
    global gen_fight_npc_search_ct_value
    gen_fight_npc_search_ct_value = gen_fight_npc_search_ct_listbox.get(tkinter.ACTIVE)


    # connect database and somehow search the fucking list
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    c.execute("SELECT * FROM npc WHERE creature_type=?", (gen_fight_npc_search_ct_value,))

    npc_ct_list = []
    searched_names = c.fetchall()
    for to_the_list in searched_names:
        npc_ct_list.append(to_the_list[0])

    global search_npc_byct
    search_npc_byct = tkinter.Tk()
    search_npc_byct.title("Search NPC by Challange Rating")
    search_npc_byct.geometry("400x400")
    search_npc_byct.iconbitmap('icon.ico')

    global searched_npc_ct
    searched_npc_ct = tkinter.Listbox(search_npc_byct, height=len(npc_ct_list))
    searched_npc_ct.grid(row=1, column=1)
    for item in npc_ct_list:
        searched_npc_ct.insert(tkinter.END, item)

    searched_npc_add_button = tkinter.Button(search_npc_byct, text="ADD", command=add_npc_to_fight_by_ct)
    searched_npc_add_button.grid(row=2, column=2)


def add_npc_to_fight_by_ct():
    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    searched_npc_todb = searched_npc_ct.get(tkinter.ACTIVE)

    c.execute("INSERT INTO fighting_npc (name) VALUES (?)", (searched_npc_todb,))

    # save and close db:
    conn.commit()
    conn.close()

    tkinter.Label(search_npc_byct, text="Adding %s to the fight was success." % searched_npc_todb, fg="blue").grid(row=4, column=1)

# faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasz













# function for the SHOW ADDED button
def gen_fight_show_added_f():
    #clean the shit
    for w in range(15):
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=3)
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=4)
        tkinter.Label(generate_fight_win, text=" "*40).grid(row=w+1, column=5)


    # connect to db:
    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()
    c.execute("SELECT * FROM fighting_char")
    fake_list = []
    global real_list
    real_list = []
    fighting_chars = c.fetchall()
    for item in fighting_chars:
        fake_list.append(item)
    if ("Putukas",) in fake_list:
        real_list.append("Putukas")
    if ("Shadow Fury",) in fake_list:
        real_list.append("Shadow Fury")
    if ("Farvizes Sallango",) in fake_list:
        real_list.append("Farvizes Sallango")
    if ("Ped Ophelia",) in fake_list:
        real_list.append("Ped Ophelia")
    if ("Stickee",) in fake_list:
        real_list.append("Stickee")
    if ("Crag Stone",) in fake_list:
        real_list.append("Crag Stone")


    #this belows prints out the added characters when SHOW ADD button is clicked
    for i in range(len(real_list)):
        tkinter.Label(generate_fight_win, text="ADDED:", bg="black", fg="white").grid(row=1, column=2)
        tkinter.Label(generate_fight_win, text="Characters:", fg="blue").grid(row=1, column=3)
        gen_fight_show_added_chars = tkinter.Label(generate_fight_win, text="{}".format(real_list[i]))
        gen_fight_show_added_chars.grid(row=i+2, column=3)


    monsters_fighting = c.execute("SELECT * FROM fighting_mon")
    real_list2=[]
    for names in monsters_fighting:
        real_list2.append(names)

    for j in range(len(real_list2)):
        tkinter.Label(generate_fight_win, text="Monsters:", fg="blue").grid(row=1, column=4)
        print_the_monster = tkinter.Label(generate_fight_win, text="%s" % (real_list2[j]))
        print_the_monster.grid(row=j+2, column=4)

    npc_fighting = c.execute("SELECT * FROM fighting_npc")
    real_list3 = []
    for names_npc in npc_fighting:
        real_list3.append(names_npc)

    for k in range(len(real_list3)):
        tkinter.Label(generate_fight_win, text="NPC:", fg="blue").grid(row=1, column=5)
        print_the_npc = tkinter.Label(generate_fight_win, text="%s" % (real_list3[k]))
        print_the_npc.grid(row=k + 2, column=5)




#MAIN WINDOW
def generate_fight_window():
    # window stats
    global generate_fight_win
    generate_fight_win = tkinter.Tk()
    generate_fight_win.title("Generate Fight")
    generate_fight_win.geometry("1600x900+0+0")
    generate_fight_win.iconbitmap('icon.ico')
    #generate_fight_win.attributes("-fullscreen", True)
    #generate_fight_win.attributes("-fullscreen", False)

    global gen_fight_show_added_chars
    global print_the_monster
    global print_the_npc


    gen_fight_top = tkinter.Label(generate_fight_win, text="Adding the need to the fight...", fg="blue")
    gen_fight_top.grid(row=1, column=1)

    gen_fight_top_under = tkinter.Label(generate_fight_win, text="What do you want to add to the fight?")
    gen_fight_top_under.grid(row=2, column=1)


    #Buttons for adding:

    gen_fight_char_button = tkinter.Button(generate_fight_win, text="Character", bg="green", fg="white", width=25, command=gen_fight_char_button_f)
    gen_fight_char_button.grid(row=3, column=1)

    gen_fight_monster_button = tkinter.Button(generate_fight_win, text="Monster", bg="red", fg="white", width=25, command=gen_fight_monster_button_f)
    gen_fight_monster_button.grid(row=4, column=1)

    gen_fight_npc_button = tkinter.Button(generate_fight_win, text="NPC", bg="blue", fg="white", width=25, command=gen_fight_npc_button_f)
    gen_fight_npc_button.grid(row=5, column=1)

    gen_fight_show_added_button = tkinter.Button(generate_fight_win, text="Show added", bg="white", fg="black", width=25, command=gen_fight_show_added_f)
    gen_fight_show_added_button.grid(row=6, column=1)

    gen_fight_continue_button = tkinter.Button(generate_fight_win, text="Continue", fg="blue", bg="white", width=25, command=continute_to_initiative)
    gen_fight_continue_button.grid(row=3, column=10)

    #some space column between buttons

    gen_fight_empty1 = tkinter.Label(generate_fight_win)
    gen_fight_empty1.grid(row=8, column=1)

    # instructions:
    instr_text = "Some instructions:\n\nIf you want to add something\nto the fight, you should search\n for it first.\n\n After you click on any search button\n in this window, you make the added\nlist empty, and than you can put\nanything you want." \
                 "\n\nIf you made a mistake while adding, you\ncan reset it by destroying and\nreopening the searching window."
    tkinter.Label(generate_fight_win, text="%s" % (instr_text)).grid(row=9, column=1, rowspan=13, sticky=tkinter.W)

    instr_butt = "\nCHARACTER button:\nadding characters to the fight\nMONSTER button:\nsearching and adding monsters\nNPC button:\nsearching and adding NPCs\nSHOW ADDED button:\nyou can see what's already in the fight" \
                 "\nCONTINUE button:\nyou are ready with adding"
    tkinter.Label(generate_fight_win, text="%s" % (instr_butt), fg="blue").grid(row=25, column=1, rowspan=10)






# "CONTINUE" BUTTON FUNCTION to the initiative

def continute_to_initiative():

    global initiative_window
    initiative_window = tkinter.Tk()
    initiative_window.title("Giving Initiatives")
    initiative_window.geometry("300x900+500+0")
    initiative_window.iconbitmap('icon.ico')

    #clearing
    for clear in range(2):
        for clearing in range(100):
            tkinter.Label(initiative_window, text=" "*30).grid(row=clearing+1, column=clear+1)


    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()


    select_char = c.execute("SELECT name FROM fighting_char")
    global fighting_character_list
    fighting_character_list = []
    for row in select_char:
        fighting_character_list.append(row)

    label1 = tkinter.Label(initiative_window, text="Characters:", fg="green")
    label1.grid(row=1, column=1)
    label2 = tkinter.Label(initiative_window, text="Initiatives:", fg="blue")
    label2.grid(row=1, column=2)

    # START BUTTON
    tkinter.Button(initiative_window, text="FASZ", command=initiative_start_f).grid(row=5, column=5)

    # ezt itt folul muszaj folytatni ez igy tud mukodni!!!!!!
    # ez a globals() cucc olyat tud, hogy egy loopon belul tobb kulonbozo valtozot hozol letre...
    # ez itt nekunk azert jo, mert igy megcsinalhatjuk a kezdemenyezos ablakot
    # egy oszlop karakter, mellette a tkinter.Entry cuccos,
    # es az entrynek hozunk letre valtozot ezzel a globals() funkcioval
    # pl:

    for i in range(len(fighting_character_list)):
        tkinter.Label(initiative_window, text="%s" % (fighting_character_list[i])).grid(row=i+2, column=1)
        globals()['char_init_entry_%s' % str(i+1)] = tkinter.Entry(initiative_window, width=4)
        globals()['char_init_entry_%s' % str(i+1)].grid(row=i+2, column=2)

    select_mon = c.execute("SELECT name FROM fighting_mon")
    global fighting_monster_list
    fighting_monster_list = []
    for row2 in select_mon:
        fighting_monster_list.append(row2)

    label3 = tkinter.Label(initiative_window, text="Monsters:", fg="red")
    label3.grid(row=len(fighting_character_list)+2, column=1)
    label4 = tkinter.Label(initiative_window, text="Initiatives:", fg="blue")
    label4.grid(row=len(fighting_character_list)+2, column=2)

    select_npc = c.execute("SELECT name FROM fighting_npc")
    global fighting_npc_list
    fighting_npc_list = []
    for row3 in select_npc:
        fighting_npc_list.append(row3)

    label5 = tkinter.Label(initiative_window, text="NPC:", fg="purple")
    label5.grid(row=len(fighting_character_list) + len(fighting_monster_list) + 3, column=1)
    label6 = tkinter.Label(initiative_window, text="Initiatives:", fg="blue")
    label6.grid(row=len(fighting_character_list) + len(fighting_monster_list) + 3, column=2)



    # printing out the monster's names
    for f in range(len(fighting_monster_list)):
        tkinter.Label(initiative_window, text="%s" % (fighting_monster_list[f])).grid(row=(len(fighting_character_list)+f+3), column=1)
    # printing out the entries for the monsters initiatives and make variables for them
    for g in range(len(fighting_monster_list)):
        globals()['mon_init_entry_%s' % str(g+1)] = tkinter.Entry(initiative_window, width=4)
        globals()['mon_init_entry_%s' % str(g+1)].grid(row=(len(fighting_character_list)+g+3), column=2)

    # printing out the npc's names
    for a in range(len(fighting_npc_list)):
        tkinter.Label(initiative_window, text="%s" % (fighting_npc_list[a])).grid(row=(len(fighting_character_list) + len(fighting_monster_list) + a + 4), column=1)
    # printing out the entries for the npc initiatives and make variables for them
    for b in range(len(fighting_npc_list)):
        globals()['npc_init_entry_%s' % str(b + 1)] = tkinter.Entry(initiative_window, width=4)
        globals()['npc_init_entry_%s' % str(b + 1)].grid(row=(len(fighting_character_list) + len(fighting_monster_list) + b + 4), column=2)








def start_the_fight6_10():
    global started_fight_window6_10
    started_fight_window6_10 = tkinter.Tk()
    started_fight_window6_10.title("Monsters ---> 1-5")
    started_fight_window6_10.geometry("1420x650+300+200")
    started_fight_window6_10.iconbitmap('icon.ico')

    # okay let's see:

    # --------------------FOR THE FIGHT WINDOW---------------------- started_fight_window

    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    duplicated_monsters = []
    duplicated_monsters2 = []
    for idontknow in real_fighting_monster_list:
        if idontknow in duplicated_monsters:
            duplicated_monsters2[duplicated_monsters.index(idontknow)][1] = \
            duplicated_monsters2[duplicated_monsters.index(idontknow)][1] + 1
            print('faszom')
        else:
            duplicated_monsters.append(idontknow)
            duplicated_monsters2.append([idontknow, 1])

    print('duplicated_monsters = ', duplicated_monsters)
    print('duplicated_monsters2 = ', duplicated_monsters2)

    print("duplicated_monsters2 lista len() fuggvenye: " + str(len(duplicated_monsters2)))

    global fighting_monsters_len_count
    global fighting_monsters_with_count
    # ez itt nekem most kurvafontos !!! 2019.12.05. (december)
    # ezek alapjan lehet megcsinalni majd a harc elkezdodott ablakot 'normalisan'
    fighting_monsters_with_count = duplicated_monsters2
    fighting_monsters_len_count = int(len(duplicated_monsters2))

    print('fighting_monsters_with_count = {}\nfighting_monsters_len_count = {}'.format(fighting_monsters_with_count,
                                                                                       fighting_monsters_len_count))

    # group of widgets

    db_column_names = ['Name: ', 'Armor Class: ', 'Hit Points: ', 'Speed: ',
                       'Strength: ', 'Dexterity: ', 'Constitution: ', 'Intelligence: ',
                       'Wisdom: ', 'Charisma: ', 'Skills: ', 'Actions: ',
                       'Challange Rating: ', 'Creature Type: ', 'Homebrew: ']

    show_Monster = []
    show_Npc = []

    for mm in range(fighting_monsters_len_count):
        get_Monster = c.execute('SELECT * FROM monsters WHERE name=?', ([fighting_monsters_with_count[mm][0]]))
        for row in get_Monster:
            for mn in range(len(row)):
                show_Monster.append(row[mn])
    print("1 show_Monster = " + str(show_Monster))

    # case 1: if there's 5 or less monsters against us in the fight:
    if fighting_monsters_len_count <= 10:

        for many in range(5, fighting_monsters_len_count):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(started_fight_window6_10, text="%s" % (db_column_names[col])).grid(row=col + 1,
                                                                                             column=((3 * many) + 1),
                                                                                             sticky=tkinter.E)

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(started_fight_window6_10, text="%s" % (show_Monster[(many * 15) + dol])).grid(row=dol + 1,
                                                                                                        column=((
                                                                                                                            3 * many) + 2),
                                                                                                        sticky=tkinter.W)

            # skills and fill + scrollbar
            geci = tkinter.Text(started_fight_window6_10, width=20, height=5)
            geci.grid(row=11, column=((3 * many) + 2), sticky=tkinter.W)
            geci.insert(tkinter.END, str(show_Monster[(many * 15) + 10]))

            sb = tkinter.Scrollbar(started_fight_window6_10, command=geci.yview)
            sb.grid(row=11, column=((3 * many) + 3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(started_fight_window6_10, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2), sticky=tkinter.W)
            geci1.insert(tkinter.END, str(show_Monster[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(started_fight_window6_10, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)

            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(started_fight_window6_10, text="%s" % (show_Monster[(many * 15) + (fol + 12)])).grid(
                    row=13 + fol, column=((3 * many) + 2), sticky=tkinter.W)

            # HP textboxes
            tkinter.Label(started_fight_window6_10, text="HP").grid(row=16, column=((3 * many) + 1), sticky=tkinter.E)
            hp_textwidget_monsters = tkinter.Text(started_fight_window6_10, width=8, height=10)
            hp_textwidget_monsters.grid(row=16, column=((3 * many) + 2), sticky=tkinter.W)

            hpsb = tkinter.Scrollbar(started_fight_window6_10, command=hp_textwidget_monsters.yview)
            hpsb.grid(row=16, column=((3 * many) + 2), ipady=50)
            hp_textwidget_monsters.config(yscrollcommand=hpsb.set)

            for szexnevek in range(fighting_monsters_with_count[many][1]):
                hp_textwidget_monsters.insert(tkinter.END,
                                              ('%s: %s\n' % (szexnevek + 1, show_Monster[(many * 15) + 2])))


    # case 2: if fighting monsters against us are more than 5
    elif fighting_monsters_len_count > 10:

        for many in range(5, 10):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(started_fight_window6_10, text="%s" % (db_column_names[col])).grid(row=col + 1,
                                                                                             column=((3 * many) + 1),
                                                                                             sticky=tkinter.E)

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(started_fight_window6_10, text="%s" % (show_Monster[(many * 15) + dol])).grid(row=dol + 1,
                                                                                                        column=((
                                                                                                                            3 * many) + 2),
                                                                                                        sticky=tkinter.W)

            # skills and fill + scrollbar
            geci = tkinter.Text(started_fight_window6_10, width=20, height=5)
            geci.grid(row=11, column=((3 * many) + 2), sticky=tkinter.W)
            geci.insert(tkinter.END, str(show_Monster[(many * 15) + 10]))

            sb = tkinter.Scrollbar(started_fight_window6_10, command=geci.yview)
            sb.grid(row=11, column=((3 * many) + 3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(started_fight_window6_10, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2), sticky=tkinter.W)
            geci1.insert(tkinter.END, str(show_Monster[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(started_fight_window6_10, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)

            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(started_fight_window6_10, text="%s" % (show_Monster[(many * 15) + (fol + 12)])).grid(
                    row=13 + fol, column=((3 * many) + 2), sticky=tkinter.W)

            # HP textboxes
            tkinter.Label(started_fight_window6_10, text="HP").grid(row=16, column=((3 * many) + 1), sticky=tkinter.E)
            hp_textwidget_monsters = tkinter.Text(started_fight_window6_10, width=8, height=10)
            hp_textwidget_monsters.grid(row=16, column=((3 * many) + 2), sticky=tkinter.W)

            hpsb = tkinter.Scrollbar(started_fight_window6_10, command=hp_textwidget_monsters.yview)
            hpsb.grid(row=16, column=((3 * many) + 2), ipady=50)
            hp_textwidget_monsters.config(yscrollcommand=hpsb.set)

            for szexnevek in range(fighting_monsters_with_count[many][1]):
                hp_textwidget_monsters.insert(tkinter.END,
                                              ('%s: %s\n' % (szexnevek + 1, show_Monster[(many * 15) + 2])))















def start_the_fight():
    print("elkezdodott")
    global started_fight_window
    started_fight_window = tkinter.Tk()
    started_fight_window.title("Monsters ---> 1-5")
    started_fight_window.geometry("1420x650+300+0")
    started_fight_window.iconbitmap('icon.ico')

    # --------------------FOR THE INITIATIVE WINDOW----------------------

    global started_init_window
    started_init_window = tkinter.Tk()
    started_init_window.title("Initiative")
    started_init_window.geometry("300x1080+0+0")
    started_init_window.iconbitmap('icon.ico')


    tkinter.Label(started_init_window, text=" " * 5).grid(row=2, column=1)

    tkinter.Label(started_init_window, text="Names", fg="blue").grid(row=1, column=2)
    tkinter.Label(started_init_window, text="Initiatives", fg="blue").grid(row=1, column=3)
    tkinter.Label(started_init_window, text="Number", fg="blue").grid(row=1, column=4)

    for i in range(len_paired_inits):
        tkinter.Label(started_init_window, text="%s" % (paired_initiatives[i][0])).grid(row=i+2, column=2, sticky=tkinter.W)
        tkinter.Label(started_init_window, text="%s" % (paired_initiatives[i][1])).grid(row=i+2, column=3)
        tkinter.Entry(started_init_window, width=5).grid(row=i+2, column=4)


    tkinter.Button(started_init_window, text="Next", bg="green", fg="white", command=init_next_button_f).grid(row=len_paired_inits+3, column=3)

    tkinter.Button(started_init_window, text="End Fight", bg="red", fg="white", command=end_fight).grid(row=len_paired_inits+3, column=1)


    global make_green
    make_green = 2

    # --------------------FOR THE FIGHT WINDOW---------------------- started_fight_window

    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    #geci = c.execute('SELECT * FROM monsters WHERE name=?', fighting_monster_list[0])
    #print("EZ A SELECT BUZISAG:\n")
    #punci=[]
    #for row in geci:
    #    for pocs in range(len(row)):
    #        punci.append(row[pocs])
    #print(punci)


    duplicated_monsters = []
    duplicated_monsters2 = []
    for idontknow in real_fighting_monster_list:
        if idontknow in duplicated_monsters:
            duplicated_monsters2[duplicated_monsters.index(idontknow)][1] = duplicated_monsters2[duplicated_monsters.index(idontknow)][1] + 1
            print('faszom')
        else:
            duplicated_monsters.append(idontknow)
            duplicated_monsters2.append([idontknow, 1])

    print('duplicated_monsters = ', duplicated_monsters)
    print('duplicated_monsters2 = ', duplicated_monsters2)

    print("duplicated_monsters2 lista len() fuggvenye: " + str(len(duplicated_monsters2)))


    global fighting_monsters_len_count
    global fighting_monsters_with_count
    # ez itt nekem most kurvafontos !!! 2019.12.05. (december)
    # ezek alapjan lehet megcsinalni majd a harc elkezdodott ablakot 'normalisan'
    fighting_monsters_with_count = duplicated_monsters2
    fighting_monsters_len_count = int(len(duplicated_monsters2))

    print('fighting_monsters_with_count = {}\nfighting_monsters_len_count = {}'.format(fighting_monsters_with_count, fighting_monsters_len_count))




    # group of widgets

    db_column_names = ['Name: ', 'Armor Class: ', 'Hit Points: ', 'Speed: ',
                       'Strength: ', 'Dexterity: ', 'Constitution: ', 'Intelligence: ',
                       'Wisdom: ', 'Charisma: ', 'Skills: ', 'Actions: ',
                       'Challange Rating: ', 'Creature Type: ', 'Homebrew: ']

    show_Monster = []
    show_Npc = []

    for mm in range(fighting_monsters_len_count):
        get_Monster = c.execute('SELECT * FROM monsters WHERE name=?', ([fighting_monsters_with_count[mm][0]]))
        for row in get_Monster:
            for mn in range(len(row)):
                show_Monster.append(row[mn])
    print("1 show_Monster = " + str(show_Monster))


    # case 1: if there's 5 or less monsters against us in the fight:
    if fighting_monsters_len_count <= 5:

        for many in range(fighting_monsters_len_count):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(started_fight_window, text="%s" % (db_column_names[col])).grid(row=col+1, column=((3*many)+1), sticky=tkinter.E)

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(started_fight_window, text="%s" % (show_Monster[(many*15)+dol])).grid(row=dol+1, column=((3*many)+2), sticky=tkinter.W)


            # skills and fill + scrollbar
            geci = tkinter.Text(started_fight_window, width=20, height=5)
            geci.grid(row=11, column=((3*many)+2), sticky=tkinter.W)
            geci.insert(tkinter.END, str(show_Monster[(many*15)+10]))

            sb = tkinter.Scrollbar(started_fight_window, command=geci.yview)
            sb.grid(row=11, column=((3*many)+3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(started_fight_window, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2), sticky=tkinter.W)
            geci1.insert(tkinter.END, str(show_Monster[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(started_fight_window, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)


            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(started_fight_window, text="%s" % (show_Monster[(many*15)+(fol+12)])).grid(row=13+fol, column=((3*many)+2), sticky=tkinter.W)

            # HP textboxes
            tkinter.Label(started_fight_window, text="HP").grid(row=16, column=((3*many)+1), sticky=tkinter.E)
            hp_textwidget_monsters = tkinter.Text(started_fight_window, width=8, height=10)
            hp_textwidget_monsters.grid(row=16, column=((3*many)+2), sticky=tkinter.W)

            hpsb = tkinter.Scrollbar(started_fight_window, command=hp_textwidget_monsters.yview)
            hpsb.grid(row=16, column=((3*many)+2), ipady=50)
            hp_textwidget_monsters.config(yscrollcommand=hpsb.set)

            for szexnevek in range(fighting_monsters_with_count[many][1]):
                hp_textwidget_monsters.insert(tkinter.END, ('%s: %s\n' % (szexnevek+1, show_Monster[(many*15)+2])))


    #case 2: if fighting monsters against us are more than 5
    elif fighting_monsters_len_count > 5:

        for many in range(5):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(started_fight_window, text="%s" % (db_column_names[col])).grid(row=col + 1,
                                                                                             column=((3 * many) + 1),
                                                                                             sticky=tkinter.E)

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(started_fight_window, text="%s" % (show_Monster[(many * 15) + dol])).grid(row=dol + 1,
                                                                                                        column=((3 * many) + 2),
                                                                                                        sticky=tkinter.W)

            # skills and fill + scrollbar
            geci = tkinter.Text(started_fight_window, width=20, height=5)
            geci.grid(row=11, column=((3 * many) + 2), sticky=tkinter.W)
            geci.insert(tkinter.END, str(show_Monster[(many * 15) + 10]))

            sb = tkinter.Scrollbar(started_fight_window, command=geci.yview)
            sb.grid(row=11, column=((3 * many) + 3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(started_fight_window, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2), sticky=tkinter.W)
            geci1.insert(tkinter.END, str(show_Monster[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(started_fight_window, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)

            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(started_fight_window, text="%s" % (show_Monster[(many * 15) + (fol + 12)])).grid(
                    row=13 + fol, column=((3 * many) + 2), sticky=tkinter.W)

            # HP textboxes
            tkinter.Label(started_fight_window, text="HP").grid(row=16, column=((3 * many) + 1), sticky=tkinter.E)
            hp_textwidget_monsters = tkinter.Text(started_fight_window, width=8, height=10)
            hp_textwidget_monsters.grid(row=16, column=((3 * many) + 2), sticky=tkinter.W)

            hpsb = tkinter.Scrollbar(started_fight_window, command=hp_textwidget_monsters.yview)
            hpsb.grid(row=16, column=((3 * many) + 2), ipady=50)
            hp_textwidget_monsters.config(yscrollcommand=hpsb.set)

            for szexnevek in range(fighting_monsters_with_count[many][1]):
                hp_textwidget_monsters.insert(tkinter.END,
                                              ('%s: %s\n' % (szexnevek + 1, show_Monster[(many * 15) + 2])))


    # add a function window to the right:
    global fight_function_window
    fight_function_window = tkinter.Tk()
    fight_function_window.title("Functions")
    fight_function_window.geometry('190x1080+1720+0')
    fight_function_window.iconbitmap('icon.ico')









def initiative_start_f():

    # for characters
    character_list = []
    character_initiatives = []
    for j in fighting_character_list:
        character_list.append(j)
    for i in range(len(fighting_character_list)):
        character_initiatives.append(globals()['char_init_entry_%s' % str(i + 1)].get())
    #testing that this shit works
    print("Chars:")
    for k in range(len(character_list)):
        print(str(character_list[k]) + ": " + str(character_initiatives[k]))

    print("Character initiatives: "+str(character_initiatives))
    character_initiatives = list(map(int, character_initiatives))
    print("Inted character inits: "+ str(character_initiatives))



    # for monsters
    monster_list = []
    monster_initiatives = []
    for l in fighting_monster_list:
        monster_list.append(l)
    for m in range(len(fighting_monster_list)):
        monster_initiatives.append(globals()['mon_init_entry_%s' % str(m + 1)].get())
    # testing that this shit works
    print("Monsters:")
    for n in range(len(monster_list)):
        print(str(monster_list[n]) + ": " + str(monster_initiatives[n]))

    print("Monster initiatives: "+str(monster_initiatives))
    monster_initiatives = list(map(int, monster_initiatives))
    print("Inted monster initiatives: "+str(monster_initiatives))

    # for npc
    npc_list = []
    npc_initiatives = []
    for e in fighting_npc_list:
        npc_list.append(e)
    for f in range(len(fighting_npc_list)):
        npc_initiatives.append(globals()['npc_init_entry_%s' % str(f + 1)].get())
    # testing that this shit works
    print("NPC:")
    for g in range(len(npc_list)):
        print(str(npc_list[g]) + ": " + str(npc_initiatives[g]))

    print("NPC initiatives: "+str(npc_initiatives))
    npc_initiatives = list(map(int, npc_initiatives))
    print("Inted NPC initiatives: "+str(npc_initiatives))

    # make the initiatives sorted and connecting them to their names

    # make the names in pair with initiative numbers in a list:
    global paired_initiatives
    paired_initiatives = []

    for aa, ab in zip(character_list, character_initiatives):
        paired_initiatives.append([aa, ab])

    for ac, ad in zip(monster_list, monster_initiatives):
        paired_initiatives.append([ac, ad])

    for ae, af in zip(npc_list, npc_initiatives):
        paired_initiatives.append([ae, af])

    # function for taking the second element of the lists
    def takeSecond(element):
        return element[1]
    print("unsorted: " + str(paired_initiatives))
    paired_initiatives.sort(key=takeSecond, reverse=True)
    print("sorted: " + str(paired_initiatives))

    global len_paired_inits
    len_paired_inits = len(paired_initiatives)

    # destroy all the windows (except the main window)
    initiative_window.destroy()
    generate_fight_win.destroy()

    howMany_enemies = int(len(fighting_monster_list))
    howMany_npcs = int(len(fighting_npc_list))


    print("fighting_monster_list = " +str(fighting_monster_list))
    bad_characters = ['[', ']', ',', '\'', '(', ')']
    vesszonelkul = str(fighting_monster_list)
    for changethis in bad_characters:
        vesszonelkul = vesszonelkul.replace(changethis, '')

    print(type(vesszonelkul))
    print('vesszonelkul = '+str(vesszonelkul))

    global real_fighting_monster_list
    real_fighting_monster_list = list(vesszonelkul.split(" "))

    print("real_fighting_monster_list = "+ str(real_fighting_monster_list))
    print("fighting_monster_list = " + str(fighting_monster_list))

    global fighting_monsters_len_count
    global fighting_monsters_with_count

    duplicated_monsters = []
    duplicated_monsters2 = []
    for idontknow in real_fighting_monster_list:
        if idontknow in duplicated_monsters:
            duplicated_monsters2[duplicated_monsters.index(idontknow)][1] = \
            duplicated_monsters2[duplicated_monsters.index(idontknow)][1] + 1
            print('faszom')
        else:
            duplicated_monsters.append(idontknow)
            duplicated_monsters2.append([idontknow, 1])

    print('duplicated_monsters = ', duplicated_monsters)
    print('duplicated_monsters2 = ', duplicated_monsters2)

    print("duplicated_monsters2 lista len() fuggvenye: " + str(len(duplicated_monsters2)))

    global fighting_monsters_len_count
    global fighting_monsters_with_count
    # ez itt nekem most kurvafontos !!! 2019.12.05. (december)
    # ezek alapjan lehet megcsinalni majd a harc elkezdodott ablakot 'normalisan'
    fighting_monsters_with_count = duplicated_monsters2
    fighting_monsters_len_count = int(len(duplicated_monsters2))





    if fighting_monsters_len_count < 6:
        start_the_fight()
    elif fighting_monsters_len_count > 5 and fighting_monsters_len_count < 11:
        start_the_fight6_10()
        start_the_fight()
    elif fighting_monsters_len_count > 10 and fighting_monsters_len_count < 16:
        pass
    elif fighting_monsters_len_count > 15 and fighting_monsters_len_count < 21:
        pass

    if howMany_npcs < 6:
        npc_infight()







def end_fight():
    try:
        started_fight_window.destroy()
    except:
        pass
    try:
        started_init_window.destroy()
    except:
        pass
    try:
        npc_infight_window.destroy()
    except:
        pass
    try:
        fight_function_window.destroy()
    except:
        pass
    try:
        started_fight_window6_10.destroy()
    except:
        pass



def npc_infight():
    print("elkezdodott")
    global npc_infight_window
    npc_infight_window = tkinter.Tk()
    npc_infight_window.title("NPCs ---> 1-5")
    npc_infight_window.geometry("1420x470+300+680")
    npc_infight_window.iconbitmap('icon.ico')


    # --------------------FOR THE FIGHT WINDOW---------------------- started_fight_window

    conn = sqlite3.connect('dnd.db')
    c = conn.cursor()

    # geci = c.execute('SELECT * FROM monsters WHERE name=?', fighting_monster_list[0])
    # print("EZ A SELECT BUZISAG:\n")
    # punci=[]
    # for row in geci:
    #    for pocs in range(len(row)):
    #        punci.append(row[pocs])
    # print(punci)

    # group of widgets

    db_column_names = ['Name: ', 'Armor Class: ', 'Hit Points: ', 'Speed: ',
                       'Strength: ', 'Dexterity: ', 'Constitution: ', 'Intelligence: ',
                       'Wisdom: ', 'Charisma: ', 'Skills: ', 'Actions: ',
                       'Challange Rating: ', 'Creature Type: ', 'Homebrew: ']

    show_Monster = []
    show_Npc = []

    for nn in range(len(fighting_npc_list)):
        get_Npc = c.execute('SELECT * FROM npc WHERE name=?', (fighting_npc_list[nn]))
        for row in get_Npc:
            for no in range(len(row)):
                show_Npc.append(row[no])
    print("show_Npc = " + str(show_Npc))

    # case 1: if there's 5 or less monsters against us in the fight:
    if len(fighting_npc_list) <= 5:

        for many in range(len(fighting_npc_list)):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(npc_infight_window, text="%s" % (db_column_names[col])).grid(row=col + 1, column=((3 * many) + 1))

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(npc_infight_window, text="%s" % (show_Npc[(many * 15) + dol])).grid(row=dol + 1, column=((3 * many) + 2))

            # entry box for hit points
            segg = tkinter.Entry(npc_infight_window, width=5)
            segg.insert(0, "(0)")
            segg.grid(row=1, column=((3 * many) + 3))

            # entry box for name (x)
            tkinter.Entry(npc_infight_window, width=5).grid(row=3, column=((3 * many) + 3))

            # skills and fill + scrollbar
            geci = tkinter.Text(npc_infight_window, width=20, height=5)
            geci.grid(row=11, column=((3 * many) + 2))
            geci.insert(tkinter.END, str(show_Npc[(many * 15) + 10]))

            sb = tkinter.Scrollbar(npc_infight_window, command=geci.yview)
            sb.grid(row=11, column=((3 * many) + 3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(npc_infight_window, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2))
            geci1.insert(tkinter.END, str(show_Npc[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(npc_infight_window, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)

            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(npc_infight_window, text="%s" % (show_Npc[(many * 15) + (fol + 12)])).grid(
                    row=13 + fol, column=((3 * many) + 2))

    # case 2: if fighting monsters against us are more than 5
    elif len(fighting_npc_list) > 5:

        for many in range(5):
            # first 10 stats..
            for col in range(15):
                tkinter.Label(npc_infight_window, text="%s" % (db_column_names[col])).grid(row=col + 1,
                                                                                             column=((3 * many) + 1))

            # first 10 stats values..
            for dol in range(10):
                tkinter.Label(npc_infight_window, text="%s" % (show_Npc[(many * 15) + dol])).grid(row=dol + 1,
                                                                                                        column=((
                                                                                                                        3 * many) + 2))
            # entry box for hit points
            segg = tkinter.Entry(npc_infight_window, width=5)
            segg.insert(0, "(0)")
            segg.grid(row=1, column=((3 * many) + 3))

            # entry box for hit points
            tkinter.Entry(npc_infight_window, width=5).grid(row=3, column=((3 * many) + 3))

            # skills and fill + scrollbar
            geci = tkinter.Text(npc_infight_window, width=20, height=5)
            geci.grid(row=11, column=((3 * many) + 2))
            geci.insert(tkinter.END, str(show_Npc[(many * 15) + 10]))

            sb = tkinter.Scrollbar(npc_infight_window, command=geci.yview)
            sb.grid(row=11, column=((3 * many) + 3), ipady=20)
            geci.config(yscrollcommand=sb.set)

            # actions and fill + scrollbar
            geci1 = tkinter.Text(npc_infight_window, width=20, height=5)
            geci1.grid(row=12, column=((3 * many) + 2))
            geci1.insert(tkinter.END, str(show_Npc[(many * 15) + 11]))

            sb1 = tkinter.Scrollbar(npc_infight_window, command=geci1.yview)
            sb1.grid(row=12, column=((3 * many) + 3), ipady=20)
            geci1.config(yscrollcommand=sb1.set)

            # CR, CT, Homebrew
            for fol in range(3):
                tkinter.Label(npc_infight_window, text="%s" % (show_Npc[(many * 15) + (fol + 12)])).grid(
                    row=13 + fol, column=((3 * many) + 2))


















def init_next_button_f():
    global make_green
    if make_green < len_paired_inits+2:
        tkinter.Label(started_init_window, text="   -->  ", bg="green", fg="white").grid(row=make_green, column=1)
        tkinter.Label(started_init_window, text=" " * 15).grid(row=make_green-1, column=1)



        make_green = make_green + 1
    else:
        tkinter.Label(started_init_window, text=" " * 15).grid(row=make_green-1, column=1)
        tkinter.Label(started_init_window, text="  -->  ", bg="green", fg="white").grid(row=2, column=1)
        make_green = 3

    print("make_green = "+str(make_green))








main_win()
