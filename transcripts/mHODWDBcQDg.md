---
video_id: mHODWDBcQDg
title: Tektronix 2225 Oscilloscope Teardown and Calibration - EEVblog #208
url: https://www.youtube.com/watch?v=mHODWDBcQDg
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 38, "3": 49, "4": 69, "5": 84, "6": 101, "7": 119, "8": 133, "9": 145, "10": 161, "11": 175, "12": 194, "13": 213, "14": 230, "15": 247, "16": 261, "17": 277, "18": 289, "19": 304, "20": 319, "21": 332, "22": 346, "23": 361, "24": 377, "25": 394, "26": 410, "27": 426, "28": 441, "29": 454, "30": 472, "31": 491, "32": 507, "33": 525, "34": 538, "35": 554, "36": 570, "37": 585, "38": 601, "39": 618, "40": 631, "41": 645, "42": 660, "43": 673, "44": 688, "45": 702, "46": 717, "47": 730, "48": 745, "49": 761, "50": 773, "51": 788, "52": 799, "53": 811, "54": 824, "55": 841, "56": 855, "57": 872, "58": 886, "59": 898, "60": 914, "61": 928, "62": 942, "63": 961, "64": 973, "65": 989, "66": 1002, "67": 1018, "68": 1036, "69": 1048, "70": 1063, "71": 1082, "72": 1102, "73": 1116, "74": 1133, "75": 1150, "76": 1165, "77": 1180, "78": 1194, "79": 1204, "80": 1216, "81": 1229, "82": 1243, "83": 1256, "84": 1269, "85": 1285, "86": 1297, "87": 1310, "88": 1321, "89": 1335, "90": 1347, "91": 1359, "92": 1373, "93": 1390, "94": 1405, "95": 1417, "96": 1433, "97": 1446, "98": 1463, "99": 1480, "100": 1493, "101": 1505, "102": 1519, "103": 1536, "104": 1551, "105": 1565, "106": 1580, "107": 1595, "108": 1614, "109": 1628, "110": 1643, "111": 1658, "112": 1670, "113": 1686, "114": 1701, "115": 1715, "116": 1731, "117": 1749, "118": 1773, "119": 1793, "120": 1805, "121": 1819, "122": 1831, "123": 1846, "124": 1863, "125": 1875, "126": 1890, "127": 1903, "128": 1918, "129": 1942, "130": 1968}
---

**Dave Jones:** Hi, a while back I got this really nice Tektronix 2225 oscilloscope and I did some basic checks on it. Well, fairly reasonably comprehensive checks anyway and found that the vertical and the horizontal calibration was slightly out. So, got

**Dave Jones:** the service manual for it. I thought we'd do a bit of a teardown and see if we can tweak this thing just a little bit to bring it back into cal. So, let's go.

**Dave Jones:** To take it apart, there's only a couple of torques screws on the side here. I don't think they're original. There's one missing, so I'm not really sure what's going on there, but you undo those screws and it should just slide

**Dave Jones:** off. That's how most scopes work, so let's give it a go. And if you're going to put your scope face down on the bench, just be aware of the controls and how far they protrude. Usually they protrude further than the

**Dave Jones:** screen like that, but these ones on the old tech scopes are pretty darn robust, but just be aware that that can be an issue and there's a couple of little catches on here like that and you get those off

**Dave Jones:** and we should be able to slide that sucker off. Yep, upside down. Ta-da! There we go. And there you have it. That's inside the tech 2225 scope and we'll take a look at in much more detail, but the first thing I noticed

**Dave Jones:** when I opened this is that the lack of lack of physical control rods like this one here going back to various circuit boards. And if you've ever opened up lots of old scopes like this. I just loved the

**Dave Jones:** design that went into them because all the controls on the front would have these lovely mechanical rods going back to vertical PCBs at the back and all sorts of things. And then they'd have right angle ones, which ah it was just

**Dave Jones:** beautiful. But ah all we've got here is most of the controls here are mounted on the front panel. There's a couple which go through the vertical ones here go through we'll take a look at the horizontal go through to a gain to

**Dave Jones:** switch there. And there's only the one rod that's for the focus adjustment which goes all the way back to the supply at the back. But yeah, apart from that it's not as elegant it's more modern than some of the older

**Dave Jones:** traditional scopes. So I just find it it's not really as exciting or as sexy. Now it's a four board construction here. We've got the front panel one we mentioned which holds the front panel controls. We've got the vertical

**Dave Jones:** amplifier panel and that it does some horizontal as well probably some time base stuff because that's the horizontal going into there. We've got a high voltage power supply vertical board under there. I love that they've got this plastic

**Dave Jones:** plastic protection thing up the front for people who start poking around inside these things. Everything high voltage is under there. And then we've got the main one main large board on the bottom of the case. And if you flip it up here like this and take a

**Dave Jones:** look at the bottom you can see that's one large board. I love it. And once again, we've got this high voltage plastic plastic protection plate here with high voltage warning on it. It's nice design. I love it. And there you go. We've got

**Dave Jones:** AC line potential and CRT high voltages under that. So, take that sucker off at your own risk. And we've got some 100 V DC stuff around here. Nice big danger warning sign again. But apart from that, they've done a really good job of

**Dave Jones:** isolating those high voltage components. And so, you can just dick around on the back, calibrate, troubleshoot, do whatever with the scope operational. And up in the corner here, we have a little bodged resistor. Well, it's not a little bodged

**Dave Jones:** resistor. It's quite a decent size. A couple of watt beasty. And it's that's obviously either some sort of repair or some sort of you know, I don't think it's a factory mod. It may be. I don't know. Anyone else

**Dave Jones:** with a with the same scope? Is your one got the same bodged resistor on it? There's one thing I really love about this scope. Not only the double-sided layout, which we'll talk about in a minute, but it's all through hole, which

**Dave Jones:** means that we can access all components on the back. But, every component on the back of this board, they've put the silk screen designators and the markings from where to where that all of the resistors and and the

**Dave Jones:** various ICs and test points as well. It's just it's brilliant. I love it. Somebody's put a lot of effort into the layout of this board and my hat's off to them. And of course, the beautiful part about the double-sided layout is that

**Dave Jones:** you can access every single component on here. You can troubleshoot everything. So, when you've got all the information on here with the with the schematic diagram and the service manual, you can do everything at the back of the scope.

**Dave Jones:** You don't even have to probe, you know, get down inside the guts of the scope. You just probe everything from the back. It's brilliant. Why isn't all gear designed like this? I love it. As for the layout itself, it's just beautiful.

**Dave Jones:** If you've ever laid out a board of this complexity, like a double-sided through-hole board like this, of this sort of complexity with this number of components, you'll realize the amount of work, effort, and sheer talent and artistry which goes into laying out a

**Dave Jones:** board like this. It's just It's brilliant. Now, the true test of any double-sided board layout to see if it's been laid out properly is how many jumper links that you can see in here. And well, I'm struggling to see any at

**Dave Jones:** all. There's a couple down here, but it looks like they're They're actually deliberately in there as voltage test points, and they're labeled as such or voltage links so that you can actually disconnect each voltage rail and perhaps measure the current as well. They might

**Dave Jones:** actually be current measurement shunts. Maybe that's what they're actually for. If you see in there There we go. We've got one down in there, and it's there There was enough room for a trace to go in there, but they decided to add a link

**Dave Jones:** and they've labeled it plus 8.6. There's another one here, and there's all the way along here. I reckon they're designed for ease of servicing and ease of troubleshooting so that you can actually cut those links and actually measure the current on that particular

**Dave Jones:** rail. But as for the links, I'm having a hard time actually finding any on this board. It's not easy to look under the vertical board here. We'd have to take that out, but really, I You know, I'm struggling to

**Dave Jones:** see any links. So, this thing has been laid out with a hell of a lot of talent and care and blood, sweat, and tears, I'm sure. Now, there's one thing I'm not noticing inside this scope, and this is

**Dave Jones:** something you got to really look for in vintage scopes, especially Tektronix ones are a bit be for it, is using custom hybrid modules and things like that, but it looks all fairly fairly discreet stuff. I'm not recognizing some of the numbers of some

**Dave Jones:** of the ICs offhand, but they're they're certainly not custom hybrid type things. Although you could say that this little one down in here is a little on the vertical board there that custom resistor. That looks like a thick film resistor

**Dave Jones:** hybrid there, but yeah, you know, apart from that it all it uses pretty much all discreet circuitry, transistors, basic op amps and digital you know, 4000 series logic ICs and so on. Now, I just checked and that MC

**Dave Jones:** Motorola MC3346 for example is a transistor array. It's got a differential pair plus a couple of discreet transistors in there. So, you know, they've decided to use an IC instead of that. Maybe for a thermal matching or you know, something like

**Dave Jones:** that, but yeah, apart from that if you uses all sort of you know, more discreet components on here then it makes it much more serviceable because if you get one of the more advanced tech scopes for example and

**Dave Jones:** they've got one of those hybrid modules in there. If that fails, you are screwed. You've got to find somebody who you know, um still has that board, but even if say that transistor array they're failed and you couldn't get it anymore then the

**Dave Jones:** chances are you could actually budge up a circuit to actually replace it. And they've been smart here. The trim pots that are obscured by boards on the on the top side here, they've actually drilled holes in the backside of the board so

**Dave Jones:** that you can adjust the pot through the back like that. I can just stick my screwdriver in there and adjust it, but you can see these ones here don't need that because you can actually adjust those from the top. If you flip it over here,

**Dave Jones:** you'll notice that those pots down in there, these ones down here, these these brown ones down in there, they can all be adjusted, but the ones that are fouled by this top board here, they will have the cutout on the bottom of it. I

**Dave Jones:** love it. And these warnings you really have to take heed of. We're on the CRT here and there's a 7 kV anode voltage. And really, this is the dangerous inside oscilloscopes, and you do not want to touch it unless you

**Dave Jones:** know exactly what you're doing. So, you do not want to touch this. You don't want to disconnect that unless you know what you're doing, you've got experience in doing that. And the anode lead goes all the way over

**Dave Jones:** here and curiously, it is actually connected Well, it's it's not connected, but it's just held down there with a with a plastic retaining clip on the vertical board, but that one goes through here onto the high into the

**Dave Jones:** high voltage circuitry under there, and you don't want to play around with that sort of stuff. Kill yourself. And there's your voltage multiplier in there which generates your your 7 kV for the CRT, and that comes from a mains

**Dave Jones:** vertical the vertical mains board in here. That's why they've got the big plastic cover on it with all the warning stickers. And really, anything in this area you don't want to poke around with unless you absolutely know what you're doing. And again,

**Dave Jones:** there's more warnings down in there on those high voltage capacitors down in there. Discharge before touching terminals. And you'd better heed it. And we've got some power resistors here coupled into heat sinks which are then coupled into the chassis here and at the

**Dave Jones:** back as well for power dissipation. And you see that in quite a few places. And you can see it here as well. Uh These transistors or regulators or whatever they are connected to their own heat sink and they were the two screws that

**Dave Jones:** we saw on the backside of the case. So, that's a design to couple the heat into the case as well as well as actually retaining the heat sink and stopping it vibrating off and things like that because if you left that larger heat

**Dave Jones:** sink just standing there vertical like that, you would get all sorts of resonant modes when you transport it and when you vibrate the instrument if you got it on a trolley or something like that. And it can just start snap off and

**Dave Jones:** ruin your day. Now, if we take a look at the vertical board here, as you can see these are the two vertical channels here. This is the horizontal ganged switch we've got here. These holes in there, there's actually pots down in

**Dave Jones:** there. There's little trimmer or caps actually trimmer caps. That's for the attenuation compensation for each channel so you can get in there and adjust the compensation for the for the voltage for the input voltage divider. And then they've got a pot as well which

**Dave Jones:** is linked through to the control on the front cuz the control is not only a switch but it's also a it's also got a rotary pot on there. You probably can't see it but there's the pot at the back

**Dave Jones:** there. You can see it turning when I rotate the switch on the front and the rest of it is all a a ganged switch in there. So, it's a totally custom thing. So, something like that fails, well, you

**Dave Jones:** know, you have to try and repair the contacts or something like that or you have to get a new board and salvage it, get a scrapped unit with a working channel or something like that. But these are the sort of things you can

**Dave Jones:** actually repair the contacts in if you really want to go to the effort and take them apart and things like that. There's various techniques you can use. And there's the horizontal uh gain switch. And if you look carefully in there, you

**Dave Jones:** can actually see the multiple uh channels cuz there are um quite a lot of channels inside there, and I love that click dot dot dot nice click mechanism. It's shame the verticals I'm moving the verticals and they have like a spongy

**Dave Jones:** feel to them. But uh the uh horizontal um time base gain switch there really nice custom mechanism. But once again, you know, if it fails, you might have to um take apart these uh sandwich uh contacts or something like that and maybe uh

**Dave Jones:** re-surface them or lubricate them. And once again, it's got a trim pot on the back here, and if I turn the um center horizontal, you can see that uh that mechanism in there um turns the turns the pot. So, it's you know, it's fairly

**Dave Jones:** basic stuff, but there's a lot of um effort goes into actually designing a custom gain switch like that. And there's something you don't see every day, made in Holland. Beautiful. Haha. Copyright Tektronix 1986. So, at least this uh top this uh vertical uh

**Dave Jones:** attenuator and time base board is made in Holland. I'm not sure of the uh rest of it, but uh this board is at the very least or maybe the entire scope is manufactured in Holland. I don't know. But uh there you go, copyright 1986. So,

**Dave Jones:** we have a um a reference uh point for the manufacturer of this thing. I'm not sure how old this scope was. It would have had a uh a decent uh product uh lifetime of 5 plus years or something like that.

**Dave Jones:** And perhaps I um after thought here, they've got some uh decoupling uh on this particular chip. And uh once again, it's duplicated on uh both uh channels. So, it may be um an after thought. I don't know. Or maybe they it

**Dave Jones:** was so it was so critical that they had to get the cap directly on the pins of the device. Who knows? But it's well done in either case. It's actually well formed and well soldered. Doesn't look like it's been hacked on. It's a rather

**Dave Jones:** unusual looking trimmer cap there. I can't say I've seen one that looks exactly like that before. It's rather unusual. And this one up here for channel one is actually been bent at about 45°. Now, I'm not sure if that's

**Dave Jones:** an afterthought because it could have failed this focus control rod here, but yeah, it looks like it's been bent on purpose. And the CRT itself made in USA, USA, USA. And if you're wondering what this big coil of wire is over here,

**Dave Jones:** that's actually a a delay line. It runs from down here and it goes around the CRT a couple of times because well, it's just convenient to do that, I guess, and goes into the back part of the board

**Dave Jones:** here. And you can see the structure of the delay line like that. It's like a plastic tube with the wires wrapped around inside there. Some more attention to detail to make the adjustments accessible to the user. These trim pots

**Dave Jones:** here are vertical, of course, because this is the CRT here. This is right over the top. And this little trimmer cap there, they've actually bent that at 45°. So, that you can access it. I like it. A bit of a botch here. They've got

**Dave Jones:** these two toroidal core inductors here with a series resistor. They've lifted up one side of the of the inductor and they've actually put a series resistor in there. Go figure. Now, on the front panel PCB here, they don't really have

**Dave Jones:** any high frequency or critical stuff at all. It's just the, you know, controls like, you know, vertical adjust and horizontal position adjust and stuff like that. Everything else the actual signals themselves go directly into these cans and we'll be able to should

**Dave Jones:** be able to see that on the bottom there they might have a little bit of trigger stuff going through here but generally speaking it's going to go straight into something like this shielded can especially when you're trying to get 500

**Dave Jones:** microvolts per division which this scope is capable of. Now here's the channel one and the channel two input BNC connectors and you'll see that they actually go straight over here they're they're actually discrete wired with these flying resistors here

**Dave Jones:** straight over into the AC DC selection switch in there which is directly on the front panel down in there as you can see there's the AC coupling cap and then it goes directly through a shielded shielded penetrator pin there which actually penetrates that

**Dave Jones:** metal shield down in there which is the main input amplifier. So it basically is just the AC DC DC coupling selection bang straight in. Now although the BNC itself is actually earth to the front panel cuz all scopes like this are mains earth

**Dave Jones:** reference very dangerous if you don't know what you're doing when you're taking measurements you can blow the crap out of your probes and all your scope but anyway they've taken and they've taken an additional grounding a fairly heavy grounding strap

**Dave Jones:** there probably up under there directly as a more of a direct a lower inductance lower impedance path directly into the vertical amplifier. They're not just going to rely on the chassis return because that would be that that would provide very

**Dave Jones:** poor high frequency performance. And there is one other rod in this I forgot to mention but the mechanical power switch here on the front actually goes back via this black rod which you see going back here it goes back into

**Dave Jones:** the um, input board. There's a green You probably can't see it, but there's a, uh, green, uh, power main switch right down on that vertical mains input board. And on top of the CRT here, wedged between the top of it and, uh, the top,

**Dave Jones:** uh, inside of the, um, front panel here is a little, uh, spring and that would take out any, uh, vibration response, um, during, uh, shipping and handling and things like that, just so you don't damage the CRT. Now, it's time to calibrate this, uh,

**Dave Jones:** because if you remembered when I actually, uh, did an incoming inspection on this when I bought it, um, it was, uh, slightly, uh, reading slightly low on all that consistently low on both channel 1 and channel 2, uh,

**Dave Jones:** vertical. It was out by, I don't know, 10% or something. It was quite significant. Um, so I just wanted to tweak that up and I think the horizontal was, uh, slightly out as well. So, I wanted to tweak that. So, um, I've got

**Dave Jones:** the service, uh, manual for it, um, because that's the best way to do it. You don't want to have to, um, because you've seen the number of trim pots in this thing. It's got, you know, a dozen plus, uh, trim pots and you

**Dave Jones:** don't just want to, uh, guess which one it is. You've got to know exactly which one it is cuz there's so many adjustment, uh, controls on this. There's, uh, balance and offset and and gain and all sorts of things and and really you don't

**Dave Jones:** want to muck around with them, um, unless, especially if all the others are in cal, you don't want to dick around with them. So, it's best to find the exact control. So, the service manual says, um, R145, um, adjustment pot is the one to use for

**Dave Jones:** the vertical, uh, gain and that's all I'm interested in. So, I had a look around inside here and, um, I'm buggered if I could find R145. So, I had to actually admit defeat and, uh, scroll through the service manual

**Dave Jones:** here and actually find it's got, uh, adjustment locations for the, where all the pots are and I thought it would be on the vertical board, but it's not. It's actually on the main board, uh, 145 and R1 95, I think it is is the other one for

**Dave Jones:** channel two. And they're actually under the uh CRT. So, let's go find it. Well, go figure. There they are tucked under there. We We looked at those before. Um, and that would have been my last guess literally for where the um vertical gain

**Dave Jones:** uh amplifier adjustment pots would be. I thought they'd be on the top here in the uh on the vertical board where there's a whole bunch of uh pots on there. But, no. As it turns out, they're it. In this

**Dave Jones:** case, um our 195 um Sorry, our What is it? Uh yeah, our 195 there for channel two. And this one under here, channel one. So, let's play around with it and see if we can tweak it. Just one

**Dave Jones:** thing to remember when you are moving these things around uh when they're powered up, just remember there can be some dangerous voltages in there even though um you know, it really sort of protects you from the dumb stuff here.

**Dave Jones:** But, you know, you want to keep away from the CRT and that sort of stuff. And really, it's always uh safety first. The service manual recommends using a 20 mV peak-to-peak um sine wave. It doesn't uh say It doesn't recommend the uh

**Dave Jones:** frequency. So, I'm using 1 kHz using my um Tektronix 3000 series scope here to generate that. And uh as you can see, 20 mV. Um I would have actually which is only four divisions on a scope. I would

**Dave Jones:** have actually much preferred to do eight divisions. Anyway, um that's what it says to use. So, we'll just use that for starters and uh see how we go. So, I've fed that into the uh scope via a 50 ohm

**Dave Jones:** um terminator is on the end here. And let's see if we can adjust that um tweak that pot on the side to uh get our even to get the exact level or pretty close to it. Now, when you're adjusting uh

**Dave Jones:** scopes like this, get yourself one of these insulated uh adjustment tools. They're a uh low reactive um adjustment tool so that um it doesn't you know it it's not metallic of course. So when you're reaching inside probing around you're not going to kill yourself

**Dave Jones:** and be it doesn't actually add any capacitance or reactive components to the sensitive sometimes if you've got little trimmer caps or something like that you can upset their value. So get one of these little alignment tools they cost next to nothing. Okay now what we

**Dave Jones:** want to do here is we want to our input signal here we want AC coupling Okay first of all we want to ground it like this and we want to get the position smack in the center. So we

**Dave Jones:** want to get smack on that center line like that switch it to AC coupling so that there's no offset issues or anything like that and as you can see it's reading low it should be four divisions because we're on five millivolts

**Dave Jones:** per division on the times one because we're not using a times 10 probe here of course. So I've got my adjustment pot over there there it is and I'm going to tweak it and as you can see with this

**Dave Jones:** alignment tool my hand looks like it's inside the scope but it's not it's actually all the way outside allows me to adjust that uh trim pot without any danger at all. So we tweak that up to it's maybe the position is

**Dave Jones:** yeah the position is slightly off. There we go. Let's put it back and you just want it so that the top of the waveform there just touches the those four divisions. So there we go four divisions peak to peak and I set my

**Dave Jones:** generator for 40 millivolts peak to peak and what do you know it is spot on as well. And we've checked out this before but we'll just double check we'll turn up the 10 millivolts per division and it's smack on four divisions there for

**Dave Jones:** 40 millivolts and then 20 obviously is two but let's uh go up to a higher level and see if we can and see if that's spot on as well. Okay, in this case I've got it set to 800 mV peak to peak on my

**Dave Jones:** generator and there you go, it's pretty darn close to spot on. I like it. There you go, that's eight divisions. Perfect. And let's do the same thing with channel two. So, we'll plug it in there, we'll switch over to channel two and we need to

**Dave Jones:** trigger from channel two, of course. And let's do the same thing. We'll ground that, we'll take the position up, and we'll AC couple that. And as you can see, it's short. There you go. So, we have to adjust the trim pot. Let me get

**Dave Jones:** in there and tweak that. Now, of course, we could have done this back down at 20 mV as they claim in the manual, but ah we'll do it at that and that's perfect. Spot on. Channel two's done. Now, let's

**Dave Jones:** take a look at the horizontal here and see if we can adjust that. So, if we go up here, we've got adjustment procedures here and we've done the vertical and there's various things for the vertical, by the way. You can have a look at the

**Dave Jones:** service manuals for these type of scopes as as well, but there's all sorts of stuff. There's balance adjustments, there's inverse balance adjustments, there's gain adjustments, there's offset adjustments. All for, you know, very tricky There's lots of them. So, if you

**Dave Jones:** muck around with them, you can really screw the thing up. So, let's go here to the adjustment procedures and we'll go into the horizontal here and find out which pot we need to do to adjust that. So, it's telling us to adjust for a 1 ms

**Dave Jones:** timing and the adjustment pot is 775. That's the one we need to find. And bingo, it's on the vertical horizontal board, go figure. And there it is, 775 * 1 meg gain. So, that's the one we need to tweak. And I spy with my little eye a

**Dave Jones:** 775 there on the vertical board. So, we'll tweak that and try and get this horizontal waveform to pull in. And I forgot to mention, of course, we've got to be on times one mode there cuz this scope has

**Dave Jones:** times five, times 10, and times 50 meg as well. So, they have separate adjustment controls for the magnification, but the one you would mostly use the scope in the times one position. And I forgot to mention, before you do these adjustments, you got

**Dave Jones:** to make sure that the calibrated vernier control, the actual variable adjustment control for both the vertical and the horizontal is all the way into the cal position because if you have it pulled around, you know, if you have it

**Dave Jones:** out of cal like that, then you adjust it at the wrong point. So, it's got to be around in the cal position and there's usually like a detent a detent position at the end of that. And also, you don't

**Dave Jones:** want your times five, well, in this case, times 10 vertical mag on, either. There we go. Use the fine control here to adjust the waveform over like that because as you move it, it will actually and maybe, if

**Dave Jones:** you leave it in the center, it should be fine, but there we go. Here it is. Spot on. I like it. And let's just check that it's still okay in the mag position. I mean, times 10 magnification down here.

**Dave Jones:** I'm in mag mode. You can put it in alt mode where you can get both the waveforms up at once, but we'll put it there and uh it should still be Oh, it's slightly It's slightly off. Uh half a bee's dick.

**Dave Jones:** But we can actually tweak that one, too, using 777, which is another control on the board here right at the back. So, let me tweak that. This is the times 10 mag control. So, there we go, spot on.

**Dave Jones:** Just tweaked it just a tad. Perfect. And times five mag mode here, we're out on that one as well. So, luckily we have a pot for that. It is uh ti- it is a 731. So, let's get in there and tweak that

**Dave Jones:** one as well. Here we go. And bingo, near enough to spot on. I like it. And just go back and check that they didn't uh interact with each other. Times one, we're spot on there. If we go to mag times five,

**Dave Jones:** yeah, the uh offset's a little bit out there. The horizontal uh offset, that is, but that's fine. And times 10 mag, beautiful. I like it. Yep, spot on. And we can go into times 50 as well if you're really uh really pedantic, but

**Dave Jones:** there's no separate control for that. It uh must use the other two, and it's pretty darn close. It's a little bit out, but uh there is no adjustment control for that one. And we'll just do a few quick spot checks on the other

**Dave Jones:** horizontal uh ranges. I've got a 100 kHz signal this time, and it is spot on, no problems uh at all. And you can check the uh mags again for that. And uh yep, just fine. So, let's take it up in

**Dave Jones:** frequency and see what we can get. And using a 10 MHz signal, once again, we're spot on it uh times five mag gain. I've got it. Because this um scope isn't particularly high bandwidth uh in on times one mode, that's as far as it

**Dave Jones:** goes. So, I can't uh get the uh 10 divisions actually across there, but uh in any case, um we can turn on the times five mag, and we are spot on. Beautiful. I like it. I think we've just calibrated

**Dave Jones:** the horizontal and the vertical gain channels. Let's actually count the pots in this thing that I can see. 1 2 3 under there, 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

**Dave Jones:** uh two under the CRT um over here, which we actually um did at it there's a bucket load of them. And there's ones on the bottom um of the main board as well. More adjustment pots than you can poke a

**Dave Jones:** stick at. That's not even counting the um trimmer caps and things like that for all your compensation adjustments. Crazy. Just imagine having to adjust these things at the factory when they first roll off the line, and all the

**Dave Jones:** pots are at center, and all the trim pots are at center or wherever, and you've got to tweak the thing. Oh, man, you'd go nuts. Now, when you're adjusting stuff like this, not just scopes, but any bit of electronics at

**Dave Jones:** all, the most important thing by far is the angle of your tongue. If you don't get it right, it's not going to work. Your adjustments are going to be completely out, and Murphy'll get you every time. Tongue angle number one.

**Dave Jones:** Watch. This is the correct technique. See? It's It's Sometimes left, sometimes right. Varies between the individual, but trust me, super important. Catch you next time.

**Dave Jones:** I almost forgot the most crucial adjustments. You can't do them with two eyes. Must have one eye and the correct tongue angle. Let me demonstrate.

**Dave Jones:** Woo!
