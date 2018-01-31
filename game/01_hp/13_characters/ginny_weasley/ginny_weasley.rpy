label ginny_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.


    #### First Meeting ####
    if not ginny_met: 
        $ changeGinny(1,2,1,665,0) #whatt
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
                $ ginny_pf_undress += 1

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
                $ ginny_pf_giveunderwear += 1
                
                with d3
                jump day_main_menu

            #"\"Masturbate for me\"":
            #    call ginny_masturbate
                #jump ginny_secondmenu

    #### Second Meeting - Shave Event ####
    elif ginny_steps == 1: ###Shave Event
        $ gw_wear_accessory1 = True
        
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
        ">You give her a sharp razor"
        
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
        #$ gw_shaved = False
        show screen blkfade
        with d3
        $ gw_pubic = "01_hp/13_characters/ginny_weasley/body/pubic/growing.png"
        $ gw_crying = True
        $ gw_tears = "01_hp/13_characters/ginny_weasley/body/tears/tears_1.png"
        show screen ginny_weasley
        hide screen blkfade
        with d3

        call ginny_main("Why are you doing this to me?", 1)
        g9 "Don't stop now"
        call ginny_main("{size=-4}(...I've never been so humiliated in my whole life...){/size}",1,10,6) #mouth,eye

        hide screen ginny_weasley
        show screen blkfade
        with d3
        $ gw_shaved = True
        #gw_pubic = "01_hp/13_characters/ginny_weasley/body/pubic/growing.png"
        $ gw_crying = True
        $ gw_tears = "01_hp/13_characters/ginny_weasley/body/tears/tears_2.png"
        show screen ginny_weasley
        hide screen blkfade
        with d3

        call ginny_main("Are you happy now?", 1,16,11)
        g9 "Yes, very happy, you can go for now"

        hide screen ginny_weasley
        show screen blkfade
        with d3
        ">Ginny puts her clothes back on as fast as she can, always with an angry glare towards you"
        
        $ gw_wear_robes = gw_wear_robes_temp
        $ gw_wear_top = gw_wear_top_temp
        $ gw_wear_skirt = gw_wear_skirt_temp
        $ gw_wear_bra = gw_wear_bra_temp
        $ gw_wear_panties = gw_wear_panties_temp

        show screen ginny_weasley
        hide screen blkfade

        g9 "See you soon"
        call ginny_main("Whatever", 1,17,11)

        $ renpy.play('sounds/door.mp3')
        hide screen ginny_weasley
        $ ginny_steps = 2
        $ ginny_whoring += 1
        $ ginny_mad += 5 
        call reset_ginny
        with d3
        jump day_main_menu

    #### Third Meeting - Personal Favours Start ####
    else:
        call ginny_main("Yes?", 1, 2, 11) #angry

        #### Return Panties ####
        #### Panties Soaked ####
        if ginny_pf_pantythief == 3:
            m "Here are your panties [ginny_name]"
            $ the_gift = gw_panties # Ginny's panties.
            show screen gw_gift
            with d3
            $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
            ">You give Ginny her panties back"
            hide screen gw_gift
            with d3
            $ ginny_pf_pantythief = 4 #you gave ginny panties soaked


            call ginny_main("They are covered in... semen",1,6,8)
            call ginny_main("Those were my favorite panties, you ruined them",1,7,11)
            m "Why the surprise? I told you I was going to cum on them"
            call ginny_main("I thought you were joking...",1,17,11)
            g9 "nope"
            call ginny_main("Well, these will require some serious cleaning before I can put them on again...",1,17,8)
            m "Or you could put them on now."
            call ginny_main("What?",1,3,3)
            call ginny_main("I really would rather not, [gw_genie_name]...",1,15,4)
            g9 "now I really want you to put them"

                    #call her_main("What?","body_72")
            call ginny_main("[gw_genie_name], you are joking, right?",1,15,6)
            m "I am not..."
            call ginny_main("B-but...",1,16,8)
            call ginny_main("........................................",1,16,7)
            call ginny_main("(Must you always have your way, [gw_genie_name]?)",1,17,7)
            m "What was that, [ginny_name]?"
            call ginny_main("It's nothing, [gw_genie_name].",1,17,8)
            call ginny_main("Putting my panties back on!",1,15,8)
            hide screen ginny_main
            with d3
            show screen blktone8
            with d3
            ">Ginny hesitantly puts on her panties..."
            ">A tiny stream of cum trickles down one of her legs..."
            ">Ginny looks very uncomfortable..."
            $ gw_wear_panties = True
            $ gw_squirting = True
            $ gw_squirt = "01_hp/13_characters/ginny_weasley/body/squirt/dripping_cum.png"
            hide screen blktone8
            with d3
            call ginny_main("(This feels funny...)",1,2,8)
            call ginny_main("(but not in a bad way...)",1,1,8)
            call ginny_main("Can I go now?",1,2,6)
            m "Yes, you can go now"
            call ginny_main("Thank you, [gw_genie_name].",1,8,2)
            call ginny_main("(Why am I thanking him, I should be angry...)",1,9,5)
            call ginny_main("(*Ugh*...whatever...)",1,9,16)


            $ renpy.play('sounds/door.mp3')
            hide screen ginny_weasley
            call reset_ginny_2
            with d3
            jump day_main_menu

                        #"\"Why don't you clean them now?\"":
                        #$ cleaned_panties = True
                        #call her_main("Clean them How? You don't have a wash basin in here.","body_31")
                        #m "You're right, you'll have to use your mouth then."
                        #call her_main("My mouth?!","body_72")
                        #m "What's the big deal? It wouldn't be the first time you've tasted my cum."
                        #call her_main("It's a bit different! I wore these panties before I gave them to you.","body_30")
                        #call her_main("Not to mention that your cum is all cold and slimey...","body_32")
                        #m "Well in that case hand them back."
                        #call her_main("What? Can't I just put them on?","body_122") 
                        #m "I'm afraid not, you clean them now or you hand them back."
                        #call her_main("{size=-4}Fine...{/size}","body_118")
                        #m "What was that?"
                        #call her_main("I said I'll clean them ok!","body_132")
                        #m "Well..."
                        #call her_main("...","body_118")
                        #">Hermione reluctantly puts her cum-soaked panties in her mouth."
                        #call her_main("Mmmmhhhhh!","body_42")
                        #m "That's it, not as bas as you thought now is it?"
                        #call her_main("...","body_222")
                        #m "Make sure you get them nice and clean now..."
                        #call her_main("*gulp*","body_224")
                        #m "That's it. Do you think they're clean yet."
                        #call her_main("*Mmmhhhmmm*","body_125")
                        #m "Well then you can probably take them out of your mouth."
                        #call her_main("*Ahhhhh*","body_135")
                        #m "There, nice and clean."
                        #call her_main("*Yes [gw_genie_name]*","body_121")
        #### Panties NonSoaked ####
        elif ginny_pf_pantythief == 1:
            call ginny_main("Can I have my panties back?",1,1,1)
            menu:
                "-Sure-":
                    g9 "of course, but first let me see if you're doing your part"
                    call ginny_main("What do you mean?",1, 2, 6)
                    g9 "Lift up your skirt"

                    call ginny_main("...",1, 2, 6)
                    $ gw_liftskirt = True
                    $ gw_wear_skirt = False
                    call ginny_main("",1,1,7)
                    $ renpy.pause (1)
                    $ gw_liftskirt = False
                    $ gw_wear_skirt = True
                    call ginny_main("That's enough",1,1,1)

                    m "(I was enjoying the view...)"
                    $ the_gift = gw_panties # Ginny's panties.
                    show screen gw_gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">You give Ginny her panties back"
                    #">You found Ginevra Weasley's diary."
                    hide screen gw_gift
                    with d3
                    $ ginny_pf_pantythief = 4 #you gave ginny panties soaked
                    #m "Ginevra Weasley??"
                    call ginny_main("There's nothing wrong with them, [gw_genie_name]?)",1,1,1)
                    m "Of course not... What did you expect?"
                    call ginny_main("I don't know...",1,1,1)
                    call ginny_main("Putting my panties back on!")
                    hide screen ginny_main
                    with d3
                    show screen blktone8
                    with d3
                    ">Ginny puts on her panties..."
                    #">A tiny stream of cum trickles down one of her legs..."
                    ">She looks a bit embarrassed for doing it in front of you..."
                    $ gw_wear_panties = True
                    hide screen blktone8
                    with d3
                    call ginny_main("(Feels good to wear panties again)",1,1,1)
                    call ginny_main("(But I felt soo free before...)",1,1,1)
                    $ renpy.play('sounds/door.mp3')
                    hide screen ginny_weasley
                    call reset_ginny_2
                    with d3
                    jump day_main_menu
                "-Not Yet-":
                    #she mad
                    call ginny_main("....", 1, 17, 11) #mouth eye



    label ginny_secondmenu: #temporary
    menu:
        "-Inventory-":
            call screen wardrobe_ginny
        "-Personal Favours-":
            #### First Personal Favour ####
            if ginny_steps == 2: #### If Never Done Any Personal Favour ####
                m "[ginny_name], I'd like yo-"
                call ginny_main("No", 1, 17, 11) #mouth eye
                m "What?"
                call ginny_main("No, I won't do it", 1, 17, 11) #mouth eye
                m "You don't even know what I was going to ask"
                call ginny_main("It's gonna be something terrible...", 1, 3, 11) #mouth eye
                g9 "You look very angry"
                call ginny_main("{size=+7}Of course I'm angry, you've been blackmailing me and humiliating me{/size}", 1, 3, 11)
                m "Ok, what can I do to calm you down?"
                call ginny_main("Just give me back my diary please", 1, 17, 6)
                g9 "We both know I can't do that"
                m "This might be a dangerous artifact"
                call ginny_main("....", 1, 17, 7)
                m "anything else?"
                call ginny_main("............", 1, 17, 7)

                call ginny_main("You're very close with professor Snape right...?",1,2,7)
                m "yes..."
                call ginny_main("I'm terrible at potions...",1,2,7)
                m "I can talk with him about your grades.."
                call ginny_main("Cool",1,1,5)
                m "So, can you do something for me now?"
                call ginny_main("...What exactly do you want, [gw_genie_name]?",1,2,10)
                $ ginny_steps = 3 #### You two have an agreement
                $ ginny_mad = 0
                $ ginny_whoring = 1

            #### Personal Favours ####
            menu:
                "-What Panties-":
                    m "What kind of panties are you wearing?"
                    $ gw_blushed = True
                    if ginny_pf_pantythief_time == 0:
                        call ginny_main("...Would you like to... see them?",1,2,7) #mouth,eye
                    else:
                        call ginny_main("...Would you like to... see them again, [gw_genie_name]?",1,2,7) #mouth,eye

                    g9 "I'd love to"
                    $ gw_liftskirt = True
                    $ gw_wear_skirt = False
                    call ginny_main("...",1,1,7)

                    ">You stare at her panties-"
                    "That's a pretty sexy underwear..."
                    call ginny_main("I suppose...",1,2,7)
                    ">The girl tries to avoid looking at you"
                    ">You study her face..."
                    pause
                    ">And wonder what's going through her mind right now."
                    pause
                    m "You don't look too embarrassed..."
                    if ginny_pf_pantythief_time == 0:
                        #call ginny_main("...Would you like to... see them?",1,2,7) #mouth,eye
                        call ginny_main("Well, it's not like I'm naked...",1,2,15)
                    else:
                        call ginny_main("Well, it's not like the first time you make me do this...",1,2,15)

                        #call ginny_main("...Would you like to... see them again, [gw_genie_name]?",1,2,7) #mouth,eye

                    pause
                    "I like your panties..."
                    call ginny_main("Thank you, [gw_genie_name]...",1,1,5)
                    ">You keep looking into her eyes"
                    call ginny_main("[gw_genie_name], please... Now you are embarrassing me.",1,6,6)
                    m "Ok, you can cover it"
                    $ gw_liftskirt = False
                    $ gw_wear_skirt = True
                    call ginny_main("",1,1,1)

                    g9 "I'd like you to give them to me"
                    if ginny_pf_pantythief_time == 0:
                        call ginny_main("What?",1,3,3)
                        #call ginny_main("...Would you like to... see them?",1,2,7) #mouth,eye
                        #call ginny_main("Well, it's not like I'm naked...",1,2,15)
                        g9 "Your panties"
                    #else:
                    #    call ginny_main("I thought so...",1,2,15)

                    call ginny_main("I knew it wouldn't be that easy...",1,17,5)
                    m "I'll return them to you next time I summon you"
                    if ginny_pf_pantythief_time == 0:
                        call ginny_main("...",1,17,7)
                        call ginny_main("do I have any other option?",1,17,8)
                        g9 "not really"
                    call ginny_main("Fine...",1,17,9)
                    call ginny_main("",1,17,1)
                    $ gw_wear_panties = False
                    
                    $ the_gift = gw_panties # Ginny's panties.
                    show screen gw_gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">You received Ginny's panties"
                    $ ginny_pf_pantythief = 1 #you have ginny panties
                    hide screen gw_gift
                    with d3
                    g9 "Thank you"
                    call ginny_main("What do you plan on doing with them?",1,15,6)
                    g9 "I'll probably jerk off and cum on them"
                    call ginny_main("...",1,3,3)
                    call ginny_main("I knew I shouldn't have asked...",1,10,7)
                    call ginny_main("Can I go now?",1,10,6)
                    m "Yes, but can you lift your skirt one more time before going?"
                    call ginny_main("...",1,10,8)
                    m "..."


                    $ gw_liftskirt = True
                    $ gw_wear_skirt = False
                    call ginny_main("...",1,1,7)

                    $ gw_liftskirt = False
                    $ gw_wear_skirt = True
                    call ginny_main("bye",1,1,7)
                    g9 "And remember to not wear any panties until I give these back to you"
                    if ginny_pf_pantythief_time == 0:
                        call ginny_main("What??? You never said anything about that",1,3,3)
                        g9 "I'm saying it now"
                    call ginny_main("Fine, whatever", 1, 10, 11)
                    g9 "good, see you soon"
                    call ginny_main("{size=-7}...Am I getting wet...?{/size}",1,2,8)
                    $ ginny_whoring += 1

                    $ ginny_pf_pantythief_time = 1
                    $ renpy.play('sounds/door.mp3')
                    hide screen ginny_weasley
                    call reset_ginny_2
                    with d3
                    jump day_main_menu



                #"-Undress For Me":
                #    call ginny_masturbate
                #    jump ginny_secondmenu 

                "-Nice Tits-":
                    if ginny_pf_showtits_time == 0:
                        g9 "I wanna see them"
                        ">You say that while pointing to her tits"
                        call ginny_main("You want too... see my breasts, [gw_genie_name]?", 1, 2, 6) #mouth eye
                        g9 "Yes, I want you to show me your tits"
                    else:
                        g9 "I wanna see them again"
                        ">You say that while pointing to her tits"
                        #call ginny_main("You want too... see my breasts, [gw_genie_name]?", 1, 2, 6) #mouth eye
                    call ginny_main("...", 1, 10, 7)
                    call ginny_main("No touching!", 1, 2, 6)
                    m "No touching"
                    call ginny_main("...Ok, but seriously, no touching!", 1, 10, 7)
                    g9 "No touching"
                    #black screen
                    hide screen ginny_weasley
                    show screen blkfade
                    with d3
                    $ gw_botharms = True
                    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/blank.png"
                    $ gw_top = "01_hp/13_characters/ginny_weasley/clothes/tops/lifting/1.png"
                    $ gw_shirt_special = True
                    $ ginny_chibi("stand_topless",700)
                    show screen ginny_weasley
                    hide screen blkfade
                    with d3
                    call ginny_main("...", 1, 10, 8)
                    g9 "You have amazing tits [ginny_name]"
                    g9 "But I can't see them quite well from this distance"
                    g9 "You know, old eyes..."
                    call ginny_main("{size=-5}(Old eyes, right...){/size}",1,6,10)
                    m "Come closer [ginny_name], let me take a better look..."
                    call ginny_main("No touching",1,12,11)
                    m "No touching"
                    call ginny_main("No touching",1,1,1)

                    hide screen ginny_weasley
                    show screen blkfade
                    with d3
                    $ ginny_chibi("stand_topless",400)
                    show screen ginny_weasley
                    hide screen blkfade
                    with d3
                    g9 "Much better now"
                    if ginny_pf_showtits_time == 0:
                        call ginny_main("...", 1, 1, 8)

                        menu:
                            "Start jerking off?":
                                pass
    
                            "Who are you kidding? Start jerking off":
                                pass

                            "teste":
                                hide screen hermione_04 #Stands with tits out.
                                hide screen genie
                                show screen ctc
                                show screen groping_ginny
                                with d1
                                hide screen blkfade
                                with d5
                                pause
                                show screen bld1
                                with d3
                                #call her_head("............","body_200")
                                #m "Very good..."
                                #call her_head(".....","body_203")
                    else:
                        call ginny_main("You're going to start jerking off now aren't you?", 1, 1, 7)
                        g9 "You know me so well"
                        call ginny_main("...", 1, 1, 8)


                    m "Just stand still, [ginny_name]..."

                    ">You stare at Ginny's breasts with hunger..."
                    hide screen ginny_main
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3

                    pause

                    if ginny_pf_showtits_time == 0:
                        call ginny_main("[gw_genie_name]?!!",1,3,3)
                        call ginny_main("Are you... Jerking off...?",1,3,4)
                        ">You keep stroking your hard cock..."
                        call ginny_main("You must... Put it away...",1,7,8)
                        m "Stop whining [ginny_name]. I'm not touching you, am I?"
                        g9 "Besides, you can't keep your eyes off of it"
                        call ginny_main("That's not true", 1,16,11)
                        call ginny_main("I should go",1,17,11)
                        m "You go and everyone will receive a copy of your diary"
                        m "Can you imagine yor parents face once they read what's in there?"
                        call ginny_main("Please don't",1,3,4)
                        m "Just stay there, with a view like this I'll be done soon"
                        call ginny_main("...Fine",1,17,7)
                        call ginny_main("...",1,17,8)
                        m "Yes... Yes, like this..."
                        ">Ginny is trying to see your dick over the table"
                        call ginny_main("{size=-5}(I never thought [gw_genie_name] would have such a huge dick...){/size}",1,2,8)
                        call ginny_main("{size=-5}(I can't imagine what that thing would to me...){/size}",1,2,8)
                        m "Yes, with your tits all naked..."
                        call ginny_main("{size=-5}(Could I even take that...?){/size}",1,6,8)
                        call ginny_main("(No Ginny, stop thinking like that.)",1,10,9)
                        m "Oh, you little slut. You nasty little slut!"
                        call ginny_main("(This kind of stuff is what got me into this situation in the first place...)",1,6,11)
                        ">You start to stroke your cock even harder..."
                        ">Ginny starts looking at it again"
                        call ginny_main("(It's even bigger now...)",1,3,8)
                    else:
                        g9 "You can't take your eyes off of it huh?"
                        call ginny_main("That's not true", 1,16,11)
                        g9 "Yeah, right"
                        ">You keep stroking your hard cock..."
                        call ginny_main("I should go",1,17,11)
                        m "Relax, I won't tell anyone"
                        call ginny_main("...",1,17,8)
                        m "Yes... Yes, like this..."
                        ">Ginny is trying to see your dick over the table"
                        call ginny_main("{size=-5}(His dick looks even bigger than last time...){/size}",1,2,8)
                        call ginny_main("{size=-5}(I can't stop imagining what that thing would to me...){/size}",1,2,8)
                        m "Yes, with your tits all naked..."
                        call ginny_main("{size=-5}(Could I even take that...?){/size}",1,6,8)
                        call ginny_main("(No Ginny, stop thinking like that.)",1,10,9)
                        m "Oh, you little slut. You nasty little slut!"
                        call ginny_main("(I can't believe I'm such a slut...)",1,6,11)
                        ">You start to stroke your cock even harder..."
                        ">Ginny starts looking at it again"
                        call ginny_main("(It's even bigger now...)",1,3,8)

                    
                    

                    call ginny_main(".......................",1,1,8)
                    g4 "Yes, I know you want this! Yes!"

                    call ginny_main("(Come on, finish it already, this is killing me...)",1,12,8)


                    g4 "Argh! You whore!"
                    call ginny_main("...",1,12,10)


                    hide screen ginny_main
                    with d3
                    show screen white 
                    pause.1
                    hide screen white
                    pause.2
                    show screen white 
                    pause .1
                    hide screen white
                    with hpunch
                    g4 "Argh! YES!"
                    hide screen ginny_main
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    #pause 3
                    pause

                    #show screen bld1
                    #with d3
                    call ginny_main("Are you done?",1,8,8)
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "Ah, shit, this feels good..."
                    ">You notice she's still looking at your dick and that she has a faint smile on her face"
                    show screen genie
                    #show screen genie_jerking_off
                    with d3
                    if ginny_pf_showtits_time == 0:
                        call ginny_main("How could you [gw_genie_name]? In front of a young innocent student!",1,3,11)
                        m "Hey, little missy, we both know that you aren't exactly innocent"
                        call ginny_main("I don't know what you're talking about...",1,3,16)
                        m "Yeah.. right"
                        call ginny_main("{size=-4}(...he sure did cum a lot{image=textheart}){/size}",1,1,10)
                    else:
                        g9 "Did you enjoy the view [ginny_name]?"
                        call ginny_main("I don't know what you're talking about...",1,3,16)
                        m "Yeah.. right"
                        call ginny_main("{size=-4}(...he sure did cum a lot{image=textheart}){/size}",1,1,10)

                    hide screen genie_jerking_sperm_02
                    with d3

                    $ gw_botharms = False
                    $ gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
                    $ gw_top = "01_hp/13_characters/ginny_weasley/clothes/tops/1.png"
                    $ gw_shirt_special = False
                    $ ginny_chibi("stand",700)
                    show screen ginny_weasley
                    hide screen blkfade
                    with d3
                    call ginny_main("I'll be going now",1,10,2)
                    m "Yes yes, of course, we should this again"
                    if ginny_pf_showtits_time == 0:
                        call ginny_main("{size=-4}(...I wouldn't mind{image=textheart}){/size}",1,1,10)
                    else:
                        call ginny_main("{size=-4}(...Can't wait{image=textheart}){/size}",1,1,10)



                    $ ginny_whoring += 1

                    $ ginny_pf_showtits_time = 1
                    $ renpy.play('sounds/door.mp3')
                    hide screen ginny_weasley
                    call reset_ginny_2
                    with d3
                    jump day_main_menu


                "-Grope Butt-":


                    ###################REQUEST_05 (Level 02) (BUTT MOLESTER).


                    hide bld1
                    with d3
                    m "Come closer. Let me molest your butt a little."
                    #First time
                    stop music fadeout 5.0
                    call ginny_main("[gw_genie_name]!?",1,3,3) #mouth eye
                    m "Relax, All I am going to do is squeeze your little butt a couple of times..."
                    call ginny_main("This is inappropriate, [gw_genie_name]................",1,9,7)
                    m "Nobody needs to know and your diary is gonna stay safe and sound here in my drawer"
                    call ginny_main("(Darn it.....!)",1,10,7)
                    hide screen bld1
                    with d3
                    #call her_walk(500, 280, 3, redux_pause = 2)
                    show screen blkfade
                    hide screen ginny_chibi
                    with Dissolve(1)
                    pause.5
                    call ginny_main("..................",1,10,5)
                    call ginny_main("Do you want me to turn around then, [gw_genie_name]?",1,2,5)
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Hm... Yes. Turn around, [hermione_name]."
                    call ginny_main("As you say, [gw_genie_name]...",1,10,6)
                    hide screen genie
                    show screen ctc
                    show screen no_groping_ginny
                    with d1
                    hide screen blkfade
                    with d5
                    pause
                    call ginny_main(".............",1,6,6)
                    call ginny_main("...........................",1,6,8)
                    call ginny_main("[gw_genie_name], I would like to be done with this sooner rather than later...",1,7,6)
                    m "Don't rush me [hermione_name]... Let me savour the moment..."
                    call ginny_main(".............................",1,17,9)
                    menu:
                        m "Hm..."
                        "-Give her butt a squeeze-":
                            pass
                        "-Give her butt a slap-":
                            $ renpy.play('sounds/slap_02.mp3') #SLAP!
                            show screen white
                            with hpunch
                            pause.08
                            hide screen white
                            show screen bld1
                            call ginny_main("!!!!!!!!!!!!!",1,3,3)
                            call ginny_main("[gw_genie_name]!!?",1,17,4)
                            menu:
                                "\"Fine, fine... I just couldn't resist....\"":
                                    call ginny_main(".......................",1,17,6)
                                    pass
                                "-Give her butt a slap-":
                                    $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                    show screen white
                                    with hpunch
                                    pause.08
                                    hide screen white
                                    show screen bld1
                                    call ginny_main("!!!!!!!!!!!!!",1,3,4)
                                    call ginny_main("[gw_genie_name]....?",1,17,11) #mouth eye
                                    menu:
                                        "\"Fine, fine... I just couldn't resist....\"":
                                            call ginny_main("It's Ok...",1,17,15)
                                            pass
                                        "-Give her butt another slap-":
                                            $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                            show screen white
                                            with hpunch
                                            pause.08
                                            hide screen white
                                            show screen bld1
                                            call ginny_main("!!!!!!!!!!!!!",1,3,4)
                                            call ginny_main("[gw_genie_name], what are you doing!?",1,17,5)
                                            call ginny_main("You said all you are going to do is touch!",1,17,6)
                                            menu:
                                                "\"Fine, fine... I just couldn't resist....\"":
                                                    call ginny_main("Just don't do it again...",1,10,6)
                                                    pass
                                                "-Give her butt another slap-":
                                                    $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                                    show screen white
                                                    with hpunch
                                                    pause.08
                                                    hide screen white
                                                    show screen bld1
                                                    call ginny_main("[gw_genie_name], stop this, please...",1,7,9)
                                                    call ginny_main("What if somebody hears us?",1,9,6)
                                                    m "Alright, alright... proceeding with groping then..."
                                                    call ginny_main("................",1,17,6)
   
            
                    pause
                    show screen groping_ginny
                    with d7
                    call ginny_main("!!!!!!?",1,17,8)
                    m "What is it, [ginny_name]?"
                    call ginny_main("I can't believe this is really happening...",1,17,9)
                    call ginny_main("This is so... wrong...",1,2,6)
                    g9 "Relax, [ginny_name]. It's not like you aren't enjoying this..."
                    call ginny_main("What? Of course I'm not! You're blackmailing me...",1,11,11)
                    g9 "Yes, concentrate on that..."
                    call ginny_main("....................",1,17,11)
                    show screen bld1
                    with d3
                    pause
                    show screen blktone8
                    with d3
                    ">You keep on playing with Ginny's buttocks..."
                    ">You slide your hands up and down her inner tighs..."
                    call ginny_main("................",1,3,11)
                    menu:
                        "-Slide your hands under her panties-":
                            ">You slowly slide one of your hands under the fabric of the girl's panties..."
                            call ginny_main("[gw_genie_name]... What are you...?",1,3,6)
                            m "It's alright, just try to relax and enjoy yourself"
                            call ginny_main(".............",1,6,6)
                            menu:
                                "-Prod her pussy with one of your fingers-":
                                    #show screen blkfade
                                    #with d3
                                    ">You slide one of your fingers down and place it against the girl's little slit..."
                                    call ginny_main("[gw_genie_name]?",1,6,4) 
                                    menu:
                                        "-Force your finger into her pussy!-":
                                            ">You force one of your fingers into her little pussy..."
                                            ">It's very tight and warm..."
                                            ">it is quite wet as well...  Seems like Ginny's taking pleasure in this..."
                                            call ginny_main("Ah....",1,2,7)
                                            call ginny_main("It's inside of me...",1,14,8)
                                            call ginny_main("No, [gw_genie_name], you must stop now...",1,11,11)
                                            m "Why? You don't like it?"
                                            call ginny_main("It doesn't matter, this is where I draw the line,",1,7,11)
                                            call ginny_main("I'm leaving",1,17,11)
                                            ">Ginny pulls away from you..."
                                            m "Heh... I see..."
                                            m "Well, in that case..."
                                        "-Let the girl go...-":
                                            pass
                                "-Prod her butt-hole instead-":
                                    #show screen blkfade
                                    #with d3
                                    ">You place your one of your thumbs against the girl's little butt-hole..."
                                    call ginny_main("[gw_genie_name]? What are you planning on doing?",1,6,4)
                                    menu:
                                        "-Force your thumb into her butt-hole-":
                                            ">You force one of your thumbs into her little butt-hole..."
                                            with hpunch
                                            call ginny_main("ah... your finger is up my...",1,2,7)
                                            ">It's very tight and warm inside..."
                                            call ginny_main("Ah....",1,12,8)
                                            ">you slowly start to pump your thumb"
                                            call ginny_main("It's inside of me...",1,4,8)
                                            ">you rotate thumb as you go"
                                            call ginny_main("No, [gw_genie_name], you must stop now...",1,6,12)
                                            ">you pull your thumb out of her tight little asshole..."
                                            call ginny_main("Thank you-",1,1,7)
                                            ">...and replace it with two fingers"
                                            call ginny_main("",1,3,4)
                                            call ginny_main("B-Bastard!{image=textheart}",1,12,12)
                                            m "Why? You don't like it?"
                                            call ginny_main("Yes...",1,14,12)
                                            call ginny_main("No, no, stop it",1,3,9)
                                            ">Ginny gathers all the little strenght she has left and pulls away from you..."
                                            call ginny_main("I should go",1,17,7)
                                            m "Heh... I see..."
                                            m "Well, in that case..."
                                        "-Let the girl go...-":
                                            pass
                                "-Stop pushing your luck. Dismiss the girl-":
                                    pass
                        "-No. That's enough for today. Dismiss her-":
                            pass

    
#                    if whoring <= 5:
#                        $ whoring +=1
                    show screen blkfade 
                    with d5
                    
                    stop music fadeout 1.0
                    ">You release her..."
                    m "This will do for now."
                    
                    hide screen blktone8
                    hide screen ctc
                    hide screen bld1
                    hide screen no_groping_ginny
                    hide screen groping_ginny
                    #show screen hermione_blink
                    $ ginny_chibi("stand",400)
                    show screen genie
                    with d1
                    
                    hide screen blkfade
                    with d3
 
                    m "good night [ginny_name]"

                   
                   
                    #$ hermione_SC.chibi.xpos = 500 #Near the desk.
                    #show screen hermione_blink #Hermione stands still.
                    show screen bld1
                    hide screen blkfade
                    with Dissolve(1)
                    
                    call ginny_main("..................",1,1,1)#,xpos=370,ypos=0
                    her "Thank you [gw_genie_name]..."
                    if daytime:
                        call ginny_main("Now if you don't mind I'd better go. The classes are about to start.")
                    else:
                        call ginny_main("I'd better go now then. It's getting pretty late...")








                "-Masturbate- incomplete":
                    call ginny_masturbate
                    jump ginny_secondmenu 

                "-Handjob- incomplete":
                    show screen blkfade
                    ">You stand up and walk around your desk, standing in front of Ginny."
                    hide screen bld1
                    hide screen genie
                    show screen chair_02
                    show screen desk_02
                    $ genie_chibi_xpos = -20
                    $ genie_chibi_ypos = 10
                    with fade
                    $ genie_sprite_xpos = 300
                    $ genie_sprite_ypos = 20
                    call gen_main("", 4, 2)
                    hide screen blktone
                    hide screen blkfade
                    with d5
                    call ginny_main("....", 1, 10, 7) #mouth,eye

                    ">You open your cloak and pull out your cock."
                    call gen_main("", 4, 5)
                    $ gw_blushed = True
                    call ginny_main("What the hell are you doing??", 1, 3, 3)
                    g9 "I read at your diary about the many handjobs you gave around."
                    g9 "I want one too."
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

                    $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/handjob.png"
                    $ changeGinny(1,6,8,389,0) #167
                    call ginny_main("....")
                    m "....."
                    call ginny_main("....")
                    m "....."
                    m "You can start now"
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

                    with d3
                    g9 "That hit the spot..."
                    call ginny_main("({image=textheart}{image=textheart}{image=textheart})", 1,2,12)
                    m "Ahh... that was fantastic slut..."

                    $ gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/default.png"

                    $ changeGinny(1,6,8,655,0) #167
                    call ginny_main("Look at this mess...")
                    hide screen genie_sprite
                    with d3
                    g9 "that looks great on you hahaha"
                    call ginny_main("How am I supposed to get to the dorms like this?",1,10,8) #mouth,eye
                    g9 "You can always just wear my cum around, It does look good on you"
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
                    

                "-Kneel- incomplete":
                    call ginny_undress
                    $ gw_kneeling = True
                    $ changeGinny(1,2,7,150,170)
                    $ genie_sprite_xpos = 530
                    $ genie_sprite_ypos = 0
                    call gen_main_mirror("", 4, 5)
                    call ginny_main("...", 1, 6, 7)
                    $ renpy.pause()
                    $ gw_kneeling = False
                    call ginny_main("...", 1)
                    $ changeGinny(1,2,1,665,0)
                    "not finished"
                    jump ginny_secondmenu

                "-Show back- incomplete":
                    call ginny_undress
                    $ gw_spread_ass = True
                    $ gw_wear_accessory1 = False

                    call ginny_main("...", 1, 2, 7)
                    $ renpy.pause()
                    $ gw_spread_ass = False
                    $ gw_wear_accessory1 = True

                    call ginny_main("...", 1)
                    #$ changeGinny(1,2,1,665,0)
                    "not finished"
                    jump ginny_secondmenu

                "-Blow- incomplete":
                    call ginny_undress
                    $ changeGinny(1,2,1,400,212)
                    
                    call ginny_main("fine, let me tie up my hair", 1, 2, 1) 
                    hide screen ginny_weasley
                    show screen blkfade
                    with d3
                    $ gw_hair = "01_hp/13_characters/ginny_weasley/body/hair/tied.png"
                    $ gw_hair_layer = "01_hp/13_characters/ginny_weasley/body/layerhair/blank.png"
                    show screen ginny_weasley
                    hide screen blkfade
                    with d3

                    $ gw_kneeling = True
                    $ changeGinny(1,2,1,400,212)
                    #
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
                    $ genie_sprite_ypos = 0
                    call gen_main("", 4, 2)
                    

                    hide screen blktone
                    hide screen blkfade
                    with d5

                    #pause
                    call gen_main("", 4, 5)
                    g9 "suck it"
                    $ gw_blushed = True
                    call ginny_main("ok....", 1, 2, 7) #mouth,eye
                    call ginny_blowjob_alittle
                    call ginny_main("you enjoying it?", 1, 2, 7) #mouth,eye
                    g9 "yes, keep going"
                    call ginny_blowjob_alittle


                    call ginny_main("....", 1, 34, 7) #mouth,eye
                    call ginny_main("...", 1, 34, 8)
                    #
                    $ renpy.pause()
                    $ gw_kneeling = False
                    call ginny_main("...", 1)
                    $ changeGinny(1,2,1,665,0)
                    $ gw_hair = "01_hp/13_characters/ginny_weasley/body/hair/default.png"
                    $ gw_hair_layer = "01_hp/13_characters/ginny_weasley/body/layerhair/default.png"
                    call gen_main("", 4, 2)
                    "not finished"
                    jump ginny_secondmenu

                "-Anal- incomplete":
                    call ginny_undress

                    hide screen bld1
                    hide screen genie
                    show screen chair_02
                    show screen desk_02
                    $ genie_chibi_xpos = -20
                    $ genie_chibi_ypos = 10
                    #$ g_c_u_pic = "jerking_off_02_ani"
                    #show screen g_c_u
                    with fade
                    $ gw_doggystyle = True
                    $ changeGinny(1,2,7,200,170)
                    $ genie_sprite_xpos = 530
                    $ genie_sprite_ypos = 0
                    call gen_main_mirror("", 4, 2)
                    call gen_main_mirror("", 4, 5)
                    

                    hide screen blktone
                    hide screen blkfade
                    with d5

                    call ginny_main("...", 1, 6, 7)
                    $ renpy.pause()
                    $ gw_doggystyle = False
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
            call reset_ginny_2
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
    $ gw_crying = False
    call ginny_change("bra","silk_bra")
    call ginny_change("panty","silk_panties")
    return

label reset_ginny_2:
    $ gw_blushed = False
    $ gw_squirting = False
    $ gw_botharms = False
    $ gw_cummed_on = False
    $ gw_crying = False
    return

label ginny_dismiss:
    $ renpy.play('sounds/door.mp3')
    hide screen ginny_weasley
    call reset_ginny_2
    with d3
    jump day_main_menu

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
    
    $ gw_squirt = "01_hp/13_characters/ginny_weasley/body/squirt/squirting.png"
    call ginny_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}Yes!!!!!{image=textheart}{image=textheart}{image=textheart}{/size}", 1, 12, 14)

    ">Suddenly, her body goes rigid and her abdominal muscles pulse in waves as orgasm rocks the young girl's body."

    hide screen ginny_weasley
    show screen blkfade
    with d3
    $ renpy.play('sounds/fall.wav')
    ">Ginny's legs, suddenly too weak to hold her body, collapse beneath her and she falls to the floor."
    "By the sands!"

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
    $ ginny_pf_masturbate += 1
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

label ginny_blowjob_alittle:
    
    $ genie_sprite_xpos = 300
    $ genie_sprite_ypos = 0

    $ count_gw = 3
    label ginny_blowjob_again:

        call gen_main("", 4, 2)
        $ changeGinny(1,31,8,279,225) #279 225
        call ginny_main("", 1, 31, 8) #mouth,eye
        $ changeGinny(1,32,8,263,216) #167
        call ginny_main("", 1, 32, 8) #mouth,eye
        $ changeGinny(1,33,8,253,212) #167
        call ginny_main("", 1, 33, 8)
        call ginny_main("", 1, 33, 8)
        $ changeGinny(1,32,8,263,216)
        call ginny_main("", 1, 32, 8) #mouth,eye
        $ changeGinny(1,31,8,279,225)
        call ginny_main("", 1, 31, 8) #mouth,eye
        $ changeGinny(1,31,8,279,225) #167
        call ginny_main("", 1, 31, 8) #mouth,eye
        $ changeGinny(1,32,8,263,216) #167
        call ginny_main("", 1, 32, 8) #mouth,eye
        $ changeGinny(1,33,8,253,212) #167
        call ginny_main("", 1, 33, 8)
        call ginny_main("", 1, 33, 8)
        $ changeGinny(1,32,8,263,216)
        call ginny_main("", 1, 32, 8) #mouth,eye
        $ changeGinny(1,31,8,279,225)
        call ginny_main("", 1, 31, 8) #mouth,eye
        call gen_main("", 4, 5)

        $ count_gw -= 1
        if count_gw > 0:
            jump ginny_blowjob_again
        else:
            return

    return

#"Liftoff!"
    