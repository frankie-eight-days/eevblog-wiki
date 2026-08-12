---
video_id: _FIiolI37RU
title: EEVblog #656 - Pacemaker Monitor Teardown
url: https://www.youtube.com/watch?v=_FIiolI37RU
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 35, "3": 50, "4": 63, "5": 72, "6": 95, "7": 110, "8": 126, "9": 137, "10": 148, "11": 157, "12": 166, "13": 181, "14": 195, "15": 205, "16": 216, "17": 226, "18": 240, "19": 260, "20": 268, "21": 282, "22": 293, "23": 307, "24": 320, "25": 330, "26": 343, "27": 356, "28": 369, "29": 381, "30": 393, "31": 405, "32": 419, "33": 432, "34": 445, "35": 460, "36": 476, "37": 494, "38": 512, "39": 522, "40": 536, "41": 550, "42": 560, "43": 579, "44": 595, "45": 604, "46": 615, "47": 625, "48": 643, "49": 659, "50": 678, "51": 688, "52": 702, "53": 711, "54": 720, "55": 734, "56": 749, "57": 759, "58": 771, "59": 790, "60": 802, "61": 814, "62": 834, "63": 843, "64": 858, "65": 870, "66": 882, "67": 891, "68": 904, "69": 919, "70": 933, "71": 948, "72": 962, "73": 973, "74": 986, "75": 996, "76": 1010, "77": 1025, "78": 1035, "79": 1051, "80": 1065, "81": 1080, "82": 1090, "83": 1106, "84": 1119, "85": 1129, "86": 1137, "87": 1151, "88": 1165, "89": 1179, "90": 1193, "91": 1208, "92": 1218, "93": 1230, "94": 1248, "95": 1257, "96": 1264, "97": 1286, "98": 1309, "99": 1329, "100": 1351}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. This one was sent in to the mail bag segment by Matt, so thank you very much Matt. And it's a remote pacemaker monitoring device and we saw a little bit of it on the mail bag, but it's basically a custom device designed for St.

**Dave Jones:** Jude Medical Center. It's the House Call Plus Transmitter model 3180T and I couldn't readily find any um info on it or anything like that. So, I think that's why I do think it was a custom manufactured that says manufactured for them anyway.

**Dave Jones:** And what it does is it presumably allows you to call up the hospital, call up the doctor or whatever, you know, there's a phone number in there. Well, there's not, but there should be.

**Dave Jones:** And you dial up, there's a phone port on the back and you can talk to someone and then you can put on these wristbands here. You can use this inductive pad to communicate or send something to your pacemaker.

**Dave Jones:** So, you stick this on your chest and you can talk to someone while you're doing it. They can probably give you instructions, you know, relax, breathe in, breathe out.

**Dave Jones:** I don't know. If anyone has a pacemaker and actually uses one of these things, please let us know, but yeah, it should be rather interesting. It's got a phone line interface and because it is a medical device, it will have different certification requirements in terms of like the power adapter and stuff like that.

**Dave Jones:** So, this power adapter here is not just a regular power adapter. It's well, it might be, but it's been certified for medical equipment. So, presumably it's got like better isolation and better type approval and testing and stuff like that.

**Dave Jones:** Presumably that's what that cardiac symbol there is. So, that uses 5 volts at 5 W there. So, anyway, should be interesting. Let's crack this thing open. And by the way, if you haven't seen some pacemakers, here they are.

**Dave Jones:** This is what gets implanted into you. And well, I'm not sure how old these particular ones are. They're probably a bit more modern these days, but these were sent in to the mailbag by Manu a long time ago.

**Dave Jones:** Sorry, Manu, I haven't got around to tearing these things apart. They are like ultrasonically welded around the outside. You can see so they require, you know, and probably potted inside or something like that.

**Dave Jones:** So, require quite a bit of tear down. I'm not sure if they still got a battery in there and can be powered up. And not even sure if they're probably not even compatible with this thing.

**Dave Jones:** All the different brands brands would have all their own protocols and things like that. But anyway, these are the pacemakers. And yes, these ones have been removed from somebody.

**Dave Jones:** They have been thoroughly cleaned and sterilized. So, it's okay. But yeah, I still got these for a future tear down. But that is what basically sits under your chest.

**Dave Jones:** And then you come along with this inductive pad like this. And presumably there's a matching resonant coil in there. And you can actually communicate to the device and get some sort of a diagnostic or maybe even reprogram it or something like that.

**Dave Jones:** I'm not quite sure what to expect inside here. There won't be a lot. Like there won't be a huge amount of processing. There's no big display on the thing.

**Dave Jones:** So, there's no point powering up unless we wanted to see actually what we got out of the inductive curl coil to see if it actually transmits anything. But it may not unless you make a connection and stuff like that.

**Dave Jones:** It may not actually do anything at all. So, anyway, there's four screws. Here we go. So, there won't be a huge amount. There will be some processing, of course.

**Dave Jones:** And Uh, sort of comms for the phone line and here we go. We've got some light pipes. There we go. There's a little light pipe for diffusing and getting the LEDs out.

**Dave Jones:** That's a nice touch. They've gone to a bit of trouble there and in we go and we've got the speaker. They've got some nice acoustic Well, you know, it's a little They've gone to a bit of trouble to make the acoustics a bit better inside this thing so you can The idea is that you dial up and you know, you call the hospital or call the doctor

**Dave Jones:** or whatever and they talk to you and you can use this hands-free. You don't have to, you know, sit with your with the phone up against your head and stuff like that.

**Dave Jones:** So, nice bit of strain relief in there. Check that out. There we go. Got a little nice little rubber grommet and they've curved the cable around like that on both the left and the right uh sensor wrist strap.

**Dave Jones:** So, that's that's quite neat and they've done exactly the same thing up the top here with the uh There we go. That is how you do strain relief properly.

**Dave Jones:** That is really good. Doesn't get much better than that. Awesome. Huge thumbs up to the designer there. And here's the volume slider on the side. It's just like an exposed carbon track one like that.

**Dave Jones:** I don't particularly like those cuz they can get gunk in them, but this is you know, pretty much a sealed unit. So, you know, it's not like there's vent holes and fans and everything else actually collecting dust in this thing.

**Dave Jones:** So, yeah, that's adequate for the task. Here's the main PCB. I'll get in there and we'll check out the individual chips, but it looks like we've got two main devices here.

**Dave Jones:** We've got some firmware there and, you know, some line interface stuff over there. Then we'll have a closer look at the board. Some transformer isolation here going around to the pads, of course.

**Dave Jones:** You can actually see it. So, if If this top lid board out here, you can see the isolation. Look, right going around there. It's covered by that sticker down there, but look at the huge ground plane isolation running under that transformer there.

**Dave Jones:** And if that transformer isolation wasn't enough, belt and braces, of course, when you got something like this, you're going to put a big ass series resistor in there. Check it out, 330 K a pop, and they aren't mucking around there.

**Dave Jones:** Look at the isolation on that. So, nothing's going to go wrong and arc over and that sort of thing. You have huge big 330 K power resistors in series with each one of those sensor lines.

**Dave Jones:** That is how you design medical devices. And presumably, you'd have to do that sort of stuff to pass compliance for isolation because, you know, this is used by the user in their home.

**Dave Jones:** And of course, you have these two metal straps connected to each arm. Look at that. That has to be the most dangerous electrical body connection scenario for electrocution that you can possibly have.

**Dave Jones:** So, no wonder you have to have the series resistors, the transformer isolation, the ground plane isolation, everything else when you're hooked up like this. I wonder if these even have a series resistor in them like you get on the anesthetic wrist straps.

**Dave Jones:** And we can check for that. Here we go. Ta-da! No, that's a dead short, so there's no series resistor in there like you'll get with those ESD straps. They'll typically have a 1 meg resistor, um often embedded into those things.

**Dave Jones:** So, you have direct connection from both of your wrists on each arm into uh directly in the circuit board. That's why you got the big ass series resistors, the big ass transformer, and the nice ground plane isolation.

**Dave Jones:** Beauty. And if we have a closer look at the sensor pad electronics here, let's go in and see what we can see. We've got an LMV 824. That's just a precision quad op-amp.

**Dave Jones:** We've got a max 4334 another precision quad op amp, 393 comparators, HCT174, and yeah, a few other comparators and well, not much else. So, that's about it for the sensor pad connection.

**Dave Jones:** So, it's basically just amplifying the differential signal probably amplifying the signal from the sensor pads and then coupling that back over the transformer there. And I couldn't find any ready data on that transformer, but here we go, we've got an optocoupler here.

**Dave Jones:** It's a CNY64 series from Vishay and sure enough that meets medical devices compliance requirements in this case VDE0750 and IEC 6601 medical standard. So, yeah, specifically designed for medical stuff.

**Dave Jones:** Now, it's interesting to note how they actually did this front panel and what effort the designers went to. Look, they've got this vertical header. This is the user interface.

**Dave Jones:** They've got the uh header on the back of that. And so, the pins on the board, that sits in there like that. LEDs shining up vertically and then they've got the right-angle light pipe going across like that.

**Dave Jones:** That's a you know, that's a lot of effort to go to to build that second board and populate that whole different assembly design and get custom-made the light pipe and everything when you really could have just you know, stuck the LEDs out the front and been a bit how you're doing with it.

**Dave Jones:** But, this is like really professional. They've gone to a lot of effort to do that. And more attention to detail here, they haven't just you know, slapped on the microphone.

**Dave Jones:** They've actually wired it over separately, used their own used its own connector, and they've mounted it in a little rubber shock-absorbing holder, too. Awesome. And no real surprises for finding an Analog Devices DSP in here, ADSP 2185 series 16-bit DSP 80 mips.

**Dave Jones:** Pretty beefy for something like this. I kind of expected to find, you know, a reasonable amount of processing in here. Not huge, but of course they have to do some sensor conditioning and stuff like that.

**Dave Jones:** So, you know, a DSP is really good for that sort of stuff. So, there you go. There's the external firmware up there for it and that's about all she wrote.

**Dave Jones:** It's probably not processing the voice from the microphone or or anything like that from the actual call. The reason you can tell that is cuz the microphone's all the way over here.

**Dave Jones:** We've got this other mysterious device over here which is almost certainly coupled directly into that. So, you can tell these sort of things just by, you know, physical location on the board.

**Dave Jones:** So, this is obviously the, you know, the telecoms processor which handles the voice and the connection and data and well, it's probably just getting, uh, you know, serial data from, oh, you know, serial parallel data from the DSP over here over to it and then transmits the data back.

**Dave Jones:** That's about all she wrote. So, see if we can get some data on that. And yep, I was right. No surprises whatsoever. This is a Conexant CX88168. Basically a smart modem in a chip with voice codec capabilities.

**Dave Jones:** Hence the microphone input directly on here and it can do like answering machine function. So, it's a full V.90 V.34 modem. So, it can do your, you know, your old school 56 kbits per second modem interface and with voice as well.

**Dave Jones:** So, you know, it'll be driving the speaker directly, microphone, speaker and accepts data from the DSP processor up the top and well, that's all she wrote. You wouldn't roll your own solution there.

**Dave Jones:** You can buy these off the shelf designed specifically for this task. Aha, wasn't 100% right on that. This main uh smart modem over here, yes, is the main chipset, but it doesn't have the voice codec built in.

**Dave Jones:** It has a companion chip, which is optional, which you they need in this case, of course. And there you go, the 2437, that is the voice uh codec part of it.

**Dave Jones:** This one's actually a pretty powerful beast. It's got a microcontroller built in with one uh megabit of RAM and uh 2 megabit of uh program flash memory as well.

**Dave Jones:** So, quite a powerful beast, and there's our speaker connector and driver over there. And once again, with the isolation, look at this. You can see the isolation start over here from the uh telephone interface here, going across.

**Dave Jones:** So, we've got some um uh suppression uh happening there, some AC suppression, but there are high uh voltage uh withstanding um ratings. And then you got the isolation with your optocoupler coming across here, and that thing is completely isolated.

**Dave Jones:** And let's let's take a look at that meter electronic uh relay up there. And of course, when you're on a winner, you're going to stick to all the same chipsets.

**Dave Jones:** So, once again, Connectsant um that's the 2463 line side device, they call it. So, that's got a codec in there and handles all the uh modem line side interface uh stuff.

**Dave Jones:** So, you can see that on the uh block diagram here of how all these pieces go together. Although this uh device Although the main uh device, the smart modem, looks like a different one they're using, but the uh line side device and the voice uh codec is um designed as part of this, you know, one big package.

**Dave Jones:** And that's what you're looking for. These manufacturers specifically provide this sort of stuff, so that it makes, you know, uh custom designs like this really quite easy, just off-the-shelf app note stuff, pretty much.

**Dave Jones:** And we've got ourselves an unpopulated uh serial or other sort of uh in a face here. Look at the big isolation slot they've got under the transformer there. That's not there.

**Dave Jones:** And they haven't populated this. There's a JTAG. Presumably that's the programming header. Of course, it is the programming header for the DSP. And yeah, we could probably try and get some, you know, if you really wanted to hack and have a little reverse engineer play around with this, you could try and find a serial interface or just get in there and and play around with the thing.

**Dave Jones:** And then over here, of course, we've got the power supply, little PCB mount heat sink here. Nothing much happening there. No huge power requirements on this thing. So that's probably adequate.

**Dave Jones:** Nice Schaffner common mode choke here. And if you're wondering what that little meter device down there, it looks like a little coaxial relay, but it's not. It's only two terminal, but it is actually a reed relay.

**Dave Jones:** It's a magnetic switch where instead of having a coil in there to actually activate activate it by an external magnetic field. So presumably it cuts off power to the sensor coil.

**Dave Jones:** It's just so, you know, just the proximity to it there. But the way it actually works is in the case here. There we go. They've got a little cutout and that sits when you fold that in.

**Dave Jones:** Sorry, we've got a mess of wires here. But when you when you fold that in, that actually sits on top of there. And where's the magnet? Well, here it is on the case.

**Dave Jones:** Ta-da. So when this case closes shut like this bingo, it goes down and disconnects the power. In fact, that may not be, come to think of it, the sensor.

**Dave Jones:** It may be actually disconnecting the power to the entire device. There's really nothing worth writing home about. There we go. We've got the LMV 824s as well. If you're going to use them in your bill of materials, well, use them bloody well everywhere.

**Dave Jones:** And if you're wondering where the ADC is for the uh sensor um arm bands, here we go. The MAX1248 uh four-channel 10-bit uh AB serial ADC. And that looks like some sort of uh regulator.

**Dave Jones:** I'm not going to look up the number or uh some sort of regulator or voltage uh reference perhaps, but uh I can't find a DAC on here at all for driving the um the inductive uh you know, pad up there.

**Dave Jones:** So, really um I guess they're probably just driving it uh you know, digitally like, you know, square wave. There's no sort of, you know, like analog um modulation or anything else going on presumably.

**Dave Jones:** All right, let's just do a quick power up and uh see what we get here. Woohoo! Got some LEDs. I can hear the speaker uh sort of punching in and out there.

**Dave Jones:** And we've got some LEDs flashing. There's no uh Oh, there we go. Green flashing green. Whatever that means. I got uh no idea. But yeah, I'm not going to hook it up to a line and try and try and call the number or anything like that.

**Dave Jones:** Solid green. That's got to be good, right? Went from flashing to solid green. So, there you go. Let's see if we get anything at all out of this inductive pad.

**Dave Jones:** Maybe not cuz as I said, it might have to actually connect first before it actually generates um anything on this at all. All right, I've put the sensor pads on my wrist and uh just to see if it uh you know, it does anything.

**Dave Jones:** Um but no. Zippity doo da. Hmm. Oh, well, I didn't really expect it to do anything though. Okay, I'm just going to use my uh scope probe uh short it out here cuz that's what you can do.

**Dave Jones:** It's not It's Well, at DC, it's shorted out. But at higher frequencies, this actually works as a one-turn pickup loop. And you can use it as a crude pickup.

**Dave Jones:** If this doesn't work, then I can go to, you know, more turns and get a bit more creative and things like that. But anyway, it's on and it's not connected and I got that 5 mV per division and there's nothing much happening there at all, I'm afraid.

**Dave Jones:** That's just boring. So, no, there's nothing significant. You see a few blips in there. I believe that's from my fluoro lights here. So, yeah, you can see a bit of crud happening there, but if I turn my lights off, does that go away?

**Dave Jones:** No, it's there. So, but you know, look, common mode noise pick-up, whatever. See, see, you just saw the big big pulse there. So, that's obviously not coming out of the loop and I can verify that by actually taking it off.

**Dave Jones:** It's nowhere near the thing. I can actually even depower the device completely. There we go and we still get that crap. So, it's nothing to do with that. It's just, you know, pick-up from the lab here.

**Dave Jones:** Oh, and by the way, if you're wondering what that weird low frequency waveform was there before, I've shown this before. Look, watch this. Look at that. Just by banging your probe on the table, that is the piezoelectric effect.

**Dave Jones:** Anyway, if you want to see more of that, I'll link in a video here and you can check that out. So, there you go. I mean, I could try and coax this thing into, you know, transmitting something in here perhaps, but yeah, I don't think it's a hugely worth it.

**Dave Jones:** I could open this thing. I think there's, you know, there's probably just going to be a coil of wire inside the thing. Nothing fancy at all. It could be completely potted.

**Dave Jones:** That wouldn't surprise me. So, might be a pain in the ass. I might try and dig into it, but don't expect to find much at all. Well, well, well, what do you know?

**Dave Jones:** What sort of voodoo is happening inside here? I expected to find a, you know, an inductive coil, but no. Looks like we've got something else. That looks like the shield of the cable in there, connected to this.

**Dave Jones:** So, this is actually a three-wire interface. Look, you can see the green wire up here is connected through to the shield. So, we've got the black and the red has to be in here somewhere.

**Dave Jones:** Doing what though? And if I lift the skirt up on that, tada! No surprises. There we go. There's our inductive coil. Not a huge number of turns. I'm not sure how many turns in there, you know, a few dozen.

**Dave Jones:** Um large gauge. Uh Uh enamel coated uh wire. But yeah, nothing fancy. So, I'm not sure exactly uh you know, what that and that pattern uh is doing there.

**Dave Jones:** But anyway, it's you know, it is quite deliberate. So, yeah, sorry I couldn't uh get anything out of this uh puppy at all. But yeah, like I could probably if I spend enough time in it, coax it into maybe uh generating uh something.

**Dave Jones:** But uh it's just you know, it's not hugely uh worth the effort unless you had a specific need. So, uh yeah, sorry. We did it some basic checks and nothing came out of it.

**Dave Jones:** So, oh well, can't always win. So, there you go. I hope you enjoyed that uh Teardown Tuesday. These medical uh devices are usually uh quite interesting. And nothing, you know, it's pretty much what I expected.

**Dave Jones:** It's got a DSP in it. It's got a coil of wire to uh inductively couple over or resonantly uh inductively coupled probably over to your uh pacemaker. And well, and it's got a line interface, but it's really well engineered, really well designed inside here.

**Dave Jones:** So, they really knew what they were doing. And uh a classic example where, you know, uh some company was hired uh some engineering firm was hired to custom manufacture this.

**Dave Jones:** Uh I don't know how many, you know, they might have made a couple of thousand of them or something like that. Could have been more. I don't know how big uh St.

**Dave Jones:** Jude uh medical uh you know thing is and how many patients and stuff like that they got but presumably like every patient with a pacemaker maybe gets one of these so it could be could have made them in the tens of thousands or something but really well engineered classic example of where you know that the designer just uses all the off the shelf chip sets for the

**Dave Jones:** line interface for the codec the modem everything else and really you know there's there's custom of course sensing circuitry for the pads and driver and stuff like that and the rest is all in the firmware and how it talks as a system and some really nice touches inside this thing so it's not bad at all so thank you very much Matt for sending that into mailbag Monday

**Dave Jones:** that's a always an interesting teardown when you do what medical devices like this so if you got any more info I couldn't find like a a manual or anything like that little one specs for this thing but if I do I'll link them in down below as always all of the data sheets for the chips that we've seen in here will be linked in down below as

**Dave Jones:** well so if you want to check out the data sheets then please do and as always if you like teardown Tuesday please give it a big thumbs up cuz that helps a lot on YouTube rankings and all that sort of jazz and if you want to discuss it jump on over to the EV blog forum also linked down below and don't forget to subscribe if you haven't subscribed what are you

**Dave Jones:** doing catch you next time
