---
video_id: pUXGQ7zQxkM
title: EEVblog #709 - EDC 4601 AC Voltage Standard Teardown
url: https://www.youtube.com/watch?v=pUXGQ7zQxkM
source: youtube-asr
timestamps: {"0": 1, "1": 9, "2": 25, "3": 45, "4": 55, "5": 77, "6": 86, "7": 101, "8": 132, "9": 147, "10": 158, "11": 175, "12": 185, "13": 200, "14": 213, "15": 236, "16": 248, "17": 257, "18": 271, "19": 284, "20": 303, "21": 315, "22": 325, "23": 341, "24": 354, "25": 361, "26": 373, "27": 386, "28": 401, "29": 415, "30": 435, "31": 455, "32": 468, "33": 479, "34": 494, "35": 504, "36": 516, "37": 529, "38": 544, "39": 554, "40": 567, "41": 580, "42": 591, "43": 603, "44": 621, "45": 637, "46": 658, "47": 675, "48": 694, "49": 704, "50": 726, "51": 733, "52": 753, "53": 777, "54": 790, "55": 808, "56": 820, "57": 832, "58": 840, "59": 853, "60": 864, "61": 871, "62": 884, "63": 895, "64": 905, "65": 917, "66": 930, "67": 948, "68": 957, "69": 970, "70": 983, "71": 998, "72": 1013, "73": 1031, "74": 1043, "75": 1053, "76": 1063, "77": 1074, "78": 1086, "79": 1096, "80": 1109, "81": 1120, "82": 1135, "83": 1149, "84": 1159, "85": 1184, "86": 1198, "87": 1211, "88": 1226, "89": 1237, "90": 1255, "91": 1272, "92": 1286, "93": 1302, "94": 1316, "95": 1326, "96": 1336, "97": 1350, "98": 1358, "99": 1372, "100": 1388, "101": 1403, "102": 1420, "103": 1430, "104": 1444, "105": 1453, "106": 1467, "107": 1481, "108": 1500, "109": 1515, "110": 1537, "111": 1550, "112": 1568, "113": 1583, "114": 1597, "115": 1617, "116": 1632, "117": 1647, "118": 1661, "119": 1677, "120": 1693, "121": 1717, "122": 1728, "123": 1752, "124": 1769, "125": 1798, "126": 1807, "127": 1819, "128": 1845, "129": 1855, "130": 1878, "131": 1890, "132": 1901}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We haven't had an interesting bit of calibration kit for a while, so I thought we'd take a look at this. This is one I scored recently.

**Dave Jones:** We've seen this brand before EDC Electronic Development Corporation from Boston, Massachusetts in the United States of America, who are now owned by Kron Hite and hence KH there in Kron Hite EDC.

**Dave Jones:** And this is the model 4601 AC voltage standard. I'll link in the Kron Hite DC voltage standard that I've done videos on in the past. And what the EEVblog Lab has lacked here, as most labs would, is an AC voltage standard like this.

**Dave Jones:** And they're not that common. There's not actually a lot of these sorts of things on the market. But this is a really nice bit of kit. Look at this.

**Dave Jones:** Six decades here, one ppm resolution. You could dial it in. So you can dial in 1.000000 AC volts. It's not quite that absolute accurate, of course, but the resolution is there.

**Dave Jones:** And you can And the ranges go anywhere from 100 mV up to a full on 1,000 V and it can deliver up to 25 W as well. It's a bit of a beast.

**Dave Jones:** And you can choose your AC frequency as well. 1 kHz, 400 Hz, 60 Hz, or 50 Hz test frequency a built-in. Or you can supply your own external frequency here if you have an oddball requirement.

**Dave Jones:** So let's take a look at it. And this one was last NIST traceably calibrated back in 2000. So it's 2015 now. So it was 15 years ago. But this is It looks like an I, you know, like a really vintage model, but this is actually I believe was first released in 1998 according to the manual which in scheme of things, you know, isn't that long ago and the manual was up last updated in

**Dave Jones:** 2001, but Chron EDC they still made standards like this and I think they probably still make them today. Really old school looking and like any good reference standard of course it must have the sense lines here and by the way, I have to be extremely careful.

**Dave Jones:** This could be potentially be a very dangerous instrument cuz it is capable of a thousand volts as I said up to I think it's a maximum of 25 watts even at a thousand volts.

**Dave Jones:** We'll take a look at the graph for that in a minute, but yeah, we've got the shunts in there to just connect across the load. Of course the four terminal current sense very important if you are driving any significant load, then of course you have to account for the drop in your cables here.

**Dave Jones:** Now, I know we're violating our don't turn on take it apart rule, but I just wanted to show because people will want to see just its spot accuracy check.

**Dave Jones:** So, I've had it going for I don't know 20 minutes or so it's taken 18,000 samples. As you can see here, I've got it producing one volt precisely dialed in at one kilohertz and this is what I'm getting.

**Dave Jones:** Don't worry about that. What we what we need to do is have a look at the average here. Look at this 1.0 00079. Whack that into your calculator and it's point double O seven percent high.

**Dave Jones:** Woohoo! Well within spec. And by the way, that is just continuing to track down as well. So, I'm not sure what it's eventually going to go to, you know, like a really actually tracking these things and can take you know, weeks to actually track and verify the performance of this thing And um I have to offhand, I'm not sure of the AC voltage spec of the uh

**Dave Jones:** Agilent 34461A, but it's one of the best uh meters I've got here in the lab. So, we're going to assume that it's bang on. And if we turn on the uh trend chart here, you can just see it uh tracking like that.

**Dave Jones:** I don't know why it just uh suddenly shot up there. I'm not sure what's uh going on there, but we can see a few wiggles in there. It's a really quite interesting.

**Dave Jones:** And if you got into the uh uh uh you know, the thermals of this thing and uh everything else, maybe if I like blow into it or something, we might see some uh Hang on.

**Dave Jones:** I've no idea. Haven't done this. Probably not, but you never know. Never know your luck until you try it. Oh, look at that. Big excursions there. Let's try that again.

**Dave Jones:** I have no idea where the reference in this thing is. Haven't taken it apart yet, but Oh, those big excursions aren't an accident, I don't think. Uh this makes for great video.

**Dave Jones:** And of course, this looks like huge variations here, but if you actually have a look at the scale here and actually calculate as a percentage um what's happening there, it's still well within spec.

**Dave Jones:** It's just that uh this Agilent uh bench meter there, a 6 and 1/2 digit bench meter, is capable of quite high resolution here. So, you get to see all the little wiggles.

**Dave Jones:** I love it. And what's really interesting with this is that it gives you an indication here whether or not it's um actually set, i.e., it's locked and presumably, you know, going to be within tolerance whether or not, you know, it's high or low outside of the boundary, it's going to give you a red LED there.

**Dave Jones:** You might uh actually um show up if we uh change the frequency or the range here. And it's um it rather interestingly got um electronic buttons here for the standby and operate mode.

**Dave Jones:** So, you can whack it in a standby mode, but you can just do that just by changing the range like that. There we go. It's gone into standby mode.

**Dave Jones:** It's still in set. So, I have uh yeah, there we go. It just went to low, so it it's going to take some time to Oh, yep, you see it just uh it sort of like overshot to high and then came back within uh tolerance there.

**Dave Jones:** So, by the way, yeah, this thing appears to be fully working. The guy I bought it from he has uh verified it against much better gear than what I've got here and uh says everything is within uh tolerance.

**Dave Jones:** So, it's pretty sweet. Let's actually um turn this sucker up to a 1,000 V and uh see what we can do. Actually, we better not take it to 1,000 because my Agilent meter here is actually um if you have a look at the input, it says uh 750 V AC maximum.

**Dave Jones:** So, I've got it set to 700 there and we can uh reset the uh trend on that to get the average. Now, I've had it there for a couple of minutes and it looks like it's a little bit out, but if you think about it, this is 700 V AC.

**Dave Jones:** What's 0.05% uh spec of that? Well, it's 0.35 V. So, actually, it's well within the 0.05% full scale spec of this thing. And just down at uh 70 V AC here, just uh left it there, but dropped a point by a decade, yeah, we're within uh 0.01%.

**Dave Jones:** Once again, well within the 0.05% nominal spec of this. I'm not sure if you can hear this, but uh there's no uh audible noise on it at uh the lower frequencies, but you whack it up to the 100 kHz, and you start hearing some hum there.

**Dave Jones:** Let me uh turn up the mic level. Never trust an instrument that doesn't hum. And down to 100 mV it's kicking some serious ass, too. Look at that. And I just love this.

**Dave Jones:** The lightweight of the unit makes it a desirable laboratory instrument. Yeah, all 18 bloody kilos of it. There you go. It looks like the 100 mV range here is attained by a divider network.

**Dave Jones:** So, really it's like a 1 V uh minimum range. And here we go. We've got the basic specs here for a 23° nominal plus minus 5. So, it looks like it's um specked over that, not including uh drift and noise, of course.

**Dave Jones:** So, on the 1,000 V down to 10 V ranges, as I said, 0.05%. In fact, it's 0.05% of both of them. The only difference is the uh range there, of course.

**Dave Jones:** You got a decade worse uh range figure on the 1 V and 100 mV ranges. And as far as the stability goes, look at this. Very impressive. 8 hours of uh course, you'd expect it to be pretty good.

**Dave Jones:** 0.0075% of setting plus almost, you know, a bugger all half a bee's dick of the range. But uh the 6-month stability So, if you left it on for 6 months, how much would you expect it to drift by maximum?

**Dave Jones:** Well, 0.015% of the setting plus, uh you know, I don't know, 3/4 of a bee's dick of the range. And also, load regulation, very impressive. 0.005%. And of course, it can go up to uh 25 W delivery on this thing.

**Dave Jones:** So, um of course, you got to use the uh four terminal sense to actually get that. And if you care about the frequency stability and uh accuracy, there you go.

**Dave Jones:** It's pretty good. But uh most people don't care about that unless you have a uh precise need for an exact uh frequency. And recommended calibration cycle, 12 months. This poor puppy hasn't been touched in 15 years, but it's still bang on.

**Dave Jones:** 18 bloody kilos, 50 lb for you Yanks. We've got bugger all on the back here. Looks like it does have some sort of options, maybe for some sort of uh you know, a couple of uh banana plug terminals or something like that.

**Dave Jones:** Couple of cutouts here which has then got plastic inserts in them. We've got the line fuse and yes, it is selectable between 230 V and 110 V operation as well.

**Dave Jones:** Handy if you're buying these internationally. So yeah, just flick the switch and Bob's your uncle. There you go. Maximum of 25 W here only at 100% of the range of course it loses some of that.

**Dave Jones:** And for the 1000 V range there's just start three different graphs here, the 100 to 300 and 300 to 1200 W but even at the full 1000 V output can still deliver 25 W and give you 0.05% accuracy and 0.0075% stability on that.

**Dave Jones:** Awesome. All right, let's have a squeeze inside this puppy. There is a screw missing on the back here so I'm not sure what the deal is there. There are no calibration seals on the thing so let's lift up the skirt.

**Dave Jones:** Slides off. Oops. Move the camera and tada! We're in like Flynn. Look at that. Monster transformer. Wow. Two huge caps, bunch of our precision resistors and switches on the front and some old school through hole stuff.

**Dave Jones:** Now first of all, take a squeeze at the decade switches down here and as you can imagine they're very very nice. They look a bit crusty because well, they're old but you know, you can these things pretty much self clean very nicely.

**Dave Jones:** Although if you do have to on the rare occasions you do have to uh clean them, E.D.C. Chronohight have some recommendations for that. You don't use a silicon based lubricant or oil so you've got to use it like a DeoxIT brand switch cleaner or something like that.

**Dave Jones:** So, yeah, you really need the proper stuff. And just like on my previous DC voltage standard, we find a trimmer board like this on the high range switch. So, that's the first decade.

**Dave Jones:** So, that's to bring the thing into calibration. Don't want to touch those. And you'll notice that they're the only adjustments. All the other ranges here, they've just got those fixed precision resistors on them and they just decrease in value as you go along right down there and they're going to be, I don't know, an ohm each or something like that.

**Dave Jones:** And as far as the rest of it goes in here, and we haven't seen it all, by the way, there is some more on the bottom, which we'll check out shortly, but very classic EDC Chronite type.

**Dave Jones:** Very old school construction. We've got ourselves a just a very old school tin plate PCB in there. Yes, it is FR4. It's not like phenolic base or anything, but um yeah, it's all through hole parts.

**Dave Jones:** They're all socketed and very very like reminiscent of like this thing was designed and built in the '70s or '80s or something like that, but get in there and look at some of the chips in a second, but it seems to be like a weird combination like they had the boards left over from a previous design back in the '80s or something and they just rehashed them and just whacked in some

**Dave Jones:** new chips and sold these things cuz they don't sell these in high quantities. I mean, they might even make them to order pretty much. So, maybe they've got like tons of old stock, you know, hanging around and things like that of various parts and chassis and whatnot.

**Dave Jones:** And uh yeah, they just put one together, hand sort of like hand build each particular one. Anyway, over here, we've got our mains input transformer. Pretty much this wouldn't pass modern uh standards and things like that.

**Dave Jones:** There's no insulation on any of the uh mains input over here. Woah, I got some heat shrink over there on the uh on that crusty um 240 V the voltage mains voltage selection switch up the back.

**Dave Jones:** That's a bit how you doing. And the uh fuse on the back and well, yeah, anyway, this is the big ass uh primary uh transformer. It's only just got a sent a single center tapped um output here and that's it.

**Dave Jones:** This other big beast over here, this is why it weighs so much with the combination of two of these. This is the big output transformer with the multiple uh taps on there.

**Dave Jones:** We've got some uh heat sinks up here with some uh either bipolar transistors or FETs. They're probably bipolar transistors. None of this field modern field effect rubbish. And then we've got some uh big reservoir caps here.

**Dave Jones:** We'll uh see those on the bottom there. They just um uh filtering the uh the main output uh supply here. That's it. You'd have one for the positive and the negative for your split rail.

**Dave Jones:** And then, curiously, we've got a plug-in board here. We'll take a look at it. It's uh the going to be the oscillator board and a couple of relays on there for switching.

**Dave Jones:** And if we take the bottom cover off here, this is uh rather interesting as well. Here we go. The caps uh protrude down through the bottom here. We've got ourselves some uh bleeder resistors across there so they discharge those caps.

**Dave Jones:** These are 70 V uh rated Nippon Chemicons. Might show you that in a minute. Uh we've got our bridge rectifier here mounted down to the chassis down there. So, we're just getting the uh split supply.

**Dave Jones:** The wiring uh comes through, I believe, there and uh goes into the bridge rectifier. So, it's just a classic um arrangement. It looks like the chassis is punched for something else.

**Dave Jones:** I mean, look at these holes here and here and they've got a cutout here for these two terminals, but I think they maybe put them there. This It doesn't look like this chassis was designed for this particular model.

**Dave Jones:** So, they've probably reused it. Although, it does have the uh cutouts for the dual transformers, but there's lots of unused holes and things around here. Anyway, they've got a bit of folded metal here, so they've got pin at the wiring penetrating.

**Dave Jones:** This is looks like an output relay down here, which switches the output. We've got some shielded cable going back up there, so we'd have the output line Well, the the sense line going back to another relay that's protruding through the board in there.

**Dave Jones:** I'll show you a close up of that. Now, check out that. They've got this relay sort of just like It's almost like this cut out in the board is like hand cut.

**Dave Jones:** It doesn't look like it's routed out. So, it's a very much how you doing, and it's what it makes me think that they just, you know, manufacture some old boards that they've got around and hack these things together.

**Dave Jones:** I don't know, but jeez, it's it's not pretty, is it? Oh, sorry, I was a bit wrong on that mains input transformer on the front. That actually has a couple of more supplies as well.

**Dave Jones:** The main supply here comes out, but as I said, it's just a split supply there, and you'll notice that the center tap for that, look, going all the way up here through this penetrator and over to this star point over here.

**Dave Jones:** So, they've got another wire running off there, which then connects this base down here, which then grounds a whole bunch of other stuff if you follow it around, and then they've got like another wire going up there from that ground point.

**Dave Jones:** So, they're, you know, tying a lot of stuff back to that central star point there. That'll be for the power, cuz this is all the power supply side of things, but of course, you would have different star point arrangements if you want to take a look around here for the various for the voltage reference stuff.

**Dave Jones:** And there's a hack down in there. Look at that. Goodness. That's the uh flyback diode on the uh relay there. So, there's the screw holding in the relay and that's just Oh, man.

**Dave Jones:** They use sockets for all the other ICs. Why couldn't they include a socket for the relay? I don't know. And over here, we clearly got a high voltage uh resistor arrangement.

**Dave Jones:** This is coming from this shielded cable, which as I said goes down to the uh it looks like an output relay down here. So, this is probably the uh sense terminal.

**Dave Jones:** And of course, when you're sensing a 1,000 V output, well, you don't want to tap off um directly a 1,000 V. You can't feed that into your, you know, your op-amp uh feedback or whatever.

**Dave Jones:** So, you've got this uh we'll see the resistors on the top side, but it's basically a high-voltage resistor divider here. And it looks like this cable pair comes from the uh switch on the front that selects your uh test frequency.

**Dave Jones:** You can see that going up to uh these various traces here going up to this uh vertical board, which is our oscillator board. So, that selects your oscillator frequency.

**Dave Jones:** And there's more hackery going on in here. Look, they've got this jumper going across there. And there's our um chassis uh reference point. They've actually tied that in there going over to there.

**Dave Jones:** Wow, this thing is like, you know, all hand-built and hacked together. And there's the mains input I was telling you about. And it all looks really quite crusty. Have a look at the board down in here.

**Dave Jones:** It's got all sorts of weird It's got like weird deposit on it. Yeah, look at that. Um so, I don't know where all that's uh all that sort of It's almost like soot or something has come from.

**Dave Jones:** Um really quite strange. So, that seems to all be in this part, which is the uh power supply, of course. That's the plat power supply section. And uh then, this is where all the magic happens over on this side.

**Dave Jones:** And as we saw in our previous uh DC voltage standard, all the magic happens in the hand selected by somebody with a gray beard and the tongue at the right angle, uh Zener voltage reference.

**Dave Jones:** So, they age these things and they've got special uh Zeners which are super super stable and they've obviously hand selected it at a particular uh current there and they've measured it 6.1 uh 517 V and then the whole thing is tweaked and uh calibrated and uh yeah, you don't touch it from that point cuz these uh Zeners are specifically uh aged and tested been to be extremely low drift.

**Dave Jones:** And that's what you need in a precision reference like this, whether it's AC or DC, it doesn't matter. Uh the the uh Zener diode itself could be like plus minus 5% absolute tolerance, doesn't matter.

**Dave Jones:** It's all about the drift because you can just uh calibrate that out later. As long as it doesn't drift, you can tweak the pots to your heart's content, do whatever the other pots we saw on the front panel.

**Dave Jones:** And once the thing is tweaked to a specific calibration, then uh it's all about the drift. So, if we have a look in here, we've got some Oppo 7s, OP177, yep, and uh OP 17.

**Dave Jones:** So, we've got some precision op amps as you'd expect and uh some date codes on there of uh 1993. If you have a look over here, look, we've got a CD uh 4013 4000 series CMOS.

**Dave Jones:** It's got a date code of the 18th week 99. So, and what's uh all the chips on here seem to have quite, you know, widely varying date codes. So, it makes me think, yeah, they've just had, you know, old stock of parts or whatever lying around cuz as I said, the manual says this is a 1998 model.

**Dave Jones:** So, that 99 there uh does make sense. So, you know, unless they've changed it, unless this has been replaced uh post manufacture, then um yeah, this date then that dates this to uh you know past 19 um 99.

**Dave Jones:** So, you know, into the 2000s. But what of other chips on there? 93 vintage. Anyway, we've got ourselves a ULN uh 2004. Uh they'd be using that to drive the relays.

**Dave Jones:** We've got a uh old school uh TL074 up here. It wouldn't be doing anything uh critical at all. It'd just be doing some miscellaneous um stuff. We've got some trim pots around this uh TL07 uh 071, is it?

**Dave Jones:** Um yeah, just, you know, once again, that's not a precision uh op amp. That's just a uh uh JFET job. And there's our high voltage resistor network here. So, it's coming there and they just uh tap it off at the point.

**Dave Jones:** So, they've got like, you know, a 100:1 division ratio or something like that. But they stagger them just to get a uh voltage rating on each one. So, that you know, they're just gilding the lily there.

**Dave Jones:** Good engineering practice than just rely on a one resistor. Why not have a bunch of them in series? Now, over around the voltage reference around uh presumably around here somewhere.

**Dave Jones:** I don't know which one is the precision uh Zener reference. Um yeah, I probably one of those, I'd be guessing. I don't know. I unfortunately do not have the uh schematic for this puppy, so I can't see.

**Dave Jones:** If I do uh get it, then I'll uh oh, eventually get it. I'll I'll definitely ask um Chronos to see if they can uh still get it for us.

**Dave Jones:** But at this stage, nah, we're just pissing in the wind. We've got ourselves a little uh probably a coaxial uh Coto relay down in there. You can see that's three terminals on one side, one on the other.

**Dave Jones:** So, the center is actually the uh relay contacts with the two outer ones being the uh coil contacts. So, that'd be like a um you know, a a really uh low thermal EMF relay just for you know, precision applications like this.

**Dave Jones:** The only really super modern part in here is this precision metal film package down in there. There you go, that's a 0.01% 10K resistor precision resistor that you get from Vishay by the looks of it.

**Dave Jones:** We've also got this very interesting part here and well, we'll find out what that is. It's more obvious when we get over to the main oscillator board, but that is what's called a vactrol.

**Dave Jones:** Go Google that one. What do you know, that does look like a MOSFET. I believe that's a 2SJ162 P channel job. And please excuse the crudity of the light source here.

**Dave Jones:** This is a 2SK1058 matching N channel MOSFET. And of course, that's where we're dissipating all the power in these two MOSFETs here and they fuse those. A nice little touch there.

**Dave Jones:** Got a separate board for that and you know, why they didn't integrate that with the main board? You know, who knows? There's not much on it. There's a couple of links, two resistors and two fuses.

**Dave Jones:** Geez. And the cap on here seems like a bit of an afterthought perhaps. Hmm. Hey Bruce, this thing's not quite stable under maximum load on this range. How do we fix it?

**Dave Jones:** Ah, just whack a cap on there. She'll be right. Ah, check out that spared no expense on the mains power switch. Oh goodness. And over on the oscillator board, here's what I told you about before.

**Dave Jones:** This is a vactrol and you're probably wondering what the hell is that? Well, it is a photo resistive opto isolator, like a photo resistive optocoupler. It's like an old school 1960s optocoupler um trademarked the Vectrol name is trademarked by Vactec.

**Dave Jones:** I don't know if they still exist or not. So, unlike a regular opto coupler which has a photo transistor on one side, this has a LED on one side and a photo cell like a CDS photo cell on the other side.

**Dave Jones:** So, there you go. So, that allows isolation and used in oscillator stable oscillators and things like that, you know, very sort of, you know, HP 200 old school using a light bulb as the you know, as the main as the main stability element in your oscillator.

**Dave Jones:** Oh, man. You know, we're talking 1960's here. So, you know, this EDC Chronos stuff goes back a long way and they don't change their designs. They just, you know, keep Yeah, they might have a few little modern refinements, but jeez, to use Vectrols?

**Dave Jones:** Unbelievable. Anyway, if you're curious to take a look at this, I'll actually link in the data sheet to this puppy down below. Check it out. And here's the oscillator board in stark contrast to the board that we, you know, the homemade hack that we saw before.

**Dave Jones:** I mean, you know, it's fairly modern compared to that. Solder mask, silk screened, all the works, you know? So, really is, you know, amazing sort of difference. Anyway, look, an interesting element down in here.

**Dave Jones:** One of these old XR brand 2228's. Now, that's a multiplier detector normally used in PLL's, of course. So, that's what they've got going on here. So, they've got a detector and they've got a that's Vectrol up there.

**Dave Jones:** And anyway, so, this is the programmable oscillator. It looks like they've got some diode gating down in here perhaps 4016's really all just, you know, discrete old school stuff in here, but a fairly modern Look at that NAIS relay.

**Dave Jones:** And the most recent chip on this board 96 Well, 1996 24th week. So, it's just Oh, it's so rather interesting. Oh, there's another one of those Coto coaxial relays in there as well.

**Dave Jones:** I don't know why they're using those for, you know, such low frequency stuff anyway. It's pretty schmick, but Oh, what's that Epson part? Oh, and that, folks, is an Epson crystal oscillator.

**Dave Jones:** Where's our Where's our crystal? I don't see it. Oh, look. We've got ourselves a JFET over here by the looks of it. Um but where's our crystal? It's a crystal oscillator.

**Dave Jones:** Another FET over here. But jeez, what's going on there? Really is quite interesting. All this diode, which is probably like diode like gating, is actually goes into this Epson chip here.

**Dave Jones:** Fascinating. And of course, it's obvious when you take a look at the data sheet, which I will link in down below. It's got a built-in oscillator and it's got a digital programmable divider in there to select multiple frequencies.

**Dave Jones:** Hence, all the diode gating and stuff like that. It's just selecting the different frequencies. So, that is our main frequency element in there. So, yeah, I'd really love to get a schematic and theory of operation of how they're doing this whole thing, not just the oscillator side of things and the detector over here, but you know, just just the whole kitten caboodle for this thing.

**Dave Jones:** And over in this power supply section here, you can see all that sort of whatever it is down there. Check out that puppy. It's an LM3914 {dot} bar display driver.

**Dave Jones:** What the hell are they using that for? Um the only thing I can think of off hand is that they're using that for the output here, which uh the uh low end um set outputs because it's got built-in comparators and you can get um you can get the LED outputs uh based on, you know, is it in the center or not?

**Dave Jones:** So, that's my guess is that driving something uh it must be driving that. I guess if you follow the wire in there, you'll probably find out. And sure enough, I did follow the wire in which uh takes off from these pins here down on the bottom of the board and then pops up up over here and there we go.

**Dave Jones:** It goes to our LEDs on the front panel there. So, it seems like they're just uh you know, creating some sort of uh DC offset voltage, which uh then gets compared with uh you know, some set uh thresholds on this uh crusty LM3914 um {dot} bar display driver using it in dot mode obviously um in this case and uh whether detect whether or not it's uh within thresholds.

**Dave Jones:** I just assumed that would have been done with, you know, some comparators or something like that, but uh whatever floats your boat. It's going to work. So, there you go.

**Dave Jones:** I think I spent enough time on this thing. I hope you enjoyed that look inside this uh EDC Chronoheight uh 4601 AC voltage standard, something that uh your average lab doesn't have.

**Dave Jones:** And this is um almost a metrology grade uh instrument. And it's amazing how they can get the performance out of this thing with, as you saw, the dodgy uh you know, sort of like do-it-yourself homemade uh construction in there, but hey, you know, there's it doesn't have nothing has to look fancy or be uh you know, what we would consider, you know, ultra professional construction to actually

**Dave Jones:** work and have the performance of this thing. It's all about, you know, the little minor things about this star point grounding and you're choosing the right components for the drift and, you know, testing it and everything else and calibrating it.

**Dave Jones:** And well, yeah, it doesn't look the business from inside, but well, you know, things like the rain switches and all that are, you know, very quite nice and all your precision resistors low drift film resistors on there and you know, stuff like that is all nice, but all the other analogy type stuff in there is it really is quite how you doing, but it does the job

**Dave Jones:** and it meets the spec and this is a pretty kick-ass instrument even today. There's not too many AC voltage standards on the market. So, that's really quite fascinating. If I can shame we don't have the schematic for it.

**Dave Jones:** If I can get it, I will eventually link it in or if anyone has it, please leave it in the comments. And as always, there will be some high-res tear down photos of this thing on eevblog.com.

**Dave Jones:** The link is down below and the eevblog forum link is there to be had. So, hope you enjoyed it. Catch you next time.
