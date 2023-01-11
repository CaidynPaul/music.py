import music
# Semibreves = 2000
# Dotted Minims = 1500
# Minims = 1000
# Crotchets = 500
# Quavers = 250



#        O     come all  ye  faith-ful,joy   ful and   tri-  um- phant o   come  ye    o  co    me  ye    to   Be---th-  le-hem   Come  and   be-  hold him  born the  king  of   an-gels
notes = ['f3','f3','c3','f3','g3','c3','a3','g3','a3','bb3','a3','g3','f3','f3','e3','d3','e3','f3','g3','a3','e3','d3','c3','c3','c4','bb3','a3','bb3','a3','g3','a3','f3','g3','e3','c3']
#                   O come all  ye faith-ful joy ful and tri-um-phant  o  come  ye o   co   me  ye  to  Be---th- le-hem  Come and be- hold him  bornthe king of an-gels
note_durations = [500,1000,500,500,1000,1000,500,500,500,500,1000,500,500,1000,500,500,500,500,500,500,1000,750,250,2000,1000,500,500,1000,1000,500,500,500,500,1000,500]
#                                                                                                      
chord1 = ['f3','c3','f3','c3','f3','bb3','f3','c3','d3','d3','c3','g3','c3','g3','c3','f3','c3','g3','c3','f3','c3','f3','bb3','f3','c3','a3','d3','g3','c3']
chord2 = ['a3','e3','a3','e3','a3','d3','a3','e3','f3','f3','e3','b3','e3','b3','e3','a3','e3','b3','e3','a3','e3','a3','e3','a3','e3','c#3','f3','e3','e3']
chord3 = ['c3','g3','c3','g3','c3','f3','c3','g3','a3','a3','g3','d3','g3','d3','g3','c4','g3','d4','g3','c3','g3','g3','f3','c3','g3','e3','a3','b3','g3']

print('{} \n {} \n {}'.format(len(chord1), len(chord2),len(chord3)))
print(len(notes))
print(chord1[25],chord2[25],chord3[25])



pos = 0 
n = 0

while pos <= len(notes) and pos <= len(note_durations):
    music.play(0,notes[pos],note_durations[pos])
    music.wait()
    # Chord Logic
    if pos == 0:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    
    if pos == 3:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 5:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1

    if pos == 6:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1

    if pos == 7:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1

    if pos == 8:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
        
    if pos == 9:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1

    if pos == 10:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 11:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 12:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 13:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 14:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 15:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 16:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 17:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 18:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 19:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 20:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    # Beth - le - __hem__ - C
    if pos == 22:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 23:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 24:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 25:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    if pos == 26:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1

    if pos == 27:
        music.play(1,chord1[n],2000)
        music.play(2,chord2[n],2000)
        music.play(3,chord3[n],2000)
        n+=1
    
    pos+=1