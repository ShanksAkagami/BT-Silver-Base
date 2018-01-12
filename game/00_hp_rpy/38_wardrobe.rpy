screen wardrobe:
    $ hermione_SC.xpos=550
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")

        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 375 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny:
    #$ hermione_SC.xpos=550
    #changeGinny(1, xpos=550)
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 210 ypos 100 size 15
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 375 ypos 100 size 15
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_robes:
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,7):
            if i < 6:
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_robe",str(i+1)),Jump("change_ginny_robe")]
            else:
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_robe",str(i+1)),Jump("change_ginny_robe")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,7):
            if i < 6:
                add "01_hp/13_characters/ginny_weasley/clothes/robe/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/robe/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15 bold 1
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 210 ypos 100 size 15
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_top:
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,9):
            if i < 6:
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_top",str(i+1)),Jump("change_ginny_top")]
            else:
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_top",str(i+1)),Jump("change_ginny_top")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,9):
            if i < 6:
                add "01_hp/13_characters/ginny_weasley/clothes/tops/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/tops/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15 bold 1
        text "Bottom" xpos 210 ypos 100 size 15
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_bottom:
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,8):
            if i < 6:
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_bottom",str(i+1)),Jump("change_ginny_bottom")]
            else:
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_bottom",str(i+1)),Jump("change_ginny_bottom")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,8):
            if i < 6:
                add "01_hp/13_characters/ginny_weasley/clothes/bottom/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/bottom/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 200 ypos 100 size 15 bold 1
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_underwear:
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground_next.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover_next.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        hotspot (535, 570,28,28) clicked Show("wardrobe_ginny_underwear_2")
        
        for i in range(0,13):
            if i < 6:
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_bra",str(i+1)),Jump("change_ginny_bra")]
                #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_panties",str(i+1)),Jump("change_ginny_panties")]
            elif i < 12:
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_bra",str(i+1)),Jump("change_ginny_bra")]
                #hotspot ((21+(90*(i-6))), 416, 83, 85) clicked [SetVariable("ginny_wardrobe_panties",str(i+1)),Jump("change_ginny_panties")]
            else:
                hotspot ((21+(90*(i-12))), 324, 83, 85) clicked [SetVariable("ginny_wardrobe_bra",str(i+1)),Jump("change_ginny_bra")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,13):
            if i < 6:
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
                #add "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 232 zoom 0.35
            elif i < 12:
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35
                #add "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 416 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+str(i+1)+"_icon.png" xpos 20+(90*(i-12)) ypos 324 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 200 ypos 100 size 15
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15 bold 1
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_underwear_2:
    
    tag wardrobe_ginny_menu
    zorder gw_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_ground_next.png"
        hover "01_hp/13_characters/ginny_weasley/wardrobe_ginny/wardrobe_hover_next.png"

        hotspot (742+280,10,42,41) clicked Jump("ginny_secondmenu")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_ginny_robes")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_ginny_top")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_ginny_bottom")
        #hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        hotspot (535, 570,28,28) clicked Show("wardrobe_ginny_underwear")
        
        for i in range(0,13):
            if i < 6:
                #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_bra",str(i+1)),Jump("change_ginny_bra")]
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_panties",str(i+1)),Jump("change_ginny_panties")]
            elif i < 12:
                #hotspot ((21+(90*(i-6))), 324, 83, 85) clicked [SetVariable("ginny_wardrobe_bra",str(i+1)),Jump("change_ginny_bra")]
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_panties",str(i+1)),Jump("change_ginny_panties")]
            else:
                hotspot ((21+(90*(i-12))), 324, 83, 85) clicked [SetVariable("ginny_wardrobe_panties",str(i+1)),Jump("change_ginny_panties")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,13):
            if i < 6:
                #add "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+str(i+1)+"_icon.png" xpos 20+(90*i) ypos 140 zoom 0.35
            elif i < 12:
                #add "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 324 zoom 0.35
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+str(i+1)+"_icon.png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+str(i+1)+"_icon.png" xpos 20+(90*(i-12)) ypos 324 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 200 ypos 100 size 15
        #text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15 bold 1
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_hair:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,13):
            hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,13):
            add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Hair" xpos 45 ypos 100 size 15 bold 1
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15
    
    
label change_hair_new:
    #call her_main("Sure, let me just ogooo change it.","body_01")
    $ hermione_SC.setHair(wardrobe_hair_style,wardrobe_hair_color)
    hide screen wardrobe_hair
    call screen wardrobe_hair

    
    
    
label change_hair():
    call her_main("Sure, let me just gooo change it.","body_01")
    call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    hide screen wardrobe_hair
    call screen wardrobe_hair

label change_ginny_robe():
    call ginny_main("Sure, let me just gooo change it.")
    $ gw_robes = "01_hp/13_characters/ginny_weasley/clothes/robe/"+ginny_wardrobe_robe+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_robes
    call screen wardrobe_ginny_robes

label change_ginny_top():
    call ginny_main("Sure, let me just gooo change it.")
    $ gw_top = "01_hp/13_characters/ginny_weasley/clothes/tops/"+ginny_wardrobe_top+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_top
    call screen wardrobe_ginny_top

label change_ginny_bottom():
    call ginny_main("Sure, let me just gooo change it.")
    $ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+ginny_wardrobe_bottom+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_bottom
    call screen wardrobe_ginny_bottom

label change_ginny_bra():
    call ginny_main("Sure, let me just gooo change it.")
    $ gw_bra = "01_hp/13_characters/ginny_weasley/clothes/underwear/bra/"+ginny_wardrobe_bra+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_underwear
    call screen wardrobe_ginny_underwear

label change_ginny_panties():
    call ginny_main("Sure, let me just gooo change it.")
    $ gw_panties = "01_hp/13_characters/ginny_weasley/clothes/underwear/panties/"+ginny_wardrobe_panties+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_underwear_2
    call screen wardrobe_ginny_underwear_2

screen wardrobe_uniform:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    $ list = ["skirt_1","skirt_2","skirt_3", "skirt_4", "skirt_5"]
    $ y_pos = 13
    if "jeans_long" in cs_existing_stock:
        $ list.append("jeans_long")
    if "jeans_short" in cs_existing_stock:
        $ list.append("jeans_short")
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")

        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        
        # (13,116) (13+90,116)
        
        # (13,208)
        
        for i in range(0,len(list)):
            hotspot ((21+(90*(i%6))), (140+(92*int(i/6))), 83, 85) clicked [SetVariable("wardrobe_uniform_selection",list[i]),Jump("change_uniform")]
        
        for i in range(0,len(list)):
            add "01_hp/13_characters/hermione/clothes/uniform/bot/"+list[i]+".png" xpos -40+(90*(i%6)) ypos y_pos zoom 0.35
            if i != 0 and (i % 5) == 0:
                $ y_pos += 100

        $ y_pos += 80
        for i in range(len(list), len(list)+6): #Shirts
            hotspot ((21+(90*(i%6))), (140+(92*int(i/6))), 83, 85) clicked [SetVariable("wardrobe_uniform_selection",("top_"+str(i+1-len(list)))),Jump("change_uniform")]
            add "01_hp/13_characters/hermione/clothes/uniform/top_"+str(i+1-len(list))+".png" xpos -10+(90*(i%6)) ypos y_pos zoom 0.25
            if i != 0 and (i % 5) == 0:
                $ y_pos += 100
            
        #for i in range(0,6):
            # for j in range (0,6):
                # hotspot ((21+(90*i)), 140+(92*j), 83, 85) clicked [SetVariable("",),SetVariable("",),Jump("change_hair")]
        
        
        text "Hair" xpos 45 ypos 100 size 15 
        text "Uniform" xpos 115 ypos 100 size 15 bold 1
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15
    
label change_uniform:
    call equip_bot(wardrobe_uniform_selection)
    hide screen wardrobe_uniform
    call screen wardrobe_uniform
    
screen wardrobe_costumes:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")

        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        $ hg_purchased_outfits = []
        for i in hermione_outfits_list:
            if i.purchased:
                $ hg_purchased_outfits.append(i)
        
        $ index = 0
        for i in range(0,5):
            for j in range(0,6):
                if index < len(hg_purchased_outfits):
                    hotspot ((21+(90*j)), (140+(92*i)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_outfits[index]),Jump("wardrobe_wear_costume")]
                    add hg_purchased_outfits[index].getStoreImage() xpos (13+(90*j)) ypos (116+(92*i)) zoom 0.18
                    $ index = index+1
        
        hotspot (471, 508, 83, 85) clicked [SetVariable("wardrobe_costume_selection",None),Jump("wardrobe_wear_costume")]
        add "01_hp/23_clothes_store/cs_gui/uniform.png" xpos 463 ypos 484 zoom 0.18
            
        text "Hair" xpos 45 ypos 100 size 15 
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15 bold 1
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15
    
    
label wardrobe_wear_costume_new:
    hide screen hermione_main
    $ renpy.show_screen(hermione_SC.main_screen)
    $ hermione_SC.setOutfit(wardrobe_costume_selection)
    hide screen wardrobe_costumes
    call screen wardrobe_costumes
    
label wardrobe_wear_costume:
    hide screen hermione_main
    call h_outfit_OBJ(wardrobe_costume_selection)
    show screen hermione_main
    hide screen wardrobe_costumes
    call screen wardrobe_costumes
    
screen wardrobe_gifts:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        # note that gift_items are indices (starting with 0) but the
        # image files are starting with/off by 1.
        for i in range(0,18):
            $ row = i // 6
            $ col = i % 6
            if gift_item_inv[i] > 0:
                hotspot ((21+(90*col)), (140+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",i),Jump("wardrobe_give_gift")]
            add "01_hp/18_store/gifts/"+str(i+1)+".png" xpos -60+(90*col) ypos (90+(90*row)) zoom 0.30
            text str(gift_item_inv[i]) xpos 20+(90*col) ypos (210+(90*row))


        #Adding custom one off items (Collar, dress, stockings)

        #Collar
        if collar == 0 and whoring >= 24:
            hotspot (470, 508, 83, 85) clicked [Jump("start_collar_event")]
            add "01_hp/13_characters/hermione/accessories/collars/collar_0.png" xpos 255 ypos 350 zoom 0.8
        else:
            add "01_hp/13_characters/hermione/accessories/collars/collar_5.png" xpos 255 ypos 350 zoom 0.8 
        #Dress 
        if whoring >= 24 and have_no_dress_hap and not gave_the_dress:
            hotspot (380, 508, 83, 85) clicked [Jump("giving_the_dress")]
            add "01_hp/23_clothes_store/cs_gui/ball_dress.png" xpos 13+(90*4) ypos 484 zoom 0.18
        else:
            add "01_hp/23_clothes_store/cs_gui/ball_dress_b.png" xpos 13+(90*4) ypos 484 zoom 0.18
            
        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15 bold 1
    
label wardrobe_give_gift:
    call give_her_gift(wardrobe_gift_item)
    hide screen wardrobe_gifts
    call screen wardrobe_gifts

screen wardrobe_accessories:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        if "SPEW_badge" in cs_existing_stock:
            hotspot (21, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",0),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/badges/spew_badge.png" xpos -185 ypos -125
        if "CUM_badge" in cs_existing_stock:
            hotspot (21+90, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",1),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/badges/cum_badge.png" xpos -95 ypos -125
        if "tiara" in cs_existing_stock:
            hotspot (21+180, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",2),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/tiara.png" xpos -55 ypos 50
        if "freckles" in cs_existing_stock:
            hotspot (21+270, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",3),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/freckles.png" xpos 50 ypos -25
        if "reading_glasses" in cs_existing_stock:
            hotspot (21+360, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",4),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/reading_glasses.png" xpos 140 ypos -30
        if "vintage_glasses" in cs_existing_stock:
            hotspot (21+450, 140, 83, 85) clicked [SetVariable("wardrobe_acc_item",5),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/vintage_glasses.png" xpos 230 ypos -20
        if "fake_cum" in cs_existing_stock:
            hotspot (21, 230, 83, 85) clicked [SetVariable("wardrobe_acc_item",6),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/cum_icon.png" xpos -215 ypos 120
        if "cat_ears" in cs_existing_stock:
            hotspot (21+90, 230, 83, 85) clicked [SetVariable("wardrobe_acc_item",7),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/cat_ears.png" xpos -28 ypos 180 zoom 0.6
        if "transparency" in cs_existing_stock:
            hotspot (21+180, 230, 83, 85) clicked [SetVariable("wardrobe_acc_item",8),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/potion.png" xpos 195 ypos 225 zoom 0.8
        if "elf_ears" in cs_existing_stock:
            hotspot (21+270, 230, 83, 85) clicked [SetVariable("wardrobe_acc_item",9),Jump("wardrobe_give_acc")]
            add "01_hp/13_characters/hermione/accessories/head/elf_ears.png" xpos 65 ypos 120 zoom 0.8


        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15 bold 1
        text "Underwear" xpos 370 ypos 100 size 15
        text "Gifts" xpos 480 ypos 100 size 15 
    
label wardrobe_give_acc:
    call give_her_acc(wardrobe_acc_item)
    hide screen wardrobe_accessories
    call screen wardrobe_accessories
    
screen wardrobe_underwear:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    $ wardrobe_underwear_selection = []
    $ wardrobe_underwear_selection.append("lace")
    $ wardrobe_underwear_selection.append("latex")
    $ wardrobe_underwear_selection.append("silk")
    $ wardrobe_underwear_selection.append("base")
    if "gryffindor_stockings" in cs_existing_stock:
        $ wardrobe_underwear_selection.append("gryffindor_stockings")
    if "fishnet_stockings" in cs_existing_stock:
        $ wardrobe_underwear_selection.append("fishnet_stockings")
    if "lace_stockings" in cs_existing_stock:
        $ wardrobe_underwear_selection.append("lace_stockings")
        
    
    
    
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_underwear")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_potions")
        
        for i in range(0,len(wardrobe_underwear_selection)):
            hotspot ((21+(90*i)), 140, 83, 85):
                #if wardrobe_underwear_selection != "lace_bra":
                clicked [SetVariable("wardrobe_underwear_selection",wardrobe_underwear_selection[i]),Jump("wardrobe_wear_underwear")]
                #else:
                #    clicked [SetVariable("wardrobe_underwear_selection",wardrobe_underwear_selection[i]),Jump("wardrobe_wear_underwear2")]
        
        for i in range(0,len(wardrobe_underwear_selection)):
            add "01_hp/13_characters/hermione/clothes/stockings/"+str(wardrobe_underwear_selection[i])+"troll.png" xpos -105+(90*i) ypos -135 zoom 0.6
        
        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15 bold 1
        text "Gifts" xpos 480 ypos 100 size 15
    
    
label wardrobe_wear_underwear:
    if wardrobe_underwear_selection != "lace" and wardrobe_underwear_selection != "latex" and wardrobe_underwear_selection != "silk" and wardrobe_underwear_selection != "base":
        "teste"
        #call set_h_stockings(wardrobe_underwear_selection)
        call equip_gryyf_stockings
        "teste3"
    else:
        call set_h_underwear(wardrobe_underwear_selection + "_bra",wardrobe_underwear_selection + "_panties")
    
    hide screen wardrobe_underwear
    call screen wardrobe_underwear
    
label wardrobe_wear_underwear2:
    #call h_panties_off
    #call h_bra_off
    call set_h_underwear("lace_bra","lace_panties")
    hide screen wardrobe_underwear
    call screen wardrobe_underwear
    
    
screen wardrobe_potions: #(Removed)
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    $ potion_name = ""
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (742+280,10,42,41) clicked Jump("day_time_requests")
        
        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        hotspot (123, 30, 67, 82) clicked Show("wardrobe_uniform")
        hotspot (212, 30, 67, 82) clicked Show("wardrobe_costumes")
        # hotspot (301, 30, 67, 82) clicked Show("wardrobe_accessories")
        # hotspot (391, 30, 67, 82) clicked Show("wardrobe_gifts")
        hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,6):
            hotspot ((21+(90*i)), 140, 83, 85):
                hovered [SetVariable("potion_name",p_potion_names[i])]
                clicked [SetVariable("wardrobe_potion",i+1),Jump("day_request_wardrobe")]
        
        for i in range(1,7):
            add "01_hp/25_mo/potion_"+str(i)+".png" xpos -80+(90*i) ypos 135 zoom 0.8
        for i in range(7,11):
            add "01_hp/25_mo/potion_"+str(i)+".png" xpos -80+(90*(i-6)) ypos 225 zoom 0.8
        
        
        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Gifts" xpos 375 ypos 100 size 15
        text "Potions" xpos 475 ypos 100 size 15 bold 1
    
label wardrobe_give_potion:
    hide screen wardrobe_gifts
    #$ renpy.jump("potion_scene_"+str(wardrobe_potion))
    
label day_request_wardrobe:
    hide screen wardrobe_gifts
    menu:
        "-Hair-":
            label day_request_hair:
            menu:
                "-Wear your hair up-" if not h_hair_style == "B":
                    call her_main("Sure, let me just go change it.","body_01")
                    call set_h_hair_style("B")
                    jump day_request_hair
                    
                "-Wear your hair down-" if not h_hair_style == "A":
                    call her_main("Sure, let me just go change it.","body_01")
                    call set_h_hair_style("A")
                    jump day_request_hair
                    
                "-Dye your hair-":
                    label day_request_hair_dye:
                    menu:
                        "-Dye Brown-" if not h_hair_color == 1:
                            call her_main("Brown seems so boring now.","body_01")
                            call set_h_hair_color(1)
                            jump day_request_hair_dye
                            
                        "-Dye Blonde-" if not h_hair_color == 2:
                            call her_main("Why do you want me to change my hair?","body_01")
                            m "I don't know, I suppose I just have a thing for blondes"
                            her "well I've always heard blondes have more fun!"
                            call set_h_hair_color(2)
                            jump day_request_hair_dye
                            
                        "-Dye Red-" if not h_hair_color == 3:
                            call her_main("this'll be fun, Maybe I'll look like Batwoman!","body_01")
                            m "You read comics?"
                            her "no, i just play certain games"
                            m "What?"
                            call set_h_hair_color(3)
                            jump day_request_hair_dye
                            
                        "-Dye Black-" if not h_hair_color == 4:
                            call her_main("I have been feeling a bit depressed recently.","body_01")
                            her "I wonder if it's because of all the favors I've been doing"
                            m "Don't worry about it"
                            call set_h_hair_color(4)
                            jump day_request_hair_dye
                            
                        "-Dye Blue-" if not h_hair_color == 5:
                            call her_main("Blue?","body_01")
                            m "Why not?"
                            her "Just seems a bit attention seeking..."
                            call set_h_hair_color(5)
                            jump day_request_hair_dye
                            
                        "-Dye Orange-" if not h_hair_color == 6:
                            call her_main("Orange?","body_01")
                            m "That's what I said."
                            her "Alright, well just let me change it."
                            call set_h_hair_color(6)
                            jump day_request_hair_dye
                            
                        "-Never mind-":
                            jump day_request_hair
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Clothing-":
            label day_request_clothing:
            menu:
                "-Don't wear a top-" if hermione_wear_top:
                    call h_top_off
                    jump day_request_clothing
                    
                "-Put top back on-" if not hermione_wear_top:
                    call h_top_on
                    jump day_request_clothing
                    
                "-Don't wear a skirt-" if hermione_wear_skirt:
                    call h_skirt_off
                    jump day_request_clothing
                    
                "-Put skirt back on-" if not hermione_wear_skirt:
                    call h_skirt_on
                    jump day_request_clothing
                    
                "-Stop wearing panties-" if h_request_wear_panties and whoring >= 6:
                    call h_panties_off
                    jump day_request_clothing
                    
                "-Wear panties-" if not h_request_wear_panties and whoring >= 6:
                    call h_panties_on
                    jump day_request_clothing
                    
                "-Stockings-":
                    label day_request_clothing_stockings:
                    menu:
                        "-Put the fishnets on-" if "fishnet_stockings" in cs_existing_stock and h_stocking != "fishnet_a":
                            call set_h_stockings("fishnet_a")
                            jump day_request_clothing_stockings
                            
                        "-Take the fishnets off-" if "fishnet_stockings" in cs_existing_stock and h_stocking == "fishnet_a":
                            call set_h_stockings
                            jump day_request_clothing_stockings
                            
                        "-Put the Gryffindor Stockings on-" if "gryffindor_stockings" in cs_existing_stock and h_stocking != "gryff":
                            if request_gryyf_stockings == False and whoring <= 6:
                                jump equip_gryyf_stockings
                            else:
                                call set_h_stockings("gryff")
                                jump day_request_clothing_stockings
                            
                        "-Take the Gryffindor Stockings off-" if "gryffindor_stockings" in cs_existing_stock and h_stocking == "gryff":
                            call set_h_stockings
                            jump day_request_clothing_stockings
                            
                        "-Never mind-":
                            jump day_request_clothing
                    
                "-Underwear-":
                    label day_request_clothing_underwear:
                    menu:
                        "-Put the Lace Bra and Panties on-" if h_bra != "lace_bra":
                            call set_h_underwear("lace_bra","lace_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Lace Bra and Panties off-" if h_bra == "lace_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Cup-less Lace Bra on-" if h_bra != "cup_bra":
                            call set_h_underwear("cup_bra","cup_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Cup-less Lace Bra off-" if h_bra == "cup_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Silk Bra and Panties on-" if h_bra != "silk_bra":
                            call set_h_underwear("silk_bra","silk_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Silk Bra and Panties off-" if h_bra == "silk_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Latex and Panties on-" if h_bra != "latex_bra":
                            call set_h_underwear("latex_bra","latex_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Latex and Panties off-" if h_bra == "latex_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                        
                        "-Never mind-":
                            jump day_request_clothing
                    
                "-Put the jeans on-" if "jeans_long" in cs_existing_stock and h_skirt != "jeans_long":
                    if request_jeans == False:
                        jump equip_jeans
                    else:
                        call set_h_skirt("jeans_long")
                        jump day_request_clothing
                    
                "-Take the jeans off-" if h_skirt == "jeans_long":
                     call set_h_skirt
                     jump day_request_clothing
                    
                "-Put the short jeans on-" if "jeans_short" in cs_existing_stock and h_skirt != "jeans_short":
                     call set_h_skirt("jeans_short")
                     jump day_request_clothing
                    
                "-Take the short jeans off-"if h_skirt == "jeans_short":
                     call set_h_skirt
                     jump day_request_clothing
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Accessories-":
            label day_request_accessories:
            menu:
                "-Put \"S.P.E.W.\" badge on-" if "SPEW_badge" in cs_existing_stock and h_badge != "SPEW_badge":
                    call h_badge_on("SPEW_badge")
                    jump day_request_accessories
                    
                "-Take \"S.P.E.W.\" badge off-" if "SPEW_badge" in cs_existing_stock and h_badge == "SPEW_badge":
                    call h_badge_off
                    jump day_request_accessories
                    
                "-Put I <3 C.U.M.\" badge on-" if "CUM_badge" in cs_existing_stock and h_badge != "CUM_badge":
                    call h_badge_on("CUM_badge")
                    jump day_request_accessories
                    
                "-Take I <3 C.U.M.\" badge off-" if "CUM_badge" in cs_existing_stock and h_badge == "CUM_badge":
                    call h_badge_off
                    jump day_request_accessories
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Collars-" if False:
            label day_request_collars:
            menu:
                "-Take off the collar-" if collar >= 1:
                    $ collar = 0
                    jump day_request_collars
                "-Put on the slave collar-":
                    $ collar = 1
                    jump day_request_collars
                "-Put on the slut collar-":
                    $ collar = 2
                    jump day_request_collars
                "-Put on the whore collar-":
                    $ collar = 3
                    jump day_request_collars
                "-Never mind-":
                    jump day_request_wardrobe
                    
        "-Overlays-":
            label day_request_overlays:
            menu:
            
                "{color=#858585}-Thigh Grool Locked-{/color}" if dribble_equippable == False:
                    "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                    jump day_request_overlays
                
                "{color=#858585}-Damp Panties Locked-{/color}" if wetpanties_equippable == False:
                    "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                    jump day_request_overlays
                
                "-Thigh Grool On-" if dribble_equippable == True and hermione_dribble == False:
                    $ hermione_dribble = True
                    call update_her_uniform
                    jump day_request_overlays
                "-Thigh Grool Off-" if dribble_equippable == True and hermione_dribble == True:
                    $ hermione_dribble = False
                    call update_her_uniform
                    jump day_request_overlays
                
                "-Damp Panties On-" if wetpanties_equippable == True and hermione_wetpanties == False:
                    $ hermione_wetpanties = True
                    call update_her_uniform
                    jump day_request_overlays
                    
                "-Damp Panties Off-" if wetpanties_equippable == True and hermione_wetpanties == True:
                    $ hermione_wetpanties = False
                    call update_her_uniform
                    jump day_request_overlays  
                    
                "-Never mind":
                    jump day_time_requests
                    
