---
video_id: U1nsYd3lG60
title: EEVblog #399 - GoPro Hero 2 Teardown
url: https://www.youtube.com/watch?v=U1nsYd3lG60
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 25, "3": 44, "4": 54, "5": 74, "6": 88, "7": 102, "8": 115, "9": 123, "10": 134, "11": 144, "12": 157, "13": 171, "14": 186, "15": 199, "16": 212, "17": 232, "18": 243, "19": 257, "20": 265, "21": 279, "22": 289, "23": 307, "24": 319, "25": 335, "26": 356, "27": 373, "28": 387, "29": 397, "30": 408, "31": 424, "32": 434, "33": 451, "34": 463, "35": 477, "36": 502, "37": 516, "38": 531, "39": 543, "40": 562, "41": 573, "42": 584, "43": 601, "44": 611, "45": 642, "46": 659, "47": 670, "48": 688, "49": 698, "50": 719, "51": 737, "52": 750, "53": 762, "54": 774, "55": 790, "56": 809, "57": 820, "58": 831, "59": 841, "60": 855, "61": 867, "62": 881, "63": 898, "64": 909, "65": 923, "66": 936, "67": 948, "68": 962, "69": 971, "70": 985, "71": 1012, "72": 1038, "73": 1051, "74": 1059, "75": 1078, "76": 1092, "77": 1102, "78": 1114, "79": 1126, "80": 1148, "81": 1164, "82": 1182, "83": 1195, "84": 1207, "85": 1227, "86": 1240, "87": 1251, "88": 1265, "89": 1285, "90": 1305, "91": 1318, "92": 1334, "93": 1355, "94": 1366, "95": 1377, "96": 1389, "97": 1402, "98": 1416, "99": 1426, "100": 1442, "101": 1461, "102": 1476, "103": 1495, "104": 1505, "105": 1521, "106": 1537, "107": 1553, "108": 1566, "109": 1577, "110": 1599}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Why do I look and sound a little bit different? Because I'm shooting this with the GoPro Hero 2 action cam, not my regular Canon HF G10.

**Dave Jones:** So, you've probably seen the lab like you've never seen it before. This thing's got a massive 170° wide angle lens on the thing. It's huge. So, I thought it'd be interesting to take a look what makes this thing tick inside.

**Dave Jones:** No, it's not the new uh Hero 3 model. It's the older Hero 2, but should still be interesting. Let's go. Woohoo! Check it out. Love it. Huge wide angle on this sucker.

**Dave Jones:** And it can also do non-wide angle as well. I've set it to a 127° medium view angle. So, this is exactly the same shot as before. Here you go.

**Dave Jones:** So, this is a 127 degrees. And exactly the same shot again with the 90° narrow field of view. So, it should be a hell of a lot different to the wide angle 170° we had at the start.

**Dave Jones:** And just as another interesting comparison, I've turned my main LED lights off here up above me, which you've seen in a previous video, and still on 90° narrow angle, and I just checked out the previous footage of this, and there was quite a bit of noise on there with the main light on.

**Dave Jones:** I mean, you know, picture noise from the sensor. So, there should be even more noise in the background now. Yes, I know you want to see the teardown, but I can't help myself doing a bit more comparison.

**Dave Jones:** This is back to the 170° wide angle, i.e., the normal mode for the GoPro, and once again with my main LED light off. So, it's relatively dark here in the corner without it.

**Dave Jones:** I think you've seen previous video with the, uh, light measurements. It's only a couple hundred lux or something like that. So, there should be less noise than the narrow angle.

**Dave Jones:** It seems that the narrow angle mode on this thing, um, drastically, uh, increases the picture noise. I think I just realized why there's more noise on the narrow angle version.

**Dave Jones:** It's because it's probably gaining up a lot more cuz you can only see this much. So, there's no bright stuff in this scene. It's all dark, so it gains it right up and, uh, causes that greater noise.

**Dave Jones:** But, the wide angle you can see all the bright stuff down that end down there and that, uh, keeps the gain lower and, hence, lower noise. That's the theory, anyway.

**Dave Jones:** Let's get to the teardown. Now, I do love these GoPro HEROes. There's just something wonderful about a, uh, product designed just optimized for a specific purpose and nothing more.

**Dave Jones:** And these are action cams. The thing is small and light. There's no LCD on the back or anything like that. It's got an expansion, uh, header, of course. And, um, it, you know, it's just designed to do the job.

**Dave Jones:** It's got a low-power, um, front panel status LCD. There's only two buttons, very minimalist interface, but it's actually very easy to use. It's got a huge, um, status LED on the front and also a status LED on the top.

**Dave Jones:** And, um, on the back as well. So, no matter no matter what angle you view this thing from, you're going to see the status LED. And it can be, you know, the firmware's quite smart.

**Dave Jones:** It can be set to, uh, power up and automatically start recording as soon as you switch the power on. Uh, just really neat. SD card slot, um, HDMI, um, output cable, um, external, uh, audio, external mic, USB interface and, uh, and a, uh, video and audio out.

**Dave Jones:** It's just really really nice. Beautifully designed. Anyway, this is not a review. This is a teardown. There's a million reviews out there. This thing is the duck's guts. Now, let's take the battery out.

**Dave Jones:** Well, it's the duck's gut guts of uh action cams. So, um looks like we can get through four screws in there and check out inside. I don't expect it to be hugely, you know, groundbreaking.

**Dave Jones:** There'll be a board or two with, you know, there'll be some flash memory, there'll be a main uh processor, and there'll be a couple of other support stuff and things like that.

**Dave Jones:** It won't be terribly exciting, but anyway, you never know. Let's go. And that's the thing. There's really, you know, not a lot of hardware that goes into uh doing something like this.

**Dave Jones:** It's all uh I mean, you know, there's going to be a lot of technology put into uh the, you know, choosing the right sensor and the right lens and stuff like that.

**Dave Jones:** But, as far as actual hardware goes, I mean, it's not uh rocket science to do a little camera like this. And uh you know, take the output from a sensor and drive an LCD and save the uh you know, do the uh H.264 compression these days and put it onto an SD card.

**Dave Jones:** I mean, you know, that was rocket science 10 years ago, but uh these days, it's uh pretty easy to do all that stuff. So, I've got the um got the screws out.

**Dave Jones:** Uh yeah, heard something crack. Here we go. Something's got Something's got to give. Well, it looks like we have to get this sticker off perhaps. That seems to be holding it down.

**Dave Jones:** So, let's Yeah. Let's peel that off. Tada! Gonsky. All right. Now, it should all pop open. We've got a cable. Can feel a cable. Ta-da! There it is. Oh, look at that.

**Dave Jones:** We've got a what looks like a heat sink here. I can't see another reason for that aluminum plate there, but yeah, we've got some quite high-density surface mount stuff in there, so let's see if we can get further.

**Dave Jones:** It looks like there's Well, there's one main board, standard 1.6 mm thickness in there. You can see it. So, it looks like what we've got in here is a secondary board down there for the expansion header.

**Dave Jones:** We've got some flat flex going over to a flat flex connector. So, we'll whip that off. We've got the microphone uh insert up there. They've got that going over on wires.

**Dave Jones:** I'm not sure why they decided to do that rather than say integrate it um onto the PCB here and just have it directly stick through the holes in the top of the case.

**Dave Jones:** I'm not sure why they've made that decision. There was some reason for that, obviously, and looks like we've got another flat flex going over here, possibly to the um uh well, either to the LCD or and or the sensor.

**Dave Jones:** So, no, there's another flat flex. Yeah, there seems to be uh quite a few, so this might be another board under this one as well, but it's quite densely packaged in there.

**Dave Jones:** I rather rather like it. I don't think they've wasted anything in terms of um space. I mean, they could have um slimmed it down a bit, which is what they've done in the Hero 3, I believe, which is smaller and lighter again than this one.

**Dave Jones:** So, um yeah, they've, you know, this one is they, you know, they got it to market. They did exactly what they wanted, but they yeah, they could have uh trimmed it down and possibly made it a bit smaller perhaps.

**Dave Jones:** We'll just leave it that up there to get our flat flex cable out. It should just pull out now. Nice. Done. There's our USB connected down there. Yeah, definitely a second board down there of course.

**Dave Jones:** Looks like we've got possibly more metal work under here. Yep, there we go. So, fair bit of metal work in this thing. So, all that metal work in there would be for uh heat sinking of the uh sensor and the processor, I'm assuming, because they're uh fairly grunty little things in terms of uh you know, uh through you know, data throughput and uh stuff like that.

**Dave Jones:** So, um they are going to be dissipating a little bit of power especially in a small case like this and especially in one that's uh designed to be uh sealed up and where the basically the heat uh cannot escape.

**Dave Jones:** So, um in terms of uh you know, you want extra thermal mass in there uh because you know, the heat's not going to get out through the uh clear polycarbonate um you know, underwater housing and stuff like that.

**Dave Jones:** So, you want this thing to still operate for a couple of hours uh while not overheating. So, they're going to add um a whole bunch of thermal mass in there with those aluminum heat sinks.

**Dave Jones:** And there you go, I took that plate off and uh that is the back of the sensor down in there and you can see the matching uh plate here has a has that um has that uh indentation which uh presses against the back of the sensor in there.

**Dave Jones:** So, it's dissipating the heat uh back out of there into this back plate. But of course, this uh big chunk of aluminum down in here is also going to be uh serving as a huge heat sink.

**Dave Jones:** But they went, "Well, that's not enough. We need to get some out the back as well. And um uh you know, uh possibly also what spread that into the battery, which this plate is against as well.

**Dave Jones:** So, here's the main board, and it is absolutely flooded with little 0402 uh passives. There's a bunch of resistor networks in there. There we go, you can see the resistor networks are in seven and so forth.

**Dave Jones:** And uh we've got a whole bunch of bypass caps. There's going to be all circuitry on the other side of the board, but there's a whole bunch of passives on there.

**Dave Jones:** We've got a couple of other support chips. And around here, we're going to have our lithium-ion battery charger and regulation as well. Around the power supply, and uh looks like there's a little There's some sort of header on the edge of the board here, possibly a uh you know, a system test header or a programming header or something like that for production.

**Dave Jones:** And I'm not sure what that 10-pin part is or what it's doing, but there's a couple of SOIC-23s around that as support. There's another five Sorry, a six-pin SOIC-23 down here.

**Dave Jones:** Yeah, a few other We've got a diode there. Not much else exciting happening here. We've got an unpopulated uh header over here, J6. I'm not sure what that one's uh doing at all.

**Dave Jones:** Once again, maybe some sort of development header or uh programming some sort of, you know, system test uh header connector or something like that. But that one over there is more likely to be some sort of system test connector than this one down here.

**Dave Jones:** I'd say that's probably development or something like that leftover. But there you go, there's the back of the sensor and uh see a bit of goop down in there.

**Dave Jones:** They've You'll notice these metal tabs here. They've hand-soldered those on the top of the board so it joins the top and the bottom board down in there. So I hope we can get this board out without having to uh desolder those cuz that would be a bit horrible, but um yeah, it's not not looking that good.

**Dave Jones:** And I've taken a few screws out around here and it looks like the whole thing might pop out as an assembly. Yep, look at that. Tada! Beautiful. There's our uh There's our LCD.

**Dave Jones:** It's hanging in there. Fantastic. So there you go, there's the front side of the unit. You can see the main uh LED there. See one of the tactile switches, the other tactile switch is uh on the board up there.

**Dave Jones:** So it looks like we've got three board construction in this thing and it really is uh quite a complicated little assembly. The flat flex there is just sort of pushed down into there.

**Dave Jones:** I can see a whole bunch of inductors along there. Check those out. They're quite uh large for a uh something like this and we've got another couple more down here as well.

**Dave Jones:** And our LCD, fully uh custom of course, doesn't cost you much to get a fully custom um LCD. So that's a custom uh COG chip-on-glass one there. You can see the chip in there.

**Dave Jones:** It's embedded on the glass like that. Has the driver. That's the uh driver for the LCD and it looks like it's just a uh serial interface there. There's some power and a couple of other lines so that'll be like an SPI interface um LCD or something like that that goes over to the uh flat flex connector over there.

**Dave Jones:** There's a rubber spongy rubber backing on that just holding it in place. And there's a bit of bulk capacitance in there with all those tantalums. And the lens pokes out through this board and that's fixed.

**Dave Jones:** I can't I'm not going to put much pressure on that, but I can't really budge that. That's all integrated into the large metal uh sensor heat sink at the back there.

**Dave Jones:** And of course that's you know, all of the performance and of this thing is of course due to the sensor and the glass lens in there. It is glass I believe.

**Dave Jones:** It's not polycarbonate. So they've specifically chosen that. That's why this thing gets awesome video quality. So they have joined these boards together. Look at this. Really rather annoying straps.

**Dave Jones:** And it looks like those straps are transferring power cuz one's labeled bat and then there's a huge thick trace coming out of there from these sock 23s and that looks like maybe a ground um tab over there.

**Dave Jones:** So it looks like that's how they're getting power through to the other boards. And you can see the battery in there. I believe it's a battery. I don't think it's a super cap.

**Dave Jones:** I think it is actually a battery soldered onto the main board for the real time clock. So it's interesting to see how this heat sink actually goes right through the entire thing and even right out to the SD card.

**Dave Jones:** Like it's it's got the cutout in there for the SD card. So they're really packing all of the three-dimensional space in here as much as they can with heat sinking.

**Dave Jones:** But that's not terribly surprising. As I said before they because the heat cannot escape this thing when it's enclosed in one of those um you in closed in the polycarbonate case.

**Dave Jones:** So, really they have to, uh, put all that heat sink in there to, uh, absorb it all and, uh, hopefully not get hot enough during the, uh, full operational time of this thing, which would be one battery charge.

**Dave Jones:** So, they probably did a lot of, uh, uh, thermal testing on this thing to ensure that it, uh, it did actually continue to perform and didn't, um, overheat in the, uh, sealed case.

**Dave Jones:** Over time, there might even be some, uh, temps and, you know, an over temp, uh, sensor in there, perhaps, although I've never heard of a report of a GoPro, um, overheating or anything like that, but they certainly, uh, may have.

**Dave Jones:** I don't know. Um, but yeah, I think you can bet your bottom dollar a fair bit of engineering would have went into the the, uh, thermal performance of this thing.

**Dave Jones:** Well, yeah, I decided to Google that and yes, you do find reports of, uh, these Hero 2's, um, overheating. So, there you go. That's why when you stick him in a case and the heat can't escape, that equals bad news for electronics.

**Dave Jones:** And I desoldered a bunch of those, um, board-to-board interconnects there and we can swing this board out like that. I haven't, uh, tried to take the lens off yet, but you can see on the bottom of that board they've got some, uh, Mylar or Kapton, uh, tape there just, um, insulating, uh, all those parts in there and, uh, and that power supply stuff we saw before.

**Dave Jones:** So, there doesn't seem to be much doing on there at all in terms of, uh, main circuitry. So, but we can get down onto this second board down here and of course it's, uh, dominated by the SD card, but if you swing this board around, you can zoom in there, you can see a couple of unpopulated, uh, footprints up on that, uh top board there and there.

**Dave Jones:** So, I'm not sure what's uh going on there. They've obviously left out a few parts after they've designed it. Your guess is as good as mine. And uh this doesn't look to be easy to get apart at all.

**Dave Jones:** It looks like uh you really do have to get that lens off to pop this board off and then separate these two. I mean, I am able to wiggle that.

**Dave Jones:** I'm not sure if you can see right down in there, but maybe not. But, um you can see the main chip in there, and there's a dob of uh heatsink compound on top of it, which uh thermally bonds that through to the main aluminum block going right through there like that.

**Dave Jones:** So, the main processor is under there somewhere. But, can I get to it? Uh I don't know. So, there you go. You can actually see the dob of Excuse the overexposure on the external parts.

**Dave Jones:** I'm trying to get a look under, but you can see that big dollop of uh heatsink compound. There's another chip down in there as well. A second one right there.

**Dave Jones:** You can see the uh heatsink compound on that one as well. So, there's two main two main chips down in there that are heatsunk. And there we have it, folks.

**Dave Jones:** I've very bravely uh removed the uh lens there. And uh I don't I do want this thing to be operational afterwards, so I don't really want to uh uh try You know, I don't want to get uh dust and other crap in here.

**Dave Jones:** But, there's the bare sensor mounted on the board there. So, the lens goes directly over that, and we have a GoPro branded device there and another one to try and take a look at, and you can see the lens assembly down the bottom there like that.

**Dave Jones:** And there's the GoPro sensor up close. It's sort of like an LCC package sort of uh directly reflow soldered onto that board there. And lots of exposed uh gold as well.

**Dave Jones:** That heat That's all uh grounded and that uh helps the uh heat sinking performance as well. So, we have a GoPro branded device. I'm not sure. I'd have to uh clean off all the gunk there all the heat sink compound to see exactly what that is.

**Dave Jones:** And they've got two uh watch can crystals there, which is really uh interesting, sort of hand soldered and folded back down there. I don't know why they've gone for that instead of a uh surface mount option.

**Dave Jones:** I don't know what's going on there at all. And we've probably got some more uh power supply stuff up there, probably for the internal uh core voltages and things like that.

**Dave Jones:** So, that is pretty much the guts of the GoPro right there. And I may have found the temperature sensor there. It almost looks like a dead giveaway. Two-leaded device, bit of uh Mylar or some other tape, and it's wedged under the heat sink there.

**Dave Jones:** Dead giveaway. And I love the look of the lens. That's really quite nice and it just drops into that uh part of the machine aluminum block. Lovely. And here you can see the uh surface mount speaker.

**Dave Jones:** You can see the port on the right-hand side there. That uh goes through a hole in the side in the bottom of the case. And it wasn't hard to find out that that GoPro branded uh chip in there.

**Dave Jones:** Look, they've even got the slogan on there, "Be a hero." is um from a company called uh Ambarella, and it's the uh A5S uh system on chip uh processor, and it's the encoder and the the uh works.

**Dave Jones:** It's basically a uh complete solution. Um And we've got the memory next to it over there and yeah, really GoPro have you know whacked on the a good lens onto this thing, the novel all of the novel packaging and stuff like that and the firmware and uh it's good to go.

**Dave Jones:** No pun intended. And here we go. Let's take a look at the data sheet for this Ambarella A5S. It's a hybrid DV camera system on chip or SOC. It's a single chip H.264 codec solution for high definition hybrid DV cameras leveraging Ambarella's leadership in professional encoding and low power DSP technology.

**Dave Jones:** The A5S provides a unique combination of high quality digital still image processing combined with full HD video processing. Woo. There you go. Um no compromise blah blah blah blah blah.

**Dave Jones:** And here's the stuff we're interested in. A5S H.264 codec integrates an image sensor pipeline capable of processing 240 megapixels per second, 1080p 30 frames per second H.264 video codec and a 528 megahertz ARM 11 processor.

**Dave Jones:** Um and yeah, you can get a full hardware reference design, software developers kit and all that sort of stuff with it. So there you go. Here's all the specs, high ISO and blah blah blah blah blah, 3D noise reduction as well, motion compensated stuff and advanced rolling shutter compensation.

**Dave Jones:** As you can see, it's got pretty much everything. I mean it does simultaneous LCD and HDMI output if you had the LCD backpack, it could do both at once, on screen display readout, touch screen support if you had a touch screen on this thing.

**Dave Jones:** It also supports on chip editing and wireless as well. For this Hero 2, you had to get the wireless backpack separately, but the new Hero 3 has the wireless built in.

**Dave Jones:** Ultra ultra compact bomb bill of materials. It's all important um as you see, but there were a lot of uh support passive uh components, of course. But, in terms of external chips, you saw it.

**Dave Jones:** It was just this main one system on chip, the A5S, and two memory chips, and uh that was basically it. And uh it claims less than 500 mW um including the DDR memory as well.

**Dave Jones:** So, that's pretty impressive. And here's the uh block diagram for the thing. And as you can see, it's uh it's got pretty much everything um embedded into there. It's got uh len- you know, it's got the uh direct um sensor input from the lens, of course.

**Dave Jones:** It's got regular GPIOs. It does um I2S uh audio codec, DDR memory interface, NAND flash memory interface. It's got a couple of UARTs if you want to use those.

**Dave Jones:** It's maybe for uh debugging during um system uh testing or, you know, or development or uh something like that. It's got a USB uh host interface, of course. The JTAG, of course, that's how you program and uh uh test the thing.

**Dave Jones:** And um it's got a wireless output, SD card, or building LCD, HDMI, blah blah blah. It's got the real-time clock building, and uh the image DSP sensor pipeline and scaling, and then the H.264 um encoding as well with dual stream uh rate control.

**Dave Jones:** Fantastic. There's a lot of functionality um built into this thing. It's, you know, it's absolutely massive. So, um yeah, if you want more details, um check out the Well, I presume Well, you probably can't get the data sheet, actually.

**Dave Jones:** You've probably, you know, got to sign an NDA or something like that to get the data sheet. And there you go, it's in the package is a 404-pin BGA, 15 by 15 mm uh designed to operate to uh 70° and it is uh manufactured using the 45-nm process.

**Dave Jones:** And you can clearly see the uh heat sink going right through this thing. So, they've really done an impressive systems engineering job and 3D envelope packaging for this thing.

**Dave Jones:** I really like it. They've done a really great job. So, there you go. As expected, there's not, you know, a huge amount in this thing. I mean, you know, there's a main processor with some memory and that pretty much handles everything.

**Dave Jones:** But, you know, it was really quite nice in terms of construction, how they've used these tabs to go to get the power between boards, and how they've jammed it all in there, and how they're able to get the thermal performance inside this thing.

**Dave Jones:** So, really is quite clever, and it's its performance is really quite phenomenal. And of course, this thing is super rugged as well in terms of the packaging. It's, you know, it's built built like the proverbial brick dunny when it's fully assembled and packaged.

**Dave Jones:** Because this thing is like survived, you know, three, four drops from airplanes and stuff like that. It's it's quite famous for being a very survival device. So, there you go.

**Dave Jones:** I hope you enjoyed that teardown of the GoPro Hero 2. I thought it was rather interesting. So, if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** And don't forget, if you like teardown Tuesday, please give it a big thumbs up. Catch you next time. Damn, now I've got to put this bloody thing back together.

**Dave Jones:** This thing has to go on the Canyon Copter. Oh.
