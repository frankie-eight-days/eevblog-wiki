---
video_id: kkFFt3vYg9U
title: EEVblog 1576 - Tektronix DMM916 Multimeter Teardown & (Easy) Repair
url: https://www.youtube.com/watch?v=kkFFt3vYg9U
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 29, "3": 50, "4": 66, "5": 84, "6": 101, "7": 114, "8": 127, "9": 138, "10": 152, "11": 169, "12": 188, "13": 205, "14": 220, "15": 246, "16": 267, "17": 283, "18": 297, "19": 317, "20": 335, "21": 352, "22": 370, "23": 385, "24": 402, "25": 419, "26": 442, "27": 459, "28": 480, "29": 506, "30": 528, "31": 546, "32": 562, "33": 578, "34": 596, "35": 612, "36": 628, "37": 642, "38": 661, "39": 688, "40": 707, "41": 724, "42": 745, "43": 765, "44": 787, "45": 806, "46": 819, "47": 835, "48": 851, "49": 863, "50": 877, "51": 895, "52": 909, "53": 925, "54": 943, "55": 956, "56": 973, "57": 995, "58": 1008, "59": 1021, "60": 1038, "61": 1053, "62": 1069, "63": 1084, "64": 1099}
---

**Dave Jones:** Hi, I'm just looking at a one of these Tektronix DMM 916 uh true RMS multimeters that I got in my box of multimeters um that I had in my dungeon. And I've got it set to a 3-V uh

**Dave Jones:** reference source here, and it's not quite 3 V, but when I plugged it in, it was bang on 3 V. Um and if I have a wiggle, wiggle, wiggle yeah, will it Can I make it go back? Hang on.

**Dave Jones:** It was It was working before. Come on. You can do it. There you go. It's Oh, 3.03, but you can see that it's bang on. So, I think that we have a uh problem with the input jack perhaps. Um so, yeah, cuz like obviously

**Dave Jones:** like ADC, reference, everything else is uh is working for this bad boy, but uh it's unfortunate like this is really high-spec uh meter. I haven't uh tried anything else yet. This was the first uh thing I tried, but it's Yeah, look, it's

**Dave Jones:** obviously working. It's bang on, right? 3 V, but spit out you doing. Uh and the only other uh thing I found wrong with it was uh this 9-V battery. Focus, you bastard. There you go. Um yeah, that can happen to 9-V batteries.

**Dave Jones:** Not just which have uh six uh 4A cells in there. Um not just to your double A's and your triple A's. So, beware. But unfortunately, it didn't really leak, but uh yeah, the uh magic smoke escaped from that one and uh physically ejected

**Dave Jones:** itself. So, it's rather interesting. All right, so let's have a look inside this thing. This one doesn't have uh the Royal Australian uh Air Force on here like my other ones. I think this is the only one that doesn't uh have it, cuz I

**Dave Jones:** got a huge auction lot uh of these, and this was donkey's years ago. I got like a dozen of these meters um and I like fixed up and so you know tested and sold the ones that worked and the ones that

**Dave Jones:** didn't work um I left them in the or that were dodgy in some way, I left them in the box. And this is this is one of them. So uh unfortunately the tilting bail actually fell off one of the little

**Dave Jones:** plastic things uh fell off but um yeah, this is like a high-spec meter. I don't know the specs off hand but uh yeah, if you got any knowledge of um who I mean, I assume Tektronix manufactured my Well, no,

**Dave Jones:** maybe they didn't. Maybe they contracted out but like it's a really high-quality meter but as you'll see inside, it's uh old school construction. Where's my bloody screwdriver? Yeah, there's no battery compartment in this thing. So it really is like your old school like 90s

**Dave Jones:** even 80s style construction of a multimeter and don't expect too many surface mount parts in here either. Um and it's got some power on options. See you go, disable auto power turn off beep, test LCD segments. Gold. Oh, nice. Anyway, oh, let's try that,

**Dave Jones:** shall we? Here we go. There you go. Test all the Test all the segments. This one's a bit uh scratched up but it is uh it is dual readout there, dual display. So uh Turn it the right angle. It's got a

**Dave Jones:** plastic clip at the top. It's not the best so don't know what the battery life on this is. There you go. Got some shielding. The piezo. And uh There you go. No, they aren't corroded. They're actually uh well, they're a bit

**Dave Jones:** tarnished but they've actually left the um solder mask off those for and that'd be guard um trace for guard trace reasons. I would suspect Are they? Anyway, that is that is a definite definite deliberate um leaving off of the solder mask there.

**Dave Jones:** And as you can see, as we got old-school trimmers in here. There's our hybrid resistor network. Board-to-board interconnect. Um, and another little carbon trimmer over there. So, that's probably for like three more three more carbon jobbies over there. Oh, we got some

**Dave Jones:** surface mount. There you go. It's not all through-hole. A meter of this advanced thing you're not going to Oh, oh, just it it just lifts out. I've not taken apart one of these in ever since the original lot. And the

**Dave Jones:** battery can like there's no battery compartment. Like it's just But then again, like your Fluke 87s, you know, still got the wired 9-V battery, hasn't it? There you go. We still got the It's got the There's the LCD.

**Dave Jones:** It's rather nice. And there's the switch. If you switch aficionados that looks pretty decent. Should actually set that back to the known position of off before I forget. And there you go. So, no wonder they make it easy to get out cuz the fuses are on the

**Dave Jones:** opposite side. There you go. They got the original uh little fuse jobbies in there. Although, that's a Yeah, yeah, that's a little fuse as well. They got genuine little few little fuse fuses in there. Two input fusible resistors over here.

**Dave Jones:** That's like going to two separate paths. And PTC encapsulated there with some heat shrink. Just in case the uh magic smoke escapes. You you want it exploding everywhere. But, uh yeah, you got the hybrid resistor network. Got another trimmer

**Dave Jones:** there. And uh that's all she wrote. Diode bridge protection. Should I take that apart completely? Oh, why not? Some people will probably get upset if I don't. Um do I have to I've got to take the LCD No. No, I don't

**Dave Jones:** No. No, I just undo it from the back there. I think that has to come off there, and the others I can get from the top side here. To get this board off. But, uh yeah, leave it in the comments

**Dave Jones:** down below if you know who actually manufactured this, and did Tek- Tektronix design it? Don't know. Um although Tektronix have acquired uh various And of course, you know, um they were all acquired by uh Danaher in the end, weren't they?

**Dave Jones:** Fluke and all the rest of them, and Wavetek, and um don't know what you're flapping around in the breeze. All right, so let's Look at me. Yeah, we got it. We got one. Oh, stand off there doesn't actually

**Dave Jones:** connect Oh, wait. No, it doesn't connect to anything. Anyway, it's an NEC jobby. Here you go. NEC fanboys go wild. 78063. So, that's doing all the um LCD uh driving. So, presumably that's not the main processor. So, there's our range switch down there.

**Dave Jones:** That looks in reasonable nick, doesn't it? Well, you know, for the age, I presume this thing is Oh, you know, that's still going to work. Yeah. Don't have a problem with that. Month and date of '97. There you go. '97

**Dave Jones:** 17. And All right, so we have that processor. And what do we got down in here? Oh, I'll have to prop this up. TC8129. What's a TC8129? I don't know, but we've got a 4069 over here. 4069 again. TL062s.

**Dave Jones:** All your favorites. 4053s, of course, maxes. More TL06s. They're fun of the TL062s. Got an 80737. That's a true RMS converter. Not seeing the reference. No? No. Don't see it. Anyway, um interestingly, there's only This is a Whoa.

**Dave Jones:** This is a Hello. That is Whoa. So, this is a two-sided This is a two-sided rain switch. Double-sided rain switch. Now, is this marked? How do I get this back in? Right? Cuz we got the contacts we saw on the other side, and then we've

**Dave Jones:** got all the contacts here. So, that's interesting. Yeah, I'm not seeing any markings there. So, hopefully I'm going to have to like rely like the shaft or do that. But if you got it turned a bit in the wrong location, you're

**Dave Jones:** going to come a gutser. That's interesting. Um Got an ice cream problem up here. That's uh calibration values. Is this your reference over here? That looks Or is that just a regulator? MTS102. No, that's just a transistor, and it's

**Dave Jones:** got emitter base collector there. So, yeah, I don't know. Anyway, this isn't a detailed teardown. I want to Actually, I haven't even looked at the solder the input jacks yet. So, let me just put this back together. So, otherwise

**Dave Jones:** um I'm probably goose that range switch up. From production point of view, this really sucks. No, it's not going to go in. It's slightly Oh, no. No, there we go. Have I got it in the right location? That's AC.

**Dave Jones:** That's DC. Yep. Yep. Yep. I got it I got it the right way. Woohoo. Win. And you can see how annoying this design Oh. This design is just from a production point of view. Please, if you design a

**Dave Jones:** multimeter, don't do it like this. And you got to, you know, take the entire board out to change your fuses. And, you know, I I guess they hadn't They didn't care too much back in those days, but these days it's bit inexcusable. Even,

**Dave Jones:** you know, you could say it's inexcusable back then as well. Oh, well. Let them off the hook. Just got myself an extra long pair of pliers like this for getting in places because I used to have one, but

**Dave Jones:** it's uh it went walkabout. All right, let's get back to the input jacks. And Aha. Sorry. Could have saved You're all probably screaming at me. Um Yeah, hello. Um Of course. Are they like loosey-goosey? I'm going to need a going to need a

**Dave Jones:** bigger boat. I mean, obviously, if you just got shake-proof washer like that, it could easily come a gata. Oh. Yeah. Well, certainly wasn't tight. And I Yeah, I can really can screw that up. No, I really don't like those, but

**Dave Jones:** they uh Nonetheless, like often, yeah, I suspect like, because we're talking like 10 megaohm input impedance there, and we were getting the uh we're getting readings like slightly low and stuff. So, I can only presume that, like, it was just a

**Dave Jones:** really high impedance path there, and that was causing causing a problem. And you probably would have seen that on ohms if I bothered to test that. But, uh yeah, I don't know. Maybe I could unscrew it and clean it and stuff like

**Dave Jones:** that, but I'm just going to put that back together. Is it that easy? Could be. Yeah, bang on. Uh 2.9996 V for 3 V. This isn't my best reference, this is. Uh and if I wiggle wiggle the jack, wiggle wiggle wiggle, yeah. Nah,

**Dave Jones:** it's all good. There you go. You can see that, 2.9996. And that's good enough for Australia, and there's no wiggle. Oh, no, 2.9999 now. Oh. Yeah. Yeah, so there you go. Nice. AC plus DC. Let's take it back to

**Dave Jones:** three. 3.008 for 3 V. Yeah, it's all looking good. Let's see if those fuses are intact and we can measure current. Probe probe probe probe. Yeah, 0.3 milliamps. Uh turn it to microamps. 299.9 microamps. At 300, bang on 300.0

**Dave Jones:** microamps. So, no worries. Although, I can only go to 30 milliamps maximum, but it's intact. There you go. 30. So, that is a winner winner chicken dinner. Probe probe probe. There you go. Um so, that is a uh real

**Dave Jones:** easy it's not even a repair. Um well, I guess it is. Right, it was just a dodgy input jack, but it's very curious that you know, it had a rather than just give no reading at all, it gave a high enough

**Dave Jones:** impedance that it was given a voltage divider with the 10 mega ohm input in nominal 10 or 11 or whatever mega ohm input impedance of this meter. Um and so yeah, it just like uh pl- maybe some kind of tarnishing on the

**Dave Jones:** contacts and combined with the looseness of them and just tighten them up and it pierces through it pierces through any oxidization tarnishing on the contacts and the winner. So, yeah, there you go. Um the Tektronix DMM at 916

**Dave Jones:** multimeter. I wonder if the others are the uh same. That would cuz I've got three of these. Um so yeah, it's a uh I have to check the specs on it, but I do believe like it's a pretty high-end.

**Dave Jones:** It's like I think it's 30 It seems to be a like 30,000 count. So, it's uh you know, it's your four and a half digit e plus. Let's get my 10k reference here. See if the ohms key's good. I'd be surprised if the ohms key

**Dave Jones:** is bad. Because you know, the meter works. It works. 9.991. Yeah, it's a little bit It's a little bit lowish. 903, but I'm pretty sure that'd be within spec, right? No worries. What is it you know, this is I'm surely this

**Dave Jones:** would be a point 05% class instrument, although you wouldn't that's DC volts. You wouldn't get that on your ohms range. That is a simple repair. Hands up if you had one of these. Aha, if we look down here

**Dave Jones:** made in Taiwan. It's in a one so it's one of the Taiwanese manufacturers. Maybe they designed it as well. Um I don't know. It's Uh, isn't early It's I don't know. Did a Brymen have a hand in it back in the early days? Brymen

**Dave Jones:** were making meters back then. But, uh, yeah. Leave it in the comments down below if you know who actually manufactured the Tektronix uh, series multimeters. But, there you go. Repaired. Beautiful. Oh, I'll screw that back together. And Bob's your uncle.

**Dave Jones:** Maybe this is this sort of stuff is annoying. Oh, no. No, that'll just Yeah, I can clean that off. That'll That'll clean up nicely. Shame about the scratches on the screen and stuff. That's not a Is that still screen underneath?

**Dave Jones:** If it is, then uh, you could get medieval on it. Um, and maybe, you know, buff out that window. And yeah, it's a fine multimeter. How's the continuity tester on it? Oh.

**Dave Jones:** That's a It's loud. It's instant. And how's the auto ranging? Ready, set. Oh, ready, set, go. What? Not bad. And it's got like a um, 30 ohm range as well. Brilliant. Or is that 300? Sorry, that'd be a 300 ohm. And 10

**Dave Jones:** milliohms resolution. Nice. And, you know, it's got all sorts of fancy stuff. Like it's got, you know, set up I don't know. All right. And it's got all sorts of fancy whiz-bang stuff. And you can store You can actually Well, if we get

**Dave Jones:** it in exit set up, we actually we can change the number of digits. There you go. It's got auto hold. So, it's got a Fluke auto holdy type thing. What does gold mean? Oh, gold. I was wondering what

**Dave Jones:** gold meant. It's the gold color here. It's invert. So, it's gold. Took me an embarrassing amount of time to figure out what the heck gold meant. Um, so, the auto hold Does that Yeah. Yeah. Yeah, it's got the fluke

**Dave Jones:** style auto hold thing. Touch hold. So, yeah, yeah, it's a fairly capable meter. Store recall. What else do we have in the setup? Can we go side to side? No. And bar graph? Oh, that What? It's got different

**Dave Jones:** mode bar graphs? Does it have like center zero and stuff like that? Probably does. So, yeah, it's got the DBMs and we've got temperature as well and it's pretty capable little thing. Didn't measure the nanofarads. Yeah, it's got 300 residual.

**Dave Jones:** puff that is. Oh, I'll tell you what, I will leave a link down below to my EV blog eBay store and I will auction this off uh starting at 99 cents. So, yeah, if you want it, go for it.

**Dave Jones:** I'm sure it'll uh serve you well. Anyway, there you go. If you've got any details on the Tektronix DMM 916, leave it down below. Last calibrated in 2010. That's still a winning meter. Anyway, if you like that video, please give it a

**Dave Jones:** big thumbs up. Leave it in the comments down below if you um know about the history of the DMM 916 or if you're still using them or you used to use them. Catch you next time.
