---
video_id: 6lBU4NwmY7s
title: EEVblog 1717 - Rigol's INSANE New $999 350MHz Oscilloscope: TEARDOWN
url: https://www.youtube.com/watch?v=6lBU4NwmY7s
source: youtube-asr
timestamps: {"0": 0, "1": 41, "2": 65, "3": 103, "4": 146, "5": 179, "6": 211, "7": 236, "8": 262, "9": 279, "10": 297, "11": 327, "12": 356, "13": 375, "14": 401, "15": 433, "16": 463, "17": 492, "18": 510, "19": 546, "20": 579, "21": 614, "22": 640, "23": 671, "24": 688, "25": 708, "26": 726, "27": 743, "28": 779, "29": 808, "30": 840, "31": 867, "32": 886, "33": 916, "34": 934, "35": 960, "36": 989, "37": 1023, "38": 1056, "39": 1073, "40": 1097, "41": 1111, "42": 1146, "43": 1163, "44": 1189, "45": 1218, "46": 1243, "47": 1272, "48": 1291, "49": 1317, "50": 1331, "51": 1366, "52": 1377, "53": 1403, "54": 1429, "55": 1457, "56": 1481, "57": 1498, "58": 1522, "59": 1534, "60": 1551, "61": 1579, "62": 1599, "63": 1639, "64": 1667, "65": 1686, "66": 1720, "67": 1758, "68": 1784, "69": 1815, "70": 1841, "71": 1881, "72": 1909, "73": 1924, "74": 1955, "75": 1985, "76": 2014, "77": 2037, "78": 2063, "79": 2083, "80": 2116, "81": 2146, "82": 2162, "83": 2187, "84": 2203, "85": 2235, "86": 2249, "87": 2283, "88": 2322, "89": 2348, "90": 2365, "91": 2381, "92": 2395, "93": 2409, "94": 2419, "95": 2436}
---

**Dave Jones:** HI, CHECK IT OUT. WE'VE GOT A BRAND NEW release Rigol oscilloscope. Look at the bling. Look at the shiny bling. This is the new MHO900 series. Oh, this is the actually the special release 1 GHz MHO98. And this is a special limited edition jobby with transparent back. Look at that. And they're only making 2,000 of these particular ones. And this special edition has gold plated connectors and metal knobs. Oh, [screaming] I pity the fool that doesn't have a blinged out oscilloscope.

**Dave Jones:** >> [laughter] >> Look at this. They really went to town. Look at this limited edition beta 07. Is mine serial number seven? Maybe. I don't know, but I heard they were going to only manufacture 2,000 of this particular model, the 1 GHz version with the gold plated connectors, the metal knobs, and the transparent backing. Oh.

**Dave Jones:** >> [laughter] >> Come on. Now, do not confuse the new MHO900 series with the DHO900 series. It's D instead of M like this. Yes, I know that the DHO900, this is the 800. Sorry, I don't physically have a 900 here. But the 900 series which starts at 560 Yankee bucks, that actually does have mixed signal capability. So, I don't know why they've called them MHO, but anyway, don't confuse MHO900 with DHO 900. Got it? As you can see, it's exactly the same size, pretty much exactly the same weight,

**Dave Jones:** uses the same moldings as and everything as the 800 900 series before it. Looks yeah, looks pretty identical. So, they're just reusing those. That makes sense, but this has more Whoop, survived a drop test there, did it? Yes, it did. Oops. Anyway, the new MHO900 series starts at 999 Yankee bucks. And that's for the 350 MHz version. So, the run to the litter, the the bottom end of this series starts at 350 MHz. And there's 500 MHz, 800 MHz, and the MHO900 limited edition here is the 1 GHz version. But

**Dave Jones:** they might eventually sell those out. So, you might be limited to the 800. So, for under 1,000 Yankee bucks, you can now get a 350 MHz four channel oscilloscope at with four gig samples per second compared to the older DHO900 and 800 series are only 1.25 gig samples per second. This new one is now four gig samples per second. And it's got 500 meg memory or maximum as opposed to 50 meg of memory in the previous one. And it's got dual signal generator capability.

**Dave Jones:** And as with the previous series, it's got the VESA mount, of course, and the HDMI out as standard, USB-C powered. So, this is crazy. Is there another 350 MHz four channel scope on the market for 999 bucks? I don't think so. As I predicted previously, they were leveraging all their custom ASIC technology. They've got custom ASIC front ends. They've got So, they can just push the price down in this lower end market. Unbelievable. So, if you're talking entry level scopes with 350 MHz bandwidth and uh sample

**Dave Jones:** rate like this one, the next nearest equivalent seems to be like if you take Siglent for example, the biggest competitor to Rigol, obviously make great scopes. But their closest 350 MHz bandwidth scope is $2,700. This is 999 bucks. This has double the maximum sample rate four gig samples per second as opposed to two gig samples per second.

**Dave Jones:** Wow. And of course, it goes without saying it's 12 bits. None of that eight bit rubbish anymore. And by the way, if you don't know how small these things are, look at it compared to the size of my hand. It is like when you first see these things I do not have a big hand. I've got quite a small hand. And well, look at the like they're just amazingly small. They take up bugger all bench space. Or with the VESA mount, you can just mount on on a

**Dave Jones:** tilt swivel arm somewhere. But of course, you don't get everything for nix. If you want that dual channel 100 MHz generator, that's 700 bucks option. If you want 50 megs, 419. If you want to upgrade from 350 MHz to 500 MHz, it's 279. To get to 800 meg, it's 419 bucks.

**Dave Jones:** And if you want the 500 point memory suite, 279 bucks extra. Yeah, it's probably hackable though. Most Rigol scopes are. Well, you know what we say here on the EEVblog, don't turn it on. Take it apart. Yes, I literally have not powered this thing up yet. Fresh out of the box.

**Dave Jones:** Let's go. And by the way, they've got the exact same flippy out feet which are really nice and like they are quite nice, very stable. It doesn't matter even if you have these not out like that. You can actually poke the buttons without it falling over even without the feet. There you go. That's inside. Large single board construction as you'd expect. The heat sink is massive. Look at this. I really like the molding on that heat sink. The fan's a lot bigger like the old DHO 800, it just had a tiny

**Dave Jones:** little fan like that. This one's bigger, but it's got the same fin arrangement like this which sucks the air through the fins like that. It's a very efficient and that's how they get the tiny slim form factor. And they've even got that going over the gen board. Look at that. That's clearly the arb gen board given the relays. And it's got dual 100 MHz arb gen. So, they need to take that seriously. So, it looks like they've put that on its own dedicated board. Nice. Oh, look. I kept the

**Dave Jones:** sticker intact. I get to keep my warranty. Not sure what happened to that screw, but they went ah, bugger it. Don't need to put that in and we don't need to make the stand off to match. So, it's not really flapping around in the breeze, but yeah, they obviously meant to put it in there at the design stage, but then didn't finish it off come production.

**Dave Jones:** Okay. We've got the heat sink off. The fan is still connected to the heat sink. And oh oh, the metal cans are practically falling off. Oh, beautiful. And oh, there we go. We've got the silk pads on the bottom there. One of them tore on the that looks like the main acquisition ASIC there, but they're not They're supposed to be soldered.

**Dave Jones:** But they're not. Look, they're solder tabs. Maybe they did this deliberately for me so I could get it off so I could have a look. So, we'll disconnect that. So, yeah. That's a beautiful machined heat sink. I'm really liking really liking that. And look, you can actually see the the front end ASIC chip through a cutout in there. Is it for just for aesthetics to show off, hey, look, we can design our own front end one gig ASIC.

**Dave Jones:** There's your dual 100 MHz arb gen. Look at that. What What is that bad boy there? I'll have to get that. And is it a custom ASIC or is it What is it a little FPGA or something? I don't know. Can't read it on my camcorder screen. But check out the back of that. Wow, look at that. That's some serious That's some serious density there. There's our two 50 ohm outputs there and 200 ohms in parallel. But of course, if you buy the entry model unit,

**Dave Jones:** it does come fitted with this board, but you have to buy the arb gen as a software upgrade unfortunately. Or maybe you could sail the high seas perhaps. There you go. We've got dual connectors. That's one little tiny one up the top for that arb module. That's why that wasn't flapping around in the breeze. But they need to extend spacer up and put a screw in it. I mean, you know, vibration and all. I mean, there's a lot of pins on there, but still you could come a gutser on that.

**Dave Jones:** Oh, those cutouts are obviously to get the heat sink contact on the main heat sink. You know, it's 1 gig bandwidth front end. You're going to have to get some thermals out of that. And check it out. There is the front end. As always, high res photos will be available on eevblog.com.

**Dave Jones:** And that chipset, that's a Rigol custom ASIC solution 1 GHz bandwidth front end. We've seen this exact chip in the much vastly more expensive first saw it in the DHO4000 series teardown. I'll link in that video as well if you haven't seen it. Exactly the same chip as I predicted has flowed down to this under $1,000 model. This is crazy. And I assume this is the same chip that's also used in the the lower models 350 to 800 because you can software upgrade from 350 to 800,

**Dave Jones:** but I'm assuming you can prob This one's probably also software upgradeable to 1 gig. It's just a more maybe they've tweaked a couple of components on there or something like that. That could certainly be the case for this limited edition model. But the regular one almost certainly contains the same front end ASIC chip because once you've developed that, you can mass produce them for almost peanuts. Once you're absorbed that NRE cost, non-recurring engineering cost of actually designing and masking the thing, then yeah, yeah, the price

**Dave Jones:** point becomes crazy. That's why no one else can match Rigol for this bandwidth for the money. And the two ADCs, so yes, we're going to multiplex. So, the four gig samples per second will go down to two gig samples per second. And it's not divided by four. So, that's a huge bonus, especially for a sub $1,000 scope. Crazy. Anyway, um yes, this is the same Once again, Rigol custom ADC here. This is the 12-bit jobbie. Uh four gig samples per second as used in the 4000

**Dave Jones:** series scope. Exactly the same chip that just flows down to these lower models. Unbelievable. Sorry, did I say DHO 4000 before? It's the HDO 4000 model. Anyway, this is interesting. We didn't see this before. It was an Artex 7. That's the acquisition engine here. But looks like they spun another custom ASIC. This is the RT 6881.

**Dave Jones:** I don't think I've seen that elsewhere. I don't know. Too many Rigol nouns. But yeah, so no longer using the Artex 7. Once again, this is how they're getting the price point down cuz those Artex 7 FPGAs, they are not cheap. And they're probably like the most expensive chip in the whole thing. So, they've gotten rid of that by spinning their own custom ASIC again. But that's not what runs the OS. That's over here on this rock chip jobbie. Seeing these more and more and that's a basically a

**Dave Jones:** processor and that's running all the GUI user interface and everything else. But this is the sampling acquisition ASIC here which talks to your memory. So, there's your 500 meg points. Yes, every scope, even the $999 one, comes fully populated with the 500 meg sample.

**Dave Jones:** There's probably more chips on the bottom as well. The 500 meg points of memory at 12 bits, by the way. Not eight-bit rubbish. And anyway, the rest of it not very exciting. You can have a look at the teardown photos of and if you want the USB-C input there. I've had I've heard of no reports where people have like broken those off or anything.

**Dave Jones:** They might even have Do they have a strain relief thing in the back? I'm not sure. And people have done like 3D printed like add-ons for these with like external battery packs and stuff like that. There's our logic analyzer input there. And well, yeah, there's not much else, really.

**Dave Jones:** But look how simplistic the one gig front end is. There's going to be a few more components on the bottom. But yeah, that's a complete one gig bandwidth front end. They just whack four of them in a $999 retail scope.

**Dave Jones:** Unbelievable. When I was a boy, jeez, 20 megahertz dual channel. Hello, you sneaky little bugger. They had some tape over that. There's our SD card, micro SD, containing the OS on this thing. What size is that? Get out of it. That's a Lexar 32 gig jobbie. There you go. So, if you want to experiment with this thing, you don't have to like dick around like reflashing the thing or anything. You can just like plug in an external card and experiment to your heart's content. Looks like there's some

**Dave Jones:** JTAG-y interfaces there. Maybe a serial boot interface as well. Wowza. Look at this. I got the main board out. I don't think the 800 series was like this, was it? You don't have to dick around. This is like beautiful. You don't have to dick around from like a production servicing point of view and assembly point of view. You don't have to dick around with trying to like put the board in and then tuck the cable in under there with minimum length and everything. They're using to board inner connect here which

**Dave Jones:** connects over here and everything's just It's It's just beautiful. The attention to detail that they've put into the just the manufacturing and assembly of this thing is absolutely fantastic. I love it. Wow, hats off. And just small details like that little alignment post there, right? Somebody put that in just to help guide this board in so you didn't crush these pins when you actually assemble this thing cuz you know, you assemble a thousand of these things and you'll probably crush like ten of them or something like that if

**Dave Jones:** you didn't have that guide post. So, yeah, fantastic. Wow, I won't bother taking out the front panel board. It's not worth it. So, there it is. There's not a huge amount extra on the bottom. You just like the bypass for you know, the main ASICs and stuff and got another little jobbie up there. Not sure what that is. Is that the clock? Is that the PLL? Maybe. Perhaps. I don't know. I can't read it on my little camcorder screen. As far as the front end goes,

**Dave Jones:** that's a bypass in for the ASIC in there. WE'VE GOT OH. OH. OH. THERE'S I WAS GOING TO SAY, there's only There's only two voltage reg I assume they're voltage regs. Why there's only two? Okay, one for each two channels. But then there's no symmetry in the layout.

**Dave Jones:** Like if this one does these two channels, then like this one's in the middle of these two channels. I'd like to see that there or or over here. I don't Just don't like unsymmetrical designs. It's like bad mojo. So, Rigol have really gone to town on this. It shows all their experience over the decades of you know, refining the cost down. Look at that. I can just push that in and it's like it's all lined up. I didn't have to worry about crushing those pins.

**Dave Jones:** And it just like everything to reduce the cost of this thing is just amazing. Unbelievable what you get for 999 bucks. But of course with the NRE and everything that went into all the ASICs for this thing, you know, they've got to make their money back. That's why they have the you know, the pricey options.

**Dave Jones:** But you know, still it's pretty cheap. So, once you've assembled that front panel connector board that we saw under there, this just sits in here and then you've just got the one gigantic assembly. You know, they would have already probably already had the fan on here and then you just whack that in with the one cable. It's like a thing of beauty, joy forever.

**Dave Jones:** Behold the Wonkamobile. A thing of beauty is a joy forever. I'd be curious to see if anyone else tears down their unit and if they've got these [laughter] metal cans just flapping around in the breeze non-soldered or if Rigol knew this was coming to me and and they did that they deliberately left them off for me. If so, I appreciate it. Thank you very much. No alignment pin for this board though. So, I've got to make sure I get that right. Woah.

**Dave Jones:** I think so. There you go. Bob's your uncle. Slippity slip. Hang on. Now that I think about it, given the fact that this wasn't rattling before and it doesn't rattle when this is assembled, obviously they've written like eliminated another step. Another They don't have to hand solder these cans on because they've engineered the bottom of this heat sink here. They've engineered the bottom of this to actually press down on those cans. So, yeah. Yeah.

**Dave Jones:** Of course, it's obvious, dull Dave. Yes, they've Look. There you go. It's holding place. Shake, rattle, and roll and those metal cans aren't going anywhere because they've engineered the height of that perfectly to push down, eliminating a hand solder step. Every step you eliminate in production equals cost. And for like And this is not not making millions of these hundreds of thousands of them. But they're making enough of these in volume to really pay a conscious effort to like minimizing the number of steps you've got to do to actually assemble

**Dave Jones:** you know, manufacture and assemble this thing. And that's how they keep the cost down and keep the profit margin up. Well, that went together a treat. That is beautiful. A thing of beauty, joy forever. Look at it shine. Woah. And boot up time.

**Dave Jones:** Let's go. Up. Yep. I can hear the fan. Fan is unfortunately annoyingly loud. I'm standing more than half a meter behind and I can hear it. I hope it throttles down cuz that's annoying. Nothing on the screen yet.

**Dave Jones:** No. No. Something flashy flashed. Jeez, I want something on the screen a bit earlier than this. At least you know it's on by the fan noise. Is there something wrong here? Thought I heard a relay click. Approaching a minute.

**Dave Jones:** I didn't touch anything as far as I'm aware. That screen's just flickering. No, something's wrong. Oopsie. I've never powered this up before. It's brand new out of the box. Well, I got it from John South from Emmona Instruments here in Sydney. They're the Australian dealers. That's where you can buy them from locally and get local support and stuff. I'm I'm pretty sure he powered this thing up. So, have I killed it?

**Dave Jones:** I thought I put that SD card back in properly. It clicked in place in the little clicky socket. So, I'm going to have to bloody open the thing again. Just another small thing on the assembly of this thing and minimizing you know, production hassle.

**Dave Jones:** They use the same screw on the outer case as they do for all of the heat sink and the main board. Exactly the same screw. Fantastic. Minimize your bill of materials. You can't goof it up. One type of screw. Brilliant. Okay, I've taken the back apart. Doesn't seem to be the SD card. Oops. But I'm getting the soft power. Was it that board to board inner connect, maybe?

**Dave Jones:** Surely. I was raving about that alignment pin. Well, I didn't crush any pins, did I? No, Skip one? But then the alignment wouldn't have matched up, SO DOLL, I FIGURED IT OUT. IT WAS THE this board. You know how I told you about the alignment? I was raving about the alignment pins here and how they didn't have one here? Yep, I was one I was one pin off, so that was obviously shorting out something and stopping it from booting up.

**Dave Jones:** Okay. Doll. Have I got it now? No, I've goofed it again. Oh, wow, they need to ah, no. Rigol. Fell at the last hurdle. Um yeah, it must have been shorting um something out there. Doll, there you go. I was raving about the alignment pin and how they didn't know on this board, fine, and this one they didn't have one and the come again. Anyway, yeah, that was a Dave fault.

**Dave Jones:** Not uncommon. All right, let's try that again, shall we? Before I put the back case back on, but I have put the heat sink on. Ah, there we go. Winner winner chicken dinner. Hopefully I didn't damage anything. Still have to check that arbitrary uh waveform generator board just to make sure nothing's gone wrong there. But obviously, like putting in the wrong row of pins on that board was obviously loading down some lines or something preventing something booting up. So, um maybe got stuck in the loop

**Dave Jones:** trying to detect the um arb gen board or something. I don't know. Anyway, I think we're good. So, 30 seconds. Fan still sounds annoyingly loud, but we'll wait until It's not loud, it's just annoying, I guess. Distracting is a better word.

**Dave Jones:** Come on. You can do it. 45 seconds. Geez. Uh twiddle your thumbs. Oh, come on. Seriously. >> [laughter] >> Come on. A minute. A minute. A minute. Wow, I saw something. Something flickered. Um sh- ah, there we go. We got a spinny wheel. We got a spinny wheel. Oh, boy.

**Dave Jones:** Oh, boy. Ah, that's a bit It's not a showstopper. There we go. A minute 12, I think that was. Uh not great, but you know. What do you want for this kind of bang for buck? All right, what's the power consumption?

**Dave Jones:** It's negotiated uh 20 volts there on the USB-C. And um the roundabout 12 It was 10 watts. Now it's jumped up to 27. 36. Oh. Okay, we got 55, 56 watts with a single channel. If I turn all the channels on, doesn't really go up. If I turn on some methody doodah with the FFTs, so four channels plus FFT, uh 56, 57 watts, something like that. Okay, let's have a quick look at the front end here. I'll move my ugly mug out of the way there so that you can uh see. We've

**Dave Jones:** just got a heat sink Sorry, I had to flip that to make it uh line up. Um 4053, of course, 4000 series uh CMOS, so that's just an analog mux. So, so there's not much on the bottom there.

**Dave Jones:** And I'll compare this with the HDO 4000 front end. And here it is here. And this HDO 4000 series, it of course, as I said, uh uses exactly the same RT 16421Q um ASIC uh front end. So, this contains the variable gain amplifiers uh for the front end cuz, you know, you've only got a little fixed uh you know, bit of attenuation uh happening here. So, this has to have the variable gains to view all your volts uh per division there.

**Dave Jones:** And it's going to have the selectable uh bandwidth filters as well. Um and then a like a driver uh going out of here and that'll be a differential uh pair going out there differentially into the um ADC. So, it's exactly the same thing happening here. There's not a lot more happening here. We do have our 50 ohm input, so there's our 50 ohms. There's not just a single 50 ohm resistor. Looks like they've got a 45R. Uh do they? And then some smaller values with some uh

**Dave Jones:** compensation on uh uh tweaking that maybe to get the 1 gig bandwidth. I don't completely know if the 1 gig layout that I've got for the 98 model is different to all the other ones that go up to 800 meg. I doubt it cuz you'd have to respin the entire main board. So, I suspect that they've just uh tweaked a couple of maybe uh things on, you know, like there's some like there's cap missing there. There's some missing bits here uh for example. Any anything else missing? Maybe like they

**Dave Jones:** might have tweaked a few things to get the 1 gig bandwidth for the special model cuz they're only manufacturing a couple of thousand of those. So, it doesn't make uh sense to respin the entire uh board cuz this is on the main board, obviously. Anyway, um so, apart from our custom ASIC, there's not much else. This three-pin jobby, that'd just be a like an op bias op amp. 1282? I don't know. Yeah, it's just a precision uh op amp. So, yeah, no worries there.

**Dave Jones:** And we've got our AC coupling cap here. And then we've got a relay to just uh short that out. So, in DC mode, it basically just um shorts out. It goes through here like that and shorts it out. So, uh this relay here, look at this, Fujitsu, made in Japan. All the best stuff's made in Japan, of course.

**Dave Jones:** So, our input uh goes into the relay here and that's our 50 ohm termination. So, you hear the relay click when you turn the 50 ohm termination off and on. And then it goes through the um AC uh coupling or uh DC. So, this is a selection relay to select the uh different ranges cuz you can't go from like, you know, 5 mV per division up to 5 V per division with the one range. So, in there at maybe 500 mV per division or whatever it is, it's going to uh switch

**Dave Jones:** out. So, you'll have the different paths. But you'll also have the different paths. This will be like the 50 ohm path and then you'll have another path coming here uh which will be the uh high impedance 1 meg uh path as well.

**Dave Jones:** So, there's nothing uh fancy there. That uh MOSFET um that we saw, I don't know what that's doing, switching off power to the circuit. But from the power measurements, it doesn't seem like it's doing much, so I'm not sure what's going on there. So, have they actually tweaked that much from the 4000? Not really.

**Dave Jones:** It's going to be very similar. Well, I mean, you know, it's relayed out slightly, but it's going to be basically um the same front end that they've got in the um HDO 4000. And this is in the bottom of the range um you know, sub $1000 unit. Now, this uh acquisition, what I thought was an ASIC, I don't think it is. It's an FPGA cuz we've got some intel from the EEVblog forum. Let's have a look here. Thank you very much uh Pel. Pel's from China. So, he maybe got

**Dave Jones:** some inside goss here. Uh according to my firmware analysis, the main processing chip uh well, it's it's an acq- acquisition engine. The processing chip for the UI and everything is the Rockchip uh one. So, um so, for the acquisition engine is a rebranded FPGA from Fudan Microelectronics part number FM230T.

**Dave Jones:** They make a one-to-one Xilinx compatible FPGA. Well, isn't that interesting? Thank you very much, Pel. Um Yeah, so this thing, that makes sense. They're tr- once again, trying to get the price point down. Kind of the And as I said, the Xilinx part, very um expensive part, the Artix-7. So, it looks like this is a rip-off of a Xilinx FPGA. Chinese rip-off of it. Um compatible and they're using this to get the price point down. Fascinating. I wonder if they do that on their higher-end uh newer, you know, they'll

**Dave Jones:** do that on the higher-end models as well. But interesting, huh? There you go. So, they haven't rolled their own ASIC there. They've just ripped off the Artix-7 FPGA from China. They got a cheaper source for it. Well, if it works. So, as I mentioned, I don't think any other scope, benchtop scope at least, can match um the price per- per- performance, what's the bang per buck that we're getting here. 350 MHz analog bandwidth, 4 gig samples per second.

**Dave Jones:** Most are like half that. Um and uh 12-bit and of course. And well, the sample memory, 50 meg for the basic one, 500 uh meg for the, you know, fully software optioned one. But you do get the 500 meg memory. You get all the hardware actually built in. And the dual 100 MHz arbitrary waveform generator.

**Dave Jones:** Again, software option, but it's built into the scope. So, you get all this for in the base hardware of $999. You just got to software option it up or maybe, you know, sail the high seas, captain. Um so, let's, you know, have a brief look at some competitors here. Um Siglent, of course, is the biggest competitor. Probably, you know, previously the best bang for buck um scope on the market, arguably, apart from the, you know, 800 uh series Rigol, of course. But Siglent, of course, massively uh popular, really great

**Dave Jones:** scopes. Probably a better user interface than the uh >> [laughter] >> than the Rigols. Rigol haven't quite nailed the uh user Haven't quite The user interface isn't quite as nice as the Siglent, I've got to admit. Anyway, the um like So, here's their low-end ones. So, the minimum you can get a 350 MHz bandwidth, right? Is their uh 2000X plus series. And the price on that for the 350 MHz model, um 200 meg points uh memory, 2400 Yankee bucks. And it's half the sample rate and it's only 8-bit. So, if you

**Dave Jones:** want the 12-bit, you've got to go the SDS 2000X here. So, let's check that out. Now we're talking. A very nice uh scope. Same screen resolution, but you do get a bigger screen. These are physically bigger scopes, 10.1 inch, but same resolution as uh 1024 by 600 as you get on the uh Rigol here. But the Rigol only has a 7-inch um screen. So, if you're after the visually bigger screen, um yeah, the Siglent's a better bet. Um cuz, you know, you you trade off that

**Dave Jones:** tiny little uh compact Rigol size. But it does have a uh HDMI output, so you can hook on an external monitor. Anyway, let's go down here. So, for the 350 MHz model, if you want 12 bits, but you're still only talking two gig samples a second, not four. That's half of what the Rigol does, and it's $3,500 almost. So, the equivalent Siglent is like three times the price at the basic spec levels. You know, horses for courses, like you know, it's probably got like a lower noise floor, maybe.

**Dave Jones:** know. Haven't measured it yet. But basically, you can get better hardware specs than this for 999 bucks now. That's nuts. Let's check out what Uni-T have to offer. To get the 350 MHz version, you got to go for the MSO 3000 or UPO 3000 E here. And here it is, UPE 3354 E. Once again, 350, four channels, of course. It's only 2.5 gig samples per second.

**Dave Jones:** And price, so you can actually get that Uni-T for 1439 Yankee bucks, but that's only eight bit. It's not the new 12-bit. So, if you want the new Uni-T MSOX 2304, so 300 MHz, not quite 350, but good enough for Australia, So, 2200 bucks. Again, not even touching the Rigol. So, Owon, another super low-cost competitor. They make okay scopes, but you know, they're not as good as the as the Siglents and the Rigols, but they're getting there. So, they have a new ADS 3000 A series. It's a 12-bit

**Dave Jones:** jobby, 350 MHz bandwidth, 2.5 gig samples per second. So, no one's touching the four gig samples per second, 12 bits. They've got a dual channel 50 MHz AFG. So, that's only half the bandwidth function gen. And price on that, bit hard to come by. The only price I can get is a Digikey, and that's $2,000. So, half the sample rate, twice the price.

**Dave Jones:** No one's even coming close. This is nuts. So, Rigol have completely flipped the table yet again for a bang for buck, price per performance. You know, up to four gig samples per second, 500 meg memory depth, a million waveforms per second.

**Dave Jones:** Haven't tested that yet. A review video is coming. I was going to include this like this teardown in the review, but it's already half an hour long, so I decided to split it out. And the pricing is just gobsmacking. 350 meg analog bandwidth for 999 bucks. Probably hackable up to Well, you won't get the one gig cuz I think there might be some little hardware tweaks in there, but someone will probably try it on the EVBlog forum, I'm sure.

**Dave Jones:** >> [laughter] >> Someone will try and get the full one gig out of the thing. But even my fully loaded one, the MHO98, which comes I think fully loaded like with all the options and the dual arb gen and all the protocol decoders and the full bandwidth, it's only 1400 bucks. But yeah, by the time you watch this, it could be sold out. So, >> [laughter] >> but anyway, you might be able to go for the 1299. You might be able to get the 984. What the hell is

**Dave Jones:** This is It's wonderful for the oscilloscope market. Absolutely fantastic, but I don't know like unless the others can roll some custom front end ICs and ADCs and stuff, not sure how they're going to be able to match this price point. So, yeah, Rigol could have this bang for buck market for quite some time. But anyway, I literally haven't used it yet, so I'm about to go do that now. But So, I've just got it connected up here. The web interface just works.

**Dave Jones:** You just plug it in, Bob's your uncle, go to the IP address, not a problem. And we can get our web control, and there it is there. It would have been nicer if it went full screen, but check it out. I did not kill my function gen. So, great. This is a 100 MHz waveform here. It's working just great. And we're 50 ohm terminating that. We can one meg terminate that.

**Dave Jones:** Look at that. I love the transparent. You can set the windows to transparent and stuff like that. We go into the big Rigol menu here. Like some people don't like the Rigol interface. I don't think it's that great myself, but some people think it's better. So, six of one, half dozen the other, whatever. So, I am connected here. We can go into the options here, and I've got the all the options here set forever. So, I believe like the pimped up version that I've got comes with

**Dave Jones:** absolutely everything, all the serial decoding. You can get CAN, FlexRay, and I2S audio stuff, and you know, 1553 bus, and and the 500 meg storage, and the dual 100 meg gen, all all built in for 1400 [laughter] Yankee bucks.

**Dave Jones:** 1 GHz, four channel, 12 bits, four gig samples per second. What? So, we can get our math waveforms up here, like splitting different screens and things like this. You've seen the user interface before on Rigol. So, we can get our histograms. We can do the bode plot as well. That is like if you get the software If you get the function gen option, you get the the bode plot. Hello. What's it doing? There it is. Anyway, with 100 meg function gen, that's really very flexible. Um so,

**Dave Jones:** yeah, like dual channel 100 MHz function gens with bode plot capability for frequency sweeps. Amazing. You can see though that the multiplexing we have good drop down to one gig sample per second with the four channels on. So, that is a bit disappointing. I was hoping to get the two. And so, with channel three off, we get the two gig samples per second. So, it looks like it's combining. Well, and if we turn off channel four, then if we only have the one channel on, then we're

**Dave Jones:** getting in our four gig samples per second there. So, unfortunately, like we can't even like separate the two. So, they're actually using combining both ADC chips there. So, like we can't even turn on channel three. We have it.

**Dave Jones:** That's how they're doing it. It's clever. So, they're only So, it's only a looks like it's only a two gig sample per second ADC, and then they're muxing them for that. So, you can't do the channel one and channel three trick like you can on some other scopes. So, that's how they're getting four gig samples per second, but hey, I'll take it. And then if you turn on either channel four or channel two, it doesn't matter which, you drop down to the one gig sample per

**Dave Jones:** second. But then of course, we've got our logic analyzer as well. It's not like an active probe logic analyzer or something, but hey, for basic logic analyzer capability, definitely take that as well. And of course, all the math functions. We can turn on the FFT.

**Dave Jones:** I think this is supposed to have better FFT in some way, but I haven't haven't investigated haven't investigated that yet, unfortunately. Just testing the one gig bandwidth. I've got my Leo Bodnar pulse gen connected up to the input here. I've only got the one channel. Unfortunately, using these via remote web interface, it's not as nice as the knobs on the front panel. It's not nearly enough. Thankfully, we do have the transparent menus here. So, here we go. We've got the rise time here, currently 360 puffs seconds there.

**Dave Jones:** So, that's actually not That's not too shabby. A response. I like it. But watch what happens if we turn on either channel two or channel three. So, we drop down to the two gig sample per second. Look at that. Look at that.

**Dave Jones:** We've got some extra genie happening there. That's not terrific, is it? So, yeah, what's going on there? And it's not like a same gives the same response on channel three as well. So, yeah, we but we are having our sample rate there. So, yeah, but that's that's interesting. Is it not? So, not sure what's what's going on there. Maybe we'd have to extract the data to look at that. But if we got the single channel, four gig samples per second, it's looking pretty schmick. And I'm feeding in a one gig

**Dave Jones:** sine wave at 100 mV RMS from my RF function gen, and it's 102 mV. It's bang on. It's got at least a one gig bandwidth. So, yeah, like it's not minus 3 dB down. I wonder where where it is minus 3 dB down. My RF gen only goes to 1.5. It rolls off very quick. I'm at 1.15 GHz here, and we're almost 3 dB down, not quite. But if I go to 1.16 GHz, it drops down like 620 mV or yeah, 62 mV or something. So, yeah, it drops

**Dave Jones:** off pretty quick, but it's at least got a one point one gig bandwidth. Wow. Unfortunately, it looks like their website's died. So, too many people trying to buy it, is it? So, that's the new MHO900 series. I hope you like to look at that teardown. Yes, I will do a review on this thing, but it's going to take more time. I was hoping to do it in this video, but no, teardown took long enough.

**Dave Jones:** Very impressive. Unbelievable price point. It's artwork on the bench. High quality metal enclosure and metal knobs. It's an ABS enclosure. It's clear. I can see through it. Transparent rear panel enables you to view the precision electric circuit structure inside.

**Dave Jones:** >> [laughter] >> Fantastic. 24K gold nameplate. A commemoration for keeping our original intention of making Rigol products. There you go. Good on them. Each MHO98 has a unique number imprinted with its unique identity and glory. Glory. So, mine is number seven.

**Dave Jones:** >> [laughter] >> Mine's double 07 or 07. Terrific. But yeah, this is really nuts. Um this is going to change things. Like if you only got a $1,000 budget, I I previously done that, didn't they? What What I said if you had a $1,000 budget, uh which scope?

**Dave Jones:** Was it one of the Rigol? Uh the Rigol 1000? Was it? If you only got a $1,000 budget and you don't mind like a physically small form factor in a 7-in uh screen, the the resolution's there, it's fine, but you know, damn.

**Dave Jones:** There's probably nothing else that can touch it for quite a while by the looks of it. Anyway, thoughts and comments down below as always and over on the EVblog forum. That's where all the action test equipment action happens.

**Dave Jones:** That's where all where all the hacks happen. That's where all the experimentation happens, all the discussion, everything else. Not only just the Rigol scopes, but every bit of test gear. It's nuts. It's the place to be. Anyway, catch you next time.

**Dave Jones:** >> [music]
