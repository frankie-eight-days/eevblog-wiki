---
video_id: zPPB7ZzO_TA
title: EEVblog #456 - CSIRO Rubidium Frequency Standard
url: https://www.youtube.com/watch?v=zPPB7ZzO_TA
source: youtube-asr
timestamps: {"0": 2, "1": 22, "2": 37, "3": 48, "4": 63, "5": 77, "6": 94, "7": 108, "8": 123, "9": 137, "10": 149, "11": 168, "12": 178, "13": 194, "14": 208, "15": 221, "16": 234, "17": 253, "18": 265, "19": 275, "20": 296, "21": 314, "22": 333, "23": 348, "24": 364, "25": 376, "26": 389, "27": 405, "28": 420, "29": 437, "30": 455, "31": 473, "32": 486, "33": 499, "34": 512, "35": 523, "36": 537, "37": 551, "38": 565, "39": 577, "40": 595, "41": 612, "42": 624, "43": 638, "44": 654, "45": 665, "46": 678, "47": 695, "48": 715, "49": 732, "50": 747, "51": 759, "52": 772, "53": 782, "54": 795, "55": 811, "56": 826, "57": 842, "58": 858, "59": 875, "60": 885, "61": 898, "62": 914, "63": 929, "64": 941, "65": 958, "66": 975, "67": 990, "68": 1009, "69": 1023, "70": 1039, "71": 1052, "72": 1072, "73": 1087, "74": 1104, "75": 1121, "76": 1136, "77": 1148, "78": 1167, "79": 1183, "80": 1195, "81": 1210, "82": 1226, "83": 1240, "84": 1251, "85": 1267, "86": 1281, "87": 1294, "88": 1313, "89": 1324, "90": 1338, "91": 1356, "92": 1375, "93": 1392, "94": 1409, "95": 1425, "96": 1439}
---

**Dave Jones:** Hi, this is a follow-up video from my previous one. Having a play around with this rubidium frequency standard I got from the CSIRO. It was there looks like their backup time measurement reference rubidium standard GPS discipline. We've got ourselves a GPS reference oscillator

**Dave Jones:** here. We've got ourselves a rubidium frequency standard, which I think might be a Stanford Research Systems one. We'll find out. And we've got um four IRT distribution amplifiers in here as well as a dual AC main source. And I've

**Dave Jones:** had it powered up for a few tens of minutes and it took maybe five minutes for the rubidium to lock in. The one pulse per second is pulsing, but I haven't got a GPS antenna attached to it. So I'm not sure whether or not that

**Dave Jones:** indicates that it hasn't. I presume it hasn't locked. I mean it is pulsing at once per second, but I don't know. I haven't looked at the details of that one yet. So let's presume it's not um GPS locked at this stage. It's just a

**Dave Jones:** rubidium standard, which is of course more than good enough for the EEVblog lab here. And I've got it hooked up. Well, I will in a second have it hooked up to the Agilent frequency counter I also got. Here it is.

**Dave Jones:** Here we go. And look at that. It is uh This is the 10 MHz out from that rubidium oscillator and it is significantly out. It's 71 Hz out. Now of course this one doesn't have any high order option on the time base. So

**Dave Jones:** it's only got the stock time base in it, which is only rated to about 5 ppm or thereabouts. Not taking into account the drift and that stuff like that. So 5 ppm on 10 MHz is actually going to be 50

**Dave Jones:** Hz here. So I you know so sort of you know as a rough ballpark you sort of would have expected it to be under uh there for this uh stock time base, but it's not at 71. So, um yeah, I you know,

**Dave Jones:** I'm assuming that this rubidium is uh you know, bang on because these things, you know, do not um they they basically they're they're you know, once they lock, they're they're pretty uh pretty reliable. You can pretty much guarantee that you're

**Dave Jones:** getting bang on 10 MHz out. I haven't checked the specs cuz we don't know what unit uh what uh brand rubidium's in there yet, but um so, that's significantly out. So, um assuming that rubidium is spot on, um

**Dave Jones:** this thing is uh probably needs a uh a tweak. But, let me hook it up here to my uh old Philips. Here we go. Old Philips PM 6672. And look at that. There we go. This one actually has an uh ovenized oscillator

**Dave Jones:** in there. It's pretty good. I forget the exact uh spec off the top of my head, but it is uh fully optioned up with the highest um ovenized oscillator in there. And it's basically bang on. So, that um

**Dave Jones:** pretty much confirms that uh the rubidium is uh locked and working. And then if we take that out and we hook it up to which is kind of not really a proper frequency counter, but it's the uh Rigol

**Dave Jones:** uh DG4000 uh series uh function generator. And it's got a counter option here you can enable. It's got a counter on the um input. I don't really like it. It jumps around a a fair bit. So, you can't really, you know,

**Dave Jones:** there's no lower order digits sort of updating there. So, you can't sort of you know, see where it's at. But, pretty much, you know, it is um the figures it's giving are well within that um well, you know, well within say the five

**Dave Jones:** PPM we're getting. Um you know, that's in the order of you know, a couple of PPM there. So, um it's you know, it's pretty good. It looks like this rubidium works fine. So, I'm pretty darn happy with this thing. So, what we'll probably

**Dave Jones:** do now is just unscrew these and take a look at what's inside because there should be a customized backplane in there and these rack modules, these Eurocard style option cards just slide into the customized backplane and we can have a

**Dave Jones:** look at that as well, but I'm really curious to know what rubidium is in there. My guess is a Stanford Research one which I've uh used before, have a bit of experience with those. They're very nice and they're worth quite a bit.

**Dave Jones:** So, let's crack it open. And here we go. We're going to looks like there's a power box power supply in there. It's going to It's got the looks like custom board built in. This would have been a custom

**Dave Jones:** design by somebody at the CSIRO or maybe they farmed it out. I I don't know, but uh we have custom board in there. There's our connector on the back. And tada! Yes. PRS 10. I was bang on. There we go. It is a

**Dave Jones:** Stanford Research Systems model PRS 10 rubidium frequency standard, you know, industry standard module. Probably every man made in the United States of America. USA USA USA. Um serial number 25,000. These things are this rubidium oscillator, I think it

**Dave Jones:** retails for about 1,300 bucks or something like that. These are um a very good units, very low phase noise. I've used them in very critical systems and stuff like that. Very low phase phase noise. So, a phenomenal um uh rubidium standard here for the

**Dave Jones:** lab. I, you know, I probably never get another one of these things. So, I think this one's definitely a keeper and all the distribution amplifiers, wow. Um awesome stuff. So, yeah, that's worth a lot. It's got like a 20-year lamp life,

**Dave Jones:** so there's no date on that one, but yeah, and they get quite warm. That one's been going for, you know, 15 minutes or something. It's heated up to at least 45° or something like that. So, uh let's have a look, see if we can uh

**Dave Jones:** get this board out and uh have a look at the main board, but of course, it's all in here. This is just a going to be a power supply here and just a little uh uh you know, it's just some some

**Dave Jones:** connections and uh stuff like that, really. There's not going to be much at all. Well, actually, there is a fair bit inside this thing because I forgot they do have on the back panel over here from the outputs here. They have direct BNCs

**Dave Jones:** from this module which have 10 MHz in the ref 10 MHz reference output, the 5 MHz reference output, and one pulse per second, and a couple of each. So, they've got to have some dividers on here and uh uh stuff like that. So,

**Dave Jones:** we've got an LT 1259 current feedback amp there, and then just some 74HC series logic and two big power bricks and some filter caps and some bridge rectifiers. That's the AC input. It looks like it can select AC or

**Dave Jones:** DC input. It's got the LED on the front panel over here to say which power source it's actually coming from. So, they're they're really beasts, those Hercules 6 power modules. Very nice. You know, 25 W modules. Brilliant. And there

**Dave Jones:** it is, National Measurements Lab SRS Rubidium version 1 2001. So, this would have been designed and laid out, I guess, by someone at the CSIRO National Measurements Lab, and this would have been designed as their uh custom, you

**Dave Jones:** know, their primary custom standard. And I've done very similar things for labs at companies I've worked out with designed I've designed and built uh custom uh test instruments and reference calibration instruments and stuff like that in almost identical uh racks to

**Dave Jones:** these ones. So, all very very familiar. Couple of bodges. Little bodge there. There's a bodge resistor in there. And there's it looks like we've got a bodge resistor across there. Looks like they put a 75 ohm terminator on the back of

**Dave Jones:** that um Oh, wait. Here we go. Oh. Look out our rubidium. Don't drop our rubidium. Um couple of bodge wires on the back there. Few little shorts, but uh there you go. Um I mean, you know, it all the magic of

**Dave Jones:** course happens in the Stanford Research module. They've got a nice heat sink here. It looks like they've put some uh thermal grease behind there to uh spread the heat onto the chassis of course. This thing's going to get quite

**Dave Jones:** warm during operation, but uh that's that's all there is to it, you know. There's nothing fancy on here. Just some dividers and stuff like that cuz they do build this into Stanford Research. I can't remember the model number, but

**Dave Jones:** they do um I used to have one. Um from my old company they um build this same rubidium standard and they sell a product that has all of, you know, a similar board to this built in. It's got like, you know, 20 BNCs on the

**Dave Jones:** back which has all the 10 MHz, 5 MHz, 1 pulse per second output, all that sort of stuff sort of built into you know, a usable an an actual usable product because if you just buy this Stanford Research

**Dave Jones:** rubidium module, you'd need to add the other stuff around it, you know. You got to add the power supply and stuff like that. In fact, there it it has the pinouts on there. There it is. 10 MHz reference output.

**Dave Jones:** Plus 7 DBM. It's got the lock and the one pulse per per second output. So, I can now look up the manual for that and go, "Aha. What happens if that one's actually you know, flashing?" So, and then

**Dave Jones:** there's a analog frequency adjust. And I'm probably not doing anything with that. Um TXTM monitor one pulse per second in or photo out. Two plus 24 V supply. Blah, blah, blah. There you go. So, beautiful little Stanford research

**Dave Jones:** module there. I love it. Huge score. And now for the GPS card. Tada! That's the great thing about these racks. You can just slide them in and out. Oh, look at that. They've actually uh put Look at that. They got the coax going.

**Dave Jones:** They designed that so that sits right out the back of the case like that. So, you know, that's what you do when all these things are custom designed. But, oh, look at that. Isn't that fancy? I like it.

**Dave Jones:** Very nice. We'll take a good look at that. And if you've never seen inside one of these uh Eurocard racks, and you know, it's it's not much. I mean, there's a uh Oh, no. That's an IRT. Okay, so what they've done, they

**Dave Jones:** haven't custom designed the backplane. That's an IRT brand, same as the uh same as the distribution amps here. So, they've just bought an off-the-shelf IRT uh rack, you know, rack unit, and the backplane's been designed by them, and

**Dave Jones:** it's got holes up in the back of the board that can just poke out the back there. And uh that's it. So, they've just uh you know, designed this standardized around that. So, they've just gone, "Right, we'll use one of these IRT. We

**Dave Jones:** need the IRT amplifiers anyway. They come with the nice uh dual AC power supply and all that sort of stuff. So, we need the distribution amps. So, we'll just buy those off the shelf, buy the whole rack, and then we'll design our uh

**Dave Jones:** rubidium uh standard and our GPS standard to go inside that." So, let's see if the uh I don't Yeah, the NMI looks like they've done this one, too. There you go. It's the Javid 031 NMI National Measurement Institute

**Dave Jones:** 2004 and it is a Topcon, they call it. Euro half or half Euro GPS receiver and it's a JAVAD navigation systems. Of course, you know, NMI wouldn't have designed the GPS receiver in this. They're just designing the backboard here, the Eurocard

**Dave Jones:** backboard to sit here. They've got a riser board going up here to mate into this off-the-shelf one from JAVAD navigation systems. I will uh Look at that package. Look at that. Don't know what's going on there, but got a big metal can down the side. Not

**Dave Jones:** sure what that chip is. We'll have to get the right angle on that and the macro lens, but uh Yeah, just an off-the-shelf uh GPS receiver. No surprises at all, but they have to be specifically designed. I mean, you know,

**Dave Jones:** not all GPS receive receivers are suitable for this. They have to have uh not not only the one pulse per second um output, but, you know, it really has to be like a, you know, low phase noise and

**Dave Jones:** blah blah blah everything else. It's got to be, you know, it's got to be properly designed. If you're, you know, this is obviously the primary reference uh standard for the uh national um institute here and really, you know, they

**Dave Jones:** you know, they're not just going to whack some eBay uh cheapy in here. So, might have made in USA. There we go. So, I might actually uh have a look at that one and see if I can get any data on it.

**Dave Jones:** No, as it turns out, I couldn't really find any info on that. I think it's a really old model. They do make the same ones, these Eurocard um connector interface modules. They still do uh make them, but I think it's a slightly older

**Dave Jones:** one. That metal can, by the way, is a battery under there and the board's actually uh conformally coated. If you can see the uh see the coating on that, perhaps. So, you can tell it's conformally coated. You can see the gloss on say,

**Dave Jones:** you know, the side of the chip down there. You can see a See that glossy coating? They put a clear conformal coating on this board. Maybe it comes standard with that because the uh uh the other board, of course, doesn't have

**Dave Jones:** uh any conformal coating on it, the custom board from the NMI. And by the way, um no surprises. It's uh hand-soldered. Um you know, they would have made uh probably two of these. Uh one is the primary one and one is the backup one,

**Dave Jones:** which I've got here. So, you know, um yeah, someone's uh crusty hand soldering there. They've had a hack job at uh that, which is a little uh little regulator there. Nothing special. It's just a power supply and a 74 uh 244, basically hooked

**Dave Jones:** onto the commercial uh GPS receiver. They've got some uh Dallas Semiconductor stuff down in there, probably a little um ID stuff and a brick power supply, of course. When you're designing a custom uh bit of test gear like this, you don't

**Dave Jones:** bother around doing the power supplies. You're only going to make, as I said, like a couple of these. I've made precisely one of something before, you know, or I've made 10. You're not going to dick around. You're just going

**Dave Jones:** to use an off-the-shelf power module. Yeah, they might cost 50 bucks from Digikey, but whoop-de-do, who cares? You know, I mean, jeez, you know, your your time's easily you know, half an hour of your worth that. So, you just buy

**Dave Jones:** off-the-shelf ones and they work. And uh so, there you go. Just an off-the-shelf GPS receiver. We've got some uh stuff on the back here in terms of uh What is it? Just a power supply stuff, really. Nothing particularly special.

**Dave Jones:** So, there you go. Um I'm going to have to uh actually try this and get uh GPS coverage on the thing. I don't actually have a connector for that. So, it looks like it's yeah, there it is. Right in right angle over there. I don't

**Dave Jones:** have a GPS connected to fit that at the moment, but I will endeavor to uh possibly get some GPS reception for this thing. See if it's still what locks in, but ah you know, I'm not that uh fussy

**Dave Jones:** here in the EV blog lab. I've now got a Stanford Research Rubidium. Beauty. And here's one of these IRT video distribution amplifiers cuz that's essentially what they are. It's a called a VDA. It's the VA VA761 model. They're just video distribution

**Dave Jones:** uh amplifiers. Quite uh good ones, of course, and you can adjust uh the equal gain and equalization of these things because these cuz the 10 MHz reference outputs of these uh Rubidiums, they're just um sine waves. So, effectively, you know, a video

**Dave Jones:** distribution amp is what you want. So, yeah, there's not much on there at all. Just some uh There you go. They went uh they went bust, didn't they? Or they were uh bought out by someone. Atlantic uh 21

**Dave Jones:** 20s and 2054 204 for 2045s, I think. Can't really read that, but uh there you go. It's got a hum adjustment as well. Look at that. Um yeah, just Atlantic video distribution amplifiers. Atlantic were uh very big in the um

**Dave Jones:** uh video uh op amp and uh that sort of video driver market, you know, big uh cable drivers and things like that. I've used those before, so nothing fancy there at all. Shielding plate on the back. Nice touch. I like it. So, I've

**Dave Jones:** got three of those, plus a VA700. It looks like it's got an output monitor and a selection switch. Not exactly sure what they're using that for. And it's another video distribution amplifier. Bit more complicated than the other one.

**Dave Jones:** Got lots of Looks like we've got some discrete trainees on here. Look at this front end. Adjustment pots. Been somebody with a gray beard and right tongue angles tweak those and sealed the pots off there. And we have some

**Dave Jones:** Burr-Brown uh op-amps. Nothing really special. Eh, it's a Euro video distribution amplifier. Woohoo! And on the back here they've gone to the trouble to of course design a custom back plate as well. NMI, there it is. This is for the uh

**Dave Jones:** GPS receiver. Couple of buttons on there. Push. What does that do? FN. No idea. There's another one, power button down here. And uh there is our reference uh Well, that's our one antenna input here. I'm not sure where

**Dave Jones:** these cables are going to then. Not sure what's going on there. Ah, I see what they've done. It's just a uh patch cable. It's basically a just a convert in here. This plugs into there like that and it just converts it to a a

**Dave Jones:** more standardized connector. And I showed these in the previous video. There's the custom NMI um SRS rubidium back plane. One pulse per second output. In fact, they've got two of those. They've got two 5 MHz outputs and they've got two

**Dave Jones:** 2 MHz outputs as well. And they've got a looks like a power supply connector output is unpopulated and a comms port as well just for getting the data out of that rubidium oscillator if they want. So, the whole idea of course is that you

**Dave Jones:** just take your 10, 5, or 1 pulse per second output. You just put them into the inputs here and you got a whole bunch of outputs to power all of your lab gear. And all of Well, in this case

**Dave Jones:** from the National Measurement Institute, all of their uh standards and uh, test gear and frequency counters and scopes and spectrum analyzers and everything else. All uh, GPS disciplined rubidium. And I thought I'd take a quick peek inside this uh, Agilent frequency

**Dave Jones:** counter here. Haven't taken one of these parts before. Look at this. It's a bit how you doing. I mean, you know, look at the just the bare power supply. Sure, it's got the nice, um, you know, insulated flap over the top, but like it just

**Dave Jones:** what? It's just sitting there. I I don't know. I didn't expect that. I was sort of, you know, been mooned again. Like you open it up and blow, there's this ugly, you know, third-party, um, you know, I'm sure it's

**Dave Jones:** a reasonably uh, good quality uh, power supply, but I don't know. It's just uh, anyway, look at the ton of room in this thing. They've got a Xilinx uh, FPGA down there or PLD. Here's the bottom of it.

**Dave Jones:** Quite a bit on the bottom, actually. Um, obviously this uh, these options and they this uh, space in here is for, you know, various options probably for the uh, you know, the high-performance oven oscillator and stuff like that, but

**Dave Jones:** yeah, nice little touch they've put a plastic foot on there just to support the board on the back case when it slides on. This isn't going to be a full tear down. I won't even bother with the close-ups, but yeah, uh, they're It's a

**Dave Jones:** bit disappointed with that. I was hoping to open it up and see if there was a uh, tweaking uh, cap for just the uh, you know, the 5 ppm mark crystal oscillator, but I think it's going to be under there

**Dave Jones:** somewhere. Bugger. No idea what that board from ERG is doing there off the off hand. It's got a uh, little isolation transformer on it. Not sure what the other chip's doing and uh, I don't know. They've gone to a bit of

**Dave Jones:** trouble, too, to mount a third-party board off there. There you go. I just flipped out the power supply. And yeah, manufactured by Delta for HP. It's got a HP part number, as you'd expect. Um dodgy little fan on

**Dave Jones:** the thing. Bloody hell, it's loud. And it goes when you actually don't even have it powered on cuz it's a soft power switch on the front. And you might have heard it in the background going before in some of the at the start of the video

**Dave Jones:** and Yeah, it's hopeless. Unbelievable. Anyway, there we are. Down in there, looks like we have a Motorola processor. We've got some ROMs there. And uh Where's the oscillator? That metal can down the bottom. Oh, I think there's an adjustment pot on the

**Dave Jones:** back. Doh, didn't even see it. See, the thing's turned off, and you can probably hear the fan noise. Listen.

**Dave Jones:** There you go. Pain in the ass. The fan just, you know, stays on. And it's just a soft power button. Crazy. Anyway, let's power it up. It's doing a self-test. Passed GPIB. Yeah, blah blah blah. Now we can plug it in. We can

**Dave Jones:** calibrate it. All right, we'll give it a go. Now, the most important thing with calibration adjustment is the tongue angle. It's got to be correct. And if you're astute, you notice the one-eye pop-eye technique as well. Very important. One eye, tongue at the right

**Dave Jones:** angle. Like that. And a non-magnetic non-metallic screwdriver as well for these I'm assuming it's a cap on the back there. So, what are these? Uh we should be able to tweak it. Ah. Half a bee's dick, I don't know. It's a bit dodgy.

**Dave Jones:** It's hard to do it, but jeez, I'm running down to 30. That's 30 ppm. That's hopeless. Let me try and do it off camera. Tell you what, this ain't this ain't easy.

**Dave Jones:** Ah. Can't talk and have the correct tongue angle at the same time. But gee, there's ah, this part these stock standard oscillators are crap.

**Dave Jones:** That's like as good as I can get it. There we go, four four lousy ppm in that that's Well, sorry, 0.4 ppm. So, yeah, cuz it's 10 MHz. So, that you know, that's okay. But yeah, these stock oscillators are awful. I mean, you know,

**Dave Jones:** I was um I put in you know, that like it's sort of got some springiness to the adjustment in there and then it just there's no sweet spot. I mean, it's just ah, it's just awful. But hey, that's all

**Dave Jones:** right. 0.6 ppm, good enough for Australia. Catch you next time.
