---
video_id: BSqKN2AaGqI
title: EEVblog 1702 : A Most Interesting REPAIR
url: https://www.youtube.com/watch?v=BSqKN2AaGqI
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 22, "3": 39, "4": 47, "5": 61, "6": 71, "7": 89, "8": 100, "9": 110, "10": 125, "11": 141, "12": 158, "13": 169, "14": 188, "15": 200, "16": 211, "17": 225, "18": 237, "19": 245, "20": 258, "21": 268, "22": 276, "23": 284, "24": 296, "25": 312, "26": 322, "27": 339, "28": 350, "29": 366, "30": 376, "31": 389, "32": 401, "33": 414, "34": 426, "35": 439, "36": 456, "37": 467, "38": 478, "39": 492, "40": 501, "41": 512, "42": 528, "43": 537, "44": 551, "45": 563, "46": 574, "47": 594, "48": 607, "49": 621, "50": 631, "51": 643, "52": 658, "53": 674, "54": 685, "55": 697, "56": 711, "57": 727, "58": 742, "59": 756, "60": 776, "61": 789, "62": 803, "63": 814, "64": 828, "65": 839, "66": 852, "67": 870, "68": 889, "69": 914, "70": 925, "71": 943, "72": 955, "73": 967, "74": 979, "75": 993, "76": 1001, "77": 1011, "78": 1022, "79": 1038, "80": 1052, "81": 1067, "82": 1079, "83": 1091, "84": 1108, "85": 1120, "86": 1135, "87": 1143, "88": 1154, "89": 1165, "90": 1171, "91": 1186, "92": 1200, "93": 1212, "94": 1225, "95": 1242, "96": 1254, "97": 1263, "98": 1277, "99": 1289, "100": 1309, "101": 1317, "102": 1330, "103": 1342, "104": 1353, "105": 1366, "106": 1376, "107": 1392, "108": 1403, "109": 1418, "110": 1430, "111": 1440, "112": 1454, "113": 1465, "114": 1479, "115": 1490, "116": 1502, "117": 1517, "118": 1528, "119": 1542, "120": 1548, "121": 1563, "122": 1584, "123": 1595, "124": 1610, "125": 1628, "126": 1640, "127": 1653, "128": 1664, "129": 1675, "130": 1689, "131": 1703}
---

**Dave Jones:** Hi, it's repair time. Uh, I've got a tennismatic. It's an Australian uh company who manufacture the tennis ball serving machines. Mrs. EV Blogger is a competitive uh tennis player.

**Dave Jones:** You don't want to mess with Mrs. E Vlog on the court, let me tell you. And she got a um secondhand uh tennismatic uh machine to do, you know, practice serving.

**Dave Jones:** you put on the other side of the court and you can shoot, you know, you can program the thing, dial it in and and it just shoots it at different angles and, you know, randomizes things so you can get your bin, top spin, bottom spin, and you can your sweep speed and your elevation and so you can just control it from the other end of the cord here.

**Dave Jones:** Um, and she said, um, it the machine works great, but uh, the remote controls not working. So, I thought I'd have a look at it. Um, 9V, uh, battery, uh, powered here.

**Dave Jones:** Um just your regular battery snap. The leads look okay, but uh yeah, let's um let's measure, shall we? First, we'll do some Ohmsky measurements and see if there's anything there.

**Dave Jones:** Let's have a look. Nothing. We do want to change polarity on that just in case that there's like the bias is not in the right direction to overcome a semiconductor junction.

**Dave Jones:** No. So, it could be open inside somewhere. But let's see. Okay, the next step would be to check if it actually draws any power. So, let's get it'll be down in the uh we'll go micro amps and we'll put it in series and Whoa.

**Dave Jones:** Hello. Hello. There's some residual. There's something there. Some residual. It's it's dialing back. That could be an input capacitor, but there is something. Okay, let's see if it draws any spikes.

**Dave Jones:** Nope. Um, you'd expect to see a current spike when you push the battery. I don't know how much what the transmit power it would be. It's, you know, using a few hundred megs or something.

**Dave Jones:** RF transmit. Um, no, nothing. Nothing. Um, what? Whoa. Hang on. Was that Was that a button? Yes. Hello. 80 micros. 90. So, that button worked. Was it I have to hold it down?

**Dave Jones:** Nope. So, these buttons don't work. That one works. What about that one? Nope. That's interesting. That button works. That button works. That button works. Are they in a row?

**Dave Jones:** Is it a row column thing? Wow. It's a row It's a row column thing. Well, it's just a row thing. Wow, that's interesting. Those buttons draw something. Wow, that's fascinating.

**Dave Jones:** Um I I didn't expect that. All right. Um let's open it up. So, I can't imagine there being any other reason for that. Um, I haven't RTFMED. I don't even know if there is a manual for this thing.

**Dave Jones:** Um, I bet why just those buttons, that one row there, and nothing else works. Um, that's interesting. Pretty old school. This is uh not a new design. Oh, all the ATM fanboys go wild.

**Dave Jones:** Look at this. Got an at tiny 2313. No worries. All right. Chong X caps here. Nothing fancy at all. Okay. So, was that actually was that red lead coming on?

**Dave Jones:** It's no real strain relief there. That's a bit how you're doing. Let's push the knowing button. Ah, yeah. There we go. So, that is definitely that should be more than the uh what is the 100 micro amps or whatever.

**Dave Jones:** But that is flushy flashy in and yeah, sure enough, the other buttons don't. Hang on. There's a pin miss in here, but there's a trace going to it. Has someone fiddled with the ribbon cable.

**Dave Jones:** I wonder. I'm going to take that off. They've put the ribbon cable on backwards. Yeah, look, there's no trace. Well, there's no trace connected to the top. I'd have to take the board off.

**Dave Jones:** I don't know. There's a trace to it and it's not connected. So, have they like has somebody taken off and then put it back on in the wrong location?

**Dave Jones:** That would be an interesting fault, would it not? Fault in quote marks. Got an antenna up here. We've just got our little um transmit module out over here. There's nothing fancy at all.

**Dave Jones:** Literally got RF on the transistor. Jeez, is that an RF transistor? I'm not sure. Is that just a coincidence? It's got RF on it. Yeah. 433 megs. Yep. Yep.

**Dave Jones:** That's what I would have guessed. So, it seems to work. Like, so the processor is doing its thing. But yeah, let me get this board out. There we go.

**Dave Jones:** I can just lever this board out. So, let me see if there's a trace. If there's no trace going to that one, then I reckon that's what's happened. I could measure that.

**Dave Jones:** If you couldn't get If you couldn't get ready access to the bottom, you could just buzz that pin out just to see if it went anywhere. Oh, is that No, I was going to say, is that a is that a pin one marker?

**Dave Jones:** No, it's not. Yes. Yes, there is. Okay, there's that going over to there. All right. So much for that theory. Solder joints look okay. That's manually been soldered. Whereas the other looks like it's a a wave soldered jobby.

**Dave Jones:** Nothing wrong with that. I'll just heat it up for kicks. Um there's actually nothing nothing doing there at all. Just looking at that. Oh, hang hang on. Is that a Oh, no.

**Dave Jones:** No. That's just a break in the plastic. It doesn't seem to be an issue there with the actual trace. Almost looks like there's an offset issue there. Okay, so we've ruled out the microcontroller.

**Dave Jones:** That's working fine. If we manually shorted out like a couple of these pins, we could probably get like different combinations working. So, there's some reason why only a row is working.

**Dave Jones:** I mean, I could just try out my wild theory, can't I? See if it No, no, no, no. The top row is working now. So, nothing obvious on there like, you know, there's no spillage or anything.

**Dave Jones:** There's no breakage in those traces at the bend points. You want to check out the bend points. No, those bend points look good. Don't be fooled by the shadows.

**Dave Jones:** We can physically see the contacts under there. Yeah, they shifted off to the side a bit. I'm sure that's not the problem, but you know what I'm going to do is probe this thing and see if I can get some uh continuity happening.

**Dave Jones:** You see that there's physically two different strips there. I could be separating those into rows and columns. That would make sense. Three columns, five for the rows. There you go.

**Dave Jones:** Yep, that makes perfect. That's a perfect count. So, let's probe across that one and that one. Like, let's just call that pin one of the row and column. Do this on the side of the bench here.

**Dave Jones:** Sorry, you can't see it. No, I didn't get anything between that pin and that pin with any of the buttons. That looks okay. That looks pretty solid. Don't want to go peeling the stick.

**Dave Jones:** It's not a sticker. It's a Yeah, it's a big chunky flat thing. I don't want to go peeling that off if I don't have to. Let's go back to the PCB here.

**Dave Jones:** I'll put it in current mode and we'll um short between because pro tip, you can use your multimeter as like a shorting um thing. Just put it in amps mode and you basically got, you know, a couple of ohms depending on your your fuse resistance plus your current shunt resistor in there.

**Dave Jones:** Anyway, let's let's see if she lights up here. Yeah. So, that's a column and that's a row. Yep. Yes. Right. I can get any of these to light up.

**Dave Jones:** Well, yeah, that one's not connected, right? Second row. Right. So, if I do two columns, it's not going to do it. Right. So, there. Yep. So, yeah, she's all good.

**Dave Jones:** Right. So, that micro is doing exactly what you expect it to. So, the problem is the bloody membrane. That's a bugger that the actual membrane's gone. Was hoping for an easier fix than that.

**Dave Jones:** I was hoping for like just a, you know, a broken battery snap wire or something like that, but I mean, this looks pretty solid and robust. It doesn't look like it's had any water damage or anything really.

**Dave Jones:** You know, you'd expect maybe one or two buttons like, and it doesn't look like it's had much use. Um, the previous owner apparently had um had only used it like four times or something.

**Dave Jones:** So, I don't even know if they used the remote control at all. So, no signs of water ingress. It looks like a completely sealed thing. So, uh, yeah, if I peel it off, then it's just I'm I'm not sure not sure if we're actually going to see anything.

**Dave Jones:** There's our contact. You can see it. We've got so many that aren't working. It's not like there's one break in there. So, that's the annoying thing about this fault.

**Dave Jones:** These things are usually very robust. Um, I know it's it's not new. What's I mean, what's the uh date code? 14 34. That could be uh 34th week 2014.

**Dave Jones:** So, it could be 10 years old. The uh actual design's probably way older than that, but 10 years old is not long enough to like degrade stuff. And it looks like it's had hardly any use at all.

**Dave Jones:** Is it the actual connector? It looks like they're crimped wrapped around there. That's That seems pretty solid, doesn't it? Doesn't explain why so many of them. Yeah, it's definitely not.

**Dave Jones:** It's offset a bit, but damn. I mean, and that's why if you wiggle that just just the whole contacts are the contacts are really solidly crimped onto there. So, I don't see how that's a problem either.

**Dave Jones:** Oh, hang on. Those three aren't working anymore now. So, that's interesting. Is it not? That don't The only row that was working is not. No, now it's working. Ah, nope.

**Dave Jones:** So, if I like put that on and I wiggle wiggle wiggle. Yeah. All over the place. Still not doing the business. I can't say I've ever seen this scenario before.

**Dave Jones:** Like, I've seen old keypads wear out and you get a worn key or whatever through use or they've had water ingress or something and it's rotted stuff away and and things like that.

**Dave Jones:** And then you'll get breaks in the ribbon cables if there's any um you know movement in them at all. And maybe you could get like one bad intermittent contact in there.

**Dave Jones:** I've seen those. But nothing that takes out the entire thing. It's just taking out the whole keypad. Damn it. And it's a simple row column thing. And if I release my thumb, it still works again.

**Dave Jones:** No. And now it's gone. If I put my finger back on there. Ah, looks like it is that connector. But why only that row? Nothing else. That that one row and the three columns work.

**Dave Jones:** But all the other rows have failed. So what? Let's let's say this is the good one. Is that that one's failed, that one's failed, that one's failed, and that one's failed.

**Dave Jones:** How can I access the contacts on the surface there? They just happen to be on the inside, don't they? Bloody Murphy. I can bend that back and we can get in there and have a look at this turd.

**Dave Jones:** And yeah. Yeah, they're piercing through. Are they soldered onto there? That seems most likely where the where the problem is because the keypad like these keypads are basically sealed things.

**Dave Jones:** They're like sandwiched in there and they're and they're sealed reasonably well. I mean, you can get water ingress to them, but um generally, yeah, I would expect the issue to be the crimp contacts down in there.

**Dave Jones:** So, I can take the pins out. Yeah, there we go. There we go. Got it. Let's have a closer look at this, shall we? There you go. That actually looks So, yeah, it's piercing the plastic there.

**Dave Jones:** My issue is is that there's just so many of them. Is that actually looks like some solder on there, doesn't it? Let's do some buzzy dudah. Okay, we're getting that.

**Dave Jones:** And once again, we got Yeah, we got exposed material here. Yeah, we're getting that's definitely connected. Is that coming off? Oh, silver's coming off. Yes. Look at Oh, I've almost come and guts are completely there.

**Dave Jones:** Is that like a silver trace? I've almost I've practically worn through that thing. Whoops. Is that our problem? Have we just got Have these just like rotted away or something?

**Dave Jones:** But but you saw it. We were getting continuity right up to there where it goes into the plastic and then after that everything looks fine, right? I mean, there's there's no issues at all.

**Dave Jones:** Look at that. Right. But once again, there's so many break. Like, I wouldn't expect so many breaks. Have we just got like a really dodgy quality keypad here, man?

**Dave Jones:** I did not expect this much trouble from a keypad. And now we've got almost all the keys are out because it looks like we've just got a poor quality keypad.

**Dave Jones:** Wow. Well, I'll see if I can get this one out of here as well. So, I'll get back to you. There we go. Okay. Yeah, I'm getting nothing. Yeah, nothing.

**Dave Jones:** Nothing. And I can I can physically scrape away. Can I? Yeah, I can physically scrape away some of that. Yeah, if I can physically scrape it away, it means that it's exposed and I'm making contacts.

**Dave Jones:** So, yeah, these are just all all dodgy. So, let's just go into ohms. No. Yeah. See, 3 400 ohms. Wow. Yeah, there's just these are just really bad contacts to the um I I don't blame the contacts.

**Dave Jones:** I blame the uh membrane material. It's just it's just poor. It's all It's completely kamaga. And annoyingly, I can't easily push these back on to here cuz they're not a complete box type.

**Dave Jones:** They're like an open top type. So, it really requires the pla the surrounding plastic in there to be able to push these back on, which is uh kind of annoying, but So, what I think's worthwhile doing here is trying to get some conductive ink onto some silver conductive ink and just like spread it all across here to see if I can like make better contact.

**Dave Jones:** Now, the only stuff I've got is this um circuit scribe came in the mailbag donkeyy's years ago, I think. So, I'm not sure like shelf life, but um beta.

**Dave Jones:** The whole point is this is you can actually repair uh probably should get some gloves on. You can actually repair stuff like this. Now, not sure if that's the original consistency or not.

**Dave Jones:** I don't think so. I kind of remember it being a bit better than that. Anyway, I could actually try and put some on, I guess. But I I think this might be very out of date.

**Dave Jones:** But anyway, so whether or not it like hardens or does whatever, I don't know. But yeah, no, I think I need some good stuff. But I don't don't have any to hand.

**Dave Jones:** And I just checked Jar, which is my nearest store. They didn't have any. RS components didn't have any. At least a couple of days away. It's not pretty, is it?

**Dave Jones:** The problem is trying to solder membranes like these, it's just it's just going to melt. So, um yeah, don't do that. That's actually that's that's that's not bad. So, that's going to set.

**Dave Jones:** Could work. But yeah, it's it's so I don't know what the shelf life of this thing is. Couldn't find a data sheet. Think you get what you get and you don't get upset.

**Dave Jones:** Now you can see where the problem's likely to be here. You can see the like it looks like discoloration, but it seems to be that the silver has just worn away on that flex.

**Dave Jones:** Even though this is not continually flexing, right? If it was continually flexing, you could um think that okay, it's going to like wear off and then little flakes had come off over time and stuff like that.

**Dave Jones:** it like there's nothing like it's not being used in something that's flexing all the time, but it looks like it's sort of almost worn off. So, if we flip that over so we can probe it, okay, if we go like you can see that the plastic ends here.

**Dave Jones:** Okay, so if we probe here and here, right, it's conductive. But if we probe here and here, it's not conductive, right? Even though on this side, if you look at the microscope on this side, you think that's not broken.

**Dave Jones:** There's no break there at all. Right. And but we can see it from the other side. So, right, that's why look the it's just it's completely worn off. So, there's nothing wrong with the contacts in here.

**Dave Jones:** Right. actually to the crimp pins. It's We flip it back over and it's it's that the silver has worn off cuz this is the bottom side right here's the it's the bottom side next to the plastic.

**Dave Jones:** This is all plastic here, right? But we can clearly see that it's kind of like the silver's just worn away or whatever. I I don't know how, but it's like it's like that for every single one of them.

**Dave Jones:** Look at that. That's crazy. Okay, so I use my dodgy silver paint. And here it is. Okay, it's it's dried now. And sure enough, we get continuity. And if I Right, 15 ohms, right, that's good enough for Australia.

**Dave Jones:** That's certainly going to uh the micro is going to recognize that. The other one looks like Yeah, like like 4 ohms, right? So yeah, so that that silver paint, as dodgy as it was, uh worked.

**Dave Jones:** But um since then I've have ordered it and I've got my um little silver conductive ink. I just got it from the local hobby store. Um in fact the same hobby store that I originally got the Indiana Jones train set from.

**Dave Jones:** Hobbies in the Hills. I got it from them. They they're just on eBay. They're not in the hills anymore. I think they're bugged off the coast or something. But anyway, um silver conductive paint.

**Dave Jones:** Haven't looked at the data sheet for it. And it comes with um this very nice very nice needle point. Look at that. That's tiny. Yeah, I didn't want to use that dodgy stuff again.

**Dave Jones:** Even though it looks like it kind of worked. It kind of worked. I don't know. Has it has it cracked in there a little bit? Yeah, don't use sort of out of date uh conductive paint like that.

**Dave Jones:** It still seems to work, but yeah, I wouldn't I wouldn't trust it. Okay, I'm going to need a clamp to hold this in place cuz this thing just boing.

**Dave Jones:** Here we go. It's because it's a syringe, it's not going to be the easiest thing to apply. And I've got this hanging up in the air. So it's a little bit I got too much on the end of that.

**Dave Jones:** But because that one is No, it's in fact it's going to short to the one next to it, isn't it? So I shouldn't have done that. Maybe I should get rid of some of that.

**Dave Jones:** That was terrible. Muriel started out with way too much there. So can we scrape away? Yeah, it doesn't really seem possible to apply to use the syringe and this at the same time.

**Dave Jones:** This is terrible. Oh, yeah. It spreads out way too much. Yeah. Yeah. I've got to have very little of that. I'll steal some from over here and place it over here.

**Dave Jones:** Yeah, that's the problem with this syringe stuff. I could have like a dispenser, like a paste, automated paste dispenser. Don't have one to hand. Anyway, we we're just trying to bridge like I'm putting it over the pins, which I don't have to do.

**Dave Jones:** Only trying to bridge over that part that's not conductive. Should be doing an end on, shouldn't I? Yeah, this is terrible. Won't give up my day job. Yeah, I really didn't need much at all.

**Dave Jones:** It's not easy when it's hanging up in the air and you can't put your wrist flat on the bench. And usually you just leave these to uh dissolve away.

**Dave Jones:** Um they like evaporate away the uh whatever like alcoholy type stuff is in there or whatever. Um and you can usually apply some heat to them as well. My box of cotton buds has vanished.

**Dave Jones:** Don't know where it is. I'm not just going to go to the shop to get it. So I'll try an alcohol wipe. The glare is really annoying here, but not going to bother to fix it.

**Dave Jones:** And no, that's not shorted. Nope. It's a bit how you're doing. Oh, I smeared it out. Oh, I smeared it out by touching the Oh, no. I've come I Look, I accidentally smeared it out.

**Dave Jones:** See if I can rub that off with the wipe. Here we go. Yes, I can. Okay. It's almost as if I'm better off like wiping it all off and then starting again.

**Dave Jones:** Wipe it all off. Start again. doll. All right. Should have been more aware of that, but oh well. Live and learn. All right. Let's try that again, shall we?

**Dave Jones:** There we go. Look at that. That's a fat ass trace, isn't it? It's hard to know how much to pick up from my pile over there. Cuz it just oozed out when I pressed my syringe.

**Dave Jones:** Another big ass fat trace. I don't care how fat it is. I just want it to work. Kind of like the fat looking ones better. Don't know. It's more conductor.

**Dave Jones:** So, yeah, you might be able to do this a lot better with a very fine automated dispenser, but it' have to be a real fine jobby. Big fat ones are hilarious, but oh well.

**Dave Jones:** Not going to complain about them not working. Like, they look bigger than they are. They look big because of the lighting on them, but uh they're actually not that huge in the scheme of things.

**Dave Jones:** So, what you do now is uh you either leave it there for like 12 hours, 24 hours or something like that. It depends on the type it is. Um yeah, they actually use like an alcohol in there and you can heat it up like if you get it to like, you know, 60° or something, you might be able to do it in an hour or something like that.

**Dave Jones:** So, you shouldn't try and measure it now while it's wet. You wait until the alcohol or whatever thinner in it um that actually evaporates um and then you're left with the conductive um silver paint.

**Dave Jones:** Yeah. I might put that on some mild heat to accelerate it. Um, but anyway, that that wasn't pretty, but I reckon that is going to work a treat. Actually, the interesting thing is the the two I did with my other silver paint.

**Dave Jones:** That actually looks better, doesn't it? Looks better than this. Uh oh, actually, this is the one that I've done now. Is it still Is it still wet or is it Yeah.

**Dave Jones:** Yeah. Yeah, she's still wet. Okay, no worries. So, I've just got my hot air gun set to 60° and I'm just going to uh blow it over that for the next hour or something.

**Dave Jones:** And hopefully that should be reasonably dry. Get back to you. Let's see if it's solidified. It's a little bit. Yeah. Okay. Maybe. Maybe cuz that's too thick. This seems okay.

**Dave Jones:** I I need to give it a little bit longer, but hey, um let's measure the ohms. Measure that. 3 ohms. No worries. And boom. Yeah, that's great. That's great.

**Dave Jones:** I think we're in business. Unless Unless it's degraded somewhere else further up the membrane as well, but I don't want to jinx it. You can see that one. Yeah, that one hasn't totally evaporated yet.

**Dave Jones:** It was too thick. Is that the same on that one? Oh, no. 25 ohms. Yeah. Okay. I I just need to leave that one for a bit longer. There's just u yeah it just hasn't evaporated all the binding agent.

**Dave Jones:** Once that evaporates then you're left with the little solder silver solder balls or whatever they are. Um so yeah I I'll give that a bit longer but it's looking promising.

**Dave Jones:** Okay, I've given it some more time and [Music] hello 12 ohms. No worries. I think that'll get better. It's still a bit spongy. 6 ohms. Yeah, no worries. You see how it's lower the thinner it is.

**Dave Jones:** The lower it is, that's because it's evaporated quicker. And so if we give it enough time, these ones will also get down to like one or two ohms each.

**Dave Jones:** Not 100% dry yet, but I'm going to put this back together. And I think we'll find that it should work as long as there's no other degradation elsewhere in the keypad.

**Dave Jones:** Like there could even be some up under here. I just don't know. All I know is that I measured it down here and we could visually see it as well.

**Dave Jones:** So anyway, um so hopefully we fixed that. So hang on. Oh, I haven't put the little uh there's little clips in there that sort of like hold it in place, but anyway, we'll put this back on here for now and we'll see if we can get it working.

**Dave Jones:** Boom. That's the top row. Top row. Yes. Yes. And then this row here. Yes. Yes. Yes, yes, yes, yes, yes, yes, and yes. There you go. Winner winner chicken dinner.

**Dave Jones:** There you have it. That should work a treat, assuming that the receiver on the other end uh works. No worries. So, there you go. That was an interesting repair.

**Dave Jones:** I did not expect that. And that's something that I'm struggling to remember where I've if I've actually seen that sort of degradation in the silver. It's like they have done like a silver roll paint on the um thing.

**Dave Jones:** Like it's not like a copper, you know, traces or anything like that. It looks like they've done a silver paint on there. And for some reason without it flexing, without it actually being part of some flexible thing, it's come a guta and it's worn off.

**Dave Jones:** And not just in one spot, it had worn off on like four of the rows like that. And this one here was borderline like intermittent as well. The columns seem to have been okay, but I redid the columns anyway.

**Dave Jones:** But yeah, all of the rows were just gone. The silver and it looked perfect from one side. It looked fine. like there's nothing wrong with it. Yet you flip it over and you can see the degradation on the other side against the plastic.

**Dave Jones:** So maybe some weird chemical things going on there. I don't know. If you seen this before and you know exactly if you're a chemist should ask Mrs. EV blog.

**Dave Jones:** She's a chemist. Anyway, um yeah, some sort of weird thing happening there. It looked fine on one side and yet the other side you can see it was clearly degraded on those lines.

**Dave Jones:** So silver paint for the win. you probably should have some of this uh lying around. And yeah, um there were some suggestions that maybe cuz I did a live um show showed this uh that maybe I could um rejuvenate this sort of stuff cuz the silver's still in there.

**Dave Jones:** Maybe um with with some acetone or something like that perhaps. I don't know. But this still seemed to actually work. So kind of sort of. But anyway, um yeah, groovy stuff and an interesting fault.

**Dave Jones:** Hope you like that. If you did, please give it a big thumbs up. As always, discuss down below. And happy wife, happy life. Catch you next time. [Music]
