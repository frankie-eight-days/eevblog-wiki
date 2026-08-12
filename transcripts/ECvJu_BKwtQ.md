---
video_id: ECvJu_BKwtQ
title: EEVblog 1511 - Solar Analytics System FAIL! (+ Dave gets ZAPPED!)
url: https://www.youtube.com/watch?v=ECvJu_BKwtQ
source: youtube-asr
---

**Dave Jones:** Hi, I've had a fire on my um solar analytics monitoring system. First thing I noticed is that I got an email report saying you haven't we haven't received any data in a week. Just showing you my fuse panel again cuz everyone marvels at

**Dave Jones:** this wonder, this ancient wonder. Um even though it's not that ancient, it's like mid '80s Australian switchboard. Anyway, they don't make them like this anymore. So anyway, here's the solar analytics uh system and of course I'll link in the video if you haven't seen

**Dave Jones:** it. It's my monitoring system that monitors both my Nphase system, your newer Nphase um system, and so that's that one there. And uh also my old Sunny Boy system as well cuz I got two different solar power systems and this

**Dave Jones:** basically uh combines the monitoring on uh both of those and it's died. Usually and this is actually a three-phase uh one but I've only got single phase here at the house and it does and the lights are out. The technical troubleshooting

**Dave Jones:** for this is Hello IT, have you tried turning it off and on again? Okay, WELL ARE YOU SURE THAT IT'S PLUGGED IN? And I tried that and I don't get any lights so um yeah, I'm going to uh going

**Dave Jones:** to take that off and see what's what. In fact, I can show you on the back here. Yeah, that's the wire there that's powering it. So if I get the cover off, there's the mains input over there here

**Dave Jones:** and I haven't physically touched anything or nothing looks like it's it's come out or anything like that. It's got a Phoenix block. There's the other side there with the uh current transformers down in there which I'm doing a weird um

**Dave Jones:** thing with those. I'm actually paralleling them up. I've done a video on that but let's measure the voltages on there and see if we're actually getting mains input. Now here's where one of these magnetic hanger things would have come in handy. Yes, I've got

**Dave Jones:** the original uh red but there's just nowhere to conveniently put the meter. I'd like to just hang it. Um you know, I could have hung it on the side or something. And no, you can't get in there with a voltage detection stick.

**Dave Jones:** The one that I've got is just too sensitive. It just, you know, it can't discriminate. This whole box is just spewing everything out and you can't detect an individual wire. So, you've got to actually uh touch probe it. Oh, I

**Dave Jones:** just remembered that this actually does have a probe option. So, Yep. There you go. Yep. And yep. Well, it turns out that it's actually wired into the light circuit. So, I didn't expect that. I thought it'd be uh

**Dave Jones:** you know, power point circuit. There's no voltage on it now. And if I re-cycle that, um there's just no leads at all and it's not just a brightness daylight thing. He's dead, Jim. Is this a dead man, doctor? Very dead,

**Dave Jones:** Mr. Spock. He's dead, Jim. He's dead, captain. There you go. That's pretty easy to get out from the uh DIN rail mount. And uh it's nice that they've got the Phoenix uh contact blocks on there. So, I didn't

**Dave Jones:** have to unscrew anything and have you know, wires flapping around in the breeze. That's really nice. And again, I'll just give you a bonus marvel at uh the wiring the rat's nest that is the back of this fuse box. Yeah, it'd be a

**Dave Jones:** bit better. There's the uh neutral block down there. And uh sorry, that's the earth uh block and neutral block as well. Yes, uh you can upgrade these things and I do believe that if I add anything substantially more to the

**Dave Jones:** house, uh then it is a automatic uh like this would not meet current standard and you have to get it redone. And I think they'd just redo it as one big box here. Of course, all the uh DIN rail stuff

**Dave Jones:** that they'd all go um in the one uh you know, just the one huge box like that. So, all the DIN rail. There's my old kilowatt-hour meter there. Like that would be that would be removed. This is the ripple control line receiver

**Dave Jones:** for the off-peak hot water system which we don't use. Anyway, I'm going to take my solar analytics back to the lab and crack her open. Now, unfortunately, it looks like these things are not designed to come apart. There's a split right down the middle.

**Dave Jones:** So, I don't know. Do I have to take that off? Might There's probably like plastic clips. Well, not having much luck so far, but listen to this.

**Dave Jones:** There's something loosey-goosey in there. Um Yeah, that's not good. Trying to get some spudger tools in there and I I don't know. It's Oh, hey, there we go. Oh, look. Look. Oh my god. Well, there's your problem. There's what rattled.

**Dave Jones:** That is a diode. IS IT NOT? THAT SURFACE MOUNT part just fell. Come on. Seriously? I can't Yeah, well, there's your problem. I don't think I've ever had that happen. Like a surface mount component just falls out. Okay, I got it. It's starting

**Dave Jones:** to crack the plastic clips, but you have to know where they are to get it apart. Well, there it is. We're in and there you go. That's really interesting, isn't it? There's our Oh, I've got some four big electrolytics here. They all

**Dave Jones:** look hunky-dory. Going to have to unscrew that. There's the SIM card cuz this is a 3G I think it's 3G. Is that an Ernie Bernie mark? Yep. There we go. No wackers. And oh, there we go. That's got a decent

**Dave Jones:** amount on it, doesn't it? Oh, there's a USB in there as well. Programming, doing whatever. Like a little um uh PCI kind of uh cartridge connector. That's really quite nice. I was wondering how they were going to do this in here cuz you

**Dave Jones:** know, there's quite a significant amount of stuff in here. This is, you know, it's got to do three-phase measurement. What's a Centurion? This is all just interface over here. Where is our cap? Vanish from. Yeah, there it is.

**Dave Jones:** Gee, yeah, zappy zappy. Um I just got zapped. I just got zapped. That cap was charged. Oh. Oh, yeah. That was a That was a good one. That was the DC side of that. That was charged up. Ouch.

**Dave Jones:** Oh goodness. ANYWAY. I SHOULD HAVE THOUGHT ABOUT THAT. WELL, WHAT? There's no bleed resistor on there? Um for the caps? Oh, of course, these things aren't designed to be serviced, but jeez. Okay, still shaking my hand on that one.

**Dave Jones:** Thumb's a bit tingly. Didn't give it a thought, actually. But yeah, with hindsight, um yep, I should have known that they were DC uh input caps charged to mains potential and yeah, zappy. So, I'm going to I'm going to get the meter and

**Dave Jones:** probe that. Oh, jeez, I'm still feeling that in the thumb. Unbelievable. There you go, trap for young players. There's the cap. There you go. Yeah, 271 V. So, I can discharge that. I'll have to get another meter cuz this one doesn't

**Dave Jones:** have the uh low Z. Look what just happened to be lying around, the ultra-rare EVBlog 555 multimeter. Um no, you can't buy it. Well, actually, technically, you can. Um go to Kyoritsu and you can actually buy this. Not the EVBlog 555 branding, but

**Dave Jones:** anyway. There we go. I've discharged that sucker. And where's the other one? That's discharged. That There will be some recovery on that. Yeah, you can see it. See the voltage recover. But uh that is now safely discharged. But yeah, wow, that held that

**Dave Jones:** for quite some time, didn't it? Let that be a lesson to you. Obviously, I came a guster there. They've got super caps on the output here. Look, uh 2.7 V 5 F for uh you know, brownout, the mains fails,

**Dave Jones:** um and that would keep it going. I don't know for how long, you know, you'd have to do your measurements or whatnot. Oh, no, here any other magic smoke escaped? The other diodes look okay. The caps look all right.

**Dave Jones:** Yeah, I can't read that on the camcorder screen, but that does look like an R in there. So, I think our resistor's come a guster where the diode D is missing from. There it is. And the This is the

**Dave Jones:** secondary side. This is secondary side. Okay, this is the primary side. 240 V in, okay? There's our switching transformer. And the secondary side here, the diode there is come completely off. The only reason it would do that is

**Dave Jones:** like if it's melted, if it's heated up so much. That's where it's come from. That whole secondary side is goneski. And that looks like a probably a fusible input resistor there. Let's Let's check that cuz obviously we've had a gross

**Dave Jones:** overload on the secondary. They are 10 ohms. So, that's that's actually intact. And if I probe the input, there you go. Yeah, there's definitely all all three phases are Well, that one's different, but yeah, all three phases there at least

**Dave Jones:** got some sort of connection. Yeah, it is definitely heated up. I like Do we have like a short in the diode or something? Cuz that discoloration in the PCB is all it's it's where it's all burnt. Let's have a look at the main processor board

**Dave Jones:** first. Let's just have a squeeze. I see a solder bridge. Got a little bridge in there. Uh granted, mine is like a I think mine is like one of the earlier units. So, take that in mind. It's probably very

**Dave Jones:** refined now. Lots of flux residue still on the header and stuff. What is Yeah, that that's the Oh, no, that's pin header. Where does that go off? That's probably a production production test headers, I would say. Oh jeez, look at

**Dave Jones:** that. Is that flux residue on the edge card edge connector down there? Jeez, that's not pretty, is it? Uh. That's like Is that happened after? Why would you have flux residue like that on the card edge connector? That's weird. I'm

**Dave Jones:** not going to go into any reverse engineering. That looks Is that just an op amp? It's a microchip part down there. The three pins tied together. They the address lines? Some sort of addressable memory? Anyway, that looks like the ADC down in there. AD I think

**Dave Jones:** if you look that up, ADE 7880. So, that's all the bottom of it. Don't know if I'll reverse engineer this thing. As I said, there is a USB interface. That's the antenna connector there. If you flip it over, it's a Cinterion

**Dave Jones:** EHS6. So, that's an all-in-one module. I guess it does 3G as well cuz there's nothing else on here. So, that'll have like a little arm processory thing or something. And it'll be one of those, you know, all-in-one Wi-Fi My No, this is not Wi-Fi. So,

**Dave Jones:** yeah, like all-in-one modules. JK Consulting did this. Did they? September 2015. I reckon that resistor it is is completely cracked in half. Look at that. Wow. It's completely cracked in half and moved and resoldered itself in the like opposite direction.

**Dave Jones:** Because like Look, the numbers are on the front and the top here. So, it's like it's it's split. It's heated up so much that it's split. Why would it rotate like that? Has anyone ever seen a part rotate, crack, and rotate around

**Dave Jones:** like that? That seems incredible. My My My thumb still hurts, by the way. Just saying. I felt that zap a couple of times before, but wow, like it was like I I put my thumb on it, I think. I have to

**Dave Jones:** rewatch the video. And so it it the path was just inside my thumb. There was no other, you know, it wasn't like going through my body to ground or anything, but my my thumb's still paying the price, let me tell you. So that resistor

**Dave Jones:** there, has completely uh char It It hasn't charred. It's just heated up the resistor cuz it hasn't like there's just gunk under it, but that that's not the I don't think that's the PCB material that's actually charred. But what has actually charred

**Dave Jones:** is the PCB down in there, and this is where the diode came out. There it is. Poor little ON Semi jobbie. It's complete D It was that DE4 or something, was it? But yeah, it's it's just completely desoldered itself. What

**Dave Jones:** watches. JK can see holding, obviously uh designed this. So JK done this design, which actually looks, you know, quite decent. I really like the design of it um and how they fitted it in a standard the standard uh DIN rail uh casing. It's

**Dave Jones:** really good. So quite happy with the design, but yeah, why is it Why is it coming out so like that? And for all you MELF fanboys, uh I'm one of them. Look at this. I I love a good MELF. Look at

**Dave Jones:** this. Look at this. Beautiful. That's obviously the input uh divider cuz this is does uh three phase measurement. So there obviously we've got three pairs there. This This looks like a, you know, a a good quality build. What What brand

**Dave Jones:** caps are these, by the way? Yep, they're genuine Matsushitas. And contrary to their name, they're actually good capacitors. They're good Japanese capacitors. So No no no worries there. DES cap, haven't heard of them, but they're the uh they're the big uh 10

**Dave Jones:** farads total of uh super caps on there. 2.7 volts. So oh, they must uh they must be in series Cuz nothing's going to be operating at less than 2.7. Probably just a 3.3 V rail. And they've got or

**Dave Jones:** could even be 5. Yeah, no, it has been in service for 6-plus years. I have to get the exact date of the video. So, I just paid for a new 5-year plan on this thing. You you know, you pay for the

**Dave Jones:** data plan because it it has to talk, you know, um to the thing. It isn't much. Doesn't actually cost a huge amount. Have you ever seen one like that? Cuz that's a that's a Bobby dazzler. Can we have a minute silence for that poor

**Dave Jones:** resistor? That that is not soldered egg. It was not This would have been nicely reflowed um soldered at the time. And yeah, no, it's just it's melted. And when you heat up components enough, yeah, they melt solder joints and components like this

**Dave Jones:** diode literally fall off. It's not uncommon. Especially if it's in the right orientation for it to fall off and gravity does its thing. Now, my first thought about the failure mode of this thing was that the diode went short

**Dave Jones:** because that is a failure mode uh for diode. Well, it went low resistance and then it you know, it had heated up internally and then that uh caused because there's no fusing on the output. Doesn't seem to be any fusing on the

**Dave Jones:** output there. They've got a series resistor here, but I think that's for Is that for charging this? And that's for charging the super caps? Is it? But anyway, um yeah, so it was drawing all the power that that the primary could

**Dave Jones:** give it uh via this uh very nice-looking uh worth uh transformer here. And uh yeah, it was giving it it was giving it all it could. And this poor resistor, which is on the primary side, um it was it was pulling all the

**Dave Jones:** power from the primary side and it just couldn't handle it. Um so, this poor resistor's come a gutser. Uh it's not like the resistor uh failed. It failed because it was drawing too much. Uh the secondary was causing too much power.

**Dave Jones:** But what caused the diode uh to fail? If you look, and you got Going we've got all this gunk down here, okay? Where did this come from? It's accumulated in the connector. Uh-huh. Have a look down in there. That super

**Dave Jones:** cap looks like it's come a gaza. Check it out. It's spewed its guts. I think it's spewed its guts everywhere. And yeah, hence why the PCB looks like filthy. And why, look, I mean, why do we have this

**Dave Jones:** gunk under the resistor here? What is this gunk? Okay? That is probably dried electrolyte from the super cap. The but I still I It's not like the electrolyte got under there and it became conductive and that's No, I think there's a serious

**Dave Jones:** excess over power event there cuz that that PCB Is it Is it actually burnt? I mean, there is some electrolyte residue under there, but yeah, it's just the dirty nature of the PCB. It seems to have like gunk like everywhere on it.

**Dave Jones:** It's like Yeah, I don't think it was that feel like, you know, it's all around here as well. And if you look at the physical location, okay, and where gravity is taking this thing. But interestingly, if you see how it's

**Dave Jones:** mounted like this, then it makes sense if like it was physically mounted like this, the leads were over this side. So if this cap super cap leaks, then it's all going to fall down like that in that direction. And yeah, it will accumulate

**Dave Jones:** in the connector. And I can't see how it can actually get up into like, you know, like climb up into here and because that's against It's It's physically this board's physically vertical like that. Um it looks like that's leaked. I'm

**Dave Jones:** going to desolder that and we'll have a look at the bottom of it. But I did test these caps before and they did actually seem to charge up with my um ohmmeter. So, you know, like very incredibly slowly. They both seem to charge up

**Dave Jones:** though. Okay. Oh, yeah. Look at that. Yeah, I reckon she's she's spewed her guts. That's uh the only reason that would happen to the bottom of that and that yellow ring all around it. Yeah. Yeah. I think this is the uh this is the

**Dave Jones:** cause. Super cap failed. Spewed its guts and then it did whatever and then the fire mode after that it doesn't it it it almost doesn't matter, does it? And you can see on the PCB down here that's electrolyte. Yeah, wet. Got you. That's

**Dave Jones:** wet electrolyte. Look at that. Yeah. Uh it's gone down okay, wicked into the connector like that and yep yep, it's all still wet. So, there you go. Super cap fire. Oh, that that track there is that starting to

**Dave Jones:** Oh, that's starting to go black. I don't I don't like it. I don't like it. Like you could fix this. You could repair it. Um and if that has actually gone conductive under there, you'd have to like probably drill it out so it's not

**Dave Jones:** uh conductive and uh everything's starting to corrode and it's it's not pretty. If you were desperate, you could actually repair this, but Uh yeah, no. Anyway, I'll send this video to uh Solar Analytics and see if they've had

**Dave Jones:** any other fires of uh these super caps. Uh Nest Cap, I don't know. I haven't used them before. Anyone know if they're any good? But uh yeah, like all the other components in this seem top quality. So, yeah, I don't doubt that they're um top

**Dave Jones:** quality caps. They've they've just failed. Did it get too hot in the Aussie sun? Uh my fuse box happens to be on the uh afternoon sun side, so it would actually get hot. Anyway, there you go. Super cap

**Dave Jones:** fire. Wow. Wow, it spewed its guts and then that caused a poor diode to completely desolder itself and then this that magnificent resistor that's just snapped. Ceramic base is just snapped in half and then resoldered in the other

**Dave Jones:** direction. That's terrific. That is a great value mode. I love it. Anyway, I hope you found that interesting. If you did, please give it a big thumbs up, especially for me zapping myself. Um yeah, that was a dumb Dave trademark. Uh yeah, don't make

**Dave Jones:** that same mistake. Anyway, give it a big thumbs up. Comments down below. Um I'll let let you know what um Solar Analytics uh say, and I guess I'm without a monitoring system, although I've got like three other monitoring systems, so

**Dave Jones:** you know, it but this one is like the combined one. But anyway, see what they have to say, and uh I'll get back to you maybe if a second channel video is for something like that for the follow-up.

**Dave Jones:** Catch you next time.
