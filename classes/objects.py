import pyxel

splits_vxy = [(-2.3, -2.9), (-1.9, -2.4), (-1.5, -3.4), (-1.4, -3.2), (-0.1, -3.9), (-0.5, -3.8), (0.9, -3.7), (1.3, -3.3), (1.0, -3.6), (1.9, -2.4), (2.9, -2.8), (0,-4),(-2.8,-2),(2.8,-2),(-3,-1.8),(3,-1.8),(-1.1, -3.6), (1.1, -3.6),]

T = (0,144,10,15,0)
Y = (12,144,12,15,0)
P = (25,144,10,15,0)
E = (38,144,11,15,0)
M = (51,144,12,15,0)
O = (64,144,10,15,0)
H = (73,144,12,15,0)
N = (86,144,11,15,0)

LIFE = (1,152,144,16,16,0)

CODE_UP = (1,112,147,5,5,0)
CODE_DOWN = (1,120,147,5,5,0)
CODE_LEFT = (1,112,155,5,5,0)
CODE_RIGHT = (1,120,155,5,5,0)
CODE_A = (1,128,147,5,5,0)
CODE_B = (1,136,147,5,5,0)
CODE_Y = (1,128,155,5,5,0)
CODE_X = (1,136,155,5,5,0)

CODE = {pyxel.KEY_UP:CODE_UP,
        pyxel.KEY_DOWN:CODE_DOWN,
        pyxel.KEY_LEFT:CODE_LEFT,
        pyxel.KEY_RIGHT:CODE_RIGHT,
        pyxel.KEY_A:CODE_A,
        pyxel.KEY_B:CODE_B,
        pyxel.KEY_X:CODE_X,
        pyxel.KEY_Y:CODE_Y}

stars = [[2, 95], [8, 16], [13, 86], [18, 225], [20, 249], [23, 223], [24, 140], [28, 49], [35, 217], [36, 185], [46, 5], [47, 112], [49, 200], [56, 48], [57, 169], [62, 106], [70, 22], [69, 151], [72, 128], [80, 166], [81, 122], [91, 89], [92, 150], [93, 199], [101, 106], [100, 76], [104, 66], [109, 37], [117, 44], [119, 229], [124, 6], [124, 203], [133, 174], [133, 190], [141, 16], [147, 94], [148, 81], [153, 157], [153, 51], [162, 255], [163, 170], [168, 225], [174, 171], [174, 87], [178, 205], [181, 128], [191, 14], [195, 138], [195, 247], [202, 9], [202, 196], [208, 146], [214, 126], [219, 138], [223, 79], [222, 180], [230, 117], [235, 175], [235, 251], [240, 20], [241, 215], [244, 81], [253, 172], [252, 36]]

SIMPLE       = 0
RANDOM       = 1 
MIRROR       = 2
SPLITS       = 3
MASKED       = 4
BONUS        = 5
METEOR       = 6

small_target = (1,144,208,8,8,0)
target = (1,128,208,16,16,0)

hit_rock_1 = [(15,10),(13,14),(12,9),(6,15),(5,8),(1,2)]
hit_rock_2 = [(15,9), (13,8), (12,4),(6,10),(5,2),(1,4)]

hit_anim = [[hit_rock_1,hit_rock_2], (0,0,1,1,2,2,1,1)]

stone_list = [(1,80,208,8,8,0),(1,88,208,8,8,0),(1,80,216,8,8,0),(1,88,216,8,8,0) ]
rock_list  = [ (1,0,208,16,16,0), (1,16,208,16,16,0),(1,32,208,16,16,0), (1,48,208,16,16,0), (1,64,208,16,16,0)]
big_rock_list = [(1,0,224,32,32,7),(1,32,224,32,32,7),(1,64,224,32,32,7),(1,96,224,32,32,7),(1,128,224,32,32,7),(1,160,224,32,32,7)]
huge_rock_list = [(1,64,96,48,48,7),(1,112,96,48,48,7),(1,160,96,48,48,7)]
meteor_list = [(1,192,216,64,48,7)]

stone_expl_anim=[[(1,96,208,8,8,0),(1,104,208,8,8,0),(1,96,216,8,8,0),(1,104,216,8,8,0),
                  (1,112,208,8,8,0),(1,112,216,8,8,0),(1,120,208,8,8,0),(1,120,216,8,8,0)],
                 [0,1,2,2,3,3,4,4,5,5,6,7]]

tiny_expl_anim=[[(1,0,192,16,16,0),(1,16,192,16,16,0), (1,32,192,16,16,0),(1,48,192,16,16,0),
                 (1,64,192,16,16,0),(1,96,192,16,16,0),(1,112,192,16,16,0)],
                [0,1,1,2,2,3,3,4,4,5,5,6,6]]

expl_anim=[[(1,0,160,32,32,0),(1,32,160,32,32,0),(1,64,160,32,32,0),(1,96,160,32,32,0),
            (1,128,160,32,32,0),(1,160,160,32,32,0),(1,192,160,32,32,0)],
           [0,1,1,2,2,3,3,4,4,5,5,6]]

normal = (0,0.5,0,0,.5)
slow   = (0,.25,0,0,0.25)
fast   = (0,0.75,0,0,.75)

lvl1 = {"poem":["""i wake and moonbeams play around my bed
glittering like hoar frost to my wandering eyes
up towards the glorious moon i raised my head
then lay me down and thoughts of home arise

li bai
"""],
        "events":[[(40, SIMPLE, 53,  slow ),
                   (20, SIMPLE, 203, slow ),
                   (20, SIMPLE, 153, normal),
                   (100, SIMPLE, 103, slow ),
                   (50, SIMPLE, 203, slow ),
                   (40, SIMPLE, 153, normal),
                   (80, SIMPLE, 3,   slow ),
                   (80, SIMPLE, 53,  normal),
                   (100,SIMPLE, 103, normal),
                   (40, SIMPLE, 203, slow ),
                   (80, SIMPLE, 3,   slow ),
                   (40, SIMPLE, 53,  slow ),
                   (100,SIMPLE, 103, normal),
                   (40, SIMPLE, 203, normal ),
                   (80, SIMPLE, 3,   slow ),
                   (40, SIMPLE, 53,  normal),
                   (100,SIMPLE, 103, normal),
                   (40, SIMPLE, 203, normal ),
                   (80, SIMPLE, 3,   slow ),
                   (40, SIMPLE, 53,  normal),
                   (80, SIMPLE, 103, fast ),
                   (100,SIMPLE, 153, normal),
                   (40, SIMPLE, 203, normal ),
                   (80, SIMPLE, 3,   slow ),
                   (40, SIMPLE, 53,  normal),
                   (80, SIMPLE, 103, fast ),
                   (100,SIMPLE, 153, normal),
                   (40, SIMPLE, 203, normal),
                   (80, SIMPLE, 3,   slow),
                   (40, SIMPLE, 53,  normal),
                   (80, SIMPLE, 103, fast ),
                   (40, SIMPLE, 203, normal ),
                   (80, SIMPLE, 3,   slow ),
                   (40, SIMPLE, 53,  normal),
                   (400,SPLITS, 103, normal),
                   (40, SPLITS, 153, normal) ]]
}


lvl2 = {"poem":["""the moon grown full now over the sea
brightening the whole of heaven
brings to separated hearts
the long thoughtfulness of night""","""it is no darker though i blow out my candle
it is no warmer though i put on my coat
so i leave my message with the moon
and turn to my bed hoping for dreams

zhang jiuling
"""],
        "events":[[(20, SIMPLE, 53,  normal ),
                   (20, SIMPLE, 203, slow ),
                   (60, SIMPLE, 153, normal),
                   (20, SIMPLE, 103, slow ),
                   (50, SIMPLE, 203, slow ),
                   (20, SIMPLE, 153, normal),
                   (80, SIMPLE, 3, normal ),
                   (10,SPLITS, 153, normal ),
                   (80,SPLITS, 103,   normal ),
                   (200, SIMPLE, 203, normal),
                   (20, SIMPLE, 53,  normal),
                   (20, SIMPLE, 153, normal),
                   (20, SIMPLE, 103, normal),
                   (200,SIMPLE, 153, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SPLITS, 103, normal),
                   (20, SIMPLE, 153, slow),
                   (20, SIMPLE, 53, normal),
                   (80, SIMPLE, 3, normal),
                   (60, SPLITS, 103, slow),
                   (10, SIMPLE, 53, slow),
                   (20, SIMPLE, 53, slow)],
                  [(220,SIMPLE, 153, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SIMPLE, 203, fast),
                   (20, SIMPLE, 153, fast),
                   (20, SPLITS, 103, normal),
                   (120,SIMPLE, 153, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SIMPLE, 203, fast),
                   (20, SIMPLE, 153, fast),
                   (20, SPLITS, 103, normal),
                   (20,SIMPLE, 153, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SIMPLE, 203, fast),
                   (20, SIMPLE, 153, fast),
                   (20, SIMPLE, 103, fast),
                   (20,SIMPLE, 153, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SIMPLE, 203, fast),
                   (20, SIMPLE, 153, fast),
                   (20, SPLITS, 103, normal),
                   (120,SIMPLE, 153, fast),
                   (20, SIMPLE, 203, normal),
                   (20, SIMPLE, 153, normal),
                   (20, SIMPLE, 203, fast),
                   (20, SPLITS, 103, fast),
                   (20, SPLITS, 53, fast),
                   (20, SIMPLE, 3,   fast),
                   (20, SIMPLE, 203, fast),
                   (20, SPLITS, 153, normal),
                   (20, SIMPLE, 103,   fast),
                   (20, SIMPLE, 3,   fast),
                   (200, SPLITS, 53, normal),
                   (20, SPLITS, 153, normal),
                   (20, SPLITS, 203,   normal),
                   (20, SPLITS, 103, normal),
                   (20, SPLITS, 153, normal),
                   (180,SPLITS, 53,  slow),
                   (10, SPLITS, 153, slow)]]
}

lvl3 = {"poem":["""moonlight drowns out all but the brightest stars

john ronald reuel tolkien""",
                """dont tell me the moon is shining
show me the glint of light on broken glass

anton chekhov""",
                """everyone is a moon and has a dark side
which he never shows to anybody

mark twain""",
            """do not swear by the moon
for she changes constantly
then your love would also change

william shakespeare""",
                """we all shine on
like the moon and the stars and the sun
we all shine on
come on and on and on

john lennon""","""we choose to go to the moon in this decade
and do the other things
not because they are easy
but because they are hard

john fitzgerald kennedy"""
],
        "events":[[(40,  SIMPLE, 153, fast),
                   (40, SPLITS, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SPLITS, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SPLITS, 103,  fast),
                   (200, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast)],
                  [(40, SIMPLE, 153, normal),
                   (40, SIMPLE, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SIMPLE, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SIMPLE, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SIMPLE, 103,  fast),
                   (40, SIMPLE, 153, normal),
                   (40, SIMPLE, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SIMPLE, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SIMPLE, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SIMPLE, 103,  fast),
                   (200, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast)],
                  [(140, MIRROR, 153, normal),
                   (240, MIRROR, 53,  fast),
                   (40, MIRROR, 103, fast),
                   (40, MIRROR, 203,  fast),
                   (40, MIRROR, 53,  fast),
                   (40, MIRROR, 153,  fast),
                   (40, MIRROR, 3,  fast),
                   (40, MIRROR, 103,  fast),
                   (40, MIRROR, 153, normal),
                   (40, MIRROR, 53,  fast),
                   (40, MIRROR, 103, fast),
                   (40, MIRROR, 203,  fast),
                   (40, MIRROR, 53,  fast),
                   (40, MIRROR, 153,  fast),
                   (40, MIRROR, 3,  fast),
                   (240,SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast)],                  
                  [(40, SIMPLE, 153, normal),
                   (40, SPLITS, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SPLITS, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SIMPLE, 53, normal),
                   (200, SPLITS, 103,  fast),
                   (100, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 53,  fast),
                   (240,RANDOM, 53,  normal),
                   (20, RANDOM, 153, normal)],
                  [(40, SIMPLE, 153, normal),
                   (40, SPLITS, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SPLITS, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SIMPLE, 53, normal),
                   (200, SPLITS, 103,  fast),
                   (100, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 53,  fast),
                   (200, SPLITS, 103,  fast),
                   (100, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 53,  fast),
                   (240,RANDOM, 53,  normal),
                   (20, RANDOM, 153, normal)],
                  [(40, SIMPLE, 153, normal),
                   (40, SPLITS, 53,  fast),
                   (40, SIMPLE, 103, fast),
                   (40, SPLITS, 203,  fast),
                   (40, SIMPLE, 53,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SIMPLE, 3,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SIMPLE, 53, normal),
                   (300, SPLITS, 103,  fast),
                   (200, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 53,  fast),
                   (300, SPLITS, 103,  fast),
                   (200, SPLITS, 153,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, SPLITS, 53,  fast),
                   (40, SPLITS, 103,  fast),
                   (40, SPLITS, 153,  fast),
                   (40, METEOR, 96,  normal) ]
        ]
}

lvl4 = {"poem":["""moon"""],
        "events":[[(80, SPLITS, 153,  normal)]]}
