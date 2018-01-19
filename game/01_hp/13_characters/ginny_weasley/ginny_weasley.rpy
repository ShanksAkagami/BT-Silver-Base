label ginny_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $ changeGinny(1,2,1,665,0) #whatt

    if not ginny_met:
        $ ginny_met = True
        call ginny_main("Hello professor, you wanted to see me?") 
        $ changeGinny(1,1)
        m "{size=-4}(wow, she's hot.){/size}"
        m "{size=-4}(but that damm robe is blocking the view.){/size}"
        if not fire_in_fireplace:
            m "{size=+4}lightus firus!!!!{/size}"
            $ fire_in_fireplace = True
            show screen fireplace_fire
        m "Welcome miss Weasley, please feel free to take off your robe, the fire will keep us warm"
        call ginny_main("Of course, sir, thanks.", 1, 2)
        hide screen ginny_weasley
        show screen blkfade
        with d3
        $ gw_wear_robes = False

        show screen ginny_weasley
        hide screen blkfade
        with d3

        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1
        call ginny_main("This feels beter", 1, 1, 5)
        g9 "{size=-4}(much better.){/size}"
        m "{size=-4}(This girl walks around dressed like that and this Hagrid Peter doesn't even notice her, what the hell is wrong with this guy??{/size})"
        call ginny_main("So, professor, what did you wannna speak with me?", 1, 2, 6) #confused a little
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
        g9 "Ok, I think I might have something in mind"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        $ gw_blushed = False
        call ginny_main("Thank you, professor...", 1, 2, 6)
        
        m "What should I tell her to do"
    
        menu:
            "\"Take off your clothes\"":
                
                m "Nothing drastic, really..."
                m "I just want you to take off your clothes."

                $ gw_blushed = True
                call ginny_main("What?!?!", 1, 3, 3) #surprised
                #g9 "Ever since I read about it on your diary I can't stop thinking about it"
                m "Your clothes, I want you to take them off."
                call ginny_main(".......", 1, 10, 9) #eyes closed mouth angry
                call ginny_main("So I take off my clothes and we're good right?", 1, 6, 7)
                m "Yes yes, of course..."
                g9 "{size=-4}(for now){/size}"
                call ginny_main("fine..", 1, 7, 9) #blushed

                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.

                call ginny_undress
                
                ">Your eyes drift over her naked body"
                call ginny_main("...", 1, 2, 6)
                ">You notice she has a very bushy pussy but decide not to point it out"
                call ginny_main(".......", 1, 2, 6)
                m "You have an amazing body miss Weasley"
                $ gw_botharms = True
                $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
                call ginny_main("Can I go now?", 1, 6, 7)
                m "Yes, you can go, but I will summon you again soon"
                call ginny_main("But, I did what you asked", 1, 2, 6)
                m "Yes, you did, and we're good for now, but only for now"
                call ginny_main("...", 1, 10, 11) 

                $ gw_botharms = False
                $ gw_blushed = False

                hide screen ginny_weasley
                show screen blkfade
                with d3
                ">Ginny puts her clothes back on as fast as she can, always with an angry glare towards you"
     
                $ gw_wear_robes = True
                $ gw_wear_top = gw_wear_top_temp
                $ gw_wear_skirt = gw_wear_skirt_temp
                $ gw_wear_bra = gw_wear_bra_temp
                $ gw_wear_panties = gw_wear_panties_temp

                show screen ginny_weasley
                hide screen blkfade

                g9 "See you soon"
                call ginny_main("Whatever", 1)

                $ renpy.play('sounds/door.mp3')
                hide screen ginny_weasley

                call reset_ginny
                $ ginny_steps = 1
                $ ginny_whoring += 1
                $ ginny_mad += 1 

                with d3
                jump day_main_menu

            "\"Give me your underwear\"":
                m "I want your bra and panty..."

                $ gw_blushed = True
                call ginny_main("What?!?!", 1, 3, 3)
                call ginny_main("My... underwear...?", 1, 2, 6)
                call ginny_main("But professor, this is...")
                m "This is what I want you to do..."
                m "You said anything. Did you change your mind?"
                call ginny_main("No, I haven't. I am.... it's just...")
                call ginny_main("You need my....")
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                call ginny_main("...underwear, professor?", 1, 6, 7)
                m "Yes I do..."
                call ginny_main("I'm not wearing anything else... How will I go back to my dorm?")
                m "You have your robe"
                g9 "So, what's gonna be?"
                call ginny_main("Fine... hang on", 1, 2, 11)

                hide screen ginny_weasley
                show screen blkfade
                with d3
                ">Ginny grabs her robes and put them back on covering most of her body"

                $ gw_wear_robes = True

                show screen ginny_weasley
                hide screen blkfade

                m "{size=-4}(damm, I wanted to see it){/size}"
                call ginny_main("I will take my underwear off now", 1)
                
                hide screen ginny_weasley
                show screen blkfade
                with d3
                ">She turns her back to you and removes her underwear as careful as possible so you don't see a thing"
                ">After it's done she turns back to you"

                $ gw_wear_bra = False
                $ gw_wear_panties = False

                show screen ginny_weasley
                hide screen blkfade

                call ginny_main("Here you go", 1)
                ">Ginny extends her arm to you and hands you her bra and panties"
                ">You see that she is trying to keep the robes closed so you can't see it"

                call ginny_main("Can I go now?", 1, 6, 7)
                m "Yes, you can go, but I will summon you again soon"
                call ginny_main("But, I did what you asked", 1, 2, 6)
                m "Yes, you did, and we're good for now, but only for now"
                call ginny_main("...", 1, 10, 11) 
        
                g9 "See you soon"
                call ginny_main("Whatever", 1)

                $ renpy.play('sounds/door.mp3')
                hide screen ginny_weasley

                call reset_ginny
                $ ginny_steps = 1
                $ ginny_whoring += 2 
                $ ginny_mad += 3
                
                with d3
                jump day_main_menu

            "\"Masturbate for me\"":
                call ginny_masturbate
                #jump ginny_secondmenu

    elif ginny_steps == 1: ###Shave Event
        
        call ginny_main("{size=+10}I want my diary back right now{/size}", 1, 2, 11) #angry
        g4 "{size=+10}And I want you to shave your pussy right now{/size}"
        $ gw_blushed = True
        call ginny_main("What????", 1, 3, 6)
        call ginny_main(".....", 1, 7, 9) #blushed
        call ginny_main("Just give me my diary back and we will forget all about what you made me do", 1, 7, 11)
        g9 "Just shave your pussy right now and I will forget how you screamed at me"
        call ginny_main("Are you serious? ", 1, 7, 9)
        call ginny_main("No, that's enough, I won't take this anymore, if I keep doing this there will be no end to it", 1, 10, 11)
        m ">You grab her diary and open it on your table"
        call ginny_main("", 1, 2, 6)
        g9 "'The x-ray glasses I ordered finally arrived, can't wait to see Harry's dick{image=textheart}{image=textheart}...'"
        call ginny_main("", 1, 6, 7)
        g9 "'Dear diary, today was a little disappointing, i thought Harry would have an ginormous dick, since he was the chosen one and all'"
        g9 "'But it was quite average... Ron on the other hand has quite a big one... is it wrong to masturbate thinking of your brother?'"
        call ginny_main("", 1, 6, 9)
        g9 "'Well, no one will know{image=textheart}{image=textheart}'"
        g9 "Well, it is wrong. If people find out about this fetish of yours... Harry would never be with you..."
        call ginny_main("You asshole...", 1, 10, 11)
        g9 "So, what's gonna be?"
        call ginny_main("Fine...", 1, 2, 11)
        
        hide screen ginny_weasley
        show screen blkfade
        with d3
 
        $ gw_wear_robes_temp = False
        $ gw_wear_top_temp = False
        $ gw_wear_skirt_temp = False
        $ gw_wear_bra_temp = False
        $ gw_wear_panties_temp = False
 
        if gw_wear_robes == True:
            ">Ginny removes her robes and put them on the chair next to her.."
            $ gw_wear_robes_temp = True
            $ gw_wear_robes = False
        if gw_wear_top == True:
            ">Finally the zipper is undone and she has no choice but to take the skirt off..."
            $ gw_wear_top_temp = True
            $ gw_wear_top = False
        if gw_wear_skirt == True:
            ">She slowly starts to unzip her skirt..."
            ">She seems very hesitant and takes her time..."
            $ gw_wear_skirt_temp = True
            $ gw_wear_skirt = False
        if gw_wear_bra == True:
            ">Ginny reaches over her head and pulls her bra off in one smooth motion, like she wants to be done with it as quickly as possible"
            $ gw_wear_bra_temp = True
            $ gw_wear_bra = False
 
        if gw_wear_panties == True:
            ">She then stops for a while, it looks like she's rethinking it, deciding if it's really worth it."
            ">Very hesitantly she finally makes her decision and pull down her panties..."
            ">Ginny slowly steps out of her panties and places them on top of the pile of clothes on the chair." 
            $ gw_wear_panties_temp = True
            $ gw_wear_panties = False
 
        show screen ginny_weasley
        hide screen blkfade
        with d3

        call ginny_main("...", 1)
        g9 "Come on girl, get to it"

        call ginny_main("Fine...", 1)
        
        hide screen ginny_weasley
        $ gw_shaved = True
        show screen blkfade
        with d3
        show screen ginny_weasley
        hide screen blkfade
        with d3

        call ginny_main("Are you happy now?", 1)
        g9 "Yes, very happy, you can go for now"

        hide screen ginny_weasley
        show screen blkfade
        with d3
        ">Ginny puts her clothes back on as fast as she can, always with an angry glare towards you"
        #">She looks very out of it"
        
        $ gw_wear_robes = gw_wear_robes_temp
        $ gw_wear_top = gw_wear_top_temp
        $ gw_wear_skirt = gw_wear_skirt_temp
        $ gw_wear_bra = gw_wear_bra_temp
        $ gw_wear_panties = gw_wear_panties_temp

        show screen ginny_weasley
        hide screen blkfade

        g9 "See you soon"
        call ginny_main("Whatever", 1)

        $ renpy.play('sounds/door.mp3')
        hide screen ginny_weasley
        $ ginny_steps = 2
        $ ginny_whoring += 1
        $ ginny_mad += 5 
        call reset_ginny
        with d3
        jump day_main_menu

    else:
        call ginny_main("Yes?", 1, 2, 11) #angry
        

    label ginny_secondmenu: #temporary
    menu:
        "-Inventory-":
            call screen wardrobe_ginny
        "-Personal Favours-":
            menu:
                "-Masturbate-":
                    call ginny_masturbate
                    jump ginny_secondmenu 

                "-Handjob-":
                    show screen blkfade
                    ">You stand up and walk around your desk, standing in front of Ginny."
                    hide screen bld1
                    hide screen genie
                    show screen chair_02
                    show screen desk_02
                    $ genie_chibi_xpos = -20
                    $ genie_chibi_ypos = 10
                    #$ g_c_u_pic = "jerking_off_02_ani"
                    #show screen g_c_u
                    with fade
                    $ genie_sprite_xpos = 300
                    $ genie_sprite_ypos = 20
                    call gen_main("", 4, 2)
                    hide screen blktone
                    hide screen blkfade
                    with d5
                    #pause
                    call ginny_main("....", 1, 10, 7) #mouth,eye

                    ">You open your cloak and pull out your cock."
                    call gen_main("", 4, 5)
                    $ gw_blushed = True
                    call ginny_main("What the hell are you doing??", 1, 3, 3)
                    g9 "I read at your diary about the many handjobs you gave around. I want one too."
                    call ginny_main("I'm not going to do that", 1, 7, 11)
                    g9 "Are you sure? How do you think Hagrid would feel if he knew about everything that's in this diary?."
                    call ginny_main("{size=+7}Harry!! His name is Harry!!{/size}", 1, 3, 11)
                    call ginny_main("", 1, 7, 11)

                    g9 "Whatever... So what's gonna be?"
                    g9 "Will Harry find out about how much of a whore you are? Or are you going to give me a handjob?"
                    call ginny_main("{size=-7}...I'm not a whore...{/size}", 1, 6, 9)
                    call ginny_main("", 1, 6, 8)
                    ">She looks down at your cock."
                    call ginny_main("{size=-7}(...so big...){/size}")
                    call ginny_main("Fine", 1, 10, 11)

                    ">She walks towards you and takes a firm hold of it with her right hand"


                    #call ginny_undress
                    #call ginny_main("Whatever", 1)
                    $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/handjob.png"
                    $ changeGinny(1,6,8,389,0) #167
                    #call gen_main("", 4, 2)
                    g9 "You can start now"
                    call ginny_main("(*Hmmph* At least it isn't small...)", 1, 10, 7) 
                    call ginny_main("(I can't even fit my hand around it.)", 1, 10, 8) 
                    ">Ginny slowly starts stroking your cock with her hand, her movements seem experienced."
                    call ginny_handjob_alittle
                    g9 "You're really good at it"
                    call ginny_main("...", 1, 6, 6) 
                    ">Ginny keeps moving her hand back and forth along the length of your cock."
                    call ginny_handjob_alittle
                    g9 "ugh... Yes, that's it..."
                    call ginny_main("{size=-4}(Looks like he's enjoying it){/size}", 1,2,7) 
                    g9 "Mmmm, yes... just like that..."
                    call ginny_handjob_alittle
                    call ginny_main("Is this good Professor?", 1,8,10) 
                    g9 "yes, yes, this is amazing..."
                    call ginny_handjob_alittle
                    call ginny_main("good...", 1,1,10) 
                    ">You can notice she's enjoying it too"
                    ">She then starts pumping your cock even faster."
                    call ginny_handjob_alittle
                    g4 "Gods yes..."
                    g4 "I'm cumming!!!"

                    #$ g_c_c_u_pic = "jerking_off_cum_ani"
                    #show screen g_c_c_u
                    #$ luna_wear_cum_under = True
                    #$ luna_cum = 10
                    show screen white 
                    pause.1
                    hide screen white
                    pause.2
                    show screen white 
                    $ gw_semen = "01_hp/13_characters/ginny_weasley/body/semen/handjob3.png"
                    $ gw_cummed_on = True
                    call ginny_main("",1,3,3)
                    pause .1
                    hide screen white
                    with hpunch
                    $ gw_semen = "01_hp/13_characters/ginny_weasley/body/semen/bottom_heavy.png"
                    call ginny_main("",1,3,8)

                    ">You start shooting your load directly into Ginny's body, coating her in cum."
                    g9 "Argh! by the gods {size=+10}YES!{/size}"

                    #hide screen genie_sprite
                    with d3
                    g9 "That hit the spot..."
                    call ginny_main("({image=textheart}{image=textheart}{image=textheart})", 1,2,12)
                    #call luna_main("Professor!", 8, 1, 3, 1)
                    #call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", 7, 8, 2, 1)
                    m "Ahh... that was fantastic slut..."
                    #call ginny_main("but...", 6, 2, 4, 2) 
                    #call ginny_main("Do you need a little more encouragement?", 8, 1, 4, 1) 
                    #m "What are you thinking?"
                    #call ginny_main("......", 9, 8, 3, 1) 
                    #call ginny_main("And you call this starting with something easy?", 1, 6, 7)
                    #$ renpy.pause()
                    #call ginny_handjob_alittle
                    #call ginny_main("", 1)
                    $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/default.png"

                    $ changeGinny(1,6,8,655,0) #167
                    call ginny_main("Look at this mess...")
                    hide screen genie_sprite
                    with d3
                    g9 "that looks great on you hahaha"
                    call ginny_main("How am I supposed to get to the dorms like this?",1,10,8) #mouth,eye
                    g9 "You can always just weat my cum around, It does look good on you"
                    call ginny_main("Yeah, right...",1,10,11) #mouth,eye

                    ">She tries to clean her clothes as best as she can"
                    $ gw_semen = "01_hp/13_characters/ginny_weasley/body/semen/on_clothes.png"

                    call ginny_main("*Ugh* This is the best I can do for now I guess...",1)
                    call ginny_main("Can I go now?", 1, 6, 7)
                    m "Yes, you can go, but be ready when I summon you again"
                    call ginny_main("Whatever", 1, 10, 10)

                    call ginny_main("{size=-4}(I'm so wet right now.){/size}", 1, 2, 8)
                    call ginny_main("{size=-4}(I'll stop by at the bathroom and finish it by myself{image=textheart}.){/size}", 1, 8, 10)

                    $ renpy.play('sounds/door.mp3')
                    hide screen ginny_weasley
                    #$ ginny_steps = 1
                    call reset_ginny
                    with d3
                    jump day_main_menu
                    

                "-Kneel-":
                    call ginny_undress
                    $ gw_kneeling = True
                    $ changeGinny(1,2,1,665,30)
                    call ginny_main("...", 1, 6, 8)
                    $ renpy.pause()
                    $ gw_kneeling = False
                    call ginny_main("...", 1)
                    $ changeGinny(1,2,1,665,0)
                    "not finished"
                    jump ginny_secondmenu

                "-Go Back-":
                    jump ginny_secondmenu

        

        "-open mouth and blush":
            $ gw_blushed = True
            $ changeGinny(1,2,1)
            jump ginny_secondmenu
        "-close mouth and unblush":
            $ gw_blushed = False
            $ changeGinny(1,1,1)
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
        "-Toggle robes-":
            if gw_wear_robes == True:
                $ gw_wear_robes = False
            else:
                $ gw_wear_robes = True
            call ginny_main("...", 1)
            jump ginny_secondmenu
        "-Toggle pubes-":
            if gw_shaved == True:
                $ gw_shaved = False
            else:
                $ gw_shaved = True
            call ginny_main("...", 1)
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
    $ gw_wear_robes = False
    $ gw_blushed = False
    $ gw_squirting = False
    $ gw_botharms = False
    $ gw_cummed_on = False
    call ginny_change("bra","silk_bra")
    call ginny_change("panty","silk_panties")
    return

label ginny_undress:
    
    hide screen ginny_weasley
    show screen blkfade
    with d3

    $ gw_wear_robes_temp = False
    $ gw_wear_top_temp = False
    $ gw_wear_skirt_temp = False
    $ gw_wear_bra_temp = False
    $ gw_wear_panties_temp = False
 
    if gw_wear_robes == True:
        ">Ginny removes her robes and put them on the chair next to her.."
        $ gw_wear_robes_temp = True
        $ gw_wear_robes = False
    if gw_wear_top == True:
        ">Ginny starts to unbutton her shirt..."
        ">She slowly fumbles with the buttons until Finally the last button is undone..."
        ">She takes off her shirt put it on the chair next to her"
        $ gw_wear_top_temp = True
        $ gw_wear_top = False
    if gw_wear_skirt == True:
        ">She slowly starts to unzip her skirt..."
        ">She seems very hesitant and takes her time..."
        ">Finally the zipper is undone and she has no choice but to take the skirt off..."
        $ gw_wear_skirt_temp = True
        $ gw_wear_skirt = False
    if gw_wear_bra == True:
        ">Ginny reaches over her head and pulls her bra off in one smooth motion, like she wants to be done with it as quickly as possible"
        $ gw_wear_bra_temp = True
        $ gw_wear_bra = False
 
    if gw_wear_panties == True:
        ">She then stops for a while, it looks like she's rethinking it, deciding if it's really worth it."
        ">Very hesitantly she finally makes her decision and pull down her panties..."
        ">Ginny slowly steps out of her panties and places them on top of the pile of clothes on the chair." 
        $ gw_wear_panties_temp = True
        $ gw_wear_panties = False
 
    show screen ginny_weasley
    hide screen blkfade
    with d3
    return

label ginny_masturbate:
    g9 "Okay, how about we start with something easy?"
    g9 "I already know you like to touch yourself a lot"
    $ gw_blushed = True
    call ginny_main("...", 1, 3, 3) #surprised
    g9 "Ever since I read about it on your diary I can't stop thinking about it"
    call ginny_main("Everyone masturbates...", 1, 10, 9) #eyes closed mouth angry
    m "Yes yes, of course, I myself do it all the time"
    call ginny_main(".....", 1, 10, 11) #angry
    m "So I want you to take off your clothes and masturbate for me"
    call ginny_main("What????", 1, 3, 3)
    call ginny_main("You can't be serious")
    m "I'm very serious, is either that, or this diary goes public..."
    call ginny_main("And you call this starting with something easy?", 1, 6, 7)
    m "Of course."
    m "I'm not asking you for anything you haven't done before..."
    call ginny_main("...", 1, 10, 11)
    g4 "{size=-4}(wow, she looks angry, maybe I pushed it too far, dammit!!){/size}"
    call ginny_main("fine..", 1, 7, 9) #blushed
    g9 "{size=-4}(nevermind){/size}"
    g9 "{size=-4}(That was way easier than with Hermione.){/size}"
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    
    call ginny_main("{size=-4}(I can't believe I'm doing this in front of him...){/size}", 1, 10, 9)
    #call ginny_main("Yes", 1, 1, 10)
    hide screen ginny_weasley
    show screen blkfade
    with d3

    $ gw_wear_robes_temp = False
    $ gw_wear_top_temp = False
    $ gw_wear_skirt_temp = False
    $ gw_wear_bra_temp = False
    $ gw_wear_panties_temp = False

    if gw_wear_robes == True:
        ">Ginny removes her robes and put them on the chair next to her.."
        $ gw_wear_robes_temp = True
        $ gw_wear_robes = False
    if gw_wear_top == True:
        ">Finally the zipper is undone and she has no choice but to take the skirt off..."
        $ gw_wear_top_temp = True
        $ gw_wear_top = False
    if gw_wear_skirt == True:
        ">She slowly starts to unzip her skirt..."
        ">She seems very hesitant and takes her time..."
        $ gw_wear_skirt_temp = True
        $ gw_wear_skirt = False
    if gw_wear_bra == True:
        ">Ginny reaches over her head and pulls her bra off in one smooth motion, like she wants to be done with it as quickly as possible"
        $ gw_wear_bra_temp = True
        $ gw_wear_bra = False

    if gw_wear_panties == True:
        ">She then stops for a while, it looks like she's rethinking it, deciding if it's really worth it."
        ">Very hesitantly she finally makes her decision and pull down her panties..."
        ">Ginny slowly steps out of her panties and places them on top of the pile of clothes on the chair." 
        $ gw_wear_panties_temp = True
        $ gw_wear_panties = False

    show screen ginny_weasley
    hide screen blkfade
    with d3
    call ginny_main("Please? I don't want to do this..", 1, 6, 6) #blushed
    g4 "no pleases, just do it."
    call ginny_main("...", 1, 6, 8) #blushed
    $ gw_botharms = True
    $ gw_legsopen = True
    call ginny_main(".....", 1, 10, 11)
    ">She slowly starts grinding her mound against her hand."
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("",1, 10, 11)
    ">She seems to know what she's doing"
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("...",1, 10, 7)
    ">You notice Ginny start grinding her hips a little faster."
    

    call ginny_masturbates_alittle
    m "It seems to me that you might be enjoying this a little too much..."
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("Shut up!!!", 1, 11, 11)
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("",1, 10, 7)
    m "Your pussy is so wet."
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("{size=-1}Shut up{/size}", 1, 3, 3)
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("",1, 10, 7)
    call ginny_masturbates_alittle
    g9 "Are you thinking about Harry?"
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("{size=-2}Stop it{/size}", 1, 7, 7)
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("",1, 10, 7)
    call ginny_masturbates_alittle
    g9 "{size=+4}Answer me{/size}"
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("{size=-2}Please stop{/size}", 1, 12, 7)
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("",1, 10, 7)
    call ginny_masturbates_alittle
    g9 "{size=+4}Answer me or everyone will have a copy of your diary.{/size}"
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    call ginny_main("{size=-4}Yes..{/size}", 1, 12, 7)
    call ginny_masturbates_alittle
    g9 "{size=+4}What? I couldn't hear you.{/size}"
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
    call ginny_main("{size=+4}Yes!!! Yes!!! I'm thinking of him{/size}",1,3,9)
    call ginny_main("", 1, 12, 7)
    call ginny_masturbates_alittle
    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
    m "that's it slut... keep going..."
    call ginny_main("{size=-4}(I need a cock){/size}", 1, 12, 12)
    call ginny_masturbates_alittle
    call ginny_main("{size=-4}(this feels so good... with someone... watching me...){/size}", 1, 12, 12)
    call ginny_masturbates_alittle
    call ginny_main("{size=-4}(I-I think I'm...I'm going to...{/size}")
    ">Ginny's thighs are squeezing faster and faster."
    call ginny_masturbates_alittle
    call ginny_main("Cum!......", 1, 12, 13)
    $ gw_squirting = True
    
    hide screen ginny_weasley
    with d3
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    
    #hide screen ginny_weasley
    



    
    $ gw_squirt = "01_hp/13_characters/ginny_weasley/body/squirt/squirting.png"
    call ginny_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}Yes!!!!!{image=textheart}{image=textheart}{image=textheart}{/size}", 1, 12, 14)

    ">Suddenly, her body goes rigid and her abdominal muscles pulse in waves as orgasm rocks the young girl's body."

    hide screen ginny_weasley
    show screen blkfade
    with d3
    $ renpy.play('sounds/fall.wav')
    ">Ginny's legs, suddenly too weak to hold her body, collapse beneath her and she falls to the floor."
    "By the sands!"
    #"Cum coats your otherwise pristine desk. The only sounds in the room are your heavy breaths and the slow *plat* *plat* of your cum dripping off your desk."
    #show screen genie_jerking_sperm_02
    #with d3
    $ gw_squirting = False
    $ gw_kneeling = True
    $ gw_ypos = 50
    show screen ginny_weasley
    hide screen blkfade
    with d3
    "Ginny looks up at you from the floor with a dazed look."
    call ginny_main("...", 1,12,14)
    call ginny_main("i can'T believe I did that.", 1,12,14)
    #call ginny_main("Can i have my points now!", 1, 1, 2, 1)

    $ gw_botharms = False
    $ gw_legsopen = False
    $ gw_squirt = "01_hp/13_characters/ginny_weasley/body/squirt/dripping.png"
    $ gw_squirting = True
    $ gw_kneeling = False
    $ gw_ypos = 0

    call ginny_main("",1)
    g9 "{size=-4}(That was great...){/size}"
    call ginny_main("Can I go now?")
    m "Yes of course, but I will summon you again soon"
    call ginny_main("{size=-4}ok{/size}")
    ">You laught as the girl heads to the door while still naked and dripping wet"
    m "Aren't you forgetting something?"
    ">You ask while pointing to her clothes"
    call ginny_main("{size=-4}right, sorry{/size}")

    hide screen ginny_weasley
    show screen blkfade
    with d3
    ">Ginny slowly puts her clothes back on"
    ">She looks very out of it"
        
    $ gw_wear_robes = True
    $ gw_wear_top = gw_wear_top_temp
    $ gw_wear_skirt = gw_wear_skirt_temp
    $ gw_wear_bra = gw_wear_bra_temp
    $ gw_wear_panties = gw_wear_panties_temp

    show screen ginny_weasley
    hide screen blkfade

    m "See you soon"
    call ginny_main("{size=-4}yeah...{/size}")
    $ renpy.play('sounds/door.mp3')
    hide screen ginny_weasley
    $ ginny_steps = 1
    $ ginny_whoring += 5 
    $ ginny_mad += 5 
    call reset_ginny
    with d3
    jump day_main_menu
    return

label ginny_masturbates_alittle:

    $ count_gw = 5
    label ginny_masturbate_again:

        $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/covering2.png"
        call ginny_main("",1)
        $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
        call ginny_main("",1)

        $ count_gw -= 1
        if count_gw > 0:
            jump ginny_masturbate_again
        else:
            return

    return

label ginny_handjob_alittle:

    $ count_gw = 8
    label ginny_handjob_again:
    #while count_gw > 0:
        $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/handjob2.png"
        call ginny_main("", 1)
        $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/handjob.png"
        call ginny_main("", 1)
    

        $ count_gw -= 1
        if count_gw > 0:
            jump ginny_handjob_again
        else:
            return

#"Liftoff!"
    