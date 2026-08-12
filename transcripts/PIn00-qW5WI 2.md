---
video_id: PIn00-qW5WI
title: EEVblog #637 - Omni Directional Laser Barcode Scanner Teardown
url: https://www.youtube.com/watch?v=PIn00-qW5WI
source: youtube-asr
timestamps: {"0": 0, "1": 34, "2": 69, "3": 98, "4": 131, "5": 145, "6": 173, "7": 203, "8": 234, "9": 260, "10": 289, "11": 311, "12": 328, "13": 358, "14": 393, "15": 425, "16": 438, "17": 469, "18": 486, "19": 515, "20": 532, "21": 544, "22": 574, "23": 594, "24": 612, "25": 629, "26": 662, "27": 688, "28": 706, "29": 747, "30": 774, "31": 807, "32": 828, "33": 846, "34": 868, "35": 899, "36": 925, "37": 960, "38": 974, "39": 1009, "40": 1028, "41": 1044, "42": 1073, "43": 1102, "44": 1127, "45": 1159, "46": 1193, "47": 1217, "48": 1237, "49": 1276, "50": 1306, "51": 1333, "52": 1365, "53": 1405, "54": 1424, "55": 1443, "56": 1461, "57": 1482, "58": 1499}
---

**Dave Jones:** Hi. Welcome to Teardown Tuesday. Today we're going to take a look at one of these omnidirectional barcode scanners that you've no doubt seen and used at your local supermarket checkout or something like that where you just wave the product in front of it and it scans the barcode at almost any angle. So, you can probably see sort of stuff rotating in there and puts like a laser pattern and it can read the barcode in any direction. So, what's inside one of these things? Well, let's find out. Now, this is a Symbol

**Dave Jones:** brand one. They used to be a real top-notch, but they got bought out or acquired by Motorola or something like that. So, this one is still available. This model is the LS 9208, but it's available as still the 9208, but under the Motorola brand. So, I'm not sure if it's if it's exactly the same. So, although it's 1996 vintage, it's was pretty much state-of-the-art at its time in terms of omnidirectional uh barcode scanners. So, it should be fairly representative of the technology. Now, you're probably familiar with these uh

**Dave Jones:** USB line scanner ones. You can pick these up on eBay for like 20 bucks or something. They're super duper cheap. And basically by line scanner, it's pretty much you can see the laser there. It just does a single line. So, if you go like that, boom, it it just reads sort of these one-dimensional or line-based barcodes. But, these ones are omnidirectional. Let's take a look at the pattern in this one. Now, it's actually quite hard to get the pattern of this one on camera because it's not

**Dave Jones:** uh very bright at all, but you can see that it pretty much has multiple scanning lines. It's still a line-based system, so to speak, but it has multiple lines in all these different axes like this going. So, one's going down like that, one's going down like that, and then scanning across like that, and then one scanning up and down like that, and across and across in all those different angles, so it can pick up the barcode in pretty much any orientation. So, no matter how you wipe the product in front

**Dave Jones:** of the scanner, it's going to pick it up. So, with your traditional line scanner like this, you have to bring it down and then over the code like that. If you bring it down, of course, in that direction, it's just not going to read it at all cuz it can't read the pattern.

**Dave Jones:** But, with these omnidirectional ones, you can read them in pretty much any orientation. Can bring it down Bring it in like that. Bring it down like that. Even on a really small angle like that. That is a ridiculously shallow angle, and it's still reading that. Now, there's no barcode on the back there. It's actually reading that, and you can come in at an angle like that, and it gets it. So, you can just pretty much just wipe the thing in front of it, and you used to doing that

**Dave Jones:** at your checkout. And it's that omnidirectional scan line pattern that makes it do that. And similar to these uh USB-based ones, which just basically simulate a USB keyboard. So, it's just like you're typing these symbols in. Your software doesn't know any difference. You don't need any fancy drivers or something like that. This one is what's called a keyboard wedge device. I mean, it wedges in between or in series with your in this case an old-style uh PS/2 keyboard. And of course, here's the uh power coming in

**Dave Jones:** from the um external uh power plug pack for this thing. And it just simulates the key presses. Uh you know, so it basically can work with any software or any point of uh sale system. But, on top of this keyboard wedge option, uh you can also get a USB option as well, and an serial RS-232 and some sort of custom IBM uh protocol interface. And I believe all the hardware's built in here. You just require a different cable. Look, it's got like an RJ45 plug on here, but

**Dave Jones:** I only have the cable supplied for the keyboard wedge here, but you can actually scan in different barcodes. This is what they give you in the manual here, and you can actually configure the device after you powered it up by oops, actually scanning the particular barcode you need and setting it up that way. It's quite a clever way to do it. So, I can configure all sorts of stuff like this from the manual by just scanning in the particular type.

**Dave Jones:** So, it's going to be interesting to take a look inside this thing, and we're obviously going to have motors and mirrors spinning around and all sorts of jazz to to make those multiple lines. So, according to the specs, it's got five different scan angles and four lines per scan angle at a 4 Hz raster rate. So, it can scan those at four times per second in those angles. So, let's take a look at it. All right, let's crack this thing open. There were just two screws down in

**Dave Jones:** there, and presumably, yeah, it's just going to pop up. Something's fallen out. That's the RJ 45 jack connected via a little flat flex ribbon, but there we go. We're in like Flynn. Look at that. Straight in, and doesn't that look gorgeous? That looks like a gold reflective mirror in there.

**Dave Jones:** Ah, beautiful. Now, without even powering it up and seeing it in operation, it's fairly obvious how this works here. Here's our laser diode here mounted in this big diecast alloy bracket here. Probably got some heat sinking happening on there.

**Dave Jones:** I'm not sure of the output power of the uh laser diode. What is it? 1 mW or something like that? And the manual says this is a class one laser diode, which is what you'd expect. It means it's basically safe in all modes of operation pretty much, which it would have to be, you know, being at a consumer checkout point here, but basically they've got the laser diode mounted in here and it's a long way reflected off this Look, you can see it shooting out there like that,

**Dave Jones:** reflecting off that inner spot right in there and then that just bounces around then that bounces off this mirror down in here like this and then it bounces off the five different segments that we've got. 1 2 3 4 5. So, there's our five segments. So, if our laser diode here is fixed, it's shock mounted. Check it out. It's actually the whole Well, the whole arrangement is shock mounted. So, you know, when you throw products down on the bench or something like on the counter top, it

**Dave Jones:** the vibration doesn't come through to the scanning optics in there. Which, you know, is a big deal when you're using it in a consumer point of view. You know, vibrations can easily go through this bench. If I sort of throw something down on this bench next to it, all that vibration and shock is going to come through into the electronics. So, they've got those nicely decoupled in there by way of these shock mounts there, there, and there, and there, the entire system. So, we've got ourselves a fixed laser diode module

**Dave Jones:** here. Screw adjust there so they they can tweak the angle on this thing after they've actually produced it. Then all of our scanning is done by this mirror down in there and you can Yeah, I can move that by hand. Oh, look at that.

**Dave Jones:** It's a prism. Look at that. That's terrific. Wow, look at the sharp point on that. So, obviously it's all in the timing, of course. So, the optic output from the sensor would have to Well, it's timed with the mirror like this to actually get the reflected image back in there from each particular angle and then it's scanning that. So, we can actually power that up and watch this thing spin around. That'll be terrific.

**Dave Jones:** Woohoo! Love it. So, they don't really have anything fancy. That's a neat way to get all of these different scanning modes, as you can see, five different angles with five lines per mode on this thing. So, it really is rather amazing.

**Dave Jones:** And there's our photodiode sensor down in there, and it's got a shroud on top. We can probably Yeah, we can peel that off. There's no part number or anything like that in there, but there you go. And that is There's nothing fancy going on there at all, but you can see that there is some extra filtering going on in that thing. Here we go. I'm going to power it up and uh Oh, there we go.

**Dave Jones:** There we go. Our mirror's scanning down in there. And yeah, you can see some of the Yeah, you can see the laser shining off there like that. Beautiful. This mirror up here, I can If I put my finger on that, I can actually feel that. I'll get in there with my macro lens and see if you can see that move. And there you go.

**Dave Jones:** Hopefully, you can see that mirror. Bit of shimmy in that mirror. If I turn it off, there we go, and I'll apply power.

**Dave Jones:** And it's starting up. There it goes. Just the tiniest little amount of wobble in that mirror. So, I'm not sure how they're coupling that through. There doesn't seem to be a motor there. They might be getting some sort of vibration through from the other one in some sort of clever way. Hmm. So, I'll show you what happens with the scanning pattern if I actually stop this mirror up here with my finger from vibrating. So, let me see if I can get that pattern. So, that's normal.

**Dave Jones:** And let me put my finger on the top of that. Here we go. You can see I can physically stop that from scanning across in that direction like that. So, the you can see the spec is correct, right?

**Dave Jones:** We've got five different angles there with four lines per angle, and that it's a scan at a rate of four times per second, and that's about what it looks like. So, yep, the spec confirmed. And that prism down in there, it's got four sides on it, but they're not identical.

**Dave Jones:** They're all angled slightly differently, even though you probably can't see it. And that's how you get your four different scan lines that you get in the spec. So, you know, they might have a lesser model that might only have three scan lines, for example. Well, that one won't be a square, it'll be a triangle.

**Dave Jones:** And I would love to be able to show you how the angled mirror in there the rotating prism, the the four-sided angled plates actually give you different scan lines, but unfortunately, if I stop that motor, then it actually just switches off the laser. So, it obviously senses that there's an issue and and switches it off. So, unfortunately, unless I bypass it, jerry-rig it somehow, then no, it's not going to work. And I can show you that by sort of slowing it down a bit.

**Dave Jones:** Here we go, maybe. Let's have a look. Whoop, there we go. I just switched the laser off. Switched it back on. There we go. Nah. But it's certainly fun to just apply your finger on the top vibrating mirror there, and I can just get that and I can just scan that manually slowly like that. That's rather neat.

**Dave Jones:** But those four lines there, 1 2 3 4 uh determined by the four different uh angled surfaces on that rotating prism. Now, what I'm going to do is I'm going to test if this laser diode here actually has any functionality as part of the scanning process. So, here we go.

**Dave Jones:** I've got my uh barcode on here and I'm just going to scan that in. There we go. Okay. No problem whatsoever. And I'm going to block off my laser diode with my pointer here and look at that. No, it clearly can't read that barcode. And no matter how many times I do that, I cannot get it to even beep or scan that thing once. So, obviously, the laser diode is a very critical part of the illumination mechanism for illuminating the barcode so that this thing can pick it up. And

**Dave Jones:** probably no wonder. I mean, I'm a little bit surprised by that, actually. I thought uh you know, it may have actually still been able to read the barcode using ambient light or something, but clearly what's happening is that the laser is scanning across the barcode like that, and then they're filtering that and with the uh lens on the front and they're then getting the difference between the dark uh i.e. it's going to reflect off the white surface and it's not going to reflect off the dark surface. So, that's how they can

**Dave Jones:** get the ones and the zeros and identify the uh barcode on that particular thing. So, there you go. That laser diode and the vibrating and the scanning and all the different angles, that's a critical part of the illumination of this barcode. It simply does not work without it. Doesn't work with just ambient light. So, that's the answer in there. I mean, you probably could tweak it to get it to work under ambient light conditions, but it's obviously much more reliable uh to get the contrast required by uh

**Dave Jones:** lighting it up with a laser diode like that. Okay, let's try that again but in dark. It's not completely dark here in the lab. You can see the grain on the camera image. It's really gained up on my camera, but it is pretty dark in here. So, let's see. Yep. No problem whatsoever.

**Dave Jones:** There you go. And if I make it even darker, I'm I'm putting my jumper over the top of this whole thing. So, it is pretty pitch black in there and no problem whatsoever. So, that illumination system works fantastic. And likewise in bright conditions, give it a test. Here we go.

**Dave Jones:** I'm going to shine my torch onto this thing. So, I'm really overexposing that. And yep, okay, you can still read that even under really bright light conditions. All right, what I really want to see is how they're vibrating this top mirror up here. So, um let's try and get this whole Hey, hey, hey.

**Dave Jones:** Thanks. Yeah, look at that. Just comes out as one big thing. We've got some soft padding in the back there. And aha, there you go. Electromechanical vibrator in there and that's just transferring that through to the top there. There we go. That's what I couldn't see before. There was that bar Well, I could kind of see a bar going down, but I thought it might have been maybe tied to the other motor or something. But no, there you go. It's got its own little uh little vibration coil there and uh a

**Dave Jones:** couple of more little uh shock mount things there and that's about all she wrote. And there's a little uh DC motor in there. And yeah, that's not just, you know, they're not just ramping that up. They're uh controlling the speed and getting uh probably getting the timing from that thing as well. And this flap they've got on here, this is obviously just to stop ambient light coming in swapping the sensor from the front there. So, you really only want the image reflected off that mirror at the

**Dave Jones:** back. And we haven't got a huge amount of chips here on our board, but let's go in there and take a look at what we have. Bam! Bam! Bedrock two chipset presumably pebbles. There you go. So, they're a fan of the Flintstones. So, I don't know. We'd have to look up a number on that, but could be one of the custom devices for particularly for decoding the sensor and getting the barcodes out. Obviously doing some sort of heavy custom processing there. No, unfortunately I can't find any info on that at all at a

**Dave Jones:** first glance. All I get is like a whole bunch of broker websites which may possibly have it, but no data sheet or any info like that. So, if you do have any info, please leave it in the comments.

**Dave Jones:** Main processor down in there Hitachi H8S old school. And likewise that one STI branded again, but I doesn't bring up anything at all. Can't find anything on the search there. So, I don't know. Not a huge amount of IO on that thing. Lot of power and decoupling there. I don't know. Is it some sort of serializer or something like that? I don't know. I'm just completely guessing. No idea, but obviously designed to match this STI chip over here. And nothing special down in there. We've just got a 74 series 240

**Dave Jones:** logic from TI. There's our crystal oscillator. Another one under here. That has a firmware uh label on it. So, presumably a programmable device. Let's take a look at that one, too. Look at that. We've got ourselves an old Atmel AT91FR4042.

**Dave Jones:** That's an ARM 7 thumb processor. That was pretty decent and grunty you know, back in the day 1996 when this thing was done. So, uh there we go. It was manufactured the 53rd week uh 05 there. So, there you go.

**Dave Jones:** That's obviously doing the heavy lifting. So, uh sort of like the image uh processing and stuff like that. So, maybe this uh chipset, this custom uh you know, Flintstones chipset in here is, you know, probably just doing some sort of uh decoding or something like that. But, probably a lot of the decoding in real time done inside that Atmel ARM processor. It makes sense cuz you've got to do a lot of processing here, especially like the five different angles all in real time, four times per

**Dave Jones:** second, scanning that image. So, So, this could be some sort of like a contrast image uh recognition, which like converts it into a more usable form, like uh filtered format that the Atmel processor can then uh process in real time and try and get a barcode out of it. Cuz you can program in, like it's not just searching for one barcode, as well as all the different types. You can actually program this with the uh software. You can hook it up to a PC. It comes with software and tell it to read,

**Dave Jones:** you know, 50 different types of barcode. So, if you enable all of them to be scanned, then this thing is got to do a lot of work. I mean, I don't envy that thing having to, you know, process all the different angles and do all that and search for all the different types of barcodes. It's crazy. So, no wonder they had to put an ARM processor in this thing. This uh one over here, of course, the Hitachi H8 H8S, that's just, you know, they're probably just doing some interfacing,

**Dave Jones:** all that uh protocol um uh stuff, the uh US cuz this has presumably a USB uh interface. So, it'd just be doing like the interface work pretty much with uh the RJ45 here. Cuz, you know, you don't want to do that in your ARM uh processor here. Just offload all that uh interfacing uh protocol stuff over to here. But, uh image processing there, and protocols. So, that's nicely segregated. I don't mind that at all. And on the back of the board here, there's a fair bit of

**Dave Jones:** passive uh work going on, but no sort of uh heavy-duty processing at all. But, this is interesting how they've added this uh flat flex copper shield over here and soldered that on to part of the tab. So, they obviously needed some extra shielding on that. So, that's clearly some sort of afterthought there, I think. Maybe pass uh EMC compliance and uh oops, let's just uh whack that across there. There's not a huge amount happening here. There's a classic LM358 op-amp, and we've got some 74 series

**Dave Jones:** logic HC4066 there. Uh absolute classic, and uh what's that little puppy? That eight-pin uh SO package next to it. Hmm. But, that there's all part of the uh laser drive circuitry there, cuz there's the laser connector on it, and uh this is all uh motor drive stuff over here. Here it is.

**Dave Jones:** So, this is all uh motor stuff around here, and uh that's about all she wrote, really. Now, that right there is a fascinating package. Look at that. Can anyone tell me what that is? Look at that. Some sort of optocoupler, perhaps, with a split going right through it.

**Dave Jones:** That is very And then, potted, like you know, two different halves potted. That is a fascinating package. Anyone? Now, look at that. I do believe there's another filter on the entry, and that doesn't surprise me at all, really, cuz you've got to get that contrast. You have to get that contrast with the uh laser diode against the bright and the dark patches on the barcode. You can see how this is clearly like an afterthought. I mean, they've even put the product barcode on the bottom here and then they've just tacked

**Dave Jones:** this on to you know, to put a bit more shielding or maybe they forgot the ground between there and there or something like that and they're joining them together and that was a way to do it, but there we go. We can get a real good look at that rotating mirror in there, the rotating prism and it looks to be a slight curvature or is that my imagination? No, no, that could be an optical illusion that there's a slight curvature on that thing. I think it is

**Dave Jones:** actually a flat surface and that is really jazzy. I like that. Woohoo! Sex on a stick. And there's the prism in there and you can probably just see how that some sides are angled slightly different than the other like that one is greater than that one there. A bit hard to see, but yeah, there's just a mild angle difference in those.

**Dave Jones:** And you'll notice that the top of the prism here has this reflective, there it is, it's reflective. We can see ourselves in there. Hello, there I am. And so it's got this reflective square with something in the corner here. I don't know if it's It doesn't appear to be a magnet or anything like that, but clearly they're doing this and the rest of it is matte black. So obviously they're getting some sort of optical thing happening there. They need that surface reflective so that they can get

**Dave Jones:** the positional rotation of this thing. So that's got to be what this mysterious device is doing here. It's obviously detecting the positional, because this is the bottom side of the board, so it's detecting the rotational position of that mirror on there as it goes around. So, how is it exactly doing that? Not 100% sure, but my best guess would be that that is maybe a UV LED there and then reflecting off into a photo diode here so that when the reflective surface comes around, boom, it bounces off and it knows the position

**Dave Jones:** of or at least the start position of that mirror and then you can calibrate that in software, of course. probably what's going on there. So, I'd love to get a little data sheet for that thing, but that seems like the most obvious thing that's happening. And if we probe our motor here, this is our for that prism. There we go.

**Dave Jones:** We're getting about 140 7 hertz or thereabouts. Little bit of jitter on that. You can see as you'd expect. In fact, I can probably get the histogram data up on that. There we go. We're getting a standard deviation there of 600 millihertz or thereabouts.

**Dave Jones:** So, there you go. That's the clock driving the rotating prism. And that's the drive signal for that top coil on the top mirror that vibrates, that has that vibrating shaft going up to it. And that's about 33.7 hertz or thereabouts.

**Dave Jones:** So, there you go. I hope you found that teardown interesting of this omnidirectional scanner. And unfortunately, we can't go huge amount further, I don't think, without any data on that Flintstones chip set exactly what it's doing in there. So, if anyone's got any data on these things, then please leave it in the comments. But there you go.

**Dave Jones:** That's how one of these omnidirectional barcode scanners work. And they're quite neat. There's a whole bunch of you know, laser optics and mirror optics and stuff going on there and lots of data processing and filtering and things like that together.

**Dave Jones:** Rather clever solution to scanning those barcodes in pretty much any orientation. I love it. Woohoo! vibrate Oh, I can play with this all day long. Catch you next time.
