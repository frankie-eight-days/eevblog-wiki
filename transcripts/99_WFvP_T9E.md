---
video_id: 99_WFvP_T9E
title: EEVblog #1231- New Uni-T UPO3000 Oscilloscope Teardown
url: https://www.youtube.com/watch?v=99_WFvP_T9E
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 30, "3": 50, "4": 61, "5": 76, "6": 93, "7": 112, "8": 124, "9": 139, "10": 152, "11": 167, "12": 184, "13": 199, "14": 214, "15": 228, "16": 244, "17": 260, "18": 273, "19": 287, "20": 305, "21": 321, "22": 332, "23": 347, "24": 367, "25": 385, "26": 403, "27": 416, "28": 431, "29": 446, "30": 466, "31": 483, "32": 496, "33": 510, "34": 526, "35": 544, "36": 560, "37": 576, "38": 591, "39": 611, "40": 624, "41": 640, "42": 657, "43": 675, "44": 687, "45": 705, "46": 722, "47": 739, "48": 760, "49": 779, "50": 795, "51": 809, "52": 825, "53": 842, "54": 859, "55": 869, "56": 886, "57": 901, "58": 921, "59": 939, "60": 957, "61": 972, "62": 986, "63": 1002, "64": 1016, "65": 1035, "66": 1049, "67": 1061, "68": 1075, "69": 1088, "70": 1101, "71": 1126, "72": 1144, "73": 1159, "74": 1174, "75": 1195, "76": 1211, "77": 1225, "78": 1240, "79": 1254, "80": 1284, "81": 1305, "82": 1317, "83": 1334, "84": 1355, "85": 1369, "86": 1384, "87": 1398, "88": 1411, "89": 1429, "90": 1442, "91": 1457, "92": 1473, "93": 1489, "94": 1500, "95": 1513, "96": 1529, "97": 1545, "98": 1563, "99": 1581, "100": 1592, "101": 1607, "102": 1628, "103": 1644, "104": 1659, "105": 1675, "106": 1687, "107": 1702, "108": 1722, "109": 1742, "110": 1759, "111": 1778, "112": 1793, "113": 1809, "114": 1828, "115": 1844, "116": 1861, "117": 1880, "118": 1898, "119": 1912, "120": 1929, "121": 1946, "122": 1967, "123": 1982, "124": 1998, "125": 2013, "126": 2026, "127": 2037, "128": 2050, "129": 2068, "130": 2080}
---

**Dave Jones:** Hi, we have another oscilloscope teardown time. This one just like randomly turned up. I wasn't informed about it. I didn't request it, and it turned up to my old address. So, it luckily my DHL courier knows that knows

**Dave Jones:** me and knows where I am. So, I got this thing. Anyway, it's a new Uni-T UPO 3000 series. Now, about a year and a half ago, we did a teardown of the Uni-T UPO 2000 series, and it was kind of it

**Dave Jones:** underwhelming in terms of like bang for buck. And this one doesn't seem too different. Sure, it's got a much higher sample rate, 2.5 gig samples per second, 250 MHz maximum. So, this is the top range model, four channels, ultra

**Dave Jones:** phosphor, and all that jazz. And it's got a numeric keypad. Oh, look at this. It's look a bit busy with the numeric keypad, I think. But man, that could be handy if you don't, as in the case of

**Dave Jones:** all of these low-end scopes, you don't have a touchscreen on it. So, yeah, for entering numbers, it's handy. Now, I presume this is very new, cuz I had a hard time finding prices on this. It's basically just one or two

**Dave Jones:** sellers on AliExpress, another one in Europe, and that's about it. And unfortunately, it starts at just over a thousand US dollars for the two-channel 150 MHz model. So, this is not any sort of upgrade for the UPO 2000 CS series.

**Dave Jones:** It's an additional model which competes in a slightly higher price bracket. As I said, like that thousand dollar plus bracket, where its direct competitors, Uni-T have told me, are the Rigol 4000 series and the Siglent 2000 series. But like the Siglent 2000

**Dave Jones:** series, the entry-level model is much cheaper than this. Yeah, this one, granted, it's got higher bandwidth, higher sample rate, that kind of stuff, but uh and maybe some other stuff, but yeah, it's like if you want the base

**Dave Jones:** model of this, two channel, still over a thousand bucks. So, I don't know where that fits into the marketplace. I you know, I'd have to do like a big comparison spreadsheet like I did with the one gig scope. So, please

**Dave Jones:** give this video a thumbs up if you want me to do a comparison of like, you know, sub thousand dollar scopes for example, like or all of the entry level four channel ones. But yeah, the two channel job here at 150 megahertz, it's

**Dave Jones:** interesting that they have 250 megahertz and 150 megahertz bandwidths cuz most of us like 100, 200. So, this is yeah, you know, you get a bit more bandwidth and sample rate for your dollars. Anyway, this is not going to be a review, this

**Dave Jones:** is going to be a teardown and we'll see if it's how different it is to the uh previous one which was the UPO 2000 CS series. So, you can see it compared to the 2000 CS series which is

**Dave Jones:** a bit smaller, same size screen, but of course it's got the keypad and it's got the new springy waveform replay type stuff. So, it is an upgraded model, but apart from that, look and feel is the same. There's no times 10 amplifier,

**Dave Jones:** very similar sort of stuff happening around here. Similar, yeah. Looks like everything's pretty much the same interface except when they squeezed in this, they had to put the menu ones vertically. Included the keypad, but apart from that, it's

**Dave Jones:** quite similar. And they've moved the print screen button to down here. There's now a page down button, so I guess they got more stuff on the menu and there's a module and a decode button. But you'll see in a minute that there's a logic

**Dave Jones:** analyzer input here, but it's there's actually no connector fitted in there. As far as the back goes, quite similar. We've got Ethernet, looks like standard USB, but we get a VGA out this time, no HDMI. Why don't they put HDMI on modern

**Dave Jones:** scopes? Well, my guess is is that the chipset inside the VGA just comes with that processor chipset for free. So, it's very little addition to the bomb cost, I suspect. Anyway, external trigger and pass/fail output. I'm not a

**Dave Jones:** fan of the exposed default button there. I like it might be hard to accidentally press it, although like if you skipped off there, you might press your default button, that could ruin your day. Looks like there is room for another button in

**Dave Jones:** there, so I'm not sure what the deal is there. Maybe that's for the digital model. And it's got the same flippy feet at the back, which I'm not a huge fan of. It's not that terrific. Anyway, let's not muck around. Let's get right

**Dave Jones:** into it. And standard fan, all metal shielding on it, which adds to its quite substantial weight. It's not a lightweight scope. There you go, 4.3 kilos. That's pretty heavy. If you compare that to the cute little Rohde & Schwarz HMO 1200 series, 1.7

**Dave Jones:** kilos. And it is supposed to have a dual channel arb waveform gen here and here, and I can feel that there's holes for that, but apparently they sent me one without it, so I'm not sure if that's because it's

**Dave Jones:** an early unit or whatnot, or whether or not you have to actually physically buy it. Not sure if it's a software upgrade, but anyway, it is supposed to have dual channel arb capability as an option. You can see

**Dave Jones:** that there's physically no connector down in there on the logic analyzer. The logic analyzer option is not available yet, but at the end of the year, apparently, you will be able to get a mixed signal MSO version of this

**Dave Jones:** scope. All right, let's lift the skirt on this and we're in. How different is that? I believe the previous model Oh. Anyway, I don't believe we had heat sinks on the 2000 CS series. So, we could have some

**Dave Jones:** upgraded hardware. We should be able to pop those cans off, too. They look doable. So, anyway, that looks neat and tidy. Single board construction. These front ends look surprisingly similar to the other one, if I remember correctly, but uh

**Dave Jones:** I'll have to do a direct comparison side by side to really see the difference, because this is a 250 MHz capable front end, whereas the only one the other one, CS series 2000, was only uh 100 MHz capable. And

**Dave Jones:** if we have a look at the front end, no surprises for finding down in there the uh programmable gain amp that I've shown in my uh vernier video. It has exactly the same one as the Siglent. So, yep,

**Dave Jones:** full vernier capability. And it does seem pretty standard fare for a 250 meg front end. There's a bit of uh you can see the uh flux residue left over on that connector. That's a bit how you doing. Anyway, we've got ourselves a uh

**Dave Jones:** solid state relay there and then a couple of real mechanical clunking relays, couple of trimmer caps you go mmm mmm mmm if your tongue at the right angle to uh trim the front end. And oh jeez, that's a bit how you doing.

**Dave Jones:** Look at that cap in there. Wow, I get the macro on that. Yeah, that's a genuine budge right there. If we go over to this one, seems seems different. That one has two in series. Look at that. Where is the other one over here?

**Dave Jones:** Only has the one. What the This one here has the two in series. What? And over here on channel one, two in series. So, it looks like this is channel one over here. Looks like channel one is somehow different.

**Dave Jones:** Um that doesn't give me the warm fuzzies. Check it out. Look at the solder dag they've got there. So, they've obviously done this after they've put the cans on. So, yeah, it's pretty how you doing. There's a whole bunch of other

**Dave Jones:** stuff bodged around there. Look at the soldering on that cap there. That's either they put way too much paste on that when they reflowed it or that's been done by hand and it's all quite messy all around here. Oh, yeah, that's a

**Dave Jones:** double Oh, there we go. I missed it. Double stacker. And look, that's So, that was channel two. Channel one has a single resistor. Look at that. Right there. Channel two has a double stacker. Can't make it out cuz it's upside down. So, all the

**Dave Jones:** electrons are going to fall out. And channel three, yeah, look at this. So, we've got that and of course the resistors there. So, channel one Oh, and this and channel four has the resistor next to a double stacked.

**Dave Jones:** Ah, wow. That's terrible, Muriel. So, all I can think of uh to explain the variability in the channels there is this is some sort of like uh select on test kind of thing. They test this channel and somebody uh tweaks it with

**Dave Jones:** various parts in uh parallel and or series to get the bandwidth and the pulse response and the performance of each channel for the 250 meg model. Um yeah, I don't know. I don't actually know if it's software upgradeable. So,

**Dave Jones:** if you buy the 150, you can go to 250. I haven't uh checked that yet, but yeah, anyway, um not particularly impressed by that. Confidence is not high. I repeat, confidence is not high. Anyway, let's have a sticky beak around the rest of

**Dave Jones:** the board. There's all the unpopulated logic analyzer stuff. So, that's actually a ton of stuff there that's uh unpopulated. Wow. Um one of the most interesting things, look over here. 4.7 F. Not that microfarad or millifarad rubbish, 4.7 F. That's a super cap. 2.7

**Dave Jones:** V. So, they've used that uh as a battery uh replacement for the real-time clock. Anyway, it's stuck down, so it's not going to flap around in the breeze, no worries. And they've also uh soldered down the 32 kHz uh watch crystal as

**Dave Jones:** well, nice touch. And that right there is an ADV7125. That's a triple video DAC. So, that's your VGA output there. It goes to a uh goes to a connector down here. Not sure what's uh doing there. Anyway, that

**Dave Jones:** goes over to this ribbon cable, which uh goes to the back. So, you know, they have actually That's an extra bomb cost for that uh VGA capability. But as I said, it'd be built in the main chipset, which is up here. Let's take a look. Put

**Dave Jones:** a damn texture on there. That's actually an AM335 uh Sitara TI series um uh an ARM Cortex A8 processor and of course operating memory down there. This would be your sample memory down here as well. It's got uh 70 meg. Uh I'm not

**Dave Jones:** sure if it's uh per channel, whether or not they uh once you turn on all the channels, that halves, but uh yep, you know, it's got a decent amount of memory on it. And that's the Ethernet interface there, no worries. And then just uh

**Dave Jones:** surrounding that, we've got various uh power supply stuff. The inductors there are a dead giveaway. There's a few local regulation stuff happening. Then, looks like we got an oscillator there for our main FPGA, which will be under here. And as

**Dave Jones:** far as the power supply goes, they don't have solid aluminum electrolytics. They've got the old fashion type. You can tell because they they have the vent on top. If they got the vent, then they ain't solid. Old school liquid. And well, looky what we

**Dave Jones:** have here. This is a Sandisk eMMC flash memory on its own little daughter board with little castellations on the side there. It's soldered down onto the board. Wow, I don't think I've seen that on any other scope. Have we?

**Dave Jones:** Hmm, version 1.01.0001 for those playing along at home. That's an unusual looking jobby right there. Um, my guess is proximity to the FPGA there, that's probably the boot flash. So, yeah, like serial boot flash chip. Well, this is interesting. There's our

**Dave Jones:** ADC. You take the heat sink off, MXT2004 and a 34th week 17. Wow, that's old. Um, anyway, this is I'm not sure if that's in the previous version. I can't remember the previous teardown. Anyway, that's obviously a custom

**Dave Jones:** not a custom chip, but a custom silk screen on there for the manufacturer. So, I'm sure you can figure out what that ADC is. There's two of them, of course, so the sample rate will halve if you turn on all four channels. So,

**Dave Jones:** anyway, that will be an off-the-shelf ADC. Uni-T aren't going to go rolling their own custom ADC, that's for sure. So, I'm sure people will figure out what that one is. Leave it in the comments. And that looks like our PLL. I can't

**Dave Jones:** read the number on the camcorder screen here, but obviously just by the look look of the how it's laid out there and the proximity to the ADC's that's generating our sample clock. And that one's for the membrane molding aficionados and here we

**Dave Jones:** go just a couple of self tappers in the plastic front and we got the whole thing out. No, this is not a touchscreen as is common on the competitor or their main competitors I believe and most low-end scopes do not have the touch screens. As

**Dave Jones:** I said, does not have the logic analyzer circuitry populated or the connector. So, yep, let's have a squeeze. And for the encoder aficionados, cuz I know Alps that's genuine Alps. There you go. No lockers. And then the moldy is that a

**Dave Jones:** you know, they do would you would you get those off the shelf or can you or would they be a custom job? Maybe they're off the shelf. Yeah. Well, there seems to be a fair bit going on on the

**Dave Jones:** bottom here, but on this side it's just all passives and yeah, there's nothing else really. There's no active stuff at all. Likewise on the front end, it's all just passive, but curiously they've got a can on the bottom of that.

**Dave Jones:** So, unfortunately that's soldered in. So, I'm not going to bother getting that out cuz I suspect there's probably still only some passive stuff under there and just some passives up the top, but still fair bit going on. The board's a bit

**Dave Jones:** dirty in terms of like hasn't been washed properly or something like that. Not a huge deal, but notable. And of course these will be thermally conductive. So, if you took that off, I'm sure you'd find the via screwed the pooch. So, if you take that

**Dave Jones:** off, there's the thermal pad for the chippy on the other side. Get back on there. Ah, she'll be right. No worries. Well, well, well, a Kintex 7. That's $386 US one-off price from Digikey. Um but, yeah, that's a

**Dave Jones:** pretty beefy uh expensive FPGA. So, well, they what are they, you know, brute force in this thing? Anyway, I uh can't remember what was in the previous uh CS 2000 series, but uh yeah, this is pretty serious. Probably

**Dave Jones:** explains um a fairly significant uh chunk of the cost of this thing, which is why the base model uh is not like the Siglent. So, I in terms of like waveform updates per second and all sorts of other stuff. And

**Dave Jones:** I'm not sure about the FFT points. You'd have to carefully compare all the specs and things, but uh yeah, they've really they haven't really spared much expense there. There's the back panel connector board, and you can see the two

**Dave Jones:** unpopulated footprints for the um dual arb wave gen uh thing. And you'll notice that these little connectors here, more of these little micro uh coaxials here, which go over to the main board. So, yeah, I don't mean there's nothing else

**Dave Jones:** doing there. It's just a connector board. But, yeah, why they didn't uh in fact, uh someone I spoke to at Unity was very surprised that they didn't send me one with the dual arb gen option. So, hmm. And the power supply, well, there's not

**Dave Jones:** much doing on there, is there? Um that's about as basic bare-bones as it gets. And uh yeah, um don't write home to your mom about it, but uh Sanwha caps on the output there. And uh they they Chong, whatever. Anyway, these ones

**Dave Jones:** are uh these ones are Chong brand as well on the primary side, so meh. Anyway, they've got all you know, it's reasonably laid out and they've got all the requisite stuff there. It's even fused. Look at that. So yeah, that looks

**Dave Jones:** you know that looks fine and dandy apart from yeah, well, it's part of the course these days with those caps. And that's going to be hard to see, but I'm not a fan of the very tight cutout down in

**Dave Jones:** there for the wires and it's a sharp edge too. So they weren't careful in assembly they could certainly if you weren't um didn't make sure all those wires were loosey-goosey, you could easily uh cut through the insulation on one of those,

**Dave Jones:** I think. Pinch it down in the metalwork. And I'm sure that fan is just a one-hung low brand. I couldn't be bothered getting it out. Well, this is embarrassing. For the life of me, I can't see where this little coax goes.

**Dave Jones:** There's a unpopulated connector up there cuz I didn't take it off. It just sort of ripped out when I took the power supply. I assume it ripped out when I took the power supply. I must be blind. Jeez, well, I'm sure Stevie Wonder could

**Dave Jones:** see it. And I I I got I It's there somewhere. Let's boot it. There you go. Let's call it just like 34 seconds. Near near enough. So I was wondering why my pulse generator doesn't work. Um there's nothing wrong

**Dave Jones:** with the pulse gen. There's nothing on the USB. Do I have to reset it? Shutting down. Please wait. Goodness. Reboot. There's nothing. There's nothing out of that USB port. What the? Have I blown it? This thing doesn't take much.

**Dave Jones:** This is ridiculous. And the fan in it it's I wouldn't say it's really loud, but it's damn annoying. I can hear it literally 10 m away on the other side of the lab in a dead quiet lab. I'm

**Dave Jones:** shooting this at like 9:30 at night. No one else here, nothing on. It's the only instrument. I can hear it. As a reference, compare that with say the Siglent 1200 series. Whilst I can still hear this at the same distance,

**Dave Jones:** it's a really low level and much nicer hum. Whereas this unit say just like And it's a pretty tight response on the pulse here. This is a 40 picosecond pulse generator and it does okay, but there's kind of a little

**Dave Jones:** a little bit of a droop in there, which I don't see on other scopes. Anyway, there's not aggressive sine X on X interpolation, so there's not much overshoot or undershoot. So that's, you know, that's tight as a nun's nasty. Channel two,

**Dave Jones:** channel three, and channel four. Yep, I'm going to call that consistent across all four channels. So those little bodges that we had on the front ends don't seem to be impacting in that respect. But I'd still like to know

**Dave Jones:** what that droop is cuz normally you get an undershoot and then it goes back, not sort of a bit droopy. Let's check out the old piezo response. Oh jeez, that was a light tap. It's all over the shop. That was really

**Dave Jones:** light. I'm just going to let that fall. Wow. As a comparison on the Siglent with the same screwdriver, if Oh, I just hit it. If I let it drop, not a thing.

**Dave Jones:** I'm got something there. Yeah, I've actually got to hit that. It's the same volts per division, 10 mV per division. Mhm. Yep, big difference. Let's do the old taparoo. NO, I'M WHACKING THAT PRETTY HARD. NO. There we go. That wasn't particularly

**Dave Jones:** hard. But it's certainly certainly triggering. Yeah, even a small tap. Yeah, there's enough to trigger that. All right, I'm just like randomly mucking around here. I thought I'd check out the uh serial decode options. Um sure, like it's got all the board rates.

**Dave Jones:** I'm just RS uh 232. So, are they are optional extra? By the way, I don't know the prices on them yet. So, yeah, I'm not sure what the deal is. Anyway, um RS232, which should be just serial, not

**Dave Jones:** RS232. Anyway, um custom uh bit rates. Um only goes down to 2400 bits per second. you want 1200 or something, oh well, yeah, 300. Um anyway, if we go into custom, like we go down here, okay. I can do that. There's no sort of

**Dave Jones:** velocity control on there, but you think, "Aha, keypad, right? I can just type in 300." Nope. There doesn't seem to be any sort of ability to enter in the numbers at all. What? What's the point in having a numeric

**Dave Jones:** keypad like this? They went to all the effort, and you can't enter stuff in. That's insanity. I don't want to even know how long it's going to take me to get down to 300 or 1200. I mean, THIS IS

**Dave Jones:** IN AH! WOW, THAT'S BAD. OH, I'll tell you what, they uh have changed this from the 2000 CS model, cuz it had this really annoying I really complained about this, so maybe they listened and fixed it. It's really annoying highlight through

**Dave Jones:** uh the currently selected one. They've got the box around it now instead of the stupid highlight. So, yeah, they fixed that. Small win. This is weird. I'm just going into a choir. Set the memory depth here. Okay, it's

**Dave Jones:** got up to 70 meg sample memory. Brilliant. And I try and change it. Function is disabled. What the? I'm in run mode. Do we have to Surely we don't have to be in Do we have to be in

**Dave Jones:** stop mode? No. What? Why can't I change the memory depth? I'm in sample. It's got peak, high res, uh envelope. Uh which should be peak really, but it gives them Anyway, um average like what? Okay, I've no idea what the problem was,

**Dave Jones:** but I hit the auto button and now I am able to change that, but jeez, what the? Let me show you another annoying thing I don't like, right? You go into your channel menu here. You would expect that this

**Dave Jones:** button would just toggle your bandwidth limit off and on. No, it highlights it first and then you got to toggle. Like why? What a complete waste of a a button press. Unbelievable. And as is not uncommon, if you change

**Dave Jones:** the position control, it freezes display updating as you continually do that. So, yep, you've got to takes it like a second for it to recover. But, it's not really slow. It's fairly, you know, it it's okay. It just it freezes a display

**Dave Jones:** update. That's not uncommon. And yeah, I really don't like the feet on this thing. And like if I'm standing up at the bench looking down, it's really not tilting back enough. And if I move the scope back to like the leg just

**Dave Jones:** foot just collapsed on itself. I So, unless you implement that feet at the back right, it's much better to have the feet at the front like that. I can just tilt it up so I can see it if I'm

**Dave Jones:** standing up at the bench. No worries. I'll tell you what though, one feature you don't see very often is independent time base for all four channels. You turn it Look, look it actually initialize I've got to press it

**Dave Jones:** independent Oh, initialize please wait. There you go. Anyway, and now we've got four individual time bases and that can be handy for various niche applications. So, There you go. Goes back into normal and bingo we've only got the single time

**Dave Jones:** base. So, you don't Oh, what I think the original Rigol DS1052E had it, but when they did the 1050 1054Z they actually removed it. And again, stuff seems to be disabled like the like the time base like main. What's the

**Dave Jones:** other option? Function is disabled. What? I'm just in regular sample mode. Nothing like I I Really? Like it's just regular run mode. I Like I I don't understand and it can't do hold off. If you go into the math

**Dave Jones:** menu here, you can go FFT of course, logic expressions, filters, very nice. Once it Let's see if we can use our keypad for the filter because Oh, look that changes a lot. Okay, once again there's no major velocity control or is

**Dave Jones:** that just the fine or is that just the steps that you can do? Once again, I I'm trying. I don't know and I don't have a manual for this thing by the way. It doesn't download from the website.

**Dave Jones:** So, like What? Nothing works. What? I've got that selected. What is the point of this keypad? I don't get it. It's the hurry menu. Aha, the help function. You have to press You got got to call up help and then it

**Dave Jones:** looks like you can do various things. So, okay, that's all right. No module decode. Yep. Oh, there you go. We can select What? We can select kind of the selection's not working. The selection doesn't work. Wow, that is so up.

**Dave Jones:** Oh, wow, that's so sensitive. So sensitive I squared C. K trigger types, what do we got? Edge, pulse, video, slope, run, window, delay, timeout, duration, setup, hold, and search pattern. That's a pretty good selection. I'm not going to go in there

**Dave Jones:** and try them all, but yeah, I assume they kind of sort of work. Version number for those playing along at home. Now, is it just me, or is that font like really horrible? Um, it's just I don't like that at all.

**Dave Jones:** It's just not smooth. It's got Look at the seven there. The seven's like almost a bold thing. And like the the the digits aren't consistent. And for you probe officianados, there you go. Uh, 300 meg uh times, you know, the usual fare times

**Dave Jones:** 10. Nah, I'm not going to write home to my mom about it. K serial decoding, trying to turn it on here. You can actually uh set it to trigger on data. I was wondering why my bus wasn't showing

**Dave Jones:** up, and apparently you got to go in here. Decode bus, and then close bus state. You have to set that, push twice because of the stupid select thing, and then open. And it looks like we've got it up

**Dave Jones:** here. It's not doing anything at the moment, so probably still haven't uh We've got a event table. And what's a PSC wave? A pulse wave? PSC wave? I don't know what that is. Can we get help? What? It can go up to a billion

**Dave Jones:** bits per second. Uh, what? That's three six that's nine zeros there. Um yeah. Can I go to decode bus? No, it looks like I can't get help for that. Right, I realized I didn't have enough memory and again, I cannot change

**Dave Jones:** the memory depth. What? Okay, I found a display bug with the time base in uh replay, well, in stop mode. Uh watch this line over here as I change the time base. Look at that. It's got that line there.

**Dave Jones:** Goes away. Data's there. It's not like I'm doing anything weird. Yep, that's a bug. Okay, I'm not sure what's going on with single shot trigger mode. Trigger there. I've just got your basic uh trigger on your um slope. That's it, your edge. Negative

**Dave Jones:** uh you know, positive. Let's put it on fall there and single shot. That, okay. But watch this. I change the time base. Now, it's going to make a fool out of me, isn't it? I swear it was triggering like in the

**Dave Jones:** middle of there where there was no pulse. I swear. Okay, this is what the display looks like when it tries to decode it. It's just weird. Um I'm not sure what the deal is there. Zoom in. Have I got the wrong baud rate?

**Dave Jones:** Well, I did manage to capture it. S I G Oh, that's a bit uh the horizontal's not great. God, I don't want a big horizontal control. Got this little little piddly horizontal control down here. It's terrible. It's like a big ass thing up here. This tiny

**Dave Jones:** little horizontal. Uh anyway, Siglent. You know what I was going to say. Sorry, I'm just using a Siglent demo board. I think this is kind of annoying. I called up my event table here and I get my data in hex, even though I'm in

**Dave Jones:** ASCII mode. So, what? Like, it's a bit inflexible. I've gone back to measure a simple square wave, and I can't change the memory depth. Okay, I figured out the memory depth. You can only change it when it's in run mode. Wow, thanks a

**Dave Jones:** lot. And as for the measurements here, well, you know, fairly comprehensive, but a tiny little waveform, little bitty waveform, and like some text here would have been helpful. Uh is this a bug? I've gone from the measure menu back to the cursor menu,

**Dave Jones:** but it's left the measure menu up on the screen. So, it like it's just there. Like, what? Dude, can I clear it? I don't know. Oh, we've got Yeah, the color intensity graded display. Woo. Um but yeah, how do I get rid of that? I

**Dave Jones:** guess I can't. Maybe I've got to auto again. Magic auto button. Look at that. It didn't auto scale a 10 MHz square wave. That's a 10 MHz square wave. Sure, I'm in I I'm still in split screen mode, even

**Dave Jones:** though I don't have my math function turned on anymore. No, there's some sort of um the weird display thing. Oh, no. I can't even see that. Is that on? There we go. Let's go auto again. All right, so the

**Dave Jones:** math is off. Auto. There we go. It worked, but it didn't work in the other display screen. Nah. There's our FFT function. For those playing along at home, you can see it in the red there. And I don't know how many points it's

**Dave Jones:** got. We can't seem to do anything else. It's pretty basic. Got the different windows, but we can go full screen or split like that, but that's about it. Um Yeah, not particularly impressed. Cursor, time. Amp Oh, this is the multi-purpose knob

**Dave Jones:** is so fiddly. I really don't like it at all. It is hopeless. Yeah, cursor doesn't seem to work on any of the math functions, so yeah. Yeah, that's that's not updating. Why is that not updating? That's a bit slow to

**Dave Jones:** update. Anyway, that's Yeah, that's pretty hopeless. Anyway, I'm done with this thing. This wasn't supposed to be a review. I'm just having a random play around with it after the teardown, and well, I'm completely underwhelmed. Not writing home to my mom about this one,

**Dave Jones:** that's for sure. Um I would need to do a complete like spreadsheet analysis to see if it's good uh bang for buck compared with the Siglent. Uni-T themselves have said that it's comparable to the as I said, the Rigol

**Dave Jones:** 4000 series, which is an old fairly old model now. Uh whereas the 5000 series you can get for um less than the price of this. Like the base model 5000, the higher end 5000s are quite expensive, but at least the like the 70 mega

**Dave Jones:** whatever it is uh base model is actually uh cheaper than this and has a bigger screen, all sorts of stuff. So, if you can hack that, then that's a a better bargain. But yeah, I don't know if this

**Dave Jones:** is hackable, got no idea. No idea what's going on with the keypad. Um couldn't download the menu. There seems to be bugs in it. There's all sorts of issues. It's uh uh piezo um uh susceptible, and there's build

**Dave Jones:** quality issues inside, and I just No. No, it's it needs a lot more spit and polish. So, yep, can't recommend this one at this stage. Um maybe it'll get better, they'll improve things, but yeah. But no, Uni-T, this one I think is

**Dave Jones:** a bit of a fail. Sorry, not impressed with that at all. So, anyway, let me know your thoughts down below. If you want me to try out anything specific on it, I can, but as I said, I don't have

**Dave Jones:** the Ryegold or the equivalent Ryegold 4000 or the equivalent 2000 series Sig so I can't do really do a shootout of these except on paper. So, anyway, let me know. Hope you liked it. Catch you next time.
