---
video_id: xQ3oJlt4GrI
title: EEVblog #1341 - AMAZING $250,000 IBM Processor TEARDOWN!
url: https://www.youtube.com/watch?v=xQ3oJlt4GrI
source: youtube-asr
timestamps: {"0": 0, "1": 28, "2": 48, "3": 69, "4": 84, "5": 102, "6": 123, "7": 139, "8": 152, "9": 168, "10": 184, "11": 198, "12": 210, "13": 225, "14": 241, "15": 257, "16": 270, "17": 285, "18": 301, "19": 314, "20": 331, "21": 353, "22": 364, "23": 378, "24": 394, "25": 422, "26": 442, "27": 459, "28": 476, "29": 493, "30": 510, "31": 524, "32": 538, "33": 558, "34": 575, "35": 591, "36": 606, "37": 621, "38": 633, "39": 658, "40": 675, "41": 691, "42": 714, "43": 729, "44": 746, "45": 761, "46": 774, "47": 794, "48": 810, "49": 830, "50": 844, "51": 864, "52": 881, "53": 898, "54": 917, "55": 931, "56": 950, "57": 961, "58": 974, "59": 991, "60": 1012, "61": 1028, "62": 1046, "63": 1066, "64": 1087, "65": 1106, "66": 1119, "67": 1138, "68": 1155, "69": 1173, "70": 1187, "71": 1212, "72": 1234, "73": 1249, "74": 1263, "75": 1286, "76": 1300, "77": 1318, "78": 1327, "79": 1346, "80": 1366, "81": 1380, "82": 1395, "83": 1413, "84": 1428, "85": 1446, "86": 1461, "87": 1476, "88": 1491, "89": 1508, "90": 1524, "91": 1537, "92": 1548, "93": 1564, "94": 1575, "95": 1589, "96": 1603, "97": 1617, "98": 1630, "99": 1644, "100": 1658, "101": 1676, "102": 1693, "103": 1703, "104": 1721, "105": 1740, "106": 1758, "107": 1769}
---

**Dave Jones:** Hi. That's not a processor. That's a processor. This bad boy is 600 watts power dissipation, 2,772 pins. Is that a socket? 2772? I guess it is. It's got 121 dies installed. It's 63 layers. It's liquid cooled. It's automatic. It's systematic.

**Dave Jones:** It's hydromatic. ULTRAMATIC. I COULD BE GREECE LIGHTNING. Thank you very much Jim Ranieri for sending this into the mailbag. I had to do a separate video for this. It's so cool. This is an IBM 9121 processor module which comes out of a

**Dave Jones:** system 390/ES9000, whatever you want to call it, parallel enterprise server from 1991. This thing beast. And we're going to tear it down. So, let's just toss this little pathetic thing away. Check it out. There's the date code there. You know, a

**Dave Jones:** second week 1991. I can't make heads or tails of the part numbers on this, but I do believe is an IBM 9129 processor out of a processor frame for a system 390 ES9000 server. It went under different names.

**Dave Jones:** It's kind of weird. If anyone knows the exact like story behind that, some people like they actually branded it system 390, other times they branded ES9000 or something apparently. And anyway, this is a state-of-the-art mainframe processor from the early 90s.

**Dave Jones:** Oh, and it's just Look at it. Oh, thing of beauty. It's a joy forever. Behold the Wankel mobile. Thing of beauty is a joy forever. We've got a gigantic ceramic substrate in here. As I said, 2,772 pins on this bad boy in a gigantic metal

**Dave Jones:** frame that weighs 2.2 kilos. Just the Just the processor module on each frame, like a physical frame. I'll try and find a photo of it. Actually had two of these processor modules, I believe. Back then, like it was a big deal. No, I didn't

**Dave Jones:** just crush the pins because it has like little tabs on the bottom. It's got like individually engraved numbers on it. So, I don't know, they tested and would have tested like and maybe characterized each individual one back then. And I found an

**Dave Jones:** old ad in a magazine back in the day that the IBM Twin 9121 processor system went for up to 1 and 1/2 million dollars. I don't think that was this actual just this module. It was probably only like a couple hundred dollars for

**Dave Jones:** this module. So, cheap as chips. This is 1991 dollars, too. None of this modern 2020 fiat currency rubbish. Now, this has around 20 mips or 20 million instructions per second. And as far as processors in the early 90s go, we're

**Dave Jones:** talking like an 80486 processor back then. I believe that came out in '89, but basically that was still like the top of the range processor. The highest speed version, the I believe the 50 megahertz of the 80486 ran at about

**Dave Jones:** double that. It was about 40 million instructions per second. So, this thing wasn't exactly state of the art in terms of mips processing power compared to desktop PCs of the day. But, you got to remember, this is a massive mainframe

**Dave Jones:** processor system designed for huge amounts of data processing and other stuff. And this could access up to 9 gig of memory per processor. That doesn't sound like a lot these days, right? 9 gig of memory. But, back in 1991, woah.

**Dave Jones:** This is heavy. And of course, heavy it is. As I said, this weighs 2.2 kilos just for the processor module itself. And this package is actually called a TCM or a thermal conduction module because it actually came in two types.

**Dave Jones:** Obviously, these pins, the 2,772 pins on it, they connected down to a matching socket in this thing. But these processors actually had a huge heat sink on top of them that weighed like 5 kilos or something like that. And I believe

**Dave Jones:** these came in like both air-cooled and water-cooled versions. And here's a picture of what one of those would have looked like. So, there were, as I said, two of these modules per physical frame they called it, which held the two

**Dave Jones:** processors and had all the wiring and another support stuff and the power supplies and the cooling infrastructure and things like that. So, yeah, this thing could dissipate up to 600 W. There's 121 chips or up to 121 chips and they can

**Dave Jones:** dissipate up to 10 W each for a maximum module power dissipation of 600 W. So, this little piss-ant thing. So, let's take this puppy apart. First, we get this frame off and check this out. Just notice this little tab on

**Dave Jones:** here. I reckon that is for a thermocouple to measure the temperature of this thing. Most likely, I'd be stunned if they weren't measuring the temperature of this thing. Look at all these screws to hold it down. I believe

**Dave Jones:** it is oil-filled inside, like the entire substrate filled with oil, and we'll see a whole bunch of heat SINKS AS WELL. OH, YEP. Can crack it. This could take a while. Yes, I do have an electric screwdriver, but not one that supports this tip.

**Dave Jones:** I just unscrewed the last screw. Damn, I didn't have the camera running and I heard this and like big O-ring seal in there. I don't know Can you I'm not sure if you can hear it. Hang on.

**Dave Jones:** Now, I'm just deciding which is the best orientation to lift this up from. Oh, I can see in the back. I'm having a peek. And I know that this will be the most impressive if I lift it up like this.

**Dave Jones:** Actually, I have to cut along there. So, sorry for all you purists out there, but we're going to void the void the warranty on this bad boy.

**Dave Jones:** A million voices just cry out in cry out in anger. All right, here we go. Are we ready? Rolling camera cuz I only get one take at this, I think.

**Dave Jones:** Look at that. Whoa! That is gorgeous. That is processor porn right there. Wow. Wow. Wow. Wow. Look at the individual copper heat sink slugs on each little chip inside there. And yes, there is a like a thin little layer of oil, but uh it

**Dave Jones:** hasn't oozed out or anything. You can see the O-ring seal around the edge there. Wow. That's just brilliant. Yes, they all have shifted. They all should be nice evenly uh spaced, but they're absolutely beautiful. And you can see that

**Dave Jones:** they all go into individual little uh machine slots in here, which by the way have little springs in them. Check that out. There's actually little springs inside each one of those. Not all of them are populated. There's some that

**Dave Jones:** actually don't have any uh heat sink slugs at all. But, yeah, it's little little springs down in there to keep the uh pressure keep the tension down on the uh the die. And you'll notice there that some of them just don't have uh dies

**Dave Jones:** installed in them. I don't know if that was like just an optional thing, but it looks like like the pattern is there. I'll show you a closer up later, but uh yeah, looks like the the die pattern is there, but uh anyway, these are like

**Dave Jones:** um flip chips. These are chip scale packages. So, they're you know, it's like from 1991. Whoa. So, you can see why this is called a TCM or thermal conduction module because it's all about the thermals. It's all about getting the

**Dave Jones:** heat out of each individual uh die on there, each individual chip. And as I said, each chip can dissipate up to 10 W. So, one of these uh copper solid copper slugs here, even though they don't actually have direct contact uh to

**Dave Jones:** this except on the sides, I guess their fit is if I can take Oh, yeah, yeah, yeah, their fit is very very not Oh, yeah, hang on. Here we go. Here's one of these copper slugs, and they just fit

**Dave Jones:** brilliantly. Now, I can see the oil the bubble oozing out, and look at that. Ah. I could play with that all day. Ah, that's just beautiful. Absolutely beautiful. So, yeah, they don't have Well, the mineral oil is going to be uh heat conductive as well.

**Dave Jones:** So, you know, it's like it's going to have an extra bit of uh thermal resistance in there, but anyway, that's how each one of those individual uh dies can uh dissipate up to 10 W with a maximum uh module dissipation of 600 W.

**Dave Jones:** It's just Ah, it's fantastic. There's some of the pattern on an unpopulated chip. Look at that. Wow. That's really something. And I know you want to know how many vias and what via hole sizes we've got on here. We're

**Dave Jones:** talking 78,500 of them and they're 100 microns a pop. Now, I'm actually going to get all of these heat sink slugs off here and I'm going to put them back over here. So, this could take a while. And they do

**Dave Jones:** have like a little noddy bit on the top, little nib on the top and that goes down into the spring just to uh center the spring on this thing. So, anyway, I'm going to stick them in and you know which ones actually

**Dave Jones:** which holes are populated because they've got springs in them. The ones that don't have springs, I won't put a copper slug in there cuz it might be hard to get out. Jeez, a lot of lot of suction on there. You've really got to

**Dave Jones:** get them off at an angle and uh Oh, and all those springs Yeah, but the springs will self-realign. So, that's nice. Obviously, the manufacturing process is not as messy as the disassembling process. This is ridiculous. What am I doing? So, I'm not sure what

**Dave Jones:** sort of mineral oil this is or what sort of oil. Seems some sort of mineral type oil. In the seismic industry, we used to use Isopar or Isopar M, I think it was. So, you can go look that one up and we

**Dave Jones:** had a license to use that with these gigantic tanks of it. Just filled with because it used to we we had one tank that was just filled with Isopar. That but that tank was wasn't just a tank, it

**Dave Jones:** was like part of the manufacturing these slippery little suckers part of the manufacturing process where we would put the outer skin onto a seismic streamer and so the outer outer poly put the kettle on skin was oh got to get the right way up

**Dave Jones:** it was yeah like extruded kind of for want of a better turn there's a little little something or other there little yeah it was like extruded out of this machine that was this big drum that was filled I'm talking bigger than a

**Dave Jones:** human size drum like 7 foot 8 foot tall or something and it was uh they would be extruded out of that and was just filled with isopar and we'd have isopar all over the floor and it was just it was yeah

**Dave Jones:** fun stuff okay that one doesn't have a spring so I'm going to do that one I missed it's only like four or five that DON'T HAVE SPRINGS OH oh yeah I've broken off are they like little bypass caps in there on the ceramics how

**Dave Jones:** would they like just come off like that there's a couple of them we'll have a look at those under the microscope but surely like I'm not putting much force on these at all so not sure why they just they wouldn't just fall off like

**Dave Jones:** that unless there's some sort of like they're not actually soldered down they're just there's another one there's another one right there and that cannot explain how unusually therapeutic this is yeah yeah I think I'm just breaking off all those little brown what look like

**Dave Jones:** caps but don't know unless I get them under the microscope and like that's all correct I got them all in the same I got them all in the correct order 1 2 3 4 5 6 unpopulated chippy and they

**Dave Jones:** didn't put the springs in and these are I don't know. But this is just so much fun. Oh boy. I wish this was feel the vision. Wow. Anyway, yeah. I've had some of these little chippy things come off like

**Dave Jones:** half a dozen of them. So, I'm not sure what the deal is. But I'm going to uh I'll just leave this gunked up and I'll just get some uh paper towels and wipe off all this cuz it'll be easier to see under the uh

**Dave Jones:** microscope and the macro lens um for the chip. So, I'll get back to you. Anyway, that is the module in glorious 4K without the with still with the mineral oil on it. And you'll notice that they're not all identical. Why aren't they all

**Dave Jones:** identical? Because these modules are supposed to contain uh SRAM chips as well. 128 K bit SRAM chips and I'm guessing that these are down here. Why are they kind of like oddball um sort of not really you know, symmetrically placed. I don't

**Dave Jones:** know. Um but anyway, like I assume that they're different types but even they're a different color slightly different color to those ones and I look, that could just be light refraction of the dyes because well, that's what dyes do. Pesky little things to look at

**Dave Jones:** and well, quite beautiful actually. You get them under the right uh light and they're they're quite spectacular but uh yeah, anyway, this is not just one module with like 121 different processors on it. It's got tons of different logic elements including 128 K

**Dave Jones:** bit SRAMs and that was that was pretty huge for '91 and they're 10 nanosecond access time SRAMs, too. Actually, it seems to be near impossible to just wipe this oil off. Yeah. Yeah, there's another one that Yeah, I can see the

**Dave Jones:** pads on the bottom of that chip. So, they're coming off. So, these are not soldered down. I reckon these are just Well, are they just press fit? Wow. That'll be interesting. Don't even know if soaking the whole thing in

**Dave Jones:** isopropyl do the job. Um cuz I Yeah, that oil's going to be hard to get rid of. Well, that's how you drop the frame out. Um I I just put it up here. So, to raise it up just so that I can take some

**Dave Jones:** macro photo shots. Over always uh my teardowns always usually always have uh high-res teardown photos over on my Flickr account. So, check that out. Um and this just And the whole thing just fell off. So, we're left with the

**Dave Jones:** ceramic substrate, which is pretty groovy, though. So, anyway, I'm really having some fun taking photos of all this at like different angles and stuff. It It really is just quite something. And I can, of course, adjust the iris

**Dave Jones:** F3.4. It's the lowest my camera will go at this zoom. If I increase our aperture, everything becomes in focus, or mostly.

**Dave Jones:** And let's check this out under the Tagano. And now, this is uh manufacturing material science at its absolute finest. It's like absolutely phenomenal. I'll link in the paper uh down below. You can read it for yourself talking about all of the uh construction

**Dave Jones:** technology that goes into this. But, we're talking about a uh 63-layer ceramic substrate here. As I said, 121 devices on here, 144 caps all in here. We'll take a look at those. Each chip has 648 pads on it. We'll check that out

**Dave Jones:** closer up. A mix of CMOS and bipolar technology devices, by the way. And there's 78,500 vias on this thing. I mean, it's just it's just absolutely incredible. And each chip there has 648 pads. And it's This is not a PCB, okay?

**Dave Jones:** This is a ceramic substrate with a mixture of thin film and thick film hybrid layer technology. So, I believe the top layer is thin film printed and the inner layers are thick film printed. Now, those 63 layers .2 mm, that's 7.8 thou

**Dave Jones:** thickness each. We're talking about 12 micron conductors. That's like half a thou. Half a thou conductors on this thing. So, yeah. It's just it's just absolutely nuts. And the top ceramic surface layer has a surface flatness of 5 microns. So,

**Dave Jones:** all the mechanical engineers out there probably getting moist over that. I don't know. Let me know. Is that good or not? 5 micron flatness over this entire module. So, the ceramic substrate here is made with the mixture of alumina

**Dave Jones:** powder, glass powder, organic binder, and plasticizers, and all sorts of stuff. So, you know, really just incredible material science involved in this. Just, you know, the manufacture of this board. Anyway, you can see the capacitors down here. And we Let's find

**Dave Jones:** one that's ripped off, cuz I did rip off a few. There we go. There's the little pad for the capacitor down there. And yep, I can feel that. Oh, look at that. Look at that. The solder, I'm going to use that term

**Dave Jones:** in quote marks, the solder Look at how I can just like this has not been heated up at all. So, they're obviously using some sort of you know, weird ass metallurgy here for the solder on these things. I'm going to assume that it's

**Dave Jones:** the same for the chips as well. But there for the capacitor There there's the capacitors, okay? I'm going to try and get this off, okay? I'm going to put a little bit of force on that. Turn at the right angle.

**Dave Jones:** Yeah. Yeah. She's budging. Yeah. There it is. There it is. Have you ever taken off a chip with that sort of ease? Oh, this is just this is magical. This is a and floating around in oil. Oh, this is my favorite thing ever.

**Dave Jones:** This is just incredible. A floating oil A capacitor floating with oil. Oh my goodness. Which you can just imagine being able to take off chips with that sort of ease. Oh, Louis Rossmann, eat your heart out. Okay, people are going to be horrified,

**Dave Jones:** but I'm going to try and do this with one of the chips. Oh, people are going to be more I mean, we've got Uh like hundreds more pads on here. Hundreds and hundreds of more pads. But let's see.

**Dave Jones:** Oh, now I'm putting a lot of force on that. Oh, I'm putting all my hand slipping. Don't you hate it when your hand slips due to the oil? Geez. Yeah, I can't I can't make that budge. But certainly,

**Dave Jones:** the capacitors piece of cake. They just go off like that. Oh, good. This is so much fun. Oh. This is great. Let's flip the There's our cap. There you go. We flipped our cap over and there it is. 16 pad capacitor, which

**Dave Jones:** looks like it contains, because we saw the top of it over here, does it contain four individual caps like that, perhaps? I don't know. Anyway, you can see that they're just like There's no no no traces coming off there. They're just

**Dave Jones:** buggering off down in the internal layers, and you can't see through these layers because they're like ceramic. There is a ceramic slurry substrate, and as I said, like individual vias down in there, we're talking 100 micron holes. Um

**Dave Jones:** and these are all, you know, like I don't know, test pads. Not sure what the deal is. I assume, you know, some sort of test pads. Something like that. I'm never going to get this oil off. I'm I'm

**Dave Jones:** not even going to try. I'm already starting to get oil over everything here, so yeah. But anyway, this is absolutely remarkable. We've got 648 pin. So, I guess you could call that BGA. Although, you know, they wouldn't have

**Dave Jones:** used that term back in the day, I don't think. And the inner layers, apparently, are made of a moly molybdenum, if I'm pronouncing that correctly, molybdenum powder. So, yeah, this is not These are not like copper exposed etched PCBs.

**Dave Jones:** This is not what's happening here. This is an entirely different technology to what you're used to with your fiberglass circuit boards. It's just yeah, it's not the same thing. All right, I'm going to get medieval on its ass. I'm going to

**Dave Jones:** get Get in there with a big pair of pliers. Oh, sorry. This is going to flame comment down below. Go ahead. I don't care. I'm I'm going to going to give that a little uh going to give that a little twisty. Last

**Dave Jones:** pretty straight without twisties. Oh, yeah, yeah, yeah. NO? UH OH, OH, NO. I'VE COME A GUTSER. LOOK AT THAT. But at least we can see under it. We can see under it, so that's useful. Here you go. Wow. Okay. Yeah, you can

**Dave Jones:** see a similar similar thing to the caps in there. You can see the individual solder pads. Once again, I look, I'm going to clear this away. Yeah. Yeah, look. Look, you can see the solder. Yeah, it's the same

**Dave Jones:** thing. It just spreads like that. So, this is not your regular solder that you are used to. Cuz this is room temperature here. This has not been heated up. Wow. So, yeah, we just completely shattered that die. Just absolutely

**Dave Jones:** butchered it. Sorry about that, but that's fascinating to see under that and confirm that it's basically the same interconnection uh technology as what the is what was under the capacitor there, which makes sense, of course. So, is this some Doug Henning

**Dave Jones:** metallurgical magic? Well, I don't think so. I had a look at the document, and it actually specifies, yes, it's solder, and it specifies it as 97/3 solder. So, not that 60/40 rubbish, but yeah, 97/3. It's not some magic room

**Dave Jones:** temperature solder or something like that. Um so, I've got to assume that's what's here. So, why does it seem to wipe off like that? Well, I can actually This is not feel-a-vision, but I can actually feel the bumps in there. What's actually

**Dave Jones:** happening here, and why I was able to um magically use the Jones method for desoldering this chip, just push it right off, is because of the tiny pitch and the tiny amount of solder that we've got here. We're talking 16 pads here, but

**Dave Jones:** these are pad dimensions I checked are only 180 microns wide. So, that's like 7,000 wide pads on here. So, there's practically no solder on there. These aren't balls on the bottom of the chip, right? These are just like they've just

**Dave Jones:** applied the solder paste, however they apply it, and they've reflowed it, you know, in a not too dissimilar manner to what you're used to, but there's just so it's such a tiny little pea sized amount of solder on there that the sheer force

**Dave Jones:** of that just my force was enough to just break all of those pads at once. There's only 16. I guess the mechanical engineers out there, please, you can you know, if you can do a like a some sort

**Dave Jones:** of shear analysis or something. I'm probably not using the right terminology, but anyway, with 180 micron wide 97/3 solder, you'll probably find that yeah, you can just push these chips off with a bit of force. Now, why don't the pads

**Dave Jones:** rip off? Because this was what would happen if you tried this at home. Don't try it at home, kitties. You'll the pads will just rip right off a regular fiberglass board, even though like the real high quality high

**Dave Jones:** temperature ones most likely, because you know, a tiny little 7,000 pad in there, 180 micron pad size, there's going to be virtually no adhesive under there. Although, it might not come off because you've got the via in the

**Dave Jones:** middle, but I don't anyway. If you relied on a tiny little pad like that, there'd be virtually no like adhesive on there to hold those pads in place, and you'd just shear them all off. You'd completely come a cropper, and

**Dave Jones:** yeah, do not try the Jones method for desoldering your BGA parts, cuz it's not going to work. And look over here, we haven't ripped off a single pad. Why is that? It's because well, this is like, you know, this is what you get when you

**Dave Jones:** pay, you know, like a hundred thousand dollars. This is like, you know, the best that the IBM research scientist can come up with. This is, you know, it's not just regular fiberglass. This is like, you know, some ceramic woo-woo mixture of

**Dave Jones:** stuff and it's all just embedded in there and these pads are they're they're probably never coming off. I put a lot of force on that. Anyway, that'd be fantastic if you could repair chips like that, but unfortunately, yeah, don't try it on anything but IBM

**Dave Jones:** magic woo-woo. So, I mentioned this document and I won't go through it. I'll just link it in down below, but it's done by J. U. Knickerbocker. Winning name and friends, of course. And it's basically them they're a bunch of,

**Dave Jones:** IBM research scientists, it's basically them boasting about all this marvelous technology that they've got in these, you know, ceramic modules in the construction of them and everything. And it's highly recommended, worth a read. Absolutely fantastic. So, just think of the people that went into

**Dave Jones:** actually making this thing and the technologies involved in manufacturing this. And they're thanking these various side divisions within IBM for doing it. Anyway, J. U. Knickerbocker apparently had a distinguished career at IBM. Don't know where he is now. They published like 90

**Dave Jones:** papers or something. I had a look. Impressive. So, there you go. I hope you enjoyed that as much as I did and I've got oil all over my fingers and Thank you very much, Jim, for sending this in.

**Dave Jones:** This was absolutely pornographic technology. Absolutely fantastic. I'd love to like maybe, you know, like x-ray this or something like that. I don't know what we see. You just see 63 layers of interconnections and stuff like that under here. So, it's got 400 m of wiring

**Dave Jones:** inside this, by the way, for those wondering. Which doesn't sound like a lot, but you know, I guess it is when you stretch it all out. Anyway, um yeah, 63 layers of state-of-the-art ceramic PCB manufacturing technology from 1991.

**Dave Jones:** Absolutely incredible. And this had like half the number of MIPS as an 805 486 at the time. Um, but as I said, you know, it's you're not comparing apples to apples there. So, wow. Um, that's absolutely incredible. Hope you enjoyed that as

**Dave Jones:** much as I did. If you did, please give it a big a thumbs up. And as always, you can discuss down below or over on the EEVblog forum or over on any all of the alternative platforms that I'm on. And

**Dave Jones:** I'm also on the Twitters, I'm on the Instagrams, I'm on the Flickers. I'm everywhere. Catch you next time.
