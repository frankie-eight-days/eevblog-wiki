---
video_id: WUZuyL4eRCQ
title: iRiver Story HD eBook Reader TEARDOWN - EEVblog #189
url: https://www.youtube.com/watch?v=WUZuyL4eRCQ
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 31, "3": 47, "4": 79, "5": 92, "6": 103, "7": 117, "8": 130, "9": 141, "10": 157, "11": 171, "12": 188, "13": 204, "14": 219, "15": 234, "16": 254, "17": 266, "18": 290, "19": 309, "20": 326, "21": 339, "22": 351, "23": 369, "24": 386, "25": 405, "26": 423, "27": 439, "28": 455, "29": 470, "30": 485, "31": 501, "32": 514, "33": 529, "34": 543, "35": 555, "36": 568, "37": 583, "38": 598, "39": 611, "40": 625, "41": 642, "42": 660, "43": 673, "44": 690, "45": 705, "46": 724, "47": 741, "48": 760, "49": 778, "50": 796, "51": 817, "52": 847, "53": 861}
---

**Dave Jones:** Hi. Welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. What's more interesting than the new iriver Story HD ebook reader? Well, what's inside of it? That's what. You

**Dave Jones:** know what we say here on the EEVblog, don't turn it on, take it apart. Let's see if we can take this sucker apart, shall we? What have we got on the back here? Well, it was uh fairly from the

**Dave Jones:** start that there's a couple of Phillips head screws under the SD card cover there. So, uh I'm not sure I'm going to assume that they're part of it and these feet uh down here are a dead giveaway. And they certainly pop out as you expect

**Dave Jones:** and there's another Phillips head screwdriver in there. So, let's take those four screws out. Uh I expect there to possibly this uh end might have to uh pry open with a spudger bar or something like that, but we'll give it a go.

**Dave Jones:** Yeah, this looks very promising. I just pried that open with my spudger and uh sure enough there's a little plastic side clip. So, I expect there to be uh those similar sort of side clips all the way around the side, just like on the

**Dave Jones:** Kindle. And sure enough we have three of them along the bottom edge like that. Let's try and find the others on the side and the top end. And we've got no less than five at the top end here. 1 2

**Dave Jones:** 3 4 5. And the sides are a bit harder to get out, but there's 1 2 3 4 there on the right hand side. And the left hand side we've got 1 2 3 4 5 6. And yeah,

**Dave Jones:** the sides are just a little bit tighter, but uh uh if we open it up, bingo, it just pops open like that. Let's take a look inside. It's not nearly as interesting really as the Kindle, but that's uh to

**Dave Jones:** be expected. It's a bit less uh feature-packed, but it's got all the basic stuff you would expect. It's got the large lithium ion battery here. We'll take a look at the PCB. We'll take a look at in detail. It's a single-sided

**Dave Jones:** uh load that gets their manufacturing cost down. There's a membrane over here which goes to the um to the e-ink display. There's another membrane which goes over to the keypad on the front. The back panel, nothing's happening there and no, there is no RFID

**Dave Jones:** tag uh built in to that at all. The main uh PCB is is pretty much um it. There's an antenna that uh runs That's your Wi-Fi antenna up there. We'll take a look in more detail. The switch down

**Dave Jones:** here, nothing really happening uh there at all. That is That's just uh boring as. It just slides across. The uh spring itself is built in to the slide switch down here on the main board. So uh you can still operate uh the unit when the

**Dave Jones:** back cover's off, no problems at all. One curious thing is the large amount of free space around here and because the battery is not really uh held in with anything, not really contained with anything there, it's just sort of uh

**Dave Jones:** double stuck down with double-sided tape, I'm assuming. Um I can't see any reason why you couldn't replace that with a uh larger one and um of the same uh type of course so that the battery charging technology is compatible. Um

**Dave Jones:** but if you got the same uh type and you actually uh hacked out actually uh drilled out these um these walls here in the back case, you could actually fit a larger capacity battery in there, I think. No surprises with the battery at

**Dave Jones:** all. It's a 3.7 V lithium ion, nominal 6.7 Wh or 1800 mA hours. And the tape over the end like this is a dead giveaway that they've actually got built-in protection circuitry into the battery. That's a must-have in consumer devices

**Dave Jones:** like this with a fairly large capacity. I mean, 6.7 Wh is a fairly large capacity battery. So, if we actually peeled back that tape, we'd see the protection circuitry in there. Let's take a look at the main board up close.

**Dave Jones:** And of course, sitting right in the middle is the Freescale i.MX 508 Cortex-A8 processor. Quite a powerful low-power beast, very common in these e-book readers and other low-power products like that. This device here is the 2 GB NAND flash memory. It's a Samsung KLM

**Dave Jones:** 2G1DEHE device. There's another Samsung device up here, presumably another flash memory. It's a K4X 1G323, from what I can see. I don't know what that one is offhand. Down here, we've got another Freescale part, and it is an

**Dave Jones:** MC13892. And it's a PMU, a power management unit. It's got all sorts of stuff built-in. It It's It's a companion device to the ARM Cortex processor up there. It's got built-in battery charging. It's got Coulomb counting for knowing how much

**Dave Jones:** battery you've got left. It's got a real-time clock and a whole bunch of DC-to-DC converters and voltage regulators to power the cores inside the processor and things like that. So, it's a It's a very essential chip. And as you

**Dave Jones:** can see, there's a lot of analog stuff surrounding that. We've got the mini-B USB connector here. There's a small cutout in the board for that. There's another small device over here. I'm not actually sure what that is, probably

**Dave Jones:** unimportant. Now, curiously, there is a spare connector here, a flat flex connector, and they haven't populated that part. So, I'm not sure what the deal was there. In fact, there's quite a lot of unpopulated footprints all around here, quite a lot

**Dave Jones:** indeed. I'm not actually sure what the deal is there. Now, here's the main flat flex connector over on this side, which goes down to the keypad, the front panel QWERTY keypad. If we look up the top here, we've got the Wi-Fi chipset, no

**Dave Jones:** surprises, and Atheros. I think it's an AR61026, that's what I'm reading on there. I think they used a sim- very similar one, or they used the same brand one in the Kindle, no surprises at all. And they're using a little micro UFL coax

**Dave Jones:** connector to go up to the Wi-Fi antenna, which just sits in its own little thing there. That's just a little strip of circuit board, little PCB mount antenna, very common. And around the Freescale processor up here, quite a few

**Dave Jones:** unpopulated parts as well. There's the main crystal oscillator, and there are a few test points as well. There There you go, those gold pads in there, they're labeled as test points, but of course, they're highly likely to be access

**Dave Jones:** points for the JTAG and things like that, cuz they have to program these devices once they're in there. So, but I don't see any labeling for that, or any sort of easy access JTAG JTAG connector for hacking. And up

**Dave Jones:** in the top left corner here, we've got our E Ink display controller. Now, I believe it's an Epson. Um, I'm reading a TP365180, but don't uh quote me on that. Uh, very unsurprising, Epson make a lot of uh E

**Dave Jones:** Ink uh E Ink display controllers. Um, I believe they use one in the Kindle as well. And of course, we've got our flat flex uh PCB here as well. There's a couple of decoupling capacitors on there, and you'll notice that the uh

**Dave Jones:** that it's actually got a designed date um just before Christmas 2010. So, there you go. So, there you have it. That's it. Uh, pretty basic. It's got uh nothing more than uh what I expected. No um bells and whistles at all. But uh

**Dave Jones:** it's it's reasonably well made. I have no problems with it whatsoever. The the predominant uh the components are predominantly um 0402. Uh, they haven't gone any smaller than that. Uh, they could have even gone for 0603 if they

**Dave Jones:** wanted to to uh possibly uh increase their manufacturing yield, but uh these sort of, you know, 0402's no problem these days. So, really, it's uh not a bad uh design whatsoever. The layout is quite good. You can see

**Dave Jones:** they've actually panelized it down here. They've got the cutouts um well, the uh actual breakout um tabs for the panelization of the board. Why they've actually uh done a cutout there and shaped it like that, uh your guess is as

**Dave Jones:** good as mine. And I don't see any uh reset switch on here either. And you really have to wonder what happens when you disconnect the battery. Well, there's only one way to find out. And it's disconnected, and of course, the uh

**Dave Jones:** display is still there. It's still going because it's an E Ink display. It doesn't need any power to retain the last image. So, I'll leave that for a little bit, and uh there's no major capacitance on the board, so it should

**Dave Jones:** have already It shouldn't have uh held a charge really at all. And I'll reconnect that and see um if it boots up from scratch. Yep, there we go. We've uh It's reset itself. I plugged it back in and it looks like it's

**Dave Jones:** just going into that reboot process. And it's booting up. There we go. And yep, we're back in. We haven't lost anything. Everything seems sweet. No problems whatsoever. Hack away. And just like the Kindle, I was able to actually reset the

**Dave Jones:** thing without removing the battery, but just by holding down the power switch for uh 10 seconds and then turning it on. And that uh puts it into a cold reset, exactly like you've taken out the battery, presumably. Taking out the PCB

**Dave Jones:** was pretty easy, just uh half a dozen screws or so, and it just uh lifts out and we can take a look at the hinged switch mechanism here. It's not terribly uh exciting, not much to write home about, but um there you go. That's the

**Dave Jones:** swing mechanism. It's built in. And if we bring the PCB in over here, we can see that the There's the um tactile switches on the bottom of the board there. So, they're just two standard uh like a I think they're a

**Dave Jones:** Panasonic uh brand one if um memory serves me correctly. And they're just a little tiny uh membrane um dome type one. So, there you go. A pretty basic uh switch implementation. Um I don't know how many um how many presses they're actually uh

**Dave Jones:** rated for, but I assume they're uh quite significant. They wouldn't have used one that only had like uh 10,000 cycles or something like that. I'm sure they would have uh chosen um some tactile domes and switches that had in

**Dave Jones:** the order of millions of uh uh switch actuation. And there's a few interesting uh labeled test points on this board. They've got uh all the various uh power supply voltages. You can see there 3.3 3 and 1.8 uh for the Wi-Fi. And over here,

**Dave Jones:** there's a couple of interesting ones, boot mode zero and boot mode one. I'm not sure what they do, but if you want to have a play around with those, that would be interesting. And there's a power key, there's a digital 1.2

**Dave Jones:** supplies, there's various supplies in this um on this board for the processor and the various chip sets, but unlike the Kindle which had its easy access serial connector on the side of the case which allowed you to access

**Dave Jones:** the boot ROM of the system, allowed you access the actual command kernel of the thing. I can't find any equivalent serial serial monitor type interface on this board. There may be one there labeled as one of the test points, but yeah, it

**Dave Jones:** doesn't look as easy to hack as the Kindle was. And a few extra screws gets the back plate panel out and we can access the keypad and the LCD itself. And nothing really surprising there in terms of the

**Dave Jones:** key switch overlay. They're pretty pretty basic stuff. And if we have a look at the LCD itself up here, we can see you can see my boom mic there in the uh in the reflection on the mirrored finish

**Dave Jones:** on the back there. We can now see the membrane going into the uh LCD the E Ink, sorry, E Ink panel display which is made by LG. Um and up the top, you can actually see the the chip on board drivers there. You

**Dave Jones:** can actually see them embedded into the actual panel itself. And they're those tiny little They're they're actually they're actually silicon chips embedded in the panel itself which are drives. They actually drive all the individual rows and columns of the E Ink display. It's

**Dave Jones:** rather fascinating construction these things but ultimately there's there's not much to them at all. It's very typical of a standard row column LCD dot matrix driver system really.

**Dave Jones:** And we have a bare PCB manufacturing date of the 20th week 11 here for my particular unit. Well, that's it for the teardown. I hope you found it interesting and if you want to see the high-res photos of this go on over to my Flickr

**Dave Jones:** account. The link's on my blog website and don't forget to subscribe, rate, thumbs up, comment, video response, whatever. Thanks. See you next time.
