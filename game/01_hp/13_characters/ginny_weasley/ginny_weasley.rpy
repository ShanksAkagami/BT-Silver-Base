label ginny_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $ changeGinny(1,2,1,665,10) #whatt
    if not ginny_met:
        $ ginny_met = True
        call ginny_main("Hello professor, you wanted to see me?") 
        $ changeGinny(1,1)
        m "{size=-4}(wow, she's hot.){/size}"
        m "{size=-4}(but that damm robe is blocking the view.){/size}"
        if not fire_in_fireplace:
                #$ renpy.play('sounds/fire01.ogg')  
                #play bg_sounds "sounds/fire01.ogg" fadeout 1.0 fadein 1.0 #LOUD!
                #play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
            m "{size=+4}lightus firus!!!!{/size}"
            $ fire_in_fireplace = True
            show screen fireplace_fire
        m "Welcome miss Weasley, please feel free to take off your robe, the fire will keep us warm"
        ">Ginny removes her robes and put them on the chair next to her."
        $ gw_wear_robes = False
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1
        call ginny_main("Of course, sir, thanks.", 1, 2)
        call ginny_main("This feels beter", 1, 1, 5)
        g9 "{size=-4}(much better.){/size}"
        m "{size=-4}(This girl walks around dressed like that and this Hagrid Peter doesn't even notice her, what the hell is wrong with this guy??{/size})"
        call ginny_main("So, professor, what did you wannna speak with me?", 1, 2, 6)
        #m "Miss Weasley, there is something that I need to discuss with you."
        m "Oh, right."
        m "While I was inspecting the dorms I found this"
        ">You show her the diary"
        $ renpy.play('sounds/scratch.wav')
        stop music
        $ changeGinny(1,3,3)
        m "Do you recognize it miss Weasley?"
        call ginny_main("That.. thats my diary")
        call ginny_main("Professor, I can explain it", 1, 6, 7)
        m "Of course you can explai- Wait, what?"
        m "{size=-4}(I took her diary and she is the one that has to explain it?? Better just hear it.{/size})"
        call ginny_main("This is just a regular diary, it has nothing to do with that one that caused that huge problem a few years ago", 1, 2, 7)
        m "{size=-4}(Now that's interesting.{/size})"
        g9 "So you do understand the reason why I had to thoroughly inspect it right girl?"
        call ginny_main("Yeah, I do...", 1, 6, 8)
        play music "music/Anguish.mp3" fadein 1 fadeout 1
        $ gw_blushed = True
        call ginny_main("Wait, you didn't read it right? Please tell me you didn't read it", 1, 3, 3)
        g9 "'It was actually really good. It hurted a lot at first, but then it started to feel really good.'"
        call ginny_main(".....", 1, 7, 9) #blushed
        g9 "'Even the pain was good.'"
        call ginny_main("Please stop", 1, 9, 4)
        g9 "This is very serious Ginny, I'll have to share this with the other professors and with your family."
        call ginny_main("No, you can't, please, I'll do anything...", 1, 3, 3)
        g9 "Anything?"
        call ginny_main("Yes, anything", 1, 3, 3)
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        call ginny_main("", 1, 1, 10)
    else:
        call ginny_main("Hello professor, you wanted to see me?")



    label ginny_secondmenu: #temporary
    menu:
        "-Personal Favours-":
            "To be done."
            jump ginny_secondmenu 
        "-Public Favours-":
            "To be done."
            jump ginny_secondmenu
        "-open mouth and blush":
            $ gw_blushed = True
            $ changeGinny(1,2)
            jump ginny_secondmenu
        "-close mouth and unblush":
            $ gw_blushed = False
            $ changeGinny(1,1)
            jump ginny_secondmenu
        "-Toggle shirt-":
            if gw_wear_top == True:
                $ gw_wear_top = False
            else:
                $ gw_wear_top = True
            call ginny_main("...", 1, 1)
            jump ginny_secondmenu
        "-Toggle bra-":
            if gw_wear_bra == True:
                $ gw_wear_bra = False
            else:
                $ gw_wear_bra = True
            call ginny_main("...", 1, 1)
            jump ginny_secondmenu
        "-Toggle skirt-":
            if gw_wear_skirt == True:
                $ gw_wear_skirt = False
            else:
                $ gw_wear_skirt = True
            call ginny_main("Pervert...", 1, 1)
            jump ginny_secondmenu
        "-Toggle panties-":
            if gw_wear_panties == True:
                $ gw_wear_panties = False
            else:
                $ gw_wear_panties = True
            call ginny_main("...", 1, 1)
            jump ginny_secondmenu
        "-Toggle robes-":
            if gw_wear_robes == True:
                $ gw_wear_robes = False
            else:
                $ gw_wear_robes = True
            call ginny_main("...", 1, 1)
            jump ginny_secondmenu
        "-Toggle pubes-":
            if gw_shaved == True:
                $ gw_shaved = False
            else:
                $ gw_shaved = True
            call ginny_main("...", 1, 1)
            jump ginny_secondmenu
        "-Select Top-":
            label ginny_selecttop: #temporary
            menu:
                "-Top_1-":
                    call ginny_change("top","top_1")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_2-":
                    call ginny_change("top","top_2")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_3-":
                    call ginny_change("top","top_3")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_4-":
                    call ginny_change("top","top_4")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_5-":
                    call ginny_change("top","top_5")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_6-":
                    call ginny_change("top","top_6")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Top_7-":
                    call ginny_change("top","top_7")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Purple Sweater-":
                    call ginny_change("top","purple_sweater")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Trainning Shirt":
                    call ginny_change("top","sports")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selecttop
                "-Go back-":
                    jump ginny_secondmenu

        "-Select Bottom-":
            label ginny_selectskirt: #temporary
            menu:
                "-Skirt_1":
                    call ginny_change("skirt","skirt_1")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Skirt_2":
                    call ginny_change("skirt","skirt_2")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Skirt_3":
                    call ginny_change("skirt","skirt_3")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Skirt_4":
                    call ginny_change("skirt","skirt_4")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Skirt_5":
                    call ginny_change("skirt","skirt_5")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Skirt_6":
                    call ginny_change("skirt","skirt_6")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Trainning Shorts":
                    call ginny_change("skirt","gym")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectskirt
                "-Go back-":
                    jump ginny_secondmenu

        "-Select Panty-":
            label ginny_selectpanty: #temporary
            menu:
                "-Latex":
                    call ginny_change("panty","latex_panties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Silk":
                    call ginny_change("panty","silk_panties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Open":
                    call ginny_change("panty","open")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Fishnet Buttoned":
                    call ginny_change("panty","fishnet_buttoned")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-White Panty":
                    call ginny_change("panty","base_panties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Bikini String":
                    call ginny_change("panty","bikini_string_black")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Black Sports":
                    call ginny_change("panty","black_athlete_bikini")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Black Panty Low":
                    call ginny_change("panty","cup_panties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Fishnet":
                    call ginny_change("panty","fishnet")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Lace Panties":
                    call ginny_change("panty","lace_panties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Punk Mudblood":
                    call ginny_change("panty","punk_mudblood")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectpanty
                "-Go back-":
                    jump ginny_secondmenu

        "-Select Bra-":
            label ginny_selectbra: #temporary
            menu:
                "-Latex-":
                    call ginny_change("bra","latex_bra")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Silk-":
                    call ginny_change("bra","silk_bra")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Princess Leia-":
                    call ginny_change("bra","princess_leia_bikini_top")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Twisted-":
                    call ginny_change("bra","twisted")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Blue Lowcut-":
                    call ginny_change("bra","blue_lowcut")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Black Sports-":
                    call ginny_change("bra","black_athlete")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Leather-":
                    call ginny_change("bra","leather_bikini")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Lace Bra-":
                    call ginny_change("bra","lace_bra")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Sling blue-":
                    call ginny_change("bra","stringbikini_blue")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Heart-":
                    call ginny_change("bra","heart_pasties")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Tape-":
                    call ginny_change("bra","insulating_tape")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Bandeau-":
                    call ginny_change("bra","bandeau")
                    call ginny_main("Of course, sir.", 1)
                    jump ginny_selectbra
                "-Go back-":
                    jump ginny_secondmenu
        "-Dismiss Her-":
            hide screen ginny_weasley
            #call reset_ginny
            with d3
            jump day_main_menu

label reset_ginny:
    $ gw_wear_panties = True
    $ gw_wear_bra = True
    $ gw_wear_skirt = True
    $ gw_wear_top = True
    return

