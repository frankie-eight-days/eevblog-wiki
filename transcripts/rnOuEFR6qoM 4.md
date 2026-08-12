---
video_id: rnOuEFR6qoM
title: EEVblog #890 - ArmourCard Active RFID Jamming Teardown
url: https://www.youtube.com/watch?v=rnOuEFR6qoM
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 26, "3": 36, "4": 48, "5": 60, "6": 70, "7": 83, "8": 92, "9": 111, "10": 127, "11": 137, "12": 150, "13": 162, "14": 172, "15": 186, "16": 197, "17": 210, "18": 223, "19": 231, "20": 241, "21": 253, "22": 263, "23": 280, "24": 296, "25": 304, "26": 312, "27": 322, "28": 333, "29": 343, "30": 354, "31": 367, "32": 387, "33": 399, "34": 409, "35": 419, "36": 427, "37": 444, "38": 455, "39": 467, "40": 478, "41": 489, "42": 498, "43": 513, "44": 533, "45": 546, "46": 559, "47": 571, "48": 584, "49": 593, "50": 607, "51": 619, "52": 629, "53": 645, "54": 652, "55": 660, "56": 674, "57": 682, "58": 694, "59": 705, "60": 715, "61": 725, "62": 734, "63": 745, "64": 755, "65": 765, "66": 771, "67": 780, "68": 790, "69": 801, "70": 810, "71": 824, "72": 841, "73": 851, "74": 864, "75": 883, "76": 896, "77": 907, "78": 915, "79": 929, "80": 939, "81": 960, "82": 971, "83": 985, "84": 997, "85": 1014, "86": 1029, "87": 1041, "88": 1051, "89": 1071, "90": 1081, "91": 1089, "92": 1106, "93": 1114, "94": 1125, "95": 1140, "96": 1150, "97": 1162, "98": 1180, "99": 1191, "100": 1202, "101": 1211, "102": 1219, "103": 1229, "104": 1242, "105": 1248, "106": 1259, "107": 1272, "108": 1285, "109": 1300, "110": 1324, "111": 1336, "112": 1344, "113": 1353, "114": 1368, "115": 1378, "116": 1393, "117": 1403, "118": 1414, "119": 1425, "120": 1438, "121": 1451, "122": 1461, "123": 1473, "124": 1490, "125": 1501}
---

**Dave Jones:** Hi, in a previous video we took a look at the security of the RFID uh Paywave, PayPass, whatever you want to call it, nearfield coms system in modern credit cards, be they uh Visa, Mastercard or whatever.

**Dave Jones:** They contain a coil in here which allows you to do a contactless uh payment. Uh they're very common in Australia. I know they're uh not common or not available in some other countries, but very common here.

**Dave Jones:** You just basically tap the things and go. And you can actually see the inductive coil inside there. These little, you know, a couple of turns around the outside of the card like that.

**Dave Jones:** And so, uh, click here if you haven't seen the previous video and watch that first. Now, somebody on, uh, Twitter pointed out that you can buy active RFID scanners.

**Dave Jones:** Uh, you can actually get them from the local JB Hi-Fi store here in Australia, which is like a local uh, you know, they sell electronic uh, consumer goods, TVs and DVDs and computers and everything else.

**Dave Jones:** They sell an active RFID jammer. So, I thought we'd do a tear down of it and also give it a try to see exactly how this thing actually works.

**Dave Jones:** It is an active one. It's not a passive one like we looked at. You can just use some al foil. For those who don't know, al foil, aluminium foil, or as Yanks like to call it, aluminum foil, no one in Australia calls it aluminum foil.

**Dave Jones:** Aluminium foil more than good enough if you put that um just like on one side of the card. Uh is good enough in your wallet or your purse or whatever.

**Dave Jones:** Good enough to protect you against um any skimming or fraud or anything like that if p if a person uh is close to you with an RFID reader. And this is an active jammer instead of a passive attenuator, which is what aluminium foil is, or you can buy wallets or purses that I looked at in the previous video.

**Dave Jones:** So, this one's actually looks like it's from Australian company. It's called the Armor Card, armor.com.au. It's um electronic geming technology, 13.56 MHz, only works on that uh frequency. And it's supposed to be uh powered, so it's supposed to be a battery inside this thing.

**Dave Jones:** It's not just a passive thing like these uh cards are where they basically just work with the uh magnetic field that they pick up from the uh reader/ transmitter.

**Dave Jones:** Uh this one actually contains a battery and actively jams it. Um so yeah, I thought we'd take a look at it. A, does it work? And B, hopefully we can do a tear down of what's inside this puppy.

**Dave Jones:** Let's go. If we have a quick look at the card itself, it's uh it's reasonably thick. So, it's not credit card thin. It's like at least uh oh, two or three credit cards or something like that.

**Dave Jones:** But considering that it contains the circuitry, the battery, everything else, then you know, n that's okay. Designed to slip into your wallet or your purse and actively continuously actively jam.

**Dave Jones:** And it's got a little uh capacitive touch switch on here that allows you to uh just test the thing or turn it off if you're doing a transaction. But it'd be a pain in the butt if you got to get this thing out of your wallet along with your credit card.

**Dave Jones:** And then de, you know, and then Well, let's try it. Press it and bingo, it's flashing. There we go. So, it does have an internal battery source. Uh, it's disabling the jamming and doing the battery test.

**Dave Jones:** Haven't read the instructions. Presumably, uh, green means the battery is okay. But uh it's also got an active jammy light which uh hopefully should come on when we put our nearfield com's mobile phone next to it and try and actually read a card.

**Dave Jones:** And if we flip it over to the other side here, you can actually uh maybe start to see a pattern of stuff inside there, but uh you can actually see the coil around the outside.

**Dave Jones:** Check it out. There we go. Looks like they got a couple of turns of this thing. Quite a few going all the way around. You have to get it the right light, of course.

**Dave Jones:** There's the little via down there going down into the board. So, we've just got a PCB material with this plastic sandwiched either side, and it's been quality assurance tested.

**Dave Jones:** So, let's put our mobile phone up with an NFC uh card reading tag. I've turned the NFC uh on, and let's see if that Yep, it comes on. Sure.

**Dave Jones:** Well, it fl Yeah, it's flashing. There you go. And that will probably coincide with the uh packets cuz as we saw in the previous video, the NFC uh is continually scanning out.

**Dave Jones:** It's continually sending out a signal uh a uh packet trying to get those cards to wake up. So yeah, it can detect that and work. How far back? Oh, it's got to be Let me Let me try it.

**Dave Jones:** It's actually got to be fairly close. It's got to be like a couple of centimeters, an inch away at most. So, yeah, it's not terrific. So, presumably, you don't need to uh disable this thing because this thing's going to typically stay in your wallet or your purse or whatever.

**Dave Jones:** Then, you're going to get your card out and you're going to uh tap it and uh do your uh payment, of course, like that. So, you know, look, it still worked.

**Dave Jones:** No problems at all. And that was, you know, like 6 in away from the thing or something. So, you know, you don't really need to disable it. It's always active.

**Dave Jones:** It's always there ready to receive and then jam. So, let's try that again. But have our card next to that. And yeah, you can actually see it's still flashing through there.

**Dave Jones:** And that is not going to scan that at all. So, yes, it does seem to work. And yes, I've played around with it. And as long as you keep it maybe if we keep it this far away.

**Dave Jones:** Well, yeah, there we go. if we get to a point where you take it a once again, you know, 5 cm away, um something like that, an inch or two away, you can easily still read your uh card.

**Dave Jones:** So, yeah, it's got to be right next to it in your wallet. So, right there, if you've got a large purse um or something like that, then it it actually may not be that effective.

**Dave Jones:** And check this out. In the store where I bought it from, JB Hi-Fi, I couldn't believe this. It was absolutely hilarious. Look where it is positioned to the FPOST terminal there, right next to it.

**Dave Jones:** So, you've got an R active RFID jammer right next to the RFID reader. And yes, I did actually have problems with it. And yes, the shop assistant said, "Oh, yeah, the cards we have to put at a certain angle to make them work." So, right there, that's a downside of one of these active jammers.

**Dave Jones:** It looks like it has to be reasonably close, as does uh the owl foil as well, but at least the owl foil can uh go like on the outer pocket of your purse or something or your wallet uh that then folds over.

**Dave Jones:** It's going to protect your card fairly well, whereas this thing um you know, it has to be close. So, just be aware of that. Right. So, just like in the previous video, I'm going to use my magnetic uh Hfield probe here.

**Dave Jones:** I'm going to be able to put that on there and then we're going to be able to uh capture uh some packets on there and exactly and see exactly how it's jamming it.

**Dave Jones:** Oh, that's not a bad one. In fact, you can see the decay uh well, you can see it ramp up in amplitude as I approached it and then uh ramp back down in amplitude.

**Dave Jones:** So, I've just captured some data here without the armor card. So, this is a proper uh credit card transaction uh as we saw in the previous video. So this is the 100% uh modulation that basically pings the uh card and then we've got the data return over here.

**Dave Jones:** You can see this is the modulation coming back the 800 kHz or so modulation on and the data coming back from the credit card. So this is what must get uh spoofed inside this uh armor card.

**Dave Jones:** It must be just sending back random data or doing something else. And as we saw in the previous video, the ISO standard for these RFID contactless cards actually contains an anti-colision uh system.

**Dave Jones:** So, it's designed to have multiple cards in the field. So, but in theory, um it shouldn't be hard to actually um spoof this at all and just corrupt it with just random data all over the place.

**Dave Jones:** You know, the window uh the time window when it's actually uh supposed to happen. So, you know, you can just go in there and just modulate um randomly and just screw everything up.

**Dave Jones:** It's probably not that hard at all. Okay, I'll do that exact same mark capture again with the same trigger point and everything else, but now I've got the armor card directly under the credit card.

**Dave Jones:** So, let's give it a go. And whoa, bingo. Look, that's very periodic, isn't it? That's periodic modulation right there. And it's the same. It does not change at all.

**Dave Jones:** So once again, here is our um here is our phone, our RFID reader uh pinging this doing its 100% modulation and then it expects something bad. But look, this thing started started to corrupt dur like it's during the whole time period before and after this.

**Dave Jones:** It's just always doing it. So it looks like as soon as it detects any sort of field at all, it's just continually modulating like that. So that will definitely completely screw it up.

**Dave Jones:** Yeah, that's that's exactly how it's doing it. And that's all you need to do. Um either but in this case, it's not just random data. It's just complete it's just continually uh repeating in that frequency range that we had before.

**Dave Jones:** We can get in there and actually measure that, but it's going to be a similar uh frequency range to uh what's expected by the ISO standard, of course, but they're just continually pumping this crap out and that's what causes the interference.

**Dave Jones:** That's going to work a treat. And yep, there you go. uh 862 kHz, round about that 847. I'm not going to get in there and dick around. So, it's within the uh modulation frequency that the RFID protocol expects.

**Dave Jones:** And that's how it's screwing it up. Too easy. And by the way, for those wondering uh if you need to fully enase your credit card in our foil, the answer is no, you don't.

**Dave Jones:** It just has to be near enough that it uh affects the the transformer properties of cuz that's effectively as I explained in previous video effectively what this is a transformer with a primary and a secondary here.

**Dave Jones:** Let's give that a try. Put it over there. Nope. Doesn't work at all. Maybe if we raise it by that I don't know the thickness of that. What 15 mm or something?

**Dave Jones:** Yep. Got it. Okay. Okay. So, it needs to be somewhere under that. So, there you go. That's not very uh thick at all. Let's try that. That will maybe work.

**Dave Jones:** No. No. Let's try a thicker one. Not as thick as the uh tape here. And yeah, we're able to get that. So, there you go. Maybe 10 mm within that rule of thumb.

**Dave Jones:** And I know people wanted to see this thing torn down before I turned it on. But in this case, it might be a destructive tear down. I'm not uh sure.

**Dave Jones:** I'm not sure if it's potted inside, whether or not this is just a cap which will just uh pop off or whether, you know, I don't know. Have to dremel the thing.

**Dave Jones:** So, wanted to try it first. But anyway, let's tear it apart. And it is starting to uh snap off not easily, but it's coming. And bingo. This solves the first question I had, which is what battery does it use inside this thing?

**Dave Jones:** It's got a lithium manganese dioxide cell in it. And I'll link in the data sheet down below. We can still make out the part number here. 3volt nominal 100 milliamp hour capacity.

**Dave Jones:** And even though this thing looks like a lithium ion rechargeable battery, it's not because that wouldn't work. That would be silly because you would, you know, you hardly ever would use this thing in a magnetic field.

**Dave Jones:** And even then, it's only for, you know, a few seconds. You wouldn't get the energy required in order to uh recharge a battery. So, it's got to have a primary battery in there.

**Dave Jones:** How long it lasts? Probably actually many, many years because this thing does not require much at all. Low power micros of course are a dime a dozen. They, you know, run on the sniff of an oily rag.

**Dave Jones:** And um, you know, even on the tiny coin cell, this is like 100 milliamp uh, capacity. It's a fairly uh, decent size, you know, grunty cell for this kind of application.

**Dave Jones:** And all you've got to do is have that lowowered. It doesn't even need to be a micro in there. It could just be discrete uh circuitry that just as we saw on because it's a regular periodic pulse.

**Dave Jones:** You could just do that with just, you know, jelly bean logic stuff and uh get away with that. And all you've got to do, as I showed in the previous video, is well, I've got it here.

**Dave Jones:** There we go. All you've got to do is have the micro like this and then just have a treat or in this case to be a MOSFET that just puts a load across the coil and that's all it is.

**Dave Jones:** It doesn't really take any, you know, any major energy to switch on that MOSFET and put that load across the coil. So, you could run for years on this thing.

**Dave Jones:** So, I wouldn't worry, I wouldn't be concerned with this thing going out. I'm sure they've done their engineering to, you know, ensure that it lasts for a long, long time.

**Dave Jones:** You know, 5 year, you know, basically shelf life of the battery kind of thing. And this thing actually still works a treat even after taking that off. Haven't taken the front off yet.

**Dave Jones:** And, uh, there we go. And if we hook that up, there we go. it's still flashing away. So, you know, the the leads on these things are going to take uh the most current on this thing.

**Dave Jones:** So, it could like just it may not even bother to detect the field. Of course, it could just be continually going switching that transistor on and on in that fixed period cuz that's all you have to do.

**Dave Jones:** And it takes bugger all energy to switch a MOSFET like that off and on. So, you know, why not just keep doing it all the time? It only needs to run at that 800 kHz or whatever.

**Dave Jones:** It's bugger all. And that there is no doubt our um incircuit programming interface for our micro whatever that happens to be. Got to get the top side off. It is sort of like heat staked in here the plastic.

**Dave Jones:** So they just got some holes in there. So hopefully we can pop the top off and have a look at the circuitry. And of course, even though I said you could do this with like jelly bean uh logic kind of stuff, you know, we've got to have the ability to read the capacitive uh touch sensor here and flash the lead and do stuff like that.

**Dave Jones:** So, no doubt it's just some low power micro like a MSP 430 or something. Oops. That's what you get when you're trying to use a knife to uh try and slice across.

**Dave Jones:** I was being quite gentle, but it looks like it hooked some of the uh case of the battery. And yeah, that's the uh magic fluid. And if this was uh smellvision, um yeah, you'd be able to smell like smell that.

**Dave Jones:** It smells like um isopropyl alcohol. But no worries. Look at that. still works a treat. And uh yep, beautiful. Well, there we go. L536 something or other. Off the top of my head, I'm not sure what that one is.

**Dave Jones:** I'll have to give that a bit of a Google. I'm surprised they use a crystal in there. You don't really need that sort of uh accuracy. So, just an internal uh the internal RC oscillator probably would have been enough inside a micro, I would have thought.

**Dave Jones:** Anyway, so yeah, that's all there is. Um, that's the only circuitry in there. Just a bunch of uh passives and that one micro. That's it. And the coil on the outside, of course.

**Dave Jones:** Now, our battery died, but granted, I have come back the next day and I'm shooting this, so it all just uh dried out. So, it just hooked on a couple of AAA's there.

**Dave Jones:** And I've been uh trying to probe around the signals here. And sorry, I haven't been able to find anything. And this is not the least bit surprising because the transistor on here, there is no external transistor.

**Dave Jones:** There's no, you know, SO 23 uh package or anything like that. So, there's no external transistor. They're obviously using an internal transistor in the micro to drive the load across the coil here.

**Dave Jones:** But, of course, it's going to be or it's going to be a MOSFET um CMOS output of course, but it's going to be an open drain one. So, if you go probing there, you're not going to see anything switching on the output because it's just going low low like like it's not you've got to have something uh you've got to have an induced magnetic field to induce a current in here so that you can

**Dave Jones:** actually have a current flowing through the uh coil and the uh transistor in order to see it switch. But I do believe that it is simply continually switching the load across this coil.

**Dave Jones:** And of course, if there's no external magnetic field, there's no current. So you can do that with essentially uh no uh current consumption penalty. So unfortunately there's nothing uh interesting to see if you probe around on this thing.

**Dave Jones:** Uh but we've seen it with our Hfield uh probe here that it's basically continually I'm not going to use the word transmitter. It's continually modulating uh this coil here.

**Dave Jones:** continually putting a load across this coil so that as soon as an a coupling field comes in, then it will instantly start uh modulating onto the primary of the transformer here and it's going to corrupt the thing because you know that's just going to screw your day.

**Dave Jones:** If you're the reader here and you're expecting a uh coded uh protocol back out of the modulation here at the 847.5 kHz modulation uh frequency, then you're just going to get the data is just going to be garbage.

**Dave Jones:** It's, you know, it's going to completely screw it up. So, yeah, this thing is going to work a treat. No worries whatsoever. And it's drawing about four micro amps for those playing along at home just sitting there like that.

**Dave Jones:** And if we go there, the lead obviously will uh huge. The lead will jump that right up. No worries. And if we bring our reader close to it, what do we get?

**Dave Jones:** Yeah, jumps up to well 300. It's doing a few things there, but yeah, it's jumping around the place. But you've got to be careful actually using a uh magnetic coupling thing like this on to essentially what is we've got like, you know, loops in here.

**Dave Jones:** We've got wires. It's going to And we're looking at uh micro amps here. So, you've got to be careful this doesn't induce something into the wiring and the test setup.

**Dave Jones:** And that's a real concern here. So, I wouldn't take those figures at face value. It's, you know, this is going to be tr something that's a bit tricky to measure.

**Dave Jones:** So, I'm just around here seeing what we got. But yeah, you would have to uh check your test setup and rule out that you're not actually uh inducing current into uh either your test setup, your wiring, uh the ground system or anything like that.

**Dave Jones:** And of course, this thing has a patent. So, we can go in here and have a look. It's from a company called Harris Te Proprietary Limited here in New South Wales.

**Dave Jones:** And they have had this uh granted apparently. So, we can look at the details. So, here it is. inhibiting unauthorized contactless reading of a contactless readable object. Patent speak.

**Dave Jones:** Yet again, they actually call it an antenna. They don't call it a uh coil. And it basically, I won't bore you with the uh details here. You can read it for yourself, but it's basically saying that it uh is sending out it emits the jamming signal in response to receiving the interrogation signal.

**Dave Jones:** So it looks like it's not continuously doing it. Even though I think that's a perfectly valid technique and it appears to be what they're doing, but maybe they couldn't get the patent on that.

**Dave Jones:** Maybe they had to, you know, get it to get the interrogation signal before the before they emit the jam in otherwise it's a like it's a different use case usage case for patenting the idea perhaps.

**Dave Jones:** So yeah, anyway, that's what it seems to uh be and blah blah blah. We can go and read all the details and blur. It's as boring as the proverbial bat poo, but they are saying here that uh about 3 cm of the jamming uh device and they're saying about 2 cm here.

**Dave Jones:** So, which one is it? I'm not sure. But, uh yeah, it's that's what we saw. Basically, it needs to be within, you know, a couple of centimeters of this thing to be uh effective.

**Dave Jones:** Although at a larger range, it could actually be annoying. If it is transmitting all the time or it's just periodically thinking it's got uh it's being interrogated, then it might just transmit something.

**Dave Jones:** So, as we saw in the example, if it's sitting next to the F-POS terminal on the counter of the store, that could be, you know, that could be a problem.

**Dave Jones:** But it does get a bit more interesting. Uh down here, we have a bit more of a block diagram modulator, de modulator, because it has to signal interrogation detector.

**Dave Jones:** It's got to do all that sort of jazz. Uh it says recharge port here, which um they've obviously gone away from that cuz this is a uh primary uh cell inside here.

**Dave Jones:** And we've actually got some schematic stuff. Look, ADC touch. So they're um they not implementing that with your more traditional thing. And it's interesting that they've got a discrete driver transistors for the leads here.

**Dave Jones:** We didn't see those in there. So they've obviously done away with them. You don't need it. I mean, you just pulse a lead. You could easily do that with the uh micro.

**Dave Jones:** So, they've got the part numbers and everything though in the pattern. And here's the uh loop antenna. Here's the RF detection uh circuitry. Four diodes. We did see a whole bunch of uh diodes in there.

**Dave Jones:** So, that's how they're getting the RF detection out. They're detecting the uh modulation uh well, they're detecting the interrogation uh frequency, the interrogation pulses that we uh saw before.

**Dave Jones:** That's boring. We've got a micro. Oh, look. Pin numbers. There we go. Can we work out what uh maybe I'll link in the uh pattern down below. Maybe we can actually get what uh micro that is because there you go.

**Dave Jones:** Is that three? Oh no. 13.56. So they are using they're you is that a 13.56 MHz crystal there? Interesting. Anyway, we should be able to get what micro that they're actually using there.

**Dave Jones:** But as I said, we didn't see any uh discrete MOSFETs on the output. So obviously it's uh it's changed and then they go into how it all works with the web browser what serving processing system are they trying to do a broader get a broader patent so that they can potentially patent troll people I hope not and then we've got the physical embodiment of the thing and uh

**Dave Jones:** oh look even example uh pass like you know example applications and everything else and then we've got a uh photo of the thing and but uh it used to looks like It used to be called payuard.

**Dave Jones:** There you go. And it's changed and that's the end of the pattern. Anyway, I'll link it in down below if you want to see all the gory details. So, there you have it.

**Dave Jones:** There's a look inside the armor card, an RFID active jammer, and it's probably going to do the business, but ultimately, I can't see why you would bother having something like this.

**Dave Jones:** And you know, it's battery's going to run out in a few years time. Just if you're worried about security with this thing, just put some owl foil inside your your wallet or your purse or whatever or wrap your passport in it or, you know, get one of the shielding.

**Dave Jones:** You can for a much cheaper cost. This was $58 Australian, much cheaper. You can get just the shielding uh sleeves that you can put your passport or your credit cards into.

**Dave Jones:** But ultimately, as I said in the previous video, the threat is actually really quite low. Yes, it's possible that people can actually skim you by walking past you or whatever, sitting in proximity to you, wherever you are, but they've got to be able to do an authorized transaction.

**Dave Jones:** It's not like they can just steal the details of your card and then go off and uh do a transaction later. They got to do a real-time transaction right there pretty much.

**Dave Jones:** So, you know, yes, in theory it's possible. In practice, the risk is, you know, fairly low and you're limited. In Australia, we're limited to $100 uh per transaction here.

**Dave Jones:** And you're not legally liable for it anyway if somebody skims it. So, not a huge deal. But these things um this armor card in particular um from what they were telling me is selling like hot cakes at JB Hi-Fi.

**Dave Jones:** So, everyone's buying one of these things. And I got like the last one there. Crazy. And I don't know. Anyway, I don't I don't see the point in having an active jammer like this.

**Dave Jones:** It's just it's just a complex solution to a problem that either a has no real risk to it or b has a simple solution in the al foil or a shielding thing.

**Dave Jones:** So yeah, it's neat, but nah, you're wasting your time. I wouldn't I wouldn't buy one. So if you like the video, please give it a big thumbs up and all that sort of jazz.

**Dave Jones:** And uh you can always discuss it down below. Link to the EV blog forum, YouTube comments. Try to read them all. Catch you next time. Hi, just a quick impromptu tear down video of one of these RFID cards.

**Dave Jones:** This one is actually the card to access my uh lab here in the EV blog corporate towers. All right, I'm down in the car park and uh about the only time that uh something like this little DSO quad will actually be uh useful.

**Dave Jones:** I think I'm just going to check the uh frequency of this thing and see what we get. see whether or not it's the one of the 125 kHz uh frequency readers.

**Dave Jones:** Um cuz I don't know. So, let's uh There we go. That's a 125 kHz one. I'm just uh
