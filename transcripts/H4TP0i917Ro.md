---
video_id: H4TP0i917Ro
title: EEVblog #137 - BK Precision 879B Handheld LCR Meter Review
url: https://www.youtube.com/watch?v=H4TP0i917Ro
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 34, "3": 49, "4": 64, "5": 77, "6": 92, "7": 105, "8": 123, "9": 139, "10": 153, "11": 166, "12": 180, "13": 198, "14": 211, "15": 225, "16": 240, "17": 252, "18": 264, "19": 278, "20": 292, "21": 304, "22": 318, "23": 335, "24": 351, "25": 369, "26": 380, "27": 395, "28": 410, "29": 422, "30": 436, "31": 452, "32": 465, "33": 484, "34": 501, "35": 515, "36": 528, "37": 541, "38": 557, "39": 572, "40": 585, "41": 600, "42": 616, "43": 630, "44": 646, "45": 658, "46": 671, "47": 683, "48": 696, "49": 709, "50": 723, "51": 735, "52": 749, "53": 764, "54": 778, "55": 790, "56": 806, "57": 819, "58": 834, "59": 846, "60": 858, "61": 875, "62": 892, "63": 905, "64": 918, "65": 936, "66": 945, "67": 957, "68": 968, "69": 982, "70": 997, "71": 1010, "72": 1025, "73": 1044, "74": 1063, "75": 1083, "76": 1107, "77": 1122, "78": 1135, "79": 1148, "80": 1161, "81": 1172, "82": 1184, "83": 1196, "84": 1212, "85": 1236, "86": 1254, "87": 1265, "88": 1279, "89": 1292, "90": 1310, "91": 1329, "92": 1345, "93": 1358, "94": 1373, "95": 1389, "96": 1406, "97": 1421, "98": 1434, "99": 1450, "100": 1464, "101": 1477, "102": 1500, "103": 1519, "104": 1538, "105": 1552, "106": 1571, "107": 1589, "108": 1607, "109": 1624, "110": 1637, "111": 1652, "112": 1667, "113": 1683, "114": 1701, "115": 1717, "116": 1731, "117": 1746, "118": 1763, "119": 1777, "120": 1793, "121": 1806, "122": 1822, "123": 1835, "124": 1848, "125": 1860, "126": 1875, "127": 1888, "128": 1903, "129": 1918, "130": 1932, "131": 1944, "132": 1966, "133": 1978, "134": 1990, "135": 2004, "136": 2017, "137": 2030, "138": 2047, "139": 2063, "140": 2079, "141": 2090}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product review time and we've got another LCR meter. This one is the BK Precision 879B,

**Dave Jones:** brand spanking new model. Let's check it out. And here it is. Now, you may notice the similarity between this BK Precision 879B and many other LCR meters on the market. Now, that's not a coincidence, it's because their original heritage is

**Dave Jones:** from company called Escort. Uh, now they design and manufacture a lot of test instruments which were re-badged not only under the Escort brand, but were re-badged under many different names including BK Precision and Agilent as well as many other uh smaller names.

**Dave Jones:** So, there's no uh mistaking this looks pretty much identical to the Agilent uh unit and quite a few others you can buy out there, but uh Agilent actually bought out Escort a couple of years ago. So, what that meant

**Dave Jones:** was that while the um the other manufacturers could still sell this meter, they still had rights to sell it. Um, BK Precision decided that no, we'll go design our own and redo it from scratch. So, although it still looks

**Dave Jones:** similar, this is a completely new design inside. And of course LCR meters aren't that exciting. What we really care about is what's inside. So, you know what we say here at the EEVblog, don't turn it on, take it apart.

**Dave Jones:** And to get the unit open, there are two screws up the top here. Somewhat disappointingly, they aren't uh metal threaded inserts, they're just self-tappers, but there's uh one extra screw under here for the metal, but this is a threaded metal insert for the

**Dave Jones:** battery compartment. So, let's lift it off and take a look. Ta-da! Here it is. And it's actually very, very nice. Let's check it out. Let's take a general look around the unit. There's two main devices up here which we'll take a look at. Uh there's

**Dave Jones:** some very interesting looking headers over here presumably for in-circuit programming which we'll check out. You've got three input terminals down here. One's a guard terminal, one's positive and negative. You've got the 9-V battery terminals straight on here like this. I love those. Um and so

**Dave Jones:** there's no wiring at all in this unit. It's just a single-board construction. Now, they've got the USB connector down the bottom here. Now, that USB connector has got to connect to these devices up the top. So, why it's right down there,

**Dave Jones:** a high-speed USB serial interface right down in the bottom corner near the terminal. In this case, it's the positive terminal over there. Why they put it down there instead of up here somewhere right next to the devices is

**Dave Jones:** beyond me. Um that just seems like a crazy layout decision. I'm not sure what they were thinking there, but anyway, the only adjustment in the whole thing is a uh nice 10- or 20-turn uh pot down here as you can see.

**Dave Jones:** And it looks like that's the only adjustment at all. There's a few a few missing components down around here. Here's the 12-V input jack. This is obviously the um the DC-to-DC converter input uh circuitry there for the external power supply. Um and these Take

**Dave Jones:** a look at these diodes down here. They're actually the incorrect footprint. So, they've designed it for a bigger um a bigger footprint like these, but they've decided just to use these uh MELF packages. And we have a large spring terminal here

**Dave Jones:** which goes up to the shielding on the back of the case. So, the shielding sort of wraps around the sides. It looks very nice. No problems there at all. Now, the input circuitry here, there is actually a fuse. I There was I was expecting like

**Dave Jones:** a glass fuse like most other LCR meters has, but there it is. There's um F200 down there. So, that's actually some sort of um some sort of poly switch or something like that. So, it does indicate on the display if

**Dave Jones:** the fuse is blown, but that's obviously not easy to change. If if you do overload the inputs and you blow the fuse, well, you may not be able to replace that. So, I'm not sure if it is a poly switch though, it'll be a

**Dave Jones:** self-resetting poly switch, so that would be good. But, if it's just one of those surface mount fuses, then that's not so good cuz that's suckers not going to be easy to change at all unless you got the gear to do it. And if we look at

**Dave Jones:** some of the other circuitry here, there's you can't read those numbers, but there's lots of discrete op-amps, lots of 4000 series analog CMOS stuff as is very typical with these class of LCR meters. They use a lot of They actually

**Dave Jones:** require quite a fair bit of discrete circuitry and I like it. It's really quite a neat layout. It's no problems whatsoever. I don't see any bodgy components at all. It really looks quite nice. Now, I got one of the first meters

**Dave Jones:** which rolled off the new production line for this model and as you can see it's already up to version 2.2 copyright 2010. So, they've gone through quite a few revisions before they actually got the product out the door, which is a

**Dave Jones:** sign that they've actually refined this thing and it works really well. Now, these are the two main devices up here and it's got two crystals. Looks like a 32 kHz watch crystal down here and a standard crystal up here which is

**Dave Jones:** 6.4 MHz, I think. Yeah, 6.4 MHz and these two devices, interestingly, I didn't expect to see an Altera MAX II device and check it out. There it If you can read the number on there. So, and this looks

**Dave Jones:** like a standard Altera JTAG header. So, what I did is I hooked this up to my to a JTAG programming interface in Altium Designer and bingo, there it is. It popped up. As you can see, it's the Max 2.

**Dave Jones:** Um EPM 240T100ISNCPLD. I like it. So, obviously, this thing is going to be quite hackable. You can reprogram the JTAG in this thing. You read it out. You can make mods if you want. Now, this micro here, it's a TI. I

**Dave Jones:** presume it's a micro. It's a TI one and I don't recognize the part number at all. I'll have to Yeah, you should be able to read that. But offhand, I don't recognize it, so I have to look that one

**Dave Jones:** up and see what it is. But why they've What the second CPLD there is doing, the Altera one, I don't know. But obviously, they deemed that they require two devices. So, obviously, this thing is quite hackable and quite powerful. This is obviously

**Dave Jones:** another serial JTAG or in-circuit serial programming {slash} debug header. So, you can do some great stuff with this. I like it. And here's the input jacks. They're quite unusual. At first, I thought I really liked them. They They sort of

**Dave Jones:** looked really good and I had no issues with them. They've got a tiny screw down here, but they're molded inside here. So, you won't screw them. They've got a single piece of folded metal, which does the blade input

**Dave Jones:** terminal. But look, there's another tiny piece of folded metal poking out, which is then soldered onto the board. So, the reason I don't like it is because if you insert something into If you insert a component continuously into blade, you might You

**Dave Jones:** can see that blade actually moving. And that is Maybe could eventually wear out that solder joint or break it off or crack the joint or something like that. So, I don't know. Maybe BK BK Precision have done their research on that and tested

**Dave Jones:** it thoroughly. But I don't know. I'm just I would have liked to have seen a different interface, either discrete wiring going over or something like that. So, not entirely trustworthy of that, but I'll give them the benefit of the doubt

**Dave Jones:** um through long-term testing. Just as a very quick reference, here is the uh old Escort design. And as you can see, it's it's uh quite uh lower tech. It's um it uses older devices. There's no CPLD up there and uh no USB uh interface either.

**Dave Jones:** And there's lots of discrete circuitry up there. And as you can see, the device down here, if you can read it, is it's going to say Escort on it. There you go. Escort. So, overall, I really love the new

**Dave Jones:** redesigned circuitry. They've really completely redone it from the ground up. It's a nice layout. It uses nice uh modern components and surface mount caps. I love it. Big thumbs up. So, what do you get in the box with the 879?

**Dave Jones:** Well, let's check it out. Tada! We get a manual, which is pretty good. We'll take a look at that later. I don't mind that at all. We get the meter, beauty, with an installed battery. We get a plug

**Dave Jones:** pack, um a real old-fashioned transformer plug pack, which is uh 12 V 150 milliamps, but it's 120 V. Um so, I didn't get the one for the Australian market, presumably, but you get the plug pack, which is great. And

**Dave Jones:** you get a mini USB um interface cable, but that's it. There's no software. Uh you download the software off the internet, which we'll do later. But that's it. Bit disappointed. Why couldn't they throw in the uh the tweezers? You can get the tweezers for a

**Dave Jones:** 26 US dollars extra. They could have thrown that in. That would have been beautiful. And it's 299 uh US dollars. So, it pretty much puts this meter pretty probably smack in the middle of the LCR meters on the market.

**Dave Jones:** There is a lower model to this, too, the 878B, and it pretty much doesn't have ESR and a bunch of other useful stuff, and it's not that much uh cheaper. So, I'd recommend going springin' if you're going to get this model for the

**Dave Jones:** top-of-the-line 879B. So, what are the headline specs? Well, they've improved this model over the existing Escort design in that the primary display is now 40,000 counts, which the old one was 20,000 counts. So, you get twice the number of counts,

**Dave Jones:** which is really useful. It means you can get uh a greater resolution for a more over a more useful range. So, if you measure a 39 um 39 nF capacitor, you'll get an extra digital resolution over a 20,000 count

**Dave Jones:** meter, which is awesome. Now, um the secondary display is 10,000 uh count, which is still pretty darn good. Um it's got USB interface, which we'll go into. Um it measures up to 10 kHz, which uh the cheaper LCR meters won't, so that's

**Dave Jones:** real handy. And the um the headline specs are 0.5% uh specs 0.5% plus one count. So, it's really super duper accurate specs, better than the more expensive ones on the market, which will have They'll be 0.5% too, but they'll

**Dave Jones:** have a higher plus count. I was a little bit disappointed that it didn't come with a calibration certificate. That would have been really nice. For 300 bucks, you get into the borderline where you might expect a calibration certificate, but you do get

**Dave Jones:** a 3-year warranty with it, which is pretty awesome. Let's take a look at the unit overall here. Now, it's a really nice fit in the hand. It's got the nice curved design on it. It's the original Escort uh case, basically. But, and it

**Dave Jones:** still feels really nice. It's got the rubber uh holster around the side, and it's got a very nice tilting bail on it. It's uh can sit Well, it sits like that, and it really is quite stable. And yes,

**Dave Jones:** you can push the buttons without the thing falling over. And it does actually I'm not sure if this is a feature, but it does actually snap back even further to give you a much shallower uh angle like that. I'm not sure if it's supposed

**Dave Jones:** to do that, but it does. And the battery compartment, as I said, in the back so you can access it, which means that you that you don't break the calibration seal cuz when you get these things calibrate calibrated by a professional

**Dave Jones:** lab, they'll typically put a cal seal on here and you want to be able to change the battery without doing that. And as you can see, it's got some some polarizing hooks in No, some polarizing tabs in there which allow you to only

**Dave Jones:** insert the battery the correct way. Although you can actually put it in, but you can't close the back on it like that. So it really only lets you put in the battery one way, which is great. It's a nice design and I like it. It

**Dave Jones:** feels really feels really quite solid. I haven't put the extra screw in there yet for the for the battery cover, but it really feels like a nice solid unit and it could survive the knocks in a general lab.

**Dave Jones:** On the side here, excellent. We've got a standard mini B USB connector. I love it. It's not optically isolated, so that is one disadvantage of this. So if you if you do require optical isolation on your LCR meter or your test gear in

**Dave Jones:** general in a lab, this one is not going to be suitable for you. But it has a great advantage, high-speed USB interface, standard connector. I love it. The input terminals down here, it's got a guard input terminal which you may

**Dave Jones:** not get on the lower cost instruments, which is great, which allows you extra shielding when you make up custom test leads to go off to a a production test jig or something like that. It's got the blade input terminals up here for the

**Dave Jones:** through-hole components and it's got standard leads down here. And I forgot when I did the unboxing, I forgot you got the leads as well. You got the standard clip leads that plug in here. They have a nice not an entirely Um, really tight fit,

**Dave Jones:** but a reasonable fit nonetheless. You don't get any guard terminal because that cable because that's only for custom leads, but these are quite reasonable alligator clips. There's an extra nice touch they've put up here, which is this display guard.

**Dave Jones:** It's designed for when that you put the meter flat on the bench. If it lands or falls flat and gets dragged across, it doesn't scratch the display screen. And let's give that a try, shall we?

**Dave Jones:** There it is. As you can see, under there like that, it's uh is the display is well and truly not touching the bench. So, it's a rather nice design. I like it. Power up the display and see what we

**Dave Jones:** get. If we hold down the power button here, as you can see, it tells us uh firmware version 2.0 and it's the model 879B. Quite neat. Now, if we have a look at the display up here, as you can see, we've got a

**Dave Jones:** primary display, as I said, 40,000 counts down here with a 10,000 count secondary display up here. And they correspond with the primary display button down here, primary functionality. Uh you can measure inductance, capacitance, resistance, and impedance. And the secondary display can uh switch

**Dave Jones:** between dissipation factor, quality factor, uh phase angle, or ESR, which is pretty much full uh fledged functionality for an LCR meter such as this. Let's try the standard GSM mobile phone interference test. Now, I'm measuring a standard cap here at just

**Dave Jones:** over 100 nF, and I've got my phone here. And as you can see, it's calling the uh thing. As you can probably hear the interference, the GSM interference through the microphone there, I'm sure you can. Um I don't even

**Dave Jones:** need to play back that. I know it's going to interfere, but look, it doesn't change the meter at all, even as you put it right over the cap. Nothing. So, it's really it really is quite nice. It's totally

**Dave Jones:** immune to GSM interference. I like it. I must say, I'm not a huge fan of this display because the the contrast isn't that great and the segments are really quite thin and it's it's quite glarey but that's no different to other this is

**Dave Jones:** pretty extreme here in the lab this glare which is seen there but that's not much to that's not much different to the other LCR meters I've got but yeah I'm not a huge fan of the display but it's

**Dave Jones:** certainly more than adequate and of course it's got all the indications and functionality you require with the dual display and everything else there's no problems there it's just the readability side of things. Now there's one thing I really

**Dave Jones:** like with this is the relative mode and sure all LCR meters have got a relative mode on them they have to it's a vital feature but this one as you can see I'm measuring 100 nanofarads here which is a

**Dave Jones:** reasonably high capacitance in the scheme of things and if I press the relative button here as you can see it all it continues to auto range it's jumped down to you know three pico around into the picofarad range down

**Dave Jones:** there it's awesome. Other LCR meters I've got will will not auto range say what once you hit the relative function they will stick on that one manual range so that could be really really useful. One of the awesome features of this

**Dave Jones:** meter is I can go down to 100 micro ohms resolution or point one million ohms let's check it out I've got the leads here let's short them together. It's not terribly quick auto ranging but I wouldn't say it's slow either there it

**Dave Jones:** is 0.06 ohms and if we relative that we hit the relative function there you go look at that fantastic and that's reasonably stable considering we're using the alligator clips and you wiggle the leads around here that's pretty darn

**Dave Jones:** impressive super fast auto ranging this is a 2200 microfarad cap okay let's check it out it's on picofarad range okay it's auto ranging let's plug it in. Bang it jumps straight to 2.2 mF. Awesome. And as you can see the the ESR

**Dave Jones:** resolution is excellent. And of course the secondary functionality up here goes from ESR through to quality factor, through to dissipation factor, and phase angle as well. And just to make sure it's not lying to us at 120 Hz,

**Dave Jones:** I've got it in parallel measurement mode here and I'm measuring 2.15 2.157. It's jumping around a bit mF on this 2200 microfarad capacitor down here. But let's see what we get when we go to impedance mode. Now at 120 Hz, 2 * pi *

**Dave Jones:** f 120 Hz * 2.15, let's call it 4 mF, okay? Invert that, and we should get an impedance at 120 Hz of 0.1657 ohms. Let's try it.

**Dave Jones:** There you go, 0.163, which isn't too bad. That's certainly within tolerance. And it's got a backlight, too. Let's try it out. You hold down this button here and bingo, backlight comes on. It's nice and even. Let me turn the lights down there

**Dave Jones:** a little bit, and it's pretty good. I like it. Nice even backlight. And if you go into the utility menu here by holding it down, you can see that you can turn the beep off and on, and you

**Dave Jones:** can turn the auto power off. 5 minutes, 15 minutes, 30 minutes, 60 minutes, or off. And that's really handy. I like that. And this mode here allows you to store the power-up setting. So if you wanted to power up at a specific

**Dave Jones:** frequency with a specific secondary display and uh a specific measurement mode, you can do that, which is quite handy. It's a bit annoying having to go through here. I'd probably uh prefer it to do that when you do the power on off

**Dave Jones:** button, but that's just a personal preference, but this is quite flexible. And it's also got a calibration mode down here. If you hold down this button, you can do uh open and short calibration compensation. So, in this case, I'm

**Dave Jones:** measuring resistance and I've got uh my leads shorted out, so I calibrate that and it takes out the test leads effectively. There's a bit of tolerance cuz there's a bit of play in the contacts in these crocodile clips, but

**Dave Jones:** that's a useful feature. This one real handy feature which is the tolerance mode down here. Now, it will allows you to measure uh components relative to a reference component. So, let's say this capacitor down here is our reference uh

**Dave Jones:** component. It's 100.06 nF, but it doesn't actually matter what it is. You press tolerance and bingo. Now, we can sort. Up here, it shows the tolerance that we're out. So, let's take some other capacitors which are the same value, but they're going to

**Dave Jones:** have this one is point .15% uh higher than the reference one. This one is 1.85% different, as you can see, higher. And this one here is 0.34% difference and you can enter different modes. You've got 1% uh 5% 10%

**Dave Jones:** and 20% modes as well. And as you can see, they've got to set to 1% tolerance mode here and let's deliberately put in a cap that's out of tolerance. And it will do several beeps instead of the single beep which you'll get

**Dave Jones:** with one that's within range. Great. If you take a quick look here at the manual for the automatic uh fuse detection we looked at when we opened this unit, it does tell you error, fuse and it basically says uh it doesn't say it's

**Dave Jones:** replaceable, it just says contact B&K uh precision for assistance. So, it looks like that is probably a an SMD fuse in there and not a resettable uh poly switch. Now, if you take a look at the manual here for the capacitance range at

**Dave Jones:** 10 kHz, there it is. These are all the different ranges at this particular frequency and the measurement mode series for all of them. It says if you go down here to parallel mode, it has a 40 pF range, which with with a 40,000

**Dave Jones:** count meter is phenomenal. It gives you 0.001 pF or 1 fF resolution, which is awesome. But, that's what it claims in the manual, but if you go here and you go into uh the capacitance mode, as you can see, pF 10

**Dave Jones:** kHz, we're in parallel mode. Bingo, it's not. It's uh not 40 pF, it's only 400 pF. So, the manual's lying. Where is the 40 pF mode? And the same thing with the inductance range 10 kHz down here in series mode,

**Dave Jones:** let's have a look at the actual meter. It says it should do a 40 micro Henry range. There it is. But, let's go down here and put it in series parallel mode, series mode 10 kHz inductance, we're not. We've only got 400 micro Henrys.

**Dave Jones:** Manual's lying again. And let's take a look at the specs in a bit more detail. Now, as you can see, they they all LCR meters or good ones will give you a uh an accuracy table like this for each

**Dave Jones:** different range of measurement value. This happens to be the inductance versus frequency. So, they'll give you a whole bunch of different uh tables for all the different frequencies for all the ranges. And this is uh not surprising that the best accuracy is typically

**Dave Jones:** obtained in the middle around the middle ranges here. So, as you can see, it's 0.5% plus minus one count, which is awesome. Absolutely awesome for a 40,000 uh count instrument. I love it. But as you can see, it starts getting 0.7% plus

**Dave Jones:** two, 1.5% plus three up here, 2.8% down here for 4 millihenries, and so forth and so on for all the different ranges. So if we go to the capacitance over here, here here's capacitance at 100 hertz, 120 hertz, and as you can

**Dave Jones:** see, 0.5% plus minus one count, but up in 20 20 millifarads, which is a huge amount of capacitance, we're talking 8% plus minus three or two and a half percent down here. And tells you which mode you got to use, series or parallel.

**Dave Jones:** So, a bit of a trap for young players, specifications on LCR meters. You can't just say, "Oh, it's 0.5% accurate." You really have to talk about the range and the frequency and the mode that you're actually using. Now, there's one thing I

**Dave Jones:** just cannot figure out. Now, I've even read the manual on this, okay? I had to actually go to the manual, which is the recording function or the min max average functionality. Now, to show this, that I don't know what the hell's

**Dave Jones:** going on here. I've got the original Escort design here, the Agilent / Escort design. They're basically the same meter, okay? Essentially like functionality and you know, breeding and all that sort of thing, is exactly the same. This one is

**Dave Jones:** derived from this. So the functionality, you'd think it'd be very similar. And if you read the manual, it's exactly what it should be. Now, if I enter Let's try the B&K Precision. I enter max average min mode. There it is, across there. And

**Dave Jones:** I plug in a cap, okay? No problems. It recorded. I plug in another one. It recorded. Plug in another one. It recorded, okay? And I hit the record function, nothing. Absolutely no It stays in min max average mode. Now, I can actually

**Dave Jones:** get it to do this. Watch this. I'll try it again. It seems a bit temperamental. But, if I try it There we go. It's taken a recording. Let's try it again. It's taken another recording. Let's try another capacitor.

**Dave Jones:** And it's taken a recording. Now, if we hit the record mode There we go. Max, okay. 100.18. It's not changing at all. It has not recorded those values whatsoever. Now, let's take a look at the Agilent over here. Let's turn this one off.

**Dave Jones:** Sorry. Well, let's switch into min max average mode and let's do it. Okay. Bang. It's recorded one. Let's do another one.

**Dave Jones:** Bang. It's recorded. Let's do another one. It's recorded it. One more for good measure. There we go. Okay. Now, if we hit press the button, max was 99.99, min was that, and the average was smack in the middle. So, what's going on with

**Dave Jones:** this B&K Precision? It doesn't That's how you'd expect it to work if you read the manual, but it doesn't. Let's try another method. Instead of disconnecting completely, we'll go into recording mode and I'll plug another one in parallel.

**Dave Jones:** Bingo. It's recorded. It's recorded, so it should have enough data to get max min average. It sticks with the one value. It's crazy. I reckon there's something wrong with this, unless I'm completely dumb and I don't know how

**Dave Jones:** this functionality works. Beats me. One other uh difference this new design over the original Escort one is that it had a an a manual range override, so it would actually allow you to go in and manually change the range.

**Dave Jones:** You don't have a manual selection capability on this new model BK Precision, or not that I can find anyway. It's only got auto ranging, which could which is great for most of the time, but when you need that manual

**Dave Jones:** ranging, it's really annoying that it only has auto ranging. Now, the manual that comes with is really quite nice. It's It's all in English, of course, and it's It's got pretty much everything you could possibly need, including the USB

**Dave Jones:** command modes. It's actually a serial port interface, but as you can see, here's all the here's all the serial commands for controlling the instrument. So, you can write your own drivers for Linux or for any other serial equipped

**Dave Jones:** machine you like. It's great. Now, let's do a basic measurement on a 1 millihenry inductor here. And as you can see, it's got an ESR of 2.6 ohms or thereabouts. Let's see if we can fool that by putting a 10-ohm resistor in

**Dave Jones:** series. We clip that on there. And no, we can't fool it at all. There it is, 12.9 ohms and still 1 millihenry. Now, I won't bore you with all the details about how I measured all sorts of components over all sorts of ranges,

**Dave Jones:** and it seems to do exactly what it's supposed to do. And spec-wise, I don't have any real high-precision high-stability capacitors and inductors to do absolute reference measurements with, but comparative measurements with other LCR meters I've got show that it's

**Dave Jones:** spot-on. And really, I have no doubt it's going to meet its manual specifications that are in the manual over all the ranges. So, it looks like it's a really high spec instrument. I like it. And here's the PC software.

**Dave Jones:** I've got it hooked up via USB here, and you have to install the drivers. You can download the drivers and the basic control software from the BK Precision website. Now, I have I had a bit of an issue here because I installed the

**Dave Jones:** driver software and it told me that it set up this serial port because it is actually a USB to UART bridge driver. So, it set mine up as COM number eight. And if you go into the software here, it only supports up to

**Dave Jones:** COM number six. So, that's something to watch out for. I had to magnet manually reconfigure it via Windows to COM five. So, if I go to COM five and connect, bingo! It showed up as remote on the LCD

**Dave Jones:** there, and we can measure. I've set it to auto update here, and it's reading the primary and the secondary display from the meter, but look at the resolution. Check it out. It's 0.1 femtofarads. It's phenomenal. And it looks like you

**Dave Jones:** can get much greater resolution than what you can get on the display here. This is really remarkable, and it could come in real handy. And basically, this is just a simple control program. You can basically control all the remote

**Dave Jones:** interface on this. So, I can measure capacitance, or I can go in and measure impedance, or measure inductance, or anything like that. So, if I stick my capacitor in there, and I measure capacitance, there it is. It's popped up, and it

**Dave Jones:** gives you much better resolution than what you can actually get on the display. Check it out. 98.25. I've got an extra digit of resolution here. And you can set up the measurement mode, series parallel, the test frequency. Of

**Dave Jones:** course, you can change all that. Um and you can do the tolerance values as well. But and uh, the only other thing it does is it allows you to record data. So, if I hit the record data thing here,

**Dave Jones:** and I can view the log data. There it goes, and it brings it in in full resolution. Check it out, which is phenomenal. And then you can just stop that in the background. So, we'll stop that there, and you can save it to Excel

**Dave Jones:** and text format. Beauty, I like it. It's an awesome little control program. But, the good thing about the serial commands on this is that, um, they are SCPI or Skippy compliant, which is, um, stands for standard commands for programmable

**Dave Jones:** instruments. So, it has a standard interface, fully documented. You can write your own drivers for it for any any control program you like. Awesome. And the serial port driver is actually, uh, the Silicon Labs VCP driver. So, it

**Dave Jones:** does support everything up to Windows 7, which is what I'm using here. And let's do a quick check of the battery consumption. Now, the MeterHit Energy here is measuring the battery voltage. Uh, the MeterHit Extra here is measuring the input, uh, battery

**Dave Jones:** current. I'm powering it from my external supply over there. And, uh, the, um, specs are actually in the, uh, manual, and it tells us that, um, it draws about 28 milliamps with the power on, and two microamps power off. But, as

**Dave Jones:** you can see, it's only drawing 0.5 microamps in standby mode. So, that's excellent. It easily meets its spec there. And just in regular mode, it's only drawing 17 milliamps. So, much for 28. So, the specs are way out. Let's

**Dave Jones:** measure a capacitor, see if it makes any difference. There we go, 17.6 milliamps, no problem, at 9 volts. And it tells us that it drops out at 6.8 volts, which is pretty good. Well, let's try that out, shall we?

**Dave Jones:** Let's wind down the power supply. And we're looking for the low battery at 6.8. Yep, there it is. There it is there. Yeah, and it is about 6.8 as they claim. As you'd expect at 6.8 volts, it's about 22 milliamps

**Dave Jones:** consumption, but still way under the data sheet spec of 28 milliamps. That sort of consumption with a 9-volt battery at around about 20 milliamps is probably going to give you about 45 to 50 hours of battery life, which isn't

**Dave Jones:** too bad for an instrument like this. So, what are the maximum measurement ranges? Well, let's check it out. The inductance we're talking about 1,000 Henries full scale, which is pretty darn good. And at the minimum range, it says it's 40 micro

**Dave Jones:** Henries, but as I said, I couldn't get that. It's only 400 micro Henries, but that's still pretty darn excellent usable range. And the capacitance we're talking about a maximum range of 20 milli Farads, which is pretty good. If

**Dave Jones:** you need to go bigger than that, well, jeez, you're into some serious stuff. And the minimum range, as I said, I couldn't get 40 pico Farads, so the minimum range is 400 pico Farads. But really, if you're going to need more

**Dave Jones:** than that, maybe you can use the PC interface to actually extend that if you really need to. And the resistance only goes up to an upper limit of 10 meg, which is well, it's not that great, really, but you

**Dave Jones:** don't typically use these LCR meters to measure high values of of resistance. And the ESR down on the minimum range is a 1 ohm range. So, it's pretty awesome in the ESR and the resistance is 4 ohms minimum range. So, the verdict on the BK

**Dave Jones:** Precision 879B? I really like it. It's probably my pick of the handheld LCR meters. It's I think it's great value for money at $299. Bit on the expensive side, maybe you could argue, not quite at the hobbyist level, but it's a really

**Dave Jones:** awesome instrument. It's precise, it's got a huge measurement range, and the PC software is really nice, and the PC interface. The only disadvantage with that is that the USB interface is not isolated. So, if you need an isolated interface for some sort

**Dave Jones:** of production work or something like that, it's probably not going to be suited unless you get an external isolator. You might have to go for another instrument. But, apart from that, it's a really great meter. It works really well. I like it. Um but, I

**Dave Jones:** have no idea what's going on with the recording min-max functionality. So, B&K Precision need to look at that and tell me I'm an idiot cuz I don't know how to use it. I don't know. Go figure. But, yeah. I really like it. Check it out.
