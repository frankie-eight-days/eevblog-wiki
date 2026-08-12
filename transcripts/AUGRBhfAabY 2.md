---
video_id: AUGRBhfAabY
title: EEVblog #1249 - TUTORIAL: Timing Diagrams Explained
url: https://www.youtube.com/watch?v=AUGRBhfAabY
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 33, "3": 59, "4": 69, "5": 82, "6": 96, "7": 110, "8": 124, "9": 141, "10": 153, "11": 171, "12": 177, "13": 188, "14": 201, "15": 214, "16": 223, "17": 239, "18": 252, "19": 264, "20": 278, "21": 292, "22": 303, "23": 319, "24": 336, "25": 354, "26": 379, "27": 392, "28": 404, "29": 422, "30": 440, "31": 449, "32": 478, "33": 500, "34": 510, "35": 526, "36": 539, "37": 551, "38": 570, "39": 584, "40": 601, "41": 613, "42": 631, "43": 645, "44": 658, "45": 669, "46": 686, "47": 702, "48": 720, "49": 739, "50": 763, "51": 780, "52": 793, "53": 803, "54": 815, "55": 834, "56": 846, "57": 862, "58": 879, "59": 894, "60": 910, "61": 927, "62": 938, "63": 948, "64": 959, "65": 973, "66": 986, "67": 999, "68": 1013, "69": 1024, "70": 1040, "71": 1051, "72": 1070, "73": 1081, "74": 1092, "75": 1110, "76": 1130, "77": 1145, "78": 1154, "79": 1167, "80": 1178, "81": 1195, "82": 1215, "83": 1223, "84": 1238, "85": 1251, "86": 1262, "87": 1285, "88": 1316, "89": 1329, "90": 1338, "91": 1349, "92": 1363, "93": 1370, "94": 1389, "95": 1408, "96": 1417, "97": 1429, "98": 1441, "99": 1452, "100": 1464, "101": 1478, "102": 1492, "103": 1508, "104": 1518, "105": 1527, "106": 1536, "107": 1550, "108": 1564, "109": 1576, "110": 1587, "111": 1614, "112": 1626, "113": 1636, "114": 1654, "115": 1670, "116": 1682, "117": 1694, "118": 1701, "119": 1722, "120": 1741, "121": 1750, "122": 1775, "123": 1789, "124": 1825, "125": 1842, "126": 1856, "127": 1868, "128": 1883, "129": 1901, "130": 1910, "131": 1926, "132": 1935, "133": 1949, "134": 1977, "135": 1988, "136": 2004, "137": 2035, "138": 2050, "139": 2061, "140": 2084, "141": 2093, "142": 2107, "143": 2119, "144": 2133, "145": 2158, "146": 2173}
---

**Dave Jones:** Hi, let's take a look at a very important aspect of electronics which you're almost certainly going to have to learn if you want to do anything serious in electronics design and in particular digital design, uh processor, microcontrollers, all that sort of stuff.

**Dave Jones:** It's timing diagrams. And I've actually done a video back here. I'll link it in at the down below and at the end. If you haven't seen it, it's about one of my old PC-based logic analyzer projects and I go through uh some of my old handwritten timing diagrams I did back in 1995 by the looks of it.

**Dave Jones:** And this is not just old-school stuff. Timing diagrams, you need to know and understand these and be able to draw them, interpret them. Because if you don't know how to interpret them, then you're going to have a real hard time understanding how chips work, implementing them, any troubleshooting issues you get in uh with chips, your your circuit's not working, you can't quite understand why, uh set up and hold

**Dave Jones:** times, at least to a whole bunch of a different things. And even basic stuff like, you know, 74 series logic. You go into the data sheets down here and you'll get these timing diagrams.

**Dave Jones:** What are they? How do you interpret them? And that leads to things like these hideously complicated-looking things, but they're not. They're real easy. Um these waveform transition diagrams and stuff like that.

**Dave Jones:** Well, let's take a look at it. Very important topic. Now, the first thing you have to understand is there is absolutely no standard in timing diagrams. I don't believe there's any sort of official standard for them.

**Dave Jones:** There's no It's There's kind of some sort of de facto standards, but it's almost guaranteed that every timing diagram you're going to see is going to be different either quite substantially or subtly in many different ways from another one you've seen before.

**Dave Jones:** Let's just take a typical 74 series logic tip, the 74HC 595. I I don't know who this man I think this is a Motorola jobby. Take a look at this timing diagram, the exact same chip.

**Dave Jones:** Let's go to diodes.com. It's just showing exactly the same thing, but it's actually I did they draw things differently. Here's another one, this is a Philips job. You go to any manufacturer of exactly the same chip to show you the operation of the chip.

**Dave Jones:** Look, some of them will have arrows on them like on the transitions like this, others won't. Some will have what's called Z state down here, others will won't have anything at all.

**Dave Jones:** Implies that it's a high impedance state, they'll put X's in there. Another one here will put a dashed lines in here. And they're all saying and telling you exactly the same thing, but it depends on how people's or companies' personal preferences when they actually draw them.

**Dave Jones:** So, you got to know how to interpret these things. And then a lot of people think, "Oh, well, this is only if you design it with discrete 74 series logic.

**Dave Jones:** What do I I don't do that. I do everything in microprocessors and everything." Well, okay, let's go in and have a look at a microprocessor, shall we? I think just to pick micro.

**Dave Jones:** I just picked a pick. I'm here all week, get it? Let's just have a look at this. You don't have to get too far into the data sheet before you start running into Tada!

**Dave Jones:** Wait for it, timing diagrams. Timing diagrams for these are the clock modes, the run modes, program counter modes, for switching to sec run mode, all that sort of jazz.

**Dave Jones:** Look at all these timing diagrams and transitioning between different modes. Look at these. We've got some oscillator startup action in happening here and all sorts of all sorts of stuff.

**Dave Jones:** Primary clock resets. Because remember, inside micros are these. They show you the internal diagrams. They have actual physical hard logic in there and just like discrete gates. And these all This is all timing diagram dependent.

**Dave Jones:** So, you'll find not only these internal diagrams, but the associated timing diagrams along with them. Here we go. That's a simple one, but you know, it shows you where things are transitioning and why.

**Dave Jones:** SPI timing mode, you're doing SPI I2C stuff, you've got to know about all these sort of timing modes. You want to implement your own bit bang serial protocol, you need to know all this sort of stuff.

**Dave Jones:** Here we go. I2C, like this is like really important stuff to know and understand. Power up startup sequences, you don't understand why your chip's not starting up properly. You've got to get into these sort of timing diagrams.

**Dave Jones:** It just timing diagrams up to the wazoo. Look at this. Wake up from sleep through interrupt. You're designing your new low-power farting 40 gadget and it needs to wake up from sleep mode.

**Dave Jones:** And well, if you don't know what the timing diagrams are doing, you can come a gutser. Clock on IO timing, if you violate any of your setup and hold times or anything else, all this sort of jazz.

**Dave Jones:** What is Like we've got timing diagrams coming out the wazoo. Now, timing diagrams are just a bunch of digital transitions represented over time. Just like you'd see on a logic analyzer or an oscilloscope if you actually probed those pins.

**Dave Jones:** So, you might have, say, a clock like this because usually a timing diagram is going to be referenced to usually to some sort of clock. That's very common. Please excuse the crudity of my little mouse inaccuracy here, but you get the idea.

**Dave Jones:** Everything's referenced to a clock and this could be T0 over here and then time just goes off like that. Okay, so that will be our clock and it pays to draw things on graph engineering grid paper like this because it's important.

**Dave Jones:** You'll see in a lot of the diagrams down here, they actually show these lines down here and it typically you won't see them but you'll be able to visually see where things are lined up or they might be handy and they might draw in the lines for you so you know exactly, okay, this transition here happens exactly the same time as this uh you know, whatever clock transition

**Dave Jones:** thing up here does. So, it's just a way to correlate all different signals together and show the differences in timing. Set up and hold times, I've mentioned these in previous videos, very important otherwise your logic just won't may not work.

**Dave Jones:** It might go into a meta-stable state or whatever. You might need to know on what edge of a clock or some sort of latch signal or something like that is your data actually fed and latched through for example.

**Dave Jones:** Okay, so the first thing you need to know is that timing diagrams are basically representing digital signals although we'll get not always, we'll get into that. So, basically you've got a logic one up here at the top and a logic zero down the bottom or high and low depends on your terminology.

**Dave Jones:** So, if you've got a 5-volt TTL signal, it'll be 5 volts and 0 volts. If you've got 3.3 volts, it'll be 3.3 and 0 for example. And as I mentioned, often things will be correlated against a clock or a latch signal or some other sort of reference signal that you're dealing with.

**Dave Jones:** So, usually in the case of a clock like this, it's very obvious when you're looking at the data sheet. So, if you see something up here for example, that's always transitioning, well, you know that's a clock.

**Dave Jones:** And the second thing is you might see these little arrows. This signifies that something happens in the logic on this positive going edge. Sometimes it'll be a negative going edge and they'll show an arrow here for example, and then that will correlate if you actually go up here, you'll notice that our clock, if you follow the logic, you'll see that this is positive edge triggered because that's why we've got that on our timing

**Dave Jones:** diagram. You'll see it here. Clock pulse STCP, it goes this that is just a buffer. It doesn't it's not an inverter. It doesn't have a if it had a not there, then you would know from looking at the logic diagram that oh, that's probably negative edge triggered or if this was not CP or this had a not in front of it there and there you would know that

**Dave Jones:** that's oh, that's negative edge triggered for example, but or it could be an inverter there and then it could have a matching not over here and then you would know that that's positive edge triggered.

**Dave Jones:** But if that was an inverter, certainly down here, you'd see that this has an arrow like that. Showing negative edge trigger. So, those arrows are conveying vital information to you that really something happens on that edge.

**Dave Jones:** I.e. it's going to clock in some data. So, your data had better be there on those pins before this positive clock edge or negative clock edge arrives and so we can latch it in and do something with it.

**Dave Jones:** So, here's your data. Let's say your data comes along here and changes at exactly the same time that that positive clock edge happens. Well, that's called a zero setup time.

**Dave Jones:** So, that means that there's zero setup time. Whereas if we actually go back, you can see that this time here where where this data transitions here, changes here and before this edge here, this is called the setup time.

**Dave Jones:** And if we go down here, they'll show that on these more detailed timing diagrams. Here it is, voltage waveform, set up and hold times, bingo. So, you can see a data input here.

**Dave Jones:** Here's our timing input, which is our clock. This is our transition here. We'll get into why it's sloped instead of straight up a later, and TSU, time setup. That's what the SU stands for, and you can see uh there's a certain time period there before it has to set up.

**Dave Jones:** So, you know that's a parameter of the chip that can be quite important. If you don't meet that, you can come a cropper, the chip can go metastable, your data's not latched, your design just goes horrible, and you can have all sorts of weird and wonderful problems.

**Dave Jones:** So, you go search for TSU in the data sheet. Here it is, setup time, data set to uh SHCP or basically clock pulse. So, a minimum, you need a minimum of at 4 and 1/2 V cuz it changes with voltage, you need a minimum of 10 ns.

**Dave Jones:** So, your data has to be there and avail Your data has to transition either it's a one or it's a zero, doesn't matter what it is, but it's got to be valid before this clock signal comes along.

**Dave Jones:** And these are what your timing diagrams are conveying to you. And that's what they're kind of implying over here is that your data should be set up some significant time, although they don't tell you, some significant time period, i.e.

**Dave Jones:** showing half a clock cycle, but it could be much, much less than that, but it's showing you that that data needs to be set up before the clock transitions.

**Dave Jones:** It's quite important. Now, as I showed, sometimes you'll see a clock signal that has a straight or other data that has a straight edge like this, but other times you'll see it like this, and it actually has a transition on it like that.

**Dave Jones:** What does that signify? Once again, there's no strict definition of this, but what this transition implies, this ramp implies, whether it's positive or negative like that, what that implies is that something is happening on there.

**Dave Jones:** So, you might find that they might put the arrow on there like that, which obviously signifies that something's happening on that edge, but they may just show it as a slope like that to show you that something is happening between your well, your trigger points.

**Dave Jones:** We won't go into voltage high and voltage low threshold levels of digital logic, but it just implies that something could be happening on that edge. Or sometimes you might have two different signals that uh going like that and they're basically mirror opposites like that.

**Dave Jones:** And what that signifies is that this signal here corresponds to this one here. They're sort of like synchronized together, so to speak. That's one interpretation of it. It's not always like that, but you know, you have to often interpret these diagrams in combination with the uh logic diagrams of the chip here.

**Dave Jones:** And next up, you might see signals like this that have both high and low, and they might transition like that, for example, or they might go from high low like this down to low, for example.

**Dave Jones:** What does this signify? Well, as you might be able to guess, it means that it can be either positive or negative. We just don't know whether or not it's a data input to a chip.

**Dave Jones:** It just signifies that it can be either positive or negative, depends on your system. You're feeding in what your signal is, or the output. We don't know, cuz the timing diagram doesn't really know what you feed in.

**Dave Jones:** It's just telling you that it can be either a one or a zero. And you might see that in different ways on different diagrams. This one here, for example, this one shows it like this.

**Dave Jones:** It's not a solid line. It shows a long dash thing at the top and a short dash at the bottom. That this the designer of this chip and or this company what sort of their standard is to use short dashes like this for zeros and long dashes for one.

**Dave Jones:** But you might find that other data sheets for exactly the same chip what might have look dashes on the top like that and just a fixed line on the bottom.

**Dave Jones:** There is no standard for this sort of stuff. You've got to interpret it. Others won't have it at all. Or if we go over to our PIC chip over here, sure enough it uses the double lines like that, which is quite common for data buses and other sort of, you know, collective group things.

**Dave Jones:** For example, and by the way, this here this shows these bits one and zero inside the registers, but we won't get too much into that. And by the way, they can add little notes inside the timing diagram T delay here.

**Dave Jones:** You know that that's important there's a time delay between it looks like I I haven't interpreted this I haven't thought about it, but it looks like something between the system clock and then when the internal oscillator starts up.

**Dave Jones:** Okay, so right, obviously this is the timing diagram for the run mode start up. So obviously they're telling you that the internal oscillator doesn't start up until a time delay period after you switch.

**Dave Jones:** It looks like Please correct me if I'm wrong. It switches when you switch those bits over in in the register, then you'll have a delay time like this, which then you can go look up in the specs before that internal oscillator starts, for example.

**Dave Jones:** And there's tons of examples like that. And here's where I said they don't always show digital logic levels. They can sort of like show, "Oh, look, the oscillator is going to look like this.

**Dave Jones:** It's going to start up in few Actually, have a look at it sample it on a scope, you'll see it actually start up like that." It's They're effectively representing an analog waveform in a digital timing diagram.

**Dave Jones:** They're just showing you that it's basically unstable during that period. And t o s t, I'm not sure what o s t uh start up the oscillator t oscillator start up.

**Dave Jones:** That's what it stands for, obviously. See, you can sort of interpret With experience, you can interpret these things as t is always time, and o s t would be also cuz we're talking about an oscillator.

**Dave Jones:** O is obviously oscillator. And it's obviously some sort of start up time because we're on a timing diagram. So, that's how you can interpret stuff like that without having knowing or seen that on this chip before.

**Dave Jones:** Now, the next thing you need to know about is these grayed out bits here. What do these mean? Sometimes they show them as a crosshatch, sometimes they'll show them as just a flat line like that, sometimes they'll put large x's through there.

**Dave Jones:** It it varies, but obviously, they're telling you that this is basically don't care. We don't care what that data is or we don't know what that data is or it's not valid, depending on whether it's an input or an output.

**Dave Jones:** In this particular case, s d o is s data output. So, it's going, "We don't know what that data is or it's the previous data." Which the timing diagram doesn't care what the data is.

**Dave Jones:** But then it's telling you, "Okay, now I've come along and this is actually bit number seven." And you can see that obviously, this is the clock thing up here, even though they didn't put an arrow on there like that to signify it's a negative going clock.

**Dave Jones:** Obviously, based on that timing there, it's smack in the middle of this data bit is going to Something's happening on that negative edge there. And as I said, they could have signified that by maybe having a sloping edge like that.

**Dave Jones:** But I Once again, it varies totally between manufacturers, designers, whatever you want to do, as long as you're conveying the information that needs to be conveyed. But obviously, something All this timing here is happening in the middle of the data bit, and that's what you want.

**Dave Jones:** But this data This is the output. So, that You'll notice that it actually changes the data on the positive going edge. So, when it's shifting out data, that happens on the positive going edge up here.

**Dave Jones:** And that's probably why they didn't put arrows on there cuz you'd have to put an arrow there plus an arrow there because things are happening on both the positive and negative edge.

**Dave Jones:** In this particular case, the data output is obviously changing on the positive edge there cuz look, they've even drawn the dashed line down there. But the input here is actually happening whoop on the positive edge up there.

**Dave Jones:** And of course, this signifies that you can actually change whether or not it's positive or negative edge triggered with this particular register entry inside this micro. So, anyway, if you take your timing down there like that, you'll see that this is a setup time like this, and this is a hold time like this for your data input.

**Dave Jones:** And it seems non-critical enough not to actually have any particular info in there, but this may be a top-level timing diagram where they don't delve into that. Just like these ones down here, they don't delve into any of the timing.

**Dave Jones:** You've actually If you want to look at the timing, you've got to look at these specific switching waveforms here. But these are still timing diagrams, even though they're called them switching waveforms.

**Dave Jones:** Another thing you'll almost certainly come across is one of these things. What is this? They sort of like break up the signal, break up the clock, and just put some typically dashed lines through here.

**Dave Jones:** I mean, have a look at that. If we go over to this Microchip one, for example, bingo, here it is here. They've They've put little s's in there, but it can be dashes, it can be, you know, it can be lines broken up.

**Dave Jones:** It can be many different variations, but it basically signifies that, well, stuff is happening over a long period of time in here, and we don't care, and we don't want to show it because we've only got a limited amount of space on our data sheet or our timing diagram to actually show you all this stuff.

**Dave Jones:** And in this particular case, they'll show bit zero, bit one, and then they'll finish with bit seven and eight here. They won't show you all the other bits cuz obviously, well, what they're doing with that is actually they're they're really implying that the same stuff happens with bits two, three, four, five, and six that it does with bit zero.

**Dave Jones:** So, if this is a negative going edge here, and it switches the bits in, it's going to be exactly the same then for the other bits. They're not going to change it up.

**Dave Jones:** So, it's just like a something happens in there thing, just to shorten up the timing diagram. Now, another thing they'll do to shorten and compress schematics, they may not put these lines in here to show you that.

**Dave Jones:** They may actually Let's just say you have a latch signal, for example, and it's a pulse like that, and there's a massive There's actually a massive time period like that between latches, but they can't show you that on the page.

**Dave Jones:** They may put that uh, you know, something happens thing in there, or they may not. They may simply just show it like this, for example, and just shorten it.

**Dave Jones:** There might be might not be anything. And this is where the timing diagram doesn't necessarily represent the exact amount of time in the system. Obviously, if they have a clock up here and the latch data as well, then if they've got that clock, then that signifies if you draw your timing diagrams right and you should, then you're implying by showing that clock that everything is in real time.

**Dave Jones:** So, unless you put that {dash} {dash} in there, then you really you can't do this trick. You can't do this trick down here or you shouldn't do it. But, just be aware that timing diagrams may not necessarily represent a fixed So, if your grid is like 1 microsecond per grid spacing, for example, based on your clock frequency, then this may not necessarily represent that exact time.

**Dave Jones:** They may actually compress the timing diagram. Just be aware of that. Whether you're drawing timing diagrams or you're reading them like this, try and look at They They'll give you this valuable information like this is word number one.

**Dave Jones:** This is word number two. So, if you're doing your I think I've done that over on my video example, didn't I? Yeah, look, I've put little notes in here like this is read back mode.

**Dave Jones:** This is write mode. This is waiting for trigger mode. By all means, when you're doing these timing diagrams, it's like doing coding. It's like comment coding, adding comments to your code.

**Dave Jones:** You can add as much information in here and it's like I've got hold. There's the word hold there for hold, hold, hold. W for write, for example. So, I know that I'm I'm in This is a read write pin, for example.

**Dave Jones:** So, I'm in write mode when it's low, like this, for example. And like So, and here I've got like Yeah, set up and hold time Well, there we go.

**Dave Jones:** I've put other notes like here like must stay low during write and things like that, reading and writing mode, and must allow trigger in this point. So, I'm adding notes to myself basically when I'm designing this in this particular case it's a logic analyzer that I'm actually designing and got published here.

**Dave Jones:** So, I'm I'm making these mental notes so that I'm you know, there's lots of signals going on here in this particular case. So, those timing diagrams translated in into this logic then then I can more readily draw and understand the logic diagrams which then went into a CPLD FPGA device.

**Dave Jones:** And then the next thing we're going to look at, let's go back to our TTL chip here, is once again a tri-state condition or a it's not a don't care condition.

**Dave Jones:** In this particular case, this is the output enable. You can see that this data going x x x x x in here is showing you that that's obviously correlated with this signal here.

**Dave Jones:** So, you've got to you know, it may not have been right next to it like this. It could have been somewhere up in in the timing diagram, but you can see that it's obviously this is the result of this here.

**Dave Jones:** And this is an output enable pin. So, if you actually go up and have a look at the block diagram, you can see the output enable pin here and this is actually a tri-state driver.

**Dave Jones:** So, it open circuits the output. It's I won't go into tri-state drivers. Anyway, it's not a logic high, it's not a logic one, it's floating. It just disables that output.

**Dave Jones:** So, cuz this chip is designed to go onto a bus with other chips and therefore it when you have multiple chips on a dress on a drop bus, you need to output it control the output enable so only one is on at any one time to give you valid data.

**Dave Jones:** So, this goes into a tri-state mode and that's what they're signifying here by showing that. They're showing it's tri-state, but you might confuse that for oh, it's either one or high, right?

**Dave Jones:** So, who who did this data sheet? So, But is a TI one. So, the people at TI drew this. This is probably not the best way to show a tri-state output or a or a floating output cuz to me that kind of means oh, it could be one or zero.

**Dave Jones:** It don't care. You have to actually go look at the block diagram and know and understand the chip from other parts of the data sheet to know what's going on here.

**Dave Jones:** Well, no, ON Semi ON Semi same they're doing the same thing. But here we go, diodes.com they actually would tell you it's a Z state or high impedance state.

**Dave Jones:** But once again, they still show that they don't put the X's in there. They show it as a gray blocked out space there. But ah, good on you Philips.

**Dave Jones:** None of this Nexperia rubbish. They actually Look look at this. Not only do they tell you it's a Z state, it's a high impedance state, they actually physically represent it by showing that it's in the middle and putting a dash line there.

**Dave Jones:** Like it's in the center. And that that can with without even having the word Z state there. We're showing that line in the center of it's not logic high or a one, it's not logic zero or low, it's in the middle.

**Dave Jones:** Oh, therefore it's an an analog state. It's a high impedance state. Obviously. But they double down on that by telling you. So, thumbs up to Philips. That's how you do it.

**Dave Jones:** But sorry to ON Semi, there's a note down here. You got to read the note. Implies that the output is in a high impedance state. So, they do actually tell you at least, but you know, you got to read the fine print.

**Dave Jones:** But this 74HC595 here, because they've got none of those little, you know, something happens, you know, time stretching markers in there, and this is the serial register clock here, then obviously they're showing you a complete cycle there of shifting data into the register, but they're not showing you shifting data out like this.

**Dave Jones:** They just sort of like truncated that off. And if you want to know actually know what they're showing you on this, it's just an example. It doesn't have to operate like this because we're talking about user inputted data here.

**Dave Jones:** It does you can feed in any sort of data, but they're just showing you an example here. Q10, for example, they're showing you the data. Okay, the first data bit.

**Dave Jones:** One the data bit is high when this is clocked in. So, when this data bit, if you put a one on the input, and then you clock it like this on the next negative going edge like this, the data gets shifted cuz this is a shift register, gets shifted through to the Q0 output.

**Dave Jones:** And then the data's gone low again like this and it stays low for the whole cycle, and then they can show that on the next clock edge. Okay, this data will be shifted in here at this particular point like this, but it's a zero.

**Dave Jones:** So, that zero there will get shifted through to this part here on this edge. So, it's now zero, and the former one that we had here has been shifted over to here.

**Dave Jones:** So, if you want to show this in a bit better detail, you could actually put a dot with an arrow there like that to show it that that one shifted over to there.

**Dave Jones:** That would sort of explain it because if you didn't have that and you didn't have me to tell you what's going on here, you'd have to figure it out on your own.

**Dave Jones:** But, that's the beauty of timing diagrams and why you need to understand them because you have to interpret this sort of stuff. And obviously, it's going it's the data is still low for the whole thing, and you can show that you know, we get through 1 2 3 4 5 6 6 clock pulses or whatever, our our one that we fed in over here has finally appeared

**Dave Jones:** over here, and then next clock pulse it finally only on Q7 over here like this, so that one has just shifted all the way through like that. Winner. And there's more information that they're conveying in the timing diagrams here, like this is this asynchronous master UART type thing.

**Dave Jones:** This is the start bit here. They're telling you that that start bit, that's always going to be zero, but bit zero here, the bits after that, they can be a high or a low.

**Dave Jones:** And the stop bit has to be a one in this particular case. So, all this sort of stuff in the timing diagram helps you further understand what's going on inside these registers and how they're affected and this block diagram, these block diagrams down here, they tell you exactly what these things do and the timing, there you go, something happens in here, we don't care about those bits.

**Dave Jones:** And then the next thing here is that they might have these arrows here. They show that after this sequence here, whatever that is, then that corresponds to this bit, the interrupt flag happening down here.

**Dave Jones:** So, they're just showing you that they correspond. Once again, this thing causes this to happen. So, these might show a sequence, for example, like they could show that this causes this, which then causes this to happen, for example, and then you might draw in a little arrow like that to show that that particular transition causes well, that transition, that one causes that one, and that one causes

**Dave Jones:** that one. You might want to show a sequence of transitions, for example. Or, you might want to show that this point here, and you'll put the little dots, so that point there corresponds in time to that point, and you might want to show that both of those cause this thing to happen over here.

**Dave Jones:** So, if you point those two points cause this one action down here to happen. And that's pretty much all the basic stuff on timing diagrams. As I said, there are different variations.

**Dave Jones:** Almost every timing diagram you see in every different data sheet, even from the same manufacturer, can be different depending on who actually wrote that diagram unless they got a very strict company policy on their timing diagrams.

**Dave Jones:** A lot of companies will copy other ones, but you might see that a new company, a newish company like Diodes Inc. for example, might copy the data sheets of one of the other manufacturers for example.

**Dave Jones:** So, you know, they might have copied Philips or who've been around for generations. In these sorts of cases, timing diagrams are sort of like these sort of like de facto quasi standards just sort of like passed down from company to company, engineer to engineer, and they just spread within companies and within groups and and other things like that.

**Dave Jones:** So, you know, you often see similarities, but sometimes there can be massive differences, but it's pretty obvious if you understand some of the basic concepts I've gone through here.

**Dave Jones:** I think I've gone through most of them. Let me know if I've left something out and maybe I can do a part two cuz there's always something new to add to timing diagrams cuz some of them can get, you know, really quite complex and involved.

**Dave Jones:** So, there you go. Just don't freak out when you see timing diagrams like this or these sorts of switching waveforms for example. They're they're really, you know, this looks hideously complex.

**Dave Jones:** A beginner looks at that and just their brain explodes. How can I possibly understand that? Well, it's just a timing diagram. You know, this is like a setup time and then they're just showing you the time difference between when this digital input switches and this one here.

**Dave Jones:** In this particular case, they're actually showing you the 10 and 90% thresholds and they're putting it in the middle. Often, they'll put a slope in there and they will show the line going smack through the middle of the slope, even though that's not actually what happens inside digital logic because they have thresholds, an upper threshold and a lower threshold, but which may or may not be 10% and 90%,

**Dave Jones:** but typically though for timing diagram set up and hold times just for, you know, the sake of clarity, they will put it smack in the center at 50% like that.

**Dave Jones:** And you can see that in this particular case here with this timeout sequence on power up thing with your master clear not master clear line, for example, this internal reset line, look at this, is time correlated and they're obviously representing, they're not putting it smack in the middle of 50%.

**Dave Jones:** They're obviously put it on the upper part of the slope. So, they're telling you that that is the upper logic threshold of that particular pin. So, that that point of time is correlated when it goes high like that instead of when it's through like that because master clear, of course, when it's low is the whole chip is reset and only when it passes through the logic high threshold here, does the

**Dave Jones:** chip come out of internal there's a internal there's a flag called internal reset. Only then does that go high. So, you wouldn't show that at 50% because that wouldn't be a real representation of what's actually happening inside the chip.

**Dave Jones:** And then, you can also show like analog thresholds. You can have like a really slow ramp like this and show 1 V. I think that 1 V is corresponding to this particular point here.

**Dave Jones:** Even though it's exaggerated, once again, it doesn't have to line up exactly like it did here. It's show it's representing that it's in the high part it's the high logic threshold as opposed to a low thresh logic threshold which might be down here like this which changes with the logic family whether it's 4000 CMOS 74 HTC or HCT or you know the TTL equivalent thresholds.

**Dave Jones:** Anyway, we won't go into that but this one obviously look it's it's got 1 volt here. So that doesn't have to be like 0 volts down here. It's 5 volts up here.

**Dave Jones:** They don't have to show it down there. They've just sort of like expanded they've taken a bit of liberty there with that but they're showing you at that 1 volt point like that that that does something.

**Dave Jones:** There's there's some sort of timing operation and we won't go into it but you can represent analog type stuff on these digital timing diagrams. And these things aren't hard so don't be scared of timing diagrams.

**Dave Jones:** Start drawing timing diagrams cuz it really allows you to not only often you might do a timing diagram first or you might do some logic then you might do a timing diagram after that to make sure everything's hunky-dory and you haven't forgotten anything.

**Dave Jones:** You may a timing diagram is good way to document what's happening inside something like this. You know, it's one thing to okay, well there's all our logic. I can maybe figure it out in my head and mentally when you're looking at that you're kind of doing a timing diagram in your head anyway but it's easier to understand that often if you've got that timing diagram and you can see things correlate

**Dave Jones:** like oh that output enables obviously causing this and and things like that. Anyway, timing diagrams are great fun. So I hope you learned something from that. If you did, please give it a big thumbs up and as always discuss down below or over on the EEVblog forum.

**Dave Jones:** Catch you next time. Mhm.
