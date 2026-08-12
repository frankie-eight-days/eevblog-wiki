---
video_id: JJgKfTW53uo
title: EEVblog #284 - Braun Toothbrush Teardown
url: https://www.youtube.com/watch?v=JJgKfTW53uo
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 23, "3": 33, "4": 44, "5": 59, "6": 76, "7": 88, "8": 104, "9": 112, "10": 122, "11": 133, "12": 147, "13": 164, "14": 175, "15": 184, "16": 204, "17": 219, "18": 235, "19": 254, "20": 280, "21": 290, "22": 301, "23": 314, "24": 324, "25": 341, "26": 352, "27": 366, "28": 377, "29": 393, "30": 406, "31": 423, "32": 440, "33": 449, "34": 465, "35": 476, "36": 485, "37": 499, "38": 517, "39": 530, "40": 543, "41": 553, "42": 564, "43": 571, "44": 582, "45": 591, "46": 603, "47": 621, "48": 640, "49": 654, "50": 670, "51": 689, "52": 704, "53": 721, "54": 731, "55": 747, "56": 766, "57": 779, "58": 791, "59": 799, "60": 816, "61": 835, "62": 848, "63": 862, "64": 896, "65": 905, "66": 917, "67": 927, "68": 940, "69": 955, "70": 969, "71": 981, "72": 993, "73": 1003, "74": 1021, "75": 1037, "76": 1055, "77": 1069, "78": 1078, "79": 1096, "80": 1110, "81": 1122, "82": 1143, "83": 1163, "84": 1176, "85": 1190, "86": 1204, "87": 1224, "88": 1234, "89": 1245, "90": 1255, "91": 1288, "92": 1298, "93": 1309, "94": 1339, "95": 1356, "96": 1368, "97": 1390, "98": 1404, "99": 1412, "100": 1435, "101": 1446, "102": 1463, "103": 1494, "104": 1503, "105": 1520, "106": 1537, "107": 1559, "108": 1576, "109": 1591, "110": 1611, "111": 1639, "112": 1656, "113": 1684, "114": 1702, "115": 1729, "116": 1741, "117": 1755, "118": 1778, "119": 1792, "120": 1821, "121": 1831, "122": 1853, "123": 1871, "124": 1885, "125": 1904, "126": 1914, "127": 1923, "128": 1945}
---

**Dave Jones:** Hi, it's teardown Tuesday again. Got something a little bit different. It's one of these Braun electric toothbrushes. I use them. I love them. They're fantastic. Can't do without my electric toothbrush.

**Dave Jones:** And you've seen them. It sits on one of these chargers, wireless power transfer to charge the internal battery. So, I thought this one uh crapped itself. I think it at least needs a new battery.

**Dave Jones:** So, I thought we crack it open and check it out. Not only what's inside here, but what's inside the charger as well. Let's take a look. Could be interesting.

**Dave Jones:** Now, here's the charger part of it. This one's uh specifically uh 220 to 240 V. So, it's not the universal type. This is model number 4729. Made in Germany.

**Dave Jones:** Hello to all my German viewers. Beauty. I know you love it. And it 2 W 50-60 Hz only. And uh it doesn't look like this sucker is going to be easy to open.

**Dave Jones:** Looks like it's uh maybe uh you know, heat sealed around the edges or something like that. So, uh before I uh really crack this thing open and see what's inside, I thought we'd um just uh run a simple uh test on it to see what we're getting out of the coil here.

**Dave Jones:** Because the coil sticks up in this part like this. So, when the toothbrush mates in there like that, it just whoop, it just sits in the bottom and that gets proper coupling from coil to coil.

**Dave Jones:** Because um you need proper coupling for these wireless power transfer systems to be anywhere near efficient. They're still going to be probably horribly uh inefficient. But, um I expect this thing not to be operated at 50 Hz, of course.

**Dave Jones:** It'll be operating at a much higher frequency. Cuz there's no way you're going to get a loose coupling like that working at 50 Hz in these sort of sizes.

**Dave Jones:** It's just not doable. So, it's probably working at a couple of hundred kilohertz or uh something like that, perhaps. So, maybe this is even potted inside. I don't know if we'll even be able to see the electronics in here.

**Dave Jones:** So, um I don't know. I might have to get the Dremel and take that sucker apart. But, uh anyway, I thought we'd uh hook on and see what we're getting out of this coil.

**Dave Jones:** Now, how do you do that? Well, um we Unless you have a matching coil to sit on there, there's a very simple thing you can do with your crow pro crow stands for cathode ray oscilloscope.

**Dave Jones:** It's an Australian term, sorry. Um old habits, I keep using it. The oscilloscope probe or scope probe, you can actually form a little transformer with it, a single loop like that, and that can be used for RF uh pickup for high frequency um pickup.

**Dave Jones:** It's it's pretty horrible and uh very inefficient, but it does actually work. It acts as a single turn, and it does actually work at high frequency. So, let's uh just put that over here.

**Dave Jones:** I'm sure it's going to be absolutely uh horrible. In fact, actually, I'm not even going to bother cuz I know it's not going to work at the couple of hundred kilohertz we've got here.

**Dave Jones:** So, what can we do? Simple. We can use our ground lead and wrap that a couple of times around like that, and that will give us better coupling. And if we go up here and take a look at the oscilloscope, let's see what we get.

**Dave Jones:** Aha. We have something. Let's have a look. What have we got here? We've got Let's center that. Expand it out. And bingo. Yep. Ah, no, I was way off on the couple of hundred kilohertz.

**Dave Jones:** I was off by an order of magnitude. It's only 20 kilohertz. There you go. And it's uh you know, around 700 mV peak to peak. The absolute the uh voltage, of course, um it doesn't really matter cuz it's just what's being picked up by our coil, but there you go.

**Dave Jones:** That's roughly sinusoidal. There's a little bit of something happening on the top there. I'm not sure what, but uh there you go. That's 22 odd kHz. All right, so you'll notice that uh with three turns of my scope uh ground lead on there, I'm getting about 250 mV uh RMS on there.

**Dave Jones:** And if I remove one loop there, let's let's have a look. There you go. It drops down. And if you remove another one, it drops down again. But actually, surprisingly, we are still picking up 20 kHz there with just the single the single loop like that is just enough.

**Dave Jones:** Very loosely coupled like that is just enough to pick up that signal. All right, so what we'll do is we'll just clean that up with some averaging in a bit.

**Dave Jones:** So, going to our acquire menu, we'll just turn on uh some averaging there. Let's do more than two averages. Let's say take it up to eight averages. There we go.

**Dave Jones:** We've cleaned up our waveform a little bit. Okay, what I'm going to do just to get consistent results, I'm going to sticky tape a just a single loop down on there like that.

**Dave Jones:** So, it's fairly consistent, as you can see. And uh it won't change around if we wiggle our probe and play around with it like that. It's pretty steady like that.

**Dave Jones:** And as you can see, it's beautifully sinusoidal on the bottom like that. Almost perfect. And then there's that distortion on the top there. Let's see what happens if we add a load by putting on the extra coil on there.

**Dave Jones:** Look at that. You can see the rising slope at the bottom there start to distort around about there. Look at that. As we load it down, the amplitude really isn't changing.

**Dave Jones:** It's staying the same. And then there's the peak. There's that little peak up the top, which is changing a bit as we load that down. Now, I'm not sure this actually doesn't charge anymore, so the lights don't come on.

**Dave Jones:** So, I'm not sure what's actually gone wrong in here. Maybe it's not actually the full load, but just the act of putting that coil on there does change that waveform.

**Dave Jones:** Does distort it a little bit more. So, you can see how it's certainly possible using this poor man's inductive pickup here to actually, you know, do some troubleshooting on these type of wireless tram power transfer circuits.

**Dave Jones:** You can at least play around and have some fun anyway. It's by no means absolute accurate, but it does allow you to couple into a system like this just using your scope ground lead.

**Dave Jones:** It's really neat trick. Now, as for taking this sucker apart, it's a pretty trivial. And it even provides instructions on the back here. It shows you to put it on the stand like this and then give it a little bit of a twist and pop goes the weasel.

**Dave Jones:** There it is. Awesome. So, let's Hey, look at that. Is our battery going to fall out? We've got a contact down in there. So, let's take a See if we can get that out and take a closer look.

**Dave Jones:** Now, you should be able to see inside there. It's actually got three wires coming off the coil down in there. And you can see the coil just down in there.

**Dave Jones:** You can see the multiple wraps in the coil. You might be able to see it Yeah, a little bit better through there. There we go. But we've got two what look like little ferrite beads just sort of stuck in there, not doing anything.

**Dave Jones:** Um I'm not sure what their purpose is. And there they are. I've taken them out and they just sat in there. There's just two of them sitting in there like that.

**Dave Jones:** I'm going to stick this back on the uh scope up there and uh see if there's any difference in the waveform. And I did stick it back on there and uh trust me, there was absolutely no difference whatsoever.

**Dave Jones:** I won't even bother showing it. So, um I'm not I'm unsure how to actually get the rest of this stuff in here out. You can see the battery in there with the welded uh contact terminal.

**Dave Jones:** That would be a uh nickel-metal hydride battery and it's sort of it's pushed all of this stuff. If I try and pull it out, it sort of pulls all this stuff with it and that bar the uh the uh vibration bar there doesn't um slide through or anything like that.

**Dave Jones:** So, I don't know. Um requires some more percussive maintenance, I think. When in doubt, just yank harder. And here it is. It just uh popped it pulled out. Look at that.

**Dave Jones:** Um I think I've uh yeah, I've busted uh something there from these two things. Here's the uh Here's the battery. There we go. What is it? A uh 607 M.

**Dave Jones:** Hey, it's Sanyo. Excellent. They put a top-quality Sanyo in there, nickel-metal hydride. There you go. So, uh technically, that's replaceable, except I think I've uh busted the whole show.

**Dave Jones:** So, I'm not sure um it's probably some sort of you know, one-off uh press-fit type thing. I don't know, but I can't find any way to get the rest of the case open.

**Dave Jones:** So, uh to get a look at the motor and stuff, which would be up the top end. Um I have to crack that open, but we have some electronics.

**Dave Jones:** Beauty. And sorry, I was mistaken about the uh number of wires coming out of there. It is actually uh four. Three didn't make uh sense, of course. So, there's uh two pairs coming out there.

**Dave Jones:** One of them is common in there on that terminal. So, there's only three terminals on the board. All right, it's times 10 macro lens time, and this is going to be uh really good.

**Dave Jones:** We should be able to uh trace out these circuits. Look like Looks like there's part readable part numbers on both of those chips we'll get into, and uh not much uh doing on the bottom there.

**Dave Jones:** Uh some test points, of course, and uh a couple of tracks. So, we should be able to trace this thing, actually reverse engineer it pretty easily. It's a 668331741500R8.

**Dave Jones:** Well, doesn't ring a bell. Might have to Google it. Well, this one uh wasn't trivial to uh find, and I think I've found it, possibly. Um it it all seems to uh match, but you Google uh you know, 668331 is really the only thing that you get, and it turns out that's an EM.

**Dave Jones:** Look, it's in the exact package you want. Uh TSOP I've got on on one of these um Ali but you know, one of these uh Chinese uh broker uh websites, and it's a TSOP 14 package, exactly what we got, and that's presumably that's obviously the manufacturer.

**Dave Jones:** So, you Google EM 6683331, and you end up popping over to uh various sites, but you get on to a company called EM Microelectronics. Um and they're part of the Swatch Group.

**Dave Jones:** Go figure. And they claim that they're uh leaders in ultra-low power and low-voltage uh solutions, including microcontrollers. And as it turns out, if you go into their microcontroller section, they've got um EM uh let's have a look here, in MCUs.

**Dave Jones:** Wait in. Wait in. They've got EM 6682, but they don't have a 6683. So, go figure. I don't know whether or not it's an older type. I still I Googled that and I still couldn't find it, but who knows?

**Dave Jones:** Maybe it's a custom uh part specifically for Braun. Who knows? But uh you go take a look at it in the EM6682 and it's a rather interesting thing. I would have had uh no idea that these things are even existed if I didn't open this toothbrush.

**Dave Jones:** That's what teardowns can do. It can lead you onto parts you search for them and it can lead you to manufacturers you didn't know about. I didn't know about these little ultra low power eight-pin microcontrollers.

**Dave Jones:** Had no idea this company even existed. But uh here you go. They've got some uh looks like some uh novel ultra low power eight-pin microcontrollers. They work from uh low 0.9 V um to 5.5.

**Dave Jones:** So, that's pretty much ideal for a single-cell um single-cell operation like single-cell alkaline uh cuz really their um energy density the energy usable energy in an alkaline battery for example, pretty much exhausts itself at around about that 0.9 V.

**Dave Jones:** Some people take it as 0.8 V. That's a more common thing, but basically from a single alkaline cell you can use up um all of the energy in say a AA alkaline battery for example with these microcontrollers.

**Dave Jones:** That's really quite neat. Another interesting thing is got a four-bit ADC or 12 levels of the supply voltage. So, obviously there's no built-in uh reference by the uh sounds of it.

**Dave Jones:** Just uses your uh supply uh voltage to do that, but it's only got a four-bit ADC which might be all you need. And these things are I don't know.

**Dave Jones:** They might be really uh dirt cheap or something like that, but it's got a mask uh ROM built-in. So, these are not flash devices. So, you can expect these to be really uh uh cheap because they don't have to have all the extra um expense of making a die with uh you know, flash memory, reprogrammable flash.

**Dave Jones:** They're a mask ROM device. Um and they've probably got development kits to go along with it if you're, you know, that's why you've probably never heard of these because well, you know, hobbyists and and uh you know, professionals just working on your standard, you know, uh stuff off-the-shelf from Digikey have no idea about these sort of things.

**Dave Jones:** And they're certainly probably not uh easy to start developing with. And the core is an EM6600. That sounds like their own uh core. It's probably based on some derivative of uh something somewhere along the line.

**Dave Jones:** Who knows? But anyway, it's a complete uh single-chip solution. Uh 4 microamps in active mode. The um uh built-in oscillator, it's designed for ultra-low power stuff. It only goes from 32 kHz to 800 kHz.

**Dave Jones:** It's the main oscillator. It's got a watchdog uh timer. It's got a sleep controller. Uh 10-bit universal counter timer. Some interrupts in there. And a 4-bit ADC. So, it's really um you know, a pretty specific uh low-power sort of, you know, consumer microcontroller in these sort of consumer appliances cuz you can bet your bottom dollar that Braun paid absolute lowest possible, they shaved every cent, lowest possible cost off the price of

**Dave Jones:** this thing. And they would have ordered millions and millions of these parts to be used in these uh toothbrushes. So, uh no wonder they picked uh uh possibly um something like this.

**Dave Jones:** This company may have offered them the cheapest price with their mask ROM and their 800 kHz and no flash and you don't need anything fancy. There you go. Typical applications: household appliances.

**Dave Jones:** And if you go down further and take a look at the CPU, it's only a 4-bit CPU. There you go. They still make them. 4-bit processor. Here's a classic example of one using your toothbrush.

**Dave Jones:** It doesn't need anything more cuz this is an intelligent, in quote marks, toothbrush. It, you know, has timers in there and and stuff like that. So, it, you know, after a set time it'll beep at you and stuff like that.

**Dave Jones:** It'll pulse the motor and do, you know, various intelligent things to tell you that, you know, you've been brushing for, you know, 3 minutes. So, it'll it'll vibrate the motor and actually warn you that, okay, you've been brushing for 3 minutes.

**Dave Jones:** Don't, you know, over brush or something like that. So, it needs some intelligent control in there. That's why I'm pretty darn sure, even though our number on the chip is the 6683, I think we've actually got the controller here.

**Dave Jones:** It matches up in terms of the package and the functionality. It's, you know, exactly what I would expect. I would have expected a super cheap, low-end consumer microcontroller in this.

**Dave Jones:** And you don't get much more low-end than a built-in mask ROM and a 4-bit core. There you go. And it's two o'clock cycles per instruction, 74 instructions. Um, and there you go.

**Dave Jones:** It's worth taking a look at this thing. And if we go down to the bottom, if we take a look at this, it's a 2008. Copyright 2008. There we go.

**Dave Jones:** Rev D. And uh package marking. There you go. EM 6682. No, it doesn't mention anything to do with 6683. So, there you go. These are SOICs, but I'm sure it can come in No, there we go.

**Dave Jones:** 14-pin TSSOP. And uh yeah, I mean, we do have those sort of numbers. We've got 00R8 on our package as well. So, who knows? But yeah, I think we've definitely got the right device here.

**Dave Jones:** And our other device here is a TSM 7401 with a marking 7K4. Once again, not familiar, going to go have to look it up. The microcontroller isn't going to be able to drive the motor directly, so let's go look that up.

**Dave Jones:** And curiously, when you're looking at these things, you'll notice sometimes you really have to get the right angle of light on these chips to read them. As soon as you get that right angle, you know, bang, it just really stands out.

**Dave Jones:** But sometimes, if you don't get the right angle, you just cannot read these things at all, and they appear just as a, you know, a completely black surface. You can't read anything at all.

**Dave Jones:** It's all about the light and the angle. Well, there's nothing complicated happening there at all. It's just an ordinary N-channel MOSFET in an SO8 package from Taiwan Semiconductor. It's only a 20-V job, but 4 1/2 amps, not much doing there at all.

**Dave Jones:** I could have used any one of countless number of N-channel MOSFETs on the market. So clearly, it's just a, you know, as you'd expect, a standard DC motor, and they're just hooking that directly across the battery and turning off and on with the MOSFET.

**Dave Jones:** That's it. Now, let's have a look at what else we've got on the board. We've got a tact switch, obviously, which goes through to the button on the front of the thing to switch it on and off.

**Dave Jones:** And got a few passives, a couple of diodes here in a mouth package, and which you don't see too much of these days, and a couple of SOT-23s there, which are like might be transistors or maybe even diodes or uh or something like that.

**Dave Jones:** So maybe even a regulator, perhaps. So and we've got a couple of LEDs here, two of them that match up different colors that match up to the uh light pipe or the or the cover on the front, the clear cover where they shine directly through there.

**Dave Jones:** And that's it. There's not much happening at all. We'll have to trace the circuit out. It shouldn't be too hard. Now, let's have a quick look at the input circuitry here, and you can see it's got two coils here with one common.

**Dave Jones:** Why they've got two coils, I don't know. Your guess is as good as mine. If you're into wireless power transfer technology and stuff like that, maybe it increases, you know, the the coupling coefficient between the coils or something like that.

**Dave Jones:** These things are fairly critical when you design these power coupling systems like this, you know, just the physical aspects of how they're wound, how they're mounted, the physical space in the coupling, the rotation, all that sort of stuff can really matter.

**Dave Jones:** So, it would have been engineered precisely to give a particular output voltage here on the rail. So, basically, we've got a rectifier on each part there. This is obviously a charging LED here, which comes from the microcontroller, and we've got another diode here, and we've got a a filter cap.

**Dave Jones:** So, we're going to generate a DC voltage here on our rails. Okay, I've got my probe hooked up to the power rail there, and as you can see, we're getting 4.53 V.

**Dave Jones:** There's a bit of uh bit of noise on there, but it's not a big deal. You'll find that will be the 20 kHz switching frequency, and we'll take a look at that in a minute.

**Dave Jones:** And if I wiggle that around a little bit, just back and forth, there's really no change there. But if I start to lift it up, you'll notice the voltage.

**Dave Jones:** You can see the voltage dropping. Got the DVM feature here. And you'll notice that voltage drops as I lift that up. I don't have to lift that up much, Only a like a millimeter, you can visually start to see that voltage drop and it's practically I'm not going to say it's linear, but it's almost a linear relationship between the uh height and the voltage there.

**Dave Jones:** There you go. Not not quite. You'll see You might notice that the LED actually flashed there when we got to a point. It's probably not going to do it.

**Dave Jones:** Probably a bit of hysteresis there. There we go. If you saw that, there we go. The LED is just fractionally switching on when it transitions through that voltage there.

**Dave Jones:** And if we probe one of the coils there, check it out. That's the waveform we get and it's about 13 just over 13 volts peak-to-peak there. And if we freeze that, you can see you can see this ringing on the rising edge there and associated ringing on the lower edge with a flat top and a flatter bottom now as opposed to what we were getting when it was unloaded.

**Dave Jones:** And a bit more interesting is if we probe the other channel, look at what we get. There we go. They're inverse waveforms. Look at that. I'll zoom in and give you a good look at that.

**Dave Jones:** There you go. Once again, they're about uh just uh on 13 volts uh peak-to-peak and we're talking there's that uh 21.8 kHz there. That's our switching frequency, but you can see they've certainly flattened on the top.

**Dave Jones:** Um this uh this channel here is uh more rounded on the bottom than this one is, but they're essentially inverse waveforms. And if we have a look at the uh ripple on our 4.5 V rail here, you can see the 22 kHz there.

**Dave Jones:** There it is, 22 kHz, but of course, you can see that second rise there, which is due to the fact that we're a full wave rectifying this thing from the second coil.

**Dave Jones:** And if I actually cut one of those coils off there, as you can see, it's not Yeah, as there it is. It's We don't have that second little rise in there.

**Dave Jones:** Well, maybe when it's charging, if it was charging the battery properly, perhaps it might matter a bit more, but I think it maybe it's got something more to do with the just, you know, better coupling coefficients between the coil, perhaps when they're doing, you know, when they've got larger charging currents, maybe, but I don't know.

**Dave Jones:** It'd be interesting to see if if we actually got full charge current on this thing. And as it turns out, the pinout for our microcontroller, by the way, on the board doesn't actually match that data sheet we saw.

**Dave Jones:** So, it's but I still think it is one of those one of those devices though, maybe a custom derivative for Braun or something like that, perhaps. All right, now let's hook up a new battery to this thing and see what we get charging current wise.

**Dave Jones:** Let's give it a go. 100 There you go, just over 100 milliamps, and you can see the charging LED flash there. I'm going to rise lift this up. Whoa, yeah, you only lift it up a millimeter and you can really see that charge current instantly drop away to way to nothing, like it's halfway up the stem there, the supporting stem, and it's it's dropped away to nothing.

**Dave Jones:** It just doesn't kick in at all. Now, let's have a look at what happens to our voltage rail up here, our 4.5 V rail, when we hook up our battery.

**Dave Jones:** Let's give it a go. Whoa, it drops to just over 3 V and it drops dramatically down in frequency. We'll freeze that and what are we getting there? We're getting 800 odd hertz.

**Dave Jones:** There you go. The switching frequency drops dramatically when we're drawing 100 milliamps charging current from this thing. And that gives us another thing to check. What happens to our the actual output waveform from the transformer?

**Dave Jones:** I've only got one side here of the transformer when we turn it into charging mode. Let's have a look. Oh, look at that. It's dropped. Looks like there's some Hey, there's something there's some pulse thing happening there.

**Dave Jones:** Let's try and capture that. There we go. Look at that. There's these pulses in there that are uh Look at check that out. Look at that. Pulses at what interval?

**Dave Jones:** We're talking, you know, a millisecond interval or thereabouts, just over. And this is it. Well, that did correspond to our 800 hertz that we were seeing before. And certainly, there it is.

**Dave Jones:** No surprise that's the 800 hertz we were getting on the 5 V Well, it dropped down to 3.3 V the voltage rail after the rectification and filtering. So, it's using some sort of It's deliberately pulsing something.

**Dave Jones:** I'm not Yeah, that probably it'd be on the charger side actually drawing, I would assume, from the charger side drawing these pulses like that. Remarkable. And indeed, if we take a second channel and measure the battery charging voltage and we freeze that, we can see that the battery charging voltage Look at that.

**Dave Jones:** It's got ripple on it. Then it doesn't for that period where it jumps back to its original um original position. So obviously, it's doing some sort of pulse charging of the battery in here at 800-odd hertz.

**Dave Jones:** So what we're actually seeing here is a pulse uh period charging period between here where we've got the ripple on uh the well, the charge ripple on the battery and the amplitude of our uh waveform from our transformer, of course, drops down due to the um extra current being drawn from the power coupling scheme there and then you have a period where it just uh goes um it it switches off the charging

**Dave Jones:** during this period, which is why you get a flat line on the battery because you're not measuring the charging ripple anymore. You've just got the flat battery voltage on there and our waveform returns to normal as we saw, which is the same waveform we saw before with the uh no load with the no uh battery load on there.

**Dave Jones:** And if we have a look at the basic reverse-engineered uh circuit here, we've got the uh dual coils over here, full wave rectified uh by these two diodes, and then it goes through another series diode here, which generates our positive voltage rail uh which you saw was 4.2 volts or drops to like a 3.3 volts uh during uh charging, but when it's in operation and there's no uh

**Dave Jones:** power coupling through the coil here, of course, the voltage rail for the IC, the microcontroller is from the 1.2 V rechargeable nickel-metal hydride battery minus the diode drop here.

**Dave Jones:** So, that's why we need a really ultra-low voltage microcontroller that can operate from anywhere, as we saw in the data sheet, from 0.9 V all the way up to 5 plus volts.

**Dave Jones:** So, you need that entire span to have such simplistic circuitry like this and powered from the single cell. Now, what we've got here is of course the motor is connected directly across the battery with the N-channel MOSFET goes directly to the IC control and it can switch that off or on under intelligent control.

**Dave Jones:** And it is actually this particular toothbrushes that like the top of the range professional model and it does things like actually pulses the motor to after a certain time to let you know, you know, oh, you've been brushing your teeth long enough.

**Dave Jones:** So, you know, so it can do smart stuff like that because it's under IC control like that and it's very simple, just a standard N-channel switch there. And we've got a simple RC filter here which goes off which allows the that 4-bit analog to digital converter inside the microcontroller or it might even be a you know, a better resolution analog to digital converter allows it to measure the

**Dave Jones:** battery voltage during charging. Now, as for charging itself, it's very simplistic. We've got a switch up here. I don't know whether or not it's a whether or not it's a MOSFET or it's a bipolar device.

**Dave Jones:** It's a little sot23 package and it basically directly there doesn't seem to be any current limiting Uh, there in series with it. it basically it looks like it connects directly from the uh, four-way rectified um, voltage on the power coupling coil here, straight through to the battery like that.

**Dave Jones:** So, really they they're relying on the um, the maximum current available extracted from the power coupling coil is the maximum charging current for the battery. And as you saw, they actually pulse that uh, charging at around about 800 hertz or there abouts.

**Dave Jones:** And uh, we've got some uh, filtering here of course for the uh, rail and uh, some reverse diode protection there. And the charging LED uh, over here which it you saw that they flash it once every two seconds or whatever while it's charging.

**Dave Jones:** And that's basically all there is to one of these rechargeable toothbrushes. And as for the base unit, yeah, unfortunately I was right. I took off this uh, back thing here and you can see the potting compound in there.

**Dave Jones:** Really freaking annoying. So, I'm afraid uh, we're not going to be able to see inside that one cuz I quite frankly couldn't be bothered. Actually, it's not that I couldn't be bothered.

**Dave Jones:** I've actually uh, run out of time for teardown Tuesday. I've got to head home and edit this video to make sure it's up on Tuesday. But uh, there you go.

**Dave Jones:** That is um, inside one of these electric toothbrushes. They're rather they're interesting. I hope you liked that uh, teardown. And if you want to discuss any of this, if you're into um, all this uh, power uh, wireless power transfer technology and uh, stuff like that, there's a lot of uh, a lot of art involved in this sort of stuff.

**Dave Jones:** And if you want to discuss it, jump on over to the EVblog forum. And remember as always, if you like teardown Tuesday, please give the video a big thumbs up and we'll catch you next time.
