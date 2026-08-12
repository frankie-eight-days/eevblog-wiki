---
video_id: M6PVarUSjqg
title: EEVblog #1364 - Compaq Portable PSU REPAIR
url: https://www.youtube.com/watch?v=M6PVarUSjqg
source: youtube-asr
---

**Dave Jones:** Hi, when we last left our intrepid adventurer he was caught up with this IBM compatible, the world's first IBM compatible compact portable machine from the early eighties and managed to get the motherboard up and working and determined that the power supply was

**Dave Jones:** shot. We weren't getting any negative rails whatsoever which actually stopped the main processor from booting up because there is a logic output from this comparator circuit around here that obviously checks the rails on all the voltages. There's plus 12, there's five,

**Dave Jones:** there's minus 12 and minus five at least I think and they're all obviously summed together and gives a signal good output and it was giving a signal bad output and that was going to the CPU holding in reset stopping the machine from starting

**Dave Jones:** up. But once we powered the motherboard up with an external power supply and bodged in that power good signal, the motherboard came to life and we're able to get video out of it. It still worked. So, let's get back to this power supply

**Dave Jones:** here, this pesky little power supply. Reason we didn't look at it last time is cuz well, look at it. It It look It's like you can't even get in there to read or measure half of the parts. It's all

**Dave Jones:** higgledy-piggledy. It's all over the shop. It's just a really horrible layout to work on and of course Murphy ensured that any trace that you try to you know, trace on here it's going to go through to the top layer where you can't

**Dave Jones:** damn well see anything. So, yeah, real pain in the butt. Anyway, we're going to solve our minus five volt and minus 12 volt issue on here. So, let's take a closer look. By the way, we're going to be using the new EE blog BM 786

**Dave Jones:** multimeter available exclusively on the EE blog available on the store as of today. I just got stock in so, yeah. Anyway, check that out. So, what we've got here is a obviously a switching power supply cuz it tells you

**Dave Jones:** it's made in the United States of America. SMPS switch mode power supply. This is obviously the primary side here. We've got 240 V mains or what that you 110 Yankee rubbish coming in here and then we've got oh yeah, a couple of

**Dave Jones:** little bridge rectifier, too. Bridge rectifiers. Anyway, we've got a bridge rectifier down there. Then that just rectifies the input mains. We've got our high-voltage caps here and then um this um contraction which looks like a giant inductor, it's not. This is actually

**Dave Jones:** your switch mode transformer. You can probably see deep down in there is some wires running off there. So, this is like it's really ugly. They're just like hand-wired over to points down in there, there, there and all over the shop. Um

**Dave Jones:** anyway, so yeah, essentially our primary side here and we've got a made in Britain. Made in Great Britain. Thank you very much. A 2N6545 for those playing along at home. Anyway, um obviously primary side and obviously the rest of this is secondary side with

**Dave Jones:** this is our isolation transformer. And the taps for this thing are right down in there. Some like secondary taps. So, these are all of our secondary regulation capacitors. Now, we're basically just looking at the topology basically cuz we've already gone over

**Dave Jones:** this board. We've done the smell test. We've done the visual test to look for, you know, a blown stuff or dry joints, you know, things like that. And we did actually detect a few dodgy joints on the LM338K. But, that's actually working

**Dave Jones:** cuz this is actually this is an adjustable voltage regulator. Here's the data sheet. So, this is going to be for either the plus 5 V or the plus 12 V rail. So, obviously right off the bat and because look at the size of the heat

**Dave Jones:** sink on this thing, Um, well, it's basically the largest one on the board here. So, that's telling us that we're well, we've got a linear voltage regulator. So, even though this is a switch mode power supply, we're looking

**Dave Jones:** at possibly um not any active switch mode regulation on the secondary side over here. We've got a linear regulator. So, what that points to is just a simple uh bridge rectifier or you know, a diode halfway the secondary side and then just

**Dave Jones:** going into the caps and then we're just got linear regulators. Now, there's another device down in here. You know, you can't get in here to read any of this stuff. It's ridiculous. Anyway, now these two here on small heat sinks,

**Dave Jones:** these are diodes. Not sure if they're primary or secondary, but they got CR on them and I can see that's an actual diode in there. Trust me about that. Here's our mains coming in over here. We've got our bridge rectifiers going to

**Dave Jones:** our main filter caps here and then obviously, yeah, this is this is all the connections for the primary side of the transformer there. And then we're going to have some optocoupler feedback somewhere. There they are. Optocouplers. They look weird, but yep, old school

**Dave Jones:** package optocouplers there. So, we've got some feedback, but I don't necessarily think it's doing much in terms of secondary regulation. As I said, we've got that linear regulator there. So, anyway, primary side and then secondary side here. We've got some

**Dave Jones:** extra stuff in here. So, yep, this diode over here is on the secondary side and the other diode on the heat sink here also on the secondary side. So, what we're looking for probably is like a classic culprit in these is blown

**Dave Jones:** rectifier diodes. I have to link in the was HP oscilloscope repair where we had a really remarkable and really elusive thermal fault in so Oh, no, spoiler alert. No. No. No. Follow along. I'll link it in. Anyway, interesting. My

**Dave Jones:** first suspect would be a diode in there somewhere. So, we'll just check these two biggies and then Well, I can see a couple of diodes really deep down in there. I don't know how I'm going to get down and measure a couple

**Dave Jones:** of those. We'll have to flip it over and measure from the bottom. Man. Cross our fingers we don't get the wrong pin. Measuring diodes in circuit not always the best thing. The one over here is here. So, 0.07

**Dave Jones:** V. 0.072. Aha. Well, that could be low in certain impedance. 0.03. No. Okay. That maybe low in certain impedance. We can go over and measure our own's, but I suspect So, yeah, 67 one way. Yep. So, they're not shorted,

**Dave Jones:** but that doesn't indicate that they're dead ski. So, what we're looking for of course is not a shorted diode cuz we're measuring like nothing I believe there was like nothing on those rails. So, it wasn't popping any caps. It wasn't doing anything. So,

**Dave Jones:** the diode was shorted, we might be in a spot of bother. You know, it could blow something up or you know, it's going to cause issues. So, I would suspect that probably like more than likely like a diode's gone open somewhere. So, bit of

**Dave Jones:** light to get down in there. And what do we got? Aha. 7912. There you go. Negative That's our negative 12 V regulator. That's not much of a heat sink, is it? For your negative minus 12. So, yeah, but probably not

**Dave Jones:** like for the minus 12 V it'd be like for RS232 or something. You wouldn't really need it for much. Hence the tiny heatsink but there's another device on the other side in there which I can't so some people wondering why we can't

**Dave Jones:** measure those diodes are hard are they short or are they open or whatever well look at these big ass resistors down in here they're probably bleed resistors directly across these caps here these are very common they discharge the caps very quickly if

**Dave Jones:** you turn the supply off so it's a regular halfway rectifier and then you've got a resistor in there you've got the couple of ohms in the secondary side turning here plus you know however you know they might be you know a couple

**Dave Jones:** of hundred ohms down there so effectively either way you're measuring the diode you effectively got like maybe you know a hundred or a couple of hundred ohms in parallel with your diode and that doesn't really let you measure the

**Dave Jones:** diode in circuit probably have to take these out to measure them but that would be a red herring because I know they're not associated with this and I can't really film down there but I was able to get in with a magnifying loop I get in

**Dave Jones:** there turn it the right angle with the light at the right angle and that's a 79 05 so bingo there's our minus 5 and minus 12 volt regulators on the one heatsink so hopefully you can see the cramped area I've got to work with

**Dave Jones:** anyway I can see two diodes down there one is horizontal and the other is tucked under that white gunk between the white silicon between the capacitors there and that one's a vertical jobby that looks bigger so I'd say the

**Dave Jones:** bigger one is probably for the like the minus 12 okay so what we've got three pins there three pins there and the center pin on both of those is going to be the input well any 79 series voltage

**Dave Jones:** reg and the one on this sorry this is a 12 volt this is a 5 volt so this one ground over here should be ground and certainly it is and then of course the trace goes around there to

**Dave Jones:** match this one that's ground okay so I can't remember which pin is our negative 5 volts but we can find that there it is as our negative 5 volts and our negative 12 volts will be there you go as our negative 12 because

**Dave Jones:** the 5 volts is almost certainly fed from the 12 volts so that would be my guess but we can check that so this is our 5 volt input here is that coming from our 12 volt output there and

**Dave Jones:** yes it is no worries so that explains why both rails are dead because the if the we don't get our minus 12 volts out then we're not going to get our minus 5 volts out so both of those are cactus so

**Dave Jones:** either we're not getting involved is to the 12 volt output or the 12 or the 7912 is dead it could be either those things so our Dave CAD reverse engineering drawing is going to look something like this we've got our transformer we've got

**Dave Jones:** our secondary tap I think it's probably only going to be a like half wave rectifier diode in there and yes you'll notice that I drew my capacitors backwards cuz I'm an absolute twit anyway yeah positive on the on the ground side there cuz it's

**Dave Jones:** negative so we're getting negative whatever voltage out of here you know a couple of volts above 12 at least and then you've got to take into account ripple and all the rest of it so anyway it's probably significantly higher so we've

**Dave Jones:** got our 7912 and then that just powers the 7905 and then we'll have some output capacitance as well also drawn in backwards but I got that one right got that one right and what you'd do as well as you'd go in there and you'd have a

**Dave Jones:** squeeze around the magnifying loop to which I use my macro lens for my camera. Um, works great. Times 10 macro lens. And uh, just look for any cracked joints or anything like that, cuz that could be the problem. May not actually be a

**Dave Jones:** component thing. And with this uh, power good here, with this LMR339 quad comparator, what's going on here is a rough sketch. Um, we've got all the power supplies coming in. There might be more than this. It'll be +5, +12, -12,

**Dave Jones:** -5. Should have drawn an extra one there. But they all basically uh, go into uh, comparators here. Uh, there'll be a voltage reference on these pins. So it's basically, you know, are they uh, like below a certain uh, spec? So 5

**Dave Jones:** volts you might put, you know, 4.75. Is Is it above that? Your typical uh, 5%? Then it gives, "Okay, I'm good." And how they're doing this diode arrangement here, you could do it like as an AND array or an OR array. It depends how you

**Dave Jones:** actually configure it and how you configure the positive negative inputs here and how you actually uh, compare them. But anyway, basically the idea is that um, yeah, this will give a output happy um, if all of the inputs here are

**Dave Jones:** above their thresholds. That's it. Okay, so let's follow the input pin of that regulator. And the There's one diode here, but it's got a little signal trace going out of it. Not sure if Yeah, you should be able to see that. Um, so I'm

**Dave Jones:** not sure it's that. And the other big one here. So let's try this. So it should be a nope. And nope-y-dope. And nope-y-dope. Oh, that one's There we go. We've got a charge discharge thing. And so therefore, yes, it must be. I'm

**Dave Jones:** bi- Like, of course it's the last one we checked. Um, so yeah. So that large diode, that's the vertical one in there. That looks like a big uh, 1 watt uh, jobby. Let's go to diode-y mode. Uh, that's all right.

**Dave Jones:** And the other way around is open. Okay, I'm just going to uh, power this sucker up here. Uh, I managed to do when I disconnected the fan, I was managed to, uh, get it out of the chassis. Just no

**Dave Jones:** touchy all of this section here on the primary side. Here we go. It shouldn't need a, uh, load. It should be okay, but yeah, there's our 5-V rail, 5.1, no worries. And it drains pretty quick with no load.

**Dave Jones:** They must have a, uh, output, uh, drain resistor on it. And we'll just verify plus 12. Yep, no worries. And that one drains, yep, quick, too. Okay, I've got a clip in there going to our do our output of our transformer tap there. So,

**Dave Jones:** let's have a look. So, we should, um, it well, it's it'll give us AC, won't it? Nothing. Wow. Really? Nothing out of the transformer? In VFD mode on there? What? .3 out of the tap of the transformer? So, I, yeah, I've got circuit ground and

**Dave Jones:** that doesn't make sense at all. And I can't actually I'll show you, it's too deep down in there, but I can actually see that the, uh, point of the diode I'm probing actually goes over to, um, the pin on the transformer. So, uh,

**Dave Jones:** what the? Ah! You're not going to believe it. Please, uh, answers in the comments down below. I found it. I found the problem. It's Hang on, I'll get that. Come out, you bastard. Show yourself. There's the ugly turd.

**Dave Jones:** There it is. Can you see that orange wire down in there? That is the transformer tap for the negative, um, the 12-V and negative 5-V rail. It was It's like it's come off. So, like, I don't know. Is this just like cuz this

**Dave Jones:** is just flapping around in the breeze. I think this is just vibrated loose over the years. Um, you know, the fan, it's got a, you know, 240 V fan on there. I'm not sure how much this thing's going to

**Dave Jones:** vibrate, but that's what it was was. So, tracing down all that Well, there could be something wrong with the circuitry. I I don't know, but um, yeah, the bloody wire. Unbelievable. Wow, could have really chased a red herring down a rabbit hole there um,

**Dave Jones:** just for the sake of a wire because like, you know, like you see it for look like it for all the world that was connected down to that point, but it damn well wasn't. Unbelievable. No wonder we'll get naff all out of it.

**Dave Jones:** There it is there. Can't quite see it. Is that a single strand? Yeah, that's a single strand jobbie, I think. It's just broken off from the board. Unbelievable. There's not much late length left on that. Going to attempt to

**Dave Jones:** get in there and strip that. This is a real dog. What the hell kind of insulation is on there? Unbelievable. It was a real dog to get that out, let me tell you. So, yeah, I got to uh

**Dave Jones:** get in there with the needle nose pliers and feed that back down. Yeah, it's not easy to get these damn connectors out either. Um, so I might take the whole chassis over or bring the soldering iron over to here.

**Dave Jones:** Ah. So, here's the tap here, these two pins. So, this one goes to ground, obviously, and this one goes over to our diode over here like this. There'll be our filter caps in there and then or somewhere and

**Dave Jones:** uh then that'll go directly into over to there um, and that's the input to our -12 V regulator. So, I've cleaned out that hole, so I should be able to feed in the wire from the top um, and hold my

**Dave Jones:** tongue at the right angle and hopefully it'll get through and then hold it with your finger on the other side and then solder from this side cuz you don't want to be soldering from the top. This is just ridiculous, seriously. You got no

**Dave Jones:** idea. It's right back under the transformer. Sorry, I can't show Oh, did I get it? I think I might have got it. Hang on, stay in there, you bastard. I think it's going to stay in there because it's a single core, so it's

**Dave Jones:** stiff as. OH, YEAH. YEAH, good enough for Australia. Yep, there we go. Can see something there. So, let's solder that back. It's got enough length on there. Should be right. Flow that through and we're good to go. Uh always give it a tug

**Dave Jones:** afterwards just to make sure. Yep. Yep, tug test complete. I think we're good to go. All right, let's power this thing up. Uh so, this probably hasn't been powered up for quite some time. Look, I don't know when

**Dave Jones:** it broke or how under what circumstances, but obviously our -12 and -5 Well, I think I've never powered up since I've had it. So, yeah, could blow something. Who knows? Release the magic smoke. But anyway, let's give it a

**Dave Jones:** whirl. -5. Yes. Winner, winner, chicken dinner. So, if our -5 works, that means our -12 works as well. Hello, -12. Let's do that again. -5.

**Dave Jones:** -12. There we go. I think I think the I just moved my ground probe. I don't think it was making loosey-goosey in the contacts. But there you go, fixed. Winner, winner, chicken dinner. So, I have absolutely no doubt that we'll be

**Dave Jones:** getting our power good signal here cuz but Murphy might say that well, something in the power good circuitry is fouled as well. But no, look, it's going to be doing going to be doing its business. There you go. That would have

**Dave Jones:** been my last guess. That was a wire tap on the secondary of the switching transformer. You you don't normally get this cuz usually they go in via a connector, of course. But this one, no, it's hardwired into the board. But not only is it hardwired

**Dave Jones:** into the board, doesn't use any of that stranded rubbish, uses single core. And of course, uh the thing with single core is that if it gets uh vibration and flex and everything else, um then it can, you know, it can break off fairly easily.

**Dave Jones:** That's why, like, uh your high-quality multimeter probes, for example, if we cut these apart, these might be like, you know, a couple of hundred strands of wire, like the real good silicone uh ones with the like the real super

**Dave Jones:** flexible ones. But basically, you know, regular uh stranded wire might be, you know, seven strands of 0.1 mm or something like that, uh for example. And of course, you know, it gives you uh redundancy, it makes them reasonably

**Dave Jones:** flexible. But uh using the solid core wires on there causes to come a gutter. Wow, I'm I'm actually glad it was that and just not a, you know, which is the most common fault, might be a like an

**Dave Jones:** open um diode or something like that or even the regulator, really, although, you know, usually diodes are file before the regulators would, but yeah, I've at least we got something interesting out of that. How long has this been

**Dave Jones:** going? 20 minutes at least. And we can actually measure out power good signal, which is pin two here. And there you go, it's 5 V. Yeah, I we were getting zero before, weren't we? So the power good So

**Dave Jones:** I have no doubt that this thing will now power up our motherboard over there. No worries, but I've got to assemble it all in the case for it to do this, so that's really annoying. So that's not something

**Dave Jones:** I'm going to do uh for today's video. So yeah, I got to like reassemble the whole thing and then, you know, see if the CRT works and all that. But you've already seen that the uh motherboard works, we

**Dave Jones:** got video out of that, and we knew uh we traced it down that it actually came from uh the failed uh power good on the power supply, and that failed because our -5 and -12 were gone, but even if we

**Dave Jones:** have one of those rails go. Anyway, that was simple, but even simple ones can be interesting. So hope you learned something and found that useful. If you did, please give it a big thumbs up. As always, discuss, comment, and down

**Dave Jones:** below. Catch you next time. But wait, hang on. I just remembered that somebody, uh the viewer, thank you very much, uh sent me in the link to the schematic, which I had. I got this a while back. I forgot I

**Dave Jones:** had it, so that would have helped. Anyway, let's go in and have a look. I believe it's the same one. It's the compact portable. This is the portable plus, but that's pretty much only uh it has like a hard drive and some upgraded

**Dave Jones:** ROM or something like that. So, anyway, Howard W. Sams & Co. Computer Facts. And we'll see why this is a Howard W. Sams & Co. uh is important in a minute. Printed in the United States of Am- Oh, you

**Dave Jones:** can't see that. But printed in the United States of America. Anyway, um so, yeah, for those aficionados here, here's all the uh digitally stuff, but we do have the power supply in here. Taken while pressing space bar. There

**Dave Jones:** you go. Look at nice nice annotations on the schematic. Absolutely brilliant. And uh anyway, let's go down to the power supply. Um that's the part that we want, and we do have it. Thank you very much. There you

**Dave Jones:** go. Um beautiful. All on uh one mostly on one sheet, although I don't like how it sort of like goes off here. It's like you know, all these like jump off like down here. It's like uh it's Anyway, um and we do have an extra one

**Dave Jones:** over here, which just has then these letters come over here, and then these are the ones that actually go to the connectors over here. But anyway, as you can see, mains in here. We've got some chokety chokes. We've got a full wave

**Dave Jones:** bridge rectifier. Then we've got our big mains filter caps. They've got some big bleed resistors across there. And uh basically, yeah, this is all just uh primary side switching here. And then it looks like it does have a feedback coil

**Dave Jones:** here, cuz that's feeding back without opto isolation into there. Yeah, yeah, and they've got little Yeah, if you really to go in there and analyze it, they got uh scope shots. But, of course, we didn't need the schematic, we didn't

**Dave Jones:** need the scope. It was fairly easy. But, you know, if we had to go in there and, you know, this diode here was you know, something in here with this cap was bust or something, you know, like you might

**Dave Jones:** have some issues. You might have to go in there and scope out waveforms and stuff. Luckily, we just had a broken wire. So, but yeah, this is handy. And, of course, on the secondary side, and yep, as I suspected, here's our 12-V LM

**Dave Jones:** 338K. I suspected that was the highest power one, and it was certainly. And, yep, we've just got a single half-wave rectifier there. There's no filter caps for that one, so they must be on the other page. Yes, they are.

**Dave Jones:** There you go. That's the 12-V source. And, as you can see, yes, it's got a 680-ohm resistor across here. This one up here has got 233K 2-W resistors. There you go. So, that's why the voltage was bleeding down, and that's why I'll

**Dave Jones:** show you in a sec. In fact, let's go into this. So, if we zoom into here, okay, so we've got our 12-V regulator here. No worries. But, this is the diode that we were These are the two diodes

**Dave Jones:** that we were measuring here. And, of course, look, this one here. Look, here it is. 68 ohms. This is your loop right here. So, if you're trying to probe your diode here and here, regardless of which way you put your probes, you're

**Dave Jones:** essentially got 68 ohms here in series with whatever this coil is. It's going to be, you know, tens of ohms tops, right? So, you got well under 100 ohms in parallel with the diode you're trying to measure. This is why you can come a

**Dave Jones:** gutser trying to read diodes in circuit like this. You might think, "Ooh, it's measuring, you know, 50 ohms both ways or something, and it must be shorted, you know, it must have like a or a high impedance short out" or

**Dave Jones:** something like that. Well, no, you've got to think about the rest of the circuit here and how there might be a bleed resistors like this in parallel. So, yep, that's what they've got here. Oh, sorry, I was getting carried away. I

**Dave Jones:** think this is the 5-V C. Let's Let's go to the next page. C C C, yes, 5 V here. That's it. Um What's So, there's no regulation for the 5 V? Really? It looks like they've just got a big

**Dave Jones:** Zener. If we look down that one one up, I think we'll find that's a 5.1 V Zener. Yeah, I couldn't get that readily, but yeah, oh, it's 5.6 V. A 5-W general-purpose voltage reference regulator diode. Well, that's a bit how

**Dave Jones:** you doing, isn't it? I mean, they go to the effort to use a a proper linear reg up here for the 12-V rail, but for the 5-V rail, they've just got a lousy a lousy Zener in there. Oh, that's

**Dave Jones:** terrible, Muriel. Anyway, here's our -12 and -5. And yep, the -5 is connected just through to the -12 V there. And yep, we've also got a 330-Ω 2-W in parallel here. So, that's why you have a hard time measuring these diodes

**Dave Jones:** in circuit. So, now, if we go check out our power good circuit. So, yep, there you go. There's our diode and gate there. And yep, LM339 voltage regulator. And this will be, as I said, it'll be coming so you got +12, -5, -12, uh etc.

**Dave Jones:** And then, yeah, you got some resistive dividers. And then, a voltage reference will be coming. Yep, it even says reference over here. Voltage reference. Yep, there it is, 2.5-V voltage reference TL431. Classic for those playing along at home. And then, we've

**Dave Jones:** got some opto-isolators and stuff like that. So, there you go. That is That is the schematic. So, that's exactly what we deduced it to be during the troubleshooting that, you know, it was just obvious this is what it was, that it wasn't actually that it

**Dave Jones:** had linear regulation on the secondary side and it wasn't doing any secondary side switch-mode regulation. Now, this is the interesting thing. I posted this on Twitter a photo fact standard notation schematic with circuit trace. Copyright Howard W. Sams & Co. 1987.

**Dave Jones:** Well, apparently this dates from like the '60s or something. We'll briefly look at this cuz it's kind of interesting. So, I posted this on Twitter and the tweet of course came through. The Scott Death Palm, the Sams photo fact, the service manuals

**Dave Jones:** published by Sams. They did a lot of manuals for all CB and amateur radios in the '80s. But, they did manuals for other types of equipment, too. And Peter, thank you very much. Bring. I'm butchering that pronunciation. Unlocking the component PCB mystery. So,

**Dave Jones:** I still don't quite understand it, but we've got an info thing, but it seems to be basically putting annotation and stuff on schematics and things like that. And here's a I guess they're a brochure. Now, photo fact helps you lick printed

**Dave Jones:** circuit board troubles in seconds. Exclusive use of Sams CircuiTrace. Features eliminate costly hunting for test points. No more maze to trace. No need to flip flop board, which means, you know, turn it up and up, bottom to top, which is what we were doing trying

**Dave Jones:** to trace out where the traces are going. Here's how CircuiTrace works for you. All test points are clearly shown on the schematic and is plainly coded. The test points are similarly coded on the printed circuit board, so you instantly know. Are they?

**Dave Jones:** Well, like is it just like they take photos? And so, I don't actually know what the product actually is. You know, write for your free photo fact. Think I like September 1958. That is great, right? So, this is like

**Dave Jones:** the late '50s. This CircuiTrace stuff. And like it was still I was still using it in the '80s, apparently. So, yeah, it was still a thing. Please leave it in the comments down below if you used CircuiTrace or not. So, yeah, I

**Dave Jones:** still don't know exactly like what they're actually selling here. Is it some sort of documentation camera then that links how does it like I don't I have no idea. Anyway, hope you found that interesting and once again, if you

**Dave Jones:** did, give it a big thumbs up. Catch you next time.
