---
video_id: 9v6OksEFqpA
title: EEVblog #427 - HP 3478A Multimeter Teardown
url: https://www.youtube.com/watch?v=9v6OksEFqpA
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 32, "3": 56, "4": 67, "5": 77, "6": 88, "7": 103, "8": 112, "9": 129, "10": 145, "11": 154, "12": 165, "13": 182, "14": 195, "15": 213, "16": 223, "17": 246, "18": 269, "19": 292, "20": 305, "21": 328, "22": 341, "23": 350, "24": 360, "25": 377, "26": 388, "27": 397, "28": 417, "29": 431, "30": 443, "31": 456, "32": 466, "33": 481, "34": 493, "35": 507, "36": 523, "37": 531, "38": 549, "39": 563, "40": 578, "41": 594, "42": 620, "43": 634, "44": 645, "45": 658, "46": 670, "47": 678, "48": 695, "49": 715, "50": 724, "51": 748, "52": 764, "53": 782, "54": 806, "55": 825, "56": 845, "57": 857, "58": 878, "59": 897, "60": 911}
---

**Dave Jones:** Hi, this is just going to be a quick follow-up video to my previous one on the HP 3457A multimeter. And you notice that I mentioned the 3478A multimeter that I was replacing with the 3458A.

**Dave Jones:** And I just realized I thought I had done a video tearing down this 3478A, but I hadn't. So I thought I'd just take the covers off and I give you a quick look around and see how very similar it is to the 34 57A.

**Dave Jones:** And really the performance of this thing is almost identical, not too far off the 3457A. So if you don't need the fancy math functions or anything like that, this is an excellent and if you don't need the extra six and a half extra digit resolution, the six and a half digits, then this is an excellent five and a half digit multimeter.

**Dave Jones:** And you can pick them up for quite reasonable prices if you look around in pretty good condition. So highly recommended as a precision five and a half digit multimeters.

**Dave Jones:** But just a brief look at the back here, it's got almost identical inputs to the front, the four wire switchable. You can switch the terminals from the front to the rear, which can be quite handy.

**Dave Jones:** It doesn't have the current on the rear terminal, but certainly does have the two and four wire ohms input. It's got GPIB interface, of course, you can set the address.

**Dave Jones:** And this one is not auto line frequency sensing like the 3457A, which automatically when it powers up detects the line frequency and takes care of it. This one you have to actually switch it between 50 or 60 hertz there.

**Dave Jones:** Standard IEC mains input, external trigger out. And the case comes off this thing quite easily. There's just two screws at back plus one on the bottom. And it just slides off.

**Dave Jones:** And single board construction basically apart from the switching board here to switch the uh terminals from the front to the back, but it's a very similar design. This this is a previous design of the 3457A.

**Dave Jones:** It actually predates it, but you can see the similarities between the two and they use lots of common parts as well as we'll see. And it's got a nice extension bar up here for the main switch and there's a main switch tucked in there very nicely heat shrunk out in there.

**Dave Jones:** They've got just a regulator, a linear, I believe it's a linear regulator. It's got a HP part number on it. Just put some wires over to here like this.

**Dave Jones:** That'll be the regulator that's powering all of this digital stuff all around here. The main processor, there's the backup battery which we'll talk about and they're just using that for heat sinking on the side.

**Dave Jones:** I mean, I don't think this thing uses much power particularly. So, that's why they can get away with the linear regulators inside this which are of course much quieter than having switching regulators and that's why they need less shielding and stuff like that inside, but there's our mains transformer there.

**Dave Jones:** It is fused on the back down there. We've got our GPIB cable going across and they basically split this thing into the just like they did in the 3457A.

**Dave Jones:** They split it into the digital or the processing and display section up here and then electrically isolated from the analog or measurement part down in the bottom here. You should be able to see that split pretty clearly from I'll show you more detail in here, but it basically splits around like that.

**Dave Jones:** There's this shield here which we'll take a look at and you can see that there's no traces and they ground planes are separated between these two halves here. These are obviously our two optocouplers.

**Dave Jones:** So, it's got that single serial line in and out actually connecting the two sections just like the 3457A and there you go. And this section, of course, has its own power supply its own transformer tap on there, completely isolated, goes into some linear voltage regulators here, plus minus 12 or 15 volts or something like that, and a 5-volt regulator as well.

**Dave Jones:** Powers all this circuitry in the measurement section. And you can see the two opto isolators there. They've got the HP part number. I won't bother looking it up. Some people in the forum have posted uh links to cross references of all the part numbers to their real things, but they'll be just, you know, like 4N25s or some sort of similar type optocoupler.

**Dave Jones:** It is an 8-pin DIP package, though. Now, curiously, the service manual I've got for the 3478A doesn't show these two devices. It actually shows two transformers instead. Actually, you know, transformer coupling the serial signals from one side to the other, but that's not what's going on here.

**Dave Jones:** So, there's clearly some design differences between these units. So, if you've got any idea where you can clarify that, please let me know. And yes, lots of those HP part numbers all the way through this.

**Dave Jones:** Probably half the chips in here have HP part numbers on them. Now, you'll notice in here that there's another actuator arm going up there like that, which mounts on goes to this riser board which has a presumably a very high-quality low EMF switch up here, which basically switches all four of the terminals from the rear.

**Dave Jones:** They go along the bottom of the case down in there. They're not shielded at all. They don't really need to be cuz there's not a lot of, you know, really high-frequency switching stuff really just spewing out noise in this thing.

**Dave Jones:** So, it's you know, it's not going to be too bad at all. And it's more than good enough, obviously, for the performance of this fairly precision 5 and 1/2 digit meter.

**Dave Jones:** But there's the four terminals on the back there, and they just switch those through. Either the front terminals are also wired through similarly front and the back. Very simple, but it works.

**Dave Jones:** And you'll notice the identical switching input switching hybrid here. That's used in its big brother we saw in the previous video. And there's lots of similarities, of course. These Koto high-quality Koto relays down in here for the switching.

**Dave Jones:** There's not nearly as many of them as there in is in its big brother. So, presumably less self-testing and stuff like that, but it still does have self-test and switching capability.

**Dave Jones:** So, really high-quality relays, high-quality parts as far as the eye can see. And the measurement process is a bit different. Instead of an 8051, it's actually an 80 Intel 8049.

**Dave Jones:** Most of the chips in here are 1990. So, this unit was uh it built in late 1990 or thereabouts, or maybe early 1991. And you'll notice exactly the same hybrid multi-slope analog-to-digital converter chip.

**Dave Jones:** Or it's actually the logic for the analog-to-digital converter. It's not an actual analog-to-digital converter as you know it. It's the external the external integration capacitor around the outside, the external switching and stuff like that is done outside.

**Dave Jones:** This is just the logic for a multi-slope analog-to-digital converter, which is a quite a neat way to do it. And of course, the voltage reference, absolutely identical linear technology.

**Dave Jones:** It's got the HP part number, but as we found out, that is a linear technology LM399. So, exactly the same voltage reference. I presume it's the same grade that's used in its big brother.

**Dave Jones:** So, the specs are going to be very similar, if not identical, to its big brother. I think they are slightly different in some respects, but not by a huge margin.

**Dave Jones:** That's why if you don't need the extra digit resolution and you don't need the math functions, this um 3478A is a really great precision meter. Now, there's some uh talk about this multi-slope uh analog-to-digital uh converter technique on the uh forum.

**Dave Jones:** So, it's well worth reading and it is a very interesting technique. It It basically um it's you know not too dissimilar, I guess, to uh your traditional uh dual slope integration.

**Dave Jones:** And it basically measures the uh the time period. So, it's basically a really precise timer instead of being a more traditional analog-to-digital uh converter as such, like a flash analog-to-digital converter, etc.

**Dave Jones:** It's based on precision timing measurements of charging and discharging a reference capacitor to a known reference voltages. And you can get very precise and by using a few tricks, very quick way to uh actually uh sample.

**Dave Jones:** That's why these things can have, you know, hundreds of samples per second. And you can see the 1 nF reference uh cap down there, C410, I believe it is.

**Dave Jones:** And yeah, it's plus minus 10%. Like its actual value does not matter. Once again, it's the stability of that cap capacitor with temperature. So, that would be a low a very stable low temp co uh capacitor, some sort of, you know, polyprop or uh something like that.

**Dave Jones:** Some sort of uh precision capacitor that would have been carefully chosen for this application. And of course, it's a dead giveaway uh that it's the reference cap because look at its physical size and proportions for a simple what?

**Dave Jones:** A 1 nF cap. You know, you could have just used a you know, a crappy bypass cap like this if it was just doing bypass application. So, it's a dead giveaway that you don't see caps like that unless unless they're used for precision applications like this one.

**Dave Jones:** And there's differences in the main processor section over here. The main processor is actually an Intel 8039 and if we go over to here, we can see an Intel 8291A GPIB controller.

**Dave Jones:** And this looks like the original Panasonic battery in this thing and it's still measuring 3.49 V, so still probably has some life left, but there's been a bit of discussion about these batteries on the EEVblog forum and how they can possibly have, depending on the type, a very flat discharge characteristic and not being able to determine, you know, how much life is left just based on the measured voltage.

**Dave Jones:** So, if you do get this sort of gear, it's often it's not a bad idea to actually replace the batteries, but as I mentioned in the previous video, this battery holds all of the calibration data in the volatile memory.

**Dave Jones:** So, if you simply just desolder this thing and wire in a new one, there's no internal capacitor on there to keep the charge on this thing while you replace the battery.

**Dave Jones:** So, if you simply just take it out and replace it, you're going to lose all that calibration data and your meter is useless. You got to send it away and pay the same money or more again as what you paid for it to get the thing properly traceably calibrated.

**Dave Jones:** So, really when you're replacing these batteries, you need to be very careful because the negative terminal on here, which is up here, is going to be mains earth referenced.

**Dave Jones:** If you use your soldering iron, for example, even if you power this thing on, if you leave the power on when you actually solder it, it might be okay.

**Dave Jones:** The soldering iron goes on the negative terminal over here, it's all ground mains earth referenced, you're not going to do any damage at all. But if you then place your iron on this positive terminal over here, bang, you've just shorted it out to mains earth and directly back to the negative terminal.

**Dave Jones:** You shorted out the battery and you could potentially, if you're not careful, lose your calibration constant. So, what you need to do is actually, well, the safest way to do it is to um solder another battery in parallel or diode or it in there.

**Dave Jones:** I would actually solder it on. Some people say, "Oh, you can just connect it in there." And you know, with uh alligator clips or something like that, but if you get a dodgy connection, uh you can lose your data.

**Dave Jones:** I wouldn't risk it. I would actually go to the effort to solder another battery in there, possibly diode or with this one, so that you can keep that contents alive while you safely desolder this one with the mains uh power cord disconnected, so that you don't create any earth loop shorts in the thing and short out the battery and therefore your contents.

**Dave Jones:** So, just be careful. And the manual for this one says the battery is supposed to be a lithium sulfur dioxide one, but it's clearly not because they would be Well, and it says it on there as well, plus 3 volts, but this one's actually, um you know, a 3.45 or a 3.5 volts.

**Dave Jones:** So, clearly they've put a different type in there. Now, this shield here is rather interesting. You notice that's actually connected down to a trace down there and it's connect it's bent like that and it's sort of shield it's a sort of attempting to shield some of the digital circuitry over here.

**Dave Jones:** You notice it's right near the crystal and that's probably the reason why it's doing it, probably trying to shield it from one side to the other. And you'll notice that that a trace actually goes around here and if you follow it, might not be easy to get on camera, but it goes down to this brown wire here, which then jumps over to the LCD um a point on the

**Dave Jones:** well, on the keypad board down there and then it goes off through the case. I'll try and get it and then it actually comes and it's connected onto the earth chassis down here and of course that then that earth is then connected over to the mains earth terminal all the way over here.

**Dave Jones:** So, yeah, that shield is mains earth referenced but they've actually got they've gone to the trouble to sort of flow that around the board there. You can see that trace snaking its way around like that so they're isolating that they're trying to shield all of this part of it from the measurement part of the circuit.

**Dave Jones:** So, I'm not not sure of the of the you know, the advantage of just that shield like that. It's not like it's you know, a can covering all of the digital circuitry any or anything like that.

**Dave Jones:** So, I'm not sure of its actual effectiveness. But it's obviously a strategically located. I don't think it's an accident that the main crystal and there's the main processor and there's probably you know, a fair bit of that's probably around here is probably the highest frequency stuff that we've actually got happening inside this multimeter.

**Dave Jones:** So, they just I don't know. They've decided to add that in. So, there you have it. There's a classic HP 3478A. Just a quick look inside this thing. It's well worth just downloading the service manual and having a read and start reading about how the multi-slow buck converter works and other stuff and they're quite fascinating devices.

**Dave Jones:** Very well engineered. As I said, I highly recommend picking one up if you're in the market for a precision five and a half digit multimeter. If you can get it for a reasonable price on eBay, by all means do so.

**Dave Jones:** So, if you want to discuss it, jump on over to the EEVblog forum. Catch you next time. Mhm.
