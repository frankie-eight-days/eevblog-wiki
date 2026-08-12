---
video_id: FKC6lnTKH-c
title: EEVblog 1561 - µSupply USB Power Supply - Part 21
url: https://www.youtube.com/watch?v=FKC6lnTKH-c
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 32, "3": 45, "4": 57, "5": 70, "6": 88, "7": 103, "8": 117, "9": 142, "10": 158, "11": 170, "12": 192, "13": 204, "14": 218, "15": 231, "16": 240, "17": 253, "18": 266, "19": 276, "20": 291, "21": 306, "22": 320, "23": 329, "24": 339, "25": 355, "26": 377, "27": 389, "28": 401, "29": 410, "30": 421, "31": 447, "32": 456, "33": 469, "34": 478, "35": 490, "36": 507, "37": 516, "38": 530, "39": 540, "40": 552, "41": 565, "42": 580, "43": 593, "44": 604, "45": 612, "46": 628, "47": 639, "48": 657, "49": 670, "50": 681, "51": 689, "52": 699, "53": 716, "54": 729, "55": 744, "56": 753, "57": 767, "58": 776, "59": 788, "60": 801, "61": 820, "62": 838, "63": 848, "64": 855, "65": 862, "66": 870, "67": 885, "68": 895, "69": 905, "70": 919, "71": 929, "72": 942, "73": 954, "74": 967, "75": 976, "76": 993, "77": 1000, "78": 1010, "79": 1024, "80": 1039, "81": 1051, "82": 1075, "83": 1084, "84": 1093, "85": 1107, "86": 1128, "87": 1139, "88": 1152, "89": 1161, "90": 1176, "91": 1197, "92": 1209, "93": 1225, "94": 1232, "95": 1245, "96": 1258, "97": 1270, "98": 1282, "99": 1292, "100": 1303, "101": 1314, "102": 1321, "103": 1335, "104": 1341, "105": 1349, "106": 1359, "107": 1370, "108": 1379, "109": 1393, "110": 1403, "111": 1429, "112": 1441, "113": 1454, "114": 1472, "115": 1489, "116": 1502, "117": 1521, "118": 1530, "119": 1544, "120": 1570, "121": 1583, "122": 1600, "123": 1616, "124": 1626, "125": 1638, "126": 1649, "127": 1660, "128": 1673, "129": 1681, "130": 1692, "131": 1707, "132": 1730, "133": 1742, "134": 1752, "135": 1764, "136": 1774, "137": 1785, "138": 1803, "139": 1815, "140": 1827, "141": 1841, "142": 1851, "143": 1870, "144": 1886, "145": 1913, "146": 1931, "147": 1939, "148": 1949, "149": 1972, "150": 1982, "151": 1991, "152": 2001, "153": 2011, "154": 2020, "155": 2034, "156": 2048, "157": 2056, "158": 2069, "159": 2081, "160": 2093, "161": 2104, "162": 2122, "163": 2132, "164": 2139, "165": 2149, "166": 2167, "167": 2180, "168": 2192, "169": 2202, "170": 2211, "171": 2222, "172": 2231, "173": 2245, "174": 2257, "175": 2270, "176": 2277, "177": 2285, "178": 2305, "179": 2321, "180": 2332, "181": 2350, "182": 2366, "183": 2382, "184": 2389}
---

**Dave Jones:** Hi, or should I say hello? In fact, the micro supply says hello. Yes, I know it's been an incredibly long time. I still get constant emails and messages from people saying, "Hey, whatever happened to the micro supply?

**Dave Jones:** Are you ever going to finish it? Ever going to get back to it?" Well, I've here is part whatever. Actually, I don't really know what part of this. I think there's 15 official videos, but there's actually more than that cuz I did two videos on designing this custom LCD here.

**Dave Jones:** I'll link them all in. I'm pretty sure I done videos on like custom heat sinking and stuff like that, custom keyboard, keypad design. Anyway, I thought that I'd go back to it and revisit and show you where the micro supply actually got to.

**Dave Jones:** And yes, here it is here. It is a an actual functioning product and I do use it occasionally. It is quite funky. Look at this. It's got basically customized everything.

**Dave Jones:** It's got a customized case. It's got a customized keypad, customized LCD, which I've done a video on, customized planar transformer in here, which I don't think I've done a video on.

**Dave Jones:** It's got customized heat sink, customized connectors as well, believe it or not. I can do a teardown and show you this, but anyway, this is not necessarily an official restarting of the micro supply designs or continuation, but I'll show you where I got to and what its current status is.

**Dave Jones:** Right off the bat, no, you cannot buy this, okay? There were only a few of these prototypes made and they do actually work. So, you can actually see here.

**Dave Jones:** Here it is here. Boop. There it is. It's actually hooked up to a load and it's drawing 200 milliamps here. You can see the set voltage and set current are up the top here and then you've got the actual measured output voltage and the measured output current here.

**Dave Jones:** It's got a nice big customized hello here, but that can be used for all sorts of stuff and it's a pretty funky little thing. You can actually if we want to program the current up here for example, if we wanted to only go to say 100 milliamps like that, we could enter 100 milliamps and boom, it drops down to 100 milliamps and entered constant current mode down there.

**Dave Jones:** And yeah, it's a nice little supply. It does actually work. It's got USB C input over here like this, so we can power that on and there it is and we can jump right back in there and it automatically stored the milliamps up there.

**Dave Jones:** And one point it did actually have Skippy command interface working at one point I think, but I don't think this particular one actually is programmed with that at the moment.

**Dave Jones:** But anyway, it does look very cool and basically the story behind this is that of course David too when he was working for me was actually he was the one working on this project at the time and then when he left, we did like a handover of all the documentation and all the you know all the design files and everything.

**Dave Jones:** Still got a folder with all the stuff. I've got a giant tub with all the parts and everything all the miscellaneous parts and prototypes. And the thing was I just kind of like lost interest in it and went on with other things.

**Dave Jones:** Like as cool as this product is, I think it's very cool. I do think it's actually too limited and somewhat a product of its day. I would actually design it very differently today.

**Dave Jones:** And I'll actually take you through a quick go through of the design files of this thing, but I'll show you inside. Ta-da, this one actually I That's There's one of the There's your problem.

**Dave Jones:** Well, no, it's not actually a problem. There's There's one of the things, right? Believe it or not, that everything is custom in this. Like, that connector there banana plug interface is a custom interface like this.

**Dave Jones:** It wasn't soldered. This one wasn't soldered in there for some reason like that. But basically, yeah, we got the banana plugs are custom manufactured like this. We got the heat sink custom manufactured.

**Dave Jones:** This planar transformer here, that's a custom manufacturer. There's a top-down look at it there. Uh it's got dual processors. There's a secondary side one, and there's also a primary side processor as well.

**Dave Jones:** And you can see on the bottom, there's no components. It all was a top side load here. And the case had metal threaded inserts in it. Check that out, Bobby Dazzler.

**Dave Jones:** And it was just basically the big custom LCD on the bottom side there. And this is under the heat sink here. We've got two power transistors under here. And that was just the bottom side of the heat sink like that.

**Dave Jones:** Which, you know, was quite a nice little fit to envelope design like that, just to go over the top. And of course, the bottom had these holes spread over like that, so the air flow would actually run through and over the fins properly.

**Dave Jones:** This was pretty much was supposed to be the finished micro supply. Although, I do remember I don't recall absolute detail. Sorry, I haven't gone back through and extensively looked at the documentation and stuff like that.

**Dave Jones:** I just switched on the camera, thought I'd give you an update here. But I I do believe the final conclusion from David was that we probably should go away from the planar transformer.

**Dave Jones:** It wasn't as good as we thought it would be. Actually, I can show you an old prototype. We didn't always go with this custom planar transformer. Here, oh, I just noticed the date code.

**Dave Jones:** Is that really the 24th week, 2019? Wow. Here's an older uh, prototype, example, and we used, um, some off-the-shelf isolated, uh, converters cuz that's the one of the one of the things with the micro supply is that I wanted it to be fully isolated.

**Dave Jones:** And with hindsight, uh, that was probably not the best idea. It was quite nice, you know, to eliminate any, uh, ground issues, but in practice, most people are going to like use this with an external battery, uh, pack or something, you know, a power bank or they're going to hook it up to their laptop which isn't, you know, which is floating anyway as long as you don't plug in the mains connection.

**Dave Jones:** I've done a, you know, a whole thing on, uh, how to not blow up your oscilloscope, how to not blow up, uh, your computer and stuff like that. So, really, you you do pay a huge penalty for having the isolation.

**Dave Jones:** If I was to do this, if I was to release an actual product, I would just do away with the isolation. And also, uh, we paid a price cuz you got to have secondary side process, isolated side processing.

**Dave Jones:** Not only do you have to do the USB, uh, power delivery negotiation, which, by the way, is much easier these days. There are much easier solutions to do USB power delivery.

**Dave Jones:** Back then, it was harder. And you can check out the source code, by the way. It's been available on the GitHubs for, uh, ever since, uh, David left, I think.

**Dave Jones:** I actually released the, uh, software for this. So, yeah, we just ended up with like multiple processes and a really complicated USB power delivery, uh, solution, I believe. And like, it just wasn't, uh, God, you you know, you wouldn't believe the amount of effort that just went into the getting into the USB power delivery working, uh, for example, and then having processor isolation, and, you know, primary and secondary and

**Dave Jones:** stuff like that and getting the serial over and, you know, it's just it's just messy. I would have, um, if I was to release a public, uh, product, if I was to sell it, I would just ditch the isolation.

**Dave Jones:** I don't know. If you think it's important, please leave it in the comments, uh, down below. But at this stage, I have no intention of actually uh, going going ahead and finishing this to an actual sellable product, but you never say never.

**Dave Jones:** Anyway, so you can see this is our prototype 1.0. So, yeah, it's got a couple of bodges. I'm not sure what this battery budge here is. I don't know.

**Dave Jones:** He was maybe experimenting with, you know, putting a DC bias in some part of the circuit or something. So, that was basically version one, and you can see that we had a different solution for the banana jacks down here.

**Dave Jones:** For example, we had this little, you know, right-angled board with the pin headers and just used off-the-shelf stuff like that. Then, at some point, we decided it was better to actually design this custom thing cuz you can actually get little folded bits of metal like this actually custom manufactured real cheap.

**Dave Jones:** It's not much NRE on it, and it's, you know, the unit cost is, you know, not much at all in the scheme of things, but, you know, everything adds up.

**Dave Jones:** Just having everything custom on this, it it really adds up. Although, you know, as you see, it's like it's a real sexy final product. If you want a real sexy final product, you know, you've got to do custom stuff.

**Dave Jones:** So, I think most of the electronics is the same. You can see it looks very similar the power section over here. I can't actually remember details. I haven't actually looked at the schematic.

**Dave Jones:** We'll go later and have a look. So, you'll be seeing it fresh as will I after many years. But, yeah, we decided to cuz these were quite expensive the off-the-shelf isolated converters like this.

**Dave Jones:** So, we went for double to get twice the power output if memory serves me correctly. So, we thought we'd try this custom planar transformer down here, and I don't think it worked out as well as we expected.

**Dave Jones:** It worked, but it just it just didn't give the power envelope actually required. So, yeah, if I was to design this again, I'd just ditch all the isolation and then just have one processor instead of multiple processors.

**Dave Jones:** I'd change the USB power delivery thing wherever that is. And yeah, cuz there's much easier solutions for that these days. There's single chip solutions that are pre-programmed. You don't have to write any firmware, but just pre-programmed.

**Dave Jones:** Pin pin strap it. What what power level do you want and it'll do the power delivery negotiation for you and stuff like that. Whereas we we had to do it all from scratch back then in like 2018.

**Dave Jones:** Anyway, that's enough waffle on the hardware, but I hope you agree that is one sexy bit of kit. And one thing I really like is the LCD on this.

**Dave Jones:** I mean, it just looks absolutely like fantastic. Like, you know, big digits. It's got the separate programming ones up here. It's got, you know, a customized display down here and nice big annunciators on and you know, you can just see them.

**Dave Jones:** And it's got other annunciations. You can change, you know, to watt hour display and stuff like that. And David he absolutely insisted on having joules. So, cuz he's a joules fanboy.

**Dave Jones:** So, he absolutely insisted on having a joules capability. So, it's got that too. I don't know if it's programmed, but yeah. I actually I think it is. Then it's got different modes down here which you can set and set limits firmware 1.00 for example.

**Dave Jones:** Reset calibration and beep and reset enable and, you know, all sorts of functionality like that. It's got a lock function and a tab programming modes as well, but I don't think they were actually programmed in.

**Dave Jones:** So, but anyway, yeah, I love the LCD. I always thought about maybe designing like or just selling the LCD so that people can use it in its own in their own projects and stuff like that.

**Dave Jones:** Or maybe, you know, design like a little universal board for it so you can retrofit old product. Cuz the LCD is it's just I really like like of it.

**Dave Jones:** And it just looks beautiful. The contrast is excellent. Oh, it's Bobby Dazzler, thing of beauty, joy forever. All right, let's take a quick look at the schematic and the PCB to see what we've got here.

**Dave Jones:** Uh now, this is the top-level uh schematic here, and this is just the overall links in um other sheets here. So, we've got the LDO, we've got the pre-buck, I've got the USB um isolation, we've got the main micro part and the HMI, which is the human machine interface.

**Dave Jones:** Um and uh like a handy little note here about where the uh binding post uh came from. And as I mentioned uh they are actually a custom uh we got them custom machined, the post machined.

**Dave Jones:** Plus, we designed our own little um right-angley PCB connectory spring connector thing, which I believe doesn't need to be soldered. It can just be a press fit, but you know, if you if you want if you can, you can solder it for extra reliability.

**Dave Jones:** Like, we can go into the micro, for example, and so there's all sorts of stuff. Uh look, there's options up here. Did you key? Like, I have not looked at any of this for like over 3 years.

**Dave Jones:** Yeah, so this is the main micro, and uh we use an STM uh 32F072CA8T6 for those playing along at home. And uh yeah, another one of the reasons were was uh production, of course.

**Dave Jones:** Um you couldn't get the STM micros. They were like a lot of the parts became really hard to get for a long time. I believe that was one of them.

**Dave Jones:** Um so, yeah, we've got a I remember why we chose that particular STM micro, you know, they've got so many variations of it. Anyway, got some regulation here. Uh we've got an E-squared PROM.

**Dave Jones:** That's over on its own um schematic. There it is there. It's just that's the only thing on it. This was a thing at Altium. I didn't draw this uh by the way, this is uh David too uh doing this.

**Dave Jones:** But this was a thing at Altium, and And was in all the examples, and then everyone in the industry started to copy it. It was like, "Okay, you're going to put just the one E2PROM on the one sheet on the one schematic sheet." And then you treat it as a sheet, and then you do the modular thing like at the top level here, and then you put it there.

**Dave Jones:** Like, why couldn't you just put the E2PROM there? It was part of Altium's modular approach. You wouldn't have to design your own boards anymore. Altium, at one point, I kid you not, made the PCB tool optional extra.

**Dave Jones:** Oh. That didn't last long. But the whole idea was that everything in the future would be modular. And it would be, you know, you wouldn't have to lay out your own board cuz someone has already designed an E2PROM.

**Dave Jones:** Why would you have to design your own? Just drop it in. And And the layout's already done for you. Why would you have to lay out your own board?

**Dave Jones:** Just drop it in. And all these modular And it was all supposed to be the future of PCB design was supposed to be modular. And of course it never happened.

**Dave Jones:** So, if you see, there's a lot of people in the industry, yeah, we'll just put one sheet. And And Altium's to blame. Wasn't me, even though I worked there.

**Dave Jones:** I It's just just just don't blame me, okay? Yeah, so we've got the voltage set DAC and the ISET DAC here. So, we're using the external like the DAC output in the STM 32 cuz it's good enough.

**Dave Jones:** Like, this is not a hugely precision supply. The internal I can't remember. It's probably a 12-bit DAC. Specs aren't great, but good enough for Australia. So, that goes off to the regulation part.

**Dave Jones:** Right, so here's the USB isolation part. And we've got These are all different sheets. So, we can go in and have a look. So, I'm not sure what's It says rough simulation up here.

**Dave Jones:** Swap for P-channel JFET if this doesn't work. So, I'm not sure if this was part of the final one or whether or not he selectively left these out. And this this is a flyback option.

**Dave Jones:** So, I can't remember exactly what's what's doing there. Anyway, let's go into the USB sheet over here. Once again, there's a few notes down here. USB-C 5 volts, USB-BC 1.2.

**Dave Jones:** So, yeah, you've you've got to remember this is not a production-ready schematic. This is a prototype schematic. If we went into production, it would have been, you know, it would have been tidied up.

**Dave Jones:** And you can see how on the isolation side we used another STM micro here. This is the STM32F070. So, this is what we did the USB power delivery stuff in, I believe.

**Dave Jones:** And it was a huge stack. It was massive. Because at the time, as I said, there were I don't think there were any like like really easy to use off-the-shelf power delivery chips available.

**Dave Jones:** They came like a year or two later. And now I think there's plenty of them on the market, isn't there? Where you can just plug in the chip. As I said, you can strap a pin.

**Dave Jones:** And they're designed for use in simple products. But back then, like there was I think it was like 32K micro just to do just to hold the stack for doing the software stack for doing the power USB power delivery negotiation and everything else.

**Dave Jones:** It was provided by ST, but we had to massage it a lot. We had lots of issues with it and all sorts of things if memory serves me correctly.

**Dave Jones:** And it was, you know, but it worked. But jeez, no, I wouldn't wish it upon anyone. It was just it was just horrible to get USB power delivery working back in what 2018.

**Dave Jones:** Actually, we did use the RT1716. Let's have a look at that. Yeah, now it's all coming back. Yeah, we ended up using this Richtek job. I don't I think this was in the second revised one.

**Dave Jones:** I don't think we originally used this. But this does the hardware negotiation for this. But, you know, it's this is a relatively simple chip. Yeah, I think we ditched um the older solution.

**Dave Jones:** I don't have to pull up the older schematic. We found this easier solution. So, we actually redesigned it, I think, using this Richtek uh programmable USB-C uh PD controller, and it's just had an I²C interface.

**Dave Jones:** That's right. So, it went it was just simpler, but we still needed that um isolated side microcontroller in there. So, it's a much smaller uh device but then the main micro uh that drives the LCD and the keypad and drives all the uh DAC power supply functionality, but you needed something when you have isolated um supply like that, you need something on the isolated uh side to do

**Dave Jones:** the USB uh power delivery negotiation and stuff as well as um doing the serial comms cuz we had to we wanted to send serial back so you can do the skippy commands and the whole works.

**Dave Jones:** Yeah, so it looks like we ended up using that. Anyway, like each aspect of this design could be a video could be a 30-minute video in its own right.

**Dave Jones:** Uh so, uh sorry if I'm going to skip things. So, we just had a simple uh 3.3 V regulator there just to power the um local micro here. So, there's notes down here about use this uh SI233 part uh if ESR is problematic.

**Dave Jones:** This limits the voltage to 9 V. So, anyway, that's the VBUS. There's our USB uh connector there. So, we got a USB uh you know, comms and the uh CC1 and CC2 pins which go over uh to the uh controller interface that that uh Richtek uh controller over there for doing negotiation.

**Dave Jones:** Um and that's just uh some soft uh power um stuff. Then, we've just got a uh programming uh interface there. And pretty much that's all she wrote on that side.

**Dave Jones:** Although, uh no, we've got the UART isolation. Here Here you go. So, this is how we got the serial comms over. So, we just used this uh Skyworks here um 8641 low-power quad-channel digital um isolator.

**Dave Jones:** It didn't need to be too quick. You know, it's what's that? Oh, no. There you go. High speed 150 megabits per second. I don't think we needed that high.

**Dave Jones:** So, not sure why we used that one. Again, the choices have been they're documented somewhere. Probably have the documentation for it. So, basically we've got our microcontroller here. We've got our USB power delivery here.

**Dave Jones:** We've got just a USB input here. Programming header, local regulation and isolation and then here is our big isolated converter with our specific planar. This would be planar transformer and we've got a characteristic curve here.

**Dave Jones:** And you know, there's a couple of engineering notes in here. Change to 82k no difference for example. So, yeah, you know, David's obviously making notes in here as he was testing the thing.

**Dave Jones:** As I said, this is not a production schematic. So, yeah. We used an LMR 3481 switching converter here and the planar transformer that was a custom transformer. That number would have been generated by the manufacturer.

**Dave Jones:** I can't even remember who manufactured it off the top of my head, but we got it custom manufactured the planar transformer. We probably have the data sheet for that somewhere, I suspect.

**Dave Jones:** Oh, look, isn't that neat? I was just browsing through the directory here and I just found like an early 3D thing. We obviously didn't have the keypad in there at the time, but that was just an early concept.

**Dave Jones:** Cool, huh? And there's another one. Check it out. This is before we had settled on the keypad user interface. And and we were using off-the-shelf case here. So, you can see it like end cap.

**Dave Jones:** So, that I can't remember who manufactured that case, but you can get like the LCD cut out in there and it had would have had rails in there um, to slide it in and like to slide the PCB in and and it says, uh, 6 W up the top here.

**Dave Jones:** So, we used actually two of those, uh, 6 W isolated converters as you saw in one of those original, uh, prototypes there. But, yeah, we we never physically made, um, this interface.

**Dave Jones:** But, you know, we just went with the keypad one in the end. Once again, I can't remember why. This one would have been a bit, uh, smaller, um, form factor than what we've got.

**Dave Jones:** Same LCD. Um, the LCD design was settled like very early on and we didn't really change that. It was just, you know, there was several different design iterations with user interface type stuff.

**Dave Jones:** And we settled on the keypad. Let us know what you prefer. Do you think that we nailed it with the, uh, keypad, um, version that we've got now or would you prefer something a bit simpler like this?

**Dave Jones:** I kind of like the keypad one, you know, you could enter the numbers. But, I can see the simplicity of the up-down current thing. But, we just wanted a bit more versatility, I think.

**Dave Jones:** And, uh, then once we, uh, decided on that, then it pushed us into a custom case. And this is quite common in the design of products like this. It can, you know, especially when your your specs are flexible and things like that.

**Dave Jones:** You sort of, you know, it you make one change, you decide on one thing and it's sort of like pushes you, oh, we now we need a custom case.

**Dave Jones:** Oh, now I've got the custom case. Oh, we need a custom, you know, we can do a custom heat sink. And oh, we can do this other thing and we can do this thing and, you know, oh, we can add a bit more power.

**Dave Jones:** So, we'll do our, you know, our own isolated, uh, plan our transformer and like, you know, it just, yeah, it it it goes on and on. You can go down the rabbit hole.

**Dave Jones:** Anyway, let us know what you think. And that's just the, uh, full LCD. But, I've shown that in the LCD design video. I have no idea WHAT THAT IS.

**Dave Jones:** I I DON'T KNOW WHAT THAT IS. What the And then there's, uh, design notes and documentation like this. I found just, you know, found some random, uh, documents in here.

**Dave Jones:** Uh, clearly we're analyzing the amount of flash memory required for the version various things, the amount of SRAM, you know, the flash like we're going through different choices for the different micros there by looks of it.

**Dave Jones:** Yeah, so these were just like selective copy and paste from the data sheet into your own design document. That's a common technique just to like so you don't have to search through.

**Dave Jones:** You've got it all like if you take out extract the important stuff, copy and paste them out into your own design documents. And then obviously, you know, we're mucking around with this and and then there's other design random design analysis stuff, negative rail solutions for example, availability like you know, risk, total risk, total cost and things like that, you know, which is the lowest risk solution for generating a negative rail

**Dave Jones:** and stuff like that, you know, just little design things. Then just some notes on the efficiency of or the potential efficiency of various switching regulator chips for example. And some compensated uh, design notes.

**Dave Jones:** For example, if once again, yeah, I I won't go through them all but yeah, neat. You know, a lot of effort was put into, you know, various selection and design processes of all the stuff that went into this.

**Dave Jones:** And there's just a close-up photo of our custom planar transformer there. You can see the multi-layers in there. If you don't know what a planar transformer is, it's basically a PCB and it's a multi-layer PCB and these put the turns on flat on there on the multi-layer PCB and you get different thicknesses of copper.

**Dave Jones:** I've done a recent video on that. And yeah, you can do there's some efficiency advantages to planar transformers but basically a real low profile thing. That's one of the major advantages to the planar technique like this is you can get all those turns in a little nice smallish form factor.

**Dave Jones:** And before we physically built anything, we would do like 3D renders like this so we could, you know, really get a feel for it and we could, you know, pan it around and everything get a real feel for, you know, what it was going to look like.

**Dave Jones:** So, that looks like yeah, that's our finished that's our finished design is what we got. It's looks almost identical to what we got. Anyway, back to our main isolated switching converter here we've got a classic TL431 down here and then just a feedback opto-isolator here.

**Dave Jones:** It's you know, it's pretty much straight out of the LM 3481 data sheet I think you'll find and you know, that's where all you know, formulas and stuff come from perhaps.

**Dave Jones:** You know, once again go check out that follow along at home if you want modified set point 15.5 volts. All right, so we must have another tracking re-pre pre-buck there it is pre-buck.

**Dave Jones:** I mentioned that at the start didn't I? So, yes, this is the tracking pre-regulator which it means that you minimize or you keep a fixed voltage drop across your output pass transistor so you've got a known power dissipation which is why we could use a relatively small heatsink in there to you know, very low quite low profile heatsink doesn't need much square area at all because we're only

**Dave Jones:** dropping at most you know, a like two say two volts for example across the output pass transistors then at one amp you're only talking two watts for example which you could dissipate in that heatsink is much easier and here is the pot.

**Dave Jones:** Okay, here is the digital pot here and that's how we adjust it and yep, there we go. It's an AD5260 go and look that up for yourself. You'll find that's a digital pot not sure how many steps or whatever but yeah, that's often one of the easiest ways to do this sort of thing is to use a digital pot.

**Dave Jones:** It's more expensive like the the digital pots generally aren't that cheap especially like an analog devices one down there but it's just a nice analog way to do it cuz you're still in the analog uh domain here and it's just yeah, it's just easy.

**Dave Jones:** Oh yeah, there it is. The uh net over here is labeled 15 V. So, that switching uh that main isolated switching converter a fixed 15 V uh output there.

**Dave Jones:** I think we did actually investigate actually using that as the adjustable and getting that adjustable, but it was like it was just easier to use a um this is an AP5313.

**Dave Jones:** Huh, not recommended for new design. There you go, the AP3513. So, even if we went with that, it's obsoleted already. So, 18 V 3 amp synchronous uh buck uh converter.

**Dave Jones:** Yes, it's just the application circuit here and you just replace R1 here with one of those digital pots. Bob's your uncle, you can uh get your tracking pre-regulator easy peasy lemon squeezy.

**Dave Jones:** But, I guarantee you that part would not have been not recommended for new designs, which is effectively obsolete. Don't use it. Um unless you're like got an older product and then do a last buy or something like that.

**Dave Jones:** Buy all you can, cuz we're not going to make this sucker anymore. Um yeah, so that would that would not have been the case. When we designed this, that was only five less than five years ago.

**Dave Jones:** So, yeah, it's goneski. So, here's what you're all here to see, I suspect, is this LDO. What do we got here? Yeah, we've got a whole bunch of uh design notes.

**Dave Jones:** I out V sense, okay. So, we've got two output pass transistors here. They are the same NTD2955. Couldn't tell you why we selected that. It might be one in one of the design uh note documents here.

**Dave Jones:** We've got a 1 ohm current shunt resistor here, then just a differential amplifier. I think in the previous version, we tried to get away with something much simpler uh than an OPA4 like we'll say trying to save like every cent on the cost and I can like yeah, anyway, we we went with uh just like a regular op amp um here.

**Dave Jones:** This is not a differential like a proper current shunt like high side current shunt op amps. Just an op amp. Yeah, it's nothing special about that at all. It's just a 10 meg rail-to-rail automotive grade op amp.

**Dave Jones:** So, yeah, no, we decided I guess for cost reasons not to go with a like a proper like a high side differential cuz this is a high side. It's not in the low side.

**Dave Jones:** If it was low side, it would be Where's Where's Where's your ground? Where's your ground pin? Where's your output ground pin? It's not there. It must be on another sheet.

**Dave Jones:** But yeah, it would be on the low side which on the ground terminal. So, that would be low side current sensing. This is be This would be what you've what you'll call high side current sensing.

**Dave Jones:** So, if you're after a like a differential a proper differential amp to do this, then you're going to be looking for high side current sense amplifiers. But, we just used an op amp there.

**Dave Jones:** No worries. Does the job. So, obviously, this here is all part of our of our current regulation circuit. So, we've got current regulation So, this is our current regulation pass transistor and this is our voltage regulation pass transistor.

**Dave Jones:** And if we're not in current limit mode, of course, this is just like basically a short circuit. It goes straight through. And then this transistor here is the one that's limiting your output voltage here.

**Dave Jones:** And once again, I could do a whole video on the design of this thing, but I believe that looks like our final Yeah, that looks like our final output stage here.

**Dave Jones:** Do we Oh, yeah. Okay. No, we didn't reuse that. That's a different op amp. That's a OPA2180. That was an OPA4172. Oh, there's the 4172 again. So, a 4172 OPA2180.

**Dave Jones:** So, we're using 2180 there and there and this one there, there, and there. I'm not sure what's going on. Oh, and up here as well. So, that that's a quad jobby by the looks of it.

**Dave Jones:** No, the 72 on the end. No, is that it? Just a dual. Whatever. So, anyway, you can knock yourself out analyzing that if you like. We've got the formula there for getting the output current there and it's just a standard configuration for the output voltage drive here.

**Dave Jones:** We've got a TVS on the output. We've got a PTC for protection. Not a huge amount and this is just tapping off. That'll be going over to the microcontroller to you know, when you saw 12.01 volts on there, that's where it's getting from.

**Dave Jones:** It's just tapping it off there. And that's about all she wrote. Oh, and then I forgot down here to know if we're in constant current or constant voltage mode hardware-wise so the micro could tell if you know, if we're in constant voltage or constant current, there's a dedicated circuit there LM 321 just a comparator here and it just knows which one and then signals the micro there.

**Dave Jones:** So, yeah, that is just power for the op amps and so there it is. That's the output circuit. Once again, you can make it simpler than that. Once again, I couldn't tell you the exact design decisions, but this has changed a lot over the years, especially in my Hands up.

**Dave Jones:** Who wants to see a video? I've got them right here actually. I've had them sitting out for ages. So, I'm probably going to do the video, but leave it in the comments down below cuz I may not get around to it.

**Dave Jones:** So, kick me up the backside if you want to see the whole history of every I think I've got every micro supply prototype I've ever done. There's like half a dozen of them all through the years.

**Dave Jones:** This project has been going on before I did the before I started the EV look. That's how long ago. I can remember when I had the first prototype. I was working at Altium at the time and Leo Simpson, the then editor of Silicon Chip magazine, he was visiting Altium for some reason.

**Dave Jones:** Just dropped in to say hi. I don't know. And chew the fat. No idea. Anyway, he knew that I was working there. So, he dropped by my cubicle. Found out where my cubicle was.

**Dave Jones:** Dropped by my cubicle, said hi. And and I happen to have my original micro supply prototype. Because this is before the blog. I was thinking about, you know, publish it in Silicon Chip magazine.

**Dave Jones:** I go, "Hey Leo, check this out." And he And he really loved it. He thought it was an absolutely fantastic idea. It fitted in the Giffy box just like the micro current.

**Dave Jones:** Fitted in the same Giffy box as my micro current. And he And it had knobs and a lead and jewel lead displays on it, I think it was. And he just loved the idea.

**Dave Jones:** And yeah, so but I never got around to finish I changed the design a couple of times. And I never got around to publish it in Silicon Chip magazine.

**Dave Jones:** So, I don't know. But he thought it was fantastic. He was desperately waiting me for me to finish it off and write the article because he loved the look of and just the idea of a USB micro supply.

**Dave Jones:** There it is. Back in 2009, that was. 2009 and then it upgraded to 2010. So, thumbs up. Comment down below if you want to see a video looking through all of the different history of the thing.

**Dave Jones:** So, yeah, this is just a really this just been a fun hobby project of mine. And it almost made it, but I'll anyway, I'll tell you about that at the end.

**Dave Jones:** Would you like to see just a quick look at the PCB here? So, here's just a 3D version of that. But you've seen the thing in real life. So, it looked pretty you know, it was pretty spot on.

**Dave Jones:** Actually. Yeah. That looks pretty good, doesn't it? And it's a four-layer board, obviously, and you can see the layout here. It's, you know, not much to it, really. What can I say?

**Dave Jones:** Um, yeah, we've got a split plane in there, obviously. So, there's our component side, uh, internal power supply, plane there, just separating them internal ground plane so that we're physically, uh, separate.

**Dave Jones:** And just bottom side there. In fact, there's hardly any traces at all on the bottom side. It's all going over to the LCD there. Oh, yeah, I forgot to show you the, uh, LCD.

**Dave Jones:** Um, human-machine interface, is it? Human-machine interface. There we go. So, there you go. That LCD had, uh, eight, uh, commons there. And however, 31, uh, segments. And a HT, uh, 1622, uh, LCD driver.

**Dave Jones:** I think we, yeah, we couldn't find the ST, some ST micros, of course, have built-in LCD drivers, but we couldn't get it. Um, or it didn't, or it increased the cost too much, and it was cheaper to get a separate chip.

**Dave Jones:** So, I'll look that one up. So, that was just a Holtek jobby. Holtek's one of, you know, they make their own micros, of course, and they make LCD drivers.

**Dave Jones:** And, you know, they're, they're pretty cheap. I don't know exactly, uh, the cost of that, but, yeah, um, it supported 32 seg, yeah, it supported 32 segments, 1622 with eight, uh, commons.

**Dave Jones:** So, we practically maxed out, uh, that whole thing. So, yeah, it was just, uh, cheaper and more betterer just to get a separate LCD controller. Cuz then you weren't really constrained with, uh, the ST micro, or your microcontroller's selection then if you try and get it, uh, built in.

**Dave Jones:** Sometimes you win with that, but this required a lot of segments, lot of commons. Like, it was, you know, quite a complex, uh, LCD on this thing. So, yeah, it was probably a no-brainer at the time for us to go to, uh, the external LCD controller.

**Dave Jones:** So, there you have it. I hope you enjoyed that, uh, update of the micro supply there. Um, yeah, as I said, at this stage I have no intention of actually releasing this as a finalized product.

**Dave Jones:** You might get to today, you know, the the meme. Just, you know, shut up and take my money kind of meme. I don't know, leave it down below if you want to shut up me to shut up and take my money.

**Dave Jones:** But I I look, I wouldn't I wouldn't go ahead with manufacturing this. I think these days it like there are portable power supplies now. Back when I was doing this, nothing existed.

**Dave Jones:** There was no such thing as a USB like a portable power supply. Now there's a few on the market. I still think this is like this is by far the coolest looking one.

**Dave Jones:** But I think with the isolation in there, I probably like we could get the bill of materials cost down cuz the bill of materials cost was getting quite high on this one.

**Dave Jones:** I was getting concerned that it was missing the market segment with the you know, the multiplier I had to add on it and everything else. I thought, you know, it was like would people pay like a real premium for this thing or is price more important?

**Dave Jones:** Once again, leave it in the comments down below. Would you pay anything for this or would you go oh no, I don't I don't I'd only pay 50 bucks or I'd only pay 100 bucks or whatever, you know.

**Dave Jones:** And by adding like a whole bunch of stuff, it all starts adding up. So yeah, if I was going to go ahead with this, as I said, I'd probably just drop the isolation and just have a simple USB solution chip.

**Dave Jones:** Although that one we had was you know, it was it's fairly decent. You just have to send it some I squared C commands and that's and Bob's your uncle, I think.

**Dave Jones:** But as I said, there's even simpler ones now which like just a I think you know, like an eight pin dip or something off off hand I couldn't tell you the number.

**Dave Jones:** Leave it in once again, leave it down below if you know of a good one. Where you just like pin strap the thing. They're designed for ultra simple products that are powered from USB and you just you know, all it does is negotiate like you strap the pin and say I want 20 watts or whatever or whatever the you know, whatever USB standard you want, and it just negotiates the highest

**Dave Jones:** one up to that depending on the capability of the supply that you actually plug into the thing. And um yeah, and then it just simply supplies that. And then I just have a um you know, a there's even easier solutions for tracking pre-regulators uh these days and stuff like that.

**Dave Jones:** Might make it entirely switching. I might go with a simpler um output stage than, you know, the than the one we the LDO stage that we done and did here because this is like quite a low noise uh ones.

**Dave Jones:** You might not worry about low noise. You can make it cheaper, and you can have just a switching uh pre what a switching a complete switching solution. Really, there are solutions out there um that, you know, you don't have to, you know, you don't have to muck around as much as we've done here.

**Dave Jones:** So, you know, you can really cost optimize those ones. All those cheap power supplies out there these days, you know, they don't go to town like this, right? They They're much cheaper, much simpler, and you just let uh who cares if it's got a bit of noise on it, you know, she'll be right.

**Dave Jones:** Um I'd rather have the lower cost and the simplicity. Anyway, let us know your thoughts down below about the micro supply. Hope you enjoyed the update, and uh if you did, if you enjoyed this video and you want me to make more on the continue the micro supply series in whatever form, please.

**Dave Jones:** Or if you want more detailed stuff on something that I've done here, let us know in the comments down below. If you liked it, give it a big thumbs up.

**Dave Jones:** Discuss down below EV Blog Forum, you know the drill. Catch you next time.
