---
video_id: SR-3l6yrAXM
title: EEVblog 1382 - Keysight EDU34450A 5.5 digit Bench Multimeter TEARDOWN
url: https://www.youtube.com/watch?v=SR-3l6yrAXM
source: youtube-asr
---

**Dave Jones:** Hi, it's new test instrument teardown time. We've got the new Keysight EDU34450A 5 and 1/2 digit multimeter. This is part of the new educational series as you've seen in the new giveaway videos that I've done and it's and probably the most

**Dave Jones:** interesting of the three new instruments. They've got a new educational power supply and a educational model function gen 20 meg function gen as well. And the both the function gen and this multimeter are in your traditional oscilloscope like you

**Dave Jones:** know short compact when I was a boy oscilloscopes were never like this thick like you know, they're out here like this but anyway, the oscilloscope form factor. Basically, they're reusing the tooling for their 1000 series oscilloscopes which you can get like an

**Dave Jones:** EDU version of the oscilloscope and the whole idea is that they provide these four instruments for the educational market as all part of one big educational package so that you can equip a typical bench. So I thought this

**Dave Jones:** is probably worthy of the first teardown just because it's interesting form factor. So let's check it out. First of all, you may have recognized the number the 34450A. They're actually reusing a product number. You can well you used to be able

**Dave Jones:** to I don't know if you still can but you can buy the 34450A 5 and 1/2 digit multimeter and it doesn't look anything like this. It's a big OLED display one and it like why? Why reuse it? Why the

**Dave Jones:** confusion like that? I like they didn't even call it B or anything but it's got the EDU on the front. So having the EDU on the front is the exact same part number. It's a totally different look and feel instrument.

**Dave Jones:** I don't get it but it's $696 US dollars. So yeah, anyway, um it looks like an oscilloscope and you can see that they've reused the tool in here cuz it's got a fan uh outlet here, but there's no fan in it. So, yeah, LAN and

**Dave Jones:** USB as standard. Well, you're either going to love it or you're going to hate the form factor. So, whatever. Anyway, you know what we say here on the EE blog, don't turn it on, take it apart. Except flatheads, not going to do it.

**Dave Jones:** Hang on, is it a 5 and 1/2 digit or is it 5 to the power of a half digit? Hmm. Got the self-tappers into plastic down here. That's not pretty. Well, they felt for all the world like self-tappers, but

**Dave Jones:** they weren't metal threaded inserts. They just had lots of Loctite on the bottom of them. So, don't get your feels versus reals mixed up. So, it looks like we got all the basic shielding you expect. Whether or not this is identical

**Dave Jones:** to their oscilloscope, I can't exactly remember offhand, but sucker should lift off. Yep, we're in. And there you have it. Isn't that nice? That looks pretty schmick. Got our processor over here and our multimeter measurement capability on a separate board.

**Dave Jones:** Very nice. And a good old-fashioned transformer in there. Look at that. Old school. You don't see that much these days. Brings a tear to the eye. Anyway, I do like the cable management in there. That looks pretty groovy. Not

**Dave Jones:** sure what the deal is going on there with that connector with that like inline spade connector. It's all terminated very nicely, doing all the right things. All your groundies down there. I'm sure they're all Loctited. We've got ourselves a ferrite on the output here

**Dave Jones:** and big ass earth going over to the processor side of things. Because of course, all your multimeter section is isolated. That's why the only thing going over here is this and that. Guarantee you that chip right there is

**Dave Jones:** an opto isolator. So, obviously not many uh connections. It's a complete serial interface. It'll be reasonably high-speed optocoupler. We've got our big shield over the measurement front end. Got some good old old-school relays. I can show you a little quirk of

**Dave Jones:** that at the end when we power it up. Check out the front end. This actually looks really good, doesn't it? I'm actually quite surprised to see the banana jacks soldered directly onto the PCB there. Got a couple of isolation

**Dave Jones:** slots cut into there. Two gas discharge tubes, GDTs, thank you very much. Two big-ass MOVs here. Look at the size of those monsters. What is the I forget what the rating on this thing is. It's It's only CAT II

**Dave Jones:** with a 300 V, which is common for bench multimeters. You almost never see any bench multimeter above CAT II. It's just a thing for them, but jeez, look at that. That's pretty juicy. Tell you what. Look at those big-ass

**Dave Jones:** diodes over there. That'd be across your fused your current shunt fuse, and there's your fuse right there. So, that'd be back-to-back diode protection. They often do that with a diode bridge, but in this case, yeah, they're they're doing that with two big-ass back-to-back

**Dave Jones:** diodes. Wow. Never seen one so large used in a multimeter before. So, that's pretty nice. Yeah, and the fuse, they've gone to the effort to wire this thing over. So, they could have maybe chose a piece of solution there, but they

**Dave Jones:** haven't. They haven't skimped. I I don't see a traditional current shunt. It's got to be these bad boys here. You traditionally don't see that. You usually see your bent like nichrome type wire current shunt. Anyway, we've got a range relay here and

**Dave Jones:** there's really nothing much doing over here. These are just our voltage regulators, just uh powering some of the uh logic and stuff. So, nothing to see there. Tension to detail, they have uh someone had fun with the silicone gun.

**Dave Jones:** Look at that. They gunked it down. Nice. Yes, I'm still waiting on hold if you can hear that in the background. Anyway, up Quick look at the uh processor board here. Uh now, you've got to think that this comes from another of the

**Dave Jones:** instruments cuz obviously they have some sort of uh BNC over here. So, is this identical to like the function gen board? Hang on, let me check the function gen. No, that's interesting. Both the function gen and the oscilloscope don't have anything in the

**Dave Jones:** way of a BNC there. And of course, uh look, you can see up on the metal work there, they actually have the BNC on the back like that. Um, maybe on the function gen version of the oscilloscope, I think, uh might have

**Dave Jones:** that. But, obviously reusing that processor board as you'd expect. Like, that'd be, you know, crazy not to uh reuse the same board. But, anyway, um the earth wire is just they've just soldered it into there. It's like gone,

**Dave Jones:** "Bugger it. We need to, you know, get a big-ass earth wire over there." And well, that's one way to do it. It's nothing inherently wrong with that. Anyway, I won't bore you with the details. There you go, you can read that

**Dave Jones:** for yourself. ST arm uh micro 1 variant and it is You got the memory and you got the flash and you got the whatnots and uh yeah, not much else. We're going to There's that the ethernet, yep. And uh

**Dave Jones:** USB, um and well, not much else. There you go. Is that the LCD flat panel driver? I don't know. Hasn't got many connections, has it? But, yeah, there's really not much happening there at all. And well, you wouldn't expect anything

**Dave Jones:** more. And if you have any doubt that they're uh reusing the metal chassis there, well, there you go. There's all your inputs for your four-channel scope. Nice. Well, you know, why not? All right, so I've taken the cables off,

**Dave Jones:** taking out a bunch of screws, and gotten rid of the fuse holder, and that should just lift out. Careful with the banana jacks, they've got to lift out vertical. And tada! There you go, there's the flip side. Oh, we can now take the metal

**Dave Jones:** shield off. Very nice, check that out. There you go, for you jack aficionados, there's none of that split jack rubbish. This is interesting, they've got a sneaky little bugger ferrite bead there. Here, see, you can see the trace, this

**Dave Jones:** is on one of the inner layers, buggering off like that, and looks like it's going under the ferrite bead. Yeah, okay, it's only cat two rated, but yeah, why you'd just rely on a layer for that sort of

**Dave Jones:** insulation, Beulah, Beulah, Beulah. What the heck is going on here? Uh, it looks like like some sort of touch switch, but it's not, because it's like it doesn't actually connect to anything as far as the case goes. It's like around about

**Dave Jones:** here on the case, it's just like it's not that. So, I can only think that it's some sort of elaborate uh, you know, open air PCB spark gap, but what does IT CONNECT TO? OH, like mains earth or something? Uh,

**Dave Jones:** it it could be. It could be. I'm going to have to buzz that out. Um, that would be my only guess, cuz it's nothing to do with the inputs. It's not like some spark gap, cuz they've already got like

**Dave Jones:** real spark gaps here. Um, it it's nothing to do with that. But, here's the thing, um, neither side of this actually connects through to the shield here, and you might think, okay, it'll able to down through to the chassis ground

**Dave Jones:** through one of the uh posts here, one of the mounting studs, right? But, look, there's your isolation around your stud there, there's your isolation around your stud there. Uh that one, that one. The only ones that are actually have something connected to

**Dave Jones:** them are these two down here. Sure enough, there's a 100 ohm resistor to mains earth there. So, where's that Where's that going? Yeah, okay. We've got 100 ohms in series with a MOV here and in series with a spark gap. And

**Dave Jones:** then, that bugger's off. Oh, yeah, then that goes to the other side of the MOV. So, you've got a spark gap and a MOV in series, by the looks of it. And that goes So, that's your positive input

**Dave Jones:** terminal, that's your uh ground input terminal. But, then the other side of that MOV goes over to this spark gap in series with Yep. Series with this MOV, which goes to your 100 ohm resistor, which then goes to your mains earth. So, they're

**Dave Jones:** actually uh overload clamping that down to mains earth. Oh, nice. By the way, all the input uh switching relays here, they've all got isolation slots between the coils and the contacts. Nice touch. And here's a nice little touch. They're your three

**Dave Jones:** slots for your uh shield. I just unscrewed it there. And you'll notice that this one will slide over, and these will slide over like that. Then it just drops out. Nice design. All right, so there's our big ass uh AC input uh

**Dave Jones:** coupling cap for AC measurements here. They've got a cardac uh resistor divider here. So, that's for the ranges. So, you know, you know, that's what you expect. You expect that in any 5 and 1/2 digit uh plus class meter. You can't Well, you

**Dave Jones:** can do it with discrete parts, but it's just it's much nicer to do it with a ceramic array. So, no surprises there whatsoever. Uh here's our two uh input strings here. These are for the uh sense lines here.

**Dave Jones:** And of course they whack them in series for extra voltage stand off of course because each one will be a couple hundred volts and well, 200, 400, 600, 800, 1000 volt rating. All right, so it looks like this is our another input

**Dave Jones:** string here and that little inductor there let's jump over the via for that is there. So that's coming from this relay here. Classic ULN2003 relay drivers here and they're buggering off to drive our relays. So you can see

**Dave Jones:** we've got our coil side here and here's our measurement side. So oops. Oh, there you go. You got one sneaky little bugger coming off there and going through. Can we see other sneaky little bugger traces going off? Hmm. So yeah, this is interesting.

**Dave Jones:** On the uh contact side, I'm not seeing any parts on those relays there. And on the bottom side down here, you can see some internal traces there but apart from that, not much doing, is there? Hmm, there's nothing exciting to see

**Dave Jones:** there. All I can see is this little one buggering off over to here. Just one thing I notice here just from a routing point of view, you can see these are going off here to drive the coils. They

**Dave Jones:** dropped the they're on the top layer here. Traces on the top layer, they bugger off to an inner layer and just go over and drive the relay here. Oh, woah, why? I'm not seeing it from a voltage um

**Dave Jones:** uh like clearance uh creepage reason. So they're doing it again here. I don't know. Oh, no, now I see. You're probably screaming at me in comments. It's very faint. You can see this is like the AC coupling No, AC coupling

**Dave Jones:** caps here, but here's another input resistor here, and it's actually going on an inner layer under these two resistors here. And um over to one of the contacts on this side of the relay. So, yeah, that's interesting. Why

**Dave Jones:** run them under something that's clearly on you know, you want your Once again, they're relying on the thickness of your uh PCB layer there for your voltage clearance. I'm I'm not sure why you'd do that. Right. So, we've got our four

**Dave Jones:** relays here and our four inputs. Um this relay here connects to the AC coupling cap. This relay here connects to a 100-ohm resistor there in series. This relay here actually connects through to the uh high end of uh the uh ceramic resistor

**Dave Jones:** uh divider there. And this relay here connects through to uh this high-voltage resistor uh array here. So, there you go. There are about four separate choices for our inputs. Um yeah, I just I just don't know why they've gone under

**Dave Jones:** the Why they gone under the resistors? I don't know. Okay, Dave, tell us how you would have done it then. Well, okay. Um clearly, I would have uh well, taken These would have stayed on the top like this. They go directly over to drive our

**Dave Jones:** coils over here. And then, I do what we what you doing here. Uh the contact actually comes through the center here like this. And then, I would have put an an isolation slot here and here so I could get cuz these are our contact

**Dave Jones:** size. So, this is a double pole double throw switch. We've got one switch here, which connects between there and there and there. And this one here here and here and here. And yeah, I would have did or taken them out

**Dave Jones:** around like that and then put the isolation slots in there. But they haven't. They put isolation slots here and here and then run the trace under there, and relied on the uh thickness of your layers between your PCB. I

**Dave Jones:** I don't I don't get it. Anyway, here's the interesting bit. Check this out. They've got a Keysight custom jobby here, and we haven't seen this in other Keysight bench meters. It might be in the other cuz I haven't torn down the

**Dave Jones:** other 534450A, the one with the OLED. Maybe, you know, maybe it's absolutely identical uh design to that one. They've just changed the form factor and the user interface and stuff like that. Anyway, you can see the little exposed guard traces there.

**Dave Jones:** Of course, they do that for leakage reasons. You probably have to do a video on that dedicated to that one day, but you know, we've seen that on low measurement stuff. You know, you see that in your you know, femto amp amplifiers and all

**Dave Jones:** sorts of stuff. Anyway, I don't know if it's genuine Keysight custom silicon or whether or not it's a rebadge one of your traditional multimeter chipsets. That would be interesting to find out. If anyone out there, and I'm sure there will be a

**Dave Jones:** lot of people interested, will I don't know, check out the pinout of something like that. So, hmm, high-res photos on the EEVblog Flickr account linked down below. So, anyway, that's going to contain our ADC. Of course, that's you know, your

**Dave Jones:** traditional multimeter like a dual slope or multi slope integration converter. It's going to have the range switching. It's going to have all the other functionality for resistance mode and capacitance mode and you know, all the other stuff. So, that's it. Yeah,

**Dave Jones:** that's your traditional multimeter chipset. And really, there's not much else doing. We're relay drivers as I said. What's that one? Oh, that's just a DG412 max. Nothing doing there. What are these bad boys down here? And a couple of LM393 comparators down

**Dave Jones:** there. But do we have some Yeah, some just some bridge rectifiers there. Nothing doing. Someone will say, "What's the brand of the electrolytic cap?" JH. Can't say that rings a bell. And before anyone screams, "Oh, there's no PTCs in

**Dave Jones:** here." They've got the moves and the GDTs and everything. Well, no, they've got one down there. It's on this input string here. Of course, they don't need it on all the input strings because well, it depends on the

**Dave Jones:** functionality that they're trying to measure. But anyway, let's have a quick look at the input circuitry around here. Once again, we've got a couple of 393 comparators there. A bunch of LEDs for diodes and all transistors. Yeah, yeah, they're all

**Dave Jones:** diodes. So, a bunch of diode protection and whatnot and just a bunch of passive. And of course, all your multimeter aficionados are asking the one question. Sorry I had to get this far into the video before you saw it.

**Dave Jones:** The voltage reference, of course. Notice this is in a six and a half digit meter, so you're not going to get your, you know, LTZ1000. Sorry. You're going to get a Renesas jobbie. Although, that's got a Fairchild on

**Dave Jones:** there, but you know, it's all Renesas these days. I don't know who's gobbled up who. Anyway, it's the 21 090 and this is a voltage reference available in different voltage standards and it's not like 0.02% at best initial accuracy, but of course,

**Dave Jones:** the initial accuracy doesn't matter cuz you can calibrate that out. What matters is the drift of the thing. The P How many PPM? Tell us PPM. 7 PPM. So, debate in the comments down below whether or not that's good enough. Is it

**Dave Jones:** good enough for a five and a half digit meter? Is it overkill or is it just adequate? And then we've got another processor there. We've got a buzzer up here for your continuity test that now because there's nothing

**Dave Jones:** left, really. Yeah, I mean, you could probably hack away there. There you go. There's some headers. Don't have a connector on there. They're being a bit naughty. But anyway, the JTAG's there. It's all labeled. So, knock yourself out. So, the conclusion

**Dave Jones:** on that is that yeah, it's pretty schmick. They've got, you know, all the dedicated parts with the relays in there. There's, you know, no sort of like like range switching other compromises you need to do in handheld multimeters. So, they're all just

**Dave Jones:** separating out all the functions there. And it all looks you know relatively good. Of course, you know, only 300 V CAT II rating. You're not going to of course because this is main mains powered. You're not going to carry it

**Dave Jones:** out with you in the field or to a switchboard or, you know, to some big power plant or something like that. That's not its job. But looks like it has more than adequate protection. And you can argue your way about the voltage

**Dave Jones:** reference and and whatever. I assume it's custom Keysight multimeter chipset silicon down in there or they don't know. I don't know. Somebody may have helped them out. Maybe they commissioned it from one of the multimeter chipset manufacturers. Perhaps. I don't know. Is it the same?

**Dave Jones:** Is this almost identical to what's used in the existing OLED model in the more traditional bench multimeter case? The one that's you know, the 34450A without the EDU one. Is it basically an identical circuit? I don't know. Never

**Dave Jones:** opened one. Still works. Takes a bit of time. It's going through its cycle there. And yep. We're in. Now, here's one of the quirks. The absolute first thing I noticed when I plugged in this meter when I actually

**Dave Jones:** got it is that yeah, here you go. It's just sitting there. We've got our five and a half digits measuring 1.8 mV. It's supposed to do that. So, my BM786 over here, it's measuring something. And I move the probes around. Done a recent

**Dave Jones:** video on this. This actually spurred that recent video on the number of power line cycles. So, I take these probes, I plug them in here. Yep, there it goes. It's doing exactly the same thing. There we go. It's just cycling through.

**Dave Jones:** It's just cycling through. Yeah, it's switching and that's 10 megaohms input impedance. I switch it to auto, which is high impedance mode. It still does it. And if we go to a 1-V range here, it just overloads because it's picking up

**Dave Jones:** the 50 Well, no, it didn't do it. There you go. Overload. Cuz it's picking up the 50 Hz. Actually, let's go into fast here because it's picking up There we go. It's picking up the 50 Hz noise in the lab here and it doesn't have the

**Dave Jones:** number of power line cycles set to at least one. Whether you're in fast, slow, or medium, it still actually does this. And if you set it to auto range, actually, if I untwist the wires, I think that's why

**Dave Jones:** it's not performing like it did the other day. Listen to that relay. Hear that? So, it'll really depend on how the leads are, how much 50 Hz I've got at any one time.

**Dave Jones:** That poor relay. Anyway, I do have a video of of it actually doing it continuously and I send it through to Keysight. Anyway, that's just Yeah, something to be aware of. And from what I can find in the menu or can't find in

**Dave Jones:** the menu, there is no ability whatsoever to like set up number of power line cycles. You got, you know, auto dim It has an annoying default auto dim where the screen dims. Jeez, why bother? There's just nothing in there that I can

**Dave Jones:** find for number of power line cycles. Anyway, we do have a secondary measurement capability, DC current. So, it looks like we can measure it because we've got the different jack. We can measure current and voltage at the same

**Dave Jones:** time. Beauty. Continuity. Here we go. This is what everyone wants to see. Multimeter still has to have a fast auto ranging.

**Dave Jones:** That's so slow. Yeah, not for an everyday use meter. But then again, we are on slow mode. Let's put it on fast. Let's see how fast she actually is. Here we go. Go up. Looks like it goes up

**Dave Jones:** to 100 meg there. Whoa. Hey, it's just flapping around in the breeze there. 100 meg. Hello. That could be the noise. That could be related to the 50 hertz pick up, I'm sure, because like you know, this is

**Dave Jones:** going to be greater than 100 meg. Oh, yeah. There we go. We're instant. Oh, yeah. Look at that. Look at that bad boy. No wackers. And the continuity buzzer? Let's give that a whirl.

**Dave Jones:** Well, it's quick, but it's so piss weak. I can barely hear that and I'm in a silent lab. It's like 10:30 p.m. here. All silence and jeez. Compare that to my BM786, same distance with the microphone pointed away.

**Dave Jones:** Huge difference. Uh, looks like it's got zero ohms compensation, so we could null that. Oh, okay. Now, uh, pre-math. Ooh, look at that. Ooh, isn't that fancy pantsy? Zero compensation. There you go. Look at that. Ooh, nice. Anyway, unfortunately, one of the things

**Dave Jones:** this thing doesn't have is, uh, your fantastic, um, trend plotting. Like live trend plotting that you get on the other HP No, HP. Keysight bench, uh, meters. Unfortunately, it just it it doesn't have it. You can actually do data acquisition though. So,

**Dave Jones:** you know, if we go into DC volts here, we can actually acquire and we can go into continuous and then we can go into data log mode and we can trigger and we can have trigger count and sample

**Dave Jones:** interval data log on like that and the minimum sample interval you can do is 1 second by the looks of it. I can't seem to go under that. Okay, so if we data log on and then we can run run. There we

**Dave Jones:** go. So, it's sampling once every second there, but it's not going to give us a like a display. So, okay, so we can just stop that then we can go into display and we can view our log and there you go. That's

**Dave Jones:** the just the 50 hertz input crap that we were seeing there and like yeah, there we go. One at a time like that. And that's basically all you can do and but of course you can export like you can

**Dave Jones:** because this thing's got full remote capability LAN and USB and I believe you get the software with it although I'm not sure if it's full capability. No, I don't think it is. No, I think it's only like the demo capability of the software

**Dave Jones:** or something like it it No, it needs to have There it is. That bloody relay again. Needs to have trend plotting in it just like the other Keysight meters. Come on, you've already got the software there to do it like how why can't you

**Dave Jones:** include it? I don't know. I I know it's probably extra work to include it, but and you should get the full license to the software as well. So, anyway, so look, I'm not going to do anything more with this. I want to keep this video

**Dave Jones:** under 30 minutes. This is not a full review. If you do want me to do a full review, I can eventually do it and have a look we can have a look at capacitance here. Let's go over. You know, but look,

**Dave Jones:** it's like a I'm not sure I how it compares with the 3440 the previous 34450A, but well, it didn't have trend plotting I don't believe. So, yeah, maybe that's what like everything's just nicked from that and that's that's one of the

**Dave Jones:** problems like one of the main drawcards of the Keysight bench meters is the trend plotting capability being able to do that and not being able to set the number of power line cycles on a bench meter with you know, like five and a

**Dave Jones:** half digit sure it's not a six and a half digit meter five and a half digits and well, Keysight might do a firmware upgrade. They have already done a firmware upgrade since I reported the rain auto ranging thing. They fixed a

**Dave Jones:** few things, but it's it's still there cuz I've I don't know I've probably got a lot of 50 hertz here in the lab, but yeah, no, you can't have your relays just flicking around with you know, it needs to have the ability to set the

**Dave Jones:** number of power line cycles. Just set it to one or have the user option to do that and you'd never get that. It just wouldn't pick it up. So, yeah, I don't know. It's like a lot of people are going to like

**Dave Jones:** the form factor. They're going to probably like the price point as well. It's not that expensive, but then again, it's not that far off their six and a half like their low end six and a half digit models and other you know, six and

**Dave Jones:** a half digit models on the market. So, you know, but anyway, yeah, there might be specials on it or something like that and it's a lot of people are going to buy it for the form factor and for the remote

**Dave Jones:** capability sort of stuff. You know, you can script things and do everything and the hardware seems pretty decent, but I like I can't help but think that they've just stumbled on a few hurdles here and it's just lacking some features that

**Dave Jones:** could make this a real killer multimeter, I think. I don't know. Leave your thoughts down below. Am I right? Am I wrong? Being too harsh? No, that'll you know, eat into the sales of their six and a half digit

**Dave Jones:** ones etc. And it's Oh, it's only designed for the educational market and, you know, it's Yeah, okay, but you know, uh it's probably like only like software things, really. So, I don't know. Anyway, that's the teardown of the new

**Dave Jones:** EDU34450A five-and-a-half-digit bench multimeter in an oscilloscope form factor. If you liked it, give it a big overexposed thumbs up because of the Keysight black. Look at this bloody Keysight black. Put my hand in there and it's just uh Sure, I'm a white pasty

**Dave Jones:** nerd, but jeez, you know. Anyway, catch you next time.
