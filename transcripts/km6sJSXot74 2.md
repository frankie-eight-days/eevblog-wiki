---
video_id: km6sJSXot74
title: EEVblog 1707 - REPAIR: Goal Zero Yeti 400 Lithium Battery
url: https://www.youtube.com/watch?v=km6sJSXot74
source: youtube-asr
timestamps: {"0": 0, "1": 35, "2": 65, "3": 93, "4": 121, "5": 146, "6": 177, "7": 201, "8": 219, "9": 248, "10": 265, "11": 300, "12": 329, "13": 359, "14": 370, "15": 400, "16": 428, "17": 459, "18": 492, "19": 519, "20": 544, "21": 564, "22": 601, "23": 635, "24": 666, "25": 679, "26": 698, "27": 712, "28": 734, "29": 752, "30": 775, "31": 796, "32": 807, "33": 841, "34": 871, "35": 894, "36": 922, "37": 935, "38": 949, "39": 980, "40": 998, "41": 1012, "42": 1039, "43": 1065, "44": 1099, "45": 1127, "46": 1161, "47": 1192, "48": 1219, "49": 1249, "50": 1277, "51": 1290}
---

**Dave Jones:** Hi, it's repair time. This one's from home. It's my old Goal Zero Yeti 400. As the name suggests, 400 watt hour battery. It's one of these, you know, little portable things. We use it to take camping. We just used it like 6 months ago for camping. It's been working great for years. You might have seen this in one of my second channel videos. This one actually powers my solar assistant Raspberry Pi from the USB output here. And that does all my solar monitoring from the DI inverter.

**Dave Jones:** And well, I've got to admit, it looks like I've goofed it because this thing ordinarily powers that Raspberry Pi, but I was mucking around with my solar setup at home and I actually like normally it's powered from this external plug pack here which can power from like, you know, external solar panel up to never exceed 22 volts input here. This is like a 16 volt plug pack. And it's normally just floats at 100% there and unless actually take it somewhere and use it. And it powers that Raspberry Pi,

**Dave Jones:** but unfortunately, I was mucking around with it and I accidentally disconnected the mains to it. So my Raspberry Pi solar assistant worked for like a week or something until it suddenly stopped working. And I, you know, was checking my solar thing on my shoe phone and it's like, it's not talking. Oh, it might need to reboot it or something. And I went back out and went out there to investigate and sure enough, this battery was completely flat. Womp womp womp womp. And this is what happens when

**Dave Jones:** I plug it in. Watch this. Hopefully, you'll see there's an input lead here and you might see this screen actually light up briefly and this lead comes up. It It just Yeah, it flashes off and it looks like it doesn't charge at all. So it looks like it's drained to a point where it can't charge anymore, which is a design oversight of this Goal Zero Yeah, yeah, you saw it actually flash again.

**Dave Jones:** It sort of periodically does that, but I've actually left it on there for many days, actually, you know, hoping that it'll just eventually recover or whatever. Um and it doesn't. So, yeah, um that's a bad design. Yep, yep, there we go. It just It just hiccuped again and tried to start, but as I said, left it there for days and it doesn't seem to overcome this. So, it looks like the internal batteries have drained to a point where it just can't start up at the charging

**Dave Jones:** system or whatever, and it just doesn't recover. So, it basically killed itself by letting itself run flat, which is, yeah, dumb. This is like a really old model. I don't have done it, you know, it's not current. They've got, you know, several generations um beyond this one now, but um yeah, it's always been a good little unit. So, that's But, I've never actually let it drain down to absolute zero before. So, if it's some other fault, it's a genuinely huge coincidence. But, no, I think I did it by just draining this

**Dave Jones:** thing, sucking, you know, a couple of watts out of here to drive a Raspberry Pi, leave it running for a week, and eventually wah wah wah wah. Anyway, let's see if we can open this thing. So, I am actually down here in the dungeon cuz I don't want to work on like relatively high-capacity lithium-ion batteries up in the lab, you know, if a fire happens, I do have my fire extinguisher down here, and there's no fire sensor down in here. So, I'm not going to get an $1,800 bill. Um I am

**Dave Jones:** using my Swiss tools set. Somebody personalized this for me and sent it in through the mailbag like a donkey's years ago. Let's crack into this thing. I don't think I've ever done a teardown of this Oh. Oh. That's just Oh, that's that's plastic.

**Dave Jones:** TURN IT OH, AFTER THAT'S THE HANDLE. OH GOD, I WAS FOOLED. THERE YOU GO, LIFT that up. Oh, that didn't make sense. So, yeah, they molded it that in there just to confuse me. So, yeah, I might have uh just opened this up. Oh, wait. Yes, I might have opened this up myself once, but uh I've never Oh, that's That's nice. That just comes off. There's nothing nothing in there at all. So, yeah, I don't think I've ever done a teardown video of this. Let's have a squeeze. Oh,

**Dave Jones:** that looks pretty neat, does it not? Uh I don't have my regular poker here. It's gone missing, but uh yeah, we've got our big heat sink along there. We've got uh seal pads there for our drivers, and there's another couple of devices down there with some seal pads.

**Dave Jones:** Um anyway, this looks pretty neat. Uh that's interesting. Um input blade fuses there. Um didn't expect to see those, but I guess that makes sense. Anyway, um that's obviously coming from uh the battery. Look at that, big and beefy. First thing I can do is actually uh measure that pack and see what it is because um probably the easiest way to fix this would be to use an external, you know, disconnect um all of this from the battery, and then uh sort of like slowly trickle charge the battery from

**Dave Jones:** an external supply, and get it back in business cuz I suspect that's what's happening here is that it's just drained to a point where it doesn't have enough voltage startup voltage um to start up, and some protective thing is kicking in, and it's just badly designed in the sense that it would allowed itself to actually drain uh below a point where it would actually um start back up. Got a fan on either side here, which is pretty decently uh designed. So, you know, it obviously sucks in one side and it blows out the

**Dave Jones:** other. That's what she said. Those caps don't look special at all. Sorry, this is not my best camera. This is not my best uh light down here. So, this board looks like just the uh 240-V mains inverter for it. So, we've got the battery coming in here, and the output, the uh 240-V output uh goes over here to the uh main socket on the front down there. It's only got like It's not It's not huge power. What is it uh 300 W, you know, 1,200 V um surge. You know, it's

**Dave Jones:** good for like little uh fridges and stuff when we're out uh camping and lights and other um sorts of things like that, but you know, nothing serious. Um you know, you're not going to go out there and use your power drill with it.

**Dave Jones:** And we've got another set of beefy red and black wires coming from the battery pack down there up to this main controller board up here. So, it it looks like two different heavy-duty wires coming from the battery pack down there. I was hoping not to have to take this completely apart cuz the battery pack's like down in here. It's I'm sure it's all messy to kind of like Although, it looks like Yeah, I I can get the I can There you go. I can just lift out

**Dave Jones:** the front panel there. That's pretty good. Oh, there you go. Look at that. Oh. Are they in-line Are they in-line connectors? We've got our rechargeable lithium-ion battery. There it is. Aha, found my uh yellow poker. I knew it was down here somewhere. So, those two big-ass battery wires, they're just soldered directly down in the PCB there. They're thick as. Got some switching transistors there.

**Dave Jones:** Uh and well, there's not much else doing. There's a processor on there, as you'd expect. That's driving all the front panel LCD. And it looks like it's just, you know, powering like the USB um outputs and stuff like that. We've got a cigarette lighter input here for those who remember the cigarette lighter in cars. Does anyone actually still use one? Uh there we go. Yep. Out of here as well. They're also going up to the main uh inverter uh board up there. So, there you go. That is a big-ass connector

**Dave Jones:** right there. I presume that they're just paralleled in there without taking all that out. I mean, it's not like they would you know split the battery or anything like that at all. Just be the one big series parallel banking there and they're just running separate wires out just from a you know a power distribution point of you know wiring distribution point of view. And one goes out to the AC inverter board on top and the other one just goes over to our main board here. So, well, I can actually measure

**Dave Jones:** that. Can measure the ohms key between two those two and it should be nothing. So, let's just do that. But yes, there you go. Yeah, they're just you know there might be some extra protection on the board up there. It's probably got some extra protection as I said there's some extra fusing up the top here on the mains input. Although this one down here, yeah, yep, yep, I see a oh yeah, it looks like they just have some SMD fusing there as well. But not as serious

**Dave Jones:** as the main side. And it looks like our BMS wiring. Although it could it could actually be on the main board and they might just be tapping these off. This actually just joins into It's interesting. It goes from this wiring harness into this ribbon cable here via this inline connector here. So, that's rather unusual. There you go. It's 10.8 V pack. That's lower than I thought.

**Dave Jones:** 40 amp hours there. 427 watt hours nominal capacity. Not sure what it have these days. It's not sure how long I've had this. Probably Oh jeez, it could be 10 years old. Not sure actually. There you go. We've got three extra pairs of switching transistors on the back of that heat sink as well we couldn't see before.

**Dave Jones:** Okay, let's see what voltage this thing is at. I'm going to be very disappointed if it's let itself drain down to something drastically small. Zero. Zero. Hello. DC volts. Yeah. You'll uh Beuller? Beuller? Well, what's obviously going on here is that some sort of a protection board on here which will have over voltage protection, it'll have under voltage protection and under voltage lockout, which is what it's probably doing here. I mean, there's no electrochemistry reason why this battery is at absolute zero just from, you know, doing this. So,

**Dave Jones:** obviously, it's gotten below a threshold on the battery protection on there where it's literally disconnected the battery to actually protect itself. So, at least they did something right cuz otherwise there's no way we're going to be reading zero on there. So, I think I suspect I'm pretty reasonably confident that once we connect an external supply to this thing, that will then overcome that and it'll charge up. But why it's like sort of like doing that hiccup in, yeah, I'm not 100% sure yet. But anyway, I'm pretty confident that that battery

**Dave Jones:** hasn't like completely come and got sir. I think it's actually protected itself with under voltage lockout. And yeah, we can just should be able to get that started again. But why it can't do it on its own off its own bat, I don't know. That sucks. All right, everything's disconnected. So, let's just plug this in and see if it Yes, it comes on, stays on, and I'm not sure if you're seeing that with the light. It's flishy flashing at 20% there. Like it's doing something, but

**Dave Jones:** there's obviously they didn't design in an error indicator on this LCD cuz this is not a this is a like a segmented LCD, it's not a graphic LCD. All I had was a Raspberry Pi hooked up to the USB here.

**Dave Jones:** It should have intelligently, once the battery was low, it should have disabled the output here. Like what the heck crap design is this? Like Goal Zero is a pretty big brand. They're one of the like the leaders out there. Um granted, this is like a really old model, but damn, very disappointed.

**Dave Jones:** Next thing I want to try here is to hook the battery back up, but I'll leave the uh inverter up the top, that inverter board, I'll leave that flapping around in the breeze, and let's see if it it what it does now.

**Dave Jones:** Here we go. Yeah, whoa, whoa. Oh, oh, it's doing better. It's doing better. It's flashing better. Are you seeing that? Yeah, so it's flashing differently. It's like hiccuping very differently, almost consistently than what it does before when it had, I guess, the extra load of that inverter board on the top there.

**Dave Jones:** Look at it. That's one sick puppy. Oh, I can get in there and measure the voltage actually at the same time. I can disconnect the negative here to see if it's actually attempting to do something. There you go. It's attempting to do something. There you go, 9.3 V.

**Dave Jones:** So, it's attempting to 9.34. 9.35. OH, 9.36. This is not drifting. This is like actually it looks like the battery is perhaps Oh, sorry. Are you seeing that? It is now. Yeah, 9.42. If I leave it 9.43. Come on, you can do it. Yes. 9.44.

**Dave Jones:** Come on. You can do it. It looks like it's slowly accepting a charge now. So, that is good. You know, I can hook on an external lab supply and try and slowly charge it and stuff, but oh, the little ring's come off. Um but, it looks like I don't have to. My Band-Aid's falling off.

**Dave Jones:** There we go. I'll take that off. Ah, put a new one on before I get to the gym tonight. So, I'm going to actually leave that cuz I'm just Oh, oh, look. LOOK. IT'S OH, IT'S PERMANENTLY ON NOW. YEP.

**Dave Jones:** YEP, it's permanently on. It is charging. Input 53 watts, 50 watts. There you go. So, it's char it's charging the battery. All I had to do was disconnect the inverter up here. It was drawing too much like peak load when it was coming on when the battery was flat, I guess so to speak. But, I'm pretty confident that well that that 50 watts has to be going somewhere and it's actually measuring that using a current shunt on the board somewhere. It's actually measuring uh the input power going to the battery.

**Dave Jones:** So, it looks like it's accepted a charge. Just the mere threat the mere threat of me um getting out the big guns, getting out the benchtop power supply and threatening uh it with a good time, that it's said, "Okay, I will cooperate and I will start charging." But, yeah, that's interesting. So, now I expect there to be nothing wrong with this thing. Yeah, it's definitely now accepting a charge. So, that 50 watts is going into the battery. No worries whatsoever. So, I'll come back in an

**Dave Jones:** hour or two and I suspect what's going to happen is once that battery is uh got sufficient charge to now boot this thing um on like normal, then we can hook up uh rehook up the uh 240 volt uh mains inverter in there and then that's obviously taking some surge current in there that the processor or something didn't like and then it was hiccuping the actual processor was hiccuping.

**Dave Jones:** That's uh called that flashing that we uh saw before. It was trying to start up, but that inverter up there had too big a input capacitance on it and it just didn't like it and it was like, "Nah, nah, I'm going to shut back down." And then it tries to start up again period and then it not shuts down again. But, because there's very little uh like capacitance in here uh for example, very little uh surge uh current to charge up when you initially uh turn it on, it the

**Dave Jones:** processor um in there, the controller was just happy with that. Now it's cooperating. So, um yeah, I think once that's back up in business, I expect to be able to hook that back up, and Bob's your uncle, I think that's our repair.

**Dave Jones:** Sorry, another one of my it's interesting, but I don't think there's going to be an electronics repair here. I think it's um didn't even have to get out lab power supply. Ah, well, I'm going to call that a win. What are we up to at the moment?

**Dave Jones:** Oh, yeah, 9.91. Come on, you can do it. Anyway, I got to say I do otherwise like uh the construction of this thing. It's a big extruded aluminum uh case like this. It's very nice with just a cutout uh in the front. So, it's like rugged as, and these plastic inserts just like slide into here, so they're not going to come off unless you absolutely like uh smash them off or slide them um up. Same thing with the uh grills. They've got like big uh deep grooves in there, so they slide

**Dave Jones:** in. So, it's a it's a really nice um physical design. I I rather like it. It's just a shame that uh they allowed the damn thing to like kill itself by draining itself. Unbelievable Yeah, you had one job. Just turn off once the battery reaches low.

**Dave Jones:** Ah, it's not rocket science. Actually, what I'm going to do is I'm going to disconnect that. Oh, that's right, I can't actually switch this off. Um it's like it's it's got a light button, but it basically stays on like all the time.

**Dave Jones:** See if it's held that. Yes, 9.91 volts. Oh, there we go, just dropped to 9.90. Maybe, but you know, it's it's barely even got any charge in it at the moment. So, All right, I'm back from the gym. I got new Band-Aids, and they held. So, we are at 38%. That's not too shabby. So, that looks like it's just charging exactly like it normally would. So, that should now have plenty of juice in it.

**Dave Jones:** There we go, 11.04 V. No worries. So, I think I'll hook up the AC inverter back and I think we'll be right. I'll manage the cables again before I put it back together. That is probably like switching the power through No, no, that comes straight from the battery. So, that's going straight on there and then they'll have the signal coming from this over here. So, we're still good. Let's turn the inverter on.

**Dave Jones:** Oh, that's all right. I've got the output disconnected. Output 11 W. Yeah, it actually draws a substantial amount of quiescent current just sitting there switching its little pants off. I've got it fed up the clacker there. And oh, yep, there it is. 230 V I've got to set for. No, this is 245 V I get here in the lab rubbish. So, that looks like my theory was correct in that yeah, this thing just went into undervoltage lockout on the battery management or the battery protection in there. It's

**Dave Jones:** not the battery management system. The management system has to do with like the charging and the cell balancing and stuff like that. Still not sure if that's done under there or because they got multiple wires coming out here, it might be done by that PIC micro in there. But anyway, that's neither here nor there. So, it could not get out of that undervoltage lockout and start recharging itself while the AC inverter was connected cuz it had like too much load on it that was just preventing the

**Dave Jones:** battery protection in there from coming back on. Or the exact mechanism we don't know until unless we've got the schematic and we did further investigation. But there you go, that's an interesting thing. I don't know like is there I'll be generous to them and say it could be the fact that this is quite an old battery. I haven't cycled it a lot, but it is actually quite old. So, maybe with its age, the ESR's increased and that didn't give it enough juice, but it just to like start up an inverter like this,

**Dave Jones:** it's not That's not a massive amount of inrush current or Well, you know, I don't know. Thoughts in the comments down below, but jeez, let that be a lesson to you. When you're designing a battery like this, make sure you actually design it to be drained down and then, like absolutely use the heck out of it and then like I would use like really depleted age batteries on the thing as part of the testing and part of the design testing for this thing to make sure that yeah, it can actually

**Dave Jones:** start up and charge again. But, the damn thing couldn't with that load on there, but once I removed the AC inverter load, Bob's your uncle and she was able to recover. So, maybe they could have had the undervoltage lockout just set too low and it just didn't have the juice available to do it, but I Given that this thing does not have an actual power switch, I I kid you not, right? That else like you can probably see it. That LCD is still on. So, that micro is still

**Dave Jones:** running. The LCD's still going, but granted that could take, you know, like microamps, right? Tens of my microamps just to keep that small segmented LCD going, so didn't take a lot, but ultimately, you know, could eventually drain down, but great like I was using the USB-C output on here, but this the micro here, this PIC micro should have determined that Oh, okay, battery like, you know, should get low battery and then shut off the USB output here, where I don't think it did. I think it just

**Dave Jones:** kept it on like I wasn't there to watch it in real time, but I could test that, but I'm not going to do it in this video. Um, but yeah, I assume that it just it just kept pumping out powering my Raspberry Pi Pi doing the absolute best it could to power my load and it didn't shut down and preserve itself and it completely come a gutsa couldn't restart. So, yeah, that is a wah wah wah wah fail in the design of this thing. So, there you go. That is

**Dave Jones:** not an electronics repair, but that is interesting nonetheless. So, if you did find it interesting, give it a big thumbs up. As always, discuss down below and over on the EEVblog forum, of course, the best forum on the interwebs.

**Dave Jones:** And if you want to get my meters, you can get those on EEVblog.store. Catch you next time.
