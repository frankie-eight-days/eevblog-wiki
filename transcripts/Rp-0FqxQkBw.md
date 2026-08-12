---
video_id: Rp-0FqxQkBw
title: EEVblog #1203 - REPAIR: Tektronix 2465B Oscilloscope
url: https://www.youtube.com/watch?v=Rp-0FqxQkBw
source: youtube-asr
---

**Dave Jones:** Hi, it's vintage Techscope time. You may remember these. Somebody sent these two classic Tektronix 2465 scopes. One's the original 2465 and one's the 2465B, the coveted 2465B. Some say many say the best analog oscilloscope ever made. Argue down below

**Dave Jones:** in the comments. Now my recent visit by Nobel laureate Barry Marshall I'm not sure. If you haven't seen that video, seriously, even if you don't think you'd be interested in hearing a Nobel Prize laureate's story, trust me, it's really good. Everyone who

**Dave Jones:** watched it thinks it's absolutely fantastic. I'll link it in at the end. Anyway, he's a tech a vintage tech buff as well as having a Nobel Prize. And he's actually got a 2465B. And he, you know, he loves these things.

**Dave Jones:** So, it reminded me of the 2465, the two of them, that I've got here. Sorry to whoever sent this in. I forget your name. It was a couple of years back. I've had these sitting on my shelves in the background in my mailbag

**Dave Jones:** segments for quite some time. And they both are scrap units. But I thought I'd pair them up and see what the status is cuz I can't remember. I think one of them had a power supply hiccup, the other didn't. This one has no trace

**Dave Jones:** written on the inside of it and it's scrap. And the both of them don't have cases on them. But I thought it's worthy of actually having a look, see if we can fix this. I'd much prefer to get the the

**Dave Jones:** newer one, the more modern B series one going cuz it's 400 MHz as opposed to 300 MHz. I do like the classic blue screen on this. I don't know why this is the red this like like maroon kind of color.

**Dave Jones:** It looks I don't know. I just don't like the look of it. Much prefer this one down here. So, I'm not sure the history of that change or not and the graticule changing like that. Anyway, if you do know, please let me know, but

**Dave Jones:** absolutely classic scopes and they're worth taking a look at. And yes, I do I did upload the video on the second channel, the Tektronix, the ancient What is it? 465 or 475? And that's a sort of like in progress repair. But if I'm

**Dave Jones:** going to spend the hours on it, I'd probably rather spend some time trying to get the 2465B fixed. So, let's power it up. Have a look. Now, if you have a look inside both of them, this is the newer B model,

**Dave Jones:** this is the older one. You can see no trace scrapped. Somebody's written that on there. And they they basically have equivalent power supplies. They look absolutely equivalent. They have the same interface, all that sort of stuff. But of course, this one looks more modern

**Dave Jones:** because it is. And everything looks very similar between these units. But this one, the older one, does have an extra card on here. I believe that's entirely integrated in the processor board on this one. But apart from that, they are

**Dave Jones:** very similar. Now, as far as the main processor board goes, I don't even think I need to tell you which one is the more modern one. It's obvious with all these surface mount down the bottom. And look at all the

**Dave Jones:** beautiful through hole resistors on the top, though. Look at that. That's just a thing of beauty. It's joy forever. But anyway, the new modern B one, it's all surface mount through hole rubbish. And And what's the processor? An SC6712.

**Dave Jones:** What's that? I'm not entirely sure. Anyway, yeah, the Dallas Semiconductor, that the non-volatile one, 19 This is 32nd week, 1990. So, we're talking 30 years now. So, jeez, Um, yeah, that battery will be no good, but anyway, um, that's the least

**Dave Jones:** of our concerns now. So, we're looking at uh getting a trace up and running on this thing. And the older one is '94 vintage. You can Well, they're the ROMs uh '80 '84. '84. Sorry, I was looking at that I was

**Dave Jones:** looking at '94 '95 there and I thought, "Geez, that's pretty recent." No, the other one's '84. Wow. Okay, 1984 and you can see the numbering on the chips as well, 1984. So, yeah, that's quite a significant difference there. So, an extra 6 years

**Dave Jones:** and an updated model, that makes all the difference. And as for all the uh analog stuff on the bottom with all the custom heat sinks, look at all these custom heat sinks. Every one of these is a custom jobby. They're near identical.

**Dave Jones:** There's a few differences like, you know, immediately spotted like this down here. Like it's got a little ground link and uh one resistor, this one's got a ground link and a couple of diodes and a bunch more resistors, but apart from

**Dave Jones:** that, you know, the layout this one's got an extra trimmer in there, does it? There's, you know, there's a few differences, but largely the architecture is very similar. So, maybe they could uh So, obviously I could possibly use one

**Dave Jones:** as a parts unit perhaps. So, definitely, if you're going to repair these, having like obviously it'd be ideal to have a like the same model, but should be able to at least salvage some parts if we ultimately need to on the

**Dave Jones:** uh from the A unit. So, I'm All the tech buffs out there. And by the way, no, I am not going to consult I should. If you're going to repair these, I highly recommend you consult like the Tektronix uh repair Yahoo group and

**Dave Jones:** stuff like that. Um, they will be screaming at me uh during these videos that, "Oh, that's obviously that capacitor there. It's all that diode, that transistor fails all the time. Everyone knows that. Well, yeah, okay. I'm just going to wing it.

**Dave Jones:** Sorry. Can see small little changes like these have discrete wiring just going to headers from the controls, the knobbies on the front. Whereas this one over here, the newer model, looks like it has flat flex on there. So, they just some,

**Dave Jones:** you know, sort of tidy up improvements in terms of manufacturability. And from the side, near identical as well. These board has changed, but the functionality hasn't. The wiring, I'm sure the wiring's even all the same. So, yeah, they've just

**Dave Jones:** changed the I don't know, changed the pots over, but it looks looks similar. All right, here we go. I'm going to power up the new 2465B. A lot of people will recommend, "Don't power it up. Just go in and

**Dave Jones:** automatically change all the caps and la la la." Yeah, okay. Okay, here we go.

**Dave Jones:** All of the lights come on. That's good. Will they go out? I do remember when I used to use one of these babies, they used to come on as a power on test, but they ain't going off. No, it shouldn't take that long.

**Dave Jones:** Can see it if I turn lights off. There we go. That's nicer. Annoying thing about this power supply, they don't really have any test points marked as such. No voltages marked on there. Ah, terrible, Muriel. We have some crop

**Dave Jones:** circles. I'm not saying it's aliens, and I can't see any marked voltage test points on this board. Maybe there is one, I've missed it, but can't see diddly squat. I'm sure the service manual has it all covered, but jeez, you know,

**Dave Jones:** put it on the silk screen, please. All right, do we have 5 V on our board? Let's go across a random chippy. Yep, 4.97 5 V rails are all right. Presumably, that's why all our LEDs are lighting up cuz they'd be under logic

**Dave Jones:** control. Just for kicks, let's plug in the the older 1984, was it? 85 Yeah, 84 83 model. Let's go. Oh, it's hiccuping. I hear something hiccuping. Tick. Tick. Tick. Tick. This scope will self-destruct in 10 seconds. Now, upon a

**Dave Jones:** close visual inspection of the board, check this out. We got some corrosion on these parts around here. That's a resistor of these two caps. I reckon these electros, they're looking pretty sick. So, I reckon they've spewed their guts

**Dave Jones:** everywhere. Mhm. And there's the same cap up on the other end of the board. That looks a bit crusty rusty, too. So, yeah, I suspect caps are gone. Well, you're not going to believe it. All of the test points, voltage test

**Dave Jones:** points, are on this 14-pin DIP socket here. Who would have known? J119. Yes, I had to read the service manual to find out. Although, if you follow the money, those pins down in there, they actually are what go through to the

**Dave Jones:** power supply board on top, but they're not really labeled anything. You can physically follow them. So, yeah, really had to RTFM to know what these uh supplies are. And sure enough, in our service manual, ridiculously comprehensive, I'll link it in down

**Dave Jones:** below. Crazy. Anyway, let's measure all our test points. So, these are all the not in order, which is kind of annoying, but these are all our different rails on here. So, let's measure those. We already know the digital plus 5 V

**Dave Jones:** digital seems okay. I'm not measuring ripple yet. I'm just making sure they're in the ballpark. Okay, pin one, minus 15. That is minus 15. Surprise, surprise. Uh pin two, digital plus five, already measured that. Yep, it's good. Four is

**Dave Jones:** plus 10 volts. Oh, bang on. Look at that. Well, one least significant digit out, but come on. Minus five volts. Winner. Six, plus 15. 15. Wow, that is bang on. Eight, plus 87 volts. Now we're getting high. Bang on.

**Dave Jones:** This is ridiculous. Uh surely one of them's got to be failed. Nine, 42.4. 42.3. Oh, it's a little bit low. It It does tell you the tolerance on here, by the way. It is within tolerance. 11 is minus eight.

**Dave Jones:** Lucky last, analog plus five on 12. Wow. Winner, winner, chicken dinner. All of our power supplies on this uh fine and dandy. Doesn't mean you wouldn't go in and fix the caps or anything like that, but all of our LEDs

**Dave Jones:** on the front uh just on. So, it's not going through the sequence. I might re- read the manual and see if it says anything about LEDs stuck on, but yeah, anyway, we do know we have some uh dodgy

**Dave Jones:** caps on there, and that non-volatile SRAM, uh that's got to be goneski. By the way, you might be able to see down in this power supply, there's a rifa madness capacitor down in there. Oh, in fact, there's two of them.

**Dave Jones:** You see another sneaky one down in there. Um yeah, I'm going to want to replace those, but right at this moment, uh no. Yeah, I need to solve the digital problem. Now, as it turns out, there's actually a whole set of comprehensive

**Dave Jones:** uh tests when this thing powers on. Uh let me turn the lights off. There we go. And uh they are indicated by not only on the CRT um like as in text on the CRT, but obviously our CRT isn't working

**Dave Jones:** here. In fact, I Well, beam find? No. Zippity doo-dah. Nothing's read out intensity. No. So, no. No good. Even the scale illumination's not working. So, yeah. No, that's one sick puppy. But, anyway, um they it does uh kernel test

**Dave Jones:** first, like basic kernel test, and errors are indicated by various LEDs uh lighting up on the front panel, but I don't see and then it goes into more uh routine uh like more thorough uh tests of all sorts of uh stuff, but um I can't

**Dave Jones:** see anything where all of these are lit up. It doesn't say anything about that in the manual. So, are are they actually on or are they just bleed through from the other can't really tell. It does take time, so

**Dave Jones:** obviously the processor is doing something cuz the processor has to drive the Oh, saw something on the screen there. Did we? Yeah, look. Got something. Wow, okay. That's Wow, yeah. All right. It doesn't say anything not that I could find about

**Dave Jones:** all the LEDs lit up, so mhm. Is that the RAM? So, I'm just going to measure the uh ripple on the 5-V digital cuz that's all we care about at the moment. So, I'll work on an AC pin two.

**Dave Jones:** The spec is 150 mV peak-to-peak ripple, and we're getting what, what, 350 mV. So, yeah, our 5-V rail has got a lot of ripple on it. That would explain a bit. Okay, I just want to have a look at that ripple with the

**Dave Jones:** scope. We're at 200 mV per division. So, yeah, uh there's your problem. We're only supposed to have 150 mV peak to peak. So, our ripple is absolutely enormous. Uh whether or not that's causing an issue, I don't know, but that's really not even

**Dave Jones:** in the ballpark compared to the total spec there. So, yeah, you'd probably want to fix that first before troubleshooting further. I've got to say, they're getting this power supply out of here is pretty horrible. It does actually slide out if you undo some

**Dave Jones:** screws at the bottom there, but then some of the wiring, especially to the voltage selection switch on the back, they've got little spade terminals that have to be lifted off the board in this direction, but they're hidden behind

**Dave Jones:** here. And to get these uh it's just a it's a mess. Don't like it. Tada! We've got a big strapping earthling there. Uh Mhm. It's been how you doing? Ooh, and there they are. They don't look in good nick. Look at that. It just

**Dave Jones:** looks just looks all cracked or whatnot. Yeah, I'd be just sucking those out as a matter of course. Anyway, what we're really interested in is the 5-V rail here cuz we want to solve our digital problem first. So, that's going to be

**Dave Jones:** our 5-V main supply under there. Um there's our big DC input filter caps after the bridge rectifier cuz this is a switching converter, obviously. And there's another sneaky bugger down in there. And yep, that's genuine Reifer madness. And there's a

**Dave Jones:** thermoelectric mechanical switch in there for measuring the temperature of the power train is on that heatsink. I love the casings on them. Look at that. Three power trains there. Anyway, that's just in short that'll just auto cut off

**Dave Jones:** uh the supply where if that heatsink over heats. Now, of course, the really annoying thing about this is that the connectors are labeled on the silkscreen. You know, you got your J's, fine. But as I said, there's no voltage test points uh like

**Dave Jones:** well, there's no like voltage marked test points or anything like that. But all of your capacitors, these aren't labeled. Like, you know, C100 or whatever. You've got to actually go and and get the service manual and schematic and get your board

**Dave Jones:** overlay, which is like, okay, well, fine. Okay, the manual's ridiculously comprehensive. Like, hats off. They just don't make them like they used to. Absolutely fantastic. But yeah, you've got to go in and get your overlay. So, uh it's kind of

**Dave Jones:** it's really annoying. Anyway, uh what we're interested in here is our 5-V regulator. Here it is. And C and our output cap C1280, that's our 5-V rail. Okay, I like this that it's labeled C1280 like this to match uh Q1280 up

**Dave Jones:** here. They label them in sections. That's a trap for niceties. I think I covered that in my um good schematic design practice video, didn't I? If I didn't, well, it should have been in there. Um yeah, like match them group

**Dave Jones:** label like this. Cuz, you know, if this was Q1280 and this was C uh 101 or something like that, it you know, it's just not as nice. Have them match up. Anyway, so uh we will check our output

**Dave Jones:** cap, but also um because the ripple, this isn't going to be a magic ripple rejection here, we're going to uh look at um this one, which is the plus 5-V unreg here. The printout didn't show it. So, we jump over to here

**Dave Jones:** and sorry for crudity of this, but if we have a look at the 5-V unreg down in here, I think it's that one, C115 there. So, we've got a 250 mic cap down in there. So, that's the input side to

**Dave Jones:** the unregulated one. So, we want to check those two caps. They're probably dead as a dodo. So, C115 there, it's that puppy and which is different to these ones. These are brown ones. These are probably lower ESR ones. So, this would be a 5-V

**Dave Jones:** cap. That's our unreg cap and the other one and then C1280 is there. So, we've got a flippity doodah and C1280, which one is it? That puppy there. But, because they're all identical like that, you know, if you got one fail, you would also suspect

**Dave Jones:** and measure the others. And a lot of people will go and go, "Oh, well, bugger it. I've got the board out. I'm replacing every single electrolytic in this thing." It's like it's already like What is it? 35 years old or something.

**Dave Jones:** And yeah, I I don't blame you. So, I don't know if I want to do that. I just want to get the 5-V rail. I just want it to sort of see if that's causing the problem of like not booting up, so to speak. So,

**Dave Jones:** one side of the board flips out here and wow, look at that burn mark from that regulator. Isn't that terrible, Muriel? Um yeah, well, it obviously gets hot, but um there's no indication that that one's failed at all cuz all our

**Dave Jones:** rails measure just fine. So, no worries. Anyway, want to suck out that. I'm just going to measure it first if I can measure anything in circuit, anything funny business and we'll get that out. And they've got a shield between here as

**Dave Jones:** well, which is actually connected, but yeah, more more burn marks down on there. Oh, somebody's had a Hang on. Is that a hairy hacker? Somebody's or they they just hand done. Look. There's a bit of a hairy hacker down

**Dave Jones:** there. With the they look botched on and all the flux residue, it doesn't look like any of the others. Were they done by hand at production time? I would be I don't know. Maybe. Hmm. Does anyone know? Oh, no, check it out.

**Dave Jones:** Look, the row of these caps here, we think that one's failed on the file suspect. Look at that. These ones are fine. These have got the original uh, wave soldering on them. That one's a hairy hacker. So, yeah, someone's had a

**Dave Jones:** go at this. Okay, we'll just do a crude in-circuit ESR here at 100 kHz. So, it's Sorry, it's this one over here. This is our 5-V one. This is our suspect one. 0.3 0.27 ohms. That sounds pretty good.

**Dave Jones:** Let's measure the other ones, which are all identical type and value. 0.29. Yep. That's good. That's good. There you go. So, they're all the same. So, oh, hang on. Just got to pierce through the flux there. That's where you need sharp

**Dave Jones:** probes. There you go. So, all those ones look They're all the same. So, you know, you wouldn't really uh, suspect that. You might suck it out and give it a more thorough test, but I would say that one's okay.

**Dave Jones:** So, that that's the output capacitor, the output of the regulator. So, the other one is this one here. 2.9 almost 3 ohms. So, I suspect that one might be cactus. That would explain it, the uh, pre-regulator one. So, yep,

**Dave Jones:** let's suck that out. Well, something is very wrong here. I sucked that out and it's only a 10 micro Farad 160 volt cap. Nippon Chemicon. But, what the what what? It's supposed to be a 250 mic like and you don't

**Dave Jones:** expect like 10 volts or something. This is ridiculous. I definitely have the correct capacitor. Look, there's two there. There's a third one up there. There's two here, a third one up there. C 111 5 and like what the

**Dave Jones:** This is the same board. I'm I'm sure this is the same board. What the heck's going on? Wow, you're not going to believe this. There's actually an error in the manual. Believe it or not, whether or not they fix this in the

**Dave Jones:** error in later versions, I don't know. But, C 1115 and C 1132, it looks like they're swapped on the overlay here. Because I was tracing out the board here. I was like I was tracing out and it's supposed to go to this 5

**Dave Jones:** volt it was supposed to go to this inductor over here and it didn't make sense. It was going to this cap here and it was just it was crazy. So, yeah, they actually swapped these two caps. So, I

**Dave Jones:** googled this and sure enough, yep, up comes the EV blog forum. Howard Long, who's a long time contributor on there, he discovered the same fault as well. And yeah, the the bloody service manual is swapped. So, there's nothing wrong with that cap, of course.

**Dave Jones:** And measuring that sort of ESR for a 10 micro Farad 160 volt cap is just fine. So, that's the 5 volt jobby there. So, that's the culprit. I need to solder that back in and suck that one out. Unbelievable.

**Dave Jones:** And that dodgy little sucker which somebody has had had a hairy hacker at, 25 ohms at 100k in circuit. So, yeah, let's suck that little turd out. And is that an original or not? I suspect not. And she's about 22 ohms

**Dave Jones:** out of circuit. That's too high. And 1.5 microfarads, 1,500 nanofarads for all you nanofarad fanboys. Yep. That would explain our poor pre-regulation on that thing. And of course, all that ripple is just Oh, he's dropped on the floor. All that ripple is passing

**Dave Jones:** through the regulator onto the output. And back at 100 hertz, 142 mic. Yep, that's no good for a 220 mic. That's way under. It's goneski. Now, I've replaced it with a just a generic one hung low brand 330 mic

**Dave Jones:** 25-volt cap. And well, yeah, I know I shouldn't do that, but that's all I've got at the moment. So, the lab is an absolute mess. I I just want to get something back in there that's going to get that 5-volt rail operating again.

**Dave Jones:** And just for now, I want to put it back in. I won't bother replacing any other caps in here. Just looking at the 5-volt rail. One thing at a time. And of course, you wouldn't do this if you were

**Dave Jones:** experienced with these sort of things. You'd go Oh, like you'd have kits that just replace all the caps and see, you know, like stuff like that in this old bit of gear. But, for the purposes of this video, please do not comment about

**Dave Jones:** it down below. Just for the purposes of this video, I want to see if just changing that one cap makes a difference. Okay, let's see what happens. I haven't changed any of those leaking electros on the main digital

**Dave Jones:** board. Just want to solve that power supply problem. So, here we go. Now, lights are different. Lights come on. No? They come on before. They're They're all on again. Bummer. Okay, well, that could still be the uh the electros on there. So, let's have

**Dave Jones:** a look at the ripple. All right, we're 200 mV peak-to-peak again. Let's power on. Whoa. No. It's still cactus. That's no good. So, I sucked out that secondary cap or a like the output cap uh 0.22 ohms. That sounds pretty good. That's

**Dave Jones:** what we had uh before. So, let's go to uh Let's change our frequency back. 100 microfarads. And that's still Oops. Off camera. 100 microfarads. That's what we expect. So, that cap's actually in good nick. It's a Nichicon. All right,

**Dave Jones:** so I'm going back to these other caps here, which have all been sucked out. So, let's have a squirt like I I think I might just go in there and replace the blinking light. Somebody Something could be uh bleeding over to

**Dave Jones:** the other to the 5-V rail, but I can't really see how, but anyway. Hmm. Okay, I've actually replaced all the caps there or at least all the major ones. So, let's switch on. And it's something's It's hiccuping. Look.

**Dave Jones:** Check that out. There we go. That's progress. Hiccuping power supply. Hiccup. Hiccup. Hiccup. Okay, I'm going to capture the 5-V rail again. There it is. Whoa, that's 2 V per division. So, as you can see, it's starting up 2 4 4.5 V and then it

**Dave Jones:** it basically just shuts back down and repeats every you know, second or two. So, that's very interesting. Going from a w- well, working in quote marks. Oh. Oh. Hang on. Look. Look, it's going through its self-test. Hang on. It's not hiccuping. We have a

**Dave Jones:** trace. Woohoo! What the I just went away for 5 minutes to have a look at the manual, came back and it it went through its power on self test. Winner. So, I'm not sure what that hiccuping was. There might be something

**Dave Jones:** else a little bit dodgy in there that was tripping the uh some sort of overcurrent protection. BUT, WOW! We're in like Flynn. Look at that. We got trace. We've got trace. We We have no display. Hang on. Readout. Yeah, yeah, we have some

**Dave Jones:** readout, too. Oh, winner! It's all fuzzy, though. Look at that. I don't like that. Is that some Is that some jitter on the readout? But, hey! It went through the power on self test. LET'S TRY THAT. WHOA! WHOA!

**Dave Jones:** WHOA! WOO! HANG ON. WHOA! THAT'S BAD. That's bad. Hang on. Whoo! A thing of beauty is a joy forever. Look at that. It's a Bobby Doesler. We released the magic smoke. Yes, it's a brand new cap I put in. And yep. PEBCAK.

**Dave Jones:** Mwah! I put it in backwards. Oh! Look at that. Isn't that just gorgeous? Insert uh meme here. Wow, that's just fantastic. That just spewed its guts right out there. Oh, Wilson! Yep, dumbass Dave uh put it in backwards. There's a positive and

**Dave Jones:** there's the negative. The reason I didn't see it is because I was looking at the board from this direction here and I thought that positive was that one. I just was not paying attention at all. So, there you go. That explains

**Dave Jones:** the hiccuping when we didn't have hiccup in before, of course, when you had a nice stable power supply, albeit we had a large ripple on the 5-V rail, and we but all the all the measurements were spot-on. There was no hiccup in at all

**Dave Jones:** before, and then all of a sudden we had changed the caps and it's hiccuping. That doesn't make sense. Uh power supplies only hiccup like this when they have overcurrent situations. So, yeah, it's obvious this thing was in backwards. It was drawing a large amount

**Dave Jones:** of current, and it was causing the shorting out that rail effectively, or loading it more than its um protection current, and the power supply was hiccuping. Hic up Hic up Hic up. That's what good power supplies will do when they have overcurrent

**Dave Jones:** protection. They'll They won't just like shut off. They won't just blow a fuse. They'll try again, and then get shut it down, try again, etc. And uh yeah, the magic smoke escaped. Brilliant. Um yeah, lucky I've got another one. Anyway, yes, these are One

**Dave Jones:** Hung Low brand uh low ESR uh caps I've put in here. I I don't recommend you use these for long term, but as you can see, um it does the scope now powers up, and we got out of trouble. So, except I put

**Dave Jones:** it in backwards. Doh! Anyway, I'm going to go in there. I'm going to replace uh some of the X uh caps as well while while I'm at it. There we go. Got two new uh X class caps on there. Nice. So,

**Dave Jones:** and there you have it, reefers. Reefer madness. So, yep. Yeah, definitely if you ever find these in gear. I've done a video on this, reefer madness. Just simply replace them. Uh don't even power it up with these. I was a bit, you know,

**Dave Jones:** it's a bit gungho. By the way, for those who are wondering about the uh the scorched burn mark around there, there's nothing wrong with that transistor, I believe. Seems fine. Um it's just that the it's gotten uh some things in the

**Dave Jones:** 2465B get notoriously hot. I'm not sure if this is one of them, but obviously over time it's just browned the uh fiberglass brown. Is that a word? Charred the fiberglass or whatever. So, it it the thing wouldn't work if that was uh

**Dave Jones:** gonski. So, yeah, obviously it's okay. So, I'm going to leave that for now. Unless you know specifically that uh something gone wrong there, let me know. You can see that we've got a similar thing happening. Bit of charring

**Dave Jones:** here. Yes, I'm going to clean up those joints. Don't worry about that. Yeah, from these diodes um these power diodes obviously getting a bit warmsky and just you know, over time just uh degrading the fiberglass. That's all. Nothing to

**Dave Jones:** worry about if your diodes are fine. Okay, after that PEBCAK, I've replaced all the uh unreg main rail caps. And the reason the unreg ones are going to fail more than the regulation or the output side caps is that the input side caps,

**Dave Jones:** the unregulated ones are susceptible to more ripple. So, therefore they have a harder working life. The internal the ESR is going to cause them to heat up in more internally and they're going to have a shorter life than the output

**Dave Jones:** caps. That's how it works in theory anyway. So, I've replaced those. I've replaced the uh X and Y class uh caps in this thing. So, let's power it on again.

**Dave Jones:** Come on. It's going through. It's going through. It's going through. It's going through. And bingo, we have that trace again, but we still have the fuzzy digits. That could be caused by Once again, there could be like an output rail cap

**Dave Jones:** or something on that, but uh yeah, that's a It's a nice bright trace, isn't it? Look at that. So, that's pretty sweet. Nice. Actually, nope, that was just our focus there. That was just our readout focus. I was uh a bit taken aback because the

**Dave Jones:** uh I forgot that it had separate controls for that. And so there you go. Our readout is beautiful. Our intensity fantastic. And it looks like we've got some cursors here. Sorry about turning the lights off here, but it does

**Dave Jones:** actually look a lot better. Like you can cuz these little LEDs are a bit a bit wimpy. They always have been on this on these model Tektronix scopes. I've never been a big fan of them. Horizontal position control works. Channel one

**Dave Jones:** channel two fantastic. I'm really liking it. And remember, I haven't replaced those caps which look, I haven't measured them, but they look to have leaked and spewed their guts out and maybe corroded some of the nearby components on the board on

**Dave Jones:** the logic board, but hey, it's working. It's working okay at the moment. Beautiful. Now, I don't recall the if this is normal. I don't think so. Like press AB trig and like a whole bunch of a whole bunch of the LEDs sort of light

**Dave Jones:** up. That could be some of that those decoupling caps on the logic board might be doing something funny, but it's obviously still operational cuz it's got it to do to put the text on the screen like that. It it basically has to be fully

**Dave Jones:** operational from a basic point of view. So yeah, I do Can anyone let me know if that's normal? Doing like uh look at the yeah, no, it it it can't be. No, there's got to be something else. Something Yeah, look you press actually

**Dave Jones:** any button. Looks like any button. No, except that. Oh yeah, maybe I can just see them flash. Oh, listen to those relays. Oh. Oh, Bobby Dazzler. And this has got 50 ohm input impedance too. Nice. Oh, I forgot we can like turn on Where is our

**Dave Jones:** other stuff? We can turn on the readout intensity, the scale factors. Beautiful. Look at that. Now I got it all. Ah. There we go. Woah. It's a little bit fuzzy. Little bit fuzzy, but jeez, you know, I'm not going

**Dave Jones:** to complain about that. That's for sure. Yeah, that's what this the readout here, the readout dial, you can actually get it to go one side and it just shows the cursors. The other side shows the uh read readout and the cursors. So,

**Dave Jones:** that'll show you your volts per division. Ah. Wow. Just going to power that up. Again, it's running through its self-test. So, the non-volatile RAM, I mean, isn't I thought that was supposed to like give an error or something if

**Dave Jones:** that we if that didn't uh check some, so maybe there is a little smidgen of battery life still left in that puppy. And anyway, let's feed in a signal. Well, channel one seems basically functional. I'm feeding in a 1 kHz uh 500 mV peak-to-peak, 484

**Dave Jones:** mV on the cursors there, you know, you're not going to complain about that. Um so, that that's all right. No worries. And we've got 20 MHz there, 50 mV signal, and yep, no worries. And the same on channel two as well, 20 MHz

**Dave Jones:** signal, 50 mV, that's working just hunky-dory. So, very happy with that. That's a 1 V 20 MHz. Yep. Beautiful. So, there you have it. I'm going to call that quits right now for this repair video. It's gone on

**Dave Jones:** long enough. This is only part one, of course, so don't consider this fully repaired or fully refurbished or anything. I would probably go through and replace, if you're properly refurbishing this and you wanted to use it over a long period of time, be

**Dave Jones:** confident with it, you'd replace every single electrolytic capacitor in there. I still have no idea about the digital caps on here or what uh you know function they actually performed if they're faulty. Haven't even measured them. I do know that they look like they

**Dave Jones:** spewed their guts and by Googling that does seem to be a known issue with the 2465s. Those electrolytic caps on the logic board do actually fail and they corrode away everything. But as you can see we've got a fully functional processor.

**Dave Jones:** It doesn't look like it's lost any of its calibration stuff. So it looks like that Dallas non-volatile RAM is still just hanging in there by the skin of its teeth. Of course you can't measure the internal battery voltage in there

**Dave Jones:** because the battery is actually internal to the SRAM chip. It's potted in that big black block on there. But yeah, you would replace that as a matter of course like a long-term thing. You'd fully recalibrate this and that's a whole

**Dave Jones:** video on its own right fully testing every function and recalibrating this. But there you go. Um by we kind of got a bit lucky on this one just by replacing a few unregulated side electrolytic caps on this as well

**Dave Jones:** as some X and Y class refer caps which in this case hadn't failed but they could spectacularly explode at any at a moment's notice. And it it has come good. There you go. So same so much for scrap and no trace on this thing. It was

**Dave Jones:** simple power supply but looks like somebody's had a shot at this cuz some of those capacitors had looked like they'd been hand soldered and replaced. So yeah, I'm not sure what's going on there. But look we're on our way.

**Dave Jones:** This is absolutely terrific. So yeah, I expected more problems with something like this. And of course I did take the easy way out by simply replacing all of the caps on the unregulated side inputs without really you know like measuring

**Dave Jones:** the ripple on all the other rails. I just replaced them as a matter of course and it just came good. So, we got a bit lucky that there weren't any other faults, no faults on the high voltage uh

**Dave Jones:** side of things. I really expected a lot more fight with this thing. Um in terms of getting it up and running, I thought maybe for this part one video, we'd at least get the processor sort of not, you

**Dave Jones:** know, at least trying to go through a sequence, boot it up again, and trying to get like a power on error or something like that cuz the non-volatile RAM's gone or those capacitors have gone or something like that. Geez, look at

**Dave Jones:** this. This is actually functional. It looks like it's basically functional scope. Right now, we've got our uh cursors, we've got our delta time. I haven't played around with the time yet, but there you go. Let's have a look at that.

**Dave Jones:** There you go, 50-odd nanoseconds. That sounds about right. Pretty happy with that. That's just fantastic. Times 10 magnification. It all seems to work hunky-dory. So, yeah, pretty darn happy. The the ground on the channel two here seems to have a little bit of a

**Dave Jones:** little bit of a little negative wiggle there. I'm not sure what's what's going on there, but the trace is reasonably sharp, more than good enough. Um and all the readouts work. Can't believe it. There you go. So, I was hoping for something a bit more

**Dave Jones:** exciting in the caps, but we did get one blow up, so that was pretty exciting, I guess. Anyway, um yeah, let me know what you want to me to do with this thing for a a potential part two video. But for

**Dave Jones:** now, that's a a part one of the repair, I guess. So, if you like the video, please give it a big thumbs up. And as always, um there's I'm sure there's plenty of tech experts on the EV blog uh forum, and they'll tell

**Dave Jones:** me all about this, no doubt about it, either on the forum or in the comments down below. So, that's pretty impressive for a 30 W plus year-old scope, and it's been sitting just on my mailbag shelf, and all it needed was, you know, a brand

**Dave Jones:** new set of caps by the looks of it. Um, pretty remarkable. Yeah, anyway. Argue down below about whether or not this is the best analog scope ever made. Oh, some people say also the 2467 instead of the 65. Yeah, yeah, yeah, go

**Dave Jones:** on. Go for it. Catch you next time.
