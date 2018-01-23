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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 210 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
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
        text "Accs." xpos 310 ypos 100 size 15
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
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
        text "Accs." xpos 310 ypos 100 size 15
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
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
        text "Accs." xpos 310 ypos 100 size 15
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
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
        text "Accs." xpos 310 ypos 100 size 15
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
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
        text "Accs." xpos 310 ypos 100 size 15
        text "Underwear" xpos 370 ypos 100 size 15 bold 1
        #text "Gifts" xpos 480 ypos 100 size 15

screen wardrobe_ginny_accessories:
    
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
        hotspot (301, 30, 67, 82) clicked Show("wardrobe_ginny_accessories")
        hotspot (391, 30, 67, 82) clicked Show("wardrobe_ginny_underwear")
        #hotspot (480, 30, 67, 82) clicked Show("wardrobe_gifts")
        
        for i in range(0,12):
            if i < 6:
                hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("ginny_wardrobe_accessory1",str(i+1)),Jump("change_ginny_accessory")]
            else:
                hotspot ((21+(90*(i-6))), 232, 83, 85) clicked [SetVariable("ginny_wardrobe_accessory1",str(i+1)),Jump("change_ginny_accessory")]

            #gryff_robe
            #hotspot ((21+(90*i)), 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 232, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
            #hotspot ((21+(90*i)), 324, 83, 85) clicked [SetVariable("wardrobe_hair_style","C"),SetVariable("wardrobe_hair_color",(i+1)),Jump("change_hair")]
        
        for i in range(0,12):
            if i < 6:
                add "01_hp/13_characters/ginny_weasley/clothes/accessories/"+str(i+1)+".png" xpos -30+(90*i) ypos 60 zoom 0.35
            else:
                add "01_hp/13_characters/ginny_weasley/clothes/accessories/"+str(i+1)+".png" xpos 20+(90*(i-6)) ypos 232 zoom 0.35



            #add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35
            #add "01_hp/13_characters/hermione/body/head/C_"+str(i+1)+".png" xpos -45+(90*i) ypos 285 zoom 0.35

        text "Robes" xpos 30 ypos 100 size 15
        text "Tops" xpos 130 ypos 100 size 15
        text "Bottom" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15 bold 1
        text "Underwear" xpos 370 ypos 100 size 15
        #text "Gifts" xpos 480 ypos 100 size 15


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
    #call ginny_main("Sure, let me just gooo change it.")
    #$ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+ginny_wardrobe_bottom+".png"
    call equip_bottom_ginny(ginny_wardrobe_bottom)
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

label change_ginny_accessory():
    call ginny_main("Sure, let me just gooo change it.")

    if gw_wear_accessory1 == True and gw_accessory1 == "01_hp/13_characters/ginny_weasley/clothes/accessories/"+ginny_wardrobe_accessory1+".png": 
        $ gw_wear_accessory1 = False
    else:
        $ gw_wear_accessory1 = True
        $ gw_accessory1 = "01_hp/13_characters/ginny_weasley/clothes/accessories/"+ginny_wardrobe_accessory1+".png"
    call ginny_main("",1)
    #call set_h_hair(wardrobe_hair_style,wardrobe_hair_color)
    #"test"
    hide screen wardrobe_ginny_accessories
    call screen wardrobe_ginny_accessories


                    
