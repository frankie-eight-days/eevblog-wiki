---
video_id: TCpo_vNWzMs
title: EEVblog #1126 - Mystery Teardown!
url: https://www.youtube.com/watch?v=TCpo_vNWzMs
source: youtube-asr
timestamps: {"0": 0, "1": 8, "2": 25, "3": 44, "4": 60, "5": 80, "6": 100, "7": 122, "8": 145, "9": 158, "10": 169, "11": 187, "12": 202, "13": 214, "14": 230, "15": 245, "16": 261, "17": 278, "18": 291, "19": 308, "20": 322, "21": 333, "22": 344, "23": 357, "24": 371, "25": 384, "26": 400, "27": 414, "28": 427, "29": 441, "30": 460, "31": 478, "32": 498, "33": 513, "34": 526, "35": 538, "36": 552, "37": 587, "38": 600, "39": 615, "40": 625, "41": 639, "42": 656, "43": 671, "44": 687, "45": 695, "46": 707, "47": 725, "48": 742, "49": 756, "50": 777, "51": 800, "52": 819, "53": 839, "54": 851, "55": 864, "56": 878, "57": 892, "58": 909, "59": 925, "60": 939, "61": 952, "62": 970, "63": 985, "64": 1000, "65": 1010, "66": 1025, "67": 1033, "68": 1047, "69": 1060, "70": 1085, "71": 1096, "72": 1119, "73": 1138, "74": 1149, "75": 1159, "76": 1170, "77": 1188}
---

**Dave Jones:** Hi, welcome to a mystery teardown. Can you guess what this is? I'm not going to tell you. I'm going to open it up and let you figure it out for yourself.

**Dave Jones:** I've covered up the brand name here because you might recognize it. We've got a line on and off status. Start, stop. It's obviously in a 19-in rack mount. There's some sort of channel label thing over there.

**Dave Jones:** And if we have a look on the back here, this is what we've got. Just got a card edge connector here, some weird ass input and output system IO connectors, a remote start made in the United States of America, and an IEC input.

**Dave Jones:** You got any ideas? Now, the interesting thing about this is though it's from a massive name which you can find almost any information on any product they've ever made, but my Google foo must be off cuz I can't find a single thing about this.

**Dave Jones:** No user manual, no specs, no schematic, no service manual, nothing, zip, nada. Which of course makes it all the more interesting. So, let's go. Yes, this is my new electric speedy screwdriver.

**Dave Jones:** Here we go. Let's take a look inside. Your guess is as good as mine. Woah. Okay, we've got some Is that 74 series stuff? No, it's not. Well, it could very well be, but they're custom part numbers and you might recognize the logo.

**Dave Jones:** HP. None of this Agilent rubbish and certainly none of this Keysight rubbish. Um we've got a bit of HP kit. Can you still figure out what this is? Um we've got a mysterious metal can down here with our card edge connector.

**Dave Jones:** Some gorgeous looking Sprague capacitors for all you Sprague fanboys. 2600 mic, none of that like 2200 e12 type rubbish. We've got looks like some power down here on standoffs and maybe some you know zenners and diodes and and as is common in HP gear, you'll find the custom part numbers.

**Dave Jones:** Now these could very well be like you know standard 74 or 4000 series CMOS chips, but they've all got the HP part numbers on them. Very very common. We've got a couple of relays.

**Dave Jones:** Got a mains over there and you know some pretty how you doing wiring down in there as well. Check that out. Geez, that's kind of like un-HP, isn't it?

**Dave Jones:** It's almost as if it's like it's you know not like a mainstream product. They've got what looks like a TO3 package down in there. Probably like a series pass transistor for a linear regulator and not that switching rubbish in something like this.

**Dave Jones:** You still got any idea what it is? Bueller? Bueller? I do believe under here we'll have some sort of adjustment. Something ah, come on. Yeah. No. What? Some sort of like wool like it's not foam.

**Dave Jones:** It's not like closed cell foam. It's more like some sort of woollen stuff. Weird. I expected to find a trimmer pot under there. Huh, the plot thickens. In fact, check this out.

**Dave Jones:** The entire thing look is mounted on this rubber sort of it's it's almost sticky kind of sort of foamy rubber backing on that. So so that's really strange. That's take a squeeze inside.

**Dave Jones:** Okay, at least I should leave Let's lift Oh, does that mean No, there might be might be something on the bottom. I think I got to get the might have to get the whole board out first and uh I don't know.

**Dave Jones:** That's Oh, what's going on? That's for all you Japanese relay fan boys, Babcock. Let's have a look what's under this board here. Ta-da! More stuff. Oh! Motorola crystal oscillator.

**Dave Jones:** Ah, oh, it's upside down, so all the electrons are going to fall out. Look at that. We've got some uh uh potted uh little custom transformers there with like, you know, half a dozen turns on each side.

**Dave Jones:** So, wow. Anyway, it's running at massive 8.38 MHz. Fantastic. But, once again, got all the HP part numbers. You can go look those up. But, you know, there's there's Signetics, stuff like that.

**Dave Jones:** Do we even have a date code yet? I don't know. Oh, look at the burn marks around that diode bridge there. Um It's got a bit warm-sky. And these little jumper pins here in the little machine pin socket, that's pretty how you do it.

**Dave Jones:** Um this is very unlike HP. It's almost as if it's not a mainstream product. And that's probably why I couldn't find any information on this thing at all. Oh, oh, look.

**Dave Jones:** It's a little Oh, that that must be a channel thing. I reckon that's a channel selector. And it smelt like mid-70s to me and sure enough, 47th week '73 and uh 23rd week '73.

**Dave Jones:** What do we got? 27th week '74. So, yeah, it's actually yeah, it's mid-70s. The smell is bang on. So, do you have any clue what this thing does yet?

**Dave Jones:** Well, actually I was wrong about the channel select up here. It's not channel select. If we actually go have a look inside here, ta-da! This might give you a clue.

**Dave Jones:** RDGS per second. Readings per second. We're currently on four readings per second. Can you guess what it is now? Bueller? And I just love the hand-taped layout on this.

**Dave Jones:** It's just classic. Look at that. Somebody's gone along there with the bishop tape and laid out that double-sided board. Brilliant. Oh, I found one that doesn't have a HP part number on it.

**Dave Jones:** 7404. Hex inverter. 7410 is it? Um well, sorry. 7410, but everything else has HP part numbers on it. So, I'd actually say that's your address select down there. There you go.

**Dave Jones:** 1 2 4 8. Just select your address in binary. Does anyone remember Stevens Arnold Inc. in South Boston, Massachusetts? They were the go-to in the mid-70s for isolation transformers, by the looks of it.

**Dave Jones:** Wow, look at the burn marks from that bridge rectifier. Anyway, all the magic's under here. Have you figured out what it is yet, by the way? And I love the PCB threaded screw eyelets in there for the power That's just fantastic.

**Dave Jones:** Ah, don't see enough of that these days. Oh, no. I don't think that they go all the way through. No, the screws were holding them in. We just have to get a bit medieval on its ass and uh lift Hey, oh, look.

**Dave Jones:** Ah, it's dead. Wrapped in plastic. You ever seen anything like that? Wow! With this like Look. They're They're like That's like thermal insulation. Look at that. Just like your woolen uh you know, your pink bats.

**Dave Jones:** Your woolen bats that you get in your house roof. Terrific. They want really wanted uh to keep this at not probably not at a fixed temperature cuz I don't see anything in terms of uh like a heating element in there.

**Dave Jones:** It's not temperature controlled, but uh they they do want to um thermally isolate it. So, they don't want any drafts drifting across here and then upsetting components cuz we've probably got a you know matched transistors in here like this and uh they you know these two matched they look like Wow, they look like precision resistors.

**Dave Jones:** We'll have a closer look at this. This is fascinating. Don't you hate it when you've got woolen hair stuck on your capacitors? So, yeah, they obviously don't want any drafts coming across even though this thing doesn't have a fan at all.

**Dave Jones:** Um you don't want any, you know, uh convection inside the case just, you know, any temperature gradients across your components. So, there you go. There's all the magic. Can you guess what it is yet?

**Dave Jones:** Should I tell you? Should I show you the front panel label? Mm. Mm. Looks like it's conformally coded. You can see the shine on that compared to the PCB.

**Dave Jones:** Probably to stop moisture on the PCB. So, whatever this is, it is a well, high precision for the time um high precision something rather. All right, I'll put you out of your misery.

**Dave Jones:** Tada! Hewlett-Packard 18652A analog-to-digital converter. Yes! None of this single chip or built-in your microcontroller ADC rubbish. No, sirree, Bob. This is obviously some sort of uh you know, precision analog-to-digital converter for some like because I can't find any information on this, it leads me to believe that it's probably some like industry specific thing thing maybe the you know the medical or research industry or something like that you know

**Dave Jones:** physics or stuff things like that physics data sampling or some other such thing that there it's not like designed for one customer cuz there's a lot of these around you can actually still buy these second-hand on eBay.

**Dave Jones:** So they must have had a lot of use but I can't find any information on the HP 18652A at all. So maybe my Google food just sucks today but anyway, this is an ADC I don't so I don't even have any specs.

**Dave Jones:** What is it? Maybe it was a like a 16-bit ADC for the day or something like that at you know four samples per second maybe it was higher than that 18 20 could have been 24-bit at the time.

**Dave Jones:** Who knows but they certainly went to a lot of effort to do this. Oh, they rubbed the numbers off. Oh, no. I thought they'd rubbed the numbers off. There you go.

**Dave Jones:** Do we have part numbers on those? Wow, I haven't seen one of those trendy packages in a long time. It looks like your standard transistor which you'd get here of course the standard TO-92 package there but then it's just got the round base on it.

**Dave Jones:** Old school. Wow. And check these out. These are fascinating. These are precision resistors. Circa trim IRC Circa trim 10K resistors but you can see that they're only plus minus 5% there.

**Dave Jones:** They're you know low tolerance resistors 10K and 5K plus minus 5% but they would have a ridiculously high temp code those things. So they'd be really schmick resistors probably paid a fortune for them.

**Dave Jones:** Maybe they were were they laser trimmed back in the day or they you know trimmed by nude virgins with gray beards. I don't know, but yeah, precision resistors. Awesome.

**Dave Jones:** And there's nothing on the bottom, but it looks like they do have that uh conformal coating on there, as well, just to stop the spread of moisture across the PCB, so to stop any uh creepage across uh the board.

**Dave Jones:** Once again, they've got that uh foam insulation there um just to stop any uh temperature gradients across the PCB. Nice. So, you'd think this is like maybe a multi- channel uh ADC, but no, then we've got ground on the uh bottom there, and just the single input on the top.

**Dave Jones:** That's all she wrote. So, it's a single input ADC, obviously high resolution, high precision. It's got a 1-V um input range, and the readings per second, um you know, you can choose uh from half a reading per second up to 32.

**Dave Jones:** I presume that would uh maybe trade off the uh bandwidth and/or the number of bits, as well. Maybe you can have a higher sample rate, um you get a greater effective number of bits.

**Dave Jones:** So, I don't know what topology they'd be using, some sort of like, you know, is it a single or dual slope integrator or uh something like that, perhaps? But yeah, it's a custom ADC, one-channel ADC in a 19-in rack for some ridiculously specific market.

**Dave Jones:** They, you know, probably cost thousands of dollars back in the '70s for one of these analog-to-digital converters. If anyone knows uh the price of this, the specs of this, anyone's got a schematic or anything like that, um you know, please let us know, even like a a manual, um and like or a some sort of data sheet for it, please let us know, cuz it's fascinating.

**Dave Jones:** A 19-in rack ADC. Did anyone to it? If you did, you win the internet. And I'm going to assume that this is our like sampling capacity here. These electrolytics wouldn't be, of course, but you know, I've got some other schmicko film ones in there that could be.

**Dave Jones:** So, it's got to be some sort of, you know, sampling ADC and then everything else is, you know, maybe time a counter stuff. Interesting. Because it's certainly not like, you know, it's not like analog comes in and digital comes out of that can.

**Dave Jones:** That's not what's going on there at all. So, anyway, this is the power supply side of it, obviously. So, this is these are main filter caps here. Then we've got some maybe some series pass here.

**Dave Jones:** Maybe some lower like some secondary regulation there because precision ADC like this one has got to have a nice regulated supply. So, these are all probably local regulation for it.

**Dave Jones:** And then you're some sort of slopey ADC integrator and then all the rest of the stuff to convert it to digital. And then this, you know, it probably shifts it out.

**Dave Jones:** Well, is it parallel out or is it No, it's serial out because on the back it's just got output and input. So, you can cascade them together probably and it probably shoves all the data into one big serial stream or something.

**Dave Jones:** It measures some voltages here. I've powered it on and we get the red status light and the relay up there goes clunk clunk. So, something's happening. So, let's measure this plus minus 15 volts in here.

**Dave Jones:** Whoa, 22. Uh 22. So, doesn't sound good. Let's measure the 5 volt rail. 5 volt rail's good. So, all the digital stuff's going to be doing its digital magic.

**Dave Jones:** Maybe they've mislabeled on the PCB in there at plus minus 15 and plus minus 22 is the go. Either that or the two regulators uh could be shot. I don't know if we got positive negative regulators in there.

**Dave Jones:** They could be goneski. And that's our 5-V rail there. That looks reasonably good. Uh that's 5 mV uh per division. And woah, what's going on there? Woah, I thought it was good.

**Dave Jones:** No? Woah, jumping around the shop. That's 50 mV uh per division. And why is it banging around like that? Wow. That's a sick puppy power supply. I hate the stupid glarey screen on this new Rigol 7000.

**Dave Jones:** Woah. And that's our 5-V rail. Wow, there's some stuff happening. Stuff high frequency Look at all that high frequency crap happening in there. Wow, that's not It's not a happy camper, is it?

**Dave Jones:** Okay, so I've given that Rigol 7000 the flick. That screen's just horrible. All right, I'm going to single shot capture uh 1 V per division. I've got the serial output here, which is, you know, the output has just like this is just the output.

**Dave Jones:** There's an input and output connector, as you saw right at the start. I'm going to press start here. See what happens. And single shot. Tada! Looks like we have something.

**Dave Jones:** It's decaying. Woah, it's going negative. Hello. Okay, we're getting stuff here when I press it. Let's actually go into roll mode, shall we? And give it a go. Now, I'm going to press the button.

**Dave Jones:** Boom. So, it gives a single Looks like it gives a single pulse. If I hold it down and let it go. If I hold it down, it goes negative.

**Dave Jones:** If I release the front panel start stop button, it goes positive. That's interesting. If I keep pressing it, it's just that just doesn't seem right. I expected some sort of serial data packet cuz the 5-V rail's working.

**Dave Jones:** So, even if the analog section was crap, I'd still expect it to be doing the business. So, you know, it's got that 8-meg clock in there. I expected it to be, you know, outputting a stream of data.

**Dave Jones:** So, but it ain't. Could be we're just one sick puppy. Like I said, if you've got any info on it at all, I cannot find a damn thing. The specs, user manual, a data sheet, anything on it at all, which is quite strange, which leads me to think that it was, you know, developed and and sold by one of the, you know, specialist divisions of Hewlett-Packard, like spun off once I

**Dave Jones:** Keysight focused on test and measurement and stuff like that back in the day. Yeah, they had just all these different divisions. So, some sort of like, you know, maybe research type analog-to-digital converter.

**Dave Jones:** I've got no idea. I just I no idea of the specs, but it's obviously precision. They went to a lot of trouble with that thermally inside this thing to match, you know, make sure there's no thermal gradients across those components, which can upset the apple cart in terms of, you know, the balance of your the symmetry of your circuit in there when you got matched that's why

**Dave Jones:** you often use matched transistor pairs in the same package on the same die cuz they're the same temperature. That's why often you'll get two transistors back in the day, still rarely, but you see it occasionally these days, two transistors back-to-back and then they'll bond them together with a piece of metal to keep them thermally matched.

**Dave Jones:** So, yeah, they've gone to a lot of trouble to do that and it's some sort of mystery analog-to-digital converter. Anyway, hope you found that interesting. If you did, give the video a big thumbs up.

**Dave Jones:** As always, you can support me over on Patreon and I rarely mention this, but you can also uh support the blog in various ways, often at no cost to yourself.

**Dave Jones:** I'll link it in down below as well. So, if you buy stuff on Amazon or AliExpress, I've got new AliExpress affiliate link and stuff like that. If you want to buy anything through that, I get a commission on that.

**Dave Jones:** Doesn't cost you anything. I support cryptocurrency donations and PayPal donations and Patreon donations and stuff like that. So, thank you very much to all those who support me. If you like this video, please give it a big thumbs up, and as always, discuss down below.

**Dave Jones:** Catch you next time.
