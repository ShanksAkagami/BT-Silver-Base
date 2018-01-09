label ginny_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ changeGinny(1,665,10) #whatt
    
    call ginny_main("Hello, Hermione said you wanted to see me, professor...") 
    m "{size=-4}(wow, she's hot.){/size}"
    m "Miss Weasley, i found something very disturbing."
    call ginny_main("Of course, sir.", 1)
    label ginny_secondmenu: #temporary
    menu:
        "-Personal Favours-":
            "To be done."
            jump ginny_secondmenu 
        "-Public Favours-":
            "To be done."
            jump ginny_secondmenu
        "-Toggle shirt-":
            if gw_wear_top == True:
                $ gw_wear_top = False
            else:
                $ gw_wear_top = True
            call ginny_main("...", 1)
            jump ginny_secondmenu
        "-Toggle bra-":
            if gw_wear_bra == True:
                $ gw_wear_bra = False
            else:
                $ gw_wear_bra = True
            call ginny_main("...", 1)
            jump ginny_secondmenu
        "-Toggle skirt-":
            if gw_wear_skirt == True:
                $ gw_wear_skirt = False
            else:
                $ gw_wear_skirt = True
            call ginny_main("Pervert...", 1)
            jump ginny_secondmenu
        "-Toggle panties-":
            if gw_wear_panties == True:
                $ gw_wear_panties = False
            else:
                $ gw_wear_panties = True
            call ginny_main("...", 1)
            jump ginny_secondmenu
        "-Dismiss Her-":
            hide screen ginny_weasley
            call reset_ginny
            with d3
            jump day_main_menu

label reset_ginny:
    $ gw_wear_panties = True
    $ gw_wear_bra = True
    $ gw_wear_skirt = True
    $ gw_wear_top = True
    return

