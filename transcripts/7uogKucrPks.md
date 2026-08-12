---
video_id: 7uogKucrPks
title: EEVblog #948 - Nixie Tube Display Project - Part 1
url: https://www.youtube.com/watch?v=7uogKucrPks
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 27, "3": 41, "4": 54, "5": 67, "6": 78, "7": 90, "8": 102, "9": 116, "10": 135, "11": 147, "12": 161, "13": 176, "14": 191, "15": 203, "16": 216, "17": 226, "18": 238, "19": 256, "20": 269, "21": 285, "22": 301, "23": 313, "24": 324, "25": 338, "26": 353, "27": 368, "28": 383, "29": 400, "30": 413, "31": 427, "32": 440, "33": 454, "34": 469, "35": 487, "36": 499, "37": 513, "38": 524, "39": 538, "40": 550, "41": 569, "42": 586, "43": 600, "44": 610, "45": 626, "46": 641, "47": 655, "48": 669, "49": 684, "50": 699, "51": 713, "52": 727, "53": 736, "54": 750, "55": 763, "56": 782, "57": 795, "58": 807, "59": 823, "60": 838, "61": 853, "62": 867, "63": 881, "64": 896, "65": 914, "66": 928, "67": 941, "68": 955, "69": 967, "70": 980, "71": 994, "72": 1008, "73": 1022, "74": 1039, "75": 1054, "76": 1069, "77": 1082, "78": 1093, "79": 1108, "80": 1122, "81": 1135, "82": 1150, "83": 1160, "84": 1178, "85": 1190, "86": 1205, "87": 1218, "88": 1233, "89": 1249, "90": 1267, "91": 1288, "92": 1307, "93": 1321, "94": 1336, "95": 1355, "96": 1367, "97": 1381, "98": 1396, "99": 1416, "100": 1432, "101": 1446, "102": 1463, "103": 1480, "104": 1497, "105": 1512, "106": 1529, "107": 1546, "108": 1559, "109": 1573, "110": 1587, "111": 1604, "112": 1620, "113": 1638, "114": 1654, "115": 1664, "116": 1680, "117": 1697, "118": 1717, "119": 1729, "120": 1744, "121": 1757}
---

**Dave Jones:** Hi, in the previous mail bag video Robert Bruce sent in eight of these very nice Russian Nixie tubes and I love Nixie tubes. They're fantastic. Look, I've got them all lit up here. They're all working and I mentioned in the mail

**Dave Jones:** bag I might do a project with it. Well, let's give it a burl. And these are the Russian B model actually has the decimal point in here. So we can have an eight digits counter with decimal point anywhere. This is going to be great and

**Dave Jones:** Robert kindly sent in the original Russian data sheet for this thing cuz I don't think there's any English data sheets available though I could be wrong. This is basically the sorry I can't pronounce these in Russian but they're

**Dave Jones:** generally known as the IN-12 series Nixie tube. In this case there's an A and a B model. You can see we've got the B model there. So the B model actually has pin 12 connected here which is the

**Dave Jones:** decimal point that we saw before. And these come in different types. You might have seen the vertical ones that look like tubes, you know, old fashioned tubes with the pins all in the bottom. I much prefer these ones. These are much

**Dave Jones:** nicer cuz you mount these directly on a PCB like that and be mounted. Well, it depends whether or not you want right angle. The others are good for right angle. These are good for the application that I've got in mind for

**Dave Jones:** this thing which you'll see in a future video. I won't tell you what it is yet but basically we're going to have an eight digit counter display. So let's take a close up view of this. If you haven't seen one before. We've got our

**Dave Jones:** nipple on the bottom. Love the nipple and that keeps the vacuum inside these things. These things are vacuum sealed. So if you're making a PCB cut out of course you can't just snap that off. Just don't come along with your side

**Dave Jones:** cutters and break it off. You got to drill a hole in and have that sitting inside your board. And what it basically is is a cold cathode display cuz there's no heater in this thing unlike valves. So it doesn't work by way of the

**Dave Jones:** thermionic emission like valves do and you can see that there's various levels inside there. They're all separated with these ceramic spaces in there like that and each one is a metal digit. You can see all the different digits. So it's got all the different

**Dave Jones:** numbers in there. It's got you know a zero through to nine and plus the decimal point as well. So and they're all wired in. You can see them going in there like that and they are just a metal

**Dave Jones:** outline of the digit that you want displayed and you can see a metal mesh in here like this in the front. That is actually the anode. You apply your positive voltage to that. You apply your negative voltage to any one of the other

**Dave Jones:** digit cathode plates in there and they'll start to glow if you give them enough voltage and current. And the way they glow is they're basically neon type lamps. You can think of them as that. The gas in there is usually mostly neon

**Dave Jones:** but it has some mercury and possibly some argon as well in there and basically the cathode i.e. the digit that you're displaying when you apply a potential between the anode grid and that, the actual cathode digit will get

**Dave Jones:** a nice glow around them. In this case a beautiful orange that you saw before. And I hook it up to my high voltage power supply through a dropper resistor and you can see we've got the digit eight lit up there and it's just one

**Dave Jones:** digit. So unlike a seven segment display, it's not made up of segments. You've just got one segment shaped like the number eight. And in this case here we've got the number two and you can see that in there even though

**Dave Jones:** if you have a look inside number two is all the way back there so that digit is all the way back there. It's got all those digits in front of it but you can still see it because it's basically

**Dave Jones:** glowing and you can see the glow around the other digits and through the mesh. Now if we take a look at the data sheet, please forgive my Russian, but you don't need to know Russian. Usually, it's, you know, fairly obvious

**Dave Jones:** because the numbers and units are pretty universal. We're talking 170 V here. This would be a nominal voltage. 2.5 mA could be a nominal current or could be a maximum current, not entirely sure. And then 0.3 mA here, well, that would

**Dave Jones:** be the minimum sustaining current to keep the thing on once you've turned it on. And that's all we really need to know. They've got a few more down here. This 200 here is probably the absolute maximum voltage. 120 to 170, that would

**Dave Jones:** be the sustaining voltage range there. And 2 to 3.5, well, maybe that's the Maybe that's the maximum with 0.7 average. Let's try and translate. And we mostly got that right by the looks of it using Google Translate here.

**Dave Jones:** No more than 170 indications for current figures. Yeah, at the 100 degrees that we had there, that was the viewing angle. 120 to 170 sustain discharge. There you go, they actually got the word sustain in there. 2 to 3.5 for digits

**Dave Jones:** for the decimal point, no more than 0.7 operating current average. So, the digits are higher than the decimal point. So, if you're going to use the decimal point, you actually want to use that at a lower current, presumably.

**Dave Jones:** But that's all you need to know, voltage and current. By the way, it's real easy to find pin one. It's the white one there. There you go, dead giveaway. Okay, I'll show you what I've got set up here. I've got my high

**Dave Jones:** voltage power supply set to 170 V here. I'm just measuring the current, and I've got my decade resistance box here so that we can adjust the current of the dropper resistor effectively cuz in the final design, we're going to need a

**Dave Jones:** dropper resistor. And I've got a 20 K resistor in there. 1.67 mA, it works just fine, and it switches on just fine. There will be slight discrepancies, of course, between different tubes. And I've got fixed exposure on the camera,

**Dave Jones:** so you'll be able to see the absolute change in the brightness there. So, 1.67 milliamps, let's actually dial um that you can see back to 10k. So, 2.75 milliamps. There's a difference there, but let's whack in Let's go up to

**Dave Jones:** 120k there. Yeah, well, 100k. There you go, and it's still on. It's still on at 0.4 milliamps, but will it start up at that? So, I'll switch it off. And yep, it still starts up at that. But, let's

**Dave Jones:** go to say 200k. Oh, it's still on 0.3. That was below the data sheet value, wasn't it? 0.2 now. It's still just on. So, it's holding in there, but I don't suspect it'll START UP. AH, NO, we're lucky. Oh,

**Dave Jones:** it's our lucky day. Go and buy a lotto ticket. 0.4 milliamps, let's actually dial up that voltage. We can see if we go up to 200 volts, it gets brighter. If we go down 160, it's still sustaining that. But, you might be able to see

**Dave Jones:** actually not all of it, only partial part of that digit is actually glowing. So, yeah, I don't think that one's going to start up. And of course, it makes a fool out of me, doesn't it? Damn it. But, let's go back to seven digits here.

**Dave Jones:** I won't bother wiring that one back in. And I've got 140 volts with 10k in there. Will it start up? And I basically only got the one dropper resistor for all of them. So, you wouldn't do that in practice, but let's

**Dave Jones:** see if any of them start up. Two of them. Two of them got there, and sometimes you actually see them come on later. But, let's wind our voltage up there. There you go, our decimal point came on. Another digit came on as we go up. So,

**Dave Jones:** as I said, there's going to be slight discrepancies between those. So, but let's drop it back down to 10k. 12 milliamps for all of them, that's pretty good. That's still within ballpark and they're all on. No worries whatsoever. So, we can

**Dave Jones:** turn that voltage down and we're still sustaining at just at 130 volts. Really drops between 130 and 140 and then boom, it's off. And there we go, it doesn't switch immediately all back on. So, there's some threshold there that some of them

**Dave Jones:** are not meeting. They just slight discrepancies between the tubes. So, that's cool. Now, we can design our circuit driving these puppies. Let's go. The first thing we're going to need is a high voltage power supply and Robert was

**Dave Jones:** kind enough to send in this little kit, which I'll link in it down below and there's tons of these on various websites and eBay. You can just buy Nixie high voltage Nixie tube driver kits. Most of them like 9 to 12 volts

**Dave Jones:** input. I was going to power this whole thing by 5 volts, but yeah, I you know, I don't want to go roll my own high voltage power supply. I just I just want to get this thing done. So, I've got

**Dave Jones:** this in hand. I'm going to use this. This is a 12 volt input to a selectable voltage output. It'll do 170 volts. It'll do 5 watts for this particular one and that's 29 milliamps capability at 170 volts. More than enough to drive our

**Dave Jones:** eight digits here if we only need, you know, a couple of milliamps each. No worries. And the good thing about that is it's just got a header on there. We can boom, solder that directly just, you know, flat down onto our board. No

**Dave Jones:** worries. Could mount vertically, but in my case, I'm going to mount it horizontally like that. So, no worries. It'll work a treat.

**Dave Jones:** There we go. Bit of a goof on the layout of the cap and the inductor there, the spacing on that. I'll get a vertical uh header for that. Um, no, that transistor is not missing. It's actually there. That's an IRF uh 2 IRDF uh 220 in the um

**Dave Jones:** four-pin DIP package there, so no worries. Um, I uh height-wise it's okay. Maybe I could have uh bent a couple of the parts over to get a lower height profile, but it should be okay for my purpose. And just a little tip with uh

**Dave Jones:** pin headers like this, you can put them in a little breadboard just to hold them in place to stop them wiggling around if you haven't done the uh hole size thing to make them uh press fit in there uh

**Dave Jones:** like this one hasn't, so that'll work a treat. And we feed 12 V in and she works a treat. Almost bang on. There's a 680 ohm uh external resistor. No touchy. It's 170 V and uh that sets your uh output

**Dave Jones:** voltage. So, yeah. Beauty. But I know what you're thinking. Will it power an array of Nixies? I've only got seven. I haven't got eight, but uh near enough. And bingo, there we go. It's drawing uh 5.6 W or 24 mA.

**Dave Jones:** Now, let's have a look at Dave Cam for a minute. Uh we've got our 170 V anode power supply. By experiment, around about 22 K should do it for a single uh display. And then for multiple uh displays along here, then you would have

**Dave Jones:** a separate resistor going up like that. You'd have another 22 K like that. And because only one segment uh one It's not a seven-segment display. Only one digit is on at any one time, you don't have to worry about uh sharing

**Dave Jones:** current through the different segments like you would if you had a traditional seven-segment display here powered through a single resistor, a single dropper resistor. And the other difference between driving a traditional seven-segment display is it's in the name, seven segments. You would have

**Dave Jones:** seven drive lines coming in like this for the seven different segments of your display. But because this is a uh digit-based display, we to do zero uh to nine, we need 10 separate lines or 11 if we want uh one for the decimal

**Dave Jones:** point as well. So, that rules out our driver chip being your traditional BCD to seven-segment display driver cuz this is not a seven-segment display. So, we basically want like a latched uh shift register type thing coming in so that,

**Dave Jones:** you know, we've got a uh clock line coming in here like this and then a latch line coming in as well and then it shifts the digits cuz you don't want um all of your outputs to uh uh change like

**Dave Jones:** in sequence as you shift the data through like this. You don't want to see that. So, you want to have an internal latch. So, you clock it in and clock the data in that you want to display and

**Dave Jones:** then uh hit the latch, strobe the latch light, and that'll transfer the data, boom, all over and display the digit you want. But, of course, the problem is the 170 V up here. Um so, that means that uh

**Dave Jones:** this chip has to have a 170 V say, you know, round it to 200 V capability. It's got to be a high voltage output driver. And of course, it can't be a totem pole output. It's got to be a

**Dave Jones:** open collector output like that. So, or an open drain if it's a MOSFET, whatever. Um so, we need individual high voltage driver transistors driving each one of these digit lines. And if we've got 10 of them * eight digits, we've got 80 drive lines

**Dave Jones:** at least. But, if we include decimal points, we've got 88. Love 88. We're going to see some serious Now, of course, you could should be saying, "Oh, Dave, you can multiplex the things. You only need the one driver

**Dave Jones:** chip and then all the lines would be common like this and then we can uh install a transistor up on the high side here to uh drive each one." And you can multiplex it and yeah, no worries. You

**Dave Jones:** can multiplex Nixie uh displays like this. They're fast enough to handle it. Now, that would work a treat except for the fact that uh your driver chip that drives the base of this puppy also has to be a high voltage output driver. So,

**Dave Jones:** you'd need another high voltage transistor here NPN to actually uh drive this high voltage transistor. So, if you did that, you'd still need a two transistor solution for each of your eight segments. So, yeah, I could multiplex this display, but you're going

**Dave Jones:** to have higher peak currents. It's going to be dimmer. It's a bit of an unknown. It's sticking around. And I I don't think I'll do it. I think I'll just go for a direct drive solution. So, I need like a huge number of driver

**Dave Jones:** chippies like this. Uh effectively, if I could find one that had 10 outputs, one to drive each individual display like this. And there is an old uh 7400 series TTL chip that's designed with high voltage open collector outputs designed

**Dave Jones:** for driving Nixie tubes, but um it's obsolete now. I don't even think you can buy it. It's not available in LS or HC or any of the other families. It's 74. I think it's the 74141, is it? Um and

**Dave Jones:** yeah, no. We'll find another solution. So, of course, one easy solution is we can just get shift registers, you know, 74HC uh 259s or something like that. Whatever your favorite latched uh shift register solution is, and then we can

**Dave Jones:** just power external high voltage transistors like that. But you need 10 of them. So, we're going to look at we would need um 80 Let's say 88 external you've got to solder those all on the board. And no, that's not

**Dave Jones:** fun. So, yeah, maybe, you know, that's the easy That's the jelly bean solution. Um but we'll see if we can find an off-the-shelf chip to do it. If we can't find uh a suitable off the shelf solution that's readily available at a

**Dave Jones:** reasonable cost, then we'll go for the external transistors. But I'm just sort of like reducing external parts count by trying to do that because we don't need, if we find a direct solution like this, we don't need the external resistors, so

**Dave Jones:** we save 88 resistors in our circuit. We don't need the 88 transistors as well. And because we've only got the one dropper up here per display. So I like the direct drive solution. You get a known constant brightness. You don't

**Dave Jones:** have to dick around with multiplexing and all that sort of stuff. But multiplexing, if you're really short on space and everything else, maybe you'd use a multiplex solution. But I'm going to go for the direct drive. Now, if you

**Dave Jones:** were going for an external transistor solution, as I said, it's got to be a high voltage transistor, so you can't just use some sort of jelly bean thing like a 2222, for example. It's only got 40 volts collector emitter voltage. For

**Dave Jones:** example, you can't use like a classic BC547. That's, you know, it's better, but you know, it's still not going to do the business. We need a high voltage transistor, so let's do a parametric search. So that's pretty easy. You just

**Dave Jones:** go into your parametric search engine of your choice. I'm going to use Digi-Key here. I'm in discrete BJT transistors. I'm not going to look at MOSFETs, nice hardy BJTs. We want an NPN, of course. So we're going to fill apply filter.

**Dave Jones:** We've still got 9,000 or something of those. And then we're going to do the collector emitter breakdown voltage. Boom, boom, boom. Let's say 200 volts and above. I mean, you know, now we're getting like we don't really want a

**Dave Jones:** massive voltage up there. I mean, you could go right up to 1,200 volts, but we're talking about, you know, ridiculous sort of transistor. So I'm going to just go say 200 to 400 for argument's sake here. We go in there, and here we go. FMMT458.

**Dave Jones:** If you want a, uh, surface mount jobbie, BST39s, and of course you can, um, sort by your, uh, breakdown voltage here, no worries whatsoever. And, or you can choose, you know, if you wanted a through-hole solution, you'd go for a

**Dave Jones:** through-hole. Ah, yes, nice. Uh, SOT223 package there, one of my favorites. Um, they're just like really nice to solder. I just enjoy soldering those. Anyway, um, yeah, there's no shortage of high voltage transistors to choose from. But, of course, if you wanted to find, you

**Dave Jones:** know, what is the jelly bean, uh, one, then generally, uh, sort by price is probably going to get that for you, you know, 2 cents a pop. There you go. Um, 2.6 cents. But, that is in, uh, 10,000

**Dave Jones:** quantity. But, yeah, there's no shortage of Oh, there's a through-hole, a 2N6517. Oh. So, just pick out a data sheet for a couple of these, and any of these will do the job. This is the 2.6 cent job.

**Dave Jones:** There we go, you know, 300 volts, and, uh, collector base voltage, 300 volts, 200 volts. Yeah, no problems whatsoever. The, uh, 458 series here available in, uh, either a SOT, uh, 23, which is really nice and small. Uh, just be

**Dave Jones:** careful of the, uh, you know, having your traces, uh, too close at high voltages on your PCB and stuff like that. Just watch your clearances. Or, the, uh, SOT223 package as well. And, it's, um, these are all going to do the business. 400

**Dave Jones:** volts, no worries. Now, if you were going to go for the external, uh, transistor solution, then you would need a, well, you would like to have a one of 10, uh, decoder. Um, in this case, here's the 74, uh, 141, which

**Dave Jones:** is now a completely obsolete. And, this one does have the built-in, uh, driver transistors for the Nixie tube, uh, display here. And, a one of, uh, 10 decoder is basically just, um, a four, uh, binary inputs here, and it turns on

**Dave Jones:** one of 10 outputs. And, that's exactly what you want, cuz you don't want any It's not a seven-segment display. It's not like you're going to have two outputs on at the same time. Now, you know, you can go in and search Digi-Key.

**Dave Jones:** I just actually search for one of 10 decoder. And you know, and up come the usual 4,000 and 7400 series ones, but none of these, because they're obsolete, none of these are high-voltage jobbies, I don't believe. So, we're barking up the wrong tree

**Dave Jones:** there. Now, as I mentioned before, a good solution for this might be shift registers, for example. That's the one I'm looking at. So, you go into logic and shift register category, and bingo, what pops up first? Well, the classic

**Dave Jones:** jelly bean 74HC595. But of course, they you'd need external wire drive transistors, external resistors for that. And you know, hey, you could do that. Choose any flavor. But I think that if we go in here, and let's try and find

**Dave Jones:** one with open collector outputs, and maybe we'll get lucky and find one that actually has a high-voltage open collector output. So, here's the output type. You don't want complementary differential, all that sort of stuff. You don't want to push-pull, your totem

**Dave Jones:** pole output. Nope, you want open collector. And of course, you can go for open drain as well. Hang on, how much does that give us? Number up here, one one remaining. And if we go open drain, that gives us 174. Okay. So, let's apply

**Dave Jones:** our filter there. And let's have a look down here. Um TI 8-bit shift register. Once again, like an 8-bit one, you'd need multiple chips. One chip couldn't handle just one display, cuz we've got 10 lines. And so, what we want is probably the larger

**Dave Jones:** packages, and they're going to be more specifically designed for driving large numbers of things like this. So, I This I think there's more chance of there being a high-voltage one in there. So, let's go from like 20-pin DIP upwards, shall we? So, let's let's

**Dave Jones:** just filter out all the smaller stuff and let's take a look at what we've got. Hello. This is what I'm looking for. Anything with HV in the number. HV stands for high voltage and Microchip. Um that's Microchip. That can't be

**Dave Jones:** traditional Microchip. That's got to be one of the companies Microchip bought. So, we can go in and have a look, but look, 220 volts. Bingo. 32-bit serial to parallel shift register. They're available. 5 bucks 67. You know, they're a little bit

**Dave Jones:** little bit pricey, but you know, it's a one-off. We've only got a few of them. They've got 200 in stock. They're in a 44-pin QFP package. Here we go. No, it is branded Microchip. So, there you go. I don't know if they were Yeah, they

**Dave Jones:** probably got that technology from some company they bought. Would be my guess. Anyway, high voltage low low voltage serial to high voltage parallel converters with open drain outputs. Primarily designed for use as a driver for electroluminescent displays. Can

**Dave Jones:** also be used to require multiple high voltage current sinking capabilities. Inkjets, plasma, vacuum fluorescent or large matrix LCD. This is exactly what we want. Here we go. Data input, clock, strobe, output enable. Aha, this is not a latched one. So, we don't want

**Dave Jones:** this. We want a latched type. Cuz if we try and shift data in there, you've got multiple chips, then you'd actually see these things updating on the display. You don't want that. You want to shift the data in and then latch it. Boom, all

**Dave Jones:** at once across all the displays. So, let's have a look at another Microchip one. This is a 32-bit. And if we open this, bingo, it's a Supertex. So, this is where they got these from. They just haven't changed the data sheet to what

**Dave Jones:** Microchip yet. So, um sink current 100 milliamps, no worries. Um ink jets, electrostatic, electroluminescent displays, and bingo, latched output. Data input, 32-bit shift register, and uh a data output, so then you can cascade it to the next one, so you can

**Dave Jones:** have multiple uh ones of these. So, how many chips of these do we need? Uh we need three of these uh chips, and they've got the output MOSFET drivers for driving that. Um so, what is the maximum output voltage? Here we go. Haha, 230

**Dave Jones:** V. Uh Bingo, 220 maximum high output voltage, 220. That will do the business. Thank you very much. Are they in stock? They're Well, they got 57 in stock. You know, they're seven bucks 91 each, bit pricey, but you know, we're getting

**Dave Jones:** towards a solution here. You can keep going and maybe try something find a bit something a bit cheaper, more available, more uh jelly beanie maybe, but you know, we're out of the realms of jelly bean now when we start searching for a

**Dave Jones:** high-voltage uh driver for these sorts of uh you know, specific serial driver application things. And of course, you might be thinking, "Oh, Dave, use one of the ULN uh you know, 2000 series jobs, you know, the 2003." Well, if you go look at

**Dave Jones:** those, they're all like 50 V, 80 V. They're like Yeah, they don't really do the business. We can go from maximum downwards. Best one we've got here, 80 V. Not going to do it. Let's actually have a look at what the logic supply voltage

**Dave Jones:** is. You might think, "Oh, that's 5 V or 3.5." Yeah, you know, that's a natural assumption. No, this one is designed for 12-V operation, minimum 10.8. And aha, does it have you know, regular CMOS TTL compatible inputs? Nope. The high-level

**Dave Jones:** input voltage. Look at this, VDD minus two. So, to get a high on the input when you're feeding your data and your clock in and everything else and your latch signal, then you need a 10-V logic signal. So, these regular inputs here

**Dave Jones:** are not even compatible with 5-V TTL logic. Useless if you're driving this from your Raspberry Pi or Arduino or whatever you know microcontroller solution you're using. It's not going to work. You're going to need a logic level translator or even a

**Dave Jones:** logic level translator chip or a you know a transistor pull-up type arrangement or whatever, but you're going to need something. What a pain in the ass, but granted we do only have we only have to drive one of these because they'll be cascaded

**Dave Jones:** together. So, we only have to drive the data input yeah, the data input, the clock, and the latch enable and well, if you're going to use the blanking line or whatever you tie the other ones and we do have 12 V available. You're going to

**Dave Jones:** we've got that for the power supply for the high-voltage power supply, so that's okay. So, that 12 V kind of worked out okay and then the data out here, that would be at a at the 12-V level. So, it can easily drive the input

**Dave Jones:** for the next one, but yeah, so we only need like three logic level translator lines. So, I guess that's not too bad, but you know, if you're rushed into buying this, hooked it up, and then you didn't look that didn't think to look at that,

**Dave Jones:** you would have come a gutter. Trap for young players. But wait, hold on to your hat. Microchip have thought of everything. Look, let's go to the list again, sort by just Microchip. They've got a 16-bit serial one in a 32-pin VQFN 24-pin

**Dave Jones:** they've got an 8-bit one. Anyway, 486 in stock, two bucks 20. Let's have a look at this HV509, shall we? It's a high-voltage uh backplane driver with push-pull output. So, it's got totem pole outputs. But anyway, 200 V here. Uh and let's go.

**Dave Jones:** Look. Whoa, logic level translators. Let's go further down, further down. Let's have a look. Aha, logic level supply voltage. Bingo. It can work from 3.3 or 5 V. No worries. High-level input uh voltage not a problem. Anything above

**Dave Jones:** uh 0.9 V. Now we're talking. So, we don't need the logic level uh translators here. And interestingly, here is this uh high-voltage output. As I said, it's a totem pole output. It also has an internal V bias here, which can actually

**Dave Jones:** you can do current limiting with this puppy. So, we can um source or sync. So, it doesn't matter. I mean, it doesn't matter that we've got a totem pole output. It'll still um it's going to survive that. But here we go. Here's

**Dave Jones:** typical high-voltage output current sync versus the bias voltage for a 200 V um supply. And there it is. You can set the current versus the V bias voltage. But of course, that will Well, you could do it with this. So, you could actually

**Dave Jones:** save technically save a resistor um on each one of those uh uh displays. So, that's awesome. Um this chip looks like it's going to do the business. 16-bit shift register, 16-bit latch. It's got the data out so that we

**Dave Jones:** can cascade them. No worries. It's all latched and so translator, I think. Winner winner chicken dinner. Except for the package. 0.5 mm pitch 32-lead QFN. What a pain in the ass. But hey, if you wanted to, you could

**Dave Jones:** have a look at this uh 8-bit job here. Yeah, they're uh $3.23 each. So, they're going to be pricey. But if you didn't want to solder that pain in the ass QFN, you could use these uh 8-bit jobs and

**Dave Jones:** they do the business as well. Logic level translator 5 volts has got data out and it's got all the goodness in an SOIC-24 pin SOIC package. So, yeah, it's a typical supply voltage 5 volts so it's compatible with typical micro

**Dave Jones:** controller modules and stuff like that and it's going to do the business. Got the same totem pole output, doesn't have the V bias but nah, you know, who cares? Right, so that would do the job as well. It's just a bit more pricey. Anyway, I

**Dave Jones:** think 30 odd minutes of waffling is enough for part one here. In future parts I'll do the schematic layout the board, talk about what my application is and stuff like that. So, stay tuned. Catch you next time.
