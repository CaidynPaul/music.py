import music
#         Do   a    deer  a   fe-male  deer. ray  a   drop of     golden    sun me   a   name  I   call  my--self. far  a    long long way  to   run. sow  a   nee - dle  pul--ling thrd. la   a  note  to   fol low  sow.  tea   a  drink with jam  and bread. that will bring us back to doe     oh  oh  oh
notes = ['c3','d3','e3','c3','e3','c3','e3','d3','e3','f3','f3','e3','d3','f3','e3','f3','g3','e3','g3','e3','g3','f3','g3','a3','a3','g3','f3','a3','g3','c3','d3','e3','f3','g3','a3','a3','d3','e3','f3','g3','a3','b3','b3','e3','f3','g3','a3','b3','c4','c4','b3','a3','f3','b3','g3','c4','g3','e3','d3'] #melody
notes2 = ['c3','e3','g3'] # C Chord at end

#       Do   a  deer a  fe--male deer. ray a  drop of gol den  sun   me   a  name I call my--self far a long long way to run  sow   a  nee-dle pulling thrd. la   a  note to fol low sow tea  a drink with jam and bread.that will bring us  back to doe oh  oh  oh
dur = [1050,250,750,500,500,500,1050,900,500,250,250,500,500,1050,1050,250,500,250,750,500,1050,1050,500,250,250,250,500,1050,1050,500,250,250,500,500,1050,1050,250,250,250,250,500,1050,1050,250,250,250,500,250,1050,1050, 500, 750,750,750,750,1050,500,500,500] # duration for entire song
dur2 = [1050] # duration of c Chord at end. numbers for duration are in milliseconds.

pos = 0


while pos < len(notes) and pos < len(dur): # loop to play the notes
    music.play(0,notes[pos],dur[pos])
    music.wait() # wait for each note to finish playing
    pos += 1 #increment for next note

music.play(1,notes2[0],dur2[0]) # play the C Chord
music.play(2,notes2[1],dur2[0])
music.play(3,notes2[2],dur2[0])
music.wait()# wait for C Chord to end