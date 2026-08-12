---
video_id: f-LTv1GqCMw
title: Brymen BM786 Power On Fault Investigation
url: https://www.youtube.com/watch?v=f-LTv1GqCMw
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 23, "3": 36, "4": 52, "5": 62, "6": 72, "7": 82, "8": 92, "9": 101, "10": 123, "11": 136, "12": 146, "13": 159, "14": 168, "15": 180, "16": 196, "17": 211, "18": 228, "19": 252, "20": 278, "21": 288, "22": 297, "23": 309, "24": 319, "25": 334, "26": 351, "27": 372, "28": 383, "29": 395, "30": 406, "31": 415, "32": 440, "33": 447, "34": 469, "35": 479, "36": 493, "37": 503, "38": 516, "39": 530, "40": 540, "41": 550, "42": 559, "43": 568, "44": 579, "45": 591, "46": 610, "47": 619, "48": 632, "49": 641, "50": 657, "51": 670, "52": 681, "53": 694, "54": 705, "55": 712, "56": 724, "57": 737, "58": 748, "59": 760, "60": 769, "61": 784, "62": 795, "63": 802, "64": 813, "65": 826, "66": 837, "67": 848, "68": 861, "69": 873, "70": 882, "71": 902, "72": 916, "73": 928, "74": 935, "75": 948, "76": 958, "77": 969, "78": 982, "79": 993, "80": 1008, "81": 1016, "82": 1031, "83": 1045, "84": 1060, "85": 1073, "86": 1081, "87": 1090, "88": 1103, "89": 1117, "90": 1129, "91": 1140, "92": 1153, "93": 1167, "94": 1180, "95": 1193, "96": 1206, "97": 1214, "98": 1222, "99": 1234, "100": 1244, "101": 1258, "102": 1270, "103": 1287, "104": 1298, "105": 1323}
---

**Dave Jones:** First place you saw it on Twitter. Yeah. Yeah, I'm now is for those who don't know, I am now posting my videos natively on Twitter. Twitter is going to be huge.

**Dave Jones:** Mark my words. Twitter is if you're a video content creator and you're not on Twitter, you are nuts. You are nuts. Get on it now. I'm telling you. Because I am having a look at today a returned BM786.

**Dave Jones:** In fact, I've got two returns. He's got back from the post office and I picked up two returned multimeters. Also, on Amazon, I'm getting a I swear I'm getting a flood of returned meters on Amazon.

**Dave Jones:** I don't know why. I can't get them back. But they I just get a customer return notification. I swear it's been increasing. I don't know why. But a lot of people on Amazon just return it cuz they didn't like the color or they didn't like that the manual didn't come with it or something like that.

**Dave Jones:** They they changed their mind. They found it cheaper somewhere else. So, they just returned They they use it for a day and then they return it, you know, cuz Amazon have that return policy, right?

**Dave Jones:** But uh the Brymen meters certainly aren't a zero uh failure rate. They're certainly not zero. Here's the uh notice. Um it is a forum user as well. I won't tell you the forum handle.

**Dave Jones:** Uh please see enclosed my BM786 is exhibiting a power issue. Sometimes the power will only come on at certain switch positions and other times it won't come on at all.

**Dave Jones:** That's interesting. I've tried my bench supply um and the issue persisted as well as cleaning the spring contacts and pads beneath. So, you know, he's had a good effort.

**Dave Jones:** Um it's not easy to use your lab supply cuz you can't Like I've I've had to like solder wires on and stuff to actually do that. Um so, yeah, we might have a look at that.

**Dave Jones:** But anyway, um yeah, let's let's let's take a look at it. One of the one of the issues with the 786 because of its unusual vertical battery compartment has been, if you don't screw these down properly, then the spring con then the contacts don't make um the contacts don't make contact with the PCB and then yeah, you might get intermittent.

**Dave Jones:** So, one of the things I that that feels like it's in solid. Yeah, that's that's that's tightened up. That's tightened up. Tight as a nun's nasty. All right. Let's turn it on.

**Dave Jones:** There. Yeah. Okay. Dead as a dodo. It might have taken out the batteries, of course. Yeah, the the other one I got returned just today. It's also got like some weird power thing Yeah, there's no batteries.

**Dave Jones:** Okay, there's some weird power thing. See, this is quite unusual. It's got the negative down here. It's got your traditional like leaf thing for the negative, but the negative's over here are the springs.

**Dave Jones:** So, it's rather unusual. So, yeah, I can see why they went for this vertical arrangement. I don't know. Does anyone know of another meter that has a vertical arrangement?

**Dave Jones:** Oh, yeah. Yeah, there you go. Solder. Solder on there. Yeah, so he's he's tried to solder a wire on there. I was wondering how you could do that without power from your bench supply without soldering and he's obviously soldered it on there.

**Dave Jones:** No worries. Yeah, and and the contacts are here. That goes down to the pad here, which the spring spring goes into. So, let's screw that back in. The solder on the pad won't make a difference.

**Dave Jones:** Course, if it's too lumpy, it could do that, but let's No. No. There we go. That's interesting. But you saw that, it didn't turn on instantly, did it? Look at that.

**Dave Jones:** Huh? Huh? It was working before and like when I came back in the position, it was working there, but it's not Wow, look at that. Now, I think this is the reported issue with the other one.

**Dave Jones:** So, the first two positions, it won't switch on. But when it gets to capacitance, it switches on. Isn't that weird? Is that That is thoroughly repeatable, right? Anywhere in the ohms range, and when you go to here is the battery the BATTERY OH, NO.

**Dave Jones:** WHOA. HANG ON. WHOA. WOW. That's a weird one, isn't it? I don't know. Anyone want to hazard a guess at that? I'm thinking it's not the switch. I'm thinking that you'd be chasing a red herring down a rabbit hole if you if you think it's the switch.

**Dave Jones:** I'm thinking like electronic power on switch. Doesn't this I think this has a Yeah, this has like a MOSFET to turn it on. I've done a video uh tracing that before.

**Dave Jones:** Um and maybe something to do with that. Now it's not working at all. Let me get the other one. And it had something weird like this as well saying it wouldn't come on or something.

**Dave Jones:** Like like it had come on sometimes and then you wouldn't be able to switch it back on. There you go. So, I This one's from somebody called Will. So, we have the Will.

**Dave Jones:** And let's let's try this. Might not be any batteries in it. Got it got it got it. Yeah, there's not showing low battery. So, the batteries are fine. Is this Yeah, there's no batteries in it.

**Dave Jones:** Check it out. I have no shortage of batteries because um I went through a period where DHL were refusing to ship my meters with batteries in them. So, temporarily I had to physically take them out.

**Dave Jones:** So, I've got And these are not all of them. Like I gave you know tons I've given tons away to people. So, they conveniently come in three packs. But I I now um ship the uh batteries with them cuz I've got the magic incantation words that they need to hear when shipping.

**Dave Jones:** No, nothing weird going on in there. It looks hunky-dory. Ah. Oh. Yeah, same thing. Same thing. I think WE GOT TWO. WOW. GIVE IT A WIGGLE, WIGGLE, WIGGLE. YEAH, but you saw that it it would not switch on.

**Dave Jones:** So, this person wasn't kidding, right? And they said like sometimes they would leave it off for an hour and then it would work or something or wouldn't work. I have to read their note again, but it was something you saw that, right?

**Dave Jones:** It would not switch on. It would not switch on and that's not good enough, right? There's something going on here. Although, this one's working a lot better. Is it like they leave it off for an hour?

**Dave Jones:** I don't know with the No, that one's okay. So, that one's working That one's working fairly consistently now, but you saw it, right? Bootstrap or race or time in race conditions.

**Dave Jones:** I I think it might be a bootstrap thing, Paul, in in that, um, I do believe there's a series MOSFET in there which they use, of course, to do the auto power off.

**Dave Jones:** Um, so I'm I'm thinking something like that. Take the batteries out and put them back in. Good point. Try banging on the table, okay? No. I I reckon this sucker is just going to See if I can do it fast and trick it.

**Dave Jones:** No, I can't. Can't trick it, but you saw it, right? Everyone saw it. Can people confirm that you had the first time I put these batteries in, it did not work.

**Dave Jones:** Anyway, it I think we've clearly got two meters with a very similar Uh, what's the serial number on these? 222 No, see they're a year apart. The last five digits is the actual serial number and then the four digits in front of that is the year or is the is the week and year.

**Dave Jones:** Yeah, yeah, I think it's week and year. So, the 22nd week 21, the 22nd week 22. So, they're a year apart. So, they're substantially different. Okay, here we go, right?

**Dave Jones:** It's off. Okay? Batteries I will just I don't know I didn't turn that on. Can I short it? It else not going to do anything. Okay? So, I'm going to plug that in.

**Dave Jones:** I'm going to switch it on. Damn it. Can somebody please confirm that it wasn't just me? This thing did actually fail the first time I just turned it on.

**Dave Jones:** Can somebody confirm that? It it it did fail. Thank you. Can confirm it it did fail at first. Okay? Yep, you're right it failed. Okay? Yeah. Okay? Wasn't just you, we saw it failed.

**Dave Jones:** Okay, everyone yep, everyone saw it fail. Thank you for the confirmation. So, I'm yeah, I think we've got a similar fault here. I'm just pushing the battery compartment in now.

**Dave Jones:** And it's and it's coming on, all right? I'll do it like 10 times and I'll see if it can come on 10 times and it is. But you saw it.

**Dave Jones:** All right? So, there's some silly bugger thing going on. So, maybe that's what they say yeah, cuz they said if they leave it for an hour and then try to turn it back on.

**Dave Jones:** So, what I'll do, okay, what I'll do is I'll put it I'll put it in. I'm going to leave that off for a bit and we'll come back to that later.

**Dave Jones:** Yep, he said it is more it's more likely to fail if on as in the turn on is more likely to fail if it's been off for hours or a day.

**Dave Jones:** You know, you start thinking cap, right? You start thinking cap residuals, stuff like that, but But don't know of any like these things only have like, you know, 10 mic tanalums in them or something.

**Dave Jones:** There's nothing in there that's going to hold charge for like hours, really. I don't think. Anyone got any good ideas? Cuz I'm leaning towards, yeah, there's something weird with the circuitry.

**Dave Jones:** There's something There's something weird happening. And Brian and I, unfortunately, have this weird history of the processors failing. Not not not in large numbers, but a a lot of the faults, in fact, I'd say most of the faults, probably all the faults.

**Dave Jones:** Mhm. No, I wouldn't say all, but probably the majority of faults in Brian and I meters have been simply that the processor has failed. It's just, you know, and it fails in weird ways.

**Dave Jones:** It doesn't, you know. So, um like it like it's a some sort of silicon rot thing or something like that. Yeah, I would rule out contacts. It's It's It's not contacts, right?

**Dave Jones:** Because you saw, you know, the the contacts work every time. Ah, there we go. Yep. All right. Right? And cuz the contacts work once it's on, there you go.

**Dave Jones:** It Once it's on, right? Look, I'm I'm pushing down on that. Wiggle, wiggle, wiggle. Yeah, right. There's nothing. I'm pulling up on it. Right? So, I'm Right? I'm pulling up on it cuz there there is a power contact which goes all the way It goes from here, right?

**Dave Jones:** It goes from the first position, and there's a power contact which got power and ground, right? Or something like that. It It's a pull up or something for the uh processor or for the transistor, right?

**Dave Jones:** Or for the the that enables the power that the enables the power on transistor to um turn on. And there's So, there's a trace which is two traces which go all the way around there like that.

**Dave Jones:** You You usually like a ground and a contact for the power on MOSFET switch. And it And it switches it on. And it's just like But the processor obviously latched it on, right?

**Dave Jones:** The processor latched it on now. So, the processor the MOSFET the power MOSFET has another output from the processor. So, as soon as it powers on, I think the processor overrides that and keeps it on.

**Dave Jones:** I don't know. And Brymen won't send me the schematic, so I don't know. I would I would I would I would have to I've I've done videos sort of tracing it before.

**Dave Jones:** Look, and once it's on it, it it's it's good, right? These have got to be the same fault. Right? There's there's nothing in there. These the Brymen switches have always been robust.

**Dave Jones:** Although, I know there is talk on the forum at the moment. There is a thread about Brymen switch contacts. Not necessarily on my model, but on the like the 789, I think, which is the same as this model.

**Dave Jones:** It's just Who agrees that I'm wasting my time tracing the power contacts, these switch contacts? Why are Fluke switches so much smoother than other meters? Yeah, they're just really nice.

**Dave Jones:** It's just the design. Although, although the others copy, you know, Fluke do the plastic indenty ball thing which moves they they do that, too. It's just I don't know.

**Dave Jones:** It's just more betterer. Paul Daniels says, "Definitely wasting time. I don't think it's the contacts." Tim thinks it's a waste of time. From what I've explained, yeah, waste of time.

**Dave Jones:** Switch looks fine. Verify there's no added amp draw when the uh display goes off from the battery back to point to a short. I I would put that at a 1% chance of being a thing.

**Dave Jones:** It's probably not something that I'd even test. I'd I'd be 99.9% confident it wouldn't draw extra power or something. Andrew reckons a waste of time, too intermittent to bother.

**Dave Jones:** Yeah, the uh Brymen's are good, but very stiff. Yes, yes, the Brymen's I give you a very stiff response on the switch. I I totally agree. Waste of time.

**Dave Jones:** Everyone says it's a waste of time. Switch looks fine. Baxter's doubling down on the battery holder. It's not the battery holder cuz I don't like cuz moving the switch does not impact the battery holder.

**Dave Jones:** It's not that. Hey, there we go, right? So, it's not powered on. Um pushing on that battery holder. It ain't the battery holder, right? It's not those contacts. It's not those contacts, right?

**Dave Jones:** I can even give it a whack, right? Look, wiggle wiggle wiggle, pushing down, pulling up, wiggle wiggle wiggle, right? Look, so it's it's not the switch. It's not the It is so not the switch.

**Dave Jones:** It is so not the battery contacts. It is electronic. Whether or not it's it's the processor or whether or not it's uh okay, cuz I would not rule that out, seriously.

**Dave Jones:** Cuz a lot of fires and Brymen fires that I've seen have happened because the processor has failed in some mysterious way. And um Brymen I think mentioned it might be some sort of silicon rot or something.

**Dave Jones:** Like we aren't talking many. We you know, we're talking like four or five units over just as many years, right? It's not many and I sell thousands of these things a year.

**Dave Jones:** Yeah, it's definitely not the switch or the battery contacts. Can really rule that out. You've had some interesting uh floating gate faults in the past with soft off circuits, especially the ground floats up.

**Dave Jones:** Yeah. Yeah, like something like that. But But once again, I don't think it's the switch causing it. All right? Yes, I can imagine that being the mechanism and the and a dodgy switch switch contact causing a floating ground or something that causes a weird intermittent cuz then you've got like a FET like it's usually a MOSFET input, right?

**Dave Jones:** So, it's high impedance. So, you can get stray, you know, fields and charges and stuff just ran intermittently turn it off and on or something. But whether it But where the actual fault is, now now it's not coming on at all.

**Dave Jones:** Yeah, but how that you know, how you'd get like a floating thing. It's definitely not floating due to the switch. But, yes, I can see I can see where you're coming from, Paul, definitely.

**Dave Jones:** I don't know what percentage, Heath. It's It's It's very small. Like now, I've got two units. Now, I've got two units which look like they've been a year apart in manufacture.

**Dave Jones:** Right, and you know, we're only talking, you know, sub 0.1% of units fail or something. It's really small. Wouldn't even be that. Yeah, I've I've done I'd have to go back and look at my previous video cuz I might be re- re-doing that.

**Dave Jones:** I've got a previous video on actually looking at the soft start circuit for one of these. I work on it, but I didn't actually document it. Let's Let's go back to the other one, shall we?

**Dave Jones:** Here we go. Here's Here's the will unit. Uh Uh Okay, I'm going to have to leave that one off for longer. Check the processor wake circuit. Yeah. Yeah, exactly.

**Dave Jones:** There is a thread on the forum about a switch issue on Brymen, and maybe it's not the switch. Maybe it's actually similar to this. So, I'll probably have to go re-read that, but it's not the 786.

**Dave Jones:** People have seen it on the 789, I believe. You will take What is firmware boot lock for $500? Yeah. Yeah, something like that. Mate, you know, like a processor reset.

**Dave Jones:** Some sort of Yeah, processor boot You know, it's it's it's not resetting properly. Like it's probably not even the power switch. You I bet you I I would be willing to bet that if I trace down there'd be nothing wrong with the switch.

**Dave Jones:** I wouldn't even bother checking it, right? That's 100% conclusive now. But, I'd be willing to bet. I I think that there's the power transistor. It's over here somewhere, right?

**Dave Jones:** I've I've I've got a board here. I believe cuz this is the one I was playing with last time, right? This one here is the switching MOSFET. This is the power here, and it switches This comes from the processor, right?

**Dave Jones:** Which latches on this MOSFET, which is not a a power MOSFET as much as it looks like there. It's It's not actually switching power. What this is doing is just switching on This is why it's latched, right?

**Dave Jones:** It's a latchy thing. It latches on or something, right? I'm willing to bet that when this is off, right? When the failure happens, the voltage actually gets through. I'd be willing to bet it's a processory boot thing.

**Dave Jones:** That's the multimeter chipset. And this is the This is the processor. I'm I'm willing to bet that the processor's not being reset properly. It's not booting properly. And I can't remember.

**Dave Jones:** I spent hours tracing this down last time. There was a reset I think I found a reset pin cuz I I I do actually know what processor it is cuz I've got the programmer for it.

**Dave Jones:** But I'm not allowed to tell you cuz I'm under in NDA, sorry. And And I can power this thing, too. I can actually power this thing through the programming header over here.

**Dave Jones:** I can actually power it. So, if I get the programmer out, I can actually program reprogram the chip. And actually I think I can like do a reset from here as well.

**Dave Jones:** Got 183 people watching. So, yes, I could Somebody say crystal not starting. Maybe it doesn't get out of deep sleep. Yeah, I'm I'm thinking this is like a re-processory resetty boot issue.

**Dave Jones:** Any clock that can be checked? Um No, I think it No, no, it uses the uses internal oscillator. You watch me burn the case. No, I didn't. I didn't burn the case.

**Dave Jones:** Oh, man. Professional. 4.5 volts, 100 milliamps. There you go. All right. So, I'm going to turn this sucker on. So, it's drawing zero at the moment. If I switch it on, there you go.

**Dave Jones:** It's drawing 1 milliamp. Unfortunately, that's all we can see. Oh, will will the 40-meter switch on? No! See? It did it. It did it. Yeah. See, leave it off for a while, right?

**Dave Jones:** It's dodgy as. Bingo, got you. Got you. So, that is confirmed. So, the Like it's it's not often that somebody who reports a fault who buys a unit reports a fault is accurate, but this this this guy was accurate.

**Dave Jones:** So, you got to leave it off for a while. Anyway, we want some current measurement. Here you go, 1.25 milliamps. So, off is Yeah, off is nothing, right? Half of a bee's dick.

**Dave Jones:** Right, so on in sleep mode is half a milliamp. So, that's the same for all the positions. So, why was it doing 1.3 before? We've We've already smacked it Q's tech service.

**Dave Jones:** We've already given it the percussive maintenance. Baxter is tripling down on the MCU. That would be the current I'd expect cuz normally it's like 3-4 milliamps, I think. Like if the processor's on and it's running and it's measuring everything.

**Dave Jones:** So, that's what I'd expect for like a things powered up and the processor is just not running cuz it's turned on power to everything else, right? The multimeter chipset and everything.

**Dave Jones:** It's just that the processor is not processing. The flux capacitor is not fluxing. Maybe if I drop the voltage What is Is the voltage going to make a difference?

**Dave Jones:** Let's drop the voltage down a bit. You'd expect it to be proportional and it is. Current is proportional with the voltage and 350 in every switch position. So, it doesn't doesn't make a difference.

**Dave Jones:** And like there's no variation in current. Once again, it's not the switch, right? There's no variation in current at all. When I first did this, it was showing 1.3 or something, right?

**Dave Jones:** The Farad I think it was 1.2. Robert says it was 1.25. Yeah, I I working trade working meter should draw about 4 milliamps, I think. All right. Well, clearly, I'm not going to be opening this up and going into the circuitry of this today.

**Dave Jones:** Something to do with that. Some sort of you know, it could be like a dodgy cap or something. I don't know. I'm I'm think cuz I I went to the effort to change the transistors last time and it wasn't that.

**Dave Jones:** It's the cutout. I'll I'll go 3.6. OH, WE GOT OUR 1.2 milliamps though. There you go. We got it. We got it. There's some weird weirdness happening here and it's 1.2 milliamps in all switch positions, right?

**Dave Jones:** So, we all weren't imagining things back when we first powered it on and watch, I'll power it off. I'll power it back on. And it's Oh, it's 1.2 Now, it's consistently 1.2.

**Dave Jones:** I'll go up to 4 volts. 1.2. Now, it's consistently 1.2. Wow. That's one weird ass fault, isn't it? It was consistent at 0.3 milliamps. Now, it's consistent at 1.2 and then this used to consistently turn on like, you know, we could at least get it to come on.

**Dave Jones:** Now, it doesn't come on at all. And now it gives us different currents. Oh, wow. It's enough for today. I'm out of here. Catch you next time.
