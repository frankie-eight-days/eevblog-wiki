---
video_id: FqN77SZF5zU
title: EEVblog 1656 - MAILBAG: ElectroPermanent Magnet, DIN PSU's, Sponge, Beelink EQ14 N150 PC
url: https://www.youtube.com/watch?v=FqN77SZF5zU
source: youtube-asr
timestamps: {"0": 0, "1": 36, "2": 65, "3": 91, "4": 117, "5": 145, "6": 178, "7": 215, "8": 235, "9": 264, "10": 278, "11": 310, "12": 330, "13": 359, "14": 389, "15": 419, "16": 433, "17": 462, "18": 478, "19": 508, "20": 544, "21": 573, "22": 596, "23": 612, "24": 632, "25": 660, "26": 689, "27": 719, "28": 736, "29": 761, "30": 782, "31": 808, "32": 838, "33": 865, "34": 893, "35": 911, "36": 945, "37": 961, "38": 985, "39": 1007, "40": 1031, "41": 1061, "42": 1085, "43": 1099, "44": 1138, "45": 1169, "46": 1189, "47": 1203, "48": 1223, "49": 1241, "50": 1264, "51": 1287, "52": 1312, "53": 1338, "54": 1352, "55": 1387, "56": 1412, "57": 1423, "58": 1440, "59": 1469, "60": 1486, "61": 1513, "62": 1542, "63": 1571, "64": 1601, "65": 1631, "66": 1644, "67": 1676, "68": 1709, "69": 1730}
---

**Dave Jones:** Hi, welcome to EVERYONE'S FAVORITE SEGMENT, MAILBAG, back on the bench in old school format because well, if you've seen my latest video look at this, it's clean. It's clean. It's an absolute clean bench. Unbelievable. You might never see it again. So, anyway, um makes that reminds me that uh yeah, this grubby old um UV faded mat, I think uh yeah, I might need to replace that with like a nice uh gray background. Leave it in the comments down below like I did with my Tenma microscope one. I had put

**Dave Jones:** like a nice new gray background on it. This is pretty drab. Anyway, Mailbag. And the reason I'm doing it old school like this instead of uh talking head on the camera is that uh my current Mailbag bench is kind of yeah, um it's half in between the clean-up now, so it's not workable at the moment. So, if you want to send something into Mailbag, send it into EEVblog Mailbag. You got to actually put Mailbag on it. P.O. Box 7949, Norwest, New South Wales, 2153, Australia, not Austria. Thank you very

**Dave Jones:** much Digital Power Systems uh dot EU there um in Kolbermoor uh in Germany. Hi to all my German viewers. Um let's check it out. It's a It's a DPS, is it? I've got no idea what a DPS is. Geez, the knife looks big on the the screen here, doesn't it? And yeah, it's kind of big. Um and for those who think oh, Dave, sharpen that thing. No, it's perfectly fine. You want to come here and find out?

**Dave Jones:** Sneak you down the side. We've got a DCC-4805 and a serial isolator. Nice. Oh, USB-C. I don't think I've got a USB serial isolator. Let's have a look. Enjoy. Thank you very much. Um let's Oh, right. Yes, okay. Um yeah, they did clue me in. Look at this, it's a little DIN rail mount. Isn't that cute? Little DIN rail mount USB. And it's like half a normal width as well.

**Dave Jones:** But, unfortunately, it is not a 240 V. I was going to say, "How do you Well, you probably could fit a 240 V in in there." I wonder if they have a 240 V like mains version. Obviously, like DIN rail aren't just designed for mains stuff. They're designed for low voltage industrial equipment as well, where you've already got an existing you know, you might have a 12 V bus or a 24 V bus or something like that. And you just want a USB The electrons are going to fly out. Um

**Dave Jones:** and what's this one? Oh, this one here is that 9 to 48 V input. Nice. Yeah, so very handy if you just want a like a 5 V and either USB-C or just like screw terminals inside your control system that uses DIN rail. So, very handy. Um it looks like we've got a positive negative input side input on this side and output on that side there. So, yeah, negative on the outside. So, yeah, they're labeled fine. And it looks like this one has your various power delivery

**Dave Jones:** voltages as well up to 12 V 1.5 amps. Jeez, they don't weigh anything either. So, yeah, let's crack it open. Looks like these just crack open nicely here. Oh, there we go. Flippity-doodah. Yeah, there you go. It's all Yeah, just one nice piece of it. 1 mm PCB. They're excited about their 1 mm PCB. It's not none of that 1.6 mm rubbish. Not that 0.8 mm standard rubbish. 1 mm. Thank you very much. Did they have to do that for some particular reason to get the exact

**Dave Jones:** height required for the USB? Yeah, so probably yeah, if you went for 1.6, it might have extended out there and you wouldn't have been able to do the plastic on the side there. Perhaps I'd say that's probably all to get the height on the inductor there. So, yeah, that's a fit envelope uh decision to go with uh 1 point and go with a 1 mm PCB.

**Dave Jones:** I guess they uh decided that uh 9.8 was too small for some reason. Hmm. The controller there is an SPM5218. I'll put up the data sheet uh for that thing, but we've got ourselves a fuse over there, so that's nice. Uh if you of course if it blows you can easily uh replace that. Just uh pop the hood off like I did and just uh solder in a new one. Bob's your uncle. And they've got an awful lot of caps there on uh the output there to try and get the uh well,

**Dave Jones:** I I don't know. They might have got a bargain on uh the caps of course. Um and of course lower uh profile, so you know, you're not limited to Although they do use some bigger jobbies over here, but uh yeah, anyway, that looks very nice.

**Dave Jones:** And inside the 48-V uh jobby, there you go. Um the very similar, like identical construction really. Uh fused as well. Uses a different converter there. I'll put up the data sheet for that one and uh yeah, it looks really nice. I like it. I do like how they actually use um these PCB soldered integral uh screw terminals like this. That's That's just a really nice design. Really nice solution. I like that. And your physical stress is uh decoupled by uh you know, these plastic um inserts here and the

**Dave Jones:** force going in this direction. So really there shouldn't be any uh stress on those solder joints. No worries. Hang on. 1 mm PCB width? Uh that'll be thickness. Germans. And if we power that up you can see that they've got a little uh right angle LED on there and they're just using the uh front panel deckle as a diffuser there.

**Dave Jones:** Nice. And at 9-V input only 2 mA quiescent current there including the LED. Nice. And at 48-V that's only dropping down to 1.1 mA. And we'll just spot check the output cuz you don't want it actually precisely 5, believe it or not. And sure enough, 5.15 there. The reason you wanted a bit above is because uh so then uh when you've got like a cable drop, 40 dropping your cable going into whatever the thing you're pairing, then you're not starting out at 5 V. You're starting a bit above,

**Dave Jones:** so then you know, because most things are going to tolerate 5 V input plus minus 5%. So you don't want to go like to 5.25, but 5.15 output voltage is a reasonable compromise like that that then you can have you know, a bit of loss on your cable and no worries. This cute little thing is an isolated USB-C serial port. I like these. You should have um a few of these in your kit for a like interfacing with you know, I'm interfacing with like I do a teardown, I

**Dave Jones:** want to like interface with a serial port or something like that, then a little isolated jobby like this is very handy. So I'll put up the data sheets for these. I can't quite read them here, but that's obviously how USB to serial, very simple. And then we've got an opto-isolator here uh denoted by the uh silkscreen of of course. So these are completely isolated. Really nice. But of course you've got to supply power to the other side for the transceiver on this optocoupler side. So this positive and

**Dave Jones:** negative has to go to your um your device under test. And yep, yep, they are labeled there. Very nice. They've even put pads there so you can like solder on your own wires. That's thoughtful. I like that. It's upside down, so all the electrons are going to fall out. There you go. That's cute.

**Dave Jones:** That's the UART ISO-DPS. So thank you very much DPS, designed in Germany of course. These are cool little bits of kit including this. These are cheap as chips, they're only 21.90 euros including that. I couldn't quite get a price on this, but it's not going to be that expensive. So yeah, I'll link them in down below. Check them out. Thank you very much Zubax, zubax.com. You can scan that if you got one of those newfangled shoe phones. And they're from Estonia.

**Dave Jones:** Hi to all my viewers in Estonia. Um all I know about Estonia is that uh they offer like really cool like digital residences. Hmm, maybe I could become an Estonian resident. What do you reckon? Australia's going to hell. What have we got in here? Ah, let's open up. Ooh.

**Dave Jones:** Open uh Siffel? Sifel? Sifel? Um I don't know how to pronounce that. Anyway, it's open, is it? Got a cool sticker. Ooh, liking that. I do kind of sort of know what this is. I like the packaging here. That's really groovy. That's we've got a module thingy. Check that out. Ooh, look at that, potted. Ah, in red. Red potting compound. Ah, thing of beauty.

**Dave Jones:** It's a joy forever. It's a Zubax FG401MA. And some people might have guessed it already. What this is, it's an electromagnet thingy. So, you apply your voltage across here and boom, you've instantly um got a super powerful magnet to do whatever you want with. And I got these as well. This is a permalloy plate, of course. Doesn't stick at the moment, but uh she will once we apply here. And it looks like um this is a CAN interface thing. So, presumably, you know, you can control this

**Dave Jones:** uh via software somehow. Um so, this is 150 euros for the electro uh magnet. And by the way, it is not just like a coil and that's it, Bob's your uncle. It's more advanced than that. Um and the CAN interfaces they've got down 75 uh euros down here. And the plate is 28 euros for your permalloy plate. Um I didn't get any instructions, so I'm going to have to uh go download and um RTFM. But there is the hero shot. Look at that. Ah, I I

**Dave Jones:** just love the red potting compound and the red stand off on it. It just looks gorgeous. It really does. That's great. So, Zubax are a aerospace specialist manufacturer, and this is one of their products that is designed for like payload attachment for drones or for robotics or something like that.

**Dave Jones:** This can hold up to 20 kilos. Now, the interesting thing about this is that there's not just an electromagnet that you know you apply power to and then you know it's chewing all that power to get your magnetism. This will actually take zero power once you turn the magnet on.

**Dave Jones:** So, you know, you're not chewing that battery from your drone or your robot or whatever it is that's holding your payload. So, you can you know you can drop something from your drone. So, this can hold up to 20 kilos and then drop it via command without using any power except when it's changing state. And it can change state in like under a second.

**Dave Jones:** So, I'm not sure if we're actually going to get details about how this works. It might be you know it might be some proprietary tech in here. Have to do some research. They don't seem to have any specific technical details of exactly how they've implemented their design, but I'll put up the Wikipedia page for these electropermanent magnets as they're called, and that'll show you that they basically have two different types of permanent magnetic material soft and a hard one they're called. And by actually reversing, you know,

**Dave Jones:** flipping the polarity of a coil cuz they will have a coil in here. By flipping the polarity of the coil temporarily, you can actually either effectively enable or disable the electropermanent magnet. And so, it takes but once you've made that switch, the magnetism will stay there and it holds onto your payload and then it takes no power. And then you just provide a bit of current to flip the thing for you know a couple of seconds. This case I think this one's rated for 1 second. And then it releases

**Dave Jones:** your payload and uh your uncle. Very cool bits of kit. So, the cool thing about this is that as I said, it comes with uh this CAN interface here, but it also comes with uh this standard um RC uh as in remote control uh PWM uh interface as well. And uh there's like digital um control as well. And there's other bus compatible uh protocols and all sorts of things uh designed to actually drive this thing. So, we're just going to use the analog input here. So, uh just got

**Dave Jones:** uh 5 It operates from 5 V up to 40 V or something. I'll put up the maximum um specs here. But yeah, um then all we have to do is take this analog input and all we have to do is put a 5.1 K resistor either uh to positive, which should switch it on I think, or negative, which will uh switch it off.

**Dave Jones:** So, let's go ahead and uh then turn this on and you can see it's got a quiescent uh current there of about 27 mA. So, it's not it's not zero power, but the fact is uh the coil is not uh taking any power. So, you know, that's like bugger all there. And you can see we've got a little flashy flashy uh thing going on there. And you can read the manual. It's incredibly kind just the data sheet and slash manual incredibly comprehensive.

**Dave Jones:** It's got all the code and all sorts of things. Um yeah, it's they've really gone to town on this. It's really amazing. At the moment we've got the metal plate. It's not magnetic, okay? So, this will have up to 20 kilos um holding force. So, here we go. Watch the display here and it should take a surge of current for a second or two and let's switch it on. Let's see what it goes to.

**Dave Jones:** Boom. Oh, I'm hearing something went up to what point eight or something. I might have missed that, but yeah, about point eight amps and it dropped back down like that. So, this is now this should be permanently magnetized. I should not be able to pull Yep, I can't I can't pull that off, right? Maybe I can prize it off, but that's held there with 28 kilo 20 kilos um maximum weight handling uh capability on that thing.

**Dave Jones:** And as you can see, it's only drawing the quiescent power now. Very cool. So, now if I put it to negative, Oh, yep, there we go. 0.8 something like that. And it just I I don't know if you heard that crackling sort of sound like shh like yeah, there's actually a sound to it. But it started at 0.8 amps and then just went down like that. And now it should just play yep, it just lifts off like that. Cool bananas, huh? So, the it looks like there is a bit of residual

**Dave Jones:** stickiness there. But yeah, it's basically gone. Fantastic. Electro permanent magnets. Beautiful. So, let's go for a drop test, shall we? We've got multimeter attached to the plate. I've magnetized that sucker. So, and I can even turn the power off and it's still holding that meter. No worries. Let's turn it back on and demagnetize. Boom. Drop test complete.

**Dave Jones:** Winner winner, chicken dinner. So, that is super cool. Thank you very much Zubax for sending in that very interesting bit of kit, an electro permanent magnet. So, if you're into your drones or your automation, your robots or whatever, and you need electro permanent magnet that you can turn off and on that doesn't take you know huge amounts of power, these things are the ducks guts. This is very well implemented. I like it. It's quite reasonably priced at 150 euros, too.

**Dave Jones:** Check it out down below. have a mystery item. No idea who it's from because it just comes from a local re-shipper. So, not sure what the deal is. Let's go. What do we got? Okay. Well, it's protected good, whatever it is.

**Dave Jones:** It's a Why do we have a plug pack? Uh It's an Aussie one. Okay. I got no idea why I got that. I did not order that. It's a Qualcomm quick charge three. Handy, but Uh generic power adapter. It's got a model number on there, but I don't know. Like can't even do a teardown because they're destructive and well, what's the point?

**Dave Jones:** Okay, I don't get it. Oh, look, it's an old-school letter. Thank you very much Don Hall. I have a firm at the United States of America, Ohio. Hello Hi to all my viewers in Ohio. Yeah, what do we got?

**Dave Jones:** It's a duh Electreon driving roads. Why? While the ascent of electric vehicles is ongoing, the speed of adoption is at best unpredictable. Yeah, and they're dropping. One major hold up for consumers and commercial range anxiety. While developing networks away from roadways, it's okay. It's an article Uh yeah, in what magazine?

**Dave Jones:** Um Electreon's system. What about it? Oh, got some ads. Oh, wide flange boxes. There you go. Fantastic. Oh, okay, this is the wireless um right. Yes, I've done a video on the wireless uh road charging thing. No, it's It's a boondoggle. It's Well, it works, but it's not practical.

**Dave Jones:** It's like for widespread adoption in roads. It's never going to happen. I've done a video on I'll link it in here. Um and it was What was it? A $50 million boondoggle or something like that? Um they had some pilot program. Can't remember where it was. Don't think it was in Michigan. This This might be a different one, but yeah, I think it was similar. Yeah, and the Mdot um which is the Department of Transport.

**Dave Jones:** And yeah, they keep pouring money into this thing thinking it's going to be a thing. So, yeah, they got this pilot program in Michigan studying EVs. No. No. The only way it's possibly going to be of value is if you say had a taxi rank or something where where cars like sit for like extended periods of time sort of like, you know, guaranteed to sit for extended periods of time waiting for people. So, you know, if you had an EV taxi, for example, yes, the taxi rank you could actually install

**Dave Jones:** just a strip of these. It wouldn't cost much and yeah, and you know, they're not hugely efficient, but they do work. You can't be then you've got to, you know, chicken and egg thing. You've got to design it into the car to begin with and no one's going to design it into the car unless there's already existing infrastructure for it. So, you'd have to order special, you know, EV taxis that actually have this. Now, I'm not going to read you can read all this BS for

**Dave Jones:** yourself, but no, it wireless charging is not going to be a thing. I just noticed there's a note. Should have read the note first. Dr. Jones. I have enclosed an article from Electrical Contractor Magazine that you may find suspect. Solar roads again.

**Dave Jones:** Yeah, it's I am nearly retired EE in Ohio and I've always appreciated your content. Thank you, Don. I would love to see you and John Cadigan do an electric car collaboration. Yes, John Cadigan, a fellow Aussie YouTuber. I'll link in his channel down below. It's rather hilarious. If you like ockerism, Australian way of talk, then yeah, he's the guy for you and he does that car related videos. So, yeah. So, yeah, no is my official verdict on wireless freaking roadways. It's not going to be a thing except in very niche locations

**Dave Jones:** even for the electric buses. I've done the videos on the electric buses. There's just no point. Like even at the bus depot where you actually, you know, park the buses overnight. It's kind of pointless to even put them there because it's so easy. I've physically done it myself. Driven a bus in an electric bus into the depot, and I've physically plugged in the charger for it. It takes like seconds to do, and you get the most efficient transfer and fastest transfer possible.

**Dave Jones:** So, no, just no. No, it's just it's just silly. Only in niche applications will that work. So, oh, this looks exciting. On camera reaction material for hours of indulgent pleasure. Where does it come from? It comes from Australia.

**Dave Jones:** It comes from Brumby on the EV blog forum. So, let's rip it apart. I wanted to get the thicker ones, but the budget wouldn't allow. What the hell are these things? Reaction material. Hang on. Hang on. Here we go.

**Dave Jones:** Oh, no, I got to turn it up the other way. Right, I thought it might have been a magazine or something like that. But, hello. Sponge sponges. Sponge porn. Sponge porn. Oh my god. Where did he get these from?

**Dave Jones:** It's a sponge bonanza. I'll never run out of sponges. This is yeah, they're just generic one hung low brand. Oh. Hang on. Going to get Going to get the water. Okay, here we go. Sponge porn in 4K. I'm going to do it right here on the bench.

**Dave Jones:** Oh, will these BE ANY GOOD? OH, NO, THEY'RE A BIT PISS-WEAK. OH. That's not exciting at all. No. No, I give that I rate that maybe a four out of 10. Leave it in the comments down below. That's like that's like thin as.

**Dave Jones:** No. No, that's it's okay, but let's try two of them. Oh. It's hard to get through to the bottom one there. Yeah, no. No, I've seen way better sponge porn than that. Anyway, thanks Bramble. I'll never run out. Oh, no. It's a third sucker of the sav.

**Dave Jones:** Beelink. Beelink. Oh my goodness. They're back at it yet again. We've had Oh, navy blue this time. Yeah, these mini PCs, which I love, and we've had both an Intel jobby, like a high-end Intel jobby, and an AMD bloody Oh, it's a slidy thing. What's this one? This one is a Twin Lake N150.

**Dave Jones:** So, this is going to be much lower cost than the ones we've looked at previously. So, all I know is that it's the EQ series, but they've got like so many different variants of all their mini PCs, which is good and also bad because I have no idea and and the exact model of this thing until I actually get it out, and it should be on the bottom. These bloody hydraulic boxes.

**Dave Jones:** Here you go. It looks similar to the one we had before. The one we had before was an EQ, wasn't it? And very similar. So, is the teardown going to be identical? But yeah, the USB, the headphones, the USB-C. Yep, that's all identical. Yep.

**Dave Jones:** Yep. Yep. Everything's very handy with the integrated PSU and everything, but what model is it? Aha, the EQ14. All right, I'll go get a price on this one. So, this one is 230 Yankee bucks or so. That's like sort of like standard price. You have been able to get it cheaper during sales and things like that. So, this is a really low-cost super powerful PC using like a low-power jobby, 25 watts with the new N150 processor, but it can scale down and they've got I'll have to link it in down below.

**Dave Jones:** There's only so many things I can screenshots I can put in. They've got extensive data available on the website to show how how much power it takes, what temperature it gets to during all sorts of operations and stuff like that. And suffice to say these things are really super quiet and super low power. So, if you want a really low power application, these things are absolutely fantastic.

**Dave Jones:** Anyway, it's the same EQ series, but we won't see I'm sure we won't see the 80 watt power supply like we did in the previous one cuz this is only 25 watt max processor. Yeah, there you have it.

**Dave Jones:** We've got a smaller 48 watt power supply. So, yeah, kind of like halfish of what we had before. Once again, direct mains input, absolutely fantastic how you know, you don't need external power bricks or anything. Just whack the mains straight in and Bob's your uncle.

**Dave Jones:** We've got our IO interface board on top here. We've got our RAM comes standard with 16 GB here, which is very nice, not that 8 GB rubbish, and 500 GB solid state drive under here and you can see it under there. They've just got a There's a second slot. Yes, there is a second slot there. So, yeah, you can expand this thing really nicely. And there you have it there. Just unscrew that and got some thermal pads on the bottom there. And look at that. So, there is

**Dave Jones:** our of course that's our 500 gig. It's even unpopulated for 500 gig. Man, when I was a boy, 500 kilobytes was a lot. No one will ever need more than 640 kilobytes. Remember that, kiddies. Anyway, yeah, dual M.2 slots there, very nice.

**Dave Jones:** And yeah, they've only got the one slot there for the RAM, but that's a plenty. You might might be able to expand that if you want. 16 gig is like plenty for any application this thing's uh going to run, but you could possibly uh expand that, too. But, yeah, extra storage, and of course, you've got the uh dual gigabit um Ethernets on there. You've got the dual HDMIs built in. You've got three USB A's, very um handy. And uh you've got the USB C and another USB A

**Dave Jones:** on the front. So, plenty of IO capability. And as we've looked at previously, I've even measured the uh heatsink temperatures. Um it uh brings air in from the bottom. The thermals on these are very good and uh pumps it out here through the uh heatsink. So, rises up through. So, they know what they're doing when they thermally design these things. They're quite remarkable for the uh size, actually. And as I mentioned, the fan is whisper quiet. It's practically silent. It's like 32 dB maximum when you're like streaming 4K or

**Dave Jones:** something. I'll put a once again, they've got extensive measurements and data on this. Um and yeah, you basically don't know the thing's running. It's great. And booting it up, there you go. We're getting the Beelink logo-y thing. And it'll have Windows installed, I do believe. Windows 11. So, out of the box, it comes ready to go. You get the uh nice USB lead with it. You get the power mains figure-8 power cord and uh Windows installed, Windows 11. And Bob's your uncle. But of course, you can install

**Dave Jones:** Linux on it, whatever you want. Knock yourself out. I love how you don't have to dick around with licenses anymore. It just like everything just works. I'm sure Microsoft are getting their coin somehow. Okay, some power measurements. We've got 1 W in standby. That's all right. So, let's power it up. And we're booting up. 20-odd watts when it's booting up. And it's uh it's going to drop down to 11, is it? Yeah, it's jumping around. I'm not sure what Windows is doing there. It was below 11. Up, nine. There it is, 10

**Dave Jones:** W. So, I don't know. Whatever Windows is doing with its thing, that's the idle consumption. It's not much. Signed in to Marty McFly. Okay, we'll run CPU-ID on this, and uh then we'll bench it. Let's bench it again and that's jumping up to 20 20 watts now while it's benchmarking. So, it looks like that's going to be its maximum. So, that was going to be its maximum 20 there, but I don't know if we're going to get higher than that because if you go over here, it says that the maximum

**Dave Jones:** TDP is 6 watts here. Well, that's obviously wrong. So, yeah, I'm not sure where it's getting that from. You probably have to go into I don't know the energy settings in Windows 11. I don't know. I don't use Windows 11.

**Dave Jones:** Whatever. But anyway, it's low power. It's not like a high-powered beast jobbie like we saw in the previous two ones. I think the previous one was even more technically more powerful than my editing PC at the moment. So, yeah. But this is designed as a nice little low-power jobbie. Anyway, I'll put up some benchmarks here for the N100 processor. Remember, this is the new N150 Alder Lake one. So, it's even slightly more powerful again that I believe than the N100. But compare it with say a

**Dave Jones:** Raspberry Pi, it's more than like twice the power of a Raspberry Pi for single and multi-core stuff. So, yeah, nice little compact low-power solution. If you don't need a lot of grunt, but it's got all the IO that the other ones have in this EQ series. So, yeah, well worth a look. The price point is very competitive. I don't know if there's much better out there at this price point, but I don't know. I'm not Linus Tech Tips. So, thank you very much Beelink for sending this one in. Might

**Dave Jones:** find a use for it around here in the lab for some you know, embedded permanent application or something. But yeah, please don't send any more. That was the third suck of the sav. Anyway, Beelink PCs very cool, very well designed. I'll link them in down below and very cost competitive. I just love these small form factors. They're great. I'm going to uh, now got three of these things.

**Dave Jones:** I'm going to use them for a whole bunch of stuff.
