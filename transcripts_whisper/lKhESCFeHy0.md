---
video_id: lKhESCFeHy0
title: EEVblog #827 - Mailbag
url: https://www.youtube.com/watch?v=lKhESCFeHy0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 50, "3": 68, "4": 94, "5": 112, "6": 127, "7": 141, "8": 153, "9": 169, "10": 186, "11": 203, "12": 225, "13": 242, "14": 262, "15": 280, "16": 298, "17": 314, "18": 333, "19": 352, "20": 370, "21": 392, "22": 411, "23": 429, "24": 444, "25": 459, "26": 481, "27": 497, "28": 507, "29": 527, "30": 551, "31": 567, "32": 585, "33": 609, "34": 633, "35": 653, "36": 678, "37": 694, "38": 710, "39": 732, "40": 750, "41": 765, "42": 782, "43": 803, "44": 820, "45": 837, "46": 851, "47": 873, "48": 904, "49": 926, "50": 952, "51": 971, "52": 993, "53": 1018, "54": 1038, "55": 1054, "56": 1074, "57": 1093, "58": 1112, "59": 1134, "60": 1152, "61": 1174, "62": 1197, "63": 1225, "64": 1253, "65": 1273, "66": 1294, "67": 1314, "68": 1331, "69": 1352, "70": 1370, "71": 1391, "72": 1410, "73": 1426, "74": 1449, "75": 1464, "76": 1482, "77": 1499, "78": 1517, "79": 1536, "80": 1554, "81": 1574, "82": 1594, "83": 1625, "84": 1640, "85": 1661, "86": 1676, "87": 1696, "88": 1724, "89": 1751, "90": 1779, "91": 1798, "92": 1815, "93": 1835, "94": 1854, "95": 1877, "96": 1898, "97": 1916, "98": 1932, "99": 1947, "100": 1964, "101": 1980, "102": 1993, "103": 2010, "104": 2029, "105": 2047, "106": 2065, "107": 2085, "108": 2105, "109": 2119, "110": 2135, "111": 2151, "112": 2167, "113": 2184, "114": 2200, "115": 2219, "116": 2242, "117": 2256, "118": 2276, "119": 2292, "120": 2308, "121": 2330, "122": 2354, "123": 2378}
---

**Dave Jones:** Welcome to everyone's favourite SIGMA MAILBAG! I said the mailbag super loudly. Welcome to everyone's favourite SIGMA MAILBAG! Let's get right into it. We've got a FedEx one, you know what that means. It's a commercial jobbie. This one's from Digilent, who of course have had like 10 sucks of the SABI thing.

**Dave Jones:** But they've always got interesting stuff. Come on, does it have one of those rip-pull things? Obviously not. Should have just used the knife. Here we go. Let's have a go. It's obviously going to be a demo board of some description. And we do like Digilent demo boards, they're always good.

**Dave Jones:** So, let's check it out. Green, nondescript green box, good. Haven't pissed away time, money and resources to get the box printed. Yeah, like, just don't bother. It's just silly. Oh, it comes out this way. Here we go. Let's have a look. Hi Dave, meet Artie.

**Dave Jones:** Have some fun with our new power bricks. There we go. Digilent, beyond theory. Alright, they're power bricks. Okay, let's check them out. Awesome. Ooh, yes, they are. Excellent. Always handy, little power modules, power bricks. Although, Artie is not a power brick. It's a Xilinx Artix.

**Dave Jones:** Alright, let's check out the Artix board. So it looks like they just sent me a whole bunch of random stuff here. We've got the Artie board, which we'll take a look at. That's a Xilinx Artix FPGA board. I don't think it's got... yeah, it's just an FPGA board.

**Dave Jones:** It doesn't have a... it's not like a zinc with the built-in processor. And then we've got these new power bricks. Here we go. These are quite neat. It allows you to plug USB in and get various voltages out. So we've got 9 volts, 12 volts and 5 volts.

**Dave Jones:** And then just plug those directly into your breadboard. Very nice. And these are the different models that they've got. I've got all of them. One's a buck, of course, 3.3 volts is dropping the voltage. 5 volts out, you might think, well, why do you need 5 volts

**Dave Jones:** when you've just got 4.5 to 5 on, you know, like a USB and you've already got your 5. And, well, I don't think these things are isolated. I'd be very surprised if they are. They don't seem to have the physical size for that.

**Dave Jones:** So anyway, that would probably be a SEPIC converter, which can do buck and boost basically to give you a regulated 5 volts out, which is okay if you get voltage drop across your USB line and stuff like that. You've got a nice fixed 5 volts, hence the lower current than what's normally available.

**Dave Jones:** And then 9 volt and 12 volt add up to 100 milliamps. Let's check them out up close. And here's the 3.3 volt one. Teeny weeny, you might think they're a molded block, but they're not. Ta-da! It's just a plastic cover. So there's our micro-USB input.

**Dave Jones:** And I've got no problems with micro-USB. I like micro-USB. I know. Why won't you use a mini-B? Oh yeah, get over it. Anyway, yeah, it's a really dense little buck converter. This one, I rather like it. There you go, you can see both sides of it.

**Dave Jones:** Yeah, those playing along at home might want to view that part number in HD. I can't read it on the camcorder LCD here. But yeah, they're certainly doing a lot of business on there. I'm not sure why they're doing so much, actually. My guess is what they're doing here, without trying to figure out what those part numbers are

**Dave Jones:** and get data sheets, they're probably trying to do this properly. I.e. not just feeding 5 volts into a buck converter and then straight out. They're trying to actually negotiate the USB bus here, likely. And then actually providing over-current protection and stuff in here.

**Dave Jones:** But also actually signaling back to the PC, OK, I want 500 milliamps, thank you, give it to me. Although, you don't have to do that. I mean, it's a misconception out there. The USB port will actually, or most, almost all of them, will actually supply 500 milliamps at 5 volts,

**Dave Jones:** regardless of whether or not you actually negotiate for it. It's just a nicety that you should actually do as part of the standard blah blah blah. Anyway, there's our output regulator. So, that's... but we've got two inductors there. We've got another chippy on top.

**Dave Jones:** So I'm not sure what the business is there. It's like they've got two converters in there. Now you might actually be a bit confused about this plus V in pin which they've got on here. Yes, you can actually power it either through the USB input or via the pin input here.

**Dave Jones:** And by the way, this is how they fit in the breadboard. The pins on the bottom just straddle your regular breadboard like that. So very nice, no worries whatsoever. But look, it allows you to actually daisy-chain them together. So that plus V in pin is actually a dual-purpose pin.

**Dave Jones:** So if you feed in 5 volts USB here like I'm doing, this plus V in actually becomes a V out. And it passes the USB voltage through. So then it allows us to daisy-chain like this. So we can have the one USB input here providing all of these different rails.

**Dave Jones:** And guess what else? They're not... they're really not talking this up too much, but they've got plus minus 320 milliamps, like plus minus current. They're actually plus minus rails. So this minus V out here, these are not just... well, these are not isolated outputs.

**Dave Jones:** They're input and output ground are referenced via the single ground pin. But this is actually plus... sorry, plus 12 volts and minus 12 volts, plus 3.3, minus 3.3. Let me show you. So that's actually rather jazzy. If I put my common ground point here,

**Dave Jones:** you'll notice that we get out, bingo! Plus minus 5 volts like that. And this one, we get plus 12, minus 12. No worries. One watt total, and then per brick. So I assume that'll be spread over both outputs, of course. Oh, and I didn't get the negative 3.3, but yeah, trust me.

**Dave Jones:** Plus minus rails. Beauty! These are nice little modules, I like them. So this is what they're actually doing on these things. All that extra circuitry is designed to like switch the input pin, and that's kind of why they've got two regulators on their positive and negative as well.

**Dave Jones:** So absolutely fantastic little power bricks. I like them, they're about $16 a pop. They're not, you know, eBay giveaway prices, but wow, they're worth having a set of those. Definitely. Well done. Just beware though, the data sheet for these things which I'll link in down below

**Dave Jones:** does say these have a maximum output capacitance. Not minimum, but maximum output capacitance, presumably for stability. They go unstable with any higher output capacitance, so just be aware of that. I'm not going to hook up a scope and put in capacitors and try and measure its performance

**Dave Jones:** and instability and all that sort of jazz. Leave that up to somebody else. And here's the Arty. It's a rather ugly looking FPGA development board. I say ugly looking because the white silk screen, I'm sorry, it just does not work. I hate it.

**Dave Jones:** It's just, no, no, wrong, wrong. Anyway, it's an FPGA development board, but those who are eagle-eyed might notice that that looks an awful lot like an Arduino shield, and that's exactly what it is, Arduino shield compatible. But the Artyx 7, of course, is not an Atmel processor.

**Dave Jones:** It doesn't contain any hard processor. It's designed to use the Micro Blaze soft FPGA processor core in this thing. And no doubt it comes with software and all sorts of stuff, but it doesn't come with anything in the box. So I guess you can download it from the website.

**Dave Jones:** I don't know, I'm not going to try it. This is a mailbag, this is, you know, I'm not going to spend a couple of hours mucking around with a dev board here. We've got a couple of switches, looks like we've got some LEDs,

**Dave Jones:** we've got some buttons, and a whole bunch of additional I.O. here, because the Artyx 7 FPGA architecture, of course, extremely powerful, so it's got all the extra I.O. on there. You can't just get it all on the Arduino shield. It's got a buttload of memory, 256 megabyte of DDR3,

**Dave Jones:** it's got 16 megabytes of quad SPI flash, and it's got Ethernet and USB and I2C, UART, all sorts of jazz, nothing fancy on the back. Oh, the white, oh no. Anyway, it's $99, so if you're looking to get into softcore FPGA programming, it's probably not a bad option worth checking out.

**Dave Jones:** And it does actually come with a voucher, I won't show you the voucher code, but anyway, you can get a barcode and a voucher code, which gives you access to the Vivado design suite and other software tools. And will it actually do anything out of the box?

**Dave Jones:** Because there's no information with it actually provided that there is actually the softcores already programmed in the bootflash to maybe run an Arduino Uno compatible, you know, processor or something like that. So let's, it can be powered from external DC, there's a jumper switch here,

**Dave Jones:** or USB, so let's go USB. Got some lights happening. Oh, switches, I expected the LEDs to light up with the switches. Oh, hello, hello, there we go. Huh, is that all it does? Press the second switch there, was it? And it flashes some lights.

**Dave Jones:** Hmm? Yeah, okay, it does something, so obviously there is a processor which is doing something. Hmm. Next up we have one from Ben Wang, he's from Australia, of course. Quick, urgent, open before December 7th. It's December 7th, beauty. Only, what, ten days until Star Wars, or is that December 18th?

**Dave Jones:** But, yeah, I think it comes out like a day early. I haven't actually booked my ticket yet. What the hell am I doing? Unbelievable. Anyway, what's Ben said, he's obviously got a Kickstarter. Urgent, open Kickstarter, yes, yes. Yes, I won't get the knife, I'll get the, oh, I'll do it faster without the big knife.

**Dave Jones:** Here we go. Oh, in so much hurry. This should be live. Hopefully I'll edit and get this up today. Anyway. Ah, ah, here we go. I've got a board. A note. And it's, oh, it's the remote boot. Just realized I still had fixed focus on my camera from when I interviewed Siglent E.

**Dave Jones:** CEO Eric. Here we go. There we go. It's the remote boot. Let's check it out. And here's Ben's remote boot project. Ben's actually having a second suck of the mailbag. Here he sent something in before, but this is his new Kickstarter project which finishes on the 15th.

**Dave Jones:** And I'm glad to say that it's already smashed its very modest $1500 Australian total. He's already got like 100 backers or something for $4500. So well done, Ben. He's actually a student at North Sydney Boys High School here. So he's still in high school.

**Dave Jones:** And what it is, if you haven't sort of figured it out from the name, it is a Wi-Fi, it just uses a Wi-Fi module, one of the ESP8266 Wi-Fi chips, but allows you, which hooks up to your regular Wi-Fi, but allows you to remote boot your computer, which is exactly what I need here, actually,

**Dave Jones:** because often I will, like, because I use a VPN to come into my, sometimes I do some stuff from home. If I've, you know, just finished editing a video and it's rendering and stuff like that, then I'll have to, but I want to go home, I need to go home and start the, and from home I can log in, remote log in to my machine here,

**Dave Jones:** start the transcoding, then start the uploading before I go to bed, etc. So I've got to leave my computer on, and then, but sometimes I've left, I've turned my computer off, gone home and I've gone, oh, damn, I wish I could remote log in to my computer, but I've switched,

**Dave Jones:** physically switched it off. This is a way to do it without it. And unfortunately, this one doesn't, is not programmed, hasn't finished the code yet, so I can't power it up and try it. But, yeah, it just hooks into your PC and then into your Wi-Fi,

**Dave Jones:** and then with a remote web interface allows you to log in and switch on your computer, physically switch it on. So how does it physically switch your computer off and on? Well, it's rather clever. It just goes in series with your reg inside your PC, your power button, and your reset button like that.

**Dave Jones:** Fantastic! It's great! I want to use it now, I want to install it, but unfortunately it hasn't finished the software yet, still working on that last minute. But I think it's a great concept. I love it! Oh, I want to give it a go!

**Dave Jones:** Anyway, if you're in need of something like this, well worth checking out. Well done, Ben! Hope it comes off well for you. I mean, there's nothing to it. I mean, it's just, you know, he's written some web interface for it and programmed the ESP8266 Wi-Fi chipset,

**Dave Jones:** and just a clever idea like that. Winner, Kickstarter. Awesome, Ben. I'll link it in down below if you want one. Next up, one from Deutschland, comes from Tim Ryman. Good on you, Tim, thank you very much. Hi to all my German viewers. Let's check it out.

**Dave Jones:** I know kind of, sort of what's in here, but I don't know what model. There's a couple of items, so let's give it a go. And we have a postcard from Paderborn. Paderborn in Germany. That looks lovely. Look at that, really fits the wide screen just beautifully.

**Dave Jones:** Love it. All right, we've got a note. I got the note just now. Let's have a look. Aha. Bit dodgy. Bit dodgy. It's a, look at this. Wow. Sinclair Multimeter. DM2, check it out. Two-minute teardown, made in the old days. You bloody ripper.

**Dave Jones:** What else have we got here? It's a wacky wit. What's a wacky wit? It looks like a Pac-Man. I've got no idea what a wacky wit is. And it's a bag. Bag o' joys. What's a bag o' joys? Looks like we've got some toys.

**Dave Jones:** Oh, what? What? What? And Tim is sending this classic Sinclair. It's actually Sinclair Radionics, which is the original company name. DM2 Multimeter. What a clunker. Doesn't work apparently, so it's just a two-minute teardown. Comes with the original wall wart. And, oh goodness, look at that.

**Dave Jones:** Made in the old, serial number 28,395. Did they make that many of them or is that BS? Here we go. Let's crack it open. Oh, wow. How crusty is that? Are they serious? Look at the main filter cap just flapping around in the breeze.

**Dave Jones:** That's got to be a bodge. That cannot be production. Surely somebody has hacked, bodged that in. I mean, oh, wow. Seriously? Ever seen a battery snap that big? What a monster. And we have ourselves a date code. Look at that. 21st week, 1977.

**Dave Jones:** Thank you very much. That's the year Star Wars came out. Jesus. Plessy. Fantastic. Ah, original RCA chips. Ah, does it get any better? Wow. Look at the M205 fuse holder just hacked on the top of there. Ah, completely how you do it. And they've got all these crusty little carbon trimmers all in there as well.

**Dave Jones:** They're just awful little things. And that one over there, that's the front panel zero set control. Oh, wow. You wouldn't even bother fixing this thing. And input protection and cat rating. What's that? Actually, I can't find any info on the Plessy MP3202 there,

**Dave Jones:** which that's actually the same part number as a modern white lead driver. So that's all that's popping up on a first quick search. But there's our right angle display board, just four little seven segment displays in there. So that's obviously doing all the magic.

**Dave Jones:** Then we've got a CD RCA 4007 and an LM classic LM 3900 there. But apart from that, like, that's it. So thank you very much, Tim. That is one sad puppy, it really is. But, you know, I'm sure that they sold a few of them.

**Dave Jones:** People might have some fond memories of it, but I've got no nostalgia for that whatsoever, and I'm a bit of a multimeter aficionado. That's just, yeah, that's just pretty bad. Ugh, gives you the heebie-jeebies. As a lot of Sinclair stuff did, you know,

**Dave Jones:** really built down to a price and hacked together. And this wacky wit actually is a board game designed by a friend of his. And, yeah, it was like all handmade, so that's just unique. There's nothing electronic, there you go. I don't know, it's the wacky wit.

**Dave Jones:** And this is some sort of 1970s vintage laughing toy that's powered from just a, like a C cell battery. And look, what it looks like, you see all the ridges in there, that looks for all the world like a record. Like, you know, those grooves in there actually

**Dave Jones:** physically contain some sort of laugh track or something. And you can see that there is actually a needle, some sort of needle down in there that scans, that obviously can scan across the surface here. And then it looks like there's just a motor in there, that's it,

**Dave Jones:** and that's driven by the rubber ring around the outside. So it, that's, it's like a little miniature record player that obviously plays some laughing thing. Bizarre. There's the top cover off. What the, you know, like there's a speaker, right, so they're using that to amplify the thing.

**Dave Jones:** Wow, that is really something. Unbelievable. Anyway, I've measured the, I tried to get the motor going, but unfortunately the motor is blown. So yeah, we can't do anything. But there's a, like a 1970s electro-mechanical laughing toy. Bizarre. Next up, one from the old dart.

**Dave Jones:** Doesn't say who it's from, but it does say what's inside, or vaguely what's inside. Screw that, let's get the, let's get the big daddy out. And, come on, there we go. All right, now we're talking. So I think, that's some, man, we've got some black crud,

**Dave Jones:** which is going everywhere. That's what happens, the stuff deteriorates over time. Oh, oh, yeah, yeah, like that's not real leather. Oh, all the crud's just, yep, fallen off that. It's a, ah, worse than imitation leather. Sony, ha ha, look at that. It's a little mini-disc walkman.

**Dave Jones:** Sony mini-disc walkman with external, what, external control thingamabob. You know, you clip it up here, oh yeah, look at this. I've got my, ah, I've got the control for my mini-disc player. Awesome. And there's something else in here as well. Oh, yeah, yeah, we love these.

**Dave Jones:** FX 7000. Whoa, have we had the 7000GA on here before? I'm not entirely sure. But if we haven't, two-minute teardown. So Dave from the old dart actually knows nothing about electronics, but he watches it all the same. Thank you very much, that's fantastic.

**Dave Jones:** He's actually a software developer working on the Lego video games. There you go, I didn't know there were Lego video games. Apparently there are. Anyway, he sent an old calculator, a Casio FX 7000GA, one of the, you know, top-of-the-line graphene calculators. He used to use this in the 90s.

**Dave Jones:** I vaguely remember actually tearing down one of these. We've done so many teardowns, calculator teardowns on the mailbag, I actually forget. So I lusted after this one back in the day, never had it. I love the separate engineering key on it, the separate inverse key.

**Dave Jones:** Very nice. Some more buttons that you can poke a stick at. Brilliant. Let's take a look inside. I really like the battery cover under here for the three CR2032 batteries. Very nice, that's why it doesn't work. It's got no batteries. There you go, pretty typical of the day.

**Dave Jones:** There's our power switch in there. And this is going to have, well, it's an NEC part, so that's probably some custom thing. I don't think you'd even bother looking that puppy up. But anyway, yeah, not much in it at all. What's that? We've got some memory, have we?

**Dave Jones:** Yes, and LCD module. And Bob's your uncle. That's about it. Ceramic resonator for the oscillator there. We've got some bulk decoupling there for the, just so that it wouldn't lose contents and stuff when you took the batteries out. It'd keep going for a little bit.

**Dave Jones:** But that's about all she wrote. Nothing fancy-pantsy at all. And it's a rather interesting switch implementation, though. It looks like it's using a membrane with some carbon tracers on there and then pushing them together. Hmm, fascinating. Why did they go to that sort of effort?

**Dave Jones:** Wah, wah, wah, wah. With batteries in there, it's a loser. Don't know why. Dave's sending a postcard from the old Dart as well. This is taken just minutes away from his house, and yes, it does look like a pic from the 1980s. Look at those cars.

**Dave Jones:** Oh, anyone remember these? Minidisc Walkman. How long did the Minidisc last? Wouldn't have been long. Jeez, look at this puppy. And what's this plastic thingamabob on there? What the hell is that? Is that an external battery pack? Wah? Minidisc was going to take over the world, wasn't it?

**Dave Jones:** With its stunning fidelity. But that is quite a marvel of engineering, though, isn't it? I mean, is that our battery down in there? That looks like our battery right down in there. But, yeah, I mean, jeez, you know, they don't waste much volume, do they?

**Dave Jones:** Absolutely incredible. All the best stuff's made in Japan. Marty says so. Check it out. It still works. I plugged in the 1.5-volt battery, just a AA, into this clip on the end, and, oh, it just switched off. But it said, yeah, it popped up and said,

**Dave Jones:** no disc. But this puppy still goes. I wonder if it would read it. There we go. I wonder if it would read a disc. Probably. So I think that actually deserves more than a two-minute teardown. And, yes, I've still got a couple of classic Sony retro products to teardown.

**Dave Jones:** So, yeah, I'm going to add that. That'll be a trio of Sony classic teardowns. Thanks, Tim. And I've got to show this postcard, because it's from a 13-year-old viewer. Hi, ExplosiveKidMC. Doesn't say what his name is. He's a 13-year-old kid. He enjoys watching my videos,

**Dave Jones:** and this is a photo that he took of Teard in Tenerife. And he also enjoys electrical engineering and hopes I can feature the postcard in the mailbag. I can. Thank you very much, ExplosiveKidMC. Fantastic. I hope you blow some stuff up on your channel.

**Dave Jones:** I'll link it in down below. Check it out. Subscribe. Up and coming 13-year-old. Beauty. Next up, one from Slovakia. Don't get many from Slovakia. Hi to all my Slovakian viewers. This one's from Jonas Gruska. Gruska? Good on you, Jonas. Let's see what he's sent in.

**Dave Jones:** It just says it's a gift. So, I don't know. What does that mean? Could be anything. Let's have a look. All right. Slovakia. Never been to Slovakia. And again, I haven't been to many places. Oh, look. Oh. What? It's a, um, it's a mailer.

**Dave Jones:** Crispbread. Yummy. Thank you very much. I will try that out. We have a note. We have another note. In a bag. We have a two-minute tip. What on earth is that? Power. Gain. Oh, it's a, it's a funky, I reckon that's an audio, some sort of preamp or something,

**Dave Jones:** is it? Electro-sloosh. The LOM electro-sloosh. Pronouncing that incorrectly. Three. But it's jazzy. Look. Let's check it out. And here's the electro-sloosh, which Jonas has sent in. He's told me this actually, um, that's Slovak for electro-hearing. And check it out. Isn't it a neat little piece of, like, I don't know what that represents, but anyway, what

**Dave Jones:** it is, you'll notice that there's two inductors. Yes, they're actually inductors. They're not little microphones or anything. Two inductors on the front here. We've got a volume control. Ooh! There we go. It lights up. There we go. See the 9-volt battery in there.

**Dave Jones:** And it allows you to hear the electromagnetic, you know, interference. Like, you know, stuff that things are emitting and things like that. So it's got an audio jack output here. So we can just plug that in. I might see if I can actually plug that directly into the audio input of my camera and see

**Dave Jones:** if we can actually get something out of this thing. So here we go. I've got it plugged into the external mic input of my camcorder. And you can hear some noise there like that. And I'm mixing it with the internal mic. And I've got my headphones on so I can hear what's coming out of that.

**Dave Jones:** So that's just sitting there on the bench. Okay. But if I put it up to the LCD of my camcorder, listen to this. Listen to this. That's over different, I'm moving that over different parts of the LCD of my camcorder. Now I'm going to lift it up the top of my camcorder.

**Dave Jones:** I know you can't see this, but. Oh, listen to that. What's that? Oh, that is the, you can't see this, but this is hilarious. I'll get a second camera. Hang on. All right, here it is. Here's the LCD. As you can see, different parts of the LCD there.

**Dave Jones:** But listen to this. Tick, tick. Buzz, buzz, buzz. Look, it's the access LED there. That's what it's picking up. It's synchronized with that LED. So it's picking up the current pulses that are turning that access LED off and on. Fantastic. I love it.

**Dave Jones:** And this multimeter here, let's have a listen to it, right? Nothing at the moment. Switch it on. There we go. Listen to that. Terrific. And it's in stereo. That's fantastic. And if I turn the backlight on. Oh, there we go. Look, we can hear the backlighting.

**Dave Jones:** I presume backlight inverter, is it? But no, no, no, it wouldn't be. No, it wouldn't be. But, so I don't know exactly how he's translating stuff into audio. But anyway, it's just fun. It's a great tool. I love it. So I really like that.

**Dave Jones:** That's awesome, Jonas. That's a bunch of fun. And probably quite a useful tool. And I love the fact that it's stereo as well. So that's fantastic. And yes, it is open source hardware. So I'll provide links down to Low Weekend. It looks like you can pre-order it.

**Dave Jones:** So yeah, it may not be available right now, but will be available shortly. You can order one. Fantastic. Made in the EU as well. Fantastic. Awesome, Jonas. Thanks. Next up, this one's been here for a while. Sorry about that. It doesn't say who it's from, but, well, Sanford.

**Dave Jones:** First name? Last name? Company name? I don't know. From Arlington in the United States of America. So let's check it out. It's got one of these rippy things. I think it does. So let's have a look. There it is. It just contains a photo and a letter.

**Dave Jones:** Item 1. Ultrasonic receiver. So let's check it out. It's from Dave. There you go. Dave Sanford. Awesome. Thanks, Dave. Now Dave's actually an aerospace engineer and doesn't know much about EE. He's only done one course, but he's got a few questions regarding this ultrasonic receiver circuit, basically.

**Dave Jones:** Here it is. There's apparently a discrepancy between the breadboard photo and stuff used and what's actually in the book or something. So his questions are, can he use non-electrolytic ceramic disc capacitors for the circuit here? And the answer is yes, you most certainly can.

**Dave Jones:** There's a 6N8 here. That's just an AC coupling input there. Then with the AC coupling the second stage there, and then they're just bypassing, doing some high frequency bypassing there, and AC coupling the output. You most certainly can use ceramics in all those cases.

**Dave Jones:** And you can see they're actually used disc ceramics in there as well. So no dramas whatsoever there. And he was told that item number 2 is the 6N8 capacitor, that one there. And yes, it certainly looks like it because it's going directly in there.

**Dave Jones:** And there's the cap there. It's AC coupling the input. That's just a big poly cap on the input. You can use basically almost any type there. It shouldn't be a problem. And his third one is that he's been told that here's an inductor up here,

**Dave Jones:** and he doesn't know what that one's for because the inductor is not in the circuit. And does he agree that I need to include an inductor? Is it required? What type? And the number of henries, milli-henries, micro-henries, whatever. Henry is a massive amount of inductance.

**Dave Jones:** We generally don't deal in henries. We deal in millis and micros and nano-henries, basically. Just like capacitors, like one farad of capacitor. When I was a boy, you know, super caps and all that sort of thing. Yeah, a farad is a lot, just like a henry is a lot.

**Dave Jones:** So anyway, it doesn't matter. Does it need an inductor? Well, the only thing I could think of was that maybe the inductor would be used to bias. Maybe there's a link there, and it's used to actually in here, going up to the positive rail,

**Dave Jones:** and it's used to bias the ultrasonic receiver. But I don't think it needs it. I guess it might depend on what type of ultrasonic receiver you need. I believe that generally this should just work without any biasing coming up here from the rail.

**Dave Jones:** And that would be a typical use for an inductor, might be to, you know, supply that, and then you couple, you AC couple it off. That's very typical in terms of how to supply power to a device, whatever it happens to be, like any sort of transducer or receiver or whatever,

**Dave Jones:** and then you tap off the AC. So I've just drawn it in here. If you have an inductor there going up to the rail, then it can actually supply power to your device down here, whatever it is. But then your device, when it, you know, it could be having some modulation output or whatever it is,

**Dave Jones:** so this thing requires power and also provides modulation output as well. Well, you don't just want a wire going up to your positive rail, because then that's going to really hardwire it to the rail, and the modulation's not going to work. Whereas the inductor, the high-frequency modulation coming out of this thing

**Dave Jones:** can't get through the inductor, okay? So, because the inductor basically resists any high-frequency stuff. That's what it's designed to do, whereas the AC cap will bypass that. So that's a way to tap off modulation while providing power. So that's where something like an inductor, I think, would fit into this sort of scheme,

**Dave Jones:** but it depends on what you're using for this ultrasonic receiver. This just looks like a regular receiver, so just the regular AC coupling with no inductor there should, I believe, work. Um, so, yeah. Best way to find out is to build it up and actually try it,

**Dave Jones:** and you'll learn a lot if it doesn't work. I hope it doesn't work. Then you'll have to troubleshoot it. That's where the fun comes in and you learn stuff. Awesome. Your other question was, well, if you did need an inductor, what value would it be?

**Dave Jones:** Well, I'm not gonna tell you. It's better if you actually experiment. Try different values and see what works. But in this case, I think the... I don't think you need an inductor at all. I think it'll just, uh, the ultrasonic transducer out straight into your Arduino there.

**Dave Jones:** Should work a treat. So, yeah, I don't know what's going on in the photo there. This big electrolytic cap over here is just some bulk decoupling for the power rail. So just between ground and the, uh, 5 volt rail there. So it's not, um, yet shown on the circuit.

**Dave Jones:** And that's, you know, fairly typical. Next up, one from Denmark. Don't get many from Denmark. Hi to all my Danish viewers. This one's from, uh, Kaspen, um, Hulsgaard-Booch. Three names. There you go. Puts his middle name as well. Let's see... What he sent in.

**Dave Jones:** I assume it's a he. Sorry, just going by sheer statistics, really. Uh, only about 2% of my audience are female. So, you know, it's a fairly safe bet that it's a... If it's a name I haven't heard of, and then I'm gonna assume it's male.

**Dave Jones:** I'm gonna goof it one day. I probably have in the past. Let's have a look. Anyway, oh! Look at that. I got it right. Love the eevee... Love the eevee. I'm sending this little teardown. Alright. He's already... He's already had a look at it.

**Dave Jones:** He was quite amazed at the simplicity of the circuitry. Well, maybe we will be equally amazed at the simplicity of the circuitry. Ah. Nope. I'm sure that's just the box. Lego creator. Oh! Um, he's included a mandatory Lego set. For Sagan. Awesome. Thank you.

**Dave Jones:** Oh, it's a train. He's gonna love the train. Thank you very much. And it's a... thing. Thing. I don't know. I can see a piezo transducer on the front, and that's about it. Two minute teardown. So Casper's sent in this little teardown. It's one of these, um, yeah, panic alarm things.

**Dave Jones:** Uh, pull the chain at my own risk. I don't think so. I'm in a office environment here. There's people next door and things like that. I think I'll pull it. I'll tear it apart. Well, there it is. Not much doing at all. A bit fancy-pantsy.

**Dave Jones:** They've got a chip on board to drive the thing. A big-ass inductor there. And, um, just, this is the pin that, uh, drives it. We've got a couple of, uh, coin cell batteries down in there. And, uh, of course the pin, they've actually got like a normally,

**Dave Jones:** uh, closed socket. So when it's, you know, so it would activate it. So you push the, push the pin in like that and it, uh, of course opens the circuit so that when you're, you know, in a panic you just, ah, ah, pull it.

**Dave Jones:** And the screamer goes off. But, yeah, I don't think that's a particularly loud screamer. I mean, it just looks like a Joe Bloggs piezo ceramic. But, eh, it could be okay. But, yeah. Not much to it at all. Just a chip on board driver and,

**Dave Jones:** yep, Bob's your uncle. Alright, somebody's setting something for you. Say again. I'm going to put it in front of you. Keep your eyes closed. You ready? Check it out. Open them. Ah! I knew it was a mail set. I knew it was a mail bag.

**Dave Jones:** I knew it. And what is it? It's a train. It's a train Lego. You want to take it out? Yeah. Take it out. Ah, how do you open this? Ah. You have the tongue angle, right? We only got two packets. Yay! But there's lots of pieces.

**Dave Jones:** Mmm. Daddy, now we can start off building the train here. Now we can take it home and do the rest. Yeah, we can show Mummy when we get home. Or we can finish it here. Yeah. Good idea. Now, let's see. Let's start opening this packet first,

**Dave Jones:** Daddy. So thanks to everyone who sent in something to today's mail bag. Sorry if I haven't gotten around to yours already. Hope you enjoyed it. Comments, as always, down below. I think I'm going to try to create some music. Yeah. Catch you next time.
