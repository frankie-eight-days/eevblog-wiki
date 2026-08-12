---
video_id: BSqKN2AaGqI
title: EEVblog 1702 : A Most Interesting REPAIR
url: https://www.youtube.com/watch?v=BSqKN2AaGqI
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 28, "3": 41, "4": 56, "5": 70, "6": 86, "7": 104, "8": 119, "9": 138, "10": 158, "11": 171, "12": 192, "13": 208, "14": 222, "15": 237, "16": 252, "17": 265, "18": 278, "19": 289, "20": 304, "21": 322, "22": 339, "23": 355, "24": 375, "25": 386, "26": 403, "27": 416, "28": 436, "29": 451, "30": 464, "31": 482, "32": 495, "33": 508, "34": 520, "35": 535, "36": 551, "37": 565, "38": 583, "39": 602, "40": 621, "41": 635, "42": 651, "43": 670, "44": 685, "45": 700, "46": 718, "47": 734, "48": 750, "49": 772, "50": 789, "51": 805, "52": 823, "53": 839, "54": 854, "55": 877, "56": 894, "57": 912, "58": 928, "59": 948, "60": 967, "61": 981, "62": 997, "63": 1011, "64": 1024, "65": 1036, "66": 1052, "67": 1067, "68": 1080, "69": 1097, "70": 1112, "71": 1126, "72": 1138, "73": 1149, "74": 1162, "75": 1176, "76": 1193, "77": 1207, "78": 1222, "79": 1238, "80": 1254, "81": 1270, "82": 1280, "83": 1303, "84": 1320, "85": 1337, "86": 1351, "87": 1366, "88": 1378, "89": 1388, "90": 1398, "91": 1414, "92": 1427, "93": 1440, "94": 1458, "95": 1477, "96": 1488, "97": 1502, "98": 1520, "99": 1537, "100": 1550, "101": 1563, "102": 1587, "103": 1603, "104": 1618, "105": 1633, "106": 1647, "107": 1662, "108": 1675, "109": 1689, "110": 1703}
---

**Dave Jones:** Hi, it's repair time. Uh, I've got a tennismatic. It's an Australian uh company who manufacture the tennis ball serving machines. Mrs. EV Blogger is a competitive uh tennis player. You don't want to mess with Mrs. E Vlog on the court, let me tell you.

**Dave Jones:** And she got a um secondhand uh tennismatic uh machine to do, you know, practice serving. you put on the other side of the court and you can shoot, you know, you can program the thing, dial it in and and it just shoots it at

**Dave Jones:** different angles and, you know, randomizes things so you can get your bin, top spin, bottom spin, and you can your sweep speed and your elevation and so you can just control it from the other end of the cord here. Um, and she

**Dave Jones:** said, um, it the machine works great, but uh, the remote controls not working. So, I thought I'd have a look at it. Um, 9V, uh, battery, uh, powered here. Um just your regular battery snap. The leads look okay, but uh yeah, let's um

**Dave Jones:** let's measure, shall we? First, we'll do some Ohmsky measurements and see if there's anything there. Let's have a look. Nothing. We do want to change polarity on that just in case that there's like the bias is not in the

**Dave Jones:** right direction to overcome a semiconductor junction. No. So, it could be open inside somewhere. But let's see. Okay, the next step would be to check if it actually draws any power. So, let's get it'll be down in the uh we'll go

**Dave Jones:** micro amps and we'll put it in series and Whoa. Hello. Hello. There's some residual. There's something there. Some residual. It's it's dialing back. That could be an input capacitor, but there is something. Okay, let's see if it draws any spikes. Nope. Um, you'd expect

**Dave Jones:** to see a current spike when you push the battery. I don't know how much what the transmit power it would be. It's, you know, using a few hundred megs or something. RF transmit. Um, no, nothing. Nothing. Um, what? Whoa. Hang on. Was

**Dave Jones:** that Was that a button? Yes. Hello. 80 micros. 90. So, that button worked. Was it I have to hold it down? Nope. So, these buttons don't work. That one works. What about that one? Nope. That's interesting. That button works.

**Dave Jones:** That button works. That button works. Are they in a row? Is it a row column thing? Wow. It's a row It's a row column thing. Well, it's just a row thing. Wow, that's interesting. Those buttons draw something. Wow, that's fascinating.

**Dave Jones:** Um I I didn't expect that. All right. Um let's open it up. So, I can't imagine there being any other reason for that. Um, I haven't RTFMED. I don't even know if there is a manual for this thing. Um,

**Dave Jones:** I bet why just those buttons, that one row there, and nothing else works. Um, that's interesting. Pretty old school. This is uh not a new design. Oh, all the ATM fanboys go wild. Look at this. Got an at tiny 2313.

**Dave Jones:** No worries. All right. Chong X caps here. Nothing fancy at all. Okay. So, was that actually was that red lead coming on? It's no real strain relief there. That's a bit how you're doing. Let's push the knowing button. Ah, yeah.

**Dave Jones:** There we go. So, that is definitely that should be more than the uh what is the 100 micro amps or whatever. But that is flushy flashy in and yeah, sure enough, the other buttons don't. Hang on. There's a pin miss in here, but there's

**Dave Jones:** a trace going to it. Has someone fiddled with the ribbon cable. I wonder. I'm going to take that off. They've put the ribbon cable on backwards. Yeah, look, there's no trace. Well, there's no trace connected to the top. I'd have to

**Dave Jones:** take the board off. I don't know. There's a trace to it and it's not connected. So, have they like has somebody taken off and then put it back on in the wrong location? That would be an interesting fault, would it not?

**Dave Jones:** Fault in quote marks. Got an antenna up here. We've just got our little um transmit module out over here. There's nothing fancy at all. Literally got RF on the transistor. Jeez, is that an RF transistor? I'm not sure. Is that just a

**Dave Jones:** coincidence? It's got RF on it. Yeah. 433 megs. Yep. Yep. That's what I would have guessed. So, it seems to work. Like, so the processor is doing its thing. But yeah, let me get this board out. There we go. I can just lever this

**Dave Jones:** board out. So, let me see if there's a trace. If there's no trace going to that one, then I reckon that's what's happened. I could measure that. If you couldn't get If you couldn't get ready access to the bottom, you could just

**Dave Jones:** buzz that pin out just to see if it went anywhere. Oh, is that No, I was going to say, is that a is that a pin one marker? No, it's not. Yes. Yes, there is. Okay, there's that going over to there. All right. So much

**Dave Jones:** for that theory. Solder joints look okay. That's manually been soldered. Whereas the other looks like it's a a wave soldered jobby. Nothing wrong with that. I'll just heat it up for kicks. Um there's actually nothing nothing doing there at all. Just looking at that. Oh,

**Dave Jones:** hang hang on. Is that a Oh, no. No. That's just a break in the plastic. It doesn't seem to be an issue there with the actual trace. Almost looks like there's an offset issue there. Okay, so we've ruled out the microcontroller.

**Dave Jones:** That's working fine. If we manually shorted out like a couple of these pins, we could probably get like different combinations working. So, there's some reason why only a row is working. I mean, I could just try out my wild theory, can't I? See if

**Dave Jones:** it No, no, no, no. The top row is working now. So, nothing obvious on there like, you know, there's no spillage or anything. There's no breakage in those traces at the bend points. You want to check out the bend points. No, those bend points

**Dave Jones:** look good. Don't be fooled by the shadows. We can physically see the contacts under there. Yeah, they shifted off to the side a bit. I'm sure that's not the problem, but you know what I'm going to do is probe this thing and see

**Dave Jones:** if I can get some uh continuity happening. You see that there's physically two different strips there. I could be separating those into rows and columns. That would make sense. Three columns, five for the rows. There you go. Yep, that makes perfect. That's a

**Dave Jones:** perfect count. So, let's probe across that one and that one. Like, let's just call that pin one of the row and column. Do this on the side of the bench here. Sorry, you can't see it. No, I didn't

**Dave Jones:** get anything between that pin and that pin with any of the buttons. That looks okay. That looks pretty solid. Don't want to go peeling the stick. It's not a sticker. It's a Yeah, it's a big chunky flat thing. I don't want to go peeling

**Dave Jones:** that off if I don't have to. Let's go back to the PCB here. I'll put it in current mode and we'll um short between because pro tip, you can use your multimeter as like a shorting um thing. Just put it in amps mode and you

**Dave Jones:** basically got, you know, a couple of ohms depending on your your fuse resistance plus your current shunt resistor in there. Anyway, let's let's see if she lights up here. Yeah. So, that's a column and that's a row. Yep.

**Dave Jones:** Yes. Right. I can get any of these to light up. Well, yeah, that one's not connected, right? Second row. Right. So, if I do two columns, it's not going to do it. Right. So, there. Yep. So, yeah, she's all good. Right. So, that micro is

**Dave Jones:** doing exactly what you expect it to. So, the problem is the bloody membrane. That's a bugger that the actual membrane's gone. Was hoping for an easier fix than that. I was hoping for like just a, you know, a broken battery

**Dave Jones:** snap wire or something like that, but I mean, this looks pretty solid and robust. It doesn't look like it's had any water damage or anything really. You know, you'd expect maybe one or two buttons like, and it doesn't look like

**Dave Jones:** it's had much use. Um, the previous owner apparently had um had only used it like four times or something. So, I don't even know if they used the remote control at all. So, no signs of water ingress. It looks like a completely

**Dave Jones:** sealed thing. So, uh, yeah, if I peel it off, then it's just I'm I'm not sure not sure if we're actually going to see anything. There's our contact. You can see it. We've got so many that aren't working. It's not like there's one break

**Dave Jones:** in there. So, that's the annoying thing about this fault. These things are usually very robust. Um, I know it's it's not new. What's I mean, what's the uh date code? 14 34. That could be uh 34th week 2014.

**Dave Jones:** So, it could be 10 years old. The uh actual design's probably way older than that, but 10 years old is not long enough to like degrade stuff. And it looks like it's had hardly any use at all. Is it the actual connector? It

**Dave Jones:** looks like they're crimped wrapped around there. That's That seems pretty solid, doesn't it? Doesn't explain why so many of them. Yeah, it's definitely not. It's offset a bit, but damn. I mean, and that's why if you wiggle that

**Dave Jones:** just just the whole contacts are the contacts are really solidly crimped onto there. So, I don't see how that's a problem either. Oh, hang on. Those three aren't working anymore now. So, that's interesting. Is it not? That don't The

**Dave Jones:** only row that was working is not. No, now it's working. Ah, nope. So, if I like put that on and I wiggle wiggle wiggle. Yeah. All over the place. Still not doing the business. I can't say I've ever seen this scenario

**Dave Jones:** before. Like, I've seen old keypads wear out and you get a worn key or whatever through use or they've had water ingress or something and it's rotted stuff away and and things like that. And then you'll get breaks in the ribbon cables

**Dave Jones:** if there's any um you know movement in them at all. And maybe you could get like one bad intermittent contact in there. I've seen those. But nothing that takes out the entire thing. It's just taking out the whole keypad. Damn it.

**Dave Jones:** And it's a simple row column thing. And if I release my thumb, it still works again. No. And now it's gone. If I put my finger back on there. Ah, looks like it is that connector. But why only that row? Nothing else. That

**Dave Jones:** that one row and the three columns work. But all the other rows have failed. So what? Let's let's say this is the good one. Is that that one's failed, that one's failed, that one's failed, and that one's failed.

**Dave Jones:** How can I access the contacts on the surface there? They just happen to be on the inside, don't they? Bloody Murphy. I can bend that back and we can get in there and have a look at this turd. And yeah.

**Dave Jones:** Yeah, they're piercing through. Are they soldered onto there? That seems most likely where the where the problem is because the keypad like these keypads are basically sealed things. They're like sandwiched in there and they're and they're sealed reasonably well. I mean,

**Dave Jones:** you can get water ingress to them, but um generally, yeah, I would expect the issue to be the crimp contacts down in there. So, I can take the pins out. Yeah, there we go. There we go. Got it.

**Dave Jones:** Let's have a closer look at this, shall we? There you go. That actually looks So, yeah, it's piercing the plastic there. My issue is is that there's just so many of them. Is that actually looks like some solder on there, doesn't it?

**Dave Jones:** Let's do some buzzy dudah. Okay, we're getting that. And once again, we got Yeah, we got exposed material here. Yeah, we're getting that's definitely connected. Is that coming off? Oh, silver's coming off.

**Dave Jones:** Yes. Look at Oh, I've almost come and guts are completely there. Is that like a silver trace? I've almost I've practically worn through that thing. Whoops. Is that our problem? Have we just got Have these just like rotted

**Dave Jones:** away or something? But but you saw it. We were getting continuity right up to there where it goes into the plastic and then after that everything looks fine, right? I mean, there's there's no issues at all. Look at that. Right. But once

**Dave Jones:** again, there's so many break. Like, I wouldn't expect so many breaks. Have we just got like a really dodgy quality keypad here, man? I did not expect this much trouble from a keypad. And now we've got almost all the keys are out

**Dave Jones:** because it looks like we've just got a poor quality keypad. Wow. Well, I'll see if I can get this one out of here as well. So, I'll get back to you. There we go. Okay. Yeah, I'm getting nothing. Yeah, nothing.

**Dave Jones:** Nothing. And I can I can physically scrape away. Can I? Yeah, I can physically scrape away some of that. Yeah, if I can physically scrape it away, it means that it's exposed and I'm making contacts. So, yeah, these are

**Dave Jones:** just all all dodgy. So, let's just go into ohms. No. Yeah. See, 3 400 ohms. Wow. Yeah, there's just these are just really bad contacts to the um I I don't blame the contacts. I blame the uh membrane material. It's

**Dave Jones:** just it's just poor. It's all It's completely kamaga. And annoyingly, I can't easily push these back on to here cuz they're not a complete box type. They're like an open top type. So, it really requires the pla the surrounding

**Dave Jones:** plastic in there to be able to push these back on, which is uh kind of annoying, but So, what I think's worthwhile doing here is trying to get some conductive ink onto some silver conductive ink and just like spread it

**Dave Jones:** all across here to see if I can like make better contact. Now, the only stuff I've got is this um circuit scribe came in the mailbag donkeyy's years ago, I think. So, I'm not sure like shelf life, but um beta. The whole point is this is

**Dave Jones:** you can actually repair uh probably should get some gloves on. You can actually repair stuff like this. Now, not sure if that's the original consistency or not. I don't think so. I kind of remember it being a bit better than that. Anyway, I

**Dave Jones:** could actually try and put some on, I guess. But I I think this might be very out of date. But anyway, so whether or not it like hardens or does whatever, I don't know. But yeah, no, I think I need some good stuff. But

**Dave Jones:** I don't don't have any to hand. And I just checked Jar, which is my nearest store. They didn't have any. RS components didn't have any. At least a couple of days away. It's not pretty, is it? The problem is trying to solder

**Dave Jones:** membranes like these, it's just it's just going to melt. So, um yeah, don't do that. That's actually that's that's that's not bad. So, that's going to set. Could work. But yeah, it's it's so I don't know what the shelf life of this

**Dave Jones:** thing is. Couldn't find a data sheet. Think you get what you get and you don't get upset. Now you can see where the problem's likely to be here. You can see the like it looks like discoloration, but it seems to be that the silver has

**Dave Jones:** just worn away on that flex. Even though this is not continually flexing, right? If it was continually flexing, you could um think that okay, it's going to like wear off and then little flakes had come off over time and stuff like that. it

**Dave Jones:** like there's nothing like it's not being used in something that's flexing all the time, but it looks like it's sort of almost worn off. So, if we flip that over so we can probe it, okay, if we go

**Dave Jones:** like you can see that the plastic ends here. Okay, so if we probe here and here, right, it's conductive. But if we probe here and here, it's not conductive, right? Even though on this side, if you look at the microscope on this side, you

**Dave Jones:** think that's not broken. There's no break there at all. Right. And but we can see it from the other side. So, right, that's why look the it's just it's completely worn off. So, there's nothing wrong with the contacts in here.

**Dave Jones:** Right. actually to the crimp pins. It's We flip it back over and it's it's that the silver has worn off cuz this is the bottom side right here's the it's the bottom side next to the plastic. This is

**Dave Jones:** all plastic here, right? But we can clearly see that it's kind of like the silver's just worn away or whatever. I I don't know how, but it's like it's like that for every single one of them. Look at that. That's crazy. Okay, so I use my

**Dave Jones:** dodgy silver paint. And here it is. Okay, it's it's dried now. And sure enough, we get continuity. And if I Right, 15 ohms, right, that's good enough for Australia. That's certainly going to uh the micro is going to

**Dave Jones:** recognize that. The other one looks like Yeah, like like 4 ohms, right? So yeah, so that that silver paint, as dodgy as it was, uh worked. But um since then I've have ordered it and I've got my um

**Dave Jones:** little silver conductive ink. I just got it from the local hobby store. Um in fact the same hobby store that I originally got the Indiana Jones train set from. Hobbies in the Hills. I got it from them. They they're just on eBay.

**Dave Jones:** They're not in the hills anymore. I think they're bugged off the coast or something. But anyway, um silver conductive paint. Haven't looked at the data sheet for it. And it comes with um this very nice very nice needle point.

**Dave Jones:** Look at that. That's tiny. Yeah, I didn't want to use that dodgy stuff again. Even though it looks like it kind of worked. It kind of worked. I don't know. Has it has it cracked in there a little bit? Yeah, don't use sort of out

**Dave Jones:** of date uh conductive paint like that. It still seems to work, but yeah, I wouldn't I wouldn't trust it. Okay, I'm going to need a clamp to hold this in place cuz this thing just boing. Here we go. It's because it's a syringe, it's

**Dave Jones:** not going to be the easiest thing to apply. And I've got this hanging up in the air. So it's a little bit I got too much on the end of that. But because that one is No, it's in fact

**Dave Jones:** it's going to short to the one next to it, isn't it? So I shouldn't have done that. Maybe I should get rid of some of that. That was terrible. Muriel started out with way too much there. So can we

**Dave Jones:** scrape away? Yeah, it doesn't really seem possible to apply to use the syringe and this at the same time. This is terrible. Oh, yeah. It spreads out way too much. Yeah. Yeah. I've got to have very little of that. I'll steal

**Dave Jones:** some from over here and place it over here. Yeah, that's the problem with this syringe stuff. I could have like a dispenser, like a paste, automated paste dispenser. Don't have one to hand. Anyway, we we're just trying to bridge

**Dave Jones:** like I'm putting it over the pins, which I don't have to do. Only trying to bridge over that part that's not conductive. Should be doing an end on, shouldn't I? Yeah, this is terrible. Won't give up my day job. Yeah, I really

**Dave Jones:** didn't need much at all. It's not easy when it's hanging up in the air and you can't put your wrist flat on the bench. And usually you just leave these to uh dissolve away. Um they like evaporate away the uh whatever like alcoholy type

**Dave Jones:** stuff is in there or whatever. Um and you can usually apply some heat to them as well. My box of cotton buds has vanished. Don't know where it is. I'm not just going to go to the shop to get

**Dave Jones:** it. So I'll try an alcohol wipe. The glare is really annoying here, but not going to bother to fix it. And no, that's not shorted. Nope. It's a bit how you're doing. Oh, I smeared it out. Oh, I smeared it out by touching the Oh, no.

**Dave Jones:** I've come I Look, I accidentally smeared it out. See if I can rub that off with the wipe. Here we go. Yes, I can. Okay. It's almost as if I'm better off like wiping it all off and then starting again. Wipe

**Dave Jones:** it all off. Start again. doll. All right. Should have been more aware of that, but oh well. Live and learn. All right. Let's try that again, shall we? There we go. Look at that. That's a fat ass trace, isn't it? It's hard to know

**Dave Jones:** how much to pick up from my pile over there. Cuz it just oozed out when I pressed my syringe. Another big ass fat trace. I don't care how fat it is. I just want it to work. Kind of like the fat looking

**Dave Jones:** ones better. Don't know. It's more conductor. So, yeah, you might be able to do this a lot better with a very fine automated dispenser, but it' have to be a real fine jobby. Big fat ones are hilarious, but oh well.

**Dave Jones:** Not going to complain about them not working. Like, they look bigger than they are. They look big because of the lighting on them, but uh they're actually not that huge in the scheme of things. So, what you do now is uh you

**Dave Jones:** either leave it there for like 12 hours, 24 hours or something like that. It depends on the type it is. Um yeah, they actually use like an alcohol in there and you can heat it up like if you get

**Dave Jones:** it to like, you know, 60° or something, you might be able to do it in an hour or something like that. So, you shouldn't try and measure it now while it's wet. You wait until the alcohol or whatever

**Dave Jones:** thinner in it um that actually evaporates um and then you're left with the conductive um silver paint. Yeah. I might put that on some mild heat to accelerate it. Um, but anyway, that that wasn't pretty, but I reckon that is

**Dave Jones:** going to work a treat. Actually, the interesting thing is the the two I did with my other silver paint. That actually looks better, doesn't it? Looks better than this. Uh oh, actually, this is the one that I've done now. Is it

**Dave Jones:** still Is it still wet or is it Yeah. Yeah. Yeah, she's still wet. Okay, no worries. So, I've just got my hot air gun set to 60° and I'm just going to uh blow it over that for the next hour or

**Dave Jones:** something. And hopefully that should be reasonably dry. Get back to you. Let's see if it's solidified. It's a little bit. Yeah. Okay. Maybe. Maybe cuz that's too thick. This seems okay. I I need to give it a little bit longer, but hey, um let's

**Dave Jones:** measure the ohms. Measure that. 3 ohms. No worries. And boom. Yeah, that's great. That's great. I think we're in business. Unless Unless it's degraded somewhere else further up the membrane as well, but I don't want to jinx it.

**Dave Jones:** You can see that one. Yeah, that one hasn't totally evaporated yet. It was too thick. Is that the same on that one? Oh, no. 25 ohms. Yeah. Okay. I I just need to leave that one for a bit longer.

**Dave Jones:** There's just u yeah it just hasn't evaporated all the binding agent. Once that evaporates then you're left with the little solder silver solder balls or whatever they are. Um so yeah I I'll give that a bit longer but it's looking

**Dave Jones:** promising. Okay, I've given it some more time and [Music] hello 12 ohms. No worries. I think that'll get better. It's still a bit spongy. 6 ohms. Yeah, no worries. You see how it's lower the thinner it is. The lower

**Dave Jones:** it is, that's because it's evaporated quicker. And so if we give it enough time, these ones will also get down to like one or two ohms each. Not 100% dry yet, but I'm going to put this back together. And I think we'll find that it

**Dave Jones:** should work as long as there's no other degradation elsewhere in the keypad. Like there could even be some up under here. I just don't know. All I know is that I measured it down here and we could visually see it as well. So

**Dave Jones:** anyway, um so hopefully we fixed that. So hang on. Oh, I haven't put the little uh there's little clips in there that sort of like hold it in place, but anyway, we'll put this back on here for now and we'll

**Dave Jones:** see if we can get it working. Boom. That's the top row. Top row. Yes. Yes. And then this row here. Yes. Yes. Yes, yes, yes, yes, yes, yes, and yes. There you go. Winner winner chicken dinner. There you have it.

**Dave Jones:** That should work a treat, assuming that the receiver on the other end uh works. No worries. So, there you go. That was an interesting repair. I did not expect that. And that's something that I'm struggling to remember where I've if

**Dave Jones:** I've actually seen that sort of degradation in the silver. It's like they have done like a silver roll paint on the um thing. Like it's not like a copper, you know, traces or anything like that. It looks like they've done a

**Dave Jones:** silver paint on there. And for some reason without it flexing, without it actually being part of some flexible thing, it's come a guta and it's worn off. And not just in one spot, it had worn off on like four of the rows like

**Dave Jones:** that. And this one here was borderline like intermittent as well. The columns seem to have been okay, but I redid the columns anyway. But yeah, all of the rows were just gone. The silver and it looked perfect from one side. It looked

**Dave Jones:** fine. like there's nothing wrong with it. Yet you flip it over and you can see the degradation on the other side against the plastic. So maybe some weird chemical things going on there. I don't know. If you seen this before and you

**Dave Jones:** know exactly if you're a chemist should ask Mrs. EV blog. She's a chemist. Anyway, um yeah, some sort of weird thing happening there. It looked fine on one side and yet the other side you can see it was clearly degraded on those

**Dave Jones:** lines. So silver paint for the win. you probably should have some of this uh lying around. And yeah, um there were some suggestions that maybe cuz I did a live um show showed this uh that maybe I could um rejuvenate this sort of stuff

**Dave Jones:** cuz the silver's still in there. Maybe um with with some acetone or something like that perhaps. I don't know. But this still seemed to actually work. So kind of sort of. But anyway, um yeah, groovy stuff and an interesting fault.

**Dave Jones:** Hope you like that. If you did, please give it a big thumbs up. As always, discuss down below. And happy wife, happy life. Catch you next time. [Music]
