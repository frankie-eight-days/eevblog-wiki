---
video_id: MMR-lOm-FfA
title: EEVblog #118 - Renesas Devcon 2010 Day 2
url: https://www.youtube.com/watch?v=MMR-lOm-FfA
source: youtube-asr
timestamps: {"0": 0, "1": 30, "2": 48, "3": 69, "4": 87, "5": 99, "6": 117, "7": 130, "8": 142, "9": 161, "10": 174, "11": 187, "12": 197, "13": 206, "14": 244, "15": 258, "16": 271, "17": 283, "18": 329, "19": 355, "20": 371, "21": 385, "22": 401, "23": 410, "24": 439, "25": 453, "26": 467, "27": 480, "28": 491, "29": 508, "30": 523, "31": 537, "32": 548, "33": 563, "34": 578, "35": 593, "36": 609, "37": 680, "38": 694, "39": 704, "40": 719, "41": 731, "42": 742, "43": 756, "44": 770, "45": 779, "46": 793, "47": 808, "48": 824, "49": 847, "50": 864, "51": 886, "52": 897, "53": 913, "54": 926, "55": 940, "56": 958, "57": 982, "58": 993, "59": 1014, "60": 1025, "61": 1036, "62": 1069, "63": 1088, "64": 1112}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. And it's 8:15 Tuesday morning and here we are in the main lecture hall about to get the keynote address and as you can see it's filling up pretty quick.

**Dave Jones:** Everyone's spilling over for breakfast. Everyone's pumped and this lecture hall will be completely full in about 5 minutes or so. That's the spillage from breakfast. Let's go. We are the largest MCU supplier with 30% market share.

**Dave Jones:** We are also ranked number one in every major segment category such as the 8 16 and the 32-bit MCU products. Number of lectures is crazy. Here's the nerve center for the hardware labs.

**Dave Jones:** This is where they get all their demo boards, put them together, get all the manuals together, program the notebooks, format the hard drives for all the hardware lecture labs and they put them all onto the trolleys and they wheel them out down the hall into the dozen or so lecture rooms they've got.

**Dave Jones:** Unbelievable. I think uh Thomas will comment on the second instruction of this discussion. Well, let's start with 8-bit. The top question is I want to start with 8-bit. I want to do what I do.

**Dave Jones:** What's on the board and if you're not within the um the rated uh minimum input voltage um for high or or maximum for low, if you're in the no-man's land, you can get um both the P channel and the N channel of the internal uh gate turned on.

**Dave Jones:** And that results in current from top to bottom and from VDD to ground. And so, watch out for those. And in addition, the PC board cleanliness itself can be an issue because it can then uh, draw hundreds of milliamps if you don't watch out.

**Dave Jones:** You will need to use more expensive diodes to be able to um, you know, deal with the recovery current. We're at the Renesas uh, one of the Renesas stands and where it looks like we got some power electronics here.

**Dave Jones:** Can you go through and explain exactly what you've got here? Yes, I can. Right. What we have right here is our setup of our our scalable VR solution. And what it is is it's a digital controller functioning with our POL SIP device which is a PWM IC with driver high side and low side FET in one package.

**Dave Jones:** And in this particular package, we're looking at an 8 by 8 device QFN 56 package. That's an 8 by 8 mm device and that's what is IT How much is it?

**Dave Jones:** It can do It can do 40 amps max. 40 amps max. Unbelievable for an 8 by 8 package like that. Amazing. Have it'll tell you what you're looking at in the V out and the temperature and the I out.

**Dave Jones:** Oh, very nice. I'm looking at this as well. going. So, we'll go ahead and just load it up to 80 amps. 80 amps? Obviously, you can see the temperature start to jump up.

**Dave Jones:** Yep. As well as the I out function now at 80 amps. And of course, the best part about these trade shows are the freebies. Check it out. Freebies, right?

**Dave Jones:** You guys give away freebies? Uh, sometimes. Excellent. Thanks. Haha. Slip 114. Score. That wasn't a freebie. Oh, shoot. Scoreless. Ah. Ah. Bring it. Beautiful. It's all good. Inside the Toyota Prius here, it looks like uh QNX software have got all these funky in-dash user interfaces.

**Dave Jones:** It's awesome. Check it out. Whoop. It's not working that well. Internet, there we go. Chumby, home control, fan base. You can operate your your home from your car, I guess.

**Dave Jones:** It's got games, it's got navigation, it's got full stuff. Oh. It's got everything. YouTube. There you go. You can get the EV blog, probably. I don't know. I think it needs some work, but it's pretty cool.

**Dave Jones:** There's nothing nerds like better than to win a free iPad. I got this in my kit. Turn up to the Avnet stand, plug in your little key you got, and you can win an iPad.

**Dave Jones:** Just check it out. Come on, guys. Spin Spin. we go. Good luck. I won a USB flash Thanks, guys. Didn't win the iPad. Unbelievable. And it's lunch time, and they've outdone themselves yet again.

**Dave Jones:** Just keeps going on and on, the food. Unbelievable. There you go. I'm on camera with one of the demo boards. It's got a real-time live updating through an SHR processor.

**Dave Jones:** Very nice. I like it. A wave. Hello. There we go. It's all real-time. I like it. And of course every man and his dog's doing a capacitive touch sense uh device and Renesas is no exception.

**Dave Jones:** They've got This is their EVK is the capacitive EVK touch kit and it looks quite neat. You can actually prop it up and you can scroll things scroll the number up and you can scroll the number up and down like that and enter numbers.

**Dave Jones:** It's all just a glass panel with capacitive touch just like that one with all the different etched patterns on there, the different button styles and things like that. So, yep, every man and his dog's doing those these days.

**Dave Jones:** I found some funky-looking device here. Check it out. What is this thing? Uh this is a millimeter wave camera and it's it's a device that's capable of seeing through solid objects.

**Dave Jones:** So, it can see through wood and it can see through gypsum wallboard and this particular version of the camera we're targeting at the construction industry to see wires and pipes and you know, leaks and and things inside buried inside a wall so a remodeler can go and understand what's in the wall before you cuts it or drills or whatever that he needs to do.

**Dave Jones:** So, is it only like a what sort of objects can it actually detect? Like is it only metal objects? Wood? No. That it can detect wood, plastic, metal, a leak meaning water.

**Dave Jones:** It can detect a something like a mouse or anything that contains water. Okay, so I'm I'm to just make a picture of my hand first which is kind of Oh, that is That is your hand.

**Dave Jones:** Yeah, behind the wall. Oh, yeah. There it is. Fantastic. And uh So, now we'll go over there's a there's a stud and I put my fork uh behind the wall and there's a wire coming down.

**Dave Jones:** There's the Right. And we just fork That's a a metal electrical box right there. There's a little piece of uh It's a brass connector. Yeah. And uh there's a wire coming up.

**Dave Jones:** Um It's funny. Here's the nylon tie wraps coming up at an angle connected to another stud. There's a wire coming up going up this way. It's funny. You don't have to take a picture of the whole scene.

**Dave Jones:** It uh Yep. Well, it's got it's got on-screen persistence. Yes, it does. some form. That's right. So, there's the the fork and uh my coffee cup uh So, there's a wire coming over and there's a stud.

**Dave Jones:** And now I'm going to stop um the antenna from spinning. Now I'm in locate mode so I can go in this little cursor right here and find objects. Like right there is the tip of the the fork.

**Dave Jones:** Yeah, got it. right there. So, there's a locating feature on the device. Fantastic. That's great. Thank you very much. And it's 2:00 on the second day and as you can see everyone's packing up.

**Dave Jones:** There goes the house. It's completely gone. There's nothing left. They've stripped it bare and they're going to completely transform the room for tonight's uh panel. Basically, they're going to have a panel.

**Dave Jones:** This will all be transformed by tonight. The people work in the background and they do an amazing job actually transforming places like this after hour from one event to the next.

**Dave Jones:** And there goes the Jeep. The Jeep's out of here. Jeep's gone. Here we go. They're lifting the Jeep out. The Jeep is going. The Jeep's going into the crate.

**Dave Jones:** It'll be shipped out tonight. No, no. They're not going to drive it home. There it is. It's all done. Now they got the Jeep out okay, but I'm not 100% sure how they're going to get the Prius out of here.

**Dave Jones:** The door looks a little bit too small and the alleyway out the back looks uh tiny. So, go figure. They'll get it out somehow. So, you're waiting for me to say something outstanding?

**Dave Jones:** Give me a thumbs up. How's that? Awesome. The customer has a strong preference, like your friend. We were uh we were pretty happy. This is it really happens in the bar.

**Dave Jones:** This is where the big deals go down, right? been there. Come back in about 6 hours. Right. That's not alcoholic enough by the looks of it. No, not very much.

**Dave Jones:** Ah. Not lubricated enough. Okay, I'll come back later, guys. And the room's starting to transform. It's uh not quite 3:30 yet. So, they haven't It hasn't been long since the main pack up and the room's been transformed into tonight's panel.

**Dave Jones:** Something tells me they're going to Disneyland. I think they're on the shuttle. Yep, they're really getting into the spirit of it. Hey, Mickey! All right, I'm excited. I'm here with Kent Loman from FDI.

**Dave Jones:** Thanks for joining us, Kent. Now, I'm excited because you actually designed the new Renesas RX62N uh demo board, which is going to be the next hot the hot item.

**Dave Jones:** Tell us about that. So, this is the rapid development kit or the RDK for the RX62N, which is Renesas' new 32-bit microcontroller platform. Very, very big deal. Very, very large worldwide launch.

**Dave Jones:** We worked very closely with their entire team, their applications engineers, the other tool vendors with MeKrim, and all the other tool suppliers to provide a turnkey solution and a development kit to the customer.

**Dave Jones:** So, this is the basis for the RX design contest that we'll be running between now and Embedded Systems San Jose in April. Which we'll both be on the judging panel, I believe.

**Dave Jones:** There you go. So, you definitely want to submit an entry to the design contest. Absolutely, and we'll critique it, shall we? After the first video, I had an email saying, "Dave, what are you doing at a Renesas event?

**Dave Jones:** Who the hell are they? You know, what about the big M, the big A, the big T? Aren't they the major players?" Well, if you believe the blurb, apparently, Renesas are the number one microcontroller manufacturer in the world.

**Dave Jones:** 30% says here, 30% of the globe More than 30% of the global market. The next nearest competitor is only around 10%. Unbelievable. Who knew? And they're number one in 8-bit, 16-bit, and 32-bit.

**Dave Jones:** Unbelievable. And but apparently they're only number two in the US with number one starting with an F. And well, they ain't doing too well, so go figure. Not surprisingly, response to the first video, I also had endless comments on the money, the paper money, this funny money, US stuff, and how it's just crap quality paper.

**Dave Jones:** It's just garbage. The print looks awful, and somebody commented that it smells like well, a combination of feet and ass. Go figure. That don't smell like real money to me, but these polymer Yes, it's plastic.

**Dave Jones:** Somebody asked, the polymer, it's a plastic banknote. Australia's had these since 1988. 22 years. Yanks, get with the program. And you betcha, smells like real money. Oh, yeah, baby.

**Dave Jones:** There are some people who wanted a better look at the note. Well, here it is. Here's the Australian $50 polymer note. All of our notes are polymer. They have been since about the mid-1990s, but the first one was 1998.

**Dave Jones:** And as you can see there, they're almost indestructible polymer plastic. You can't rip them. You can't tear them at all. They're almost indestructible. You can fold them a million times, and they just totally recover.

**Dave Jones:** You can scrunch them up, and they just They're fantastic. Whereas this US note, check it out. It's just paper. I can just rip that in half easily. These things just I don't know how many weeks they must last on average, but it's very poor.

**Dave Jones:** So, the Australian $50 money note, far superior. All the notes are the same, but they are different multiple colors, not as ugly as the Euro money, and it is Australian technology.

**Dave Jones:** The polymer notes were designed and developed here. But, of course, the US won't buy our technology, will they? No. And here we go. It's now just a few hours later, and as you can see, the place has been transformed into the dinner event.

**Dave Jones:** And what was once the breakfast foyer area is now turned into a gaming area. They've even got blackjack. Ah, good. A victim. Thank you very much. Ah, it's tough here at Renaissance.

**Dave Jones:** And you're not going to believe it. What was the lecture hall this morning for the keynote is now being transformed into the Renaissance gaming room. Haha, it's nerd nirvana.

**Dave Jones:** Check out the huge screens. We've got more gambling, we've got pool, we've got ping pong, we've got large screen Wii. Haha, the stuff of wet dreams, really. The event hasn't even started yet, and he's already into it.

**Dave Jones:** And of course, it wouldn't be complete without classic 80s arcade machines. And this one's really drawing a crowd now. Must be a bunch of managers trying to outdo each other.

**Dave Jones:** It's the engineering management pissing contest. And dinner has gone off, and they're just opening the panels. The panels are actually moving. They're opening those to go into the gaming event.

**Dave Jones:** Isn't that awesome? Renaissance spared no expense again. Fantastic. Apparently my wife plays ping pong. Check it out. And this is the after dinner gaming event. PEOPLE PLAYING BLACKJACK. HE LOST.

**Dave Jones:** HE LOST. AND WE GOT SOME TRAGIC people up on stage. Karaoke, guitar hero. Ah, I don't know. It's tragic. Anyway, this is how Renaissance do their after dinner parties.

**Dave Jones:** Unbelievable. And the video games are popular. We've got Asteroids, Space Invaders, Froggers, and Ms. Pac-Man. And these are the ones who have spilled out of the main gaming hall into the corridor, which still has gaming.

**Dave Jones:** And if you didn't know, we're at DevCon. Well, not everyone could be at the gaming event. These videos don't edit themselves. Catch you next time.
