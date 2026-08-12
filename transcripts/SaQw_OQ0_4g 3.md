---
video_id: SaQw_OQ0_4g
title: EEVblog 1538 - NEW PROJECT Part 2 - Microcontroller Selection
url: https://www.youtube.com/watch?v=SaQw_OQ0_4g
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 48, "4": 62, "5": 73, "6": 90, "7": 105, "8": 121, "9": 135, "10": 150, "11": 165, "12": 178, "13": 197, "14": 210, "15": 227, "16": 238, "17": 251, "18": 268, "19": 283, "20": 297, "21": 309, "22": 322, "23": 338, "24": 351, "25": 368, "26": 382, "27": 396, "28": 417, "29": 430, "30": 452, "31": 470, "32": 488, "33": 506, "34": 528, "35": 547, "36": 570, "37": 581, "38": 594, "39": 608, "40": 620, "41": 633, "42": 647, "43": 658, "44": 675, "45": 688, "46": 702, "47": 717, "48": 734, "49": 751, "50": 772, "51": 791, "52": 805, "53": 819, "54": 835, "55": 849, "56": 862, "57": 880, "58": 895, "59": 912, "60": 924, "61": 939, "62": 952, "63": 966, "64": 983, "65": 995, "66": 1008, "67": 1024, "68": 1042, "69": 1057, "70": 1073, "71": 1087, "72": 1101, "73": 1117, "74": 1133, "75": 1153, "76": 1169, "77": 1185, "78": 1197, "79": 1210, "80": 1225, "81": 1238, "82": 1250, "83": 1267, "84": 1284, "85": 1296, "86": 1308, "87": 1323, "88": 1340, "89": 1357, "90": 1371, "91": 1390, "92": 1404, "93": 1418, "94": 1436, "95": 1453, "96": 1465, "97": 1485, "98": 1499, "99": 1512, "100": 1525, "101": 1538, "102": 1551}
---

**Dave Jones:** Hi, it's new project time again, and today I'm looking for a microcontroller. I'm pretty microcontroller agnostic. I don't care which one I use as long as it meets several requirements that I have. Now, the requirements that I have are A,

**Dave Jones:** it's got to be low power cuz I'm targeting a really low power single battery design. So, we're talking like a year battery life kind of stuff, right? We're talking like really low power. Two, it's got to have an LCD controller

**Dave Jones:** built in. Up to I think 73 at current count, 73 segments. So, it's got to support, you know, a reasonably complex LCD built in. I could use an external LCD controller, of course, but that's an extra bomb item, extra cost, everything

**Dave Jones:** else. Nicer if it's built into the microcontroller, but if I can't get a suitable microcontroller with the number of LCD driver segments built in, columns or rows, haven't figured out my columns and rows yet. I've done an LCD design video,

**Dave Jones:** which I'll link in if you haven't seen it, how to design your own custom LCD, and I'll be doing that again for this project as well. So, you can probably see that in the future. So, it's got to

**Dave Jones:** drive up to, you know, over 70 LCD segments, and the third major requirement is actually multiple 32-bit timers, internal timers. Now, this doesn't necessarily mean I have to go to a 32-bit microcontroller. You know, everyone's going to go, "Oh,

**Dave Jones:** today just use a micro and code it and blah blah." Okay, right. And you don't you can possibly even there might I don't know offhand if there's an 8-bit micro with a 32-bit timer built in. Usually you don't get a 32-bit timer in

**Dave Jones:** a microcontroller unless that like it's a dedicated 32-bit micro, perhaps, but usually you'll get like maybe a 16-bit timer, and often you can actually cascade the two of those uh together to give you a 32-bit uh timer. So, you

**Dave Jones:** know, multiple 16-bit uh timers is okay as long as they are cascade-able. Uh and then you've got uh prescalers and stuff like that. We might go into that other um things to do with the timer. So, I want two high-resolution timers uh

**Dave Jones:** hardware timers uh to do some dedicated counting and it it won't fit the count thing that I'm counting won't uh fit in 16 bits. So, I really need that uh 32-bit uh count. So, uh you know, there's ways to get around like if

**Dave Jones:** you've only got a 16-bit counter, there's ways to get around it. But nah, no. I just want like a 32-bit timer. So, I've I can't remember the last time I needed a 32-bit timer in a microcontroller. It may be never. Um

**Dave Jones:** I wouldn't say that, but yeah, I I can't remember the last time. I think I cascaded two uh 16-bit timers. I don't think I've ever used an actual dedicated hardware 32-bit timer. Now, when I first think of a microcontroller that has LCD

**Dave Jones:** and ultra low power, I'm thinking of uh the TI MSP430, of course, absolute classic. Um I'm also thinking of uh the PIC uh 24F uh series, for example, which I've used before in many projects and stuff. Maybe even the PIC32 series, but

**Dave Jones:** I think I'd I'd be surprised if I couldn't find something in like a PIC uh 16 uh series cuz I'm pretty sure the PIC 16 series from memory has uh cascade-able 16-bit uh timers in it, but I don't know if any uh 8-bit uh micro

**Dave Jones:** actually, you know, the 8-bit PICs or or whatever actually have a um multiple cascade-able 16-bit timers can't off offhand. Uh Rusty old memory, I don't actually remember. So, we're going to do some parametric searching today to see if we can find it. Now, I'm open to

**Dave Jones:** pretty much any brand uh micro, but I don't want overkill. It's not going to be running fast. It's probably only to be running at a megahertz or something like that, right? So, not fast um at all, but I want it to be low power. So,

**Dave Jones:** any low power sleep modes, any sort of, you know, um any funky like LCD uh like low power LCD stuff and other things are built in. That'd be really nice. So, uh going to go to Digi-Key here. I'm in the

**Dave Jones:** microcontroller section and basically one of the uh things because one of the main requirements is that 32-bit timer, um I'm just looking through the parametric search here and it might show none of them even show timer, right? It's not a thing that they have in the

**Dave Jones:** parametric search and certainly not um you know, telling you whether or not it's like 32-bit capable. So, really um you know, you're like in search for LCD, like you can get ones for that have LCD and stuff like that and then you can't

**Dave Jones:** separate these. So, it's yeah, it's pretty much useless. Um in fact, totally useless. Let's go to Mouser um and see if they're any better. Um they separate them into uh 16 bits, so we can go into 16-bit micros here.

**Dave Jones:** For example, uh cuz you stand more of a chance to get your uh timer. Now, let's see what peripherals, you know, ADC and stuff like that, right? Um and I number of I/O pins. I don't need many I/O pins

**Dave Jones:** apart from all the pins required, of course, for the uh LCD. Of course, I don't need 70 uh plus pins for the LCD cuz the LCD will be multiplexed. It'll have uh commons and um lines as well. So, I could easily get away with like a

**Dave Jones:** 44-pin quad flat pack or something like that. Um and memory and memory and uh RAM really doesn't matter. Um this is not a complicated uh project application which I've got in mind here. So, yeah, I you know, a few K of memory is probably

**Dave Jones:** enough, really. But yeah, we got absolutely nothing here in uh the parametric search for that. I I go try, you know, Element 14 and all the rest of it, but but nah. Nah, it This is the kind of thing when you're searching for

**Dave Jones:** specific individual peripherals like this and they're important in your parametric searches, you really do want to go straight to the manufacturer's website. But hey, but this is 2023. Let's ask Chat GPT. Let's see if Chat GPT version 4 knows.

**Dave Jones:** Of course, it doesn't have like live data like recent, but you know, a couple of year-old data is fine. List all the microcontrollers that have internal 32-bit timers. Let's Let's give it a go. There are many microcontrollers available on the market with internal

**Dave Jones:** 32-bit timers. While it's difficult to list every single one, here are some of the more popular controllers that have internal 32-bit timers. The STM32 um Cortex. Yeah, like it's that's um Cortex is overkill. Well, it may not be. Um

**Dave Jones:** PIC32 series. Yeah, the MIPS core by Microchip. Yep, particular examples. So, Chat GPT knows the Tiva C series by TI. Um the NXP LPC series, the Atmel SAM series, which is another Cortex. Expressive and Tensilica. Okay, Renesas. Um ARM Cortex cores. Silicon

**Dave Jones:** Labs EFM32. Is that That's the Gecko or is the Gecko the smaller series? I can never remember. Um Infineon, Cypress. Keep in mind that this is not exhaustive and there are many other microcontrollers that that feature 30 additional new microcontrollers being

**Dave Jones:** developed. Yeah, I'll ask it specifically, are there any 8-bit microcontrollers with internal 32-bit timers? Yes, there are 8-bit microcontrollers with internal 32-bit timers. Although less common than they with 32-bit timers, few include Atmel ATmega series. Really? ATmega64, 128. They've got a 32-bit counter timer?

**Dave Jones:** Do they? I didn't know that. PIC18 series. Oh, okay. They've got have 8-bit architecture and offer a 32-bit timer. Chat GPT-4 is slow. Thank you. I will review the data sheet cuz I didn't think that the ATmega 128

**Dave Jones:** had a 32-bit timer in it. Two 8-bit timers with separate prescalers and compare modes to expand a 16-bit time counters to separate prescaler compare modes and compare modes. Okay, you might be able to join those two expanded 16-bit time

**Dave Jones:** counters. I I don't think I've ever I've only used like an Atmel once or twice at the microcontroller level and I don't recall having to use the 16-bit timer in it. So, yeah, I'm not really seeing the 32-bit. Can we do 32-bit?

**Dave Jones:** Uh AB instructions are 32-bits wide. No, there's nothing else in there. 32-bit No, 32-bit 32-bit instruction, 32-bit ID register No. No, there's nothing about using the timer as a 32-bit timer. So, the AI is wrong. And let's try this uh

**Dave Jones:** PIC 18 uh 18F25K40. Geez, could they make it more more convoluted? It's got a watchdog timer, three 8-bit timers, four 16-bit timers. Okay, but can we do can they be cascaded as 32-bit timers? Hardware ti- hardware limit timer, hardware

**Dave Jones:** monitoring fault detection, cool bananas. 8-bit uh precharge time No, that's for the uh capacitive touch. Oscillator startup timer, four 16-bit timers. Search for 32-bit. No, 32-bit 32 result 32-bit Okay, it's got a hardware multiplier. Uh wow, really? In the 18F series, didn't know that. Uh

**Dave Jones:** no, no, I didn't really just just the multiplier result, that's it. I It's not related to the timer, I don't think. So, yeah, nah. So, we're probably going to have to go to like a up it to a 16-bit.

**Dave Jones:** But, as I said, once you're after specific requirements for something like a timer like that, um you really need to go to the manufacturers uh parametric search. So, uh let's go to TI here. So, let's view all products.

**Dave Jones:** And does this give us the parametric search? It does. It does. And we can filter all filters over here. Timers, 16-bit. There you go. I was going to look under peripherals, but uh no, it's they've got a separate thing down here.

**Dave Jones:** Cuz I know Oh, they have up to six. Okay. So, there you go. You want at least two Let Let's say four timers. 4 16-bit. Looks like we're only going to get 16-bit timers, as I suspected. Uh as

**Dave Jones:** my memory uh served me correctly. We can go across here. 16-bit timers. There you go. Sorry, my head's in the way, but you can see that that column there, we can get five or six timers. That's pretty groovy. Uh 16-bit

**Dave Jones:** timers. And I'm pretty sure that they can be uh cascaded to a 32-bit timer. Six 16-bit timers with up to seven capture compare registers. A 32-bit CRC. That's pretty groovy. No, it looks like we'd have to go to the timer section to

**Dave Jones:** actually uh figure to actually see it. Sometimes you know Well, I'm not going to I'm not getting it on a keyword uh search. They certainly don't tell you at the top level of the data sheet, which is not very handy is, but I'm pretty

**Dave Jones:** sure from memory the MSP430 timer can uh be cascaded. Let's have a look. Timer B. So, there's your timers down there. Seven capture compare registers. Uh looks like it's got internal external as well. Timer A, timer B, input. And then

**Dave Jones:** you start getting into the complexities as we might look at of the internal architecture of the timers and where it can get its clocks from and prescalers and all sorts of things like that. So, it gets messy, but I'm

**Dave Jones:** I'm pretty sure anyway, without getting bogged down in the the details, I'm pretty sure you can cascade these 16-bit timers in here to do 32-bit, but maybe not this one. This is an ultrasonic sensing for water metering applications. I

**Dave Jones:** It looks like they've got you'd probably have to choose the like the specific one. Okay, so yeah, no, okay. Let's I certainly wouldn't rule that out, but let's go over to Microchip and see what they've got. Now, let's explore these

**Dave Jones:** 16-bit micros here. And which I've used before. Uh, product selection guide, that's what we want. Is that our parametric search? No, it's PDF. Ah, clocks and timers. There you go, 16 32-bit there, and they've all got them. They've

**Dave Jones:** all got them. The entire PIC19 range. I thought they had more than that. Uh, timers. General purpose 16 32-bit timer with compare capability. Yep, that looks pretty groovy. But I also want one with segment um LCD as well. So, what I

**Dave Jones:** actually want is the segment LCD over here. Is that How does that work? Does that That That doesn't click. It's broken. What? Graphics LCD? What? It's broken. Anyway, uh, we've got the LCD segments. So, we can have up to 200 like we get

**Dave Jones:** That's plenty. 256 is absolutely plenty. So, let's go look at a PIC24F uh, the GL30X. That's the GL family low pin count value line. Segment LCD USB I don't need USB. Don't need any of that. Uh, comparators. Um,

**Dave Jones:** no, don't really need comparators. Uh, and these are all extra low power. Oh, hello. Feature core independent peripheral LCD with autonomous animation. I need that. It allows you to like toggle between different states. Like if you've got a

**Dave Jones:** clock or something, it it flashes and it looks like you can do that in the LCD module. You don't have to do that in code. I'm sold. I'm sold. Um hats off to Microchip marketing. I don't know how you would find that. Let us

**Dave Jones:** know. Leave in the comments down below if any other micros with LCD capability have this um autonomous animation thing. Most display applications involve a few common animations like blinking periodically alternating between displays and blanking the pixels by using the integrated LCD drive with

**Dave Jones:** autonomous animation you can offload most of these animation routines from the CPU. This allows you to to enable animation in power saving modes while the CPU is in those idle or sleep modes. Perfect. This is exactly what I want.

**Dave Jones:** Like you flash things off and on. And you can actually switch between I wonder if they've got like a mapping for two entire displays. And you can actually it looks like you can presumably however many segments you got, you know, your

**Dave Jones:** 256 segments that it has dual mapping and it'll just automatically switch between those. So you load up both memory maps with the info you want and it can just toggle between them. Wow. I'm sold. Hang on. I might be sold further.

**Dave Jones:** Quickly design a display interface with MPLAB Code Configurator. MCC reduce your display design time to minimize the help of MCC eliminates the meticulous and time-consuming task of mapping the pins and segments. Allows you to import display icons. Ah,

**Dave Jones:** I am sold. Ding-a-ling, winner winner chicken dinner. Um I I'm I'm going to stop looking now. I'm going to stop looking. I'm I am sold. Ultra low power, ultra sleep. Yeah, cuz battery friendly. Also, we've got it it meets the requirements.

**Dave Jones:** It's ultra low power. Oh, by the way, I forgot it'd be nice if it also had an internal real-time clock um as well with an external watch crystal as well so that it can keep the time. That would be nice. I can always

**Dave Jones:** use an external chip for that. That's not a deal breaker, but I'm I'm sold. I haven't used this configurator thing. Learn more about the MCC. It looks like it's not Okay, code configure. Yeah, no, I I think I might have touched on this

**Dave Jones:** before, but yeah, I haven't used the LCD one. It does other things, not just LCD. And then it'll have different peripheral stuff that allows you just a nice GUI interface that allows you to actually configure everything. And one of the

**Dave Jones:** annoying things about LCD designs is actually as they said, mapping those segments in, especially if you're multiplexing the displays. If that takes care of all that, you save save a day's work just digging around with that. So GL302

**Dave Jones:** segment LCDs are 42. 42 segments, that's not enough. 80 will cover it. I don't need 64K of memory, but you know, that's that's what you end up with, right? 36 pin count, right? So it can map 80 segments, so that's low that's low pin

**Dave Jones:** count. No USB, don't need it. It looks like No, it looks like they've got more devices. Why why can't you show me the whole lot? View all parameters. They keep changing that. Oh, this is Oh, this has got one of these jazzy thingamabobs.

**Dave Jones:** Okay, there's nine parts in this series, so you know, it's not like the configurator is a huge amount of help. Actually, let's go up here. We want a minimum 71.5. 75. I think I might be able to get away

**Dave Jones:** with 75. I really don't want like hundreds of segments, so let's like narrow the range like that. We got No, we're still got nine parts. What? And pricing, not too concerned about pricing, but might as well go for like the cheapest $1.90. 24

**Dave Jones:** FJ128GL303. It's got 80 segments, which is enough. And no no USB interface, that's fine. Don't care about ADCs. Pin count, 36. 36 pin jobbie. 8K of RAM. And and tons. It looks like it's that one. That's a winner winner chicken

**Dave Jones:** dinner. Let's look at the 24 FJ64GL303. Can we actually buy that? Can we buy it? First thing you do before you design the PCB, pro tip, before you design the PCB, order your parts. Make sure you can get them.

**Dave Jones:** Search. I've had this problem. Digikey like just takes forever. Give me bloody Mouser. 630 in stock, two bucks 90 one off, 340, no stock of that one. Woah. Yeah, I'm not going to design in one that's only got those so you know, I

**Dave Jones:** want like 10,000 in stock, please. Not that I plan on making 10,000, but you know, it's it's the vibe. What I'm going to do is I'm going to expand it a bit so that I can get more of a selection of parts

**Dave Jones:** cuz maybe the higher pin count jobbies are going to be better. Look, if I just search for the 64GL, let's just search for that and don't worry about the ones afterwards. There we go. 4,800 in stock. Now we're

**Dave Jones:** talking. Another 10,000 expected of 1st of the 1st '24. Hope you don't want to make any more than that. But yeah, so you can might buy the 4,800 now. Yeah, 64 pin quad flat pack, no worries. Digikey finally

**Dave Jones:** worked. We've got 2,000 stock here for the 302. No, that's probably not going to have that's not going to have enough pins if 306 here, 1,200 in stock. Let's go for the 128 GL series. Maybe we'll actually get with

**Dave Jones:** more memory. You know, like you might go for the slightly pricier higher priced part if it's more available. If it's more readily available. And here we go. 11,000 stock. Now we're talking. The 24 FJ128GL306. I'll take that one, thank you very much.

**Dave Jones:** How much is that? Three bucks, two bucks 62 in 1200. No wackers, right? So, we can get them. Okay, I'm going to run with that for now. So, 128 GL306 family data sheet. Dead man timer for monitoring health of software. Nice.

**Dave Jones:** Yeah, it's it's really overkill, but it's got 32 segments by eight commons with up to 256 pixels. Absolutely plenty. It's got the LCD charge pump. Don't need anything else. Separate core independent LCD animation. So, it's got that animation thing, that cool funky

**Dave Jones:** animation feature, which is really nice. Don't care about it, but then it's, you know, it got all the extremely low power, like, you know, half a dozen different low power modes and stuff like that. Does it have a real-time clock?

**Dave Jones:** Yes, hardware real-time clock calendar. I'm liking this. This is looking like a winner winner chicken dinner. But, yeah, as I said, like, the smaller 80 one would probably do the business, but if you can't get it, it might be better to

**Dave Jones:** actually design in the larger footprint. In fact, this is probably an example of where we might be able to design in dual footprints so that cuz the pics are going to be fairly pin compatible. So, you actually put in the dual footprint

**Dave Jones:** and you populate whichever one you can actually get. And then you can just generate two binaries and the program whichever part you happen to be able to to get cuz one's going to be physically larger, one's going to be like the 64 pin

**Dave Jones:** jobbie, isn't it? And one's going to be like the 44 pin or or something and maybe the 44 pin footprint will fit inside the 64. That'll be interesting to have the dual footprints in there and you could have one inside the other and

**Dave Jones:** just join them, you know, short them out and populate whichever one you can actually get cuz we're still in the component crisis and probably forever will be now. Okay, timing modules provides five independent general purpose 16-bit timers, four of which can be combined

**Dave Jones:** into two 32-bit timer timers. Winner. The device also includes five five multiple output advanced capture compare modules. Well, let's go to the timer videotape, shall we? Timers 2, 3, 4, and 5. Okay? Oh, look. Uh refer to timers.

**Dave Jones:** They've got a dedicated They give you a link. This is really good. Uh so, here you go. They give you the document a dedicated document just for the timers. So, this might provide, you know, more detailed information. So, yeah, you

**Dave Jones:** know, we've we've got the prescaler. Um do we have a dedicated a second dedicated uh clock input? So, we can actually have an external clock, but they had Do they have an external oscillator? We might actually have to go

**Dave Jones:** back to the individual data sheet. Here Here they are. They're configuring timers uh two and three or four and five to give you a 32-bit um output. And it can tie into the ADC as well, but I don't need uh

**Dave Jones:** any of that. Then have Then there's the capture compare modules as well. Uh timer clock uh generator. So, all the different clock sources readily available diagram that shows me time base generator, clock sources for the capture compare timer modules. It

**Dave Jones:** looks like it has tons of flexibility. Trigger and sync logic as well. I might be needing that. Aha, here's the family clock diagram. This might uh tells Yeah, it's got a secondary oscillator here. Secondary oscillator enabled. Uh the

**Dave Jones:** post scaler, uh frequency to CPU. Yeah, and that can go through to the uh capture compare modules, which is part of the timer modules. Uh it goes to the peripherals as well via a divide by two. So, yeah, it looks like we can switch

**Dave Jones:** through a secondary oscillator. Or will the secondary oscillator Uh that's a low-power RC oscillator. Okay. Oh, no, that that's the internal low power. So, maybe if you use a main oscillator, a secondary oscillator a secondary oscillator for the timer, you

**Dave Jones:** probably can't then have the real-time clock one as well. So, you might have to use the secondary one for the uh real-time clock. Oh, yeah, there it is. Secondary oscillator goes off to the RTCC. See there. So, if you're using the

**Dave Jones:** real-time clock counter, if you've got a 32 kHz watch uh crystal just for that, um that goes off to the RTCC, then you can't unless it you happen to use that frequency, maybe. Let me think about that one. I might be

**Dave Jones:** able to, actually. Yeah. Yeah, I might be able to. I might be able to use the RTCC. I might be able to use the 32.768 kHz watch crystal to not only power the RTCC that I want, but also

**Dave Jones:** um as an input via this mux here to go into my timer. Anyway, I'm liking the look of this. Winner winner chicken dinner. I think I've found my part not maybe not this exact part, you know, but I'm loving the

**Dave Jones:** sound of that configurable um LCD. I know a lot other manufacturers, people are probably screaming in the comments down below. "Yeah, I can do this on um and yeah, I can do this on ST and yeah, go ahead, leave it in the comments

**Dave Jones:** down below. I know. Um Please. Seriously, like yeah, put you know, if you've got a nice uh micro down there that's low power, supports, you know, 32-bit uh flexible 32-bit timer capabilities, uh real-time clock and can drive um you know, 70-plus segment LCD

**Dave Jones:** as well, um leave it in the comments. I can probably do it on the MSP430 as I uh said cuz it's I I I'm pretty sure the two 16-bit timers can be configured into one cascade into one 32-bit. So, anyway, there you go. And

**Dave Jones:** please let me know if there is a parametric search function that can go across manufacturers that will find an individual peripheral like a timer. There might be. I don't know. Anyway, that was fun. And that's what I'm doing

**Dave Jones:** with this new project. Anytime I'm kind of like doing something on it, I might just press record here and just you know, there's no formal design process. It's just whatever I happen to be aspect over it, I happen to be working on, I'll

**Dave Jones:** probably just shoot and record a video if I can. And if you enjoy me doing this sort of stuff, I know these types of videos don't get, you know, a huge number of views. The enclosure one I released yesterday, it's doing

**Dave Jones:** not, you know, it's a biggest people have like specific needs. But if you like these sorts of design projecty type videos of stuff I'm just working, I happen to be like doing some real work here, the finding stuff. If you like me

**Dave Jones:** doing these kind of videos, please give the engagement with the thumbs up, subscribe, bell notification. Although I've done a video on how the bell notification BS. Anyway, yeah, hope you enjoyed it. Catch you next time.
