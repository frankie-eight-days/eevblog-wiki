---
video_id: FqN77SZF5zU
title: EEVblog 1656 - MAILBAG: ElectroPermanent Magnet, DIN PSU's, Sponge, Beelink EQ14 N150 PC
url: https://www.youtube.com/watch?v=FqN77SZF5zU
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 32, "3": 47, "4": 59, "5": 76, "6": 90, "7": 106, "8": 121, "9": 132, "10": 145, "11": 160, "12": 175, "13": 194, "14": 210, "15": 222, "16": 235, "17": 251, "18": 262, "19": 273, "20": 289, "21": 303, "22": 315, "23": 330, "24": 344, "25": 357, "26": 371, "27": 385, "28": 397, "29": 411, "30": 424, "31": 438, "32": 453, "33": 467, "34": 483, "35": 498, "36": 520, "37": 535, "38": 551, "39": 563, "40": 576, "41": 596, "42": 609, "43": 622, "44": 636, "45": 648, "46": 663, "47": 680, "48": 689, "49": 701, "50": 717, "51": 728, "52": 741, "53": 752, "54": 764, "55": 777, "56": 789, "57": 805, "58": 820, "59": 833, "60": 850, "61": 869, "62": 885, "63": 897, "64": 920, "65": 942, "66": 957, "67": 977, "68": 998, "69": 1015, "70": 1026, "71": 1040, "72": 1054, "73": 1068, "74": 1078, "75": 1089, "76": 1106, "77": 1127, "78": 1142, "79": 1156, "80": 1173, "81": 1193, "82": 1207, "83": 1233, "84": 1248, "85": 1272, "86": 1291, "87": 1309, "88": 1321, "89": 1338, "90": 1350, "91": 1366, "92": 1381, "93": 1395, "94": 1410, "95": 1423, "96": 1438, "97": 1453, "98": 1467, "99": 1482, "100": 1495, "101": 1507, "102": 1521, "103": 1532, "104": 1547, "105": 1562, "106": 1575, "107": 1589, "108": 1601, "109": 1616, "110": 1628, "111": 1641, "112": 1657, "113": 1673, "114": 1690, "115": 1705, "116": 1718, "117": 1730}
---

**Dave Jones:** Hi, welcome to EVERYONE'S FAVORITE SEGMENT, MAILBAG, back on the bench in old school format because well, if you've seen my latest video look at this, it's clean. It's clean. It's an absolute clean bench. Unbelievable. You might never see it

**Dave Jones:** again. So, anyway, um makes that reminds me that uh yeah, this grubby old um UV faded mat, I think uh yeah, I might need to replace that with like a nice uh gray background. Leave it in the comments down below like I did

**Dave Jones:** with my Tenma microscope one. I had put like a nice new gray background on it. This is pretty drab. Anyway, Mailbag. And the reason I'm doing it old school like this instead of uh talking head on the camera is that uh my current Mailbag

**Dave Jones:** bench is kind of yeah, um it's half in between the clean-up now, so it's not workable at the moment. So, if you want to send something into Mailbag, send it into EEVblog Mailbag. You got to actually put Mailbag on it. P.O. Box

**Dave Jones:** 7949, Norwest, New South Wales, 2153, Australia, not Austria. Thank you very much Digital Power Systems uh dot EU there um in Kolbermoor uh in Germany. Hi to all my German viewers. Um let's check it out. It's a It's a DPS, is it? I've

**Dave Jones:** got no idea what a DPS is. Geez, the knife looks big on the the screen here, doesn't it? And yeah, it's kind of big. Um and for those who think oh, Dave, sharpen that thing. No, it's perfectly fine. You want to come here and find

**Dave Jones:** out? Sneak you down the side. We've got a DCC-4805 and a serial isolator. Nice. Oh, USB-C. I don't think I've got a USB serial isolator. Let's have a look. Enjoy. Thank you very much. Um let's Oh, right. Yes, okay. Um yeah,

**Dave Jones:** they did clue me in. Look at this, it's a little DIN rail mount. Isn't that cute? Little DIN rail mount USB. And it's like half a normal width as well. But, unfortunately, it is not a 240 V. I

**Dave Jones:** was going to say, "How do you Well, you probably could fit a 240 V in in there." I wonder if they have a 240 V like mains version. Obviously, like DIN rail aren't just designed for mains stuff. They're

**Dave Jones:** designed for low voltage industrial equipment as well, where you've already got an existing you know, you might have a 12 V bus or a 24 V bus or something like that. And you just want a USB The electrons are going to fly out. Um

**Dave Jones:** and what's this one? Oh, this one here is that 9 to 48 V input. Nice. Yeah, so very handy if you just want a like a 5 V and either USB-C or just like screw terminals inside your control system

**Dave Jones:** that uses DIN rail. So, very handy. Um it looks like we've got a positive negative input side input on this side and output on that side there. So, yeah, negative on the outside. So, yeah, they're labeled fine. And it looks like

**Dave Jones:** this one has your various power delivery voltages as well up to 12 V 1.5 amps. Jeez, they don't weigh anything either. So, yeah, let's crack it open. Looks like these just crack open nicely here. Oh, there we go. Flippity-doodah. Yeah,

**Dave Jones:** there you go. It's all Yeah, just one nice piece of it. 1 mm PCB. They're excited about their 1 mm PCB. It's not none of that 1.6 mm rubbish. Not that 0.8 mm standard rubbish. 1 mm. Thank you very much. Did

**Dave Jones:** they have to do that for some particular reason to get the exact height required for the USB? Yeah, so probably yeah, if you went for 1.6, it might have extended out there and you wouldn't have been able to do the

**Dave Jones:** plastic on the side there. Perhaps I'd say that's probably all to get the height on the inductor there. So, yeah, that's a fit envelope uh decision to go with uh 1 point and go with a 1 mm PCB.

**Dave Jones:** I guess they uh decided that uh 9.8 was too small for some reason. Hmm. The controller there is an SPM5218. I'll put up the data sheet uh for that thing, but we've got ourselves a fuse over there, so that's nice. Uh if you of

**Dave Jones:** course if it blows you can easily uh replace that. Just uh pop the hood off like I did and just uh solder in a new one. Bob's your uncle. And they've got an awful lot of caps there on uh the

**Dave Jones:** output there to try and get the uh well, I I don't know. They might have got a bargain on uh the caps of course. Um and of course lower uh profile, so you know, you're not limited to Although they do

**Dave Jones:** use some bigger jobbies over here, but uh yeah, anyway, that looks very nice. And inside the 48-V uh jobby, there you go. Um the very similar, like identical construction really. Uh fused as well. Uses a different converter there. I'll

**Dave Jones:** put up the data sheet for that one and uh yeah, it looks really nice. I like it. I do like how they actually use um these PCB soldered integral uh screw terminals like this. That's That's just a really nice design. Really nice

**Dave Jones:** solution. I like that. And your physical stress is uh decoupled by uh you know, these plastic um inserts here and the force going in this direction. So really there shouldn't be any uh stress on those solder joints. No worries. Hang

**Dave Jones:** on. 1 mm PCB width? Uh that'll be thickness. Germans. And if we power that up you can see that they've got a little uh right angle LED on there and they're just using the uh front panel deckle as a diffuser there.

**Dave Jones:** Nice. And at 9-V input only 2 mA quiescent current there including the LED. Nice. And at 48-V that's only dropping down to 1.1 mA. And we'll just spot check the output cuz you don't want it actually precisely 5,

**Dave Jones:** believe it or not. And sure enough, 5.15 there. The reason you wanted a bit above is because uh so then uh when you've got like a cable drop, 40 dropping your cable going into whatever the thing you're pairing, then you're not starting

**Dave Jones:** out at 5 V. You're starting a bit above, so then you know, because most things are going to tolerate 5 V input plus minus 5%. So you don't want to go like to 5.25, but 5.15 output voltage is a

**Dave Jones:** reasonable compromise like that that then you can have you know, a bit of loss on your cable and no worries. This cute little thing is an isolated USB-C serial port. I like these. You should have um a few of these in your kit for a

**Dave Jones:** like interfacing with you know, I'm interfacing with like I do a teardown, I want to like interface with a serial port or something like that, then a little isolated jobby like this is very handy. So I'll put up the data sheets

**Dave Jones:** for these. I can't quite read them here, but that's obviously how USB to serial, very simple. And then we've got an opto-isolator here uh denoted by the uh silkscreen of of course. So these are completely isolated. Really nice. But of

**Dave Jones:** course you've got to supply power to the other side for the transceiver on this optocoupler side. So this positive and negative has to go to your um your device under test. And yep, yep, they are labeled there. Very nice. They've

**Dave Jones:** even put pads there so you can like solder on your own wires. That's thoughtful. I like that. It's upside down, so all the electrons are going to fall out. There you go. That's cute. That's the UART ISO-DPS. So thank you very much DPS, designed in

**Dave Jones:** Germany of course. These are cool little bits of kit including this. These are cheap as chips, they're only 21.90 euros including that. I couldn't quite get a price on this, but it's not going to be that expensive. So yeah, I'll link them

**Dave Jones:** in down below. Check them out. Thank you very much Zubax, zubax.com. You can scan that if you got one of those newfangled shoe phones. And they're from Estonia. Hi to all my viewers in Estonia. Um all I know about Estonia is that uh they

**Dave Jones:** offer like really cool like digital residences. Hmm, maybe I could become an Estonian resident. What do you reckon? Australia's going to hell. What have we got in here? Ah, let's open up. Ooh. Open uh Siffel? Sifel? Sifel? Um

**Dave Jones:** I don't know how to pronounce that. Anyway, it's open, is it? Got a cool sticker. Ooh, liking that. I do kind of sort of know what this is. I like the packaging here. That's really groovy. That's we've got

**Dave Jones:** a module thingy. Check that out. Ooh, look at that, potted. Ah, in red. Red potting compound. Ah, thing of beauty. It's a joy forever. It's a Zubax FG401MA. And some people might have guessed it already. What this is, it's an electromagnet

**Dave Jones:** thingy. So, you apply your voltage across here and boom, you've instantly um got a super powerful magnet to do whatever you want with. And I got these as well. This is a permalloy plate, of course. Doesn't stick at the moment, but

**Dave Jones:** uh she will once we apply here. And it looks like um this is a CAN interface thing. So, presumably, you know, you can control this uh via software somehow. Um so, this is 150 euros for the electro uh magnet. And

**Dave Jones:** by the way, it is not just like a coil and that's it, Bob's your uncle. It's more advanced than that. Um and the CAN interfaces they've got down 75 uh euros down here. And the plate is 28 euros for

**Dave Jones:** your permalloy plate. Um I didn't get any instructions, so I'm going to have to uh go download and um RTFM. But there is the hero shot. Look at that. Ah, I I just love the red potting compound and

**Dave Jones:** the red stand off on it. It just looks gorgeous. It really does. That's great. So, Zubax are a aerospace specialist manufacturer, and this is one of their products that is designed for like payload attachment for drones or for robotics or something like that.

**Dave Jones:** This can hold up to 20 kilos. Now, the interesting thing about this is that there's not just an electromagnet that you know you apply power to and then you know it's chewing all that power to get your magnetism. This will actually take

**Dave Jones:** zero power once you turn the magnet on. So, you know, you're not chewing that battery from your drone or your robot or whatever it is that's holding your payload. So, you can you know you can drop something from your drone. So, this

**Dave Jones:** can hold up to 20 kilos and then drop it via command without using any power except when it's changing state. And it can change state in like under a second. So, I'm not sure if we're actually going to get details about how this

**Dave Jones:** works. It might be you know it might be some proprietary tech in here. Have to do some research. They don't seem to have any specific technical details of exactly how they've implemented their design, but I'll put up the Wikipedia

**Dave Jones:** page for these electropermanent magnets as they're called, and that'll show you that they basically have two different types of permanent magnetic material soft and a hard one they're called. And by actually reversing, you know, flipping the polarity of a coil cuz they

**Dave Jones:** will have a coil in here. By flipping the polarity of the coil temporarily, you can actually either effectively enable or disable the electropermanent magnet. And so, it takes but once you've made that switch, the magnetism will stay there and it holds onto your

**Dave Jones:** payload and then it takes no power. And then you just provide a bit of current to flip the thing for you know a couple of seconds. This case I think this one's rated for 1 second. And then it releases

**Dave Jones:** your payload and uh your uncle. Very cool bits of kit. So, the cool thing about this is that as I said, it comes with uh this CAN interface here, but it also comes with uh this standard um RC

**Dave Jones:** uh as in remote control uh PWM uh interface as well. And uh there's like digital um control as well. And there's other bus compatible uh protocols and all sorts of things uh designed to actually drive this thing. So, we're just going to use

**Dave Jones:** the analog input here. So, uh just got uh 5 It operates from 5 V up to 40 V or something. I'll put up the maximum um specs here. But yeah, um then all we have to do is take this analog input and

**Dave Jones:** all we have to do is put a 5.1 K resistor either uh to positive, which should switch it on I think, or negative, which will uh switch it off. So, let's go ahead and uh then turn this on and you can see it's got a quiescent

**Dave Jones:** uh current there of about 27 mA. So, it's not it's not zero power, but the fact is uh the coil is not uh taking any power. So, you know, that's like bugger all there. And you can see we've got a

**Dave Jones:** little flashy flashy uh thing going on there. And you can read the manual. It's incredibly kind just the data sheet and slash manual incredibly comprehensive. It's got all the code and all sorts of things. Um yeah, it's they've really

**Dave Jones:** gone to town on this. It's really amazing. At the moment we've got the metal plate. It's not magnetic, okay? So, this will have up to 20 kilos um holding force. So, here we go. Watch the display here and it should take a surge

**Dave Jones:** of current for a second or two and let's switch it on. Let's see what it goes to. Boom. Oh, I'm hearing something went up to what point eight or something. I might have missed that, but yeah, about point eight amps and it dropped back

**Dave Jones:** down like that. So, this is now this should be permanently magnetized. I should not be able to pull Yep, I can't I can't pull that off, right? Maybe I can prize it off, but that's held there with 28 kilo 20 kilos um maximum weight

**Dave Jones:** handling uh capability on that thing. And as you can see, it's only drawing the quiescent power now. Very cool. So, now if I put it to negative, Oh, yep, there we go. 0.8 something like that. And it just I I don't know if you

**Dave Jones:** heard that crackling sort of sound like shh like yeah, there's actually a sound to it. But it started at 0.8 amps and then just went down like that. And now it should just play yep, it just lifts off like

**Dave Jones:** that. Cool bananas, huh? So, the it looks like there is a bit of residual stickiness there. But yeah, it's basically gone. Fantastic. Electro permanent magnets. Beautiful. So, let's go for a drop test, shall we? We've got multimeter attached to the plate. I've

**Dave Jones:** magnetized that sucker. So, and I can even turn the power off and it's still holding that meter. No worries. Let's turn it back on and demagnetize. Boom. Drop test complete. Winner winner, chicken dinner. So, that is super cool. Thank you very

**Dave Jones:** much Zubax for sending in that very interesting bit of kit, an electro permanent magnet. So, if you're into your drones or your automation, your robots or whatever, and you need electro permanent magnet that you can turn off and on that doesn't take you know huge

**Dave Jones:** amounts of power, these things are the ducks guts. This is very well implemented. I like it. It's quite reasonably priced at 150 euros, too. Check it out down below. have a mystery item. No idea who it's from because it

**Dave Jones:** just comes from a local re-shipper. So, not sure what the deal is. Let's go. What do we got? Okay. Well, it's protected good, whatever it is. It's a Why do we have a plug pack? Uh It's an Aussie one.

**Dave Jones:** Okay. I got no idea why I got that. I did not order that. It's a Qualcomm quick charge three. Handy, but Uh generic power adapter. It's got a model number on there, but I don't know. Like can't even do a teardown because they're

**Dave Jones:** destructive and well, what's the point? Okay, I don't get it. Oh, look, it's an old-school letter. Thank you very much Don Hall. I have a firm at the United States of America, Ohio. Hello Hi to all my viewers in Ohio.

**Dave Jones:** Yeah, what do we got? It's a duh Electreon driving roads. Why? While the ascent of electric vehicles is ongoing, the speed of adoption is at best unpredictable. Yeah, and they're dropping. One major hold up for consumers and commercial range anxiety.

**Dave Jones:** While developing networks away from roadways, it's okay. It's an article Uh yeah, in what magazine? Um Electreon's system. What about it? Oh, got some ads. Oh, wide flange boxes. There you go. Fantastic. Oh, okay, this is the wireless um right. Yes, I've done

**Dave Jones:** a video on the wireless uh road charging thing. No, it's It's a boondoggle. It's Well, it works, but it's not practical. It's like for widespread adoption in roads. It's never going to happen. I've done a video on I'll link it in here. Um

**Dave Jones:** and it was What was it? A $50 million boondoggle or something like that? Um they had some pilot program. Can't remember where it was. Don't think it was in Michigan. This This might be a different one, but yeah, I think it was

**Dave Jones:** similar. Yeah, and the Mdot um which is the Department of Transport. And yeah, they keep pouring money into this thing thinking it's going to be a thing. So, yeah, they got this pilot program in Michigan studying EVs. No.

**Dave Jones:** No. The only way it's possibly going to be of value is if you say had a taxi rank or something where where cars like sit for like extended periods of time sort of like, you know, guaranteed to sit for extended periods of time

**Dave Jones:** waiting for people. So, you know, if you had an EV taxi, for example, yes, the taxi rank you could actually install just a strip of these. It wouldn't cost much and yeah, and you know, they're not hugely efficient, but they do work. You

**Dave Jones:** can't be then you've got to, you know, chicken and egg thing. You've got to design it into the car to begin with and no one's going to design it into the car unless there's already existing infrastructure for it. So, you'd have to

**Dave Jones:** order special, you know, EV taxis that actually have this. Now, I'm not going to read you can read all this BS for yourself, but no, it wireless charging is not going to be a thing. I just noticed there's a note. Should have read

**Dave Jones:** the note first. Dr. Jones. I have enclosed an article from Electrical Contractor Magazine that you may find suspect. Solar roads again. Yeah, it's I am nearly retired EE in Ohio and I've always appreciated your content. Thank you, Don. I would love to

**Dave Jones:** see you and John Cadigan do an electric car collaboration. Yes, John Cadigan, a fellow Aussie YouTuber. I'll link in his channel down below. It's rather hilarious. If you like ockerism, Australian way of talk, then yeah, he's the guy for you and he does that car

**Dave Jones:** related videos. So, yeah. So, yeah, no is my official verdict on wireless freaking roadways. It's not going to be a thing except in very niche locations even for the electric buses. I've done the videos on the electric buses.

**Dave Jones:** There's just no point. Like even at the bus depot where you actually, you know, park the buses overnight. It's kind of pointless to even put them there because it's so easy. I've physically done it myself. Driven a bus in an

**Dave Jones:** electric bus into the depot, and I've physically plugged in the charger for it. It takes like seconds to do, and you get the most efficient transfer and fastest transfer possible. So, no, just no. No, it's just it's just

**Dave Jones:** silly. Only in niche applications will that work. So, oh, this looks exciting. On camera reaction material for hours of indulgent pleasure. Where does it come from? It comes from Australia. It comes from Brumby on the EV blog forum. So, let's rip it apart. I wanted

**Dave Jones:** to get the thicker ones, but the budget wouldn't allow. What the hell are these things? Reaction material. Hang on. Hang on. Here we go. Oh, no, I got to turn it up the other way. Right, I thought it might have been

**Dave Jones:** a magazine or something like that. But, hello. Sponge sponges. Sponge porn. Sponge porn. Oh my god. Where did he get these from? It's a sponge bonanza. I'll never run out of sponges. This is yeah, they're just generic one hung low brand. Oh.

**Dave Jones:** Hang on. Going to get Going to get the water. Okay, here we go. Sponge porn in 4K. I'm going to do it right here on the bench. Oh, will these BE ANY GOOD? OH, NO, THEY'RE A BIT PISS-WEAK.

**Dave Jones:** OH. That's not exciting at all. No. No, I give that I rate that maybe a four out of 10. Leave it in the comments down below. That's like that's like thin as. No. No, that's it's okay, but let's try two of them.

**Dave Jones:** Oh. It's hard to get through to the bottom one there. Yeah, no. No, I've seen way better sponge porn than that. Anyway, thanks Bramble. I'll never run out. Oh, no. It's a third sucker of the sav. Beelink. Beelink.

**Dave Jones:** Oh my goodness. They're back at it yet again. We've had Oh, navy blue this time. Yeah, these mini PCs, which I love, and we've had both an Intel jobby, like a high-end Intel jobby, and an AMD bloody Oh, it's a slidy thing. What's

**Dave Jones:** this one? This one is a Twin Lake N150. So, this is going to be much lower cost than the ones we've looked at previously. So, all I know is that it's the EQ series, but they've got like so

**Dave Jones:** many different variants of all their mini PCs, which is good and also bad because I have no idea and and the exact model of this thing until I actually get it out, and it should be on the bottom. These bloody hydraulic boxes.

**Dave Jones:** Here you go. It looks similar to the one we had before. The one we had before was an EQ, wasn't it? And very similar. So, is the teardown going to be identical? But yeah, the USB, the headphones, the

**Dave Jones:** USB-C. Yep, that's all identical. Yep. Yep. Yep. Everything's very handy with the integrated PSU and everything, but what model is it? Aha, the EQ14. All right, I'll go get a price on this one. So, this one is 230

**Dave Jones:** Yankee bucks or so. That's like sort of like standard price. You have been able to get it cheaper during sales and things like that. So, this is a really low-cost super powerful PC using like a low-power jobby, 25 watts with the new

**Dave Jones:** N150 processor, but it can scale down and they've got I'll have to link it in down below. There's only so many things I can screenshots I can put in. They've got extensive data available on the website to show

**Dave Jones:** how how much power it takes, what temperature it gets to during all sorts of operations and stuff like that. And suffice to say these things are really super quiet and super low power. So, if you want a really low power application,

**Dave Jones:** these things are absolutely fantastic. Anyway, it's the same EQ series, but we won't see I'm sure we won't see the 80 watt power supply like we did in the previous one cuz this is only 25 watt max processor. Yeah, there you have it.

**Dave Jones:** We've got a smaller 48 watt power supply. So, yeah, kind of like halfish of what we had before. Once again, direct mains input, absolutely fantastic how you know, you don't need external power bricks or anything. Just whack the

**Dave Jones:** mains straight in and Bob's your uncle. We've got our IO interface board on top here. We've got our RAM comes standard with 16 GB here, which is very nice, not that 8 GB rubbish, and 500 GB solid state drive under here and you can see

**Dave Jones:** it under there. They've just got a There's a second slot. Yes, there is a second slot there. So, yeah, you can expand this thing really nicely. And there you have it there. Just unscrew that and got some thermal pads on the bottom

**Dave Jones:** there. And look at that. So, there is our of course that's our 500 gig. It's even unpopulated for 500 gig. Man, when I was a boy, 500 kilobytes was a lot. No one will ever need more than 640 kilobytes. Remember that, kiddies.

**Dave Jones:** Anyway, yeah, dual M.2 slots there, very nice. And yeah, they've only got the one slot there for the RAM, but that's a plenty. You might might be able to expand that if you want. 16 gig is like plenty for

**Dave Jones:** any application this thing's uh going to run, but you could possibly uh expand that, too. But, yeah, extra storage, and of course, you've got the uh dual gigabit um Ethernets on there. You've got the dual HDMIs built in. You've got

**Dave Jones:** three USB A's, very um handy. And uh you've got the USB C and another USB A on the front. So, plenty of IO capability. And as we've looked at previously, I've even measured the uh heatsink temperatures. Um it uh brings

**Dave Jones:** air in from the bottom. The thermals on these are very good and uh pumps it out here through the uh heatsink. So, rises up through. So, they know what they're doing when they thermally design these things. They're quite remarkable for the

**Dave Jones:** uh size, actually. And as I mentioned, the fan is whisper quiet. It's practically silent. It's like 32 dB maximum when you're like streaming 4K or something. I'll put a once again, they've got extensive measurements and data on this. Um and yeah, you basically

**Dave Jones:** don't know the thing's running. It's great. And booting it up, there you go. We're getting the Beelink logo-y thing. And it'll have Windows installed, I do believe. Windows 11. So, out of the box, it comes ready to go. You get the uh

**Dave Jones:** nice USB lead with it. You get the power mains figure-8 power cord and uh Windows installed, Windows 11. And Bob's your uncle. But of course, you can install Linux on it, whatever you want. Knock yourself out. I love how you don't have

**Dave Jones:** to dick around with licenses anymore. It just like everything just works. I'm sure Microsoft are getting their coin somehow. Okay, some power measurements. We've got 1 W in standby. That's all right. So, let's power it up. And we're

**Dave Jones:** booting up. 20-odd watts when it's booting up. And it's uh it's going to drop down to 11, is it? Yeah, it's jumping around. I'm not sure what Windows is doing there. It was below 11. Up, nine. There it is, 10

**Dave Jones:** W. So, I don't know. Whatever Windows is doing with its thing, that's the idle consumption. It's not much. Signed in to Marty McFly. Okay, we'll run CPU-ID on this, and uh then we'll bench it. Let's bench it again and that's jumping up to

**Dave Jones:** 20 20 watts now while it's benchmarking. So, it looks like that's going to be its maximum. So, that was going to be its maximum 20 there, but I don't know if we're going to get higher than that because if you

**Dave Jones:** go over here, it says that the maximum TDP is 6 watts here. Well, that's obviously wrong. So, yeah, I'm not sure where it's getting that from. You probably have to go into I don't know the energy settings in Windows 11.

**Dave Jones:** I don't know. I don't use Windows 11. Whatever. But anyway, it's low power. It's not like a high-powered beast jobbie like we saw in the previous two ones. I think the previous one was even more technically more powerful than my

**Dave Jones:** editing PC at the moment. So, yeah. But this is designed as a nice little low-power jobbie. Anyway, I'll put up some benchmarks here for the N100 processor. Remember, this is the new N150 Alder Lake one. So, it's even slightly

**Dave Jones:** more powerful again that I believe than the N100. But compare it with say a Raspberry Pi, it's more than like twice the power of a Raspberry Pi for single and multi-core stuff. So, yeah, nice little compact low-power solution. If you don't need a lot of

**Dave Jones:** grunt, but it's got all the IO that the other ones have in this EQ series. So, yeah, well worth a look. The price point is very competitive. I don't know if there's much better out there at this price point, but I don't know. I'm not

**Dave Jones:** Linus Tech Tips. So, thank you very much Beelink for sending this one in. Might find a use for it around here in the lab for some you know, embedded permanent application or something. But yeah, please don't send any more. That was the

**Dave Jones:** third suck of the sav. Anyway, Beelink PCs very cool, very well designed. I'll link them in down below and very cost competitive. I just love these small form factors. They're great. I'm going to uh, now got three of these things.

**Dave Jones:** I'm going to use them for a whole bunch of stuff.
