---
video_id: 5kGhoRuhlxM
title: EEVblog #801 - How To Design A Digital Clock
url: https://www.youtube.com/watch?v=5kGhoRuhlxM
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 32, "3": 48, "4": 64, "5": 77, "6": 93, "7": 109, "8": 127, "9": 144, "10": 156, "11": 169, "12": 185, "13": 198, "14": 207, "15": 223, "16": 240, "17": 253, "18": 266, "19": 283, "20": 303, "21": 315, "22": 328, "23": 343, "24": 353, "25": 364, "26": 382, "27": 396, "28": 408, "29": 421, "30": 438, "31": 452, "32": 469, "33": 481, "34": 499, "35": 513, "36": 536, "37": 552, "38": 567, "39": 580, "40": 590, "41": 602, "42": 617, "43": 629, "44": 647, "45": 659, "46": 669, "47": 683, "48": 696, "49": 711, "50": 726, "51": 739, "52": 751, "53": 768, "54": 780, "55": 795, "56": 812, "57": 826, "58": 841, "59": 854, "60": 870, "61": 886, "62": 898, "63": 912, "64": 928, "65": 940, "66": 954, "67": 966, "68": 979, "69": 994, "70": 1007, "71": 1021, "72": 1040, "73": 1058, "74": 1070, "75": 1088, "76": 1103, "77": 1115, "78": 1126, "79": 1141, "80": 1155, "81": 1166, "82": 1179, "83": 1191, "84": 1205, "85": 1221, "86": 1236, "87": 1248, "88": 1265, "89": 1282, "90": 1297, "91": 1313, "92": 1326, "93": 1340, "94": 1355, "95": 1374, "96": 1385, "97": 1401, "98": 1415, "99": 1428, "100": 1443, "101": 1458, "102": 1470, "103": 1490, "104": 1503, "105": 1520, "106": 1534, "107": 1549, "108": 1565, "109": 1578, "110": 1593, "111": 1611, "112": 1625, "113": 1637, "114": 1649, "115": 1661, "116": 1674, "117": 1688, "118": 1704, "119": 1715, "120": 1730, "121": 1741, "122": 1760, "123": 1770, "124": 1786, "125": 1800, "126": 1813, "127": 1826, "128": 1841, "129": 1858, "130": 1870, "131": 1883, "132": 1898, "133": 1911, "134": 1925, "135": 1938, "136": 1953, "137": 1965, "138": 1979, "139": 1994, "140": 2008, "141": 2028, "142": 2045, "143": 2058, "144": 2072, "145": 2090, "146": 2103, "147": 2120, "148": 2139, "149": 2152, "150": 2165, "151": 2177, "152": 2189, "153": 2204, "154": 2219, "155": 2235, "156": 2248, "157": 2263, "158": 2275, "159": 2289, "160": 2309, "161": 2323, "162": 2343, "163": 2357, "164": 2371, "165": 2387, "166": 2403, "167": 2415, "168": 2427, "169": 2439}
---

**Dave Jones:** Hi, with all the recent to-do about clocks, I thought I'd show you how to design and build your own do-it-yourself clock using this example that I built myself back when I was a teenager back in the 1980s. So, I thought we'd take it

**Dave Jones:** apart, hopefully reverse-engineer it a bit because unfortunately I've lost the schematics for this. I did originally, well, I've lost it twice actually. My original hand-drawn you know, scrap notes that I originally uh designed this thing from, I lost that

**Dave Jones:** and then I redrew it I don't know, 15 years ago or something and I've lost that one as well. So, it won't be an accurate reverse-engineering as you'll see inside why, but hey, I thought we'd have a look at it. And this clock sat on

**Dave Jones:** my shelf for a long, long time and it's got features where you can uh accelerate it like that to actually set the time and you can actually get different speeds for that. Look at that. Beautiful and it's got AM/PM indication

**Dave Jones:** and fantastically 1/10 of a second. If you going to design your own clock, highly recommend you add 1/10 of a second. Add some excitement to it. Beauty. Let's take a look inside. And here it is. Please excuse the crudity of

**Dave Jones:** the model. I didn't have time to build it to scale or to paint it. Check out this classic Vero board rat's nest construction. Wow. I made this with basically junk bin parts at the time. I think I only had to

**Dave Jones:** uh go to the local Tricky Dick's store or wherever I went to to just get a couple of parts for the thing. So, mostly like you know, used and salvaged parts from other either other projects or from stuff that I'd torn down. And of

**Dave Jones:** course back in the 1980s there were no microcontrollers that you take for granted these days. So, this is all done with as you'll see uh discrete TTL type chips. I use the term TTL generically. Um these aren't actually uh 7400

**Dave Jones:** series TTL. They're actually 4000 series CMOS. I'm pretty sure all of them are actually 4000 series CMOS. So, let's take a look, but uh jeez, look at this. This This is really embarrassing, isn't it? But hey, you know, this is what you do

**Dave Jones:** because not only didn't you have microcontrollers back in the day, so you designed everything using discrete logic and maybe there's a couple of couple of trainees down in there as well, couple of transistors. And and you build it on

**Dave Jones:** breadboard because yes, I did make my own PCBs back in the day, but I I can't remember. I probably just couldn't be bothered for this one. Um so, you know, I just sort of, you know, hacked it together on a weekend

**Dave Jones:** just using some Veroboard or point-to-point wiring. And this front panel, it's just got a red uh filter, which actually helps a lot. I can show you that with and without that. And the display panel just pops off here and I've got There's the

**Dave Jones:** AM/PM indicator. That's obviously a different type to these other ones. I think I may have got spurred on to build this cuz I may have actually got these from somewhere. I don't think these were I'm not sure if they were salvaged. This

**Dave Jones:** one might be, but yeah, these old ones, I think I got them and I went, "Oh, what can I do with them? Oh, I don't know. I'll make a clock." So, yeah, that's what I did. And I added

**Dave Jones:** some 3 mm LEDs in there. They're just always on to give you traditional colon look that separate your hours from your minutes and your seconds. And obviously, I did a bit of tweaking of the lead dropper resistors. Look at this, all just point-to-point

**Dave Jones:** coming out like that. This one over here needed its own thing. And anyway, um hopefully be able to reverse engineer that. The case I probably salvaged from another project. I believe some of the chips in here, the 4026's,

**Dave Jones:** um, as we'll see, I got those from an old frequency counter. I would continually actually, reuse parts from old projects. In fact, if we have a look at some of the date codes of the chips in here, I did actually salvage some of

**Dave Jones:** the chips out of this clock to build another, to build other projects at the time, but eventually I replaced them. So, we'll probably, if we have a look at the date codes, we might find some like, you know, 1980's

**Dave Jones:** labeled chips, perhaps even 1970's maybe, where I, you know, desoldered them out of products and things like that. But, anyway, and probably replaced with some modern, you know, ones that might have been manufactured in the 90's perhaps. So, I did get it going again at

**Dave Jones:** one point, but yeah. Look at that. Rat's nest construction. Crikey. And those old timers in Australia will have fun memories of Ferguson transformers. Are they still around? I don't know what happened to Ferguson. Anyway, very famous manufacturer, Australian manufacturer of transformers.

**Dave Jones:** And as you might be able to tell, this one was like salvaged out of some bit of gear I tore down and salvaged parts because we didn't have the mail order stuff. We didn't have the Digikeys and the Mousers and everything that you take

**Dave Jones:** advantage for these days. Yeah, we had our local Tricky Dick store here, Dick Smith Electronics, or the local Tandy store if you wanted to buy, you know, two resistors in a packet for, you know, a couple of bucks, then you could do

**Dave Jones:** that. But, you know, it was, it was really worthwhile back in the day to salvage parts from, from products that you actually tore down. So, this fuse holder here would have come from something else. Even the mains cord would have come from something

**Dave Jones:** else. You can see I've just got a a of uh strain relief just tying it in there. It's a bit how you're doing, bit of electrical tape over there, but you know. Um like and the heat sink I would

**Dave Jones:** have got uh from something else. As you can see, it's got some weird pinout in there for, you know, some uh package that it was used from. So, I just bent that over there to sort of fit under

**Dave Jones:** these uh switches. Now, based on my very vague recollection, I reckon that date's probably accurate uh 1987 cuz I think I had this vague memory that I actually went out and bought a couple of parts for this thing, including the uh 7805 5-V

**Dave Jones:** regulator here. So, that one Yeah, it probably dates this clock to about late '87. You can see one of the replaced chips in here, CD4026. As I was very fond of uh 4026s back in the day, as you'll see, very handy little uh

**Dave Jones:** versatile chip, used them in frequency counters and and clocks like this and all sorts of stuff. Um that one's got a date code of uh 1999. So, yeah, that was um one of the chips I salvaged out and

**Dave Jones:** would have uh replaced at a later date. In fact, that's probably when I redrew the schematic, I'd be guessing cuz I did I'm pretty sure I redrew an accurate schematic and bugger it if I can find it though. I went to a lot of effort to do

**Dave Jones:** that. Damn. I think I might have even scanned it in as well on one of the very early scanners, but bugger it if I can find it. And there's a very sorry-looking uh 4013. Is that I Is that '82? I don't know and like so

**Dave Jones:** yeah, I'm not quite sure of the date code, but I think that one's actually got some solder on some of the pins down in there. So, that would have been a um a desoldered chip that I desoldered. Right, probably yeah, in the early '80s.

**Dave Jones:** So, I reused that one. Actually, here's a whole bunch of 4000 series chips from my original stock pile back when I was a kid and uh yeah, you can see look there's a there's a 4013 1984 vintage uh

**Dave Jones:** probably put some more recent ones in there from '92. So, I may have got those from uh who knows? I might have got those surplus parts from a company I used to work at back in the early '90s. Perhaps

**Dave Jones:** there's a there's a sad-looking sight. Oh, yeah, Toshiba part. Look at that desoldered. Still work today, absolutely no doubt. And of course you'd go to that effort because like something like a 40161 wasn't actually one of the more common

**Dave Jones:** chips that you typically find at your store. So, you'd be tearing down a product and you'd go 40161. Jeez, don't have one of those in my stock. So, you'd quickly desolder that and whack it in your junk bin. Well, I think

**Dave Jones:** I found my earliest too. Get the dust off those. Look at that, 4512 from 1975, 1977 a 4011. Ah, terrific stuff. Sorry, I can't help but going down memory lane here. Check out some of the dates, '80, '82, '87, '81, '84. You

**Dave Jones:** know, I It was a different world back then. You had to do this to get a decent um stockpile of parts that you could just uh you know, lash up new designs with. So, there's a 30-plus year-old parts

**Dave Jones:** bin. Haven't had the heart to throw it out. I didn't show the resistors on the side there. They're obviously the dropper resistors for uh most of the uh seven-segment displays at the front here. Just use that 0.1-in pin

**Dave Jones:** headers on the side here just as a convenient point to solder the wires after I did the main board. So, I've got a combination of green wire wrap wire in there to just do main and main circuitry, but all the off-board uh

**Dave Jones:** stuff, it was easier just to put in 0.1 in headers instead of trying to insert um individual wires and have them coming out. And some of this is really messed up. But give me a break, you know, I was

**Dave Jones:** only a teenager at the time. Look at my I got my AC input here. I got diode bridge. I have to tap that off, as you'll see, to uh get the 50 Hz uh mains reference cuz this is not a crystal-controlled uh

**Dave Jones:** clock. It uses the 50 Hz mains, which is incredibly stable over long term. Anyway, um yeah, so yeah, we got some transistors in there doing something. Got a big bypass cap. And uh don't ask me what's going on there. I obviously

**Dave Jones:** bodged something in because I was making this up as I went along. I don't know. Yeah, whatever. And I'll show you the difference that uh red filter makes. We'll whack it in. Whack it in there. Look at that. That

**Dave Jones:** makes a big difference. And you'll notice this segment here is all out of whack. Um that was just like a power-up uh glitch. You know, I obviously didn't get the uh reset correct on that. Here we go. It'll come good.

**Dave Jones:** There we go. It came good. So, that wasn't really a problem. That was just a quirk, you know, I didn't put, you know, decent um like RC power-up uh reset on there and things like that. So, it didn't matter.

**Dave Jones:** Once you actually set the thing, then it worked just fine. And no, there was no battery backup on this thing. If the uh mains failed, then this thing failed. But I had it going for years. We had a

**Dave Jones:** very stable mains. And tada, here it is. A hopefully uh semi-reverse engineered schematic for this thing. It's not complete. I haven't gone in and looked at individual, you know, pin numbers and put all that sort of stuff on here. But

**Dave Jones:** I think I've got the original functionality of this thing in sort of like a block uh chip form. So, you know, if you wanted to build your own from this, you could certainly do it. All you'd need to do is look up the pin

**Dave Jones:** numbers and whatnot. So, hopefully I've got it right. Now, I know this looks messy and stick with me. Hopefully it'll come together at the end. So, what we've got here are our eight seven segment displays like this. They're all common

**Dave Jones:** cathode type, which means that they go down to ground. All the cathodes are connected together and a one on the output of the chip will actually turn the LED on. Common anode is probably more common, but I had common cathode at the time and

**Dave Jones:** it works with the chip that I loved and used a lot back when I was a kid, the 4026. So, anyway, we've got the eight digits here. We've got our tens of seconds display here. We've got our seconds

**Dave Jones:** display here. This decimal point is permanently turned on there, so we had to just have an individual dropper resistor in there just tied to the rail to turn that on permanently. We've got our colon display in here. Once again,

**Dave Jones:** it'll just have two diodes in series with a dropper resistor. We've got minutes, another colon display permanently on, and then we've got our tricky, which we'll go into 12 display. And of course, this one over here, it only has to count up to 12. So,

**Dave Jones:** while this one can go from zero to 10, this one only has to basically do a one or an off as you here because we don't actually display the zero. So, it's it either shows a one or it doesn't show or

**Dave Jones:** it just switches off. And then we've got an AM/PM indicator here that I really didn't reverse engineer. That's just a 4013 um flip flop. That's it to actually do that. And by the way, AM/PM, it's always displaying P here. So, basically

**Dave Jones:** the C segment, that bottom one there, is just toggles off and on basically. That's pretty much all it is. And if you're not familiar with seven segment display annotation, they're always uh labeled like this. So, A B C D E F and

**Dave Jones:** the middle one there is G. That's just a common industry notation. Okay, so what we've got here is 240 V mains in just that uh isolation transformer. Don't even know what voltage it is. What is it uh I don't know. 9 V or something. I'm

**Dave Jones:** not sure. Anyway, it doesn't matter. Um then we've got just a half wave uh rectifier here and a uh filter cap and a 7805 to power this whole thing. Now, I didn't actually need the 7805 because the um CMOS chips I'm using can actually

**Dave Jones:** go up to even Well, the 4020 4026s can go up to 20 V. Um so, I didn't really need the 7805. I think I just did that it was just a nicety to, you know, have a known fixed

**Dave Jones:** level uh to work from that no mains variation changes the uh brightness and all that sort of jazz. So, strictly speaking, not needed. And what we do here is we tap off before the halfway rectifier here, tap off the AC. And uh what we do is just uh

**Dave Jones:** diode clamp that uh down here so it doesn't go negative. And then that will actually produce a 50 Hz um pulse into here. You've got a a resistor divider here. And then we can get our 50 Hz clock coming from our mains into this

**Dave Jones:** chip. Let's have a look at that on the scope. And there it is. If we probe pin 10 of our 4040 uh ripple counter here, then we can see that the 50 Hz there it is. Um well, it says 49 on here, but uh

**Dave Jones:** yeah, well, 50. There we go. Oh, look at that. I noticed on the signaling here displaying all those decimal places, but uh looks like we don't have the resolution. So, that's a bit of a That's a bit of a fail.

**Dave Jones:** It's giving you a false sense of precision there. Anyway, that's bang on 50 Hz regulated by um the generators is the uh local power station. No problems at all. So, very accurate long-term 50 Hz. Anyway, here's our uh ground level

**Dave Jones:** here. So, that's being diode clamped negative there to .6 cuz you don't want to damage the chip. And on the uh top side here, I've actually I must be uh clamping it positive because it's just going um just

**Dave Jones:** over the uh rail there as well. Or maybe I chose my resistors to do that. No, I think I'm uh clipping there. So, there you go. We have got a good enough uh 50 Hz input to our 4040 ripple counter.

**Dave Jones:** So, this 4040 binary ripple counter here, it just uh counts up in binary. It's got a I don't know. What is it got eight outputs or whatever. And um we're tapping off the uh Q1 and the Q3 out cuz

**Dave Jones:** what we want to do is divide that 50 Hz by five to give us 10 Hz cuz remember, we've got our 10th of a second display. So, you want that to turn over 10 times per second, 10 Hz. So, you want to uh

**Dave Jones:** decode that on when it switches to six. So, 00011011 100. And when it gets to six, boom, reset the thing here. Now, I've noted that um it should be that easy. And then we can just feed the output of

**Dave Jones:** that into our following stage. But I note that I've actually got a couple of transistors and some uh caps and things down in here. So, something's going on in there. I haven't reverse engineered it. Sorry, couldn't be bothered. Um it's

**Dave Jones:** not terribly easy without looking at the bottom. Um anyway, so I'm obviously doing some sort of um RC uh transistor pulse stretching or something like that just to give a bit of a cleaner clock to the next stage.

**Dave Jones:** So, here's where the magic of the 4026 chip comes in. I love these puppies. As I said, I've used them for everything. And uh what they are is a decade counter uh divider. So, they've basically got a combination of a um BCD uh

**Dave Jones:** counter plus a decoded seven segment output display driver. So, you know, traditionally to do this you need like two chips to do it. You need one for the BCD counter and then you need a BCD to seven segment decoder. But this one's

**Dave Jones:** got them both built in. So it's a single chip solution for decade type counting display. So very useful for frequency counters and things like that. If you want to count from zero to nine and display it on seven segment LED, this is

**Dave Jones:** your man right here. There's the internal circuitry for those playing along at home. So it's got a buffered output and I recall these things you didn't really have to add dropper resistors on the output. They would drive LED displays direct and

**Dave Jones:** it wasn't too much of a drama. If we had a look down here, you know, maximum typical output high source current because that's what we're doing with sourcing because we've got a common cathode display here. So we're and a one turns

**Dave Jones:** the LED on. You know, look we're looking at you know, couple of milliamps but I I do believe I added like a single dropper resistor over here. I think just to dim the display a bit. I think it was

**Dave Jones:** actually too bright and I didn't want the thing glaring all the time. I didn't add an auto brightness adjustment for at night time. So I pretty much sort of you know, experimented with the resistor value in there just to do that. I didn't

**Dave Jones:** put seven resistors in here. I did for the 4511 which we'll take a look at later but it it it had a different output drive and yeah. So but for the 4026 I think I got away with just the one resistor in the

**Dave Jones:** common cathode line here. Experimented with that until I got the brightness I wanted. So at this point it's far too easy. This one ticks over zero to nine uh 10 times uh per second and then it's got a carry out um output pin, which of

**Dave Jones:** course is designed to go into the clock of the next one. So, these chips are designed to be cascaded like this. And there's a companion chip to this, the uh 4033, which has ripple blank in and all sorts

**Dave Jones:** of other things if you uh want to get fancy pantsy, but we didn't need that. So, um just yeah, carry straight into the clock input. The next one counts up 0 to 9, not a problem whatsoever. But what we

**Dave Jones:** want is for this um seconds display here to to count from 0 to 5 and then reset. Well, how do we do it? Well, we do it exactly the same as we did down here with this uh diode AND gate here. We

**Dave Jones:** ANDed these two's together and fed it back to the reset. We do essentially exactly the same thing here. We tap off the digits we want to signify that we've reached the digit 6. And when we get to the digit 6, we want to uh diode AND

**Dave Jones:** gate that here, so that this is just your standard diode AND gate with your pull-up resistor here. And we can ordinarily, imagine that's not there, we could ordinarily feed that straight into our positive reset pin here. But there's a reason why we need these

**Dave Jones:** transistors. And that reason is because the 4026 is a seven-segment display driver. There is no BCD output, no logic level output that we can actually tap off and feed back in because this uh reset pin is a logic input pin. It needs

**Dave Jones:** whatever threshold is required for this particular CMOS logic and your supply voltage. And remember, the output of this seven-segment display here is driving this LED. So, it's not going to be 5 V. It's not going to be outputting

**Dave Jones:** 5 V here. It's actually going to be limited to uh in internally to whatever to the diode drop here down to ground. So, the drop across the resistor here plus the drop across the LED here, red LED, you know, 1.8 V say typical, then

**Dave Jones:** you might have a bit extra drop, Say, it's 2 V, you'll get like 2 V s on this pin here. That 2 V is not enough to actually reset this thing here. Well, actually, that's not strictly true. Um what it is is it's not enough

**Dave Jones:** to actually pull these diodes back to the positive rail up here like this. So, with this pull-up resistor, and of course, you know, we could put this to like 2 V or whatever, and our AND gate would work, but then we wouldn't have

**Dave Jones:** the threshold level required here. So, essentially, it's a combination problem of not being able to operate this diode AND gate here. Hence, why we have to add this two transi- well, two transistor inverters here, so it's a buffer. So, effectively,

**Dave Jones:** we're buffering this thing here. And if we probe one of those LED outputs, there you go, you can see that it's being clamped to about 2 V there. So, that's the LED drop voltage plus the LED drop on any

**Dave Jones:** series resistor. Now, unlike down here, where we actually had the binary output here to decode, we don't actually have the binary output to decode here. It's all internal to the chip. There's an internal BCD counter, but we don't have

**Dave Jones:** access to it. We only have access to the seven-segment decoded outputs. But thankfully, if you look at how a number six is constructed on here with like that, and B is the only one that's not on, then you can work out if you look at all the

**Dave Jones:** numbers 0 1 2 3, and just visualize all those segments coming on for each digit. When you get to the number six, there are three segments segment E, F, and G, and those ones are uniquely all lit up when

**Dave Jones:** we have the number six. So, we're able to tap off segments E, F, and G like this, and the other four just go uh through. Well, they all go straight through, but we tap off E, F, and G. So,

**Dave Jones:** we want an AND gate, hence the diode AND gate, when all three of those segments are lit up, we must have the number six. And bingo, when that happens, none of these diodes are pulled low, they're all pulled high, so therefore,

**Dave Jones:** our resistor is going to pull the base of this transistor high, and bingo, it's going to pull turn this transistor on and pull this low here, and this low here will actually uh turn off this transistor, which will then

**Dave Jones:** pull due to this pull-up resistor here, pull the reset pin high. Bingo. So, as you can see, it just works as one big buffered AND gate. A one, a one, and a one gives us a one on the output. If

**Dave Jones:** there's If it's 1 1 0, we're going to get zero on the output. But those who are keen-eyed might go, "Dave, there's something not quite right with this circuit." And pause the video here and figure out if you can find the fault. If

**Dave Jones:** you want a little fault-finding exercise, there's something wrong here. This, as it's drawn, is not going to work. So, pause the video now, and I'll tell you after the break. All right, did you figure it out? Well, I hope you did. If not, here's the

**Dave Jones:** explanation. Okay, when the output of all these is zero, okay, this is going to be zero. Then let's say, well, it doesn't matter. Even one of the diodes going zero, okay, uh is going to, due to this pull-up resistor, there's going to

**Dave Jones:** be no 0.6 V across that diode, right? So, we've now got 0.6 V at the base of our NPN transistor here. What? 0.6 V diode in there isn't basically exactly the same drop as the base uh emitter junction inside this

**Dave Jones:** transistor, so effectively, this transistor is going to turn on. It's not going to turn on super hard, but it's going to turn on. So, basically, if you just had this arrangement as it's shown, this transistor would always be turned

**Dave Jones:** on, regardless of the inputs here. So, how do you fix that? Well, it's simple. You just add another diode in there like that, and bingo, with basically zeros on the input here, or even 1 0, then we've now got two diode drops to overcome. So,

**Dave Jones:** therefore, this transistor is going to do its business. So, that's actually the true circuit right there. So, that was easy peasy. We now have a display which counts up to basically 59.9 seconds, and then resets, and just repeats that over

**Dave Jones:** and over again. And once again, the carry output of our 4026 goes into our next minutes display now. So, every minute we'll get a pulse out of this carry, and it will turn over this first digit on the minutes display here.

**Dave Jones:** Once again, that counts 0 to 9, no problems whatsoever. But, we've got the same issue we had here with the 59, cuz there's only 59 minutes, or 60 minutes in an hour. So, we've got exactly the same six decoder reset circuit I've called it

**Dave Jones:** here. Exactly the same thing happening here. Easy. And you might be wondering how I got the speed up display on those digits. Well, I got two switches on the back. One here, and one here. And what I'm doing is just on the seconds here,

**Dave Jones:** I'm just basically optionally switching in that 10 Hz signal. So, I can increment the seconds at 10 times per second. I can also increment the tens of minutes as well. But, it had a neat little thing, whereas if you put the

**Dave Jones:** switch right in the middle, okay, it was break before make. So, essentially, the input to this CMOS chip was floating here, the clock input. And if you know anything about CMOS 4000 series CMOS, they are essentially infinite input impedance. So, any noise

**Dave Jones:** at all being picked up on that line, especially the big long antenna line, there you go, going into the back, switch in, this big long line going over with a 50 hertz running everywhere, right? It would easily pick

**Dave Jones:** up the 50 hertz on there. So, if you actually just sat these switches that are used on the back, you could actually just sit them in the middle and leave them there. You could even hold them there or they'd sort of stay there on

**Dave Jones:** their own. So, instead of 10 times per second, we get 50 times per second here or here. So, that'd be like So, it had a slow set and a fast set as well. Awesome little feature. And I can show you that

**Dave Jones:** uh dual speed thing here. Like it's going normal, then it's going at 10 times per second. And if I put it in the middle, as you can see, 50 hertz, because that pin is floating. But if I actually go in there and

**Dave Jones:** uh probe the clock pin, so even though we've got effective 10 meg input resistance of our probe, you'll note that bingo, nope, that just went down like that. And you'll notice that it's not incrementing there at all, because

**Dave Jones:** well, there's nothing going through. We're just pulling that clock pin low. So, that's a great thing about 4000 series uh CMOS using these. Effectively so ultra, you can build really great ultra low power designs with them, because there are effectively infinite

**Dave Jones:** input impedance like that. And uh you can like the pull-ups, you can use like 10 meg pull-up resistors. So, you're not pissing away any current at all. 10 meg works just fine on a 4000 series CMOS. Although, it's not a hard pull-up. So,

**Dave Jones:** if you had a long line, but as you can see, I got this long line in here. And it you know, 10 meg, it was it wasn't picking up anything. But yeah, you got to be careful. But hold on to your hats,

**Dave Jones:** folks. This is where it gets nasty, and this is where it actually took me quite some time to figure out what was going on again after all these years. And well, I think I've got it right. anyway. I hope I have. So, uh what we've

**Dave Jones:** got here Okay, we can count up This is, you know, this is circuit's pretty easy, right? We can count up to 60 and then reset. No problems at all. But, the hours is really weird. It's got to count

**Dave Jones:** up to 12. And well, that doesn't sound too hard, but the 12 is split over two digits. So, this uh hours the first hours digit here actually has a convoluted um sequence, okay? This is what it looks like. It has to count like this. Just

**Dave Jones:** ignore that there. It's got to count 1 2 3 4 5 6 7 8 9 0. Okay, that's fine. We can do that. Okay, we could have done that with our 4026. No problems at all. And then it resets back to zero. No

**Dave Jones:** problems, right? Exactly the same as what we've seen before. And then it starts counting up again. You think, "What's the problem?" Well, it's got to go 9 0 1 2 and then back to 1 like this. Not to zero, but back to one. So, that's

**Dave Jones:** what that digit has to do. It's got that convoluted sequence. It's got like 1 2 and then 1 2 again. So, how the hell do you do that? Well, you can't do it with your 40 uh 26 cuz you don't have access

**Dave Jones:** to the internal BCD output, as I mentioned before. So, what I did is it did it the more traditional way and used a 4518, which is basically the same as the first half of the 4026. It's a just

**Dave Jones:** a BCD counter. That's it. And there's the four outputs there. It counts from zero to nine. Exactly uh you know, exactly like the 4026 here. But, uh then, of course, we need to drive our seven-segment display. So, we've got a

**Dave Jones:** 4511, which is a BCD to seven-segment display driver. No problems at all. This is sort of like your traditional method of uh driving seven-segment displays. If you don't have like in TTL uh for example, there's equivalent ones. I don't think the TTL

**Dave Jones:** 7400 series has an equivalent to the 4026. That's from rusty memory. I stand to be corrected on that, but to get that weird count, we have to have all this convoluted circuitry here, and you're going to have to stick with me on this

**Dave Jones:** one. It will work out in the end. Okay, just forget that all of this is here for a minute, okay? And we've got basically the equivalent to our 4026 here, okay? Our carry output comes in there at clock

**Dave Jones:** input here of our BCD. It counts from zero to nine, and it displays from zero to nine on there. No problems at all. So, we can get, you know, our our thing going from zero to nine here. Not a problem whatsoever,

**Dave Jones:** okay? But what we have to do is have some additional circuitry over here that actually starts to detect when we're actually transitioning over at the end of the count here. So, what I've got, you'll notice that well, I've got a big

**Dave Jones:** diode or gate here. There's actually five diodes. There's four I've tapped off all four BCD outputs, okay? This is an or gate as opposed to an and gate we saw before, and it's going into the transistor here, and that's basically

**Dave Jones:** one big or gate, right? The five-input or gate. One comes from this chip over here, and four come from the BCD lines. Okay, so what we're going to do here is the Q4 output, okay? Which corresponds in binary, of course. BCD It corresponds

**Dave Jones:** to eight. So, when it gets to eight here, this is why in the sequence here, this thing counts up normally until it gets to eight, and then Q4 line here goes high, okay? And we're tapping that off here. Don't worry about the or thing

**Dave Jones:** at the moment. Tapping off here, and that goes into the clock pulse of this 4518. It's actually a dual BCD counter. So, I'm actually using It's the same chip, but there's two per chip. Um and it's got both a negative clock input and

**Dave Jones:** a positive going clock input. So, you can choose whether or not you want to trigger from the negative going edge or from the positive going edge. It's quite handy, you know, you don't have to put an inverter on the on the input for the

**Dave Jones:** thing. So, we're going to actually you'll notice that I've got the positive going one connected to ground cuz we don't want to use that. So, we've got another BCD counter here that will start counting when the clock pulse goes low,

**Dave Jones:** okay? But, we've transitioned Q4 when it counts up to eight that line goes high. So, we're not clocking this thing yet, okay? Just assume it's all still reset. It'll only clock when it goes low. So, in effect, you could say that we've kind

**Dave Jones:** of like armed this second BCD counter here. Probably not the right term, but I don't know. That sounds okay. Now, nothing happens when it counts up to nine, everything's still when this one counts up to nine, everything's still fine, okay? But, when

**Dave Jones:** it actually goes to zero, okay, then this Q4 output drops back down to zero. Bingo, we've just fed a clock pulse into our second BCD counter here. And what happens when we get a clock pulse on here? Well, it counts up one and the Q1

**Dave Jones:** output here, so I'll call it Q1B so it's not confused with this one output here. And I've got in the notes here Q4 goes low, okay? This thing goes low, it clocks this 4518 and it starts counting up. So, it counts to one and then this

**Dave Jones:** Q1B output, of course, goes high, which is one, and then it gives a 10 on the display. Remember, this chip is reset, so we're going to get a zero up here, but we want when we're counting up 1 2 3

**Dave Jones:** 4 5 6 7, we want it in nine, we want it to actually now display 10. It's 10:00. So, the output here goes up. We've got another diode or gate up here and that switches on this digit here. So, bingo,

**Dave Jones:** we've counted up to 10 and we've displayed 10 on both digits here. With me so far? So, hopefully everything's reasonably clear at this point. Our display Our clock has counted 1 2 3 4 5 6 7 8 9 and then 10, 1 0.

**Dave Jones:** Okay? So, we've got 1 0 on display. This chip keeps counting because it's kept being fed by the clock and it'll start from 0 again. It'll count up to 1. Okay? So, we'll it'll be It'll go from 10

**Dave Jones:** 10:00, 1 0, to 11:00, 1 1. And that's all fine up until this point. But, here's where some of the magic happens when we actually go to 12:00. Check it out. We've actually tapped off Q2 output here, which is a 2. Okay? So, when this

**Dave Jones:** line goes high, we've got a diode AND gate in here for the reset of this chip. But, it will only reset when both where at count two here, Q2 is high, and also when we've armed this second BCD counter. See, cuz we're

**Dave Jones:** tapping off the output here as well as going up here and displaying our one, we're also tapping off here and going down and going, "Aha, we've got a one here now." So, we sit there. We're at the point where we're eight. We go up to

**Dave Jones:** nine, 10, one, and then we're waiting for it to come to the two. And when it comes to the two for 12:00, bingo, our chip resets and this goes back to zero. Well, in fact, both of these chips go

**Dave Jones:** back to zero because we want to count up to 12, remember? So, our count resets. So, that's why these two reset lines are tied like this. So, both chips reset. We're back to exactly where we were before. But, I know what you're

**Dave Jones:** thinking, "Dave, we don't want to We actually want to display 12 up here. We don't want it to go back to zero. Okay, the output here has gone back to zero. That's no good to us. What what good is

**Dave Jones:** that? Well, this is where this diode or gate comes in here. You'll notice that once again how we tapped off our 12 here, this same line went through a diode I actually I didn't tell you to ignore that diode before but you should

**Dave Jones:** have. So, this sneaky little thing here, what it's doing is forcing a basically a two into there. Okay, the the output counter of this is zero. Remember it's reset itself back to zero. This and this is all reset back to zero. So, it should

**Dave Jones:** display a zero up here. But, we're actually forcing this diode or line here and this is where this diode or gate comes into it as well. The combination of these two or gates are going to force a 12 display up here when we've actually

**Dave Jones:** got zero in this counter here because we don't want to display zero at that point. So, if we've got a 0 0 0 0 on the output here because this chip has just reset itself, this diode or gate is going to

**Dave Jones:** have a Oops, I made a small error in this thing. This is actually a Norg Let that come through. This is actually a diode Norgate. So, if we've got a 0 0 0 0 here because our chip is reset,

**Dave Jones:** okay, then we're going to actually going to get a one out of here due to this pull-up resistor because all these diodes and this chip is reset, too. So, all these diodes coming in, all five inputs are zero, we're going to get a

**Dave Jones:** one out of here cuz this transistor's turned off and we've got a pull-up. Bingo, if we've got a pull-up here, this is going to turn this diode on and force a one into the input of this BCD to

**Dave Jones:** seven-segment decoder. So, even though this counter here is at zero, we're forcing our seven-segment decoder to display two. Beauty. But, we don't want zero two, We want 12. So, once again, the output of this NOR gate here goes up here and actually forces

**Dave Jones:** once again, it's an OR gate here, so it forces our one here. So, even though all of our circuitry down here is reset, we've got zero and zero, we're actually forcing, tricking this thing into displaying 12. Ah, sneaky. So, in our

**Dave Jones:** countdown here, our BCD counter is actually zero. Okay? It's actually zero at this point, but we're displaying our 12. And that's how And then the BCD counter starts is at zero, so we can start counting 1 2 3, and it can start that sequence

**Dave Jones:** again. It's that tricky point there that we have to force the display to 12. But, otherwise, the BCD counter doesn't know the difference. And then, as I said right back at the start, we've just got a uh flip-flop over here, 4013, which is

**Dave Jones:** just connected down to the reset line down here, so it toggles every uh 12 hours and then just toggles between A displaying A and P just by turning this segment here on or off. As you can see, it displays an A if that's on or a P if

**Dave Jones:** that's off. Simple. Goodness, how long's this video been going for? Uh well over half an hour. Sorry about that. Maybe 40 minutes or something. 45? I don't know. Crazy. But, anyway, I I hope you enjoyed that look at uh an

**Dave Jones:** old-school 4000 series CMOS uh digital clock. And it works really well. As I said, it's been working for decades and decades, since the late '80s this thing, apart from some brief downtime where I ripped the bloody chips out, but I put

**Dave Jones:** them back in and uh got the thing going again. It's worked a treat. It almost never missed a beat. As long as your mains is uh good, you know, you don't get constant mains disruption and uh uh things like that. Just doing the 50

**Dave Jones:** hertz is um is really very good. It was probably the most accurate clock I ever had in my house because over the long term that 50 hertz it's pretty darn close to bang on. So, there you go. I

**Dave Jones:** hope you enjoyed that little look at designing a CMOS clock. If you liked it, please give it a big thumbs up and all that jazz and discuss it on the in the comments or at the EVBlog forum, wherever you want to do it.

**Dave Jones:** Catch you next time.
