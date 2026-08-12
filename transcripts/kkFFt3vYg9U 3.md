---
video_id: kkFFt3vYg9U
title: EEVblog 1576 - Tektronix DMM916 Multimeter Teardown & (Easy) Repair
url: https://www.youtube.com/watch?v=kkFFt3vYg9U
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 17, "3": 31, "4": 59, "5": 73, "6": 84, "7": 101, "8": 110, "9": 132, "10": 141, "11": 152, "12": 162, "13": 182, "14": 193, "15": 205, "16": 217, "17": 236, "18": 253, "19": 269, "20": 280, "21": 291, "22": 311, "23": 322, "24": 338, "25": 349, "26": 364, "27": 381, "28": 391, "29": 408, "30": 426, "31": 442, "32": 456, "33": 466, "34": 487, "35": 509, "36": 530, "37": 546, "38": 562, "39": 576, "40": 590, "41": 608, "42": 615, "43": 630, "44": 642, "45": 660, "46": 671, "47": 700, "48": 717, "49": 730, "50": 742, "51": 761, "52": 773, "53": 792, "54": 807, "55": 830, "56": 844, "57": 863, "58": 872, "59": 889, "60": 899, "61": 912, "62": 923, "63": 938, "64": 949, "65": 960, "66": 979, "67": 992, "68": 1003, "69": 1013, "70": 1028, "71": 1040, "72": 1051, "73": 1063, "74": 1079, "75": 1091, "76": 1108}
---

**Dave Jones:** Hi, I'm just looking at a one of these Tektronix DMM 916 uh true RMS multimeters that I got in my box of multimeters um that I had in my dungeon.

**Dave Jones:** And I've got it set to a 3-V uh reference source here, and it's not quite 3 V, but when I plugged it in, it was bang on 3 V.

**Dave Jones:** Um and if I have a wiggle, wiggle, wiggle yeah, will it Can I make it go back? Hang on. It was It was working before. Come on. You can do it.

**Dave Jones:** There you go. It's Oh, 3.03, but you can see that it's bang on. So, I think that we have a uh problem with the input jack perhaps. Um so, yeah, cuz like obviously like ADC, reference, everything else is uh is working for this bad boy, but uh it's unfortunate like this is really high-spec uh meter.

**Dave Jones:** I haven't uh tried anything else yet. This was the first uh thing I tried, but it's Yeah, look, it's obviously working. It's bang on, right? 3 V, but spit out you doing.

**Dave Jones:** Uh and the only other uh thing I found wrong with it was uh this 9-V battery. Focus, you bastard. There you go. Um yeah, that can happen to 9-V batteries.

**Dave Jones:** Not just which have uh six uh 4A cells in there. Um not just to your double A's and your triple A's. So, beware. But unfortunately, it didn't really leak, but uh yeah, the uh magic smoke escaped from that one and uh physically ejected itself.

**Dave Jones:** So, it's rather interesting. All right, so let's have a look inside this thing. This one doesn't have uh the Royal Australian uh Air Force on here like my other ones.

**Dave Jones:** I think this is the only one that doesn't uh have it, cuz I got a huge auction lot uh of these, and this was donkey's years ago. I got like a dozen of these meters um and I like fixed up and so you know tested and sold the ones that worked and the ones that didn't work um I left them in the or that were dodgy in some way, I left them

**Dave Jones:** in the box. And this is this is one of them. So uh unfortunately the tilting bail actually fell off one of the little plastic things uh fell off but um yeah, this is like a high-spec meter.

**Dave Jones:** I don't know the specs off hand but uh yeah, if you got any knowledge of um who I mean, I assume Tektronix manufactured my Well, no, maybe they didn't.

**Dave Jones:** Maybe they contracted out but like it's a really high-quality meter but as you'll see inside, it's uh old school construction. Where's my bloody screwdriver? Yeah, there's no battery compartment in this thing.

**Dave Jones:** So it really is like your old school like 90s even 80s style construction of a multimeter and don't expect too many surface mount parts in here either. Um and it's got some power on options.

**Dave Jones:** See you go, disable auto power turn off beep, test LCD segments. Gold. Oh, nice. Anyway, oh, let's try that, shall we? Here we go. There you go. Test all the Test all the segments.

**Dave Jones:** This one's a bit uh scratched up but it is uh it is dual readout there, dual display. So uh Turn it the right angle. It's got a plastic clip at the top.

**Dave Jones:** It's not the best so don't know what the battery life on this is. There you go. Got some shielding. The piezo. And uh There you go. No, they aren't corroded.

**Dave Jones:** They're actually uh well, they're a bit tarnished but they've actually left the um solder mask off those for and that'd be guard um trace for guard trace reasons. I would suspect Are they?

**Dave Jones:** Anyway, that is that is a definite definite deliberate um leaving off of the solder mask there. And as you can see, as we got old-school trimmers in here. There's our hybrid resistor network.

**Dave Jones:** Board-to-board interconnect. Um, and another little carbon trimmer over there. So, that's probably for like three more three more carbon jobbies over there. Oh, we got some surface mount. There you go.

**Dave Jones:** It's not all through-hole. A meter of this advanced thing you're not going to Oh, oh, just it it just lifts out. I've not taken apart one of these in ever since the original lot.

**Dave Jones:** And the battery can like there's no battery compartment. Like it's just But then again, like your Fluke 87s, you know, still got the wired 9-V battery, hasn't it? There you go.

**Dave Jones:** We still got the It's got the There's the LCD. It's rather nice. And there's the switch. If you switch aficionados that looks pretty decent. Should actually set that back to the known position of off before I forget.

**Dave Jones:** And there you go. So, no wonder they make it easy to get out cuz the fuses are on the opposite side. There you go. They got the original uh little fuse jobbies in there.

**Dave Jones:** Although, that's a Yeah, yeah, that's a little fuse as well. They got genuine little few little fuse fuses in there. Two input fusible resistors over here. That's like going to two separate paths.

**Dave Jones:** And PTC encapsulated there with some heat shrink. Just in case the uh magic smoke escapes. You you want it exploding everywhere. But, uh yeah, you got the hybrid resistor network.

**Dave Jones:** Got another trimmer there. And uh that's all she wrote. Diode bridge protection. Should I take that apart completely? Oh, why not? Some people will probably get upset if I don't.

**Dave Jones:** Um do I have to I've got to take the LCD No. No, I don't No. No, I just undo it from the back there. I think that has to come off there, and the others I can get from the top side here.

**Dave Jones:** To get this board off. But, uh yeah, leave it in the comments down below if you know who actually manufactured this, and did Tek- Tektronix design it? Don't know.

**Dave Jones:** Um although Tektronix have acquired uh various And of course, you know, um they were all acquired by uh Danaher in the end, weren't they? Fluke and all the rest of them, and Wavetek, and um don't know what you're flapping around in the breeze.

**Dave Jones:** All right, so let's Look at me. Yeah, we got it. We got one. Oh, stand off there doesn't actually connect Oh, wait. No, it doesn't connect to anything. Anyway, it's an NEC jobby.

**Dave Jones:** Here you go. NEC fanboys go wild. 78063. So, that's doing all the um LCD uh driving. So, presumably that's not the main processor. So, there's our range switch down there.

**Dave Jones:** That looks in reasonable nick, doesn't it? Well, you know, for the age, I presume this thing is Oh, you know, that's still going to work. Yeah. Don't have a problem with that.

**Dave Jones:** Month and date of '97. There you go. '97 17. And All right, so we have that processor. And what do we got down in here? Oh, I'll have to prop this up.

**Dave Jones:** TC8129. What's a TC8129? I don't know, but we've got a 4069 over here. 4069 again. TL062s. All your favorites. 4053s, of course, maxes. More TL06s. They're fun of the TL062s.

**Dave Jones:** Got an 80737. That's a true RMS converter. Not seeing the reference. No? No. Don't see it. Anyway, um interestingly, there's only This is a Whoa. This is a Hello.

**Dave Jones:** That is Whoa. So, this is a two-sided This is a two-sided rain switch. Double-sided rain switch. Now, is this marked? How do I get this back in? Right? Cuz we got the contacts we saw on the other side, and then we've got all the contacts here.

**Dave Jones:** So, that's interesting. Yeah, I'm not seeing any markings there. So, hopefully I'm going to have to like rely like the shaft or do that. But if you got it turned a bit in the wrong location, you're going to come a gutser.

**Dave Jones:** That's interesting. Um Got an ice cream problem up here. That's uh calibration values. Is this your reference over here? That looks Or is that just a regulator? MTS102. No, that's just a transistor, and it's got emitter base collector there.

**Dave Jones:** So, yeah, I don't know. Anyway, this isn't a detailed teardown. I want to Actually, I haven't even looked at the solder the input jacks yet. So, let me just put this back together.

**Dave Jones:** So, otherwise um I'm probably goose that range switch up. From production point of view, this really sucks. No, it's not going to go in. It's slightly Oh, no. No, there we go.

**Dave Jones:** Have I got it in the right location? That's AC. That's DC. Yep. Yep. Yep. I got it I got it the right way. Woohoo. Win. And you can see how annoying this design Oh.

**Dave Jones:** This design is just from a production point of view. Please, if you design a multimeter, don't do it like this. And you got to, you know, take the entire board out to change your fuses.

**Dave Jones:** And, you know, I I guess they hadn't They didn't care too much back in those days, but these days it's bit inexcusable. Even, you know, you could say it's inexcusable back then as well.

**Dave Jones:** Oh, well. Let them off the hook. Just got myself an extra long pair of pliers like this for getting in places because I used to have one, but it's uh it went walkabout.

**Dave Jones:** All right, let's get back to the input jacks. And Aha. Sorry. Could have saved You're all probably screaming at me. Um Yeah, hello. Um Of course. Are they like loosey-goosey?

**Dave Jones:** I'm going to need a going to need a bigger boat. I mean, obviously, if you just got shake-proof washer like that, it could easily come a gata. Oh. Yeah.

**Dave Jones:** Well, certainly wasn't tight. And I Yeah, I can really can screw that up. No, I really don't like those, but they uh Nonetheless, like often, yeah, I suspect like, because we're talking like 10 megaohm input impedance there, and we were getting the uh we're getting readings like slightly low and stuff.

**Dave Jones:** So, I can only presume that, like, it was just a really high impedance path there, and that was causing causing a problem. And you probably would have seen that on ohms if I bothered to test that.

**Dave Jones:** But, uh yeah, I don't know. Maybe I could unscrew it and clean it and stuff like that, but I'm just going to put that back together. Is it that easy?

**Dave Jones:** Could be. Yeah, bang on. Uh 2.9996 V for 3 V. This isn't my best reference, this is. Uh and if I wiggle wiggle the jack, wiggle wiggle wiggle, yeah.

**Dave Jones:** Nah, it's all good. There you go. You can see that, 2.9996. And that's good enough for Australia, and there's no wiggle. Oh, no, 2.9999 now. Oh. Yeah. Yeah, so there you go.

**Dave Jones:** Nice. AC plus DC. Let's take it back to three. 3.008 for 3 V. Yeah, it's all looking good. Let's see if those fuses are intact and we can measure current.

**Dave Jones:** Probe probe probe probe. Yeah, 0.3 milliamps. Uh turn it to microamps. 299.9 microamps. At 300, bang on 300.0 microamps. So, no worries. Although, I can only go to 30 milliamps maximum, but it's intact.

**Dave Jones:** There you go. 30. So, that is a winner winner chicken dinner. Probe probe probe. There you go. Um so, that is a uh real easy it's not even a repair.

**Dave Jones:** Um well, I guess it is. Right, it was just a dodgy input jack, but it's very curious that you know, it had a rather than just give no reading at all, it gave a high enough impedance that it was given a voltage divider with the 10 mega ohm input in nominal 10 or 11 or whatever mega ohm input impedance of this meter.

**Dave Jones:** Um and so yeah, it just like uh pl- maybe some kind of tarnishing on the contacts and combined with the looseness of them and just tighten them up and it pierces through it pierces through any oxidization tarnishing on the contacts and the winner.

**Dave Jones:** So, yeah, there you go. Um the Tektronix DMM at 916 multimeter. I wonder if the others are the uh same. That would cuz I've got three of these. Um so yeah, it's a uh I have to check the specs on it, but I do believe like it's a pretty high-end.

**Dave Jones:** It's like I think it's 30 It seems to be a like 30,000 count. So, it's uh you know, it's your four and a half digit e plus. Let's get my 10k reference here.

**Dave Jones:** See if the ohms key's good. I'd be surprised if the ohms key is bad. Because you know, the meter works. It works. 9.991. Yeah, it's a little bit It's a little bit lowish.

**Dave Jones:** 903, but I'm pretty sure that'd be within spec, right? No worries. What is it you know, this is I'm surely this would be a point 05% class instrument, although you wouldn't that's DC volts.

**Dave Jones:** You wouldn't get that on your ohms range. That is a simple repair. Hands up if you had one of these. Aha, if we look down here made in Taiwan.

**Dave Jones:** It's in a one so it's one of the Taiwanese manufacturers. Maybe they designed it as well. Um I don't know. It's Uh, isn't early It's I don't know. Did a Brymen have a hand in it back in the early days?

**Dave Jones:** Brymen were making meters back then. But, uh, yeah. Leave it in the comments down below if you know who actually manufactured the Tektronix uh, series multimeters. But, there you go.

**Dave Jones:** Repaired. Beautiful. Oh, I'll screw that back together. And Bob's your uncle. Maybe this is this sort of stuff is annoying. Oh, no. No, that'll just Yeah, I can clean that off.

**Dave Jones:** That'll That'll clean up nicely. Shame about the scratches on the screen and stuff. That's not a Is that still screen underneath? If it is, then uh, you could get medieval on it.

**Dave Jones:** Um, and maybe, you know, buff out that window. And yeah, it's a fine multimeter. How's the continuity tester on it? Oh. That's a It's loud. It's instant. And how's the auto ranging?

**Dave Jones:** Ready, set. Oh, ready, set, go. What? Not bad. And it's got like a um, 30 ohm range as well. Brilliant. Or is that 300? Sorry, that'd be a 300 ohm.

**Dave Jones:** And 10 milliohms resolution. Nice. And, you know, it's got all sorts of fancy stuff. Like it's got, you know, set up I don't know. All right. And it's got all sorts of fancy whiz-bang stuff.

**Dave Jones:** And you can store You can actually Well, if we get it in exit set up, we actually we can change the number of digits. There you go. It's got auto hold.

**Dave Jones:** So, it's got a Fluke auto holdy type thing. What does gold mean? Oh, gold. I was wondering what gold meant. It's the gold color here. It's invert. So, it's gold.

**Dave Jones:** Took me an embarrassing amount of time to figure out what the heck gold meant. Um, so, the auto hold Does that Yeah. Yeah. Yeah, it's got the fluke style auto hold thing.

**Dave Jones:** Touch hold. So, yeah, yeah, it's a fairly capable meter. Store recall. What else do we have in the setup? Can we go side to side? No. And bar graph?

**Dave Jones:** Oh, that What? It's got different mode bar graphs? Does it have like center zero and stuff like that? Probably does. So, yeah, it's got the DBMs and we've got temperature as well and it's pretty capable little thing.

**Dave Jones:** Didn't measure the nanofarads. Yeah, it's got 300 residual. puff that is. Oh, I'll tell you what, I will leave a link down below to my EV blog eBay store and I will auction this off uh starting at 99 cents.

**Dave Jones:** So, yeah, if you want it, go for it. I'm sure it'll uh serve you well. Anyway, there you go. If you've got any details on the Tektronix DMM 916, leave it down below.

**Dave Jones:** Last calibrated in 2010. That's still a winning meter. Anyway, if you like that video, please give it a big thumbs up. Leave it in the comments down below if you um know about the history of the DMM 916 or if you're still using them or you used to use them.

**Dave Jones:** Catch you next time.
