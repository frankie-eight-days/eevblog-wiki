---
video_id: 13jeHBvsoSg
title: EEVblog #265 - Philips PM6672 Timer Counter Teardown
url: https://www.youtube.com/watch?v=13jeHBvsoSg
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 22, "3": 34, "4": 43, "5": 56, "6": 63, "7": 81, "8": 89, "9": 112, "10": 124, "11": 135, "12": 151, "13": 163, "14": 173, "15": 201, "16": 215, "17": 239, "18": 250, "19": 262, "20": 280, "21": 294, "22": 305, "23": 317, "24": 330, "25": 344, "26": 359, "27": 372, "28": 390, "29": 399, "30": 415, "31": 430, "32": 445, "33": 469, "34": 485, "35": 504, "36": 516, "37": 533, "38": 541, "39": 557, "40": 578, "41": 590, "42": 606, "43": 620, "44": 637, "45": 652, "46": 664, "47": 677, "48": 691, "49": 701, "50": 720, "51": 739, "52": 753, "53": 767, "54": 789, "55": 806, "56": 818, "57": 831, "58": 844, "59": 857, "60": 873, "61": 888, "62": 904, "63": 919, "64": 935, "65": 949, "66": 967, "67": 978, "68": 992, "69": 1011, "70": 1028, "71": 1039, "72": 1062, "73": 1077, "74": 1091, "75": 1106, "76": 1117, "77": 1133, "78": 1147, "79": 1164, "80": 1182, "81": 1201, "82": 1232, "83": 1256, "84": 1270, "85": 1288, "86": 1305, "87": 1344, "88": 1366, "89": 1379, "90": 1396, "91": 1416, "92": 1436, "93": 1450, "94": 1461, "95": 1477, "96": 1495, "97": 1511, "98": 1526, "99": 1540, "100": 1552, "101": 1568, "102": 1591, "103": 1603, "104": 1614, "105": 1627, "106": 1639}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Huh? What's Teardown Tuesday I hear you ask? Well, I decided to add a bit of regularity to the blog. So, every Tuesday Sydney time I'm going to do a teardown.

**Dave Jones:** Could be test gear. Could occasionally be anything. I don't know. It's a bit of test gear today. We all love test gear, but it's going to be a regular segment.

**Dave Jones:** Hopefully, I can keep it up. So, every Tuesday from now on you can expect a teardown. What have we got today? Haha, we've got a bit of test gear vintage time.

**Dave Jones:** Uh we have you've seen this briefly before and I promised that I'd do a teardown of it. So, I'm going to do just that. It's the Philips PM 66 72.

**Dave Jones:** Got to get it right. 1 GHz counter timer or frequency counter, but they called these counter timers cuz they're actually capable of counting things as well. It's not just a frequency uh counter.

**Dave Jones:** It's capable of timing and counting and doing all sorts of functions like that. So, you know what we say here on the EVBlog. Don't turn it on. Take it apart.

**Dave Jones:** Let's go. Yeah. And we'll just take a quick look at it. It's a classic eight-digit uh LED red LED display here and it's a timer counter. It's got dual channels A and B.

**Dave Jones:** It's got a C input which is the high frequency one which goes from 70 MHz to 1 GHz. The A and B's go to from DC to 120 MHz.

**Dave Jones:** It's got various uh trigger uh sensitivity uh stuff here and you can pull various things. You've got times 10 attenuators and slope and filters and stuff like that. And it's got uh LEDs here to indicate what range it's on either Hz, kHz, MHz, GHz, or nanoseconds, microseconds, and milliseconds, and seconds for the uh time display.

**Dave Jones:** And it's got your other basic uh controls like your uh measurement time from 10 milliseconds all the way up to 96 uh seconds uh sample time. And if you're frustrated, you can just push it to read it.

**Dave Jones:** And uh we're on the uh count uh capability here. And uh that's just allowing us to uh count up like that. Um otherwise, you can actually count uh the input.

**Dave Jones:** So, if you've you know, you could count switch bounce or you could count anything um that you desire. It's got uh pulse width of the A channel. It's got um a time interval uh average of the A and B time, the period of A of course.

**Dave Jones:** It does RPM. It does frequency. It does the ratio between A and B. And it does the phase between A and B in degrees. It's quite a versatile instrument.

**Dave Jones:** And if you go and have a look at the uh manual for it, and I'll link the manual in there, it really is quite a flexible beast. I like it.

**Dave Jones:** Look at that counting capability. On the back here, we've got a standard IEC uh input power connector. We've got a voltage uh selection switch over here. And we've got uh the um a nice flexible uh capability is that you can um have uh an external frequency uh standard in, or you can actually uh output the internal frequency standard out, the 10 MHz standard, because this thing does have

**Dave Jones:** the included option of the PM uh 9690 high stability oven stabilized 10 MHz reference oscillator. And it's got the gate monitor output here. And external battery uh the battery pack, I believe, uh went inside there.

**Dave Jones:** So, you could power this. It would be completely uh portable. You could get a rechargeable battery option. And no surprises at all inside. It's a classic uh construction you'd expect of an '80s uh era uh frequency counter like this one.

**Dave Jones:** We've got our oven stabilized uh reference oscillator option up there. We've got basically it's all DIP and through-hole. There's none of this surface mount stuff cuz this would have been designed a lot earlier.

**Dave Jones:** It would have been, you know, a follow-on from various previous models and things like that. And an old-school type uh like PCB layout it'd only be double-sided, classic green crinkly solder mask.

**Dave Jones:** I love it. It's beautiful. We've got hand wiring over here and uh we've got it looks like a protection thing over the uh transformer. And if you take a look at the mains input stuff around here, there's a core type uh transformer.

**Dave Jones:** You don't see uh that construction very often these days. Exposed wiring down here on the um IEC connector and the power switch as well. Completely exposed. That's a no-no these days.

**Dave Jones:** You've got some main filter caps. You've got a fuse. It's got a It's warning uh warning you that there's a thermal uh fuse in there as well inside the uh transformer.

**Dave Jones:** And there's a close-up of the strapping uh used to uh hold the core of the transformer in there. And uh haven't seen one of those in uh quite some time.

**Dave Jones:** And my German viewers can get very excited. There it is. Made in Germany. The main filter caps. Brilliant. Haven't seen one of those uh can styles in quite a long time either.

**Dave Jones:** And those can styles are somewhat out of place compared to the newer electrolytics. There you go. They would still would not look out of place today. Now, I'm not sure what this riser daughter board here does.

**Dave Jones:** It's uh but um the clearly the date code 8922, 22nd week '89. It clearly dates It's very similar for the other chips. So, it clearly dates this design to late '89, maybe early '90 build.

**Dave Jones:** And that's a Signetics 10216. And that's a a triple high-speed differential amp. So, what it's actually why they've gone and put that on a daughter board like that, I don't really know.

**Dave Jones:** And there's another familiar chip, the Motorola MC10116P. And it's used in practically most of the frequency counter kits back in the '80s and things like that, probably even extending before that.

**Dave Jones:** I'm not sure when that chip first came around. It's a very similar to the other one. It's a triple differential line receiver. And it's used in the front end.

**Dave Jones:** And here it's used on the on the inputs on the back here. And here's an old Electronics Australia 50 MHz frequency counter kit. And you open it up and you have a look on the input.

**Dave Jones:** And bingo, what do you have? The 10116. It was used in every frequency counter kit I think I ever saw. And there's the processor. It's an 8049, which is based on the MCS48 microcontroller family from Intel.

**Dave Jones:** This is manufactured by NEC in Ireland. Look at that. Excellent. Go the Irish. And this thing had like half a MIPS or a MIPS processing capability. Reasonably good for its time.

**Dave Jones:** And the 8049 I believe actually has 2K of mask ROM built in as well. So, that's why you don't see any memory actually surrounding that. Although this windowed Well, it's not really a window, but this device up in here looks like an EEPROM of sorts, but the number doesn't uh doesn't ring a bell at all.

**Dave Jones:** It's a OQ 0040. So, go figure. It could be some custom masked ROM or something like that, perhaps, because this 8049 processor did have the capability to have an external ROM, as well, I believe.

**Dave Jones:** And we've got some single turn adjustment pots in here for the 5-V rail, measuring time adjust, and a couple of test points. The hold-off time The hold-off time adjust, that's a little test post there, and it looks like there's a missing pot in there, another missing footprint here.

**Dave Jones:** So, maybe I don't know. Maybe there's an an optional upgraded model that has some additional capability, or they just left it out in the design, which is probably more likely.

**Dave Jones:** Some 74LS logic, and look at that, a little test jumper down there. So, I wonder what that does. I'm actually tempted to power the thing up with that test Well, it's got a test It's got the jumper on there, so I'm tempted to power it up without the jumper on there and see what happens.

**Dave Jones:** And I've done just that. One interesting feature, though, is it's actually got a standby LED on here, so it tells you that the power's plugged in, and let's power it on.

**Dave Jones:** I've got that test jumper taken off, and hey, we've got something. If we hit check, does nothing. Reset resets it. Display hold. Ah, look at this. We've got like Yeah, look at that.

**Dave Jones:** We've got It's allows you to adjust It allows you to test the switches. Doesn't allow you to test the rotary stuff, but it certainly No. No. Anyway, it does allow you to test a few things to do with the switches by the looks of it.

**Dave Jones:** So, it's not much functionality there, but I guess, yeah, it's it's certainly doing something. I'm not sure if you can see that, but look at the green solder mask around there.

**Dave Jones:** You can see the sort of like the crinkly nature of it. Very common for this era and this type of board. And some of them actually had very bad solder mask that would actually flake off with time as well.

**Dave Jones:** And looking what presumably is part of the level control circuitry, this device looks pretty important. It's a AMD AM 687. And you realize eh, it's boring as bad It's just a dual comparator.

**Dave Jones:** Reasonably fast one, but a dual comparator nonetheless. And this section here is actually got a a shield around it mounted onto the board. I'm not uh sure how massively effective that thing's going to be, but anyway, there's a couple of single turn adjustment pots in there.

**Dave Jones:** There's a trimmer cap down in there and not much doing in there. And here's the knob. These are the input level control with the pullout switch like that. So, it's a it's a pot with one of these adjustable pullout switches.

**Dave Jones:** Try buying one of those if you had to replace it. Buckley's. And apart from some other miscellaneous circuitry around here, a couple of 4000 series CMOS, couple of other different dual line receivers.

**Dave Jones:** Not terribly exciting. We've got a vertical front panel display board which handles the seven segment LCD. So, that's pretty much all for the top really. It's not terribly exciting.

**Dave Jones:** It looks like we're going to have to take the bottom panel off and have a look. There might be a board underneath. Well, I got to admit that's pretty disappointing.

**Dave Jones:** I expected a a bit more uh circuitry under there, but no. All we got is the uh PCB mount uh push button switches on the front here, and the optional uh 1 GHz uh board.

**Dave Jones:** And it's a dead giveaway because there's the there's the coax in there going through this connector here onto the 1 GHz connector on the front. And that's an optional, like if you uh don't buy the 1 GHz uh option, you wouldn't get the board or the connector.

**Dave Jones:** They just put the blank uh panel in there, but gee. Uh I don't know. Bit disappointed. Expected something a bit more. Some uh jumper uh some jumpers uh down here, something going on there, and uh you set them based on the uh internal battery.

**Dave Jones:** So, all that space uh is probably taken up. The battery is probably that length like that. And that's a 1 GHz uh input can, and you'd expect there to be some circuitry in there, but if you actually have a look in there, there's not.

**Dave Jones:** There's just some uh uh passive components in there and a couple of other through-hole ICs. Terribly boring. And those ICs are the SAB 1009 and the SAB 1046. Your guess is as good as mine.

**Dave Jones:** And you can see that the front panel switch is just one of those uh classic open frame style. Nothing unusual there at all. Now, I'm kind of suspicious of that uh gold capped uh what looked like sort of a mask ROM chip or something cuz there needs to be some other functionality on this board to uh do the timing and counting uh capability.

**Dave Jones:** So, I'm suspecting it might be some sort of uh custom device. That's certainly what the uh numbers on top might uh lead you to believe anyway. So, as it turns out, you can actually download the full uh service manual for this thing, which has um the full schematic.

**Dave Jones:** So, we'll uh go through on it. It tells you all the various things. Here's our oven stabilized oscillator, which we'll take a look at. It's you know, a short-term over the span of 24 hours.

**Dave Jones:** We're talking 1 point less than 1.5 * 10 to the minus nine there, which is pretty good. It's this one here, the 9690. You can even get a better one there with better short-term and long-term stability.

**Dave Jones:** Anyway, um let's go down and see if we can find the schematic. But, there's other good stuff in here. There's all sorts of formulas and things to tell you how it all works.

**Dave Jones:** Very nice. If you I highly recommend even just having a browse of this to figure out how one of these time counters works. It's got not bad stuff in there at all.

**Dave Jones:** Anyway, what we want to do is go down here by girl all the usage. Ta-da! Here we go. We've got our schematic, and we looks like we're going to have to rotate this sucker around, and uh is this the one we want?

**Dave Jones:** This is our double 672. That's the one we got. So, over here is our mains input. There's our IEC mains input, some EMI stuff, the transformer, the voltage selection switch, standard full-wave bridge rectifier with some filtering.

**Dave Jones:** The external battery just goes through a 1N4003 there. And then, this section around here looks for all the world like a switch mode power supply. I think you'll find that a TDA 1060 is a switch mode controller.

**Dave Jones:** So, that and there's a 7905 up there, and some divider resistors there to set the output voltage. And that's it for the power supply section. And if we take a look down here, we've got Aha!

**Dave Jones:** Here's our input. There's channel A. I love these uh hand-drawn schematics. They're They're just great and it looks like it's been photocopied one too many times and and uh roughly scanned and I don't know, faxed a few times and uh yeah, I love it.

**Dave Jones:** Anyway, we've got our BNC input here, channel A, our uh selectable AC uh DC coupling there, our selectable input attenuator with the uh trimmer cap there to trim that out.

**Dave Jones:** And uh looks like we've got some clamping diodes here. Um that looks like That's our what tells you that's the uh 50 kHz uh filter. They either switch that in or you can bypass it by going around there and that goes into the uh AM um uh the the uh fast comparator there.

**Dave Jones:** So, that's pretty much all there is and you'll find that the other the input the other input to the comparator will come from tada, no surprise, your trigger level sensitivity knob.

**Dave Jones:** There it is. So, you set your trigger level and that's pretty much all you uh need to uh sense the input there. So, that's pretty darn easy. And here you go, I think we've found the meat of it.

**Dave Jones:** That looks like the processor, the 8049, and that's hooked into the display system over here. Here's the uh it's the multiplexed um eight-digit display there and it's got There's the driver transistors for it and it's multiplexed in both ways.

**Dave Jones:** So, that's how you can uh drive that uh eight-digit display with only looks like they've got eight lines there. So, really easy to actually drive that and that means you don't need many pins on your micro, but uh-huh, look at what we have here.

**Dave Jones:** Looky looky looky. 0000 Is that four zero? That I think that's what that uh custom chip was and it looks about right based on the uh it was like a 28-pin device, and that goes up to 20 28.

**Dave Jones:** There we go. So, that is a custom device. It is It's got things like decade uh What is that? TBD counter, scan clock, the data clock. So, that is obviously some custom uh LSI device, which uh implements all the um timer counter functions basically.

**Dave Jones:** Uh we've got a divider there, and uh that's Yeah, looks like all the magic happens inside that custom LSI device. I wonder how old that is. It might have been used in uh previous uh models uh maybe, who knows?

**Dave Jones:** And they just carried it over to this model. That wouldn't be surprising. And looky what we have here. We have two 745s, not regular 555s, but they've put in the uh CMOS version.

**Dave Jones:** And uh this one here is the uh measurement uh time. That's the measurement uh gating time uh pot on the front panel. There's the control there. And uh that just uh controls uh the amount of uh time that it uh requires to take a measurement.

**Dave Jones:** And the other one here is the uh hold-off uh time. It looks like the hold-off is not available function is not available in in um other versions. So, there you go.

**Dave Jones:** 555s, they're everywhere. And obviously, here's the 1-GHz uh option board, cuz here's the uh coax uh input over here. It's AC coupled, and those uh passive components around there were the ones that were uh inside the can.

**Dave Jones:** And then we've got our SAB 1009, as we mentioned, and our SAB 1046. And that's obviously some sort of uh prescaler uh circuitry, cuz that's basically all a uh 1-GHz uh option board would be.

**Dave Jones:** It would be a front-end uh prescaler to divide uh the high frequency down to the lower frequency that the regular uh frequency counter circuit is capable of handling. And as for this oven oscillator here, I've got There were two screws on the bottom.

**Dave Jones:** I've undone those and I think it just pops. I think it just pops off. Oop, way. Yes, there we go. Tada! It's just got a .1 in header and that's where the existing crystal goes if you just get the standard option.

**Dave Jones:** That's the standard crystal and it's even got a note saying, "Please remove the crystal when you're installing this oscillator module." And this high stability oven oscillator module 10 MHz it It The option must have cost like a you know almost $1,000 maybe or $500 or $1,000 or something like that.

**Dave Jones:** So, let's crack this thing open and see what's inside. And perhaps no surprise inside, we have some foam, very hard cell stuff. It's certainly not soft and that's what you know keeps this thing uh thermally stable inside or it is going to help a great deal.

**Dave Jones:** So, I think we need to take the screws off the other end now. Now, let's see if we can take this thing out. Look, there's a flat flex cable there going down into the foam sandwich.

**Dave Jones:** So, the crystal's going to be down in the foam sandwich. I'm going to do my best not to uh physically stress this thing. There's a regulator bolted on the on the back.

**Dave Jones:** Oh, that's a Yeah, some sort of regulator. There's the uh 10-turn trim pot there for the fine adjustment. There's a coarse adjustment in here somewhere as well. So, let's take this thing open and there's our coarse adjustment.

**Dave Jones:** There's another board in there presumably. What's that? Ta-da! Oh. Look at that. Magic can. Now, I'm thinking that I would be quite silly to try and take this can apart.

**Dave Jones:** Uh but I should be able to lift it out of there perhaps. Gently. This is rather rather fascinating. Look at that. They've gone to all the trouble to add that flat flex cable on there going down to both ends like that and that'd be like a um an SC you know, or a standard cut crystal inside there and there's obviously a uh a temp sensor there which keeps it all

**Dave Jones:** regulated. There'd be a heater inside there as well cuz these things draw like 10 watts or something like that, you know, 5 watts. They They draw quite a lot of power to keep these to get this thing up to temperature and keep it there and that's why they need the foam to uh um make it immune to outside thermal shocks and things like that.

**Dave Jones:** So, there you go. There's a I guess we could uh try and take that off. I don't know. I want to keep this intact really. I want to keep it functional.

**Dave Jones:** You can see that there appears to be quite some circuitry inside there. So, it's all a rather complicated and convoluted uh construction. It's really really unusual, but uh there you go.

**Dave Jones:** That's the coarse adjustment pot on the top. Uh what the heck? Nothing ventured, nothing gained. I've taken the spring clip off that. And I'm going to see if I can potentially uh lever this top.

**Dave Jones:** Yep. It's gone pop. Ta-da! Bingo. Look at that. We're in. We're in. So, screw the timer counter. This is the most interesting thing we've seen today. And there it is.

**Dave Jones:** You can see the crystal here under this copper shield. And it's a quite a large case. I can't remember the name of that case off hand. It's a very large old style one, and there's some circuitry on there.

**Dave Jones:** Looks like probably a transistor uh something like that. But, the really interesting thing is I see right down the bottom in there. Not sure if you can see it.

**Dave Jones:** There's a ceramic high what looks like a ceramic hybrid PCB underneath the crystal. Wow. I really don't think I'm going to have much luck cracking this thing open any further without uh some major drama.

**Dave Jones:** But, you can see a couple of surface mount devices on the hybrid down there. And another, not sure if you can see it right down in there. But, uh yeah, there's definitely And that looks like for all the world like a ceramic hybrid ceramic board.

**Dave Jones:** So, why would they be using a ceramic hybrid board? Well, my guess is temperature, thermal stability because ceramic hybrid boards are very stable in terms of temperature. So, there's no expansion or anything like that.

**Dave Jones:** So, really that would be my guess as to how they're why they've actually put that hybrid board down in there. But, I don't know. If you've got a better idea, let me know.

**Dave Jones:** Leave it in the comments. And clearly, that's going to be our heater there. And that's our temperature sensor, which is curiously actually on the outside of the case like that rather than the inside.

**Dave Jones:** Go figure. But, that's that's clearly the heater element with the feedback. And that would regulate the temperature inside this can. Well, there you go. I hope you enjoyed that.

**Dave Jones:** I think that was the icing on the cake there with that oven stabilized oscillator. That was excellent because well, quite frankly, the time and counter was boring as batshit as you know, I that's it's pretty much what I expected, really.

**Dave Jones:** Time and counters aren't really that exciting pieces of kit because it's basically just a microprocessor, some input differential amps, comparators, and dividers, and things like that. And well, you know, it just divides it down and and measures it with an against a reference oscillator, some gating and stuff like that.

**Dave Jones:** Not rocket science. So, you can see why these actually probably cost a fair bit cuz each one would have been individually hand assembled, hand tweaked by a guy with a long gray beard.

**Dave Jones:** And he strokes it and gets the tongue angle right. And he trims the the coarse and the fine trim pots. And they and they would have uh soaked it in and measured it and ah you know, characterized the thing.

**Dave Jones:** So, you can see why these are actually cost the money. I like it. So, and if you like the video, give it a thumbs up, please, cuz that really helps with the rankings and things like that.

**Dave Jones:** And if you want to comment on this, jump over to the EVblog forum. And if you like the teardown Tuesday idea, let me know and I'll keep it up.

**Dave Jones:** But, I'll probably keep it up anyway. Want it to be a regular thing. So, catch you next time.
