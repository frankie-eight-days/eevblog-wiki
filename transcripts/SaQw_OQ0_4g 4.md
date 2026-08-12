---
video_id: SaQw_OQ0_4g
title: EEVblog 1538 - NEW PROJECT Part 2 - Microcontroller Selection
url: https://www.youtube.com/watch?v=SaQw_OQ0_4g
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 24, "3": 39, "4": 60, "5": 69, "6": 84, "7": 92, "8": 118, "9": 130, "10": 143, "11": 151, "12": 161, "13": 173, "14": 194, "15": 219, "16": 229, "17": 236, "18": 247, "19": 266, "20": 283, "21": 297, "22": 306, "23": 316, "24": 330, "25": 343, "26": 359, "27": 372, "28": 386, "29": 406, "30": 420, "31": 430, "32": 446, "33": 464, "34": 481, "35": 501, "36": 519, "37": 535, "38": 549, "39": 566, "40": 575, "41": 589, "42": 599, "43": 610, "44": 620, "45": 631, "46": 641, "47": 653, "48": 661, "49": 671, "50": 684, "51": 695, "52": 707, "53": 723, "54": 732, "55": 746, "56": 758, "57": 775, "58": 789, "59": 803, "60": 810, "61": 826, "62": 839, "63": 849, "64": 867, "65": 882, "66": 893, "67": 907, "68": 922, "69": 931, "70": 944, "71": 957, "72": 970, "73": 983, "74": 991, "75": 1001, "76": 1014, "77": 1030, "78": 1042, "79": 1055, "80": 1065, "81": 1077, "82": 1089, "83": 1108, "84": 1117, "85": 1130, "86": 1143, "87": 1155, "88": 1174, "89": 1187, "90": 1194, "91": 1212, "92": 1221, "93": 1238, "94": 1260, "95": 1274, "96": 1285, "97": 1294, "98": 1306, "99": 1317, "100": 1327, "101": 1343, "102": 1354, "103": 1370, "104": 1383, "105": 1397, "106": 1416, "107": 1445, "108": 1453, "109": 1465, "110": 1485, "111": 1497, "112": 1509, "113": 1521, "114": 1533, "115": 1549, "116": 1558}
---

**Dave Jones:** Hi, it's new project time again, and today I'm looking for a microcontroller. I'm pretty microcontroller agnostic. I don't care which one I use as long as it meets several requirements that I have.

**Dave Jones:** Now, the requirements that I have are A, it's got to be low power cuz I'm targeting a really low power single battery design. So, we're talking like a year battery life kind of stuff, right?

**Dave Jones:** We're talking like really low power. Two, it's got to have an LCD controller built in. Up to I think 73 at current count, 73 segments. So, it's got to support, you know, a reasonably complex LCD built in.

**Dave Jones:** I could use an external LCD controller, of course, but that's an extra bomb item, extra cost, everything else. Nicer if it's built into the microcontroller, but if I can't get a suitable microcontroller with the number of LCD driver segments built in, columns or rows, haven't figured out my columns and rows yet.

**Dave Jones:** I've done an LCD design video, which I'll link in if you haven't seen it, how to design your own custom LCD, and I'll be doing that again for this project as well.

**Dave Jones:** So, you can probably see that in the future. So, it's got to drive up to, you know, over 70 LCD segments, and the third major requirement is actually multiple 32-bit timers, internal timers.

**Dave Jones:** Now, this doesn't necessarily mean I have to go to a 32-bit microcontroller. You know, everyone's going to go, "Oh, today just use a micro and code it and blah blah." Okay, right.

**Dave Jones:** And you don't you can possibly even there might I don't know offhand if there's an 8-bit micro with a 32-bit timer built in. Usually you don't get a 32-bit timer in a microcontroller unless that like it's a dedicated 32-bit micro, perhaps, but usually you'll get like maybe a 16-bit timer, and often you can actually cascade the two of those uh together to give you a 32-bit uh timer.

**Dave Jones:** So, you know, multiple 16-bit uh timers is okay as long as they are cascade-able. Uh and then you've got uh prescalers and stuff like that. We might go into that other um things to do with the timer.

**Dave Jones:** So, I want two high-resolution timers uh hardware timers uh to do some dedicated counting and it it won't fit the count thing that I'm counting won't uh fit in 16 bits.

**Dave Jones:** So, I really need that uh 32-bit uh count. So, uh you know, there's ways to get around like if you've only got a 16-bit counter, there's ways to get around it.

**Dave Jones:** But nah, no. I just want like a 32-bit timer. So, I've I can't remember the last time I needed a 32-bit timer in a microcontroller. It may be never.

**Dave Jones:** Um I wouldn't say that, but yeah, I I can't remember the last time. I think I cascaded two uh 16-bit timers. I don't think I've ever used an actual dedicated hardware 32-bit timer.

**Dave Jones:** Now, when I first think of a microcontroller that has LCD and ultra low power, I'm thinking of uh the TI MSP430, of course, absolute classic. Um I'm also thinking of uh the PIC uh 24F uh series, for example, which I've used before in many projects and stuff.

**Dave Jones:** Maybe even the PIC32 series, but I think I'd I'd be surprised if I couldn't find something in like a PIC uh 16 uh series cuz I'm pretty sure the PIC 16 series from memory has uh cascade-able 16-bit uh timers in it, but I don't know if any uh 8-bit uh micro actually, you know, the 8-bit PICs or or whatever actually have a um multiple cascade-able 16-bit timers can't off

**Dave Jones:** offhand. Uh Rusty old memory, I don't actually remember. So, we're going to do some parametric searching today to see if we can find it. Now, I'm open to pretty much any brand uh micro, but I don't want overkill.

**Dave Jones:** It's not going to be running fast. It's probably only to be running at a megahertz or something like that, right? So, not fast um at all, but I want it to be low power.

**Dave Jones:** So, any low power sleep modes, any sort of, you know, um any funky like LCD uh like low power LCD stuff and other things are built in. That'd be really nice.

**Dave Jones:** So, uh going to go to Digi-Key here. I'm in the microcontroller section and basically one of the uh things because one of the main requirements is that 32-bit timer, um I'm just looking through the parametric search here and it might show none of them even show timer, right?

**Dave Jones:** It's not a thing that they have in the parametric search and certainly not um you know, telling you whether or not it's like 32-bit capable. So, really um you know, you're like in search for LCD, like you can get ones for that have LCD and stuff like that and then you can't separate these.

**Dave Jones:** So, it's yeah, it's pretty much useless. Um in fact, totally useless. Let's go to Mouser um and see if they're any better. Um they separate them into uh 16 bits, so we can go into 16-bit micros here.

**Dave Jones:** For example, uh cuz you stand more of a chance to get your uh timer. Now, let's see what peripherals, you know, ADC and stuff like that, right? Um and I number of I/O pins.

**Dave Jones:** I don't need many I/O pins apart from all the pins required, of course, for the uh LCD. Of course, I don't need 70 uh plus pins for the LCD cuz the LCD will be multiplexed.

**Dave Jones:** It'll have uh commons and um lines as well. So, I could easily get away with like a 44-pin quad flat pack or something like that. Um and memory and memory and uh RAM really doesn't matter.

**Dave Jones:** Um this is not a complicated uh project application which I've got in mind here. So, yeah, I you know, a few K of memory is probably enough, really. But yeah, we got absolutely nothing here in uh the parametric search for that.

**Dave Jones:** I I go try, you know, Element 14 and all the rest of it, but but nah. Nah, it This is the kind of thing when you're searching for specific individual peripherals like this and they're important in your parametric searches, you really do want to go straight to the manufacturer's website.

**Dave Jones:** But hey, but this is 2023. Let's ask Chat GPT. Let's see if Chat GPT version 4 knows. Of course, it doesn't have like live data like recent, but you know, a couple of year-old data is fine.

**Dave Jones:** List all the microcontrollers that have internal 32-bit timers. Let's Let's give it a go. There are many microcontrollers available on the market with internal 32-bit timers. While it's difficult to list every single one, here are some of the more popular controllers that have internal 32-bit timers.

**Dave Jones:** The STM32 um Cortex. Yeah, like it's that's um Cortex is overkill. Well, it may not be. Um PIC32 series. Yeah, the MIPS core by Microchip. Yep, particular examples. So, Chat GPT knows the Tiva C series by TI.

**Dave Jones:** Um the NXP LPC series, the Atmel SAM series, which is another Cortex. Expressive and Tensilica. Okay, Renesas. Um ARM Cortex cores. Silicon Labs EFM32. Is that That's the Gecko or is the Gecko the smaller series?

**Dave Jones:** I can never remember. Um Infineon, Cypress. Keep in mind that this is not exhaustive and there are many other microcontrollers that that feature 30 additional new microcontrollers being developed.

**Dave Jones:** Yeah, I'll ask it specifically, are there any 8-bit microcontrollers with internal 32-bit timers? Yes, there are 8-bit microcontrollers with internal 32-bit timers. Although less common than they with 32-bit timers, few include Atmel ATmega series.

**Dave Jones:** Really? ATmega64, 128. They've got a 32-bit counter timer? Do they? I didn't know that. PIC18 series. Oh, okay. They've got have 8-bit architecture and offer a 32-bit timer. Chat GPT-4 is slow.

**Dave Jones:** Thank you. I will review the data sheet cuz I didn't think that the ATmega 128 had a 32-bit timer in it. Two 8-bit timers with separate prescalers and compare modes to expand a 16-bit time counters to separate prescaler compare modes and compare modes.

**Dave Jones:** Okay, you might be able to join those two expanded 16-bit time counters. I I don't think I've ever I've only used like an Atmel once or twice at the microcontroller level and I don't recall having to use the 16-bit timer in it.

**Dave Jones:** So, yeah, I'm not really seeing the 32-bit. Can we do 32-bit? Uh AB instructions are 32-bits wide. No, there's nothing else in there. 32-bit No, 32-bit 32-bit instruction, 32-bit ID register No.

**Dave Jones:** No, there's nothing about using the timer as a 32-bit timer. So, the AI is wrong. And let's try this uh PIC 18 uh 18F25K40. Geez, could they make it more more convoluted?

**Dave Jones:** It's got a watchdog timer, three 8-bit timers, four 16-bit timers. Okay, but can we do can they be cascaded as 32-bit timers? Hardware ti- hardware limit timer, hardware monitoring fault detection, cool bananas.

**Dave Jones:** 8-bit uh precharge time No, that's for the uh capacitive touch. Oscillator startup timer, four 16-bit timers. Search for 32-bit. No, 32-bit 32 result 32-bit Okay, it's got a hardware multiplier.

**Dave Jones:** Uh wow, really? In the 18F series, didn't know that. Uh no, no, I didn't really just just the multiplier result, that's it. I It's not related to the timer, I don't think.

**Dave Jones:** So, yeah, nah. So, we're probably going to have to go to like a up it to a 16-bit. But, as I said, once you're after specific requirements for something like a timer like that, um you really need to go to the manufacturers uh parametric search.

**Dave Jones:** So, uh let's go to TI here. So, let's view all products. And does this give us the parametric search? It does. It does. And we can filter all filters over here.

**Dave Jones:** Timers, 16-bit. There you go. I was going to look under peripherals, but uh no, it's they've got a separate thing down here. Cuz I know Oh, they have up to six.

**Dave Jones:** Okay. So, there you go. You want at least two Let Let's say four timers. 4 16-bit. Looks like we're only going to get 16-bit timers, as I suspected. Uh as my memory uh served me correctly.

**Dave Jones:** We can go across here. 16-bit timers. There you go. Sorry, my head's in the way, but you can see that that column there, we can get five or six timers.

**Dave Jones:** That's pretty groovy. Uh 16-bit timers. And I'm pretty sure that they can be uh cascaded to a 32-bit timer. Six 16-bit timers with up to seven capture compare registers.

**Dave Jones:** A 32-bit CRC. That's pretty groovy. No, it looks like we'd have to go to the timer section to actually uh figure to actually see it. Sometimes you know Well, I'm not going to I'm not getting it on a keyword uh search.

**Dave Jones:** They certainly don't tell you at the top level of the data sheet, which is not very handy is, but I'm pretty sure from memory the MSP430 timer can uh be cascaded.

**Dave Jones:** Let's have a look. Timer B. So, there's your timers down there. Seven capture compare registers. Uh looks like it's got internal external as well. Timer A, timer B, input.

**Dave Jones:** And then you start getting into the complexities as we might look at of the internal architecture of the timers and where it can get its clocks from and prescalers and all sorts of things like that.

**Dave Jones:** So, it gets messy, but I'm I'm pretty sure anyway, without getting bogged down in the the details, I'm pretty sure you can cascade these 16-bit timers in here to do 32-bit, but maybe not this one.

**Dave Jones:** This is an ultrasonic sensing for water metering applications. I It looks like they've got you'd probably have to choose the like the specific one. Okay, so yeah, no, okay.

**Dave Jones:** Let's I certainly wouldn't rule that out, but let's go over to Microchip and see what they've got. Now, let's explore these 16-bit micros here. And which I've used before.

**Dave Jones:** Uh, product selection guide, that's what we want. Is that our parametric search? No, it's PDF. Ah, clocks and timers. There you go, 16 32-bit there, and they've all got them.

**Dave Jones:** They've all got them. The entire PIC19 range. I thought they had more than that. Uh, timers. General purpose 16 32-bit timer with compare capability. Yep, that looks pretty groovy.

**Dave Jones:** But I also want one with segment um LCD as well. So, what I actually want is the segment LCD over here. Is that How does that work? Does that That That doesn't click.

**Dave Jones:** It's broken. What? Graphics LCD? What? It's broken. Anyway, uh, we've got the LCD segments. So, we can have up to 200 like we get That's plenty. 256 is absolutely plenty.

**Dave Jones:** So, let's go look at a PIC24F uh, the GL30X. That's the GL family low pin count value line. Segment LCD USB I don't need USB. Don't need any of that.

**Dave Jones:** Uh, comparators. Um, no, don't really need comparators. Uh, and these are all extra low power. Oh, hello. Feature core independent peripheral LCD with autonomous animation. I need that. It allows you to like toggle between different states.

**Dave Jones:** Like if you've got a clock or something, it it flashes and it looks like you can do that in the LCD module. You don't have to do that in code.

**Dave Jones:** I'm sold. I'm sold. Um hats off to Microchip marketing. I don't know how you would find that. Let us know. Leave in the comments down below if any other micros with LCD capability have this um autonomous animation thing.

**Dave Jones:** Most display applications involve a few common animations like blinking periodically alternating between displays and blanking the pixels by using the integrated LCD drive with autonomous animation you can offload most of these animation routines from the CPU.

**Dave Jones:** This allows you to to enable animation in power saving modes while the CPU is in those idle or sleep modes. Perfect. This is exactly what I want. Like you flash things off and on.

**Dave Jones:** And you can actually switch between I wonder if they've got like a mapping for two entire displays. And you can actually it looks like you can presumably however many segments you got, you know, your 256 segments that it has dual mapping and it'll just automatically switch between those.

**Dave Jones:** So you load up both memory maps with the info you want and it can just toggle between them. Wow. I'm sold. Hang on. I might be sold further. Quickly design a display interface with MPLAB Code Configurator.

**Dave Jones:** MCC reduce your display design time to minimize the help of MCC eliminates the meticulous and time-consuming task of mapping the pins and segments. Allows you to import display icons.

**Dave Jones:** Ah, I am sold. Ding-a-ling, winner winner chicken dinner. Um I I'm I'm going to stop looking now. I'm going to stop looking. I'm I am sold. Ultra low power, ultra sleep.

**Dave Jones:** Yeah, cuz battery friendly. Also, we've got it it meets the requirements. It's ultra low power. Oh, by the way, I forgot it'd be nice if it also had an internal real-time clock um as well with an external watch crystal as well so that it can keep the time.

**Dave Jones:** That would be nice. I can always use an external chip for that. That's not a deal breaker, but I'm I'm sold. I haven't used this configurator thing. Learn more about the MCC.

**Dave Jones:** It looks like it's not Okay, code configure. Yeah, no, I I think I might have touched on this before, but yeah, I haven't used the LCD one. It does other things, not just LCD.

**Dave Jones:** And then it'll have different peripheral stuff that allows you just a nice GUI interface that allows you to actually configure everything. And one of the annoying things about LCD designs is actually as they said, mapping those segments in, especially if you're multiplexing the displays.

**Dave Jones:** If that takes care of all that, you save save a day's work just digging around with that. So GL302 segment LCDs are 42. 42 segments, that's not enough. 80 will cover it.

**Dave Jones:** I don't need 64K of memory, but you know, that's that's what you end up with, right? 36 pin count, right? So it can map 80 segments, so that's low that's low pin count.

**Dave Jones:** No USB, don't need it. It looks like No, it looks like they've got more devices. Why why can't you show me the whole lot? View all parameters. They keep changing that.

**Dave Jones:** Oh, this is Oh, this has got one of these jazzy thingamabobs. Okay, there's nine parts in this series, so you know, it's not like the configurator is a huge amount of help.

**Dave Jones:** Actually, let's go up here. We want a minimum 71.5. 75. I think I might be able to get away with 75. I really don't want like hundreds of segments, so let's like narrow the range like that.

**Dave Jones:** We got No, we're still got nine parts. What? And pricing, not too concerned about pricing, but might as well go for like the cheapest $1.90. 24 FJ128GL303. It's got 80 segments, which is enough.

**Dave Jones:** And no no USB interface, that's fine. Don't care about ADCs. Pin count, 36. 36 pin jobbie. 8K of RAM. And and tons. It looks like it's that one. That's a winner winner chicken dinner.

**Dave Jones:** Let's look at the 24 FJ64GL303. Can we actually buy that? Can we buy it? First thing you do before you design the PCB, pro tip, before you design the PCB, order your parts.

**Dave Jones:** Make sure you can get them. Search. I've had this problem. Digikey like just takes forever. Give me bloody Mouser. 630 in stock, two bucks 90 one off, 340, no stock of that one.

**Dave Jones:** Woah. Yeah, I'm not going to design in one that's only got those so you know, I want like 10,000 in stock, please. Not that I plan on making 10,000, but you know, it's it's the vibe.

**Dave Jones:** What I'm going to do is I'm going to expand it a bit so that I can get more of a selection of parts cuz maybe the higher pin count jobbies are going to be better.

**Dave Jones:** Look, if I just search for the 64GL, let's just search for that and don't worry about the ones afterwards. There we go. 4,800 in stock. Now we're talking. Another 10,000 expected of 1st of the 1st '24.

**Dave Jones:** Hope you don't want to make any more than that. But yeah, so you can might buy the 4,800 now. Yeah, 64 pin quad flat pack, no worries. Digikey finally worked.

**Dave Jones:** We've got 2,000 stock here for the 302. No, that's probably not going to have that's not going to have enough pins if 306 here, 1,200 in stock. Let's go for the 128 GL series.

**Dave Jones:** Maybe we'll actually get with more memory. You know, like you might go for the slightly pricier higher priced part if it's more available. If it's more readily available. And here we go.

**Dave Jones:** 11,000 stock. Now we're talking. The 24 FJ128GL306. I'll take that one, thank you very much. How much is that? Three bucks, two bucks 62 in 1200. No wackers, right?

**Dave Jones:** So, we can get them. Okay, I'm going to run with that for now. So, 128 GL306 family data sheet. Dead man timer for monitoring health of software. Nice. Yeah, it's it's really overkill, but it's got 32 segments by eight commons with up to 256 pixels.

**Dave Jones:** Absolutely plenty. It's got the LCD charge pump. Don't need anything else. Separate core independent LCD animation. So, it's got that animation thing, that cool funky animation feature, which is really nice.

**Dave Jones:** Don't care about it, but then it's, you know, it got all the extremely low power, like, you know, half a dozen different low power modes and stuff like that.

**Dave Jones:** Does it have a real-time clock? Yes, hardware real-time clock calendar. I'm liking this. This is looking like a winner winner chicken dinner. But, yeah, as I said, like, the smaller 80 one would probably do the business, but if you can't get it, it might be better to actually design in the larger footprint.

**Dave Jones:** In fact, this is probably an example of where we might be able to design in dual footprints so that cuz the pics are going to be fairly pin compatible.

**Dave Jones:** So, you actually put in the dual footprint and you populate whichever one you can actually get. And then you can just generate two binaries and the program whichever part you happen to be able to to get cuz one's going to be physically larger, one's going to be like the 64 pin jobbie, isn't it?

**Dave Jones:** And one's going to be like the 44 pin or or something and maybe the 44 pin footprint will fit inside the 64. That'll be interesting to have the dual footprints in there and you could have one inside the other and just join them, you know, short them out and populate whichever one you can actually get cuz we're still in the component crisis and probably forever will be now.

**Dave Jones:** Okay, timing modules provides five independent general purpose 16-bit timers, four of which can be combined into two 32-bit timer timers. Winner. The device also includes five five multiple output advanced capture compare modules.

**Dave Jones:** Well, let's go to the timer videotape, shall we? Timers 2, 3, 4, and 5. Okay? Oh, look. Uh refer to timers. They've got a dedicated They give you a link.

**Dave Jones:** This is really good. Uh so, here you go. They give you the document a dedicated document just for the timers. So, this might provide, you know, more detailed information.

**Dave Jones:** So, yeah, you know, we've we've got the prescaler. Um do we have a dedicated a second dedicated uh clock input? So, we can actually have an external clock, but they had Do they have an external oscillator?

**Dave Jones:** We might actually have to go back to the individual data sheet. Here Here they are. They're configuring timers uh two and three or four and five to give you a 32-bit um output.

**Dave Jones:** And it can tie into the ADC as well, but I don't need uh any of that. Then have Then there's the capture compare modules as well. Uh timer clock uh generator.

**Dave Jones:** So, all the different clock sources readily available diagram that shows me time base generator, clock sources for the capture compare timer modules. It looks like it has tons of flexibility.

**Dave Jones:** Trigger and sync logic as well. I might be needing that. Aha, here's the family clock diagram. This might uh tells Yeah, it's got a secondary oscillator here. Secondary oscillator enabled.

**Dave Jones:** Uh the post scaler, uh frequency to CPU. Yeah, and that can go through to the uh capture compare modules, which is part of the timer modules. Uh it goes to the peripherals as well via a divide by two.

**Dave Jones:** So, yeah, it looks like we can switch through a secondary oscillator. Or will the secondary oscillator Uh that's a low-power RC oscillator. Okay. Oh, no, that that's the internal low power.

**Dave Jones:** So, maybe if you use a main oscillator, a secondary oscillator a secondary oscillator for the timer, you probably can't then have the real-time clock one as well. So, you might have to use the secondary one for the uh real-time clock.

**Dave Jones:** Oh, yeah, there it is. Secondary oscillator goes off to the RTCC. See there. So, if you're using the real-time clock counter, if you've got a 32 kHz watch uh crystal just for that, um that goes off to the RTCC, then you can't unless it you happen to use that frequency, maybe.

**Dave Jones:** Let me think about that one. I might be able to, actually. Yeah. Yeah, I might be able to. I might be able to use the RTCC. I might be able to use the 32.768 kHz watch crystal to not only power the RTCC that I want, but also um as an input via this mux here to go into my timer.

**Dave Jones:** Anyway, I'm liking the look of this. Winner winner chicken dinner. I think I've found my part not maybe not this exact part, you know, but I'm loving the sound of that configurable um LCD.

**Dave Jones:** I know a lot other manufacturers, people are probably screaming in the comments down below. "Yeah, I can do this on um and yeah, I can do this on ST and yeah, go ahead, leave it in the comments down below.

**Dave Jones:** I know. Um Please. Seriously, like yeah, put you know, if you've got a nice uh micro down there that's low power, supports, you know, 32-bit uh flexible 32-bit timer capabilities, uh real-time clock and can drive um you know, 70-plus segment LCD as well, um leave it in the comments.

**Dave Jones:** I can probably do it on the MSP430 as I uh said cuz it's I I I'm pretty sure the two 16-bit timers can be configured into one cascade into one 32-bit.

**Dave Jones:** So, anyway, there you go. And please let me know if there is a parametric search function that can go across manufacturers that will find an individual peripheral like a timer.

**Dave Jones:** There might be. I don't know. Anyway, that was fun. And that's what I'm doing with this new project. Anytime I'm kind of like doing something on it, I might just press record here and just you know, there's no formal design process.

**Dave Jones:** It's just whatever I happen to be aspect over it, I happen to be working on, I'll probably just shoot and record a video if I can. And if you enjoy me doing this sort of stuff, I know these types of videos don't get, you know, a huge number of views.

**Dave Jones:** The enclosure one I released yesterday, it's doing not, you know, it's a biggest people have like specific needs. But if you like these sorts of design projecty type videos of stuff I'm just working, I happen to be like doing some real work here, the finding stuff.

**Dave Jones:** If you like me doing these kind of videos, please give the engagement with the thumbs up, subscribe, bell notification. Although I've done a video on how the bell notification BS.

**Dave Jones:** Anyway, yeah, hope you enjoyed it. Catch you next time.
