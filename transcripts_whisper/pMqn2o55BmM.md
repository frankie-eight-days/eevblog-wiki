---
video_id: pMqn2o55BmM
title: EEVblog #913 - Mailbag
url: https://www.youtube.com/watch?v=pMqn2o55BmM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 50, "3": 68, "4": 88, "5": 107, "6": 128, "7": 145, "8": 164, "9": 179, "10": 194, "11": 216, "12": 234, "13": 259, "14": 276, "15": 295, "16": 316, "17": 337, "18": 353, "19": 372, "20": 390, "21": 409, "22": 429, "23": 445, "24": 465, "25": 481, "26": 499, "27": 514, "28": 533, "29": 550, "30": 566, "31": 585, "32": 607, "33": 623, "34": 638, "35": 651, "36": 668, "37": 688, "38": 708, "39": 723, "40": 741, "41": 760, "42": 778, "43": 797, "44": 827, "45": 845, "46": 863, "47": 889, "48": 909, "49": 927, "50": 949, "51": 971, "52": 995, "53": 1011, "54": 1029, "55": 1045, "56": 1059, "57": 1077, "58": 1095, "59": 1111, "60": 1127, "61": 1147, "62": 1163, "63": 1185, "64": 1201, "65": 1221, "66": 1243, "67": 1259, "68": 1275, "69": 1291, "70": 1313, "71": 1333, "72": 1347, "73": 1363, "74": 1381, "75": 1405, "76": 1419, "77": 1443, "78": 1463, "79": 1479, "80": 1499, "81": 1519, "82": 1533, "83": 1551, "84": 1567, "85": 1583, "86": 1603, "87": 1625, "88": 1645, "89": 1659, "90": 1675, "91": 1689, "92": 1717, "93": 1741, "94": 1757, "95": 1771, "96": 1789, "97": 1813, "98": 1829, "99": 1849, "100": 1879, "101": 1897, "102": 1913, "103": 1933, "104": 1947, "105": 1967, "106": 1981, "107": 1995, "108": 2017, "109": 2049, "110": 2065, "111": 2083, "112": 2099, "113": 2117, "114": 2137, "115": 2155, "116": 2171, "117": 2187, "118": 2201, "119": 2225, "120": 2241, "121": 2261, "122": 2285, "123": 2305, "124": 2327, "125": 2343, "126": 2363, "127": 2387, "128": 2405, "129": 2421, "130": 2439, "131": 2457, "132": 2479, "133": 2497, "134": 2519, "135": 2551, "136": 2569, "137": 2587, "138": 2603, "139": 2621, "140": 2645, "141": 2677, "142": 2697, "143": 2719, "144": 2755, "145": 2773, "146": 2789, "147": 2807, "148": 2825, "149": 2845, "150": 2867, "151": 2887, "152": 2905, "153": 2927, "154": 2945, "155": 2961, "156": 2977, "157": 2995, "158": 3019, "159": 3041, "160": 3059, "161": 3075, "162": 3089, "163": 3103, "164": 3127, "165": 3149, "166": 3169, "167": 3189, "168": 3213, "169": 3235, "170": 3263, "171": 3287}
---

**Dave Jones:** Hi, welcome to everyone's favourite segment, Mailbag! Let's get straight into it. Got one from Australia. Beauty, this one is from Malcolm. Good on ya, Mal. Thank you very much. No last name, just Malcolm. Let's go. Sorry about the lack of videos. Recently I've been busy with various stuff which you'll see soon.

**Dave Jones:** What have we got? Oh, NBN! NBN, the National Broadband Network here in Australia which is a complete turkey because our government completely and utterly screwed it up. They spent like 30, 40 billion dollars or something on our National Broadband Network. What it is is the huge master plan to make Australia

**Dave Jones:** a super-duper technology country with all these... everyone gets... It was supposed to be fibre to the home and then the dickhead Abbott government got in and it was fibre to the node and then copper and wireless and all sorts of bullshit like that.

**Dave Jones:** Anyway, it was a complete schmuzzle. Anyway, no business park here in Sydney actually has the NBN. Yet here, just across the road, brand new houses have the NBN. Like... crazy. Like business doesn't matter. Anyway, found a bunch of these out in the shit

**Dave Jones:** and have absolutely no use for them. Alright, thanks Mal! So yes, we have a property of NBN Co. Ltd. Yeah, it's fibre. There it is. Wow. Okay, so that's an NBN fibre modem. Cool, we'll crack that open. It'll be just like a normal modem set

**Dave Jones:** but it'll have a fibre interface on it. And this is a NBN... What is it? UPS. It's some sort of... there's no battery in it. But cool, okay. It's some sort of backup power gen. Awesome. 2 minute, 10 hour. So these are actually consumer level stuff as it turns out.

**Dave Jones:** This is if you get fibre to the premises which they're not doing much of here in Australia. Unbelievable. I don't know, this is the I240G-R modem. I don't know if it's actually Alcatel-Lucent. I don't know if it's just like a re-badged another one

**Dave Jones:** or whether or not they actually had it specifically done for them. Anyway, fibre in, power supply connection and your Ethernet and also 2 phone outlets as well. So, there you go. And this is an optional battery backup thing. There we go, there's no battery in there.

**Dave Jones:** You can buy it as and you can actually once again this is consumer level, well they have guides for it anyway available on their website and that's just a battery backup so your phone can still work if your local power goes out. Anyway, let's crack it open.

**Dave Jones:** And we're in like Flynn and this is exactly what you'd expect. One big massive ASIC controlling everything. We've got our fibre optic which is just a connector. It's not a PCB mount. That's going over to here. We've got some sponge on top of that.

**Dave Jones:** I don't think that would be thermally conductive because like there's no reason to do it. Yeah, I don't really get that. There's no, you know, nothing to dissipate it to. So yeah, go figure. Anyway, got our requisite Ethernet isolation transformers and not a huge amount more.

**Dave Jones:** There's some telephone interface stuff with some protection. There's a poly switch down there. And Bob's your uncle. Not a huge amount more. And the power supply here, just regular mains input. Then we've just got some sort of Phoenix contact connector there and Bob's your uncle.

**Dave Jones:** Classic single-sided power supply. Nothing special there. Just yeah, it's not even FR4 grade material. Very common. Ooh, high pin pitch dip in a socket there. Interesting. Anyway, opto-isolation over to the main Phoenix contact connectors there. Bridge rectifier. Main cap. It's all happening. So you've seen that all before.

**Dave Jones:** Got double-sided load on the bottom of course. That's all wave-soldered so they'd all be stuck down. And well, it's a reasonable implementation. It's got all the requisite protections and everything else. You know, they wouldn't be skimping on this baby and I don't think they have.

**Dave Jones:** They've actually gone to the trouble to embed a thermistor underneath the battery there, measuring the battery temperature. Nice touch. Postcard time. Thank you very much, John McGruin. Got another one from Australia. This one is from a company I know. 4D Systems, you may have heard of them.

**Dave Jones:** They're just here in Sydney out west and they design and manufacture LCD modules and stuff like that. So hi to Attila, who's the founder and CEO. So let's have a look. They've sent, whoa, goodies. Oh wow, look at this. Gen 4 series LCDs.

**Dave Jones:** Apparently they bought, they're so big now, they actually bought their own LCD company in China or Taiwan or somewhere like that. So they're going great guns. But these things are still designed and manufactured here in Sydney. Awesome. Bit of swag. 4D Systems. You know, hobbyists do use them, but they're quite pricey.

**Dave Jones:** But they've got performance, all the graphic stuff is all built in, and everything incredibly easy to use. And trust me, when I was developing production test systems and other types of systems where we'd build one or ten of them or something like that,

**Dave Jones:** you wouldn't dick around rolling your own stuff. It didn't matter that these cost how much these types of modules actually cost. It saves you so much development time and effort and grief and all sorts of stuff that, you know, they were an absolute bargain.

**Dave Jones:** So anyway, very cool. They've got new Gen 4 stuff. Let's check them out. 4D Systems, turning technology into art. Ooh, they got themselves a new slogan, I don't remember that one. Anyway, we've got the Gen 4, Generation 4 micro LCD 24 DT, micro LCD.

**Dave Jones:** Guess I can't make anything put micro LCD. Ah, well. Anyway, and we've got the micro LCD 43 DCT. T for touch, no doubt. And the big daddy, look at this, 7.0. Is that because it's 7 inches diagonal? I think it might be. Wow.

**Dave Jones:** Look at this. What a Bobby Dazzler. Oh, that. That's like a mini tablet. Yep, mini 7 inch LCD, look at that. And they've got nice genuine 3M tape around there to stick it on. So if you're designing your product, you're designing your test system or whatever it is,

**Dave Jones:** you just get the cut out like that and hang on, 3M. Oh yeah, genuine 3M adhesive smell, love it. And, whoop, that's, oh, there we go. Anyway, they've just taped that on there for you just to keep it in place. Stop it going loosey-goosey inside the case.

**Dave Jones:** And they've got their 4D Systems chipset. They actually do their own chipset. I don't believe it's a custom ASIC. I think it, well, it was a pre-programmed micro, pre-programmed PIC back in the day with all their, all their graphics drivers and everything else in there.

**Dave Jones:** Because these things are designed to be super duper easy to use. You don't really need to know anything about them. But yeah, we've got an SD card on there. And that's a beautiful module. I guess I should read the manual first to figure out how this baby works.

**Dave Jones:** But anyway, we've got some user I.O. there. And that's what, like there's no, like, power pins on the thing. So presumably you power it through that. Comes with a little Gen 4 interface module. Look at that, that's like a serial RS-232 interface for the thing

**Dave Jones:** if you want to drive it old school. Ah, here's a breakdown of the different modules in there. Lovely quick start guide here. The Diablo processor, that's the one. They've got their own processor and their own language for driving graphics displays and things like that.

**Dave Jones:** The 7-inch we've got here, 800x480 resolution. And then if you've got the touch version, you've got a capacitive touch or DT's resistive touch, DCT, capacitive touch, choose your flavor depending on your application. Um, and all the interface types. It can do SPI, serial, I2C, GPIO, it can do analog.

**Dave Jones:** So it can actually, because it's a processor, you can actually program it to do its own thing. It can be its own controller. So if you're developing some sort of interactive user display terminal or something and you want to have it do some basic processing,

**Dave Jones:** respond to touches and do all that sort of stuff, you don't need a processor board. You can actually do everything inside this thing. Well, you can try to anyway. And you can even, you know, analog inputs and do stuff like that. Fantastic. Ah ha, looks like the little serial interface here

**Dave Jones:** is designed to hook up to your PC. Why it doesn't have USB interface, I don't know. Because that's where you would program the thing from. So that's the only disappointing thing so far. Connect the micro USB cable to the Gen 4 PA. Oh, don't have that one.

**Dave Jones:** Only got the serial. Bummer. And then a little 4-inch-er one here. Oh, isn't it cute? Yes, you do get the same little serial adapter in there, but yeah, isn't that cute? Just put it straight on your product and Bob's your uncle. Fantastic. Presumably, you can use the programming system,

**Dave Jones:** the workshop for IDE and program that and whack it on, whack your code on an SD card and put it in there rather than have to hook it up to the PC. But that is a 100% guess. So I'm going to have to leave playing around with these puppies

**Dave Jones:** to a separate video. I don't think it's warranted in the mailbag, but the only thing I'm disappointed about these is power. I would have liked to have seen a couple of screw terminals on there. I don't know what they run from, 5 volts or 3.3 or whatever.

**Dave Jones:** I would have liked to have seen a couple, just a couple of screw terminals on there so you don't have to power it through the flat flex. These are supposed to be self-contained modules, so I really would have liked to have seen that,

**Dave Jones:** and I don't know why they haven't done that. Looks like you've got to power it through the ribbon cable interface. Actually, these puppies are cheaper than I thought. Maybe they've got the prices down. I remember 4D Systems graphics modules being more expensive than this,

**Dave Jones:** although it could be my imagination. The small ones like this start from 29 US bucks, and going up to the 7-inch baby like this, only 129 US dollars. That's an absolute bargain for a completely developed self-contained display system that you can embed into your projects.

**Dave Jones:** You know, not great for volume manufacture. If you're making 100,000 widgets, you know, you wouldn't use these, but if you're making tens or even hundreds of units for a client or for some particular purpose, or especially just for a one-off, yeah. If you need a graphical interface, you wouldn't roll your own.

**Dave Jones:** It's just not worth it when you can get something like this which has all the graphics display and processing capability built in, and it can do user I.O. and all sorts of stuff. No contest. Awesome. I'll link them in down below. Thanks 4D Systems and Attila.

**Dave Jones:** Alright, let's see if this thing does anything. I've got it hooked up to my power supply. I don't like the fact that the ground is not the bottom pin down there. Yeah, it's second from the bottom. No. Anyway, here we go. Let's turn it on

**Dave Jones:** and see if it does anything. Out of the box. Oh? Oh yes, it does! Oh? It's upside down! All the electrons are going to fall out. Please refer to the quick start guide. Anyway, coms, it looks like 9600 board is the standard interface.

**Dave Jones:** Presumably if we had an SD card in there with the program compiled on there from their visual compiler system software that you can get, then it'd just work, but no. Anyway, powered up. And that draws 2 watts for those playing along at home.

**Dave Jones:** Don't get many letters. This one's from the United States of America from Rocco Rossetti. Awesome name. Let's have a squiz. Yeah, don't get many letters at all. I'll try not to rip the letter that's in here. I've done that on more than one occasion.

**Dave Jones:** Here we go. We have a nice letter. Oh, it's not handwritten or typed. It's printed. Here we go. Enclosed is a USB light. Notice that you could input it. What? Oh. Was it attached to another item? Did it fall out? Anyway. Hmm. Weird.

**Dave Jones:** Email address. I won't tell you, but it involves out of time. Beautiful. He's had it for 15 years. Fantastic. Yeah, maybe it fell off or out of something else. Oops. So many things on the shelf there. It's ridiculous. And you know you've got

**Dave Jones:** too many multimeters when, like, you've just got them under the mailbag items. Go figure. Have we had one from Trinabad and Tobago before? I don't think so. Anyway, one from person unknown. We're going to let oh no, there could be a little something in there.

**Dave Jones:** Anyway, we've got ourselves a letter. Thank you very much, anonymous person. Let's have a squiz. Yeah, it's a little pieces of something or other. Simplest and most useful vintage Tektronix repair accessory. Ooh, vintage tech repair. For all you vintage tech repair fanboys. Let's take a

**Dave Jones:** squiz. Hmm. I absolutely love products like this. Purpose-designed thing and it's popular on eBay. Sold 40 in under 24 hours on eBay. It's for the old Tech 500 series plug-ins with a busted pull tab. So they're made of Lexan and there you go.

**Dave Jones:** It's designed for if you're a tech fanboy, you've got the old Tech 500 series and you blow on these things. eBay item. Check it down below. Awesome. Made in Trinidad. Brian Lara country. For you cricket fans, you yanks probably have no idea who Brian Lara is or what cricket is.

**Dave Jones:** Ah, goodness. Anyway, awesome Ansel. That is perfect. Niche product. Great stuff. Made in Canada. By all my Canadian viewers, beauty, this one's from Epiphan, if I'm pronouncing that correctly, Epiphan Systems Inc. in Canada. And this one is quite interested in this one because it's a

**Dave Jones:** tool which I can most certainly use here in the lab I suspect. I hate it when they've got invoices on the outside because you've got to tear through like ten sheets of paper. And yeah, so this is for people like me and maybe some of my audience as well.

**Dave Jones:** Ta-da! The simplest way to share video. It's the Avio, Epiphan, Avio. Anyway, it's a 4K video capture device. Awesome! Let's check it out. So here we have the made in Canada Avio? Avio? Avio, I think it is. Yeah, 4K video capture. HDMI in, USB out.

**Dave Jones:** Of course it has to be USB 3 and yep, you get a USB 3. And it allows you to capture, stream, record, no software to install. All you do is connect the cables. Fantastic, up to 4K. I'm hoping that, I haven't checked the actual specs of this thing,

**Dave Jones:** but hoping that, I don't shoot in 4K here, but I might in the future. Who knows? But I do have my Togano microscope which is a pain in the arse to capture from. At the moment I'm using an Ava microscope. Ava, Ava, Ava Media?

**Dave Jones:** Yes, hang on, I'll get it. There it is. I'm using the Ava Media Live Gamer portable, which will capture, which will input 60 frames per second, and it saves it, I just save it to the SD card. It can go to the PC and stream

**Dave Jones:** as well, but I do all my capture from that, and then I just have my, I have an external mic coming in here which I record from at the same time. And this works reasonably well. It's a bit buggy, sometimes it doesn't record properly anyway.

**Dave Jones:** This will only record, it'll input at, it'll accept 60 frames per second at full HD, but it won't record. So it only records at 30 frames per second, but at least it works. Maybe this one with its big beefy processor and everything else will actually

**Dave Jones:** sample and at 60 frames per second. Same shame, it's not SD card saveable. It's, you've got to stream it to the USB. Eh, but it's designed for streaming applications, live video, all that sort of jazz. Wah! Don't turn it on, take it apart.

**Dave Jones:** And it is a nice bit of kit, let me tell you. Feels super high quality, made in Canada, thank you very much. And, yeah, there you go. HDMI in, got some vents in there, we can see some big, it's actually hefty, looks like we've got some decent

**Dave Jones:** sized heat-sinking in there. And you can see it through that, or is that just the end of the can? Anyway, I've taken the screws off. Ah, ah, might have to pry it open. Here we go, we want the reveal. Ta-da! Oh, look at that!

**Dave Jones:** Little low-profile fan inside that thing. Isn't that sexy as? No wonder they had the vents in there. Ooh. What's that? Ooh, that's a little light pipe. It's a little light pipe on there, but yeah, that is beautiful. Heat-sinking, I'm not sure, yeah, I can get the heat-sink off.

**Dave Jones:** Hang on. You can see on the base of the board here, before I take the heat-sink off, we've clearly got three BGA parts, one here. That looks like a, for all the world, like an FPGA pinout, wouldn't surprise me. And then they've probably got, you know, like an ARM

**Dave Jones:** interface, ARM micro or something like that. Who knows, anyway? Let's flip it open. Oh, I don't know where the cable for that fan's going. But let's... oh, yeah, got a bit of paste. Oh, there we go. We're good. We're being slimed! And here you go, this makes complete

**Dave Jones:** sense now. Yep, it was an FPGA, but it's upside down. Yes, all the electrons will fall out. No surprises for finding a Xilinx Artex 7 here. Real high-end FPGA. Big grunty beast. I didn't get the exact model number there, anyway. You can look it up.

**Dave Jones:** And it's probably like $100 in like one-off quantity. It's, you know, doing a lot of horsepower inside this puppy. And they haven't decided to roll their own 4K HDMI interface. Why would you? Analog devices do a whole range of HDMI interfaces. I've used the analog devices

**Dave Jones:** HDMI interface before, but when I did it, jeez, 4K wasn't even invented then. Anyway, that's the ADV7619 and that is an absolute beast as well. It's got a 36 to 48-bit output bus for all the component video. That'll be funnelled straight over. Look, you can see the termination resistors

**Dave Jones:** there. There you go. And that'll be funnelling all that data through to the Artex, which will be doing all of the processing, all the heavy lifting of that thing. And then the USB interface, yeah, you're not going to roll your own USB3. Hey, Cypress Semiconductor

**Dave Jones:** do that as well with the CYUSB31-4 for those playing along at home. But yeah, that's what you're paying for. All the magic inside there. But then again, from memory, the analog devices, HDMI chips I used to use, they were like $50 parts or something.

**Dave Jones:** They weren't cheap. I'm not sure what this one is, actually. I'll have to look it up. And I'll annotate the video. Anyway, that's a very nice board, and I like the fact that they left the solder mask off there and gold-plated that, gold-flashed it, because that

**Dave Jones:** connects through to the case down in there, and that makes a half-reasonable RFI shield connection to the case. Anyway, no whoppers. So that is a nicely engineered bit of kit. And they claim it's tough as nails, and yes, it is. I love the case.

**Dave Jones:** It feels absolutely robust. You could stand on that thing and drive over that thing in a car and no worries whatsoever. It's gonna survive. It costs $399 US bucks, which sounds like a lot, but for a professional 4K USB streamer like this, then yeah,

**Dave Jones:** it's value for money. Anyway, the proof is in the pudding in terms of actually streaming video, make sure there's no bugs in the thing, it does it reliably, all that sort of jazz. So obviously I can't do that in the mailbag, I'll have to leave that

**Dave Jones:** for a separate video, but I'll definitely try it out on my Togano microscope, and I just checked the specs, and yes, it does do 1080p at 60 frames per second streamed. So, beauty. I've got the perfect test platform for that. And by the way,

**Dave Jones:** these end pieces look like plastic, but they ain't. I got one from Elektor in Germany. You know Elektor, they've had like, this is probably their fourth Suck of the Sav, is it? Anyway, some people have asked, like, what does Suck of the Sav mean?

**Dave Jones:** It's an Australian expression. I'll let you research it for yourself. Anyway, yeah, common expression here in Australia. Fair Suck of the Sav, mate. Anyway, what have Elektor sent? Oh! Elektor magazine. Okay, excellent. I haven't read Elektor for, oh, donkey's years. Yep. Used to be, oh,

**Dave Jones:** we've got a ruler. A ruler. It's not as good as the Elektor Lab's ruler. Not as good as the MicroRuler. Sorry, I have to get back and actually release the MicroRuler 2 that I've, um, that some people have got, but yeah, I've been slack.

**Dave Jones:** Anyway, uh, eurocircuits.com? Anyway, it's got some gauges and stuff on there. It's got more paperwork than items. It's got a bunch of stuff, which I like. There we go. Um, alright, what have we got in here? Oh! It's the Elektor Uno. Arduino! And this comes from Jan,

**Dave Jones:** the editor-in-chief of Elektor magazine, and they're freaking, they are fans of the blog, by the way. Thank you very much. Um, and they've sent through not only the new Elektor Lab's Arduino compatible clone. Here you go. Let them explain it. There are a zillion Arduino

**Dave Jones:** things out there, but this one's special. Um, the Elektor Uno 4 is an evolution of the Uno R3, uses a blah blah blah, supercharged bee brother, blah blah blah. This puppy has two USARTs. Awesome. Um, 4 SPI, 2 I squared C, 5 times a whopping

**Dave Jones:** 9 PWM channels, plus an extra 4 GPIO ports. Sweet. Can also run off 3.3, so it's goodbye to the level shifters. Awesome. There you go. So apparently it's an Uno R3 on steroids. There it is, the Elektor Lab. It's, yeah, an Arduino looking thing.

**Dave Jones:** Check it out if you want it. Oh, there's the barcode. There you go. Scan it. And for you ruler aficionados, here's the Elektor Lab's ruler. Ooh, it's upside down. Inches and millimetres. 1.6 millimetres standard. It's got hole gauges, it's got trace gauges. But, yeah, sorry, I still

**Dave Jones:** like my micro ruler better. This is my micro ruler 3. Jeez, am I up to revision 3? There you go. Anyway, um, I have to, uh, get this one. Some people have them, um, but yeah, I've got to get them back into, uh,

**Dave Jones:** mass manufacturer again. Anyway. My one's got a flux capacitor. Can't be beat. And it's good to see that Elektor magazine is still going. Look, it's chock-a-block with all sorts of stuff. Um, 26. I haven't bought this for many years. It wasn't available, um, easily available

**Dave Jones:** in Australia for a long, long time. But, uh, anyway, there's Jan. Thank you very much for, uh, sending this in. And there's a whole bunch of stuff. Look at these tips and tricks. Oh, analog meter. Gotta love it. There's, uh, Arduino stuff. Uno.

**Dave Jones:** No doubt there's going to be lots of micro and stuff like that. Circuit maker tips and tricks. There you go. Ooh, we've got some Internet of Things. Anyway, there's a whole assembler crash course. Good old through-hole. It's, actually, this looks really good. They've got a lot of

**Dave Jones:** stuff in here. I like it. Haven't looked through Elektor for a long time. But, uh, oh, there's the old Philips meter. There you go. You can still pick those up for a song on eBay. What are they doing? That's a... Hey, that's neat.

**Dave Jones:** Someone put in a new display. Fonz Jansen from Maxim put an integrated new display into one of these Philips system multimeters. Neat. Software to find radio stuff. It's all in there. iPendulum. Ooh. Geez, there's all sorts of cool stuff in here. Bat detector.

**Dave Jones:** If you're into your bats, why wouldn't you be? Awesome. There's the Uno, which they had, and brick by brick, uh, a brick power supply. Terrific. So there you go. Magazines are still going. And when I was a boy... Ooh. Hexadoco. There you go, if you're into that sort of thing.

**Dave Jones:** Anyway, um, when I was a boy, before we had the internet, the magazine was it. This is where you got all your information apart from, uh, you know, data sheets and app notes and, uh, things like that which you had to get in physical

**Dave Jones:** form. You couldn't download them. There were no websites back then. And this is, you know, where the hobby revolved around was the magazines. And it's good to see them still going. It's getting very difficult to compete with the interwebs these days, but good on them.

**Dave Jones:** Support them. I'll link it in down below if you want to get a lector. Don't know how much it is. Doesn't say. One from Germany again. Um, I'm not sure if this is a name or not. Volker Oth. O-T-H. I'm not sure if

**Dave Jones:** that's a name or not. Sorry. Um, interesting. What's inside this one? Let's check it out. Sometimes I know because there's a description. Nope. Yes! Volker! Forum nickname. Oh, yes! Um, uh, deadbeef. Yes. On the forum. 0xHex deadbeef. On the forum. Yes! The EVE email forum, that is.

**Dave Jones:** Oh! Isn't that cute? Wow! IRDA USB interface. Let's check it out. Oh, for multimeters. Awesome! Hey, I like that. Love that case. This is jazzy. So Volker here has come up with this little, um, infrared interface for Gossen MetriHit multimeters, because Gossen are

**Dave Jones:** famous for their real expensive infrared interface. Now, I was going to extol the virtues of this, but I just plugged it in, and I tried to pull it back out of my MetriHit energy here, and oops! It broke off from there. Um, yeah.

**Dave Jones:** I think something needs to be done with the robustness there, but look, there we go. It's a bit brittle, but something... Come on, come out of there. But look, I think maybe there's something wrong with my plastic. See how it curves in? Like that?

**Dave Jones:** So I don't know what the hell's going on there, but yeah. Anyway, it was a real tight fit in there, so I tried to just pull it directly back out, and it was wedged in there too far, and it broke! But it'll still work, because there's a little

**Dave Jones:** infrared receiver, or transceiver in there, and USB um, sorry, uh, serial interface, and some dip switches to set various stuff, whatever that is. And yeah, Volca has a reverse-engineered Gossen's one, and this is open-source hardware available, and in Creative Commons, all that stuff, I'll link it in down below.

**Dave Jones:** Much, much cheaper than the Gossen one. My other Gossen made it, nah, it's the same. It's got that curved in, so what part it was supposed to go into, I tried to shove it into the center there, and um, yeah. Oops. Next up, one from

**Dave Jones:** Chris Hopkins from Sukasuna in New Jersey, in the United States of America. We have a, well, I won't tell you. It'll just spoil it. Oh, oh, oh, hang on, I thought it might have had one of those pull things. Yep, there we go.

**Dave Jones:** Ta-da! Ah, and bubble wrap for our protection, we've got a note. Let's see. Ah, and static shielding for our protection. What is this? Ooh! Sony VAIO. Um, MotionEye, what? Bluetooth, wireless LAN, what the hell is it? Um, it's one of the, you probably, a lot

**Dave Jones:** of people might know what that is, but um, it's a Sony thingamabob, broken screen. Aha, it's a micro PC, that's why I do, I have not seen this before, I don't recall it at all. Was a handheld pocket computer equipped with an x86 processor, none of this arm

**Dave Jones:** rubbish. Lots of features that ran full version of XP Pro or Vista. Wow, in a little pocket sized thing, they didn't sell very well due to the high price. Wow, like two grand US, weak battery life of two to three hours, interesting but annoying keyboard,

**Dave Jones:** and the general pain in the ass using desktop interface on a 4.5 inch screen. Yeah, um, it's, yeah, this one's dead. Anyway, um, yeah, there's the slidey up keyboard, look at that, and that is a pretty horrible feeling keyboard too, there's no, uh,

**Dave Jones:** you know, tactile response, very, uh, there kind of is, I guess there's a little tactile dome on the PCB underneath, if we did a tear down on it, um, but it doesn't feel good at all. It is not a good tactile response, it's real

**Dave Jones:** squishy and ugh, it's just no, like, no, this is just like, what, what, you know, meeting did this come out of, what design meeting did this come out of? Everyone walked out thinking, oh yeah, at least we got a, um, at least we got

**Dave Jones:** something out of it, but everyone probably, the engineers probably went back and, ugh, groan, we've got to design this thing, it's going to be a complete nut of flop. Windows XP, obviously this is more than a, uh, two minute tear down, so that will be a retro

**Dave Jones:** tear down, vintage computer retro tear down, coming up soon. Thank you very much. Chris, awesome. Wait, not only do they have a camera on the front, the motion eye, ta-da, they've got one on the back as well, look at that, they thought of everything in that

**Dave Jones:** meeting. Brilliant. Isaac Porous, g'day, Isaac from Portland, Oregon, and I'm concerned with what this is. Anyway, look, I'm an expert on these, um, United States Postal Service packages, packages now, ah, he's in the, he's the inventor of the solder doodle. I guess we have a solder doodle.

**Dave Jones:** Ooh. It's a, it's a, it's a USB rechargeable soldering iron. I don't know. I, I don't get the feel of that. I don't under, that, it's supposed to be moulded for your hand, but I don't kinda, oh, yeah, oh, maybe, maybe, but it just, oh, okay, and then you've got

**Dave Jones:** instant heat, I don't know, I'm afraid of, it's gonna, probably gonna do the business if you're desperate and you're in the middle of nowhere and you need, you know, you're on the road and you need a, uh, USB, ooh, we've got all sorts of tips,

**Dave Jones:** ooh, interesting, all custom tips, um, and you need a portable, when you need a portable soldering iron, you need one, and there are various ones on the market of various quality and things like that, and they're all, even the good ones are meh, you know, they get you by,

**Dave Jones:** um, but you wouldn't want to do anything serious with it, but it gets you out, it gets you by in a pinch. Ooh, nice chisel tip, useless conical, we've got ooh, a little, um, a fine bent conical, some people like those, anyway, let's have a look at the solder doodle.

**Dave Jones:** So there you go, Isaac is the designer of this thing, and thankfully uh, he says that it's good for 24 gauge wire and higher, um, heats up in 15 seconds, yeah, I wouldn't be recommending this for, uh, you know, like, SMD work or

**Dave Jones:** anything like that, it's designed for, you know, rough and ready soldering in the field and stuff like that. Solder doodle, it is, um, open source, USB rechargeable soldering iron, there you go. Um, first thing is it rattles, um, second, I don't know, I

**Dave Jones:** swear this grip just doesn't so I can see what you've tried to do, you know, like with the shaping of that, um, and it could be right or left-handed as well, I can see, but I, I don't, uh, I guess, I guess but yeah, something just doesn't feel

**Dave Jones:** right, I'm not sure what it is, anyway, uh, one of the first things I noticed is that there's no, uh, guard to stop yourself, whoop, slipping like that, and burning your fingers on the tip of this thing, so, um, that would be my first thing, is it should have had

**Dave Jones:** a guard ring on here, any good soldering iron will have a guard ring, so it's just, I think it's probably too easy to just slip off the end like that, and, um, here's the various tips, I guess they're, uh, custom design, comes with all

**Dave Jones:** yep, comes with different types of tips anyway, look at that, that's a yeah, like a, that looks like a hot knife to cut through stuff, anyway what you need is a, yeah, couple of millimetre chisel, that's what you want, oh wow, is that

**Dave Jones:** that looks for all the world like an RCA connector I think it is I think it is it's an RCA it does look for all the world like an RCA wow anyway, hmm I don't know alright let's give it a burl, here we go

**Dave Jones:** I've got to switch it on, and then press down the button uh, what did he say, 15 seconds or something, alright, let's heat it up, and, uh, I've got some 60-40 stuff here on this lead-free rubbish and, uh, let's see if we can

**Dave Jones:** let's see if we can heat up something like this connector here oh, oh, it doesn't, no that, that feels that, you probably can't see it, but that's flexing, it's not heating up that pad is it? come on you can do it oh jeez, oh this is really

**Dave Jones:** struggling to tell you what it's melting just but, yeah there's no thermal capacity in this thing at all I'm holding that on, how long have I been holding that on, for at least 30 seconds and there's no right, so I can't even heat up a pad

**Dave Jones:** on a, like yeah, the solder's melting, okay got our melted solder but even if I blob it on there to try and get good thermal coupling it's not heating up it's not heating up that pad, at all and that's just a, I would

**Dave Jones:** have expected would have expected that to work, it's just not working, and there's no temperature adjustment on the thing nah, nah um, so maybe okay if you want to join some wires together but nah, sorry Isaac, this I think this is just failing, I mean the light's on

**Dave Jones:** somebody's home nah, it simply can't do this pad and no, that one's not connected through to the ground plane, it can't do a pad of that size, it can't even do one of the legs of this common mode choke here, it can't do that, the best I'm

**Dave Jones:** able to do, is like a pin you know, you can do eventually yeah, it does take about 15 seconds to warm up, you can sorry, you can't see that, but I can actually do pins on this connector okay, so that is that is possible, but

**Dave Jones:** yeah, the thermal capacity is terrible using a nice big chisel point, I nah, I it's just not working sorry, it does not have the thermal capacity to heat up one pad and one pin nah, gotta call that a fail sorry, solderdoodle, thumbs down

**Dave Jones:** and if we have a look inside, single 18650 cell excellent, so you've got no issues with multi-cell charging and stuff like that, the little board in there looks quite, uh looks more than adequate, I'm gonna say that's solar cycle, what's that? hmm, anyway

**Dave Jones:** wiring looks a bit wimpy, going off to the connector over there, anyway, you can see how the switch mechanism works, it doesn't do anything there, but where you switch it on, boop, it can come on like that eh, it's, you know it's okay, anyway

**Dave Jones:** no good as a soldering iron, really, unless you're just joining a couple of wires together or something like that, and these are 3D tools 3D trimming tools, you know to trim plastic and stuff like that I'm sure it does work for that sort of purpose, I think I had a little

**Dave Jones:** review of a 3D cutting tool a couple of mailbags ago, and yeah, similar sort of thing so yeah, if you're looking for a soldering iron for the field this one, like for real electronics use, this one's probably not going to cut the mustard I'm afraid

**Dave Jones:** more work required in the thermal capacity aspect of it thank you very much Jason Olszewski from Rochester in New York another one from the United States of America, and let's have a look it's not a complete mailbag without a vintage device and that's what this one is, spoiler alert

**Dave Jones:** but I don't know what, it just says vintage, so I like vintage stuff, oh is this oh that's a typewriter, here we go no worries thank you very much, I typed this on my very awesome wide carriage Royal Express from the 1960s street cred

**Dave Jones:** I think I get the impression it was kind of special edition since it has some sciency add-ons oh, plus, minus, and degrees, keys oh, anyway awesome fantastic let's have a look, oh yeah oh yeah haven't had one of these puppies on here before

**Dave Jones:** an Adler 805 wow, look at that Germany not actually, it's from a German company but it's made in Japan, all the best stuff's made in Japan awesome hang on that's got a distinct mid-1970s smell to it hmm, am I right? sweet 1970s vintage circuit board, Adler from

**Dave Jones:** 1974 the nose knows so here's the Adler 805 look at this eight digit display and it's just a four banger basically, and it is huge you'd expect it, like it's big enough to have the tape and the, you know, like the thermal printing and stuff like that

**Dave Jones:** but then there it is, made in Japan only uses four watts, no worries sniff of an oily rag there 1970s construction all the way with LBJ look at that what's, the tin plate it's all like hand tape laid out of course, what's happened

**Dave Jones:** to the, look they've got, you know, tin plate there but then they've got sections left out there, it had something on it and they didn't get any tin plate good old single-sided construction with the jumper links, NEC processor for those playing along at home

**Dave Jones:** couple of discreet trennies down here and look how they've done the wiring, look how they've done the connections there, in some weird shape, what the, what's going on there, look at the display, it's got a like, is that like power of ten display?

**Dave Jones:** there you go, and we've got our nipple of course, because it's a vacuum fluorescent, but look it's just classic absolutely classic from, can we get a date code sadly no date codes on that chip at all wow transistor regulator there is it oh, classic

**Dave Jones:** just like, wow look at it mains trenny over here well shielded, no worries there alright, let's see if this puppy works I'll turn my 110 volt transformer on and oh, it works look at this ah, bobby dazzler 2 plus 3 equals 5, and there you go

**Dave Jones:** winner, what's that doing over there, I'm not entirely sure, but hmm it does kind of work, and the combined minus and equals, plus and equals sign here is a bit disturbing, because that's not that's just one button oh, yeah well, you know, I don't know what K is

**Dave Jones:** ah constant? some constant thing or something, I've got no idea no idea, anyway winner winner chicken dinner, the Adler 805 another vintage device that's had the crap beaten out of it lucky it made it here it hasn't got a huge amount of padding

**Dave Jones:** but anyway, thank you very much George, or Georgie Chankov, from Bulgaria hi to all my Bulgarian viewers wow you don't get many from Bulgaria, so let's check it out another vintage thingamabob ta-da five and a quarter inch floppy woo-hoo from it's Bulgarian 1987

**Dave Jones:** wow ok, ah it was made in Bulgaria in 1987 it was made in Bulgaria in 1986 it was supposed to work with the Bulgarian made Pravitz computer there you go, hands up if you've heard of the Pravitz computer, I'll link it in down below, there is a wiki page

**Dave Jones:** for it, um, I bet you haven't had the chance of tearing apart Bulgarian made computer parts, no, I don't think we have thank you very much Georgie for sending that in two minute tear down oh wow, and mid 80's everyone was switching to three and a half

**Dave Jones:** inch floppies by then but not in Bulgaria look at this bobby dazzler would ya five and a quarter inch floppies who can remember those, yes and that, if you can read that, anyway 1987, let's take a look inside flat head screws, none of this Philips rubbish

**Dave Jones:** I'll tell you what, there's a few screws loose in the top paddock here that board just slips in there like that, and yeah I think it's oh yeah, there we go missing a couple of screws sure enough, look at this, all through hole

**Dave Jones:** of course, none of this surface mount rubbish, we've got a date code there we go, 11th week 86 so it's at least you know mid 86 construction, I just love the little bit of extra heat sinking down there little bit of aluminium plate on the

**Dave Jones:** tranny down there, fantastic oh man, this is just we've got a couple of trimmers here and yeah, they would be for well, I don't know speed adjustment or something like that, but yeah, there's not much to it, I mean there's very little like, well there's no like digital

**Dave Jones:** processing or anything going on here, it's pretty rudimentary controller so to speak, very I don't know, was drive reminiscent or something, there's very little electronics in here to actually drive this so I'm not sure how much was being done on the computer side of things, but we've basically

**Dave Jones:** got our head is going to be down in there and it's going to come through this little shielded cable here so this is going to be our head amplifier we've obviously got our motor driver transistors here they are going down to the going down to the motor down there

**Dave Jones:** the stepper motor and yeah, there's not a huge amount in these things they are really quite simple in the scheme of things and if we lift that up, there we go the head is going to be stuck under there somewhere yeah, you can just see it

**Dave Jones:** right down in there, jeez I can remember cleaning five and a quarter inch floppy heads, you get the cotton bud out, the isopropyl alcohol and clean away, beauty or you'd use one of those cleaning discs you'd whack the alcohol on the cleaning pad and shove it in and make it

**Dave Jones:** make the drive head seek across and it'd clean the head that was reasonably efficient back in the day but there you go, beautiful mid 80's, I mean I would have thought if I opened this up and didn't have any date codes, I would have thought

**Dave Jones:** maybe this came out of the late 70's or something like that, but they're still making this in at least mid 86, so there you go, got an extra board down in there and a big 10 turn trimmer, thank you very much and yeah

**Dave Jones:** a little heat sink down in there I don't know what's doing down there we're on a roll, let's do some more, another one from Australia, from the lovely Blue Mountains, from Person Unknown thank you very much two minute tear down something old that's what it says, alright

**Dave Jones:** oh yeah to go with our five and a quarter inch floppy thank you very much old school phone it's a modem a Sendata modem that's a 300 board oh yeah what a bobby dazzler check that puppy out, 300 board modem, hands up if you

**Dave Jones:** have a 300 board modem that's what I started with 300 board, what was the 300 no, what was the 1275, oh I forget what was the one that had the 75 um I can't get anywhere yet, 300 board, that's basically 300 bits per

**Dave Jones:** second, and I would connect to local BBS's, local bulletin board systems, and yet this was not, none of this auto-dial rubbish, you had to dial this yourself so you'd have answer originate, and you'd have phone data switch, so you would dial the number on the phone and then

**Dave Jones:** you'd listen to the the modem sex sound, and then you'd flick the switch and hopefully connect to your bulletin board, which was run from people's homes, and they'd have 10 phone lines coming into their house, so you know, depending on which bulletin board you

**Dave Jones:** called up and the generosity of the person running it, and with all those phone lines, you would hopefully get a connection, sometimes you'd have to wait in line and you'd just keep dialing all the time until you get in, and then usually they'd have a time limit and they'd

**Dave Jones:** boot you off, like after an hour or whatever it is, so that you know you don't just hog the thing and stay connected all the time and using one of the connections, but yeah old school 300 board modem oh, those were the days

**Dave Jones:** then I upgraded to 1200 board modem, and then I got the netcom after that was it? After that was the netcom trailblazer anyway, I ended up with the netcom trailblazer, which was, oh, what was it? 13,000, 14,000 or something board, I can't remember, anyway

**Dave Jones:** it was the ducks guts, but you had to have somebody else who had a trailblazer compatible modem on their end to use it, but oh, beauty. Anyway, 2 minute teardown sorry, nostalgia Sendata direct connect modem electro medical engineering proprietary limited in Armadale um

**Dave Jones:** in Victoria, wow made in Australia Australia, I'm assuming I think it might have been I think it might have been made here what a bobby dazzler, 300 bits per second answer and originate, who can remember answer and originate mode who can remember their AT commands, come on, hands up

**Dave Jones:** originate, answer phone, data, that's all you needed and you can dial your own number, preferably with an old school rotary dialer and then flick your modem in and massive 300 board oh man, you can see the characters coming up on the display brilliant, who remembers Kermit

**Dave Jones:** Kermy, oh, check it out classic, single sided construction, look at the big ass AC, um, caps here for our line interface over here it's just did this, yeah this had telecom approval, didn't it yeah, telecom approval number, there you go it's telecom approved, no worries

**Dave Jones:** and a little piddly bridge rectifier there for our mains, sorry, mains DC plug pack input our serial interface bugger all else well you didn't need much really um, so yeah we've got a LM324 what are we, recon R5631, don't know what that is

**Dave Jones:** but an LM324 and not sure, that's an XR um, that's an XR brand and the ICL7660 charge pump yeah, we've got 2 charge pumps here to generate the negative rail and how much else line isolation transformer, oh goodness, classic made in Australia, and that's

**Dave Jones:** late 83, so this would have been manufactured early 84 or thereabouts weee swap your transmit and receive hi, welcome to Teardown Tuesday we've seen this one before, this was sent into the mailbag segment recently by Chris Bowden from the Geek Group, so I'll link in the Geek Group down below

**Dave Jones:** thank you very much Chris, and what it is is it's an analogue computer for an inertial navigation system, an astro compass system used on the B52 bomber, so let's check it out awesome, and I think she's about to pop maybe a few more whacks
