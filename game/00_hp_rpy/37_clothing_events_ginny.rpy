
label equip_bottom_ginny(skirt = '1'): 
    
    #hide screen ginny_main 
    #with d3
    #m "{size=-4}(Tell her to wear this skirt?){/size}"
    #$ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    #menu:
    #    "\"(Yes, let's do it!)\"":
    #        pass
    #    "\"(Not right now.)\"":
    #        return

    if skirt == '1':
      #$ gw_genie_name = "Professor"
      #$ ginny_name
      m "[ginny_name]..."
      call ginny_main("yes, [gw_genie_name]?", 1, 2, 2) #mouth #eyes
      m "I'd like you to wear this longer skirt."
      call ginny_main("Isn't that skirt a little too long?", 1, 3, 7)
      if whoring >= 10:
        call ginny_main("I think not even Hermione would wear such a long skirt", 1, 17, 8)

      m "Is that a problem?"
      call ginny_main("..........", 1, 17, 10)
      call ginny_main("I suppose not...", 1, 2, 10)
      $ gw_blushed = False
      

    elif skirt == '2':
      m "[ginny_name]..."
      call ginny_main("yes, [gw_genie_name]?", 1, 2, 2)
      m "I'd like you to wear your normal skirt."
      call ginny_main("really?", 1, 8, 10)
      m "Sure, why not?"
      call ginny_main("Ok [genie_name]. I'll go change now.", 1, 8, 17)
      $ gw_blushed = False
    
    elif skirt == '3':
      m "[ginny_name]..."
      m "I would like you to wear this skirt from now on."
      ">You hand her the skirt."
      call ginny_main("What?",1,3,3)
      call ginny_main("Isn't that too short?",1,2,6) #mouth #eyes
      m "Nah, it's perfect."
      call ginny_main("You can almost see my panties",1,2,8)
      g9 "Okay, almost perfect"
      call ginny_main("...",1,17,11)
      call ginny_main("(I mean, It's not that short...)",1,17,10)
      call ginny_main("Fine...",1,17,9)
      m "Fantastic!"
      call ginny_main("Let me just go change...",1,2,5)
      $ gw_blushed = False

    elif skirt == '4':
      m "[ginny_name]..."
      m "I would like you to wear this skirt to classes from now on."
      ">You hand her the skirt."
      call ginny_main("What?!?",1,3,3)
      call ginny_main("This doesn't cover anything!",1,3,4)#mouth #eyes
      call ginny_main("I can't wear this around the school, it's too short!",1,8,6)
      m "Of course you can"
      call ginny_main("...",1,6,8)
      call ginny_main("{size=-4}(Everyone will be able to see... everything...){/size}",1,15,9)
      call ginny_main("................",1,17,8)

      call ginny_main("Alright... I'll do it...",1,17,7)
      
      #call ginny_main("................",1,3,6)
      call ginny_main("Let me just go change...",1,10,7)
      $ gw_blushed = True



    elif skirt == '5':
      m "[ginny_name]..."
      m "I would like you to wear this skirt from now on."
      ">You hand her the skirt."
      call ginny_main("You expect me to wear this to class?", 1, 3, 3)
      m "That I do [ginny_name]."
      call ginny_main("But there's almost nothing there", 1, 3, 4)
      g9 "That's the point"

      call ginny_main("Why not just go without a skirt then? It would be basically the same...", 1, 2, 11)
      g9 "Great idea [ginny_name]"
      call ginny_main("No no, nevermind, I'll wear it", 1, 15, 4)#mouth #eyes
      call ginny_main("{size=-4}(It's better than nothing I guess){/size}",1,17,6)
      call ginny_main("................",1,17,8)
      call ginny_main("Let me go change...",1,17,10)
      $ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+skirt+".png"
      $ gw_blushed = True
      call ginny_main("I have belts bigger than this", 1, 16, 8)


    elif skirt == '6':
      m "[ginny_name]..."
      m "I would like you to wear this skirt from now on."
      ">You hand her the skirt."
      call ginny_main("It's see-through!!!!", 1, 3, 4)
      g9 "Amazing right?"
      g9 "Snape put a spell on this skirt to make it like that"
      call ginny_main("...", 1, 10, 6)
      call ginny_main("Is there any way I can convince you otherwise?", 1, 15, 7)
      g9 "Nope"
      call ginny_main("Fine...",1,10,9)
      call ginny_main("Let me go change...",1,17,10)
      $ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+skirt+".png"
      $ gw_blushed = True
      call ginny_main("{size=-4}(You can see everything...){/size}", 1, 7, 8)



    elif skirt == '7':
      m "[ginny_name]..."
      m "I would like you to wear this shorts from now on."
      ">You hand her the shorts."
      call ginny_main("They're so cute", 1, 1, 5)#mouth #eyes
      call ginny_main("You want me to wear them to class?", 1, 2, 5)
      m "I do..."
      call ginny_main("Is that allowed?", 1, 2, 10)
      m "I'm the head master, [ginny_name]. It's well within my power to change the school uniform."
      call ginny_main("sure, as long as I don't get into any trouble...", 1, 13, 5)
      call ginny_main("Let me go change...",1,1,5)
      $ gw_blushed = False

    elif skirt == '8':
      m "[ginny_name]..."
      m "I would like you to wear this pants from now on."
      ">You hand her the pants."
      call ginny_main("They look great for trainning", 1, 1, 5)
      call ginny_main("You want me to wear them to class?", 1, 2, 5)
      m "I do..."
      call ginny_main("Is that allowed?", 1, 2, 10)
      m "I'm the head master, [ginny_name]. It's well within my power to change the school uniform."
      call ginny_main("sure, as long as I don't get into any trouble...",1, 13, 5)
      call ginny_main("Let me go change...",1,1,5)
      $ gw_blushed = False

    $ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+skirt+".png"


#        if whoring < 13:
#            m "[hermione_name]..."
#            call her_main("yes, [genie_name]?","body_01")
#            m "I'd like you to wear your normal skirt."
#            call her_main("really?","body_82")
#            m "Sure, why not?"
#            call her_main("nixwThank you [genie_name]. I'll go change now.","body_16")
#        else:
#            m "[hermione_name]..."
#            call her_main("yes, [genie_name]?","body_01")
#            m "I'd like you to wear your normal skirt."
#            call her_main("...that old thing?","body_69")
#            m "Sure, is that a problem?"
#            call her_main("..........","body_70")
#            call her_main("I suppose not...","body_71")
#            call her_main("niceIt's just so plain...","body_69")
#
#    elif skirt == '2':
#        if whoring < 10:
#            m "[hermione_name]..."
#            m "I would like you to wear a shorter skirt today."
#            ">You hand her the skirt."
#            call her_main("What?","body_48")
#            call her_main("And break school uniform?","body_48")
#            jump too_much
#        elif whoring <= 18:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("What?","body_50")
#            call her_main("But it's not proper school uniform...","body_28")
#            m "Well as your headmaster I think I can decide what is and isn't school uniform..."
#            call her_main("I suppose you're right...","body_29")
#            m "Of course I am."
#            call her_main("But what if I'm a bad influence on the other students?","body_11")
#            m "I'm sure it'll be fine..."
#            call her_main("...","body_29")
#            call her_main("(It's not too short...)","body_33")
#            call her_main("Alright I'll do it.","body_61")
#            m "Fantastic!"
#            call her_main("................","body_69")
#            call her_main("Let me just go change...","body_66")
#        else:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("What?","body_72")
#            call her_main("But it's so long...","body_71")
#            call her_main("Can't I wear something a little shorter?","body_69")
#            call her_main("Just a bit shorter please...","body_97")
#            m "I've made up my mind [hermione_name]."
#            call her_main("Fine.","body_103")
#            call her_main("Let me go change...","body_120")
#
#    elif skirt == '3':
#        if whoring < 15:
#            m "[hermione_name]..."
#            m "I would like you to wear this little skirt from now on."
#            ">You hand her the skirt."
#            call her_main("What?","body_48")
#            call her_main("You want me to wear that... thing?","body_48")
#            jump too_much
#        elif whoring <= 20:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("What?","body_77")
#            call her_main("That's not even a skirt!","body_76")
#            m "Of course it is."
#            call her_main("It's barely more than a rag!","body_62")
#            m "Well if you wear it I might be inclined to give \"Gryffindor\" 15 points..."
#            call her_main("...","body_50")
#            call her_main("(I mean It's not too short...)","body_29")
#            call her_main("Fine... but I want 20 points","body_32")
#            m "Fantastic! 20 points to Gryffindor!"
#            $ gryffindor += 20
#            call her_main("................","body_50")
#            call her_main("Let me just go change...","body_66")
#        else:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("...","body_88")
#            call her_main("(It's so short... it'll barely cover anything...)","body_87")
#            call her_main("ok...","body_69")
#            m "really, you'll wear it?"
#            call her_main("Of course [genie_name].","body_105")
#            call her_main("just Let me go get changed...","body_107")
#
#    elif skirt == '4':
#        if whoring < 16:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt to classes from now on."
#            ">You hand her the skirt."
#            jump too_much
#        elif whoring <= 20:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt to classes from now on."
#            ">You hand her the skirt."
#            call her_main("What?!?","body_62")
#            call her_main("This doesn't cover anything!","body_61")
#            call her_main("You cannot expect me to wear this around the school!","body_49")
#            m "40 points..."
#            call her_main("...","body_50")
#            call her_main("(It's not like I have any reputation left to protect...)","body_71")
#            call her_main("Alright... I'll do it...","body_79")
#            m "Fantastic! 40 points to Gryffindor!"
#            $ gryffindor += 40
#            call her_main("................","body_66")
#            call her_main("Let me just go change...","body_69")
#        else:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("{size=-4}(Everyone will be able to see... everything...){/size}","body_88")
#            call her_main("Alright [genie_name].","body_107")
#            call her_main("just Let me go get changed...","body_107")
#            call her_main("{size=-4}(..........){/size}","body_105")
#
#    elif skirt == '5':
#        if whoring < 20:
#            m "[hermione_name]..."
#            m "I would like you to wear a shorter skirt today."
#            ">You hand her the skirt."
#            jump too_much
#        elif whoring <= 23:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("You expect me to wear this to class?","body_50")
#            m "That I do [hermione_name]."
#            call her_main("{size=-4}(What have I become?){/size}","body_88")
#            call her_main("................","body_105")
#            call her_main("Let me just go change...","body_107")
#        else:
#            m "[hermione_name]..."
#            m "I would like you to wear this skirt from now on."
#            ">You hand her the skirt."
#            call her_main("...","body_122")
#            call her_main("Can't I wear something a little shorter?","body_189")
#            m "I don't think they make anything shorter."
#            call her_main("I guess This will just have to do then...","body_196")
#            call her_main("Let me go change...","body_205")
#            
#    call set_h_skirt(item) 
    return



###Jeans ###
#label equip_bot(item = ""):
#    if item == "jeans_long":
#        call equip_jeans_long
#    elif item == "jeans_short":
#        call equip_jeans_short
#    elif (item[:1]) == "s": #set skirt
#        call equip_skirt(item[-1:])
#    elif (item[:1]) == "t": #Set top
#        #call equip_top(item[-1:]) TODO
#        call set_h_top(item)
#    return
#label equip_jeans_long:
#
#    if whoring >= 0 and whoring <= 2: # Lv 0
#        call her_main("Muggle pants?","body_11")
#        m "Very astute [hermione_name]."
#        call her_main(".....?","body_11")
#        call her_main("Wait you want me to WEAR them!?","body_31")
#        m "Yup"
#        call her_main("At school!?")
#        m "How does 10 points sound?"
#        call her_main("These are not part of the school uniform! I could be suspended!","body_18")
#        m "15 points?"
#        call her_main("NO amount of points are worth being suspended over!","body_07")
#        m "30?"
#        jump too_much
#    elif whoring >= 3 and whoring < 6: #Lv 1  - 2
#       call her_main("Muggle pants?","body_11")
#       m "Quick as ever [hermione_name]..."
#       call her_main(".....","body_11")
#       call her_main("You... want me to wear them...","body_31")
#       m "Yup"
#       call her_main("At school?")
#       m "How does 10 points sound?"
#       call her_main("But they're not part of the school uniform... I could get suspended...","body_18")
#       m "I'm the head master, [hermione_name]. It's well within my power to change the school uniform."
#       m "15 points?"
#       call her_main("............")   
#       call her_main("... How on earth am I going to explain this to my classmates?","body_21")
#       show screen bld1
#       with d3
#       show screen blktone
#       with d3
#       call set_h_skirt("jeans_long")
#       call her_main("","body_21",xpos=120,ypos=0)
#       show screen ctc
#       with d3
#       pause
#       m "15 points for Gryffindor!"
#       $ gryffindor +=15
#       call her_main("Thank you, [genie_name]","body_29",xpos=410)
#    elif whoring >= 6 and whoring < 9:
#       call her_main("Jeans?","body_02")
#       m "Yup."
#       call her_main("You want me to wear them at school?","body_17")
#       m "That's right..."
#       call her_main("*sigh* as long as I don't get into any trouble...","body_16")
#       call her_main("and I get some points for Gryffindor!","body_14")
#       m "Well, it looks like it's 15 points for Gryffindor!"
#       $ gryffindor +=15
#       call her_main("Thank you, [genie_name]! (These might.. get me some extra attention)","body_59")
#       call her_main("(Not that I want the attention!) I'm only in it for the points!","body_58")
#       show screen bld1
#       with d3
#       show screen blktone
#       with d3
#       call set_h_skirt("jeans_long")
#       call her_main("","body_58",xpos=120,ypos=0)
#       show screen ctc
#       with d3
#       pause
#       call her_main("","body_01",xpos=410)
#    elif whoring >= 9 and whoring <= 15: 
#       call her_main("Jeans?","body_02")
#       m "..."
#       call her_main("Aren't they a little... plain?","body_66")
#       m "How do you mean?"
#       call her_main("How am I going to save Gryffindor if I look like just another boring girl?","body_16")
#       call her_main("How am I going to get my points?","body_16")
#       call her_main("At least make this worth while... Please, [genie_name]","body_17")
#       m "15 points for Gryffindor, I guess?"
#       call her_main("You're the best, [genie_name]!","body_129")
#       show screen bld1
#       with d3
#       show screen blktone
#       with d3
#       call set_h_skirt("jeans_long")
#       show screen ctc
#       with d3
#       call her_main("*humph* ... (These are so stuffy... How am i supposed to get my hands into...)","body_12",xpos=120)
#       call her_main("(What if [genie_name] needs me to...)","body_12",xpos=120)
#       call her_main("(No... i shouldn't think about things like that! Keep your head in the game, [hermione_name]","body_141")
#       call her_main("...","body_141")
#       call her_main("(ahh... i thought about it again... naughty [hermione_name]!)","body_188")
#       g9 "....."
#       call her_main("","body_188",xpos=410)
#    elif whoring > 15: 
#        call her_main("...Jeans?","body_02")
#        m "Yup"
#        call her_main("*sigh*...are you serious?","body_04")
#        m "...? You're going to draw the line at... a pair of jeans, [hermione_name]?"
#        call her_main("Of course not, [genie_name]!","body_87")
#        call her_main("It's just that... they take... time to get off","body_204")
#        g4 "..."
#        call her_main("I have needs and...","body_204")
#        call her_main("There's a lot of fabric, [genie_name]")
#        call her_main("...")
#        call her_main("I'll go change immediately, [genie_name]","body_209")
#        show screen bld1
#        with d3
#        show screen blktone
#        with d3
#        call set_h_skirt("jeans_long")
#        call her_main("","body_209",xpos=120,ypos=0)
#        show screen ctc
#        with d3
#        pause
#        call her_main("If you still have time, [genie_name], we could test how long it takes to get out of these things?","body_205")
#        g9 "(I love my job)"
#        call her_main("","body_209",xpos=410)
#    hide screen blktone
#    return
#    
#label equip_jeans_short:
#
#    if whoring >= 0 and whoring < 9: # Lv 0
#        call her_main("What are these?","body_11")
#        m "Pants, [hermione_name]."
#        call her_main(".....?","body_11")
#        call her_main("These aren't pants!","body_31")
#        m "What are they then?"
#        call her_main("underwear!")
#        m "So you're not going to wear them?"
#        jump too_much
#    elif whoring >= 9 and whoring < 14:
#       call her_main("Cut offs?","body_02")
#       m "Yup."
#       call her_main("You want me to wear them class?","body_17")
#       m "I do..."
#       call her_main("Well I suppose they're not too bad...","body_16")
#       call her_main("and it's all to help out Gryffindor!","body_14")
#       m "Speaking of that, 15 points for Gryffindor!"
#       $ gryffindor +=15
#       call her_main("Thank you, [genie_name]! (These might.. get me some extra attention)","body_59")
#       call her_main("(Not that I want the attention!) I'm only in it for the points!","body_58")
#       show screen bld1
#       with d3
#       show screen blktone
#       with d3
#       call set_h_skirt("jeans_short")
#       call her_main("","body_58",xpos=120,ypos=0)
#       show screen ctc
#       with d3
#       pause
#       call her_main("","body_01",xpos=410)
#    elif whoring >= 14 and whoring <= 20: 
#       call her_main("Jeans?","body_02")
#       m "..."
#       call her_main("Aren't they a little... plain?","body_66")
#       m "How do you mean?"
#       call her_main("How am I going to save Gryffindor if I look like just another boring girl?","body_16")
#       call her_main("How am I going to get my points?","body_16")
#       call her_main("At least make this worth while... Please, [genie_name]","body_17")
#       m "15 points for Gryffindor, I guess?"
#       call her_main("You're the best, [genie_name]!","body_129")
#       show screen bld1
#       with d3
#       show screen blktone
#       with d3
#       call set_h_skirt("jeans_short")
#       show screen ctc
#       with d3
#       call her_main("*humph* ... (These are so stuffy... How am i supposed to get my hands into...)","body_12",xpos=120)
#       call her_main("(What if [genie_name] needs me to...)","body_12",xpos=120)
#       call her_main("(No... i shouldn't think about things like that! Keep your head in the game, [hermione_name]","body_141")
#       call her_main("...","body_141")
#       call her_main("(ahh... i thought about it again... naughty [hermione_name]!)","body_188")
#       g9 "....."
#       call her_main("","body_188",xpos=410)
#    elif whoring > 20: 
#        call her_main("...Jeans?","body_02")
#        m "Yup"
#        call her_main("*sigh*...are you serious?","body_04")
#        m "...? You're going to draw the line at... a pair of jeans, [hermione_name]?"
#        call her_main("Of course not, [genie_name]!","body_87")
#        call her_main("It's just that... they take... time to get off","body_204")
#        g4 "..."
#        call her_main("I have needs and...","body_204")
#        call her_main("There's a lot of fabric, [genie_name]")
#        call her_main("...")
#        call her_main("I'll go change immediately, [genie_name]","body_209")
#        show screen bld1
#        with d3
#        show screen blktone
#        with d3
#        call set_h_skirt("jeans_short")
#        call her_main("","body_209",xpos=120,ypos=0)
#        show screen ctc
#        with d3
#        pause
#        call her_main("If you still have time, [genie_name], we could test how long it takes to get out of these things?","body_205")
#        g9 "(I love my job)"
#        call her_main("","body_209",xpos=410)
#    hide screen blktone
#    return


    








### Gryffindor Stockings ###
#label equip_gryyf_stockings:
#    if whoring < 3:
#        call her_main("Is that!?","body_11")
#        call her_main("A pair of Gryffindor stockings!?","body_48")
#        m "Yep?"
#        call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","body_48")
#        m "Probably?"
#        call her_main("I NEED THEM! What'll it cost me!?","body_34")
#        m "No cost"
#        call her_main("!","body_48")
#        m "It's a gift, [hermione_name], to show you what a great guy ME, Proffesor DeltaDwarf, really is!"
#        call her_main("...")
#        call her_main("hhmppphhh", "body_42")
#        call her_main("hahahahahahaha!","body_80b")
#        call her_main("ahhh....","body_157")
#        call her_main("You're too funny! Thanks for the gift! I'll put them on right away","body_01")
#        g6 "(...What did I say?)"
#        call her_main("I've always wanted a pair of these! They're warm, and they reduce unwanted attention from the boys","body_45")
#        call her_main("I will be the next best thing to having a skirt that's twice as long!","body_46")
#        m "Just glad to help, [hermione_name]!"
#        g4 "(hehehe... hope you remember those words after I've made you so needy and desperate you'll suck off a hundred boys just to get off once)"
#        call her_main("They feel great!","body_01",xpos=120,ypos=0)
#        show screen bld1
#        with d3
#        show screen blktone
#        with d3
#        call set_h_stockings("gryff")
#        show screen ctc
#        with d3
#        pause
#        call her_main("Thanks again, [genie_name]! You're too kind","body_01",xpos=410)
#        g9 "(We'll see)"
#        $ request_gryyf_stockings = True
#        
#    #elif whoring >= 3 and whoring <= 6:
#    else:
#        "testedfoteste"
#        $ hermione_wear_skirt = True
#        $ hermione_wear_top = True
#        
#        call her_main("Is that...","body_11")
#        $ hermione_emote_exclam = True
#        call her_main("A pair of Gryffindor stockings!?","body_48")
#        m "Yep?"
#        call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","body_48")
#        m "K?"
#        call her_main("....")
#        $ hermione_emote_exclam = False
#        $ hermione_emote_hearts = True
#        call her_main("I NEED THEM!", "body_34")
#        call her_main("What'll it cost me!?", "body_34")
#        call her_main("WHAT DO I HAVE TO DO!?","body_32")
#        $ hermione_emote_hearts = False
#        m "Just a small favour"
#        call her_main("(!)","body_48")
#        m "All I want, [hermione_name], is to see how great they look on you."
#        m "Easy, right?"
#        call her_main("...")
#        call her_main("You just want to see me in stockings? That should be no problem...", "body_14")
#        call her_main("(Is he up to something?)","body_07")
#        call her_main(".....")
#        call her_main("","body_01",xpos=120,ypos=0)
#        show screen bld1
#        with d3
#        show screen blktone
#        with d3
#        call set_h_stockings("gryff")
#        show screen ctc
#        with d3
#        pause
#        call her_main("What do you think, [genie_name]?")
#        m "Impressive..."
#        m "They look great, [hermione_name]!"
#        call her_main("[genie_name]! My appearance has no bearing on my academic ability.","body_217") #Embarrassed mouth wide eyes closed angry
#        call her_main("......","body_186")
#        call her_main("(That does make me feel kinda nice, though...)","body_186") #Embarrassed mouth open angry
#        g9 "But, I'm having a hard time seeing all the details with that skirt in the way"
#        call her_main("(Oh no...)","body_28") #Worried, teeth showing
#        call her_main("(I knew it! That pervert!)","body_47") #Angry, teeth showing
#        call her_main("(sigh...)","body_47")
#        call her_main("(alright, [hermione_name], we've done this before, it's as easy as Arithmancy)","body_47")
#        call her_main("(there's nothing embarrassing about this!)","body_140") #Worried, embarrassing, small tears
#        call her_main("I'm just showing that bastard a little square of fabric", "body_186")
#        call her_main("That's all!")
#        call her_main("And think of how much more I'll get done without boys staring at my legs all day...","body_141") #Worried, angry, embarrassed
#        m "I'm waiting, [hermione_name]. Don't tell me you don't want your gift?"
#        call her_main("No, [genie_name], I want it.")
#        g9 "Then earn it, [hermione_name]"
#        call her_main("....","body_182b",xpos=120) #embarrassed, eyes closed, mouth closed
#        call set_hermione_action("lift_skirt")
#        $ skirt_up = True
#        show screen hermione_03 #Hermione lifts her skirt
#        with d3
#        pause
#        show screen bld1
#        with d3
#        show screen blktone
#        with d3
#        call her_main("","body_141",xpos=120)
#        show screen ctc
#        with d3
#        pause
#        $ skirt_up = False
#        #call reset_hermione_main
#        show screen hermione_blink #Hermione stands still.
#        with fade
#        m "They suit you, [hermione_name]"
#        call her_main("Again with the sweet talk?")
#        call her_main("(it won't work on someone like me...)", "body_182")
#        m "Your panties, your stockings... they make you look so pretty"
#        call her_main("(ahh! he called me pretty)", "body_188")
#        call her_main("You saw what you wanted... now I can go, right [genie_name]?","body_141",xpos=120)
#        #call her_main("Please?","body_141")
#        m "(True, I did get a great panty shot)"
#        g9 "(But I could try to get more out of her...)"
#        m "What should I do?"
#        menu:
#            "What a cutie! Let her go":
#                m "Of course, [hermione_name]. Enjoy your stockings"
#                $ hermione_emote_hearts = True
#                call set_hermione_action("")
#                call update_her_uniform
#                call her_main("Thanks, [genie_name]! I'll wear them whenever you want.","body_209")
#                call her_main("(phew. why does it feel like a dodged a bullet, though?)","body_209")
#                $ hermione_emote_hearts = False
#                $mad = 0
#            
#            "Cute is boring. Break her.":
#               m "That was certainly adequate, [hermione_name]..."
#               call her_main("(Adequate...?)","body_81",xpos=120)
#               m "But..."
#               call her_main("oh no...","body_48",xpos=120)
#               m "You're one of our top students..."
#               m "And there were still areas I couldn't see..."
#               m "You're not giving it 100\%, here!"
#               call her_main("(No way...)","body_48",xpos=120)
#               g4 "You're going to remove your skirt"
#               g4 "Then you're going to remove your panties."
#               g9 "And then I'm going to get a proper look. Just as we agreed."
#               call set_hermione_action("")
#               $ hermione_emote_anger = True
#               call her_main("NO", "body_218")
#               g4 "(?)"
#               call her_main("NO WAY!")
#               call her_main("THERE IS ABSOLUTELY NO WAY AM I GOING TO DO THAT!!!")
#               call her_main("I'm not some cheap slytherin slut that you can just play with!","body_148")
#               g4 "..."
#               m "Would you like to have your gift taken back from you?"
#               $ hermione_emote_anger = False
#               $ hermione_emote_exclam = True
#               call her_main("....","body_140")
#               m "Forfeit your points?"
#               $ hermione_emote_exclam = False
#               call her_main("...........","body_140")
#               m "How about I remove some points for disobeying the head master?"
#               call her_main("...............","body_48",xpos=145)
#               m "And end our tutoring arrangement all together..."
#               m "I wonder what will happen to your report card?"
#               m "I wonder what your parents will think..."
#               g9 "When they realize they've raised a failure"
#               call her_main("Stop it...","body_143")
#               g9 "(Hmm?)"
#               call her_main("I get it already...","body_143",xpos=120)
#               call her_main(".......","body_143")
#               $mad += 55
#               ">With tears rolling down her soft cheeks, Hermione begins to unzip her skirt"
#               ">Her trembling hands make it difficult just to keep hold of the zipper"
#               ">Eventually she gets it, and after hooking her thumb over her panties, she lowers the rest of her dignity to the floor"    
#               $ hermione_wear_skirt = False
#               #$ h_request_wear_panties = False
#               call update_her_uniform
#               hide screen ctc
#               with d3
#               pause
#               $ hermione_wear_panties = False
#               call update_her_uniform
#               show screen bld1
#               with d3
#               show screen blktone
#               with d3
#               call her_main("","body_147")
#               pause
#               show screen ctc
#               with d3
#               m "Hands behind your back, [hermione_name]. I want to see everything."
#               call her_main(".....","body_145")
#               call set_hermione_action("hands_behind")
#               call set_hermione_action("")
#               ">Too weak to fight back, Hermione does as she's told"
#               hide screen ctc
#               with d3
#               show screen bld1
#               with d3
#               show screen blktone
#               with d3
#               call her_main("","body_145")
#               pause
#               show screen ctc
#               with d3
#               m "Good girl."
#               g9 "(What a spectacular body...)"
#               call her_main(".......","body_145")
#               call her_main("(After all he's done to me... why do i feel...)","body_145")
#               call her_main("(like i'm still on fire...)","body_145")
#               call her_main("this doesn't make any sense","body_145")
#               call her_main("Ahh... hehehehehehehe","body_142")
#               m "(...has she lost it already?)"
#               call her_main("(whatever... it doesn't need to make sense)")
#               call her_main("(You're headed straight to Azkaban once this is over, anyway)","body_142")
#               call her_main("(so at least for now, keep looking at my body!)","body_142")
#               call her_main("(my whole body needs to melt)","body_142")
#               g9 "(hehehehe, i hope [hermione_name] can feel it)"
#               g9 "(how a bitch feels when she's in heat)"
#               ">Slowly but surely, you see a trickle of nectar begin to leak out of Hermione."
#               $ hermione_dribble = True
#               call h_update_body
#               hide screen ctc
#               with d3
#               show screen bld1
#               with d3
#               show screen blktone
#               with d3
#               call her_main("","body_158")
#               pause
#               show screen ctc
#               with d3
#               call her_main("(This is....)")
#               call her_main("(too good)")
#               g9 "(heh. once i'm done with you, you'll be dripping like this every day)"
#               call her_main("(more....)")
#               call her_main("(i want to be tutored more by [genie_name]!)")
#               m "..."
#               g9 "....."
#               call her_main (".....")
#               m "We're done here, [hermione_name]"
#               call her_main(".....","body_158")
#               m "You can keep the stockings."
#               call her_main(".......","body_158")
#               m "And 50 points to Gryffindor for your outstanding preformance."
#               $ gryffindor += 50
#               call her_main("..........","body_158")
#               g4 "What do you say when you've been given a gift?"
#               call her_main("..........","body_158")
#               call her_main("Thank you, [genie_name]","body_158")
#               g9 "That's right, [hermione_name]."
#               m "Don't forget your clothes on the way out."
#               call her_main("(my... p..)","body_158")
#               call her_main("(..pussy is throbbing)","body_158")
#               call her_main("(i might become an addict if i'm not careful)","body_158")
#               ">Hermione retrieves her clothes and starts putting them back on"
#               call her_main("(just the panties touching...)","body_142")
#               call her_main("(feels incredible!)","body_142")
#               "You can't help but notice stains on the pure white fabric that's hugging her leaking cunt "
#               call set_hermione_action("hands_free")
#               call set_hermione_action("")
#               $ hermione_wetpanties = True
#               $ hermione_wear_panties = True
#               call update_her_uniform
#               hide screen ctc
#               with d3
#               show screen bld1
#               with d3
#               show screen blktone
#               with d3
#               call her_main("","body_142")
#               pause
#               call her_main("(ahh, i've made them all sloppy)","body_142")
#               g9 "We're going to have a lot of fun in future, [hermione_name]"
#               call her_main("","body_142")
#               $ hermione_wear_skirt = True
#               $ hermione_dribble = False
#               call update_her_uniform
#               with d3
#               call her_main("","body_158")
#               ">'Leaking' overlay now equip-able!"
#               ">'Wet panties' overlay now equip-able!"
#               $ hermione_wetpanties = True
#               $ dribble_equippable = True
#               $ wetpanties_equippable = True
#       
#        hide screen blktone
#        hide screen bld1
#        hide screen hermione_main
#        hide screen hermione_stand_f #Hermione stands still.
#        with d3
#        call her_walk(400,610,2)
#        $ request_gryyf_stockings = True
#        ">Gryffindor stockings now equip-able!"
#        #call reset_hermione_main
#       
#        jump end_hg_pf
#    
#    #jump day_request_clothing
#    return
