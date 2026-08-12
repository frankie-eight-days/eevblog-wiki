---
video_id: MMR-lOm-FfA
title: EEVblog #118 - Renesas Devcon 2010 Day 2
url: https://www.youtube.com/watch?v=MMR-lOm-FfA
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 41, "3": 64, "4": 87, "5": 117, "6": 130, "7": 146, "8": 169, "9": 187, "10": 201, "11": 220, "12": 267, "13": 283, "14": 329, "15": 363, "16": 395, "17": 430, "18": 445, "19": 467, "20": 482, "21": 502, "22": 536, "23": 552, "24": 578, "25": 593, "26": 676, "27": 694, "28": 719, "29": 746, "30": 770, "31": 784, "32": 819, "33": 858, "34": 883, "35": 917, "36": 932, "37": 948, "38": 965, "39": 982, "40": 1009, "41": 1021, "42": 1041, "43": 1058, "44": 1083, "45": 1106, "46": 1121}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones.

**Dave Jones:** And it's 8:15 Tuesday morning and here we are in the main lecture hall about to get the keynote address and as you can see it's filling up pretty quick. Everyone's spilling over for breakfast. Everyone's pumped and this lecture hall will be completely full in about 5 minutes or so. That's the spillage from breakfast. Let's go.

**Dave Jones:** We are the largest MCU supplier with 30% market share. We are also ranked number one in every major segment category such as the 8 16 and the 32-bit MCU products.

**Dave Jones:** Number of lectures is crazy. Here's the nerve center for the hardware labs. This is where they get all their demo boards, put them together, get all the manuals together, program the notebooks, format the hard drives for all the hardware lecture labs and they put them all onto the trolleys and they wheel them out down the hall into the dozen or so lecture rooms they've got.

**Dave Jones:** Unbelievable. I think uh Thomas will comment on the second instruction of this discussion. Well, let's start with 8-bit. The top question is I want to start with 8-bit. I want to do what I do. What's on the board and if you're not within the um the rated uh minimum input voltage um for high or or maximum for low, if you're in the no-man's land, you can get um both the P channel and the N channel of the internal uh gate turned on.

**Dave Jones:** And that results in current from top to bottom and from VDD to ground. And so, watch out for those. And in addition, the PC board cleanliness itself can be an issue because it can then uh, draw hundreds of milliamps if you don't watch out.

**Dave Jones:** You will need to use more expensive diodes to be able to um, you know, deal with the recovery current. We're at the Renesas uh, one of the Renesas stands and where it looks like we got some power electronics here. Can you go through and explain exactly what you've got here?

**Dave Jones:** Yes, I can. Right. What we have right here is our setup of our our scalable VR solution. And what it is is it's a digital controller functioning with our POL SIP device which is a PWM IC with driver high side and low side FET in one package. And in this particular package, we're looking at an 8 by 8 device QFN 56 package.

**Dave Jones:** That's an 8 by 8 mm device and that's what is IT How much is it? It can do It can do 40 amps max. 40 amps max. Unbelievable for an 8 by 8 package like that. Amazing. Have it'll tell you what you're looking at in the V out and the temperature and the I out.

**Dave Jones:** Oh, very nice. I'm looking at this as well. going. So, we'll go ahead and just load it up to 80 amps. 80 amps? Obviously, you can see the temperature start to jump up. Yep. As well as the I out function now at 80 amps.

**Dave Jones:** And of course, the best part about these trade shows are the freebies. Check it out. Freebies, right? You guys give away freebies? Uh, sometimes. Excellent. Thanks. Haha. Slip 114. Score. That wasn't a freebie.

**Dave Jones:** Oh, shoot. Scoreless. Ah. Ah. Bring it. Beautiful. It's all good. Inside the Toyota Prius here, it looks like uh QNX software have got all these funky in-dash user interfaces. It's awesome. Check it out. Whoop. It's not working that well. Internet, there we go. Chumby, home control, fan base. You can operate your your home from your car, I guess. It's got games, it's got navigation, it's got full stuff. Oh. It's got everything. YouTube.

**Dave Jones:** There you go. You can get the EV blog, probably. I don't know. I think it needs some work, but it's pretty cool. There's nothing nerds like better than to win a free iPad. I got this in my kit. Turn up to the Avnet stand, plug in your little key you got, and you can win an iPad.

**Dave Jones:** Just check it out. Come on, guys. Spin Spin. we go. Good luck. I won a USB flash Thanks, guys. Didn't win the iPad. Unbelievable. And it's lunch time, and they've outdone themselves yet again.

**Dave Jones:** Just keeps going on and on, the food. Unbelievable. There you go. I'm on camera with one of the demo boards. It's got a real-time live updating through an SHR processor. Very nice. I like it. A wave. Hello. There we go. It's all real-time.

**Dave Jones:** I like it. And of course every man and his dog's doing a capacitive touch sense uh device and Renesas is no exception. They've got This is their EVK is the capacitive EVK touch kit and it looks quite neat. You can actually prop it up and you can scroll things scroll the number up and you can scroll the number up and down like that and enter numbers. It's all just a glass panel with capacitive touch just like that one with all the different etched patterns on there, the different

**Dave Jones:** button styles and things like that. So, yep, every man and his dog's doing those these days. I found some funky-looking device here. Check it out. What is this thing? Uh this is a millimeter wave camera and it's it's a device that's capable of seeing through solid objects. So, it can see through wood and it can see through gypsum wallboard and this particular version of the camera we're targeting at the construction industry to see wires and pipes and you know, leaks and and things inside buried inside a wall

**Dave Jones:** so a remodeler can go and understand what's in the wall before you cuts it or drills or whatever that he needs to do. So, is it only like a what sort of objects can it actually detect? Like is it only metal objects? Wood?

**Dave Jones:** No. That it can detect wood, plastic, metal, a leak meaning water. It can detect a something like a mouse or anything that contains water. Okay, so I'm I'm to just make a picture of my hand first which is kind of Oh, that is That is your hand.

**Dave Jones:** Yeah, behind the wall. Oh, yeah. There it is. Fantastic. And uh So, now we'll go over there's a there's a stud and I put my fork uh behind the wall and there's a wire coming down. There's the Right.

**Dave Jones:** And we just fork That's a a metal electrical box right there. There's a little piece of uh It's a brass connector. Yeah. And uh there's a wire coming up. Um It's funny. Here's the nylon tie wraps coming up at an angle connected to another stud.

**Dave Jones:** There's a wire coming up going up this way. It's funny. You don't have to take a picture of the whole scene. It uh Yep. Well, it's got it's got on-screen persistence. Yes, it does. some form. That's right. So, there's the the fork and uh my coffee cup uh So, there's a wire coming over and there's a stud. And now I'm going to stop um the antenna from spinning. Now I'm in locate mode so I can go in this little cursor right here and find objects. Like right there is the tip of

**Dave Jones:** the the fork. Yeah, got it. right there. So, there's a locating feature on the device. Fantastic. That's great. Thank you very much. And it's 2:00 on the second day and as you can see everyone's packing up. There goes the house. It's completely gone.

**Dave Jones:** There's nothing left. They've stripped it bare and they're going to completely transform the room for tonight's uh panel. Basically, they're going to have a panel. This will all be transformed by tonight. The people work in the background and they do an amazing job actually transforming places like this after hour from one event to the next.

**Dave Jones:** And there goes the Jeep. The Jeep's out of here. Jeep's gone. Here we go. They're lifting the Jeep out. The Jeep is going.

**Dave Jones:** The Jeep's going into the crate. It'll be shipped out tonight. No, no. They're not going to drive it home. There it is. It's all done. Now they got the Jeep out okay, but I'm not 100% sure how they're going to get the Prius out of here. The door looks a little bit too small and the alleyway out the back looks uh tiny. So, go figure. They'll get it out somehow.

**Dave Jones:** So, you're waiting for me to say something outstanding? Give me a thumbs up. How's that? Awesome. The customer has a strong preference, like your friend. We were uh we were pretty happy. This is it really happens in the bar.

**Dave Jones:** This is where the big deals go down, right? been there. Come back in about 6 hours. Right. That's not alcoholic enough by the looks of it. No, not very much. Ah. Not lubricated enough. Okay, I'll come back later, guys. And the room's starting to transform. It's uh not quite 3:30 yet. So, they haven't It hasn't been long since the main pack up and the room's been transformed into tonight's panel.

**Dave Jones:** Something tells me they're going to Disneyland. I think they're on the shuttle. Yep, they're really getting into the spirit of it. Hey, Mickey! All right, I'm excited. I'm here with Kent Loman from FDI. Thanks for joining us, Kent. Now, I'm excited because you actually designed the new Renesas RX62N uh demo board, which is going to be the next hot the hot item. Tell us about that.

**Dave Jones:** So, this is the rapid development kit or the RDK for the RX62N, which is Renesas' new 32-bit microcontroller platform. Very, very big deal. Very, very large worldwide launch. We worked very closely with their entire team, their applications engineers, the other tool vendors with MeKrim, and all the other tool suppliers to provide a turnkey solution and a development kit to the customer.

**Dave Jones:** So, this is the basis for the RX design contest that we'll be running between now and Embedded Systems San Jose in April. Which we'll both be on the judging panel, I believe. There you go. So, you definitely want to submit an entry to the design contest.

**Dave Jones:** Absolutely, and we'll critique it, shall we? After the first video, I had an email saying, "Dave, what are you doing at a Renesas event? Who the hell are they? You know, what about the big M, the big A, the big T? Aren't they the major players?" Well, if you believe the blurb, apparently, Renesas are the number one microcontroller manufacturer in the world. 30% says here, 30% of the globe More than 30% of the global market. The next nearest competitor is only around 10%. Unbelievable. Who knew? And they're

**Dave Jones:** number one in 8-bit, 16-bit, and 32-bit. Unbelievable. And but apparently they're only number two in the US with number one starting with an F. And well, they ain't doing too well, so go figure. Not surprisingly, response to the first video, I also had endless comments on the money, the paper money, this funny money, US stuff, and how it's just crap quality paper. It's just garbage. The print looks awful, and somebody commented that it smells like well, a combination of feet and ass.

**Dave Jones:** Go figure. That don't smell like real money to me, but these polymer Yes, it's plastic. Somebody asked, the polymer, it's a plastic banknote. Australia's had these since 1988. 22 years. Yanks, get with the program. And you betcha, smells like real money.

**Dave Jones:** Oh, yeah, baby. There are some people who wanted a better look at the note. Well, here it is. Here's the Australian $50 polymer note. All of our notes are polymer. They have been since about the mid-1990s, but the first one was 1998. And as you can see there, they're almost indestructible polymer plastic. You can't rip them. You can't tear them at all. They're almost indestructible. You can fold them a million times, and they just totally recover. You can scrunch them up, and they just They're fantastic. Whereas

**Dave Jones:** this US note, check it out. It's just paper. I can just rip that in half easily. These things just I don't know how many weeks they must last on average, but it's very poor. So, the Australian $50 money note, far superior.

**Dave Jones:** All the notes are the same, but they are different multiple colors, not as ugly as the Euro money, and it is Australian technology. The polymer notes were designed and developed here. But, of course, the US won't buy our technology, will they? No.

**Dave Jones:** And here we go. It's now just a few hours later, and as you can see, the place has been transformed into the dinner event. And what was once the breakfast foyer area is now turned into a gaming area.

**Dave Jones:** They've even got blackjack. Ah, good. A victim. Thank you very much. Ah, it's tough here at Renaissance.

**Dave Jones:** And you're not going to believe it. What was the lecture hall this morning for the keynote is now being transformed into the Renaissance gaming room. Haha, it's nerd nirvana. Check out the huge screens. We've got more gambling, we've got pool, we've got ping pong, we've got large screen Wii. Haha, the stuff of wet dreams, really.

**Dave Jones:** The event hasn't even started yet, and he's already into it. And of course, it wouldn't be complete without classic 80s arcade machines.

**Dave Jones:** And this one's really drawing a crowd now. Must be a bunch of managers trying to outdo each other. It's the engineering management pissing contest. And dinner has gone off, and they're just opening the panels. The panels are actually moving. They're opening those to go into the gaming event. Isn't that awesome?

**Dave Jones:** Renaissance spared no expense again. Fantastic. Apparently my wife plays ping pong. Check it out.

**Dave Jones:** And this is the after dinner gaming event. PEOPLE PLAYING BLACKJACK. HE LOST. HE LOST. AND WE GOT SOME TRAGIC people up on stage. Karaoke, guitar hero. Ah, I don't know. It's tragic.

**Dave Jones:** Anyway, this is how Renaissance do their after dinner parties. Unbelievable. And the video games are popular. We've got Asteroids, Space Invaders, Froggers, and Ms. Pac-Man.

**Dave Jones:** And these are the ones who have spilled out of the main gaming hall into the corridor, which still has gaming. And if you didn't know, we're at DevCon.

**Dave Jones:** Well, not everyone could be at the gaming event. These videos don't edit themselves. Catch you next time.
