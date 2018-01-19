screen ginny_weasleyold:
    ### BASE IMAGE
    #add cc_arms xpos cc_xpos ypos cc_ypos #Add the arms
    if not gw_wear_top and not gw_wear_bra:
        $ gw_base = "01_hp/13_characters/ginny_weasley/base/base_00_nip.png"
        add gw_base xpos gw_xpos ypos gw_ypos #Add the base body
    else:
        $ gw_base = "01_hp/13_characters/ginny_weasley/base/base_00.png"
        add gw_base xpos gw_xpos ypos gw_ypos #Add the base body
   
    
    #add cc_hair_shadow xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ### EMOTIONS
    #add cc_eye xpos cc_xpos ypos cc_ypos #Add the eye outline
    #add cc_pupil xpos cc_xpos ypos cc_ypos #Add the pupil
    #add cc_eyebrow xpos cc_xpos ypos cc_ypos #Add the eyebrow
    #add cc_hair xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ###MOUTH
    #add cc_mouth xpos cc_xpos ypos cc_ypos #Add the mouth
    ###TEARS for fears
    #add cc_tears xpos cc_xpos ypos cc_ypos #Add the tears
    ### CLOTHES 
    if gw_wear_bra and not gw_wear_top:
        add gw_bra xpos gw_xpos ypos gw_ypos # Add the bra
    if gw_wear_panties and not gw_wear_skirt:
        add gw_panties xpos gw_xpos ypos gw_ypos # Add the panties
    elif gw_wear_panties and gw_wear_skirt:
        add gw_panties xpos gw_xpos ypos gw_ypos # Add the panties
        add gw_skirt xpos gw_xpos ypos gw_ypos # Add the skirt
    if gw_wear_top:
        add gw_top xpos gw_xpos ypos gw_ypos # Add the top
    
    #if cc_wear_acc:
    #    add cc_acc xpos cc_xpos ypos cc_ypos # Add the accessory
    #if cc_wear_vest:
    #    add cc_vest xpos cc_xpos ypos cc_ypos # Add the vest
    #if cc_wear_stockings:
    #    add cc_stock xpos cc_xpos ypos cc_ypos # Add the stockings
    ### OTHER
    #add cc_l_hand xpos cc_xpos ypos cc_ypos # Add the left hand
    ### ZORDER
    #zorder gw_zorder
    zorder gw_zorder

screen ginny_weasley:
    ### BASE IMAGE
    #add cc_arms xpos cc_xpos ypos cc_ypos #Add the arms
    #if not gw_wear_top and not gw_wear_bra:
    #    $ gw_base = "01_hp/13_characters/ginny_weasley/base/base_00_nip.png"
    #    add gw_base xpos gw_xpos ypos gw_ypos #Add the base body
    #else:
    #    $ gw_base = "01_hp/13_characters/ginny_weasley/base/base_00.png"
        #add gw_base xpos gw_xpos ypos gw_ypos #Add the base body

    #$ gw_freckles = "01_hp/13_characters/ginny_weasley/body/overlay/freckles_body.png" #not good when arms change and stuff

    if not gw_kneeling:
        $ gw_torso = "01_hp/13_characters/ginny_weasley/body/torso/default.png"
        add gw_hair_layer xpos gw_xpos ypos gw_ypos
        if not gw_botharms:
            add gw_arms_right xpos gw_xpos ypos gw_ypos

        add gw_torso xpos gw_xpos ypos gw_ypos
        #if not gw_botharms:
        #    $ gw_legs = "01_hp/13_characters/ginny_weasley/body/legs/default.png"
        #else:
        #    $ gw_legs = "01_hp/13_characters/ginny_weasley/body/legs/open.png"
        if not gw_legsopen:
            $ gw_legs = "01_hp/13_characters/ginny_weasley/body/legs/default.png"
        else:
            $ gw_legs = "01_hp/13_characters/ginny_weasley/body/legs/open.png"

        add gw_legs xpos gw_xpos ypos gw_ypos
        if not gw_botharms:
            add gw_arms_left xpos gw_xpos ypos gw_ypos
            #add gw_arms_right xpos gw_xpos ypos gw_ypos
        
        if not gw_wear_top and not gw_wear_bra:
            $ gw_tits = "01_hp/13_characters/ginny_weasley/body/tits/default.png"
            #add gw_base xpos gw_xpos ypos gw_ypos #Add the base body
        else:
            $ gw_tits = "01_hp/13_characters/ginny_weasley/body/tits/pressed.png"
            #add gw_base xpos gw_xpos ypos gw_ypos #Add the base body
    
        add gw_tits xpos gw_xpos ypos gw_ypos

        add gw_head xpos gw_xpos ypos gw_ypos

    #add gw_nose xpos gw_xpos ypos gw_ypos
    #add gw_cheeks xpos gw_xpos ypos gw_ypos
        add gw_eyes xpos gw_xpos ypos gw_ypos
        add gw_mouth xpos gw_xpos ypos gw_ypos

    ###BLUSHED
        if gw_blushed:
            add gw_cheeks xpos gw_xpos ypos gw_ypos #Add blush
    
    ###PUSSY
        add gw_pussy xpos gw_xpos ypos gw_ypos #add pussy
        if not gw_shaved:
            add gw_pubic xpos gw_xpos ypos gw_ypos

        if gw_squirting:
            add gw_squirt xpos gw_xpos ypos gw_ypos


        if gw_botharms:
            add gw_arms_both xpos gw_xpos ypos gw_ypos
    else:
        $ gw_torso = "01_hp/13_characters/ginny_weasley/body/kneel/kneel.png"
        add gw_hair_layer xpos gw_xpos ypos gw_ypos
        add gw_torso xpos gw_xpos ypos gw_ypos
        add gw_head xpos gw_xpos ypos gw_ypos

    
        add gw_eyes xpos gw_xpos ypos gw_ypos
        add gw_mouth xpos gw_xpos ypos gw_ypos
        if gw_blushed:
            add gw_cheeks xpos gw_xpos ypos gw_ypos #Add blush
    
    

    #add gw_freckles xpos gw_xpos ypos gw_ypos


    
    
    #add cc_hair_shadow xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ### EMOTIONS
    #add cc_eye xpos cc_xpos ypos cc_ypos #Add the eye outline
    #add cc_pupil xpos cc_xpos ypos cc_ypos #Add the pupil
    #add cc_eyebrow xpos cc_xpos ypos cc_ypos #Add the eyebrow
    #add cc_hair xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ###MOUTH
    #add cc_mouth xpos cc_xpos ypos cc_ypos #Add the mouth
    ###TEARS for fears
    #add cc_tears xpos cc_xpos ypos cc_ypos #Add the tears
    ### CLOTHES 
    

    if gw_wear_bra and not gw_wear_top:
        add gw_bra xpos gw_xpos ypos gw_ypos # Add the bra
    if gw_wear_panties and not gw_wear_skirt:
        add gw_panties xpos gw_xpos ypos gw_ypos # Add the panties
    elif gw_wear_panties and gw_wear_skirt:
        add gw_panties xpos gw_xpos ypos gw_ypos # Add the panties
        add gw_skirt xpos gw_xpos ypos gw_ypos # Add the skirt
    elif not gw_wear_panties and gw_wear_skirt:
        add gw_skirt xpos gw_xpos ypos gw_ypos # Add the skirt
    if gw_wear_top:
        add gw_top xpos gw_xpos ypos gw_ypos # Add the top
    
    if gw_wear_robes:
        add gw_robes xpos gw_xpos ypos gw_ypos

    add gw_hair xpos gw_xpos ypos gw_ypos


    ### CUM 
    if gw_cummed_on:
        add gw_semen xpos gw_xpos ypos gw_ypos


    #if cc_wear_acc:
    #    add cc_acc xpos cc_xpos ypos cc_ypos # Add the accessory
    #if cc_wear_vest:
    #    add cc_vest xpos cc_xpos ypos cc_ypos # Add the vest
    #if cc_wear_stockings:
    #    add cc_stock xpos cc_xpos ypos cc_ypos # Add the stockings
    ### OTHER
    #add cc_l_hand xpos cc_xpos ypos cc_ypos # Add the left hand
    ### ZORDER
    #zorder gw_zorder
    zorder gw_zorder
    
screen cho_chang:
    ### BASE IMAGE
    add cc_arms xpos cc_xpos ypos cc_ypos #Add the arms
    add cc_base xpos cc_xpos ypos cc_ypos #Add the base body
    add cc_hair_shadow xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ### EMOTIONS
    add cc_eye xpos cc_xpos ypos cc_ypos #Add the eye outline
    add cc_pupil xpos cc_xpos ypos cc_ypos #Add the pupil
    add cc_eyebrow xpos cc_xpos ypos cc_ypos #Add the eyebrow
    add cc_hair xpos cc_xpos ypos cc_ypos #Add the hair shadow
    ###MOUTH
    add cc_mouth xpos cc_xpos ypos cc_ypos #Add the mouth

    ###TEARS for fears
    add cc_tears xpos cc_xpos ypos cc_ypos #Add the tears
    ### CLOTHES 
    if cc_wear_bra and not cc_wear_top:
        add cc_bra xpos cc_xpos ypos cc_ypos # Add the bra
    if cc_wear_panties and not cc_wear_skirt:
        add cc_panties xpos cc_xpos ypos cc_ypos # Add the panties
    if cc_wear_skirt:
        add cc_skirt xpos cc_xpos ypos cc_ypos # Add the skirt
    if cc_wear_top:
        add cc_top xpos cc_xpos ypos cc_ypos # Add the top
    if cc_wear_acc:
        add cc_acc xpos cc_xpos ypos cc_ypos # Add the accessory
    if cc_wear_vest:
        add cc_vest xpos cc_xpos ypos cc_ypos # Add the vest
    if cc_wear_stockings:
        add cc_stock xpos cc_xpos ypos cc_ypos # Add the stockings
    ### OTHER
    add cc_l_hand xpos cc_xpos ypos cc_ypos # Add the left hand
    ### ZORDER
    zorder cc_zorder
    #zorder gw_zorder

screen susan_bones:
    ### BASE IMAGE
    add sus_hair xpos sus_xpos ypos sus_ypos #Add hair
    add sus_arm_base xpos sus_xpos ypos sus_ypos #Add the arm base
    add sus_arms xpos sus_xpos ypos sus_ypos #Add the arms that need to be below the body
    add sus_base xpos sus_xpos ypos sus_ypos #Add the base body
    add sus_breast xpos sus_xpos ypos sus_ypos #Add the breast
    add sus_legs xpos sus_xpos ypos sus_ypos #Add the legs
    add sus_arm_2 xpos sus_xpos ypos sus_ypos #Add the arms that need to be above the body
    add sus_left_arm xpos sus_xpos ypos sus_ypos #Add the left arm
    ### EYES AND HAIR SHADOW
    add sus_eye xpos sus_xpos ypos sus_ypos #Add the eye outline
    add sus_pupil xpos sus_xpos ypos sus_ypos #Add the pupil
    add sus_eyebrow xpos sus_xpos ypos sus_ypos #Add the eyebrow
    add sus_hair_shadow xpos sus_xpos ypos sus_ypos #Add the hair shadow
    ### MOUTH
    add sus_mouth xpos sus_xpos ypos sus_ypos #Add the mouth
    ### CLOTHES 
    add sus_skirt xpos sus_xpos ypos sus_ypos # Add the skirt
    add sus_top xpos sus_xpos ypos sus_ypos # Add the top
    add sus_acc xpos sus_xpos ypos sus_ypos # Add the accessory
    add sus_vest xpos sus_xpos ypos sus_ypos # Add the vest
    add sus_stock xpos sus_xpos ypos sus_ypos # Add the stockings
    ### OTHER
    
    ### ZORDER
    zorder sus_zorder

label cho_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None):
    if eye!=None and pupil!=None and eyebrow!=None and mouth!=None:
        $ changeCho(eye, eyebrow, pupil, mouth)
    if text != "":
        $ renpy.say(cho, text)
    return
    
label ginny_main(text="", body=None, mouth=None, eyes=None):
    if body!=None:
        $ changeGinny(body,mouth,eyes)
    if text != "":
        $ renpy.say(ginny, text)
    return

label ginny_change(type="", name=""):
    if type == "top":
        $ gw_top = "01_hp/13_characters/ginny_weasley/clothes/top/"+name+".png"
    elif type == "skirt":
        $ gw_skirt = "01_hp/13_characters/ginny_weasley/clothes/bottom/"+name+".png"
    elif type == "panty":
        $ gw_panties = "01_hp/13_characters/ginny_weasley/clothes/underwear/"+name+".png"
    elif type == "bra":
        $ gw_bra = "01_hp/13_characters/ginny_weasley/clothes/underwear/"+name+".png"
    return
    


init python: ###Method Definition for new characters
    #def changeGinny(  ginny_eye=None,
    #                  ginny_eyebrow=None, 
    #                ginny_pupil=None, 
    #                ginny_mouth=None, 
    #                x_pos=None, 
    #                y_pos=None): # ginny
    def changeGinny(  ginny_body=None,
                      ginny_mouth=None,
                      ginny_eyes=None,
                      x_pos=None, 
                      y_pos=None): # ginny
        ###DEFINE GLOBAL VARIABLES
        global gw_xpos
        global gw_ypos
        global gw_base

        global gw_torso
        global gw_arms_left
        global gw_arms_right
        global gw_arms_both
        global gw_arms_boths
        global gw_legs
        global gw_tits
        global gw_head
        global gw_nose


        global gw_cheeks




        global gw_eyes
        #global gw_pupil

        global gw_mouth
        #global gw_eyebrow
        global gw_pubic
        global gw_squirt
        global gw_pussy
        global gw_hair
        global gw_hair_layer
        global gw_top
        ###CHANGE INTS TO STRING
        #ginny_eye = str(ginny_eye)
        #ginny_eyebrow = str(ginny_eyebrow)
        #ginny_pupil = str(ginny_pupil)
        #ginny_mouth = str(ginny_mouth)
    
        ginny_body = str(ginny_body)
    
        ###HIDE OLD SCREEN
        #renpy.hide_screen("ginny_weasley")
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            gw_xpos = x_pos
        else:
            gw_xpos = gw_xpos
        if y_pos is not None:
            gw_ypos = y_pos
        else:
            gw_ypos = gw_ypos

        ###EMOTION CONTROLish
        
        


        gw_torso = "01_hp/13_characters/ginny_weasley/body/torso/default.png"
        gw_arms_left = "01_hp/13_characters/ginny_weasley/body/arms_left/default.png"
        #gw_arms_right = "01_hp/13_characters/ginny_weasley/body/arms_right/default.png"
        #gw_arms_both = "01_hp/13_characters/ginny_weasley/body/arms_both/fingering2.png"
        gw_legs = "01_hp/13_characters/ginny_weasley/body/legs/default.png"
        gw_tits = "01_hp/13_characters/ginny_weasley/body/tits/default.png"
        gw_head = "01_hp/13_characters/ginny_weasley/body/head/default.png"
        
        gw_nose = "01_hp/13_characters/ginny_weasley/body/nose/default.png"
        gw_cheeks = "01_hp/13_characters/ginny_weasley/body/cheeks/blush.png"
        #gw_eyes = "01_hp/13_characters/ginny_weasley/body/eyes/default.png"

        if ginny_eyes is not None:
            ginny_eyes = str(ginny_eyes)
            if ginny_eyes == "0":
                gw_eyes = "01_hp/13_characters/blank.png"
            else:
                gw_eyes = "01_hp/13_characters/ginny_weasley/body/eyes/"+ginny_eyes+".png"
                #gw_mouth = "01_hp/13_characters/ginny_weasley/body/mouth/lipstick/2.png"


        #gw_pupil = "01_hp/13_characters/ginny_weasley/body/pupil/default.png"
        
        if ginny_mouth is not None:
            ginny_mouth = str(ginny_mouth)
            if ginny_mouth == "0":
                gw_mouth = "01_hp/13_characters/blank.png"
            else:
                gw_mouth = "01_hp/13_characters/ginny_weasley/body/mouth/lipstick/"+ginny_mouth+".png"
                #gw_mouth = "01_hp/13_characters/ginny_weasley/body/mouth/lipstick/2.png"


        #gw_mouth = "01_hp/13_characters/ginny_weasley/body/mouth/lipstick/"+ginny_mouth+".png"
        gw_pubic = "01_hp/13_characters/ginny_weasley/body/pubic/au_naturel.png"
        #gw_squirt = "01_hp/13_characters/ginny_weasley/body/pubic/au_naturel.png"
        gw_pussy = "01_hp/13_characters/ginny_weasley/body/genitalia/default.png"
        
        gw_hair =  "01_hp/13_characters/ginny_weasley/body/hair/default.png"
        gw_hair_layer = "01_hp/13_characters/ginny_weasley/body/layerhair/default.png"
        #gw_face = "01_hp/13_characters/ginny_weasley/face/default.png"
    
        #if ginny_eye is not None:
            #if ginny_eye == "0":
        #        gw_eye = "01_hp/13_characters/blank.png"
            #else:
        #    #    gw_eye = "01_hp/13_characters/ginny_weasley/eye/eye_0"+ginny_eye+".png" #nao tem 

        #if ginny_eyebrow is not None:
        #    if ginny_eyebrow == "0":
        #        cc_eyebrow = "01_hp/13_characters/blank.png"
        #    else:
        #        cc_eyebrow = "01_hp/13_characters/ginny_chang/eye/eyebrow_0"+ginny_eyebrow+".png" 

        #if ginny_pupil is not None:
        #    if ginny_pupil == "0":
        #        cc_pupil = "01_hp/13_characters/blank.png"
        #    else:
        #        cc_pupil = "01_hp/13_characters/ginny_chang/eye/pupil_0"+ginny_pupil+".png" 

        #if ginny_mouth is not None:
        #    if ginny_mouth == "0":
        #        cc_mouth = "01_hp/13_characters/blank.png"
        #    else:
        #        cc_mouth = "01_hp/13_characters/ginny_chang/mouth/mouth_0"+ginny_mouth+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("ginny_weasley")
        renpy.with_statement(Dissolve(0.3))

    def changeCho(  cho_eye=None,
                    cho_eyebrow=None, 
                    cho_pupil=None, 
                    cho_mouth=None, 
                    x_pos=None, 
                    y_pos=None): # Cho
        ###DEFINE GLOBAL VARIABLES
        global cc_xpos
        global cc_ypos
        global cc_base
        global cc_cheeks
        global cc_eye
        global cc_pupil
        #global cc_eyebrow
        global cc_mouth
        global cc_eyebrow
        ###CHANGE INTS TO STRING
        cho_eye = str(cho_eye)
        cho_eyebrow = str(cho_eyebrow)
        cho_pupil = str(cho_pupil)
        cho_mouth = str(cho_mouth)
        ###HIDE OLD SCREEN
        #renpy.hide_screen("cho_chang")
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            cc_xpos = x_pos
        else:
            cc_xpos = cc_xpos
        if y_pos is not None:
            cc_ypos = cc_ypos
        else:
            cc_ypos = cc_ypos

        ###EMOTION CONTROL
        if cho_eye is not None:
            if cho_eye == "0":
                cc_eye = "01_hp/13_characters/blank.png"
            else:
                cc_eye = "01_hp/13_characters/cho_chang/eye/eye_0"+cho_eye+".png" 

        if cho_eyebrow is not None:
            if cho_eyebrow == "0":
                cc_eyebrow = "01_hp/13_characters/blank.png"
            else:
                cc_eyebrow = "01_hp/13_characters/cho_chang/eye/eyebrow_0"+cho_eyebrow+".png" 

        if cho_pupil is not None:
            if cho_pupil == "0":
                cc_pupil = "01_hp/13_characters/blank.png"
            else:
                cc_pupil = "01_hp/13_characters/cho_chang/eye/pupil_0"+cho_pupil+".png" 

        if cho_mouth is not None:
            if cho_mouth == "0":
                cc_mouth = "01_hp/13_characters/blank.png"
            else:
                cc_mouth = "01_hp/13_characters/cho_chang/mouth/mouth_0"+cho_mouth+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cho_chang")
        renpy.with_statement(Dissolve(0.3))

        
    def changeSusan(    susan_eye=None, 
                        susan_eyebrow=None, 
                        susan_pupil=None, 
                        susan_mouth=None, 
                        susan_arms=None, 
                        susan_left_arm=None,
                        x_pos=None, 
                        y_pos=None): # Susan
        ###DEFINE GLOBAL VARIABLES
        global sus_xpos
        global sus_ypos
        global sus_base
        global sus_breast
        global sus_cheeks
        global sus_eye
        global sus_pupil
        global sus_arms
        global sus_arm_2
        global sus_arm_base
        global sus_left_arm
        global sus_mouth
        global sus_eyebrow
        ###HIDE OLD SCREEN
        renpy.hide_screen("susan_bones")
        ###CHANGE INTS TO STRING
        susan_eye = str(susan_eye)
        susan_eyebrow = str(susan_eyebrow)
        susan_pupil = str(susan_pupil)
        susan_mouth = str(susan_mouth)

        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            sus_xpos = x_pos
        else:
            sus_xpos = sus_xpos
        if y_pos is not None:
            sus_ypos = sus_ypos
        else:
            sus_ypos = sus_ypos
        ###EMOTION CONTROL

        if susan_eye is not None:
            if susan_eye == "0":
                sus_eye = "01_hp/13_characters/blank.png" 
            else:
                sus_eye = "01_hp/13_characters/susan_bones/eye/eye_0"+susan_eye+".png" 


        if susan_eyebrow is not None:
            if susan_eyebrow == "0":
                sus_eyebrow = "01_hp/13_characters/blank.png" 
            else:
                sus_eyebrow = "01_hp/13_characters/susan_bones/eye/eyebrow_0"+susan_eyebrow+".png" 


        if susan_pupil is not None:
            if susan_pupil == "0":
                sus_pupil = "01_hp/13_characters/blank.png" 
            else:
                sus_pupil = "01_hp/13_characters/susan_bones/eye/pupil_0"+susan_pupil+".png" 


        if susan_mouth is not None:
            if susan_mouth == "0":
                sus_mouth = "01_hp/13_characters/blank.png" 
            else:
                sus_mouth = "01_hp/13_characters/susan_bones/mouth/mouth_0"+susan_mouth+".png" 

        if susan_arms is not None:
            sus_arms = "01_hp/13_characters/susan_bones/base/blank.png"
            sus_arm_2 = "01_hp/13_characters/susan_bones/base/blank.png" 
            sus_arm_base = "01_hp/13_characters/susan_bones/base/blank.png" 
            if susan_arms == 1:
                sus_arms = "01_hp/13_characters/susan_bones/base/arm_01.png"
                sus_arm_base = "01_hp/13_characters/susan_bones/base/arm_base.png" 
            elif susan_arms == 2:
                sus_arm_2 = "01_hp/13_characters/susan_bones/base/arm_02.png"
            elif susan_arms == 3:
                sus_arm_2 = "01_hp/13_characters/susan_bones/base/arm_03.png"
                sus_arm_base = "01_hp/13_characters/susan_bones/base/arm_base.png" 
            elif susan_arms == 4:
                sus_arm_2 = "01_hp/13_characters/susan_bones/base/arm_04.png"
            elif susan_arms == 5:
                sus_arm_2 = "01_hp/13_characters/susan_bones/base/arm_05.png" 
            else:
                sus_arms = sus_arms

        if susan_left_arm is not None:
            if susan_left_arm == 1:
                sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_01.png"
            elif susan_left_arm == 2:
                sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_02.png"
            elif susan_left_arm == 3:
                sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_03.png"
            elif susan_left_arm == 4:
                sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_04.png"
            elif susan_left_arm == 5:
                sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_05.png"
            else:
                sus_left_arm = sus_left_arm



        ###Update her arm pose

            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("susan_bones")
        renpy.with_statement(Dissolve(0.3))



    def sus_outfit(     outfit=None,   #WIP
                            outfit_var_1=None, 
                            outfit_var_2=None, 
                            outfit_var_3=None):

        global sus_skirt 
        global sus_top 
        global sus_acc
        global sus_vest 
        global sus_stock 
        global sus_breast

        ###HIDE OLD SCREEN
        renpy.hide_screen("susan_bones")

        if outfit == "naked":
            sus_vest = "01_hp/13_characters/blank.png"
            sus_top = "01_hp/13_characters/blank.png"
            sus_acc = "01_hp/13_characters/blank.png"
            sus_skirt = "01_hp/13_characters/blank.png"
            sus_stock = "01_hp/13_characters/blank.png"
            sus_breast = "01_hp/13_characters/susan_bones/base/breasts_01.png" 
        elif outfit == "uniform":
            sus_vest = "01_hp/13_characters/susan_bones/clothes/uniform/vest.png" 
            sus_top = "01_hp/13_characters/susan_bones/clothes/uniform/top.png" 
            sus_acc = "01_hp/13_characters/susan_bones/clothes/uniform/tie.png" 
            sus_skirt = "01_hp/13_characters/susan_bones/clothes/uniform/skirt.png" 
            sus_stock = "01_hp/13_characters/susan_bones/clothes/uniform/stockings.png" 
            sus_breast = "01_hp/13_characters/susan_bones/base/breasts_02.png" 
        elif outfit == "dress":
            sus_vest = "01_hp/13_characters/blank.png"
            sus_top = "01_hp/13_characters/susan_bones/clothes/heart_dress/Dress.png" 
            sus_skirt = "01_hp/13_characters/blank.png"
            sus_acc = "01_hp/13_characters/blank.png"
            sus_skirt = "01_hp/13_characters/blank.png"
            sus_stock = "01_hp/13_characters/blank.png"
            sus_breast = "01_hp/13_characters/susan_bones/base/breasts_01.png" 


        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("susan_bones")
        renpy.with_statement(Dissolve(0.3))



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        