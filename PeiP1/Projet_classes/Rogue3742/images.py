import tkinter as tk
from tkinter import PhotoImage
from typing import Union

def get_dictionaries() -> tuple[dict[str, Union[PhotoImage,list[PhotoImage]]], dict[str, list[PhotoImage]], dict[str, PhotoImage], dict[str, PhotoImage], dict[str, PhotoImage], dict[str, PhotoImage], dict[str, PhotoImage], dict[str, PhotoImage], dict[str, list[PhotoImage]], dict[str, PhotoImage], dict[str, PhotoImage]]:
    genPATH = __file__
    nomprogramme = __file__.split("/")[-1]
    imgPATH = genPATH[0: -len(nomprogramme)] + "images/"
    hero_fi = tk.PhotoImage(file=imgPATH + "hero_face_i.png").zoom(2)
    hero_ri = tk.PhotoImage(file=imgPATH + "hero_right_i.png").zoom(2)
    hero_bi = tk.PhotoImage(file=imgPATH + "hero_back_i.png").zoom(2)
    hero_li = tk.PhotoImage(file=imgPATH + "hero_left_i.png").zoom(2)
    hero_fw1 = tk.PhotoImage(file=imgPATH + "hero_face_w1.png").zoom(2)
    hero_rw1 = tk.PhotoImage(file=imgPATH + "hero_right_w1.png").zoom(2)
    hero_bw1 = tk.PhotoImage(file=imgPATH + "hero_back_w1.png").zoom(2)
    hero_lw1 = tk.PhotoImage(file=imgPATH + "hero_left_w1.png").zoom(2)
    hero_fw2 = tk.PhotoImage(file=imgPATH + "hero_face_w2.png").zoom(2)
    hero_rw2 = tk.PhotoImage(file=imgPATH + "hero_right_w2.png").zoom(2)
    hero_bw2 = tk.PhotoImage(file=imgPATH + "hero_back_w2.png").zoom(2)
    hero_lw2 = tk.PhotoImage(file=imgPATH + "hero_left_w2.png").zoom(2)
    hero_tf = tk.PhotoImage(file=imgPATH + "hero_tombe_face.png").zoom(2)
    hero_tr = tk.PhotoImage(file=imgPATH + "hero_tombe_droite.png").zoom(2)
    hero_tb = tk.PhotoImage(file=imgPATH + "hero_tombe_dos.png").zoom(2)
    hero_tl = tk.PhotoImage(file=imgPATH + "hero_tombe_gauche.png").zoom(2)

    # elements pour afficher les points de magie
    magic_img = tk.PhotoImage(file=imgPATH + "magic.png")

    # images hero/equipement Arou
    hero_fb = tk.PhotoImage(file=imgPATH + "herofoulard.png").zoom(2)
    hero_cb = tk.PhotoImage(file=imgPATH + "herobadge.png").zoom(2)
    hero_p1 = tk.PhotoImage(file=imgPATH + "heroplaid1.png").zoom(2)
    hero_p2 = tk.PhotoImage(file=imgPATH + "heroplaid2.png").zoom(2)
    hero_p3 = tk.PhotoImage(file=imgPATH + "heroplaid3.png").zoom(2)
    hero_fp1 = tk.PhotoImage(file=imgPATH + "herofoulardplaid1.png").zoom(2)
    hero_fp2 = tk.PhotoImage(file=imgPATH + "herofoulardplaid2.png").zoom(2)
    hero_fp3 = tk.PhotoImage(file=imgPATH + "herofoulardplaid3.png").zoom(2)
    hero_cp1 = tk.PhotoImage(file=imgPATH + "herobagdeplaid1.png").zoom(2)
    hero_cp2 = tk.PhotoImage(file=imgPATH + "herobagdeplaid2.png").zoom(2)
    hero_cp3 = tk.PhotoImage(file=imgPATH + "herobagdeplaid3.png").zoom(2)

    sol_img1 = tk.PhotoImage(file=imgPATH + "sol_1.png").zoom(2)
    sol_img2 = tk.PhotoImage(file=imgPATH + "sol_2.png").zoom(2)
    sol_img3 = tk.PhotoImage(file=imgPATH + "sol_3.png").zoom(2)
    sol_img4 = tk.PhotoImage(file=imgPATH + "sol_4.png").zoom(2)
    wetsol_img1 = tk.PhotoImage(file=imgPATH + "sol-mouille1.png").zoom(2)
    wetsol_img2 = tk.PhotoImage(file=imgPATH + "sol-mouille2.png").zoom(2)
    wetsol_img3 = tk.PhotoImage(file=imgPATH + "sol-mouille3.png").zoom(2)
    wetsol_img4 = tk.PhotoImage(file=imgPATH + "sol-mouille4.png").zoom(2)
    wall_default = tk.PhotoImage(file=imgPATH + "wall.png").zoom(2)
    wall_img1 = tk.PhotoImage(file=imgPATH + "wall1.png").zoom(2)
    wall_img2 = tk.PhotoImage(file=imgPATH + "wall2.png").zoom(2)
    wall_img3 = tk.PhotoImage(file=imgPATH + "wall3.png").zoom(2)
    wall_img4 = tk.PhotoImage(file=imgPATH + "wall4.png").zoom(2)
    pot_img1 = tk.PhotoImage(file=imgPATH + "fiole_1.png").zoom(2)
    pot_img3 = tk.PhotoImage(file=imgPATH + "fiole_3.png").zoom(2)
    bequille_img = tk.PhotoImage(file=imgPATH + "bequille.png").zoom(2)
    chew_img = tk.PhotoImage(file=imgPATH + "chewing-gum.png").zoom(2)
    gum_img = tk.PhotoImage(file=imgPATH + "gum.png").zoom(2)
    sucette1_img = tk.PhotoImage(file=imgPATH + "sucette_1.png")
    sucette2_img = tk.PhotoImage(file=imgPATH + "sucette_2.png")
    sucette3_img = tk.PhotoImage(file=imgPATH + "sucette_3.png")
    cookie_img = tk.PhotoImage(file=imgPATH + "cookie.png")
    happypills_img = tk.PhotoImage(file=imgPATH + "happy_pills.png")
    foulard_img = tk.PhotoImage(file=imgPATH + "foulard.png")
    coffre_img = tk.PhotoImage(file=imgPATH + "coffre.png")
    plaid3_img = tk.PhotoImage(file=imgPATH + "plaid3.png").zoom(2)

    boul_img = tk.PhotoImage(file=imgPATH + "boulimie.png").zoom(2)
    tireur_img = tk.PhotoImage(file=imgPATH + "archer.png").zoom(2)
    sad_img = tk.PhotoImage(file=imgPATH + "tristesse.png").zoom(2)
    fear_img = tk.PhotoImage(file=imgPATH + "fear.png").zoom(2)
    colere_img = tk.PhotoImage(file=imgPATH + "colere.png").zoom(2)
    ted_img = tk.PhotoImage(file=imgPATH + "ourson_1.png").zoom(2)
    ghost_img = tk.PhotoImage(file=imgPATH + "ghost.png").zoom(2)
    sad_img = tk.PhotoImage(file=imgPATH + "tristesse_1.png").zoom(2)
    araig = tk.PhotoImage(file=imgPATH + "araignee.png").zoom(2)
    or1_img = tk.PhotoImage(file=imgPATH + "or1.png").zoom(2)
    bourse = tk.PhotoImage(file=imgPATH + "or1.png")
    or2_img = tk.PhotoImage(file=imgPATH + "or2.png").zoom(2)
    or5_img = tk.PhotoImage(file=imgPATH + "or5.png").zoom(2)
    or10_img = tk.PhotoImage(file=imgPATH + "or10.png").zoom(2)
    marchand_f = tk.PhotoImage(file=imgPATH + "marchand_de_face.png").zoom(2)
    marchand_f = tk.PhotoImage(file=imgPATH + "marchand_de_face2.png").zoom(2)
    marchand_d = tk.PhotoImage(file=imgPATH + "marchand_vers_droite.png").zoom(2)
    marchand_g = tk.PhotoImage(file=imgPATH + "marchand_vers_gauche.png").zoom(2)
    marchand_sf = tk.PhotoImage(file=imgPATH + "marchand_sucette_de_face.png").zoom(2)
    bedup = tk.PhotoImage(file=imgPATH + "lit_vert_haut_final.png").zoom(2)
    beddown = tk.PhotoImage(file=imgPATH + "lit_vert_bas_final.png").zoom(2)
    wheelchair = tk.PhotoImage(file=imgPATH + "fauteuil.png").zoom(2)
    flowerpot = tk.PhotoImage(file=imgPATH + "arbuste.png").zoom(2)
    hole = tk.PhotoImage(file=imgPATH + "trou.png").zoom(2)
    docteurM_img = tk.PhotoImage(file=imgPATH + "medecin1.png").zoom(2)
    docteurF_img = tk.PhotoImage(file=imgPATH + "medecin2.png").zoom(2)
    infirmiere1_img = tk.PhotoImage(file=imgPATH + "infirmiere1.png").zoom(2)

    badgemedecin_img = tk.PhotoImage(file=imgPATH + "badgemedecin.png")

    img_stonelance = tk.PhotoImage(file=imgPATH + "lancepierre.png").zoom(2)

    esc_up = tk.PhotoImage(file=imgPATH + "escalier_up.png").zoom(2)
    esc_down = tk.PhotoImage(file=imgPATH + "escalier_down.png").zoom(2)
    vide = tk.PhotoImage(file=imgPATH + "empty.png").zoom(2)
    hotbar = tk.PhotoImage(file=imgPATH + "hotbar.png").zoom(2)
    faim100 = tk.PhotoImage(file=imgPATH + "faim100.png").zoom(2)
    faim75 = tk.PhotoImage(file=imgPATH + "faim75.png").zoom(2)
    faim50 = tk.PhotoImage(file=imgPATH + "faim50.png").zoom(2)
    faim25 = tk.PhotoImage(file=imgPATH + "faim25.png").zoom(2)
    faim0 = tk.PhotoImage(file=imgPATH + "faim0.png").zoom(2)
    rede = tk.PhotoImage(file=imgPATH + "red.png")
    dred = tk.PhotoImage(file=imgPATH + "darkred.png")
    gree = tk.PhotoImage(file=imgPATH + "green.png")
    dgre = tk.PhotoImage(file=imgPATH + "darkgreen.png")
    blue = tk.PhotoImage(file=imgPATH + "blue.png")
    dblu = tk.PhotoImage(file=imgPATH + "darkblue.png")
    yell = tk.PhotoImage(file=imgPATH + "yellow.png")
    dyel = tk.PhotoImage(file=imgPATH + "darkyellow.png")
    ligt = tk.PhotoImage(file=imgPATH + "lightblue.png")
    dlig = tk.PhotoImage(file=imgPATH + "darklightblue.png")
    oran = tk.PhotoImage(file=imgPATH + "orange.png")
    dora = tk.PhotoImage(file=imgPATH + "darkorange.png")
    black = tk.PhotoImage(file=imgPATH + "black.png")
    health = tk.PhotoImage(file=imgPATH + "health.png")
    cle_img = tk.PhotoImage(file=imgPATH + "cle.png")
    multi_img = tk.PhotoImage(file=imgPATH + "multipass.png")
    # equipement(objets sans zoom pour quand on a besoin) Arou
    equip_bequille = tk.PhotoImage(file=imgPATH + "bequille.png")

    herobox0 = tk.PhotoImage(file=imgPATH + "box0.png").zoom(3)
    herobox10 = tk.PhotoImage(file=imgPATH + "box10.png").zoom(3)
    herobox20 = tk.PhotoImage(file=imgPATH + "box20.png").zoom(3)
    herobox30 = tk.PhotoImage(file=imgPATH + "box30.png").zoom(3)
    herobox40 = tk.PhotoImage(file=imgPATH + "box40.png").zoom(3)
    herobox50 = tk.PhotoImage(file=imgPATH + "box50.png").zoom(3)
    herobox60 = tk.PhotoImage(file=imgPATH + "box60.png").zoom(3)
    herobox70 = tk.PhotoImage(file=imgPATH + "box70.png").zoom(3)
    herobox80 = tk.PhotoImage(file=imgPATH + "box80.png").zoom(3)
    herobox90 = tk.PhotoImage(file=imgPATH + "box90.png").zoom(3)

    dialoguebox = tk.PhotoImage(file=imgPATH + "dialogue.png")

    img_psn1 = tk.PhotoImage(file=imgPATH + "poison1.png").zoom(2)
    img_psn2 = tk.PhotoImage(file=imgPATH + "poison2.png").zoom(2)
    img_psn3 = tk.PhotoImage(file=imgPATH + "poison3.png").zoom(2)
    img_feu1 = tk.PhotoImage(file=imgPATH + "feu1.png").zoom(2)
    img_feu2 = tk.PhotoImage(file=imgPATH + "feu2.png").zoom(2)
    img_feu3 = tk.PhotoImage(file=imgPATH + "feu3.png").zoom(2)
    img_ice1 = tk.PhotoImage(file=imgPATH + "ice1.png").zoom(2)
    img_ice2 = tk.PhotoImage(file=imgPATH + "ice2.png").zoom(2)
    img_ice3 = tk.PhotoImage(file=imgPATH + "ice3.png").zoom(2)
    img_wnd1 = tk.PhotoImage(file=imgPATH + "wind1.png").zoom(2)
    img_wnd2 = tk.PhotoImage(file=imgPATH + "wind2.png").zoom(2)
    img_wnd3 = tk.PhotoImage(file=imgPATH + "wind3.png").zoom(2)
    joie9 = tk.PhotoImage(file=imgPATH + "joie9.png")
    joie8 = tk.PhotoImage(file=imgPATH + "joie8.png")
    joie7 = tk.PhotoImage(file=imgPATH + "joie7.png")
    joie6 = tk.PhotoImage(file=imgPATH + "joie6.png")
    joie5 = tk.PhotoImage(file=imgPATH + "joie5.png")
    joie4 = tk.PhotoImage(file=imgPATH + "joie4.png")
    joie3 = tk.PhotoImage(file=imgPATH + "joie3.png")
    joie2 = tk.PhotoImage(file=imgPATH + "joie2.png")
    joie1 = tk.PhotoImage(file=imgPATH + "joie1.png")
    sad9 = tk.PhotoImage(file=imgPATH + "sad9.png")
    sad8 = tk.PhotoImage(file=imgPATH + "sad8.png")
    sad7 = tk.PhotoImage(file=imgPATH + "sad7.png")
    sad6 = tk.PhotoImage(file=imgPATH + "sad6.png")
    sad5 = tk.PhotoImage(file=imgPATH + "sad5.png")
    sad4 = tk.PhotoImage(file=imgPATH + "sad4.png")
    sad3 = tk.PhotoImage(file=imgPATH + "sad3.png")
    sad2 = tk.PhotoImage(file=imgPATH + "sad2.png")
    sad1 = tk.PhotoImage(file=imgPATH + "sad1.png")
    peur9 = tk.PhotoImage(file=imgPATH + "peur9.png")
    peur8 = tk.PhotoImage(file=imgPATH + "peur8.png")
    peur7 = tk.PhotoImage(file=imgPATH + "peur7.png")
    peur6 = tk.PhotoImage(file=imgPATH + "peur6.png")
    peur5 = tk.PhotoImage(file=imgPATH + "peur5.png")
    peur4 = tk.PhotoImage(file=imgPATH + "peur4.png")
    peur3 = tk.PhotoImage(file=imgPATH + "peur3.png")
    peur2 = tk.PhotoImage(file=imgPATH + "peur2.png")
    peur1 = tk.PhotoImage(file=imgPATH + "peur1.png")
    angry9 = tk.PhotoImage(file=imgPATH + "angry9.png")
    angry8 = tk.PhotoImage(file=imgPATH + "angry8.png")
    angry7 = tk.PhotoImage(file=imgPATH + "angry7.png")
    angry6 = tk.PhotoImage(file=imgPATH + "angry6.png")
    angry5 = tk.PhotoImage(file=imgPATH + "angry5.png")
    angry4 = tk.PhotoImage(file=imgPATH + "angry4.png")
    angry3 = tk.PhotoImage(file=imgPATH + "angry3.png")
    angry2 = tk.PhotoImage(file=imgPATH + "angry2.png")
    angry1 = tk.PhotoImage(file=imgPATH + "angry1.png")
    equipBar = tk.PhotoImage(file=imgPATH + "equipBar.png")
    gameover_img = tk.PhotoImage(file=imgPATH + "gameover.png")
    marchandepage_img = tk.PhotoImage(file=imgPATH + "marchandepage.png")

    dicimages = {
        "C": coffre_img,
        "cle": cle_img,
        "mul": multi_img,
        "G": sad_img,
        "W": fear_img,
        "O": colere_img,
        "B": ted_img,
        "D": boul_img,
        "Ar": araig,
        "magic": magic_img,
        "showcase": hero_fi,
        ".": sol_img1,
        ",": sol_img2,
        "`": sol_img3,
        "´": sol_img4,
        ".m": wetsol_img1,
        ",m": wetsol_img2,
        "`m": wetsol_img3,
        "´m": wetsol_img4,
        "|": wall_default,
        "|1": wall_img1,
        "|2": wall_img2,
        "|3": wall_img3,
        "|4": wall_img4,
        "@": [hero_fi, hero_bi, hero_li, hero_ri],
        "@*": [hero_tf, hero_tb, hero_tl, hero_tr],
        "!": pot_img3,
        "fv": ghost_img,
        "s": bequille_img,
        "a": img_stonelance,
        "c": pot_img3,
        "b": or1_img,
        "j": or2_img,
        "p": or5_img,
        "P": or10_img,
        "M": marchand_f,
        "inventory": hotbar,
        "faim100": faim100,
        "faim75": faim75,
        "faim50": faim50,
        "faim25": faim25,
        "faim0": faim0,
        "empty": vide,
        "health": health,
        "dialogue": dialoguebox,
        ">": esc_up,
        "<": esc_down,
        "u": chew_img,
        "g": gum_img,
        "Be1": bedup,
        "Be2": beddown,
        "Fa": wheelchair,
        "Po": flowerpot,
        "Tr": hole,
        "s1": sucette1_img,
        "s2": sucette2_img,
        "s3": sucette3_img,
        "herobox0": herobox0,
        "herobox10": herobox10,
        "herobox20": herobox20,
        "herobox30": herobox30,
        "herobox40": herobox40,
        "herobox50": herobox50,
        "herobox60": herobox60,
        "herobox70": herobox70,
        "herobox80": herobox80,
        "herobox90": herobox90,
        "cc": cookie_img,
        "HP": happypills_img,
        "pl": plaid3_img,
        "T": tireur_img,
        "foulard": foulard_img,
        "docM": docteurM_img,
        "docF": docteurF_img,
        "inf": infirmiere1_img,
    }
    dicanim = {
        "@": [
            hero_fw1,
            hero_bw1,
            hero_lw1,
            hero_rw1,
            hero_fw2,
            hero_bw2,
            hero_lw2,
            hero_rw2,
        ],
        "@*": [
            hero_tf,
            hero_tf,
            hero_tf,
            hero_tr,
            hero_tr,
            hero_tr,
            hero_tb,
            hero_tb,
            hero_tb,
            hero_tl,
            hero_tl,
            hero_tl,
        ],
    }
    dicappear = {
        "hero_foulard": hero_fb,
        "hero_badge": hero_cb,
        "hero_plaid": hero_p1,
        "hero_foulardplaid": hero_fp1,
        "hero_badgeplaid": hero_cp1,
    }
    dicequipement = {
        "s": equip_bequille,
        "Cd": badgemedecin_img,
        "foulard": foulard_img,
        "pl": plaid3_img,
    }
    dicinventory = {
        "equipBar": equipBar,
        "@": hero_fi,
        "!": pot_img3,
        "a": img_stonelance,
        "s": bequille_img,
        "c": pot_img3,
        "b": or1_img,
        "j": or2_img,
        "p": or5_img,
        "P": or10_img,
        "g": gum_img,
        "s1": sucette1_img.zoom(2),
        "s2": sucette2_img.zoom(2),
        "s3": sucette3_img.zoom(2),
        "Cd": badgemedecin_img.zoom(2),
        "cc": cookie_img.zoom(2),
        "bourse": bourse,
        "HP": happypills_img.zoom(2),
        "pl": plaid3_img,
        "cle": cle_img,
    }
    dicinventoryM = {
        "!": pot_img3.zoom(2),
        "a": img_stonelance.zoom(2),
        "s": bequille_img.zoom(2),
        "g": gum_img.zoom(2),
        "s1": sucette1_img.zoom(4),
        "s2": sucette2_img.zoom(4),
        "s3": sucette3_img.zoom(4),
        "Cd": badgemedecin_img.zoom(4),
        "cc": cookie_img.zoom(4),
        "bourse": bourse,
        "HP": happypills_img.zoom(4),
    }
    dicseen = {
        "dy": dyel,
        "do": dora,
        "dl": dlig,
        "db": dblu,
        "dg": dgre,
        "dr": dred,
    }
    dicviewable = {
        "ye": yell,
        "or": oran,
        "li": ligt,
        "bl": blue,
        "gr": gree,
        "re": rede,
    }
    dicatk = {
        "psn": [img_psn1, img_psn2, img_psn3],
        "feu": [img_feu1, img_feu2, img_feu3],
        "ice": [img_ice1, img_ice2, img_ice3],
        "wnd": [img_wnd1, img_wnd2, img_wnd3],
    }
    dicemotion = {
        "joy1": joie1,
        "joy2": joie2,
        "joy3": joie3,
        "joy4": joie4,
        "joy5": joie5,
        "joy6": joie6,
        "joy7": joie7,
        "joy8": joie8,
        "joy9": joie9,
        "sad1": sad1,
        "sad2": sad2,
        "sad3": sad3,
        "sad4": sad4,
        "sad5": sad5,
        "sad6": sad6,
        "sad7": sad7,
        "sad8": sad8,
        "sad9": sad9,
        "peur1": peur1,
        "peur2": peur2,
        "peur3": peur3,
        "peur4": peur4,
        "peur5": peur5,
        "peur6": peur6,
        "peur7": peur7,
        "peur8": peur8,
        "peur9": peur9,
        "angry1": angry1,
        "angry2": angry2,
        "angry3": angry3,
        "angry4": angry4,
        "angry5": angry5,
        "angry6": angry6,
        "angry7": angry7,
        "angry8": angry8,
        "angry9": angry9,
    }
    dicother = {
        "gameover": gameover_img,
        "marchandepage": marchandepage_img,
        "black": black}
    return dicimages,dicanim,dicappear,dicequipement,dicinventory,dicinventoryM,dicseen,dicviewable,dicatk,dicemotion,dicother


#  /bin/python3 -m pip install -U autopep8