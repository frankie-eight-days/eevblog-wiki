---
video_id: X0sT72u_Jl4
title: EEVblog #482 - Retro Iskra Multimeter Teardown
url: https://www.youtube.com/watch?v=X0sT72u_Jl4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, it's retro moldy meter time. Check this puppy out. It's a It's a Digimet 10 from a company called Iskra and it's actually a Yugoslavian made moldy meter. I mean, you know, real retro. It's not a modern design. Check

**Dave Jones:** out those 4 mm banana socket inputs there. Really ancient, but obviously some sort of LED display in there and we've got the manual for it. It was sent by Sylvain. He's an EVBlog viewer. Hi Sylvain, thank you very much.

**Dave Jones:** Sent it into the mailbag segment and we saw that on there and it's even got some tips for using this sucker on the back. There it is and it's in a really quite good nick and we have the full schematic

**Dave Jones:** which I'll link in down below which is in the back of this. Look at this. Got the original manual for it and the foldout schematic. Fantastic. So I'll scan that in and that will be linked down below. Actually, the

**Dave Jones:** circuits are rather fascinating and worth a look. I mean, check out the power supply down here. Look at this. We have a discrete switching power supply. It's even got the switching waveforms down in here. For example, what have we

**Dave Jones:** got? TP 2.1. There it is. Plus five. We've got a multivibrator classic two transistor multivibrator circuit here and that allows it to generate the required supply voltages for this thing. Really quite neat. Our display driver up here. Look at what

**Dave Jones:** we've got. We've got an MC 4511 seven segment driver. Absolute classic and it really LD triple one looks like one of them looks like the main device down here. There's an LD 110 and an LD 111. So, it looks like

**Dave Jones:** it's a two-chip set multimeter. Haven't seen these ones before. I'm going to have to Google that. See if we can get anything on there. And once again, we've got more waveforms down here. I like it. Got some op-amp action down here. Lots of

**Dave Jones:** quite a few trim pots in this thing. I think I can see. We've got one there, one there. We've got a discrete JFET input there by the looks of it. And here's our input. Yeah, here it is over here. Volts

**Dave Jones:** and ohms going in. We've got some yeah, compensated 10 mega resistor there. We've got ourselves another trim pot down there. Another trim pot. Trim pots absolutely all over the place. And this is rather unusual down here. Look, these are these are resistors, but

**Dave Jones:** they've actually Look how they've actually drawn them here like they're inductors or something like that. I don't know. Really weird. Is that common in Yugoslavia? I don't know. Any viewers out there, please let us know. But that's our current input

**Dave Jones:** there. They're a different range switching. I'm going to assume that that means these are wire-wound resistors. So, it wouldn't surprise me at all if we open these up and found a wire you know, wire-wound resistors in there. But why

**Dave Jones:** would you use like a 9K wire-wound resistor up here? I I just don't know. But you know, it it makes sense for you know, the lower current shunt ranges, of course. It's got really nice. It goes down to 20 microamps full scale. Check

**Dave Jones:** that out. Really quite neat. So, it's rather quite a usable meter. I mean, anything that goes from you know, 20 microamps full scale up to 2 amps is going to be you know, is a pretty useful multimeter. 200 milliamps, it's got AC

**Dave Jones:** and DC. I assuming of course, it's not a RMS. It's just going to be average average responding there and yeah, that is quite neat. Goes up to 20 meg, 200 ohm minimum scale, but quite a usable meter for its day. And you guessed it, it's

**Dave Jones:** got a triple 5 timer. Beauty. Check out this legend down here. Here are the different types of resistor symbols that they're using in this. If you've been wondering why they look a bit weird, I said no, you know, look these are carbon

**Dave Jones:** film metal film power resistor. Haven't seen that before using different ohm symbols like that. Once again, is this a Yugoslavian thing? I have no idea. So yes, obviously you know, it needs a plus minus 12 volt rails here to power the main chip set

**Dave Jones:** over here. So those ones operate, there we go. Plus and minus 12. Where's plus? There it is, up there. And if we have a look at some of the specs here, there we go. It's rated for operation at 23° C.

**Dave Jones:** Operating temperature 0 to 55, storage temp. Frequency range for the AC of course, 30 hertz to 20 kilohertz. Once again, assuming average responding powered from four NiCad batteries. There you go. Recharge time 16 hours. Doesn't tell you what the consumption of

**Dave Jones:** this sucker is. It might up here anyway. Standard 10 meg input impedance. They even specify the capacitance there. Three readings per second. Not bad at all. Um settling time 1 second max for all DC ranges. So looks like it might

**Dave Jones:** have a bit of a settling issue there and and maximum potential on the ohms V connector with open sockets plus minus 14 volts. And there's our measurement ranges. Goes up to an impressive 2000 volts DC. I you know, that's very rare to find

**Dave Jones:** that. The only ones I've seen above a thousand volts are an old triplett analog meter I've got here which I got I think goes up to 6,000 volts or something like that. But yeah, very handy. I mean 20 microamps full

**Dave Jones:** scale the maximum reading it can actually go over range just a little bit. But have a look down here. It's actually quite impressive point two percent of reading and point one percent full scale with and it specifies the temp co in terms of the

**Dave Jones:** per 10 degrees Kelvin. Look at that instead of per degrees C. But that's pretty good. You know, even on DC current, you know, point two. Not bad at all. I like it. Point two percent for ohms. This was pretty good

**Dave Jones:** for its day. And there's our block diagram. Nothing really special of course. Got the input attenuator and the ohms to voltage converter for the ohms range, your current shunts and then it's got a the triple five timer in there was obviously operating the

**Dave Jones:** analog to digital converter there with the voltage reference. I didn't have a look what voltage reference and then we've just got a basic BCD to seven segment decoder to drive the LED display and the converter in there and a AC to

**Dave Jones:** DC average responding converter. So let's crack this puppy open and we have some sort of little key lock here on the side. I'm not sure what that does. That does that just No. What does that? What? Whoop. There we go. Oh, that's our fuse.

**Dave Jones:** There we go. Oh, beauty. I like that. There's our fuse. We'll put that back in. There we go. It looks like probably these four feet on the back here. Do they Yep, they pop out. Oh. Oh, hang on. What's that?

**Dave Jones:** We've got ourselves I don't know what that is. They Oh, it's one of those Yeah, I don't know the name for those actually, but uh I might have one of those in my kit. Yeah, there we go. I've got uh one of those, those

**Dave Jones:** little two-pronged ones. The name escapes me at the moment. Everyone's probably screaming at their camera going, "Oh, I know what that is." And uh yeah, well, Okay, no, I need a bigger one. Aha, found a date code. Look at that, 7th

**Dave Jones:** month. I assume it's a date code, 7th month 1980. Yeah, that'd be about the vintage that this then that that's probably what I guessed uh would have guessed, you know, late '70s, very early '80s um at the outside. So, woo, 33 years old, folks.

**Dave Jones:** That's probably older than the age of my average audience. So, yes, this will be uh rather interesting. I mean, it's going to be all uh through-hole, of course. Surface mount wouldn't have uh made its way into something like this

**Dave Jones:** back then. So, I expect uh you know, um I well, I don't know the quality of the construction. I've no idea about uh this brand. Never even heard of it before. And uh but we'll have a look for

**Dave Jones:** a 33-year-old technology anyway. All through-hole, but you know, probably no solder mask on the board or some or anything like that. It'll be uh I think that's done enough. And uh it'll just be like a tin maybe a tinned

**Dave Jones:** um board PCB or something like that. Uh we'll see how the I'm not sure how the uh I'm probably two-ball construction maybe for the LCD, something like that perhaps. Anyway, um it should be fascinating. And I don't expect uh you know, CAT

**Dave Jones:** input rating on this thing and uh huge input protection and isolation slots and all that sort of stuff. No, they didn't care about that sort of stuff back then. Heck, even the Flukes really uh weren't Whoop. Whoop. Better not lose those.

**Dave Jones:** Hang on. Better chase it. Right, here we go. Got them out. And I I wonder if the batteries are still uh still in here. No, they're not. There we go. Ta-da! There we go. There's our four NiCads. I assume it

**Dave Jones:** would uh work off um alkalines as well. Check it out though. This is uh chock-full of retro goodness. Look at ourselves a little shield on the top there. Twang! Got a a couple of adjustment what looks like adjustment uh caps there, probably

**Dave Jones:** for the uh AC uh performance there. And uh what have we got down here? Looks like that's weird. It looks like maybe some sort of something what one of the wire wound resistors. Yeah, there's a monster inductor or wire wound resistor there.

**Dave Jones:** Not sure what's going on there, but uh yeah, basically um two board construction. It looks like the Knight 3 with the LCD with the LCD. That LCD. Sacrilege. Wash my mouth out. Um LED down in there. We'll take a look at

**Dave Jones:** this. This actually could be real uh tricky to take apart. I've got to get all these off and then these have to lift out and then uh the top board. Who knows what that rain switch does anyway. Um check out here. There's our battery

**Dave Jones:** compartment for our four IEC KR23/42 43 um NiCad batteries. And uh there we go. If we have a look at the board down there, it looks like it is uh looks like it is gold plated down there. Hand um drawn

**Dave Jones:** PCB. That looks like it's done with uh uh good old Delo pin or something like that. By the way, it got the original plug pack for it as well. Sylvain sent that in and there it is. It's even an Iskra branded uh

**Dave Jones:** plug pack. Check it out. Fantastic. Oh man, that does smell as old as it looks, folks. Oh, that old electronic smell. So, we'll whip this uh shield off here and uh hopefully we can just uh peel it off layer by layer cuz I haven't

**Dave Jones:** powered this thing up yet. I don't even know if it works. Um Sylvain uh didn't mention whether it works or not. Oops. There we go. And oh, wait. Look at the range switch. Oh, this is a beauty, folks. Check this

**Dave Jones:** out. Have you ever seen such a sort of uh uh you know, sort of slapped together Heath Robinson-ish type um contraption range switch? Oh my goodness, that is that is just really something. Look at those contacts in there. And it's sort

**Dave Jones:** of, you know, we've got these wires just bodged across the board going down there. We got these wires going down here. Big beefy things. They must be carrying the range um sorry, the current. Anyway, let's see. Here we go. It's

**Dave Jones:** about to pop up. So, we'll be able to see this contact here now pop into place. Ready? There we go. So, that one just Oh man. That is really that is really something. Look at that. Wow. That is That is bodgy brothers. But

**Dave Jones:** actually, the more I look at that, the more I think, "Well, that's a you know, that is rather clever. I mean, you know, it looks all bodged together up the top here, of course, but the actual uh arrangement itself there um isn't

**Dave Jones:** that bad. I'll see if I can Let's see if we can uh switch You see it? Look at that. You know that That's actually just really quite quite nice. The more I look at that, the more I think, "Yeah, that's really

**Dave Jones:** rather clever." Look at that. Somebody had fun anyway uh designing that. And we have all uh gold plated uh tracking there, of course, very reminiscent of uh say the early um HP uh gear and stuff like that. Um that's, you

**Dave Jones:** know, you don't uh see that anymore. You can't just uh you know, piss away the gold uh these days with gold prices the way they are. But, of course, all of that is uh hand taped, of course, back

**Dave Jones:** on the old uh you know, in the days of the uh light boxes and stuff like that, when you put in the curly traces and everything else. Beautiful. You don't see that anymore these days. And because the nature of how these boards are

**Dave Jones:** wired together like this, they've got the wires going uh down between the two boards like that, and then wires, and then uh and cables um snaking over the top like that. And they've got the same Heh. Love this uh ribbon pink ribbon.

**Dave Jones:** First teardown that contains a pink ribbon. Make of that what you will. Um and of course, they've wired these boards together like that. So, it's it's really not designed to come apart, and I'm really uh quite hesitant to take those boards off,

**Dave Jones:** but I'll take um these Take these nuts off and see if the entire sort of assembly uh lifts out. But, yeah, I don't really don't want to go uh cuz I haven't powered this thing up. I really want to see

**Dave Jones:** um what it's like. But, yeah, don't Oh, man. It's like I really don't want to don't want to ruin the sucker. There's the other No, what's that? I thought that was a switch. No, that's like some big-ass inductor down in there.

**Dave Jones:** Monster. But, uh yeah, this is probably the one of the most difficult multimeter teardowns I've ever done because it's just uh so hand-built and just man. Not designed to be mass-assembled. Designed for manufacture. What's that? Just build it and ship. And

**Dave Jones:** in there, you can see your traditional uh PCB mount range switch with the uh like a wafer uh type switch there. Uh contact switch going between the etched uh gold-plated things on there. And it looks in really good nick, actually. So,

**Dave Jones:** uh I'd be surprised if this thing uh uh doesn't uh work anymore or in that's a you know, probably still within spec. So, before I actually uh attempt to take this apart, I will actually power it up. So, I've got uh external 5-V uh supply

**Dave Jones:** there hooked onto the battery. So, uh hopefully, let's give it a go, shall we? Let's put it Does that the voltage of the battery, I guess? Let's turn it on. Hey, there we go. Yep. There you go. It works. 5.07. Um well,

**Dave Jones:** my power supply is showing 5.00, but I could measure that with a multimeter and see which one's more precise. No, there you go. It's a little bit out reading the battery. Ah, well, you can't have everything, but uh

**Dave Jones:** there you go. It seems to be working a treat, at the very least. Awesome. And what do you know? I've got that hooked up to my uh calibration lab calibration standard here set to bang on 2 volts in fact

**Dave Jones:** 2.00000 volts and we're getting 1.997. That's within spec. And by the way, if you want to know the current drawer, just over 200 milliamps there. So, there you go. That is fantastic. Ah. It's a thing of beauty, joy forever.

**Dave Jones:** Let's overload it. Ooh, flashing, flashing, warning Will Robinson, warning. Let's measure my resistance standard here. It's like 0.005% good enough to measure this puppy and it's really good these are dual adjustments. I haven't used a multimeter like this in a

**Dave Jones:** long time. And yet, you know, you move it around here, it's annoying, it doesn't work at all. You've got to actually switch it over to ohms and we're bang on. We are bang on, folks. Not a problem whatsoever.

**Dave Jones:** Awesome. This thing 33 years old. Ah, can't beat Yugoslavian technology. There you go. 1K. Let's switch it down. There we go. That's pretty good. That's pretty good. I'll give that a win. And if you put the leads open, there we

**Dave Jones:** go. It just goes full scale and just uh flashes at you. And of course no continuity buzzer. And there's something seems to be something wrong with the current range here. I've got it on 200 microamps there and it's uh

**Dave Jones:** flashing its digits at me. And shouldn't be doing that cuz I'm only feeding 10 microamps there. So, really I don't know don't know what the deal is there at all. And well, 2 milliamps, yeah, there it is. 10 microamps. So, the 2 milliamp

**Dave Jones:** range works. So, let's wind the wick up on my Keithley current source. No. No. No. No, that's not budging. No, there's something that's supposed to be like 100 milliamps. No, there's something wrong with that. But that's pretty cool that

**Dave Jones:** that puppy still works. So, let's see what happens if we try and take these boards out. Actually, there's another shot of the contacts down in there and they've got numbers on them, which is rather quite neat. And you can see those uh

**Dave Jones:** It doesn't seem to be uh much if any wear on these contacts at all. Very, very nice. But, you know, it's almost as if like these have been budged on as like a you know, an afterthought or something like that cuz that you

**Dave Jones:** know, cuz that range switch construction is actually rather quite nice. We might get lucky. The range switch looks like it's just going to pull straight off. The screen The LED display's coming out. So, I better I don't know. Hang on. Uh

**Dave Jones:** Yeah. Sorry, I'm not keeping that on camera. Too busy worried. There we go. Look at that. There's a range switch down in there. There it is. I better like leave it in the correct position. But nice balls in

**Dave Jones:** there. I love a multimeter with a good set of balls. Interestingly, that uh red Perspex window is not held in with anything. It just just sits there. Well, if it did have some glue on it, it's worn off with age. And there we go. We

**Dave Jones:** have our LED display and the top of the board. Look at that. Intersil chips, check them out. There we go. Look at that. Well, they're bright. The LD 11 and there's our triple five timer. Beautiful. Yeah, my, confirmed our

**Dave Jones:** manufacturing date, 20th week, 1980, 25th week, 1980. Fantastic 4511 LED display driver. Oh, look at that. We've got ourselves a, uh, looks like what was supposed to go to a shield, and you can see the mark. Ah, it is. Has that got that shield in? Look

**Dave Jones:** at that. They've actually exposed that. And that is like a, like a nickel shield or something like that. Yeah, there we go. That's for real, folks. Excellent shielded front cover. Brilliant. Now, as for the, uh, input sockets, they've actually manufactured that as a,

**Dave Jones:** uh, complete assembly. Look at that, screwed it down to the board. Not bad at all. They've even put the identifying marks on the PCB. Nice attention to detail. Excellent. There's some, you know, wiring attached directly to that. I mean, check that out. Big beefy wiring

**Dave Jones:** going, well, somewhere. Does it actually snake under there? And is that the one that pops out? No, they've got that going to there. That looks like almost, no, I thought it was, I thought it was, that was like a little bit of

**Dave Jones:** coax. Sorry, got off camera there. Thought that was a bit of coax going across there, but it's, uh, it's not. And, uh, Oh, look. We have ourselves, is that a, no, I thought it was like a thermistor, but it

**Dave Jones:** looks like it's a tantalum that they've just bent over on the board. Look at that. Oh, that's hilarious. So, that looks like a 16 mic, uh, tantalum, 35 volts. The, uh, the old, uh, dipped, uh, tantalum types, and they are notoriously

**Dave Jones:** unreliable. They're horrible little beasts. There's a few of them in here. Looks like there's a couple over there as well. They are yeah, absolutely horrible little things and uh uh I'm surprised that it still works, but look at that

**Dave Jones:** sucker. Wow, look at that. We have our That's our wire transformer. That's our DC to DC uh converter transformer that we saw on the schematic before. That's being driven by BFJ64 transistors there. Massive can package, look at that. Ah.

**Dave Jones:** This is like really home-built stuff. Then we got some, you know, traditional uh carbons there with sort of like um just uh you know, the brush painted on type. They would have just had the They spun the resistors on there and just

**Dave Jones:** painted that uh uh painted those um uh color code rings on and then uh lacquered them and ah man, that's just it's just classic. I love it. Look at that really old-school stuff. Unbelievable. I mean, you know, it's not a thing of

**Dave Jones:** beauty, really. It's It's pretty darn horrible. And just below our sockets there, there's our big beefy 10 meg input resistors down there. Absolutely massive. That's our uh LED display. Standard up pinout. I love the tape. Uh the taped artwork there just

**Dave Jones:** going connecting those displays up. Ah, brilliant. That brings back a lots of memories, let me tell you. Individual uh digit um uh driver transistors there in your classic uh plastic package there instead of you know, these I don't know why they

**Dave Jones:** got these metal can packages down there. You know, they're obviously power transistors. And there's our function switch there. Look at that, you know, all sort of all custom made PCB contacts down in there. And the boards join together. I mean,

**Dave Jones:** I'm not going to take these boards apart. I don't think it's worth it. Um I'm sorry, but I really, you know, I I really like this little multimeter. It's classic and I'd hate to have to just desolder everything and rip

**Dave Jones:** the damn thing apart. I don't I don't think it's worth it. Um I don't know. Maybe I'll run a poll on the forum. Who wants me to tight strip the thing down and really, you know, I I can't see a huge

**Dave Jones:** benefit in that cuz we can see, you know, most of the hideous construction in this thing. But I guess it wasn't too unusual for its day. I mean, you know, actually let's do an interesting comparison to my old Soar

**Dave Jones:** ME-533 digital multimeter. This is the first digital multimeter I ever got. It was a hand-me-down when I got it and yeah, it's served me well for many many years. Unfortunately, the screen is cracked now and I do remember, but I cannot find

**Dave Jones:** this. I'm going to have to go through my old collection of Electronics Australia magazines, but I've talked about this before. This was the multimeter that was used, I believe, the same one that was used in a Fluke ad of the time

**Dave Jones:** advertising the Fluke 70 series and the slogan was how to beat the high price of cheap multimeters and this was like it was beat up and it had tape all over it and all sorts of stuff. So this was the

**Dave Jones:** cheap cheap multimeter that Fluke were comparing it to and yeah, I remember seeing that ad and going almost crying because well, this was my pride and joy back in the day. I'm not sure of the age of this. Let's open and

**Dave Jones:** find it out. I I there's not much in there. This is basically a single chip. Um I do remember taking it out. It's like a single chip solution that does everything, but you know, really um old school, you know, end on resistors

**Dave Jones:** there. They've just used like an off-the-shelf um rotary switch there, you know, pretty crusty. Ooh, look. We have some MOV input protection. Wow, stunning. But uh yeah, put some tape around there to pull the fuses out. Obviously, some battery

**Dave Jones:** leakage there, but let's uh That's, you know, this is like a big contrast in terms of um you know, the system integration in the single chip multimeter, but I think this is not um too dissimilar age. So, let's see if I

**Dave Jones:** can pop that off and have a look at the chip. Get a date. Here we go. I got the sucker off. It looks like I had uh put some tape on there cuz yeah, I kind of remember that. That's uh I put some like

**Dave Jones:** uh plumber's tape on there, I think, because the the shaft of that was just one of those uh uh fluted um shafts, and uh it my knob fell off, and I I fixed it. Oh, yeah, tada. There we go.

**Dave Jones:** Look at that. Oh. But um yeah, I mean, you know, streets ahead in terms of uh integration and uh technology and uh construction and everything like that. By the way, this one had the unique ability to do uh low ohms um measurement

**Dave Jones:** as well. So, it wouldn't turn on a diode junction. Really quite uh neat for its time. And uh there it is. There's my poor old sore multimeter. What's the date on that chip? 9773. Well, I can guarantee you that's not a

**Dave Jones:** date code cuz this thing wasn't manufactured in 1997 nor 73. Brings back so many memories, so many measurements. And that's actually rather neat how they've mounted that uh LED display board there on that angle. They've just sort of done a

**Dave Jones:** cutout in that PCB there just what and it looks like they've beveled it just wide enough for that to for that board to slip in at a certain angle. And if we have a look under the display board here, I took off the two screws on

**Dave Jones:** top there. Ta-da! There's our other chip and look, it's mounted in um those free standing machine pin sockets. Look at that. Oh man, it just it gets bodgier every time you look at this thing. Unbelievable. So, that's the LD111

**Dave Jones:** down in there with the uh LD110 on the top, but oh man. So, there you have it. I think we'll call it quits on this Yugoslavian multimeter, but look at that. Uh have you ever seen multimeter construction like that? That is great. Oh man,

**Dave Jones:** unbelievable. Anyway, thank you very much uh Sylvain for sending that in cuz that is terrific stuff. And it's a Digima 10 Iskra multimeter. Now you know, bit of pub trivia there. Uh name a 1980s vintage Yugoslavian multimeter. Ah,

**Dave Jones:** that's easy. It's an Iskra. And that is cheapo retro multimeter porn at its finest. I love it. If you want to discuss it as there are many uh vintage multimeter aficionados on the EVblog forum, but that is the best place

**Dave Jones:** to do it. The link to individual forum threads for each video is down below. That's down there if you're on YouTube, maybe up there if you're watching on the blog uh website if you watch the embedded video. If you're watching the

**Dave Jones:** podcast version, we can't link it anywhere. Tough luck, you have to just type it in manually. And yes, I'll scan the schematic for this thing, so you can take a look. If you like teardown Tuesday, please give it a big

**Dave Jones:** thumbs up. One thumb up, two thumbs up, I don't care. Or if you don't like it, you can give it a thumbs down. Whatever. Catch you next time.
