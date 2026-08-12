---
video_id: 96Wz6NIalC4
title: EEVblog #217 - Lecroy 9384C Oscilloscope Teardown
url: https://www.youtube.com/watch?v=96Wz6NIalC4
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 35, "3": 52, "4": 76, "5": 97, "6": 110, "7": 124, "8": 138, "9": 161, "10": 172, "11": 182, "12": 192, "13": 206, "14": 218, "15": 233, "16": 257, "17": 266, "18": 277, "19": 298, "20": 308, "21": 323, "22": 344, "23": 360, "24": 375, "25": 386, "26": 401, "27": 418, "28": 439, "29": 462, "30": 486, "31": 497, "32": 509, "33": 521, "34": 535, "35": 552, "36": 562, "37": 576, "38": 587, "39": 597, "40": 610, "41": 633, "42": 648, "43": 664, "44": 687, "45": 698, "46": 711, "47": 735, "48": 758, "49": 768, "50": 784, "51": 804, "52": 826, "53": 842, "54": 859, "55": 872, "56": 885, "57": 901, "58": 918, "59": 926, "60": 944, "61": 956, "62": 969, "63": 984, "64": 996, "65": 1009, "66": 1025, "67": 1036, "68": 1045, "69": 1066, "70": 1084, "71": 1095, "72": 1106, "73": 1118, "74": 1136, "75": 1145, "76": 1155, "77": 1210, "78": 1243, "79": 1260, "80": 1268, "81": 1282, "82": 1300, "83": 1314, "84": 1332, "85": 1346, "86": 1359, "87": 1367, "88": 1418, "89": 1427, "90": 1446, "91": 1459, "92": 1472, "93": 1485, "94": 1498, "95": 1527, "96": 1547, "97": 1557, "98": 1569, "99": 1586, "100": 1600, "101": 1619, "102": 1632, "103": 1645, "104": 1656, "105": 1667, "106": 1682, "107": 1696, "108": 1707, "109": 1721, "110": 1750, "111": 1767, "112": 1783, "113": 1797, "114": 1809, "115": 1824, "116": 1839, "117": 1857, "118": 1866, "119": 1886, "120": 1905, "121": 1920, "122": 1934, "123": 1951, "124": 1960, "125": 1972, "126": 1990, "127": 2004, "128": 2018, "129": 2032, "130": 2047, "131": 2066, "132": 2078, "133": 2092, "134": 2106, "135": 2119, "136": 2128, "137": 2142, "138": 2154, "139": 2170, "140": 2186, "141": 2212}
---

**Dave Jones:** Hi, look what I just scored. I got a LeCroy 9384C 1 GHz analog bandwidth scope, four channels, uh 4 gig samples per second maximum if you do a single channel, uh 400K points memory as you can see up here, and it's a not a bad scope at all.

**Dave Jones:** It's about a 12-year um old model, and it does have some physical damage to it on the side, which I'll show you, but hopefully, fingers crossed, we'll power it up, and it should at least maybe hopefully work, but anyway, we'll see, and we'll do a teardown of it as well.

**Dave Jones:** Now, now, if you don't know LeCroy scopes, they're part of the big three in {quote} marks um oscilloscope manufacturers. There's LeCroy, Tektronix, and Agilent, of course. And LeCroy have always uh they like a pioneered a lot of the digital scopes out there.

**Dave Jones:** They've always had huge sample memories, and very fast acquisition um rates, and high analog bandwidths. And they're one of the three big major manufacturers out there before a lot of the uh smaller companies started to be able to do uh 1 gig sample per second and the higher uh bandwidths, you know, the 300, the 500 MHz, and even 1 GHz these days.

**Dave Jones:** But these LeCroy scopes aren't nearly as popular um on the second-hand market as the um Agilents and the Tek's, of course. But if you're if you're after a um high bandwidth, uh high sample rate, high and deep memory uh scope, you can pick up some decent bargains if you search for LeCroy uh scopes, cuz they're not nearly as popular.

**Dave Jones:** Um now, as you can see, this one's got some uh screen burning here. It looks um fairly fairly bad, actually, in terms that you can see the uh waveform, you know, you can see the um the waveform graticule there.

**Dave Jones:** You can see the menus all sort of burned in over here. That's a bit nasty. That's something to watch out for if you're buying these second hand scopes, but anyway, I thought we'd power it up, see if it still works, fingers crossed, and do a teardown.

**Dave Jones:** It should be quite exciting. Let's go. Now, as you can see, there's some damage here on the left-hand side, and this bracket here, this internal bracket has fallen out of here.

**Dave Jones:** I guess they'd have a similar one up there, which looks like it just holds the front panel on, but I don't know if it's been dropped or or what, you know, transit damage or what the hell's going on there, and but anyway, there is some damage, and if you have a look on the side here, it's got a nice carry strap, but there are starting to appear the odd crack down in there.

**Dave Jones:** So, yeah, it's not looking It's not looking that sturdy at least on the outside case. Maybe the plastic's a bit brittle. I don't know. Maybe it's had a tough life.

**Dave Jones:** Now, you can see the floppy drive up here on the top. I am not a fan of these at all. They're just huge dust collectors. You Just get dust in there, and it all falls down in the floppy drive.

**Dave Jones:** I don't like that design aspect at all. Now, I'm definitely not a huge fan of the layout of these LeCroy scopes, but they do at least have them separated.

**Dave Jones:** Time base and trigger has its own setting there. The channels, there's no separate vertical attenuation control for each channel. You got to select the channel and then do your volts per division, and your time per division, you know, little tiny knobs.

**Dave Jones:** I don't know. I much prefer bigger ones, and you know, there's no color coding or anything like that that you get on more modern scopes, but anyway, you know, it's a LeCroy.

**Dave Jones:** And on the back here, we've got an old school Centronics parallel interface. We've got the card with the RS-232 serial, and the even older school IEEE-488 GPIB interface. And the third uh expansion thing's unpopulated.

**Dave Jones:** Huge fan on it and uh as you can see right down the bottom here beauty, made in the USA. And the manufacturing date, 17th of May, '99. Uh just over 12 years old and so in that sort of time you would expect um you know, there's a fairly good chance that it would still work unless it's been physically abused or something like that.

**Dave Jones:** Now, I reckon the odds are fairly good for a 12-year-old scope. All right, let's power it up and see if she works. One of the annoying things about these scopes, no front power switch at all.

**Dave Jones:** You've got to reach around the back here and uh flick the big mechanical clunker. Here we go. WHOA, HEY! IT IT TRIPPED MY LOOKS like it tripped my earth leakage circuit breaker.

**Dave Jones:** Ah. Brilliant. Give it another go, shall we? There we go. No problems at all. Do we get anything on the screen? It's beeping. Yeah, there we go. We've got something with the time, date.

**Dave Jones:** Whoa! There we go. It's at least powered up. It's giving us some garbage on the uh on the vertical there. I don't know what all that is, but anyway, it's uh at least booted.

**Dave Jones:** Now, I've gone into the menu here and turned up the waveform intensity and the grid intensity. Waveform intensity 100%, grid intensity 90, and you can still see the ghosting is a bit of a pain in the butt, but it's uh you know, it it's sort of some of the text is sort of washed out.

**Dave Jones:** It's not as bright as it could be, but hey, you know, it it's still completely viewable even with the um uh burned-in display. Well, it's popped up with multiple calibration failures, so it looks like it has uh some sort of You know, I almost got to the point where I had a had at least There we go.

**Dave Jones:** There we go. At least we've got some ground signal up there, but you get these pulses in here and I've got, you know, I disconnect that. There's no signal going in there at all and yeah, it's just garbage popping up and I seem to get that on all four channels.

**Dave Jones:** What a bummer. You would have expected at least one channel to work. But of course, if you get the same fault across all four channels, then that's probably not a bad thing cuz it indicates maybe there's something else common between all of the four what?

**Dave Jones:** Maybe there's a power supply issue or something like that instead of just one, you know, somebody's overloaded one acquisition channel and blowing the crap out of it or something.

**Dave Jones:** It indicates that there's something else going on there. Now, in the utilities menu here, I can't find any diagnostics stuff really. It seems to just all do sort of like auto calibration test all the time.

**Dave Jones:** So, I you know, there's no real diagnostic thing that I can find. I don't want to have to read the manual. That'd be defeatist. Now, there's one interesting thing you'll note is that it doesn't have the the traditional spade lug terminal for the calibration output.

**Dave Jones:** It's got a proper BNC and you can actually get that calibration output via the software menu to do other various things. You can get it to output pulses in different frequencies and stuff like that, which is rather quite nice and of course, the the external inputs on the front and the fourth channel here, as you can see, they don't have It looks like in these model Lecroys,

**Dave Jones:** I'm not sure about the more modern ones off hand, but they've got like a separate connector here for the interface for the external probes. In whereas the other Techronix Agilent ones seem to have the just the pins around the outside of the BNC connector, but they've got a physically a separate connector there, but it all plug in as the the unit though.

**Dave Jones:** And here I'm feeding in a 5 volts 10 kilohertz sine wave and I am getting my sine wave, but the vertical seems to be all over the shop. Whereas before I was on 1 volt per division before and it was showing like, you know, 5 volts amplitude, but now it's just dropped back down cuz it it seems to go through this auto calibration thing every so often and and and as you

**Dave Jones:** can see it's getting those those pulses on there, there's little glitches that go all the way down to this There we go. I just changed it by one setting to 0.5 volts per division and it's all over the shop.

**Dave Jones:** There we go. It's back to that 1 volt per division. So it you know, it's it looks like data is getting through the vertical channel, but the trigger doesn't seem to work at all.

**Dave Jones:** And if let's try the auto setup. If we just go bang, press the auto the evil auto setup button and let's see if it can do anything and actually detect that signal and trigger on ADC fires.

**Dave Jones:** I just saw a little message there eight ADC fires. Or maybe that was eight channel eight ADC's failing, but oh, check that out. Look at that. That's rather interesting.

**Dave Jones:** So it seems we got it to a point where it is actually triggering. I can get the start of the trigger level over here. There's the There's the trigger level there, but check out that acquisition problem where it just bang, it just sort of re-synchronizes and does something weird there.

**Dave Jones:** That's bizarre. I've never seen anything like that before. Now, one interesting thing here is that you can set up our single, dual, or quad grids on the screen like that.

**Dave Jones:** So I split that into two separate displays or four separate displays like that. Very nice. And there you go. I'm feeding the same thing into three channels and we're getting that same glitch across the three different uh like that.

**Dave Jones:** I'll do the fourth one and uh bang, we get the same the same effect down there. So, it looks like it's a It's uh totally consistent. And the vertical plays around a lot.

**Dave Jones:** You change it and it doesn't scale correctly and things like that, but at least it's consistent across all four channels, which uh might make uh troubleshooting a bit easier perhaps.

**Dave Jones:** And by the way, the fan on this thing is damn loud. It's about 3 dB past a norm. So, there you go. That's one real sick puppy we've got here, but uh I don't think I'll play around with it much longer.

**Dave Jones:** I want to crack this sucker open. So, you know what we say here on the AV blog, don't turn it on, take it apart. Now, it looks like this top lid here is just going to pop straight off based on these four screws here.

**Dave Jones:** And ta-da! And here's the inside. That uh lid popped off real easy with four screws. We've got our uh floppy drive over here via ribbon cable to uh one of these um expansion cards here.

**Dave Jones:** So, we can easily Looks like we can easily disconnect that. And here's the insides of it. It's uh fairly uh surprisingly uh open actually. There's one huge main board on the bottom, which is uh all shielded here with uh heat sinks poking out of it.

**Dave Jones:** The CRT's exposed and the rear board's all exposed there. That's the uh CRT uh driver board. On the front there, we've got our power supply over here in its own um It's a huge uh DC power supply, but considering that this thing um is rated for like 350 W uh maximum, that's going to be a 350 W uh capable power supply.

**Dave Jones:** We've got a main processing board over here, which we'll take a look at. The very short little uh expansion uh boards here, and that's about it. So, let's take a closer look.

**Dave Jones:** And that's the CRT driver board, and it's rather unusual, I think, that it's actually bolted to the front panel like that. And it does look like the entire front panel assembly with the CRT and that board just up pulls off.

**Dave Jones:** So, I guess you could say it's actually quite neat design aspect in that case that the whole that the CRT with its with its control board and all of its wiring, you can just looks like you can flip all of that front panel completely off so that you can work inside the scope, and you don't have to disconnect any high voltage or touch any high voltage stuff at all.

**Dave Jones:** So, I rather like that. I find it unusual, but I rather like it. Ta-da! Look at that. I think that's really rather clever. I like it. That's just fantastic that you can take out the front panel with the CRT and its driver board like that, and just put it aside and work on your scope.

**Dave Jones:** That's just great design. I love it. But not only that, though, because there's only two little there's only two ribbon cables on the side here, which actually connect into it.

**Dave Jones:** There's no other power cables at all. You can actually still swing it out, and looks like you can still connect them in there, so you can work on the scope in here while still having the display active out there and plugged in.

**Dave Jones:** Let's just get an air duster in there and blow some of this out. And if you look down on the four 1-GHz bandwidth vertical channels down here, you can see all the little trimmers available through the shielding here.

**Dave Jones:** That's rather neat. I like it. And they've made a cutout there for the little freestanding heatsinks. It looks like for as part of the analog or trigger circuitry and they've got more cutouts here for these rather large heatsinks here and it looks like there's some really wicked looking hybrids in there.

**Dave Jones:** You can see that ceramic substrate in there. You see that See that white ceramic that that looks like a big ceramic hybrid huge multi-pin. It looks like a big dual inline hybrid with a massive heatsink stuck on the top.

**Dave Jones:** There's another heatsink stuck on top over there. That might be the processor or something like that. Some more heatsinks in here. So it's this beast generates a fair bit of heat or at least some fairly inefficient 12 you know 15 12 year old processing grunt in here.

**Dave Jones:** And that noisy fan I spoke about looks like you know really easy standard fan easy to get in there and change it to a quiet one. If you had a scope like this that's one of the first things I'd be doing is putting in a nice silent fan for it.

**Dave Jones:** And there's the vertical expansion boards there for the serial the GPIB and the parallel and they're all connected via a daisy chain ribbon cable through to the main processor board here.

**Dave Jones:** And we've got some decent mains filter in there on the input. And the huge switch mode power supply here it all comes out in one ribbon cable assembly which goes down to a big big main connector on the board so you can just whip that out and pull the power supply out.

**Dave Jones:** It's rather modular. What this spare cable is coming out here your guess is as good as mine. It's been cable tied up like that unused. I don't know maybe for some optional thing but I think this is the highest end model in this particular series so go figure.

**Dave Jones:** And it looks like this processor card here just lifts straight out of here. There's a if as long as you undo this ribbon cable down in here. There we go.

**Dave Jones:** Bang. Just pops straight out. And this main processor board looks fairly old school. It's got a Motorola MC 68 000 680030 embedded controller here with a float with an 80-bit floating point co-processor.

**Dave Jones:** Awesomely old school. I love it. So, the floating point processor here does all the math capabilities which these LeCroy scopes are famous for having their math capability and stuff like that.

**Dave Jones:** So, and we've got an Intel flash here. It looks like we've got some sort of custom LeCroy device here. I have no idea what that is. It's got some memory here and but there you go.

**Dave Jones:** We've got a a DRAM slot here. A spare DRAM slot up the top here. Isn't populated on this one. All these ones with stickers there. Little gals or pals or something like that, I figure.

**Dave Jones:** They've got quite a few of those on the board. We've got a backup battery there. We've got a can here. We'll try and pop the shield off that and some discrete logic down here to handle the PCMCIA adapter.

**Dave Jones:** And underneath that shield, there's a custom LeCroy large scale integration ASIC. Some sort of BT device here running with its own local clock. But these ones go off to the display.

**Dave Jones:** This is probably the display processor cuz these two go off to the display board. It seems to be a little bit of gunk around the base of that the corner bottom corner of that tin on there, but I think it's Yeah, it's just some looks like just some dust.

**Dave Jones:** And yep, that cleaned up just fine. Nothing wrong there. There was also a little bit of that down on the bottom here which all the dust that had actually accumulated inside.

**Dave Jones:** But apart from that, it's actually a pretty clean board. I don't I don't mind it at all. It looks pretty good. It looks like there's no obvious issues on there.

**Dave Jones:** There's no electrolytic caps that can fail. There's a few tantalums, of course. The tantalums can fail, but the actual but because the main display is working and the processing is working, I'm you know, you can be fairly confident that there's probably not going to be anything wrong with this main processor board.

**Dave Jones:** It's got to be on the main board in the rest of the unit. Now, I found a fair bit of this this dust this accumulated black dust sort of wedged between the base of the PCB and the and the metal case.

**Dave Jones:** So, I'm just going to probe that to see if it's at all conductive. Just just curious. I'm reading nothing on my meter. There's nothing there, but still, you never know.

**Dave Jones:** It's worth checking for stuff like that. And that's where some of that accumulated dust was found sort of there there it is. You can see it uh You see it there and there's ICs directly under there.

**Dave Jones:** So, that's not particularly nice. It needs a little bit of a clean. And that power supply popped out real easy, too. Just a single screw on the side of the case and a single screw on the back and you disconnect the two power connectors and that's it.

**Dave Jones:** But, take a look inside this thing. Here's all that accumulated horrible accumulated dust. Not terribly surprising that it tripped my earth leakage circuit breaker just a bit. And that really is some horrible stuff in there.

**Dave Jones:** It's just uh it's all accumulated. Look at it. Yuck. It needs I need to take the cover off that and really give it a good blowout with the air duster.

**Dave Jones:** And there's the innards of that switch mode power supply and there's a whole bunch of gunk that's accumulated up here, but it's mostly on this end here. That's what will usually happen.

**Dave Jones:** Most of will actually accumulate on the one end because air will be forced through a certain way. Okay, I've cleaned that up and I'm much happier. So, let's go on a bit of a visual tour for those power supply aficionados.

**Dave Jones:** And the power supply is made by a company called Integrated Power Design, made in the USA. Now, to get this top metal cover off, it looks like it's attached Well, it's you can disconnect the back here and that sort of hinges up and it's held with the It looks like it's held with these bunch of whole bunch of Phillips screws on top here, which hold down some of the

**Dave Jones:** shields here on the ADC front end by the looks of it. So, let's take these off and see if it just lifts straight off. Now, the screws on top here are really quite long and they go penetrate all the way through into the bottom block and you can see the shielded blocks in there, which is no surprise.

**Dave Jones:** It's got a 1 GHz front end, so you really want some decent shield in there. So, it goes all the way through those two blocks on both sides of the PCB.

**Dave Jones:** And it's fairly easy to guess what these four uh high ceramic hybrid packages are in here. There's no surprise that there's uh four of them. Uh that they're obviously the uh hybrid analog-to-digital uh converter for each uh channel.

**Dave Jones:** But why um channel 1 and channel 2 here has a much smaller heat sink than these two, I don't know. I guess it was a bit of a compromise that uh the power supply had to fit uh along here, and uh they just found that uh they had to lower these uh heat sinks just to fit the power supply in, and it was probably good enough.

**Dave Jones:** So, they thought, "Oh, we'll put a beefier one on here." And uh well, that's what they've done. Clearly, they put uh larger heat sinks on these and smaller ones here because these are obviously uh duplicated um across all four channels.

**Dave Jones:** It's coming out. Ta-da! There it is. And that's just a beautiful integrated design with the metal work. They've got the uh shielding here between the uh channels on the input and the uh So, we've got there four uh analog um uh channels here with some hybrid uh action there.

**Dave Jones:** We've got our um trigger external uh trigger here and our calibration. And it separates uh shields in between all of those. Brilliant. I like it. We've got our four uh clearly uh analog-to-digital uh converter hybrids over there.

**Dave Jones:** We've got a clock oscillator over here. And we'll go away and uh looks like we've got uh sample memory up here by the looks of it. I It's a really nice bit of system design.

**Dave Jones:** I love it. And once again, we've got more of that crap that's blowing in all along here by the fan. It's just uh crud. We're going to have to clean all that out.

**Dave Jones:** Well, where do you start with this board? Well, let's do a visual flyover. And let's take a look at the uh sample memory. They've got two boards here uh to share the four channels.

**Dave Jones:** So, there's obviously uh two channels per board, and there's um eight channel eight chips uh per channel cuz there's um eight on the top and eight on the bottom.

**Dave Jones:** So, and these are uh Toshiba 32K um high-speed uh SRAMs. So, they're um that means there's uh 256 um K per uh channel of the scope. And they've got some bulk tantalum decoupling up here, I should expect.

**Dave Jones:** Um and they've got these um high-speed um uh board-to-board interfaces as well. And there's some uh looks like there's some extra memory under here. And oh, hey, that looks like a bodgy mod wire.

**Dave Jones:** Let's check it out. And they've got some 74ABT uh logic there. And they've got a mod wire on that. They have celastic it uh downed globbed it down. So, I love this sort of thing.

**Dave Jones:** There's a few uh mods throughout this scope, actually. And if you look carefully at these connectors, you'll find that they're not actually soldered. They're just a um a uh spring terminal press-fit uh type connector.

**Dave Jones:** And here's the ceramic hybrid uh analog-to-digital converter. And it's a dead giveaway. It's a HAD, which obviously, well, presumably, stands for hybrid analog-to-digital converter 61-80. That's probably an internal proprietary thing.

**Dave Jones:** Probably are spun internally by LeCroy or I don't know who would actually manufacture this, but interestingly, they've each one's got a handwritten number on it. So, these are probably individually tested and they may be even been as well to match them to match the performance of the time and or whatever between the all four channels on this particular scope cuz they do have different numbers.

**Dave Jones:** This one over here has number 54, 104, 56, 140. And of course, that's not really surprising. You'd expect that in these really high-performance 1 GHz type scopes that they would actually individually been and match these analog-to-digital converters for this particular scope.

**Dave Jones:** You know, there's probably some wise old guy with a gray beard there. He strokes his beard and sticks his tongue out the right angle and tests and and measures each one and then bins them individually.

**Dave Jones:** And that's what you're paying for. I'll tell you what I'm not keen on. These freestanding TO220s that can just wiggle. Vibration is a big problem for this sort of mount.

**Dave Jones:** I'm surprised they've done that. And they've done them and there's another one over here which is bent to an angle. At least these ones have heat sinks attached to them and there's another couple over here which they have heat sinks, but they are actually soldered down one side.

**Dave Jones:** So, that's not too bad, but come on. These standing TO220s not acceptable. And they've got a 10 MHz TXO or a temperature compensated crystal oscillator in there. And this metal can, I can't get that off.

**Dave Jones:** It looks like it's soldered down in a couple of corners. I might have a go, but I think it might be soldered in. I I would guess that maybe is the uh phase-locked loop that uh um takes your 10 MHz and ups it to your uh sample rate required high sample rate required for the analog-to-digital converters.

**Dave Jones:** That'd be my guess anyway, but uh if you got a better guess, let me know. And they've got a DAC 8800 one between two hybrid modules and that's a octal 8-bit digital-to-analog converter.

**Dave Jones:** So, they obviously need four DACs there per analog channel for some reason, offsets and uh possibly things like that. And that's supported by a couple of LF 347 op amps.

**Dave Jones:** And there's another huge quad flat pack on the top side of the analog-to-digital hybrid once again one for each channel and I can't look at the number on that.

**Dave Jones:** They got the heat sink well and truly stuck on there, the bastards. And there's a couple of trimmers in there associated with each one up there. And what their function is, well, your guess is good as mine.

**Dave Jones:** My guess is that it's some sort of custom glue logic from the ADC into the sample memory just by its physical placement there. You can tell that you know, these things are the operation of these things is fairly obvious.

**Dave Jones:** I mean, you got your analog-to- I mean, sorry, you got your front end over here which then flows into your analog-to-digital converter for each channel and then this is some sort of custom gate array which I don't know.

**Dave Jones:** You know, buffers and does whatever it does some magic in there and it stores it's some sort of memory controller or something and then it stores it in the high-speed SRAM up here.

**Dave Jones:** And it's obviously got some sort of memory controller in it cuz not only does it have to handle writing the data to here, but it also has to handle reading the data back out for the main the main software processor which then displays the data on the screen.

**Dave Jones:** So, it's got to have that dual path access. And it would also have some smarter logic which ties the sampling between channels because you can actually with these Lecroy scopes or this particular model anyway, you can actually choose if you're only using one channel, you can actually store the samples across all four channels and you can get a fourfold increase in your sample rate as well if you're only using

**Dave Jones:** one channel. So, these controllers probably handle all that sort of stuff. And if you have a look around this part, we've got these Thesis brand chips as well. And if you remember before we actually saw that on the processor control board, that's a TH1001.

**Dave Jones:** This is a TH4022 and this is a TH1106. I have no idea what they do, but they're obviously custom Lecroy branded parts. Once again, we've got some gal/pal devices here and some other miscellaneous logic.

**Dave Jones:** And this device here in a fairly old school PLCC package, that's probably some sort of local processing would be my guess. And this is our calibration waveform generator section.

**Dave Jones:** They've got some voltage negative voltage regulators here as you'd expect and they've got some analog switches here by the looks of it and some op amps and that's, you know, pretty much what you'd expect in a basic waveform generator.

**Dave Jones:** And here's the top half of our external trigger circuitry. It's got its own oscillator. It's got its own crystal here, 14.31 MHz and quite a few ICs here with heatsinks stuck on them.

**Dave Jones:** So, I can't exactly see what those are, but this is the external trigger circuitry and this is the bottom half of it here. We've got a DG508 multiplexer there and just some miscellaneous stuff.

**Dave Jones:** And once again, we've got a couple of budge resistors on here, as you can see they've had a little tweak there. Oops. And there's a fair bit of discrete stuff around there, as you'd expect, and the rest of it is just muxes and op amps and things like that.

**Dave Jones:** There's a trimmer cap in there, but I guess there's a fair bit going on inside those devices under the heat sinks. There's an Analog Devices AD705 bipolar JFET op amp.

**Dave Jones:** And towards the center here, we've got a couple of more trim pots and another device I don't know what it is, and a little riser board here with a couple of passive components and a SOT23, and there's two MEL resistors actually paralleled up on there.

**Dave Jones:** And there it is. I just love this classic budge stuff. It's brilliant. And of course, we have the LeCroy custom hybrid here. You know, who knows? It's you know, some sort of high-speed differential amp or something like that, and it's actually clipped down onto the board here.

**Dave Jones:** I'm not sure why they've done that. Got a DG202 analog switch here, and up here we've got an LM339. Old school. Terrific stuff. This is rather curious. A ULN2003 Darlington transistor array.

**Dave Jones:** That's the last thing I would have expected to see in something like this. Some 74 series logic up here, a couple of um uh 0.1 inch pin headers. I'm not sure what they're doing.

**Dave Jones:** Another Analog Devices device, and well, that's about it for the 1 GHz front end, unless there's something on the bottom side, which we can't see from here. And if you take off a whole bunch of screws on the top of the board, bingo, it just comes out, and we can access the bottom side of it.

**Dave Jones:** Looks like there's some coaxials on there. And there's the bottom of the base board, and I'm quite surprised to see these uh coaxials. What these are, I have no idea.

**Dave Jones:** Your guess is as good as mine. Uh we've got a couple of coaxials up here going into channels um two and three. And why they're going to two and three and not uh one and four as well, I've got no idea.

**Dave Jones:** And uh there's a bunch of uh miscellaneous uh circuitry across here which um lines up with the uh hybrid um analog-to-digital uh converter modules. And that's the bottom part of that uh memory uh management chip, I guess uh ASIC, I guess you could uh call it.

**Dave Jones:** On the top side, they've got some uh bulk uh decoupling there and a few other uh passives. And there's also a um I don't know what that device is there, but it's uh probably some sort of uh driver or something like that, perhaps.

**Dave Jones:** And the bottom of each uh ADC hybrid has got a whole bunch of passives plus uh these ICs there. Function unknown. Um and once again, that uh bridges over into the uh mini memory management uh device here.

**Dave Jones:** So, that indicates that that is um some sort of uh driver or something like that, perhaps. Um Now, if you take a look over here, and here's the analog uh front ends uh one through four, the base of them, and the uh eight hybrid ADCs here.

**Dave Jones:** And you can clearly see the uh serpentine uh differential pair traces here. And this uh trace here would be coming out of the uh final differential uh buffer amplifier, which would drive it into the ADC.

**Dave Jones:** That'd be the ADC uh driver. And this trace here would uh precisely match the length of this trace here and the other traces on the other channels, so that your uh skew so that your timing or your skew between channels is as near to identical as you can get it.

**Dave Jones:** On the bottom side of each analog uh channel here, an AIS high-quality uh relays in there. So, they're all the relays you can hear go click click click click when you power the thing on or when you change ranges in auto range.

**Dave Jones:** And this is what the clips hold on to underneath that hybrid module in the front end. And you can see clearly that it is actually a a circular heat sink like that.

**Dave Jones:** They've put those ridges in there to help with the to help increase the surface area for the power dissipation. So, there may even be a hole on the bottom side of that board.

**Dave Jones:** That'd be my guess. A hole on the back side of that chip and that heat sink would actually contact directly through to the device. Perhaps. Either that or it's got some thermal vias in there.

**Dave Jones:** A whole bunch of, you know, dozens and dozens of thermal vias to actually connect the bottom of the device, which would be the thermal pad, through the heat sink on the bottom side.

**Dave Jones:** And we've got another dodgy resistor over here going towards the processor board. No idea what it is. Probably a pull up or pull down or something. They probably found some erratic behavior or something like that after they designed the thing and go, "Ah, we'll fix it.

**Dave Jones:** We'll just whack in a pull up or a pull down. She'll be right." So, there you go. That was a rather interesting teardown. Now, what I want to do is actually attempt to troubleshoot this and find out what's wrong with it.

**Dave Jones:** Now, there's first thing you're going to look for is any physical damage. Nothing seems to be blowing up, overheated. There's no capacitor leakage. There's no capacitor bulges here to indicate those caps are gone.

**Dave Jones:** So, you know, it's There's no physical signs at all. So, it's going to be something electrical, I think, perhaps, or something that has failed that's obviously that hasn't manifested itself as a physical failure.

**Dave Jones:** Now, looking over this board, there's one thing that I don't find and that's any test points and especially any labeled test points like voltage test points. I mean, these are, you know, I can measure these voltage regulators here and I will do so, but yeah, there's just no, you know, I expected it'd be nice to see just a bunch of connectors and bunch of test points there saying, "Okay, measure

**Dave Jones:** here for 5 volts, for 3.3, make sure it's all hunky-dory." But, there's not. So, I don't see anything labeled on the power supply either. So, I'm just going to have to suck it and see.
