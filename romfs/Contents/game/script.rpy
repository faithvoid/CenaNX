# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#define e = Character('Eileen', color="#c8ffc8")

#JOHN CENA GAME VERSION 1.2
#FIX LOVE SONG NOT PLAYING
#ADDED SPANISH DUB
#ADDED JEWISH DUB

#JOHN CENA GAME VERSION 1.1
#ADDS DAY 4 (NEW GAME PLUS)
#OPTION TO ENABLE IT WHEN YOU START GAME
#CHANGED MUSIC TO BE NON-COPYRIGHTED COVERS
#FIXED, LET'S GO INSIDE OF TEACHER ROUTE
#ADD DAY 5 WHERE YOU FIGHT AN EVIL JOHN CENA MONSTER IN A SEWER (I THOUGHT I WAS JUST GOING TO SCHOOL!) (SIR JOHN CENA)

init:
    transform my_shake:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
define pc = Character("Fucco-san")
define jc = Character("Cena-senpai")
define buly = Character("Johnny")
define teach = Character("Mr. Cena")
define unk = Character("???")
define nerd = Character ("Johnathan")
define tsun = Character("Tsundere Cena")
define sexy = Character("Jane Cena")
define ref = Character ("Referee")
define guard = Character("Security Guard")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define mon = Character ("Monster")
define kni = Character ("Sir Johnathan Cena of York")
define all = Character ("Everyone")
define jesus = Character ("Jesus Cena")

image bg outschool = ("school_out.png")
image bg classroom = ("class.png")
image bg outclass = ("class_out.png")
image bg bedroom = ("bedroom.png")
image bg black = ("blank.png")
image bg alley = ("alley.png")
image bg outprom = ("outprom.png")
image bg prom = ("prom.png")
image bg sex = ("sexscene.png")
image bg jcpin = ("jcpin.png")
image bg nerdpin = ("nerdpin.png")
image bg bulypin = ("bulypin.png")
image bg explode = ("world.png")
image bg teachpin = ("teachpin.png")
image bg teachpin2 = ("teachpin2.png")
image bg teachwin = ("teachwin.png")
image bg jail = ("jail.png")
image bg spiral = ("spiral.png")
image bg sewer = ("sewer.png")
image bg classroom_teach = ("classteach.png")
image bg pipe = ("pipe.png")
image bg knightlose = ("knightlose.png")
image bg fire = ("fire.png")
image bg goodend = ("goodend.png")
image white = ("white.png")
image jc stand = ("Orange.png")
image teach stand = ("Teacher.png")
image buly stand = ("Bully.png")
image buly blush = ("Bully_blush.png")
image nerd stand = ("Nerd.png")
image nerd cry = ("Nerdcry.png")
image nerd dirty = ("Nerd_dirty.png")
image tsun stand = ("Orange.png")
image sexy stand = ("Sexy.png")
image guard stand = ("Guard.png")
image mon stand = ("Monster.png")
image kni stand = ("Knight.png")
image mon dead = ("Monster_dead.png")
image mon mad = ("Monster_mad.png")
image jesus stand = ("Jesus.png")

# The game starts here.
label start:
"Have you played/beaten the game before?"
menu:
    "No / I'd like to start from the beginning":
        jump startgame
    "Yes / I'd like to start New Game Plus":
        jump newgameplus
label startgame:
pc "Oh man, It sucks I have to move school..."
pc "All my friends were bullying me..."
pc "But at least I hope I can make much more friends at Cena High!"

scene bg outschool
with fade

pc "Huh, nobody's here..."

play music "cena.ogg"
show jc stand
with fade
jc "Hey there! It's me, John Cena!"

menu:
    "Wah! You scared me!":
    
        jump scare
    
    "Woah! John Cena!":

        jump fan

label scare:
jc "Oh, sorry about that! Didn't know you were the new kid!"
jump scarefan

label fan:
jc "Hey, you're the new kid, right?"
jc "Glad to have you here!"
jump scarefan

label scarefan:
pc "Thank you. Where should I go?"
jc "You should probably meet the teach, Mr. Cena"
jc "Or you can hang out with me and the gang!"
pc "Ok, I'll think about it!"                                                     
jc "Awesome! Later!"

hide jc stand

pc "Oh shoot! What should I do?"
menu:
    "Go to Mr. Cena's classroom":
        
        jump meetteach
    
    "Follow Senpai's crew":
    
        jump senpai
###############GO WITH FRIENDS#############
label senpai:
pc "Cena! Wait up!"
"You ran and ran until you catch up with Cena-Senpai"
scene bg outclass
with fade
show jc stand
jc "Oh! Hey bro! I want you to meet everyone!"
jc "This is Johnny, the tough guy of the group. Don't get on his bad side!"
show buly stand
buly "Yo chump! Don't get in my way!"
hide buly stand
jc "Alright, this is Johnathan. He ain't as talkative like all of us."
show nerd stand
nerd "h-Hi..."
nerd "Sorry, I have a project I need to do..."
hide nerd stand
jc "Hahaha, that's all he does. All he does is work"
jc "Wait, work! Ahh shoot, we gotta get to class!"
jc "Let's go, champ!"

scene bg classroom
with fade
jump classtime1


###############GO TO TEACHER###############
label meetteach:
pc "I should really meet the new teacher..."

scene bg classroom
with fade
pc "Hello? Is anyone here?"
unk "Hi, I'm here."

show teach stand

teach "Hello, I'm Mr. Cena, you're teacher, and you are?"
menu:
    "Fucco, sir":
        jump meetteach1
    "None of your business!":
        jump meetteach2

label meetteach1:
pc "i-It's Fucco, sir!"
teach "Ahh, a nice name for a nice boy. Nice to meet you, Fucco!"
jump meetteachnext

label meetteach2:
pc "It's none of your DAMN business!"
teach "Watch it, mister! With that attitude, you're not gonna get anywhere..."
jump meetteachnext

label meetteachnext:
teach "So, how can I help you?"
pc "I'm new to the school, and somebody told me to go to you"
teach "Ahh, it was probably that John Cena boy. He's nice, isn't he?"
pc "Yeah, he's cool I guess..."
teach "Oh! It's almost time! You'd better take your seat!"
pc "Alright, thanks!"

hide teach stand
with fade
jump classtime1

label classtime1:
"You barely listen to the lesson, but understand it enough..."
show teach stand
teach "...and that's it for today! Remember to do your assignment on the history of the WWE belt by tomorrow!"

scene bg outschool
with fade

"You leave the classroom with everyone else. What should you do now?"
menu:
    "Find Cena-senpai":
        jump findcenasenpai
    "Go home":
        pc "I'm going home, I'd better work on that assignment..."
        jump notsofast

label findcenasenpai:
"You look all around, but find nothing"
pc "F******k this, I'm going home"
jump notsofast

label notsofast:
unk "Not so fast, chump!"
"You turn quickly"
show buly stand
with fade
buly "Hey, nerd! You better work on my assignment, or else!"
buly "In fact, take this!"
"He whacks your notes into a puddle, completely drenching them"
pc "Ahh, crap!"
menu:
    "F******k that guy, fight back!":
        "You swing your fist, but Johnny moves his head quickly, dodging your punch"
        buly "Hahaha! This chump's tryna knock me out! Take this!"
        "He hits you hard on the head"
        scene bg black
        with fade
        "You don't think you're getting up..."
        "He's pinning you!"
        "1..."
        "2..."
        "3!!!"
        "Bells go off, Johnny's celebrating!"
        "Meanwhile, you're not"
        "You're dead"
        ".:. BAD END .:."
        return
    "Run home like a crybaby chump":
        pc "Man, I don't need this!"
        scene bg black
        with fade
        "You bolt it back home"
        scene bg bedroom
        with fade
        pc "Oh man, Teach's gonna kill me!"
        pc "or Johnny's gonna do it first!!!"
        pc "I'll just go to bed, it's late..."
        scene bg black
        with fade
        jump day2

label day2:
scene bg bedroom
with fade
pc "Oh man, I had a horrible night..."
pc "Oh shoot! The assignment! I completely forgot about it!"
pc "But I don't have my notes! What do I do?!?!?!"
pc "I'll see when I go to school..."
scene bg outclass
with fade
pc "Who should I go to?"
menu:
    "Cena-Senpai":
        jump day2cena
    "Johnny":
        jump day2johnny
    "Johnathan":
        jump day2nerd
    "Mr. Cena":
        jump day2teacher
"To-do, day 2"

label day2cena:
pc "Cena! Cena!"
show jc stand
jc "Woah! What is it, champ?"
pc "I lost my notes and didn't do my assignment! What do I do?"
jc "Hey bro, you came to the right guy! Let's do it together!"
pc "Ok!"
scene bg black
with fade
$ choice = "jc"
pc "This is tricky! What happened in 1998 with the WWE belt?"
jc "It's simple! Thats when..."
"After a few minutes, you get your assignment done with Cena"
scene bg outclass
show jc stand
with fade
pc "Thanks, John!"
jc "Hey, no problem champ!"
jc "Oh dang, we gotta get to class pronto!"
jump day2classroom

label day2johnny:
$ choice = "buly"
pc "Johnny! Where are you?"
scene bg alley
with fade
pc "Johnny! Where are you?"
pc "I don't like this place... It's scary..."
show buly stand
buly "Look! It's the chump! Ready for your payback?"
pc "Payback? I need your help!"
pc "Hey, why is it so dark here?"
buly "Oh, it's always dark here."
buly "Well, I WON'T help you!!!"
pc "Please! I need to do the assignment or else I'll fail!"
buly "Well, now that you mentioned it..."
buly "Tough luck, chump!!!"
hide buly stand
pc "Hey! Come back here!"
menu:
    "Go to class without an assignment":
        pc "I guess I'll have to tell the teacher the bad news..."
        scene bg classroom
        with fade
        show teach stand
        pc "Hey, sir. I have bad news..."
        teach "What is it sir? You don't have your assignment?"
        pc "Ummm...."
        pc "Yeah..."
        teach "Oh, that's not good!"
        teach "Since this is an extremely small scholastic year lasting only 3 days, this assignment was literally your whole grade!"
        teach "I'm sorry, but you've just failed this year."
        pc "OH NO!!!"
        scene bg black
        with fade
        ".:. BAD END"
        return
    "Chase Johnny":
        pc "Oh no you don't!"
        pc "g-Gimmie your assignment!"
        show buly stand
        buly "What did you say to me, chump?"
        pc "Y-You heard me! Gimmie your assignment!"
        buly "Hahaha! I like you, chump!"
        buly "Tell ya what, I'll give you what I stole from that nerd"
        "You got a perfectly written and cited assignment!"
        pc "Wow! Thanks!"
        buly "Haha! Now scram, chump!"
        jump day2classroom

label day2nerd:
$ choice = "nerd"
pc "Hey Johnathan!"
show nerd stand
nerd "Huh? Are you calling me?"
pc "Yeah! Why, does nobody usually talk to you?"
nerd "Yeah. Usually I'm on my own..."
pc "Well, I need help with my assignment. I lost my notes. Can you help me?"
nerd "Yeah!"
nerd "Wait, are you gonna just use me for my vastly superior intelligence, then ditch me after getting a perfect score on the assignment?"
menu:
    "Yeah!":
        nerd "Huh. Typical. You're just like Johnny..."
        nerd "Well, t-take this!"
        "He grabs your neck and throws you on the ground"
        scene bg black
        with fade
        "You blank out, but feel him holding your legs down"
        "You hear a countdown"
        "1..."
        "2..."
        "3!"
        "You were pinned! How embarrasing!"
        "You hear bells ringing and people cheering before your life and dignity fade out of your body"
        ".:. BAD END"
        return
    "No":
        nerd "Ah, phew!"
        nerd "Anyways, sit down here with me, I'll help you out!"
        scene bg black
        with fade
        "He helps you with the assignment"
        "You also help him and have an intellectual conversation about the history of the WWE"
        scene bg outclass
        with fade
        show nerd stand
        nerd "Wow! I didn't know you knew so much about the history of the WWE!"
        pc "Well, yeah. I thought everyone knew about our country"
        nerd "Anyways, we gotta go to class, or we'll be late by 1.32 seconds!"
        jump day2classroom

label day2teacher:
$ choice = "teach"
scene bg classroom
with fade
show teach stand
teach "Fucco! You're early! What's the rush, you look like you've seen a ghost!"
pc "I'm sorry Mr. Cena! I couldn't do my assignment!"
teach "Hey now, don't get upset. It's just an assignment... It isn't even that hard..."
teach "How about I give you the answer sheet, and you quickly copy it out before the others come in"
pc "y-You really mean it?"
teach "Sure, but you'd better do it now before the others'll want to do the same!"
pc "Oh yeah! Thanks again, Teach'!"
"You quickly copy the answers and have a nice assignment ready"
teach "Now, give back the answers and take your seat. We're starting."
jump day2classroom

label day2classroom:
scene bg black
with fade
scene bg classroom
with fade
show teach stand
teach "So class! Hand in your assignments!"
"You proudly hand in your assignment to the teacher"
teach "Thank you all! Johnny, is yours the same as Johnathan's again?"
show buly stand
buly "Uh... No! This time mine's legit!"
teach "Hmmm. It even says Johnathan crossed out with to say your name!"
buly "C'mon teach! I need this so I can join the WWE!"
teach "Ugh, for the last time, I won't fix your grade!"
buly "Not cool!"
hide buly stand
"Johnny storms out angrily"
teach "Dang. There he goes again..."
teach "Now, where was I?"
teach "Oh yeah, today's lesson!"
scene bg black
with fade
"You nearly fall asleep in class, barely making out what the lesson was about"
scene bg classroom
with fade
show teach stand
teach "... and that's how Brock Lesnar got pummeled!"
teach "No homework today, but remember that the prom is tomorrow!"
pc "Wait, the prom's tomorrow?! We have a prom?"
show jc stand
jc "Well, yeah! You didn't know?"
pc "Nobody told me!"
hide jc stand
teach "Well, there's no time to explain it, school's over, get out!"
scene bg bedroom
with fade
pc "Prom's tomorrow!?"
pc "Oh well, I think I know who to invite for the prom..."
scene bg black
with fade
"You pick up your phone and call..."
scene bg outprom
with fade
pc "Today's the day of the prom!"
pc "I wonder if my date is here yet..."
pc "Ahh, I think I see them now!"
if choice == "buly":
    jump day3buly
pc "Oh shoot, that's not them!"
show buly stand
buly "Hey chump! What are you doing with no date, huh?"
pc "Oh, I'm just waiting for my date"
buly "Well, I got my piece of ass! Ain't that right, sweetie?"
show sexy stand
sexy "Heehee, you're so funny Johnny-pie!"
hide sexy stand
buly "WHAT DID I SAY ABOUT CALLING ME THAT IN FRONT OF EVERYONE?!"
hide buly stand
"You witness Johnny doing an Irish whip to Jane, knocking her down"
"He holds the pin!"
"1..."
"2..."
"3!"
"DING DING DING!"
show buly stand
"Johnny stands up proudly"
buly "You didn't see me!"
hide buly stand
pc "Well, that was weird"
pc "They're probably inside..."
scene bg prom
with fade
pc "Oh man, where are they?"
pc "Oh, THERE they are!"
if choice == "jc":
    jump day3jc
if choice == "nerd":
    jump day3nerd
if choice == "teach":
    jump day3teach

label day3jc:
show jc stand
jc "Hey bro, you called me here?"
pc "Cena! I wanted to tell you something..."
stop music
play music "love.ogg"
jc "Shh..."
jc "You don't have to tell me anything..."
jc "I knew you were a good guy when you first stepped through the gates..."
jc "You'll always be my champ"
pc "Cena-senpai..."
jc "Hey, let's ditch this joint and go back to your place..."
pc "Oh yeah..."
scene bg bedroom
with fade
show jc stand
jc "So, are you ready?"
pc "Never been more..."
scene bg sex
with fade
jc "Oh yeah..."
pc "Go right in!"
jc "Yeah!"
scene bg jcpin
with fade
stop music
play music "cena.ogg"
jc "I GOT YOU! COUNT THE PIN!!!"
pc "AH SHIT!"
ref "ONE!!!"
pc "I GOTTA GET OUT!"
ref "TWO!!!"
pc "NONONO!!!"
ref "THREE!!!"
jc "YEAH!"
scene bg bedroom
with fade
show jc stand
jc "Woah! You're really good!"
jc "That was fun, we should wrestle more sometimes, champ!"
pc "Yeah! Thanks a lot!"
scene bg black
with fade
pc "I got a friend!"
pc "I guess I turned from a chump into a champ!"
".:. SENPAI END"
jump day4

label day3nerd:
show nerd stand
nerd "Why did I come here?"
nerd "My feet hurt, the music's loud"
nerd "I wish I was at home winning titles..."
pc "It's because I like you..."
stop music
play music "love.ogg"
nerd "w-What?!"
nerd "Impossible! The statistics that anyone is my friend is between 15 to-"
pc "Forget your statistics! You're hiding behind them!"
pc "I want you to remember this moment and embrace it..."
nerd "i-I think you're serious"
pc "Let's do it..."
nerd "d-d-Do what?!"
pc "IT"
scene bg sex
with fade
nerd "Oh my gosh!"
nerd "They never talked about THIS in the text books!"
pc "Oh yeah!"
pc "Oh yeah!!!"
scene bg nerdpin
with fade
stop music
play music "cena.ogg"
nerd "No fair!"
ref "ONE!"
pc "I got you now!"
ref "TWO!"
nerd "I can't fail! I never failed!"
ref "THREE!!!"
pc "YEAH!!!"
scene bg prom
with fade
show nerd stand
nerd "That was lots of fun! I never had a wrestling partner!"
show teach stand
teach "What were you doing? Were you wrestling in the hall?!"
pc "t-Teach! I can explain!"
teach "Explain in the principal's office tomorrow morning! Both of you!"
nerd "Uh oh!"
teach "I never expected such behaviour from you, Johnathan. Ahh well, I guess kids change..."
hide teach stand
nerd "Ohh geesh..."
pc "Hey..."
nerd "What?"
scene bg black
with fade
pc "Don't worry about it"
".:. NERD END"
jump day4

label day3buly:
show buly stand
buly "Why did you call me, chump?"
pc "Because I know your true feelings!"
buly "?!"
pc "I know you like me! I saw it since day one!"
show buly blush
buly "i-I don't like you or anything!!!"
pc "Haha! I knew it!"
buly "c-Chump! Can we go somewhere more private?"
pc "Alright, follow me"
scene bg alley
with fade
show buly stand
pc "Now, admit it!"
buly "Admit this!"
scene bg sex
with fade
pc "w-What are you doing?!"
buly "What I wanted to do for a looong time!"
pc "Oh no, this is bad touch!!!! Most likely illegal!"
scene bg bulypin
with fade
buly "TAKE THIS NERD!"
ref "ONE!!!"
pc "YOU CAN'T..."
ref "TWO!!!"
pc "SEE..."
ref "THREE!"
pc "MEEEEEEEEEEEEE!!!!!"
stop music
scene bg explode
with flash
"And so, the world was destroyed."
"Good job, you dumbo."
scene bg black
with fade
".:. BULLY END"
return

label day3teach:
show teach stand
teach "Why did you call me?"
pc "I was wondering..."
pc "Why did you give me the answers to the assignment? Shouldn't you have failed me?"
teach "That is because..."
stop music
play music "love.ogg"
teach "There is something called, forbidden love"
teach "Normally, I'm not supposed to have feelings for one of my students, but..."
teach "When I saw you, begging..."
teach "Little did you know that..."
teach "That was my fetish..."
pc "Teacher-san?"
teach "I'll have you know..."
scene bg sex
with fade
teach "Oh yeah..."
pc "Teach, that's my..."
teach "Don't worry..."
pc "I knew it!"
pc "Take THIS!"
teach "Why you little!"
"BLAM!"
pc "Ugh..."
stop music
play music "teach.ogg"
scene bg teachpin
with flash
teach "I played in WWE, you know!"
teach "Would've gone pro if I didn't start teaching!"
pc "Why you..."
teach "In my new WWE, people will wrestle for what they believe!"
teach "Not for praise! Not for fans!"
pc "You're evil!"
scene bg teachpin2
with flash
teach "Ow"
teach "This isn't...wrestling..."
pc "I didn't come to this school to get friends..."
pc "I came to this school to stop you!"
teach "You..."
scene bg teachwin
stop music fadeout 1.0
pc "I've done it..."
pc "I've stopped the apocalypse..."
scene bg black
with fade
pc "I wish I had a wrestling partner though..."
".:. TEACHER END"
jump day4

label newgameplus:
"Did you achieve all 4 possible endings?"
menu:
    "No I didn't, I'm going to do that now!":
        jump startgame
    "Yes I did, and I know what happens in each of them!":
        play music "cena.ogg"
        "So, you achieved all the endings, huh?"
        "Well, as of version 1.1, you can skip past the endings for the brand new day(s)!"
        "However, we need to know who you went to the prom with."
        jump newgameplus2
label newgameplus2:
"So, who did you romance?"
menu:
    "Johnny":
        "Due to the world literally exploding and everyone dying, you cannot really continue from there."
        "Please choose another waifu"
        jump newgameplus2
    "Cena-senpai":
        $ choice = "jc"
        jump day4
    "Johnathan":
        $ choice = "nerd"
        jump day4
    "Mr. Cena":
        $choice = "teach"
        jump day4
        
label day4:
scene bg black
with Pause(5)
play music "cena.ogg"
pc "Oh wait, I have to go to school tomorrow!"
scene bg bedroom
with fade
pc "That was some prom..."
pc "Oh shoot! I'm late!"
scene bg outschool
with fade
pc "I gotta get to class quick!"
unk "Oh no you don't, mister!"
show guard stand
guard "It's past homeroom, school's closed to newcomers!"
pc "Wait, when did they add this?"
guard "After what happened last night!"
if choice == "nerd":
    guard "Hey, aren't you the kid who wrestled in the middle of the prom?!"
    pc "Ummm...."
    pc "I think so..."
    guard "You're going to jail, chump!"
    pc "Oh rats..."
    jump day4jailnerd
if choice == "jc":
    guard "Apparently, there was wrestling in the prom!"
    pc "But I didn't do that!"
    pc "I practice safe wrestling at home!"
    guard "That's disgusting. You're going to detention!"
    pc "What?! That doesn't make sense! Why?"
    guard "Are you questioning authority? Now I have two reasons for you to be locked up!"
    pc "Dang!"
    jump day4jail
if choice == "teach":
    guard "YOU killed the only teacher in this school, so we're going to have to hire a new one!"
    pc "It wasn't my fault! I was in the zone!"
    pc "The music was really cool!"
    guard "That's everyone's excuse, sport!"
    guard "I'm gonna have to arrest you for murder."
    pc "Arrest! You're a school guard!"
    guard "You're going to somewhere worse than prison though..."
    guard "Detention!"
    pc "Nooooooo!"
    jump day4jail
    
label day4jailnerd:
scene bg jail
with fade
pc "Oh man! This sucks!"
show nerd stand
nerd "What? Oh no, it's you!"
pc "Me? What's the problem with me?"
pc "Wait, what are you doing here? Aren't you an A student?"
nerd "Well it turns out the teacher was not lying and actually put me in detention"
nerd "And it's all your fault!"
nerd "What did you say last night? Oh yeah!"
nerd " 'Don't worry about it' "
nerd "What good that did, huh?"
pc "I still think that's correct, as all we gotta do is break out of here!"
nerd "Break out?! Are you mad?!"
nerd "Then we'll get into more trouble!"
pc "I'll think of something, Johnathan-senpai."
nerd "Well you'd better! I'm gonna go cry into my pillow"
hide nerd stand
jump day4nerdbreakout

label day4nerdbreakout:
hide nerd stand
hide nerd cry
menu:
    "Check under the bed":
        "Nothing!"
        jump day4nerdbreakout
    "Check in the bookshelves":
        "Just a bunch of old books"
        "You see a math book"
        pc "Hey, this may hold you off"
        show nerd cry
        nerd "h-Huh?"
        show nerd stand
        nerd "Oh hey! An first edition! I haven't seen one of those in years!"
        nerd "Thanks Fucco!"
        pc "Um... No problem?"
        jump day4nerdbreakout
    "Check in the toilet":
        "You see a rope and a turnbuckle"
        pc "A rope? What if I..."
        "You stick your hand in the toilet and tug the rope"
        "It isn't coming out"
        pc "Come on you..."
        "You pull it out, and the toilet water starts draining"
        pc "What the?"
        "Suddenly, an idea springs to mind"
        pc "Johnathan! Jump in!"
        show nerd stand
        nerd "w-What? I'll get my pens dirty!"
        pc "Just do it!"
        hide nerd stand
        nerd "Oh, what the hey. Here I go!"
        "You bodyslam into the toilet and go through the magical pipeline"
        scene bg spiral
        with flash
        pc "Woah..."
        nerd "I can't believe it..."
        pc "I think we're almost out..."
        scene bg sewer
        with flash
        pc "Haha! We made it!"
        pc "Umm... Johnathan?"
        show nerd dirty
        nerd "Ugh! Mother's going to be so cross with me!"
        pc "Ok, well do you know what time it is?"
        nerd "Umm, according to the angular trajectory of the Sun from our current location, I'd say it's exactly 4:12"
        pc "That means school's over!"
        pc "I finished that puzzle really quickly, how the heck did it take so long?"
        nerd "Beats me, I lost track of time remembering my times tables"
        pc "Wow dude, you need to get laid"
        nerd "Well, I'd better get home before Father thinks I'm out with Johnny injecting steroids. See you later!"
        pc "Umm... See you later?"
        pc "(I never see my parents at home. Huh...)"
        scene bg black
        with fade
        jump day5
        

label day4jail:
scene bg jail
with fade
pc "Oh man! This sucks!"
jump day4breakout
label day4breakout:
menu:
    "Check under the bed":
        "Nothing!"
        jump day4breakout
    "Check in the bookshelves":
        "Just a bunch of old books"
        "You see a math book"
        pc "Booring!"
        jump day4breakout
    "Check in the toilet":
        "You see a rope and a turnbuckle"
        pc "A rope? What if I..."
        "You stick your hand in the toilet and tug the rope"
        "It isn't coming out"
        pc "Come on you..."
        "You pull it out, and the toilet water starts draining"
        pc "What the?"
        "Suddenly, an idea springs to mind"
        pc "I'm going in!"
        pc "As the Gospel says..."
        pc "Never Give Up!"
        "You bodyslam into the toilet and go through the magical pipeline"
        scene bg spiral
        with flash
        pc "Woah..."
        pc "I've never seen anything more beautiful..."
        pc "Well, other than John Cena's fantastic conquering of the Undertaker's Streak which happened"
        pc "I see an exit!"
        scene bg sewer
        with flash
        pc "Haha! I'm out!"
        pc "But I smell worse than a locker room!"
        pc "I'd better get home and change out of my clothes!"
        pc "(Wait, who am I even talking to?)"
        scene bg black
        with fade
        pc "(Now I'm really confused...)"
        jump day5
label day5:
stop music
play music "cena_2.ogg"
scene bg bedroom
with fade
pc "Wow! These have been amongst the most exciting days ever!"
pc "I don't think they could be topped!"
scene bg outschool
with fade
pc "Hello?"
scene bg classroom
with fade
pc "Hello?"
show teach stand
teach "Hello, Fucco. You're late again, sit down."
if choice == "teach":
    pc "Wait, didn't I kill you?"
    teach "What? Kill me?"
    "The teacher comes closer towards you and starts whispering"
    scene bg classroom_teach
    teach "Listen, you little chump"
    teach "One more mention about what happened at prom and it's pounding time"
    teach "I just barely got my job back, so you'd better be on my good side"
    scene bg classroom
    show teach stand
    teach "Now, please take your seat Fucco"
scene bg classroom at my_shake
show teach stand
teach "Now class, we're going to learn how..."
teach "What now!?"
show nerd cry
nerd "Oh geesh! It's an earthquake!"
hide nerd cry
teach "No, I think it's something far worse..."
teach "Come with me, children. We need to go down..."
show buly stand
buly "Down where, 'teach?"
hide buly stand
teach "I'll show you..."
scene bg pipe
with fade
show nerd cry
nerd "Oh no, it stinks down here!"
show buly stand
buly "Can it, chump!"
buly "Teach, my abs are aching, how long do we need to keep walking?"
show teach stand
teach "Until we can find the-"
stop music
play music "action.ogg"
teach "Stop!"
teach "There it is!"
show mon stand
mon "BLARGH!"
unk "Stand back, foul beast!"
pc "Who said that?"
show kni stand
unk "Stand back, children, for it is I!"
kni "Sir Johnathan Cena of York!"
kni "I am here to slay this evil monster once and for all!"
show mon stand
mon "BLARGH!"
pc "I THOUGHT THIS WAS JUST A HIGH SCHOOL SIM, WHAT THE HECK'S GOING ON?!"
show kni stand
kni "Ye shall meet thine end, foul beast!"
mon "BLARGH!"
scene bg knightlose
with flash
kni "Help! I hath lost!"
mon "BLARGH!"
kni "He shant go for the pin! I'll lose my knighthood!"
menu:
    "Help Sir Cena":
        jump day5help
    "Fight the monster yourself":
        jump day5canon
    "Watch":
        jump day5bad
label day5help:
pc "Don't worry, Sir!"
"You ram yourself right into the monster's belly"
scene bg pipe
with flash
show mon stand
pc "Go Sir! Get him!"
"He slashes his sword and chops the monster clean in half"
stop music
hide mon stand
show mon dead
with flash
mon "Ow"
hide mon dead
with Pause(2)
play music "cena_2.ogg"
all "Hooray!"
scene black
with fade
"And so, they went back to the surface and had a neat party"
"It was full of pizza, candy and wrestling!"
"Everyone became bestest friends with Fucco, and Fucco had never been more happy"
pc "Now guys, you know I wouldn't have been able to do it without Mr. McMahon, our Lord and Saviour"
all "True that!"
all "Hahahahahaha!"
".:. GOOD END"
scene bg black
with fade
"But is it the TRUE ending?"
return

label day5canon:
pc "Hey, chump!"
mon "Huh?"
"You tackle the monster in the chest, knocking the Knight onto the ground"
kni "What art thou doing, squire?! You'll hit-"
buly "The fuse box!"
"You tackle the monster into a fuse box, alighting the sewer"
stop music
scene bg fire
with flash
play music "teach.ogg"
show mon mad
mon "Grr!"
pc "Come at me, chump!"
"He tackles you, knocking you to the ground"
scene black
with flash
pc "Ugh..."
pc "Did I die?"
pc "Did I get pinned?"
pc "I can't lose!"
pc "I need to remember what everyone taught me!"
scene bg goodend
with flash
mon "NO!"
pc "Ref! Ref!"
pc "Count them!"
scene black
with flash
pc "I need to remember the most important person in my life..."
pc "My love..."
if choice == "nerd":
    pc "Johnathan..."
    pc "Oh, all the times we've had..."
    scene bg outclass
    with flash
    show nerd stand
    nerd "h-Hi..."
    nerd "Sorry, I have a project I need to do..."
    scene black
    with flash
    jump day5canonend
if choice == "jc":
    pc "Cena-senpai..."
    pc "Oh, all the times we've had..."
    scene bg outschool
    with flash
    show jc stand
    jc "Hey, champ!"
    scene black
    with flash
    jump day5canonend
if choice == "teach":
    pc "Mr. Cena..."
    pc "Oh, all the times we've had..."
    scene bg classroom
    with flash
    show teach stand
    teach "Do your homework!"
    scene black
    with flash
    jump day5canonend

label day5canonend:
pc "Good times..."
pc "Wait a minute, what am I doing?"
pc "I have a match to win!"
scene bg goodend
with flash
mon "BLARGH!"
ref "One!!!"
pc "COUNT FASTER!!!"
ref "TWO!!!"
pc "COME ON!!!"
ref "THREE!!!"
stop music
play music "cena_2.ogg"
pc "YEAH!!!!"
mon "NOOOOOO!!!!"
pc "Uh oh!!!"
scene white
with flash
stop music
pc "Did I die?"
pc "Oh no, I think I did..."
unk "Don't worry, my son..."
pc "Is that? No, it can't be"
unk "It most certainly is..."
show jesus stand
with flash
unk "It's me..."
jesus "Jesus Cena..."
pc "Jesus!"
pc "Does this mean I died?"
jesus "Sadly, yes, but your sacrifice did not go unnoticed..."
jesus "Look down at the world to see what happened to everyone..."
scene bg outschool
with flash
show jc stand
jesus "Cena-senpai kept meeting new students until he got his PhD in Wrestlography"
scene bg alley
with flash
show buly blush
jesus "Johnny was arrested for multiple cases of assault and steroid abuse."
jesus "He is currently serving 5 life sentences"
jesus "A sixth one was recently added, however, for loitering around a ring"
scene bg classroom
with flash
show teach stand
jesus "Mr. Cena kept teaching until he was forced to retire"
jesus "He later started a gym and taught people how to make people not see him"
scene bg outclass
with flash
show nerd stand
jesus "Johnathan ran for Congress, and later won the elections for the President of the WWE"
scene white
with flash
show jesus stand
jesus "And all of this wouldn't have been possible without you"
jesus "You stopped the monster, so you inspired everyone to Never Give Up"
jesus "The world thanks you"
pc "w-Wow... I don't know what to say..."
jesus "All you need to say..."
scene black
with fade
jesus "Don't worry about it"
scene black
with Pause(1)
stop music
".:. TRUE END"
return

label day5bad:
teach "Somebody help him!"
buly "No way man! i-I've strained my muscles pounding chumps!"
nerd "I can't, my mom'll kill me if I stain my shirt!"
jc "I'm a pacifist, not a fighter..."
pc "Uhh... Uhh..."
mon "BLARGH!!!"
"The monster threw Sir Cena across the room"
scene bg pipe
with flash
show mon mad
mon "ROAR!!!"
"He comes closer..."
"Quickly, he jumps on everyone!"
scene black
with flash
"Oh no!"
"He's pinning EVERYONE!!!"
buly "Hey, not cool man!"
ref "ONE!!!"
nerd "Hey, where did the referee come from?"
ref "TWO!!!"
jc "No! It can't end like this!!!"
ref "THREE!!!"
"DING DING DING!!!"
mon "ROAR!!! :D"
"He just pinned everyone at the same time..."
"You cannot go on..."
"Nobody's standing up"
"I think they all died!"
"You wish you did too after what had happened next..."
scene bg explode
with flash
"The monster had even pinned the whole world"
"The world had been destroyed"
"All because you wanted to just watch"
scene black
with fade
"The world ended..."
"and it's all your fault"
".:. BAD END"
return
