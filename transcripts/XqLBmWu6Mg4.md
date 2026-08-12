---
video_id: XqLBmWu6Mg4
title: EEVblog #410 - Microtek 8086 In-Circuit Emulator Teardown
url: https://www.youtube.com/watch?v=XqLBmWu6Mg4
source: youtube-asr
timestamps: {"0": 1, "1": 20, "2": 35, "3": 48, "4": 69, "5": 90, "6": 100, "7": 122, "8": 149, "9": 164, "10": 173, "11": 186, "12": 201, "13": 216, "14": 234, "15": 250, "16": 269, "17": 278, "18": 306, "19": 324, "20": 348, "21": 362, "22": 379, "23": 392, "24": 403, "25": 424, "26": 442, "27": 452, "28": 460, "29": 472, "30": 489, "31": 504, "32": 520, "33": 536, "34": 553, "35": 574, "36": 592, "37": 605, "38": 622, "39": 632, "40": 642, "41": 652, "42": 670, "43": 698, "44": 711, "45": 736, "46": 751, "47": 772, "48": 798, "49": 812, "50": 837, "51": 852, "52": 873, "53": 889, "54": 901, "55": 912, "56": 925, "57": 944, "58": 960, "59": 975, "60": 987, "61": 999, "62": 1014, "63": 1034, "64": 1054, "65": 1063, "66": 1078, "67": 1091, "68": 1103, "69": 1115, "70": 1132, "71": 1147, "72": 1158, "73": 1167, "74": 1185, "75": 1205, "76": 1219, "77": 1232, "78": 1249, "79": 1263, "80": 1273, "81": 1296, "82": 1309, "83": 1326, "84": 1340, "85": 1359, "86": 1371, "87": 1388, "88": 1413, "89": 1435, "90": 1445, "91": 1456, "92": 1465, "93": 1473, "94": 1484, "95": 1493, "96": 1514, "97": 1523, "98": 1547, "99": 1561, "100": 1566, "101": 1586, "102": 1601, "103": 1628, "104": 1639, "105": 1656, "106": 1667, "107": 1684, "108": 1692, "109": 1701, "110": 1714, "111": 1725, "112": 1738, "113": 1748, "114": 1761, "115": 1769, "116": 1787, "117": 1799, "118": 1814, "119": 1833, "120": 1844, "121": 1857, "122": 1878, "123": 1897, "124": 1919, "125": 1935, "126": 1945, "127": 1964, "128": 1979, "129": 1997, "130": 2014, "131": 2027, "132": 2042, "133": 2059, "134": 2075, "135": 2083, "136": 2097, "137": 2112, "138": 2129, "139": 2138, "140": 2153, "141": 2169, "142": 2185, "143": 2202, "144": 2211, "145": 2221, "146": 2246, "147": 2258, "148": 2272, "149": 2281, "150": 2299, "151": 2315, "152": 2326, "153": 2337, "154": 2354, "155": 2375, "156": 2387, "157": 2401, "158": 2419, "159": 2442, "160": 2453, "161": 2462, "162": 2478, "163": 2493, "164": 2517, "165": 2529, "166": 2551, "167": 2566, "168": 2574, "169": 2590, "170": 2600, "171": 2612, "172": 2625, "173": 2640, "174": 2656, "175": 2679, "176": 2695, "177": 2709, "178": 2723, "179": 2736, "180": 2756, "181": 2767, "182": 2782, "183": 2799, "184": 2812, "185": 2826, "186": 2837, "187": 2856, "188": 2873, "189": 2881, "190": 2892, "191": 2902, "192": 2922, "193": 2936, "194": 2951, "195": 2967, "196": 2985, "197": 2998, "198": 3011, "199": 3026, "200": 3041, "201": 3055, "202": 3074}
---

**Dave Jones:** Hi, welcome to Tear-down Tuesday. Yes, it's vintage time again and we've got not vintage computer, but vintage microprocessor development tool. We've got a Microtek 8086 in-circuit emulator or ICE tool and we'll take a good look at it in detail.

**Dave Jones:** I scored this baby on eBay for 99 cents. I was the only bidder. Fantastic. Came in the original box with all the original manuals, all the original cables, all the pods and zip sockets and everything.

**Dave Jones:** Beauty. Can't believe it and yep, check it out. There it is. This is the 8086, but this particular unit supports the 8088 processor and the NEC equivalents, the V20 and the V30 as well.

**Dave Jones:** If you remember, the 8086 or the 8088 was what was used in the original IBM PC back in the early '80s and that's what all modern Intel Wintel type PCs are based on and this was an incredibly valuable development tool back then.

**Dave Jones:** If you were developing a PC or hardware for a PC, something like that, you really or even software, you really needed one of these in-circuit emulators or ICE. Now, as you'll see later, I'll show you the real thing, but it basically is a box like this, which we've seen, cables coming out.

**Dave Jones:** We've got pods, which then go off and plug into the socket on your processor. Now, you might think that well, these aren't used anymore, but well, they effectively still are.

**Dave Jones:** An in-circuit emulator is the penultimate tool for embedded system design and embedded computer, you know, software debugging, hardware debugging, stuff like that and you might be familiar with say the, um, PICkit uh 3, you know, microcontroller debug tools.

**Dave Jones:** These are not in-circuit emulators. These are in-circuit debuggers or ICDs and they work differently because these are what are known as intrusive, uh, debuggers. That means that you have to actually put code into your PIC chip or AVR chip when you're actually developing it to, you know, to debug and breakpoint and stop and look at stuff and play with it and debug it.

**Dave Jones:** And well, that's not your final code. These things do not, these in-circuit debuggers do not allow you to debug your final code. And that's important and that's where these in-circuit emulators, um, you know, they might be called emulators.

**Dave Jones:** This they go under various names, but they're generally known as an ICE or an in-circuit emulator. That's where these come in. These are non-intrusive. These emulate the actual processor.

**Dave Jones:** So, they've got specific hardware in here and they emulate the whole chip. They're very complex, uh, things to actually, uh, design and hence they're very expensive. And well, back then in the day, they were very big as well.

**Dave Jones:** They'll be a lot of circuitry in here which we'll take a look at. Now, in-circuit emulators are still used today, but they're generally still quite an expensive and rare tool to have, but absolutely essential when you want to do non-intrusive debugging on a design.

**Dave Jones:** And there is no substitute for it, really. On, um, uh, microprocessor-based, um, systems that have separate memory and the, you know, the processor separate IO chips and separate memory.

**Dave Jones:** Really old school stuff instead of the embedded, uh, micro, uh, processors and microcontrollers we have these days. You could use a, uh, logic analyzer or something like that. That's another non-intrusive technique to debug your applications, but, uh, they're not the best.

**Dave Jones:** You cannot beat an in-circuit emulator that allows you to monitor your code real time, trace your code in real time, see exactly which part of your C program is executing, all that sort of stuff, break into it, breakpoints, do your usual debugging stuff on your actual release code.

**Dave Jones:** And that's the vital part of it. So, anyway, I think these things this is going to be really, well, it's going to be interesting inside, unfortunately, I'm not going to be able to power the sucker up because, well, it comes with a plug-in ISA bus card for a PC.

**Dave Jones:** I don't actually have the original software for this either, and I don't have an 8086 target system to play with either. But, hey, we'll take it apart and see what's inside.

**Dave Jones:** I expect a whole bunch of through-hole 80s technology. Let's go. Now, I just expand on this in-circuit commentary a little bit more. Here's a pretty old, you'll notice the date code there, 9804 PIC 16C74A microcontroller, but, you know, it's a typical still a fairly typical microcontroller these days, and everything is built into this thing.

**Dave Jones:** All of the memory, all of the IO and UARTs and, you know, various other stuff are all built into there. And how do you emulate this thing? Well, you can emulate it using a, you know, dedicated hardware that actually emulates the chip, but you always wonder, well, how accurate is that?

**Dave Jones:** And of course, we can't get in there to actually probe any of the signals normally if we use the regular chip, like we can't break into the memory and simulate it and, well, you know, program the memory, trace it, examine the contents, put contents in there, do all that sort of jazz because in fact, uh, ROM memory in this one is UV erasable.

**Dave Jones:** It's not a flash memory. Hence, why it has this clear window on top. You have to actually erase this thing under ultraviolet light. Well, in-circuit, uh, emulators, they work, uh, differently.

**Dave Jones:** Even if you've got a flash-based controller, in-circuit emulators will generally use, um, RAM memory, fast volatile memory, to simulate the flash or the ROM memory in a system. So, you don't have to, uh, wait for the flash memory to be programmed or something.

**Dave Jones:** You can just do it very quickly, almost instantaneously, in static memory. So, how would you actually, uh, probe into a system like this to do this? Well, you have to actually rely on the manufacturer.

**Dave Jones:** Um, and manufacturers still manufacture these, uh, these days, I believe, but, uh, back in the old days, they definitely, uh, did it all the time. They would manufacture a special version of the chip called a bond out chip.

**Dave Jones:** And what it does is it actually, um, instead of all the regular pins on there, it, uh, bonds out extra wires out to extra pins, which are then, um, able to, uh, tap all the internal parts of the circuit, so you'd like the memory and, um, you know, all sorts of other peripherals and, uh, various important points within the microprocessor.

**Dave Jones:** You can break those out and then use that, uh, special, very expensive, uh, chip, usually, to develop an in-circuit emulator. So, it emulates the real chip. But, often with these, uh, bond out chips, they would, uh, lag behind the real production versions of the chips.

**Dave Jones:** If there's silicon bugs in the production chips are being fixed, well, whoops, you know, your in-circuit, uh, emulator using that bond out chip could be, uh, out of date.

**Dave Jones:** And it was always a struggle to, uh, keep up with these things using, uh, bond out chips. But, yeah, the manufacturers would actually manufacture a special version of this chip.

**Dave Jones:** Um they didn't make many of them cuz these in-circuit emulators don't sell in, you know, the tens of thousands or hundreds of thousands like the little, you know, PICkit uh debuggers and stuff do these days.

**Dave Jones:** These were very expensive, very specialized chips. And of course, as you might be aware, a lot of modern uh microcontrollers have built-in um sort of, you know, in-circuit emulator and in-circuit debugger type functionality already built into the production die.

**Dave Jones:** That's why, say, you know, on the Microchip, you can use the um in-circuit debugger, which actually has some circuitry already built into the die that allows you to do basic break breakpoints and basic debugging, stuff like that.

**Dave Jones:** And for those who uh love to see the original boxes, it's I've got all the original uh foam uh inserts in there. I've got a um the Universal Symbolic uh debugger user's manual as well as well as the original uh disk for the uh Symbolic debugger.

**Dave Jones:** Fantastic stuff. Um I've got all the uh all the connecting ribbon cables for the things. I've got the pods, of course, which we'll uh take a look at, complete with the original, hopefully, all the pins intact.

**Dave Jones:** Ah. All the pins intact. Fantastic. That uh plugs into your uh circuit under test with the uh ZIF sockets. I've got Actually, there's a couple of those. They're both for the 80 86 and it supports the 8087 as well.

**Dave Jones:** There's the emulation micro processor. Fantastic stuff. And comes with the original ISA uh board control board as well. Copyright 1986 Microtek. Although, I think this actual uh unit is about um Well, the manual says uh '89 or thereabouts.

**Dave Jones:** So, but it could have certainly been manufactured in the very early '90s and various other connecting leads as well. They're the That's the trace pin output leads. So, yep, going to some micro grabbers down in there.

**Dave Jones:** Even got the warranty card. Fantastic. And a whole bunch of stuff. Brilliant. All for night There's a third. There you go. I've got a third pod which doesn't have the 8087.

**Dave Jones:** It's only got the 8086 socket in it. So, here's how the thing would hook up. You would have your ISA PC card running the emulation software which allows you to do all the on-screen displays, the waveforms, the debugging, the whole works, and all the timing stuff.

**Dave Jones:** And that would plug in and connects to the cable on the back, which we'll have a look at. And then you would plug these lovely long ribbon cables here.

**Dave Jones:** There we go. This one's specific for the 8086. If I'm not sure what different cable would be for the 8088, for example, but they would These would plug into there like that.

**Dave Jones:** Bingo. There you go. And then you would plug your actual microprocessor that you wanted to emulate into here and your 8087 as well if you were using the 8087.

**Dave Jones:** And then this cable would connect into your circuit under test. It would plug into your microprocessor socket. So, instead of this processor plugging directly into the socket like normal, you would put all this circuitry and this in-circuit emulator or ice in between it.

**Dave Jones:** Now, this is actually um uh not so much an emulator cuz it's not actually emulating the microprocessor. The circuitry inside this thing is not emulating the microprocessor. It's It's just It's using a real microprocessor and it's tapping into that and just tapping into all the memory signals and the clock signals and everything else required to run the PC because the processor is just that.

**Dave Jones:** It's just a processor. It needs all external memory and everything else. So, that's why you could do this with the 8086 which you couldn't do, for example, on that PIC we saw earlier.

**Dave Jones:** You would have had to use a bond out version of the chip. Now, this is um using the real microprocessor, of course, is much, much better than using a circuitry that, you know, is like a PLD or an FPGA that's just emulating your microprocessor because then you don't know if there's any bugs or any issues with your emulation at all.

**Dave Jones:** You don't know if it's 100% but when you're using your real actual production silicon in there, you can be 100% sure it's a true emulation. Now, one of the issues with in-circuit emulators, which is still true today, you can't get around it.

**Dave Jones:** It's basic physics, uh the speed limitations. Now, when you're talking about big cables like this which, um you know, break into your circuit under test. Look at all this These signals have to be broken out, go into here, all through the circuitry in here, all through these huge cables in here, all to the circuitry inside this box and that is a lot of extra copper.

**Dave Jones:** Remember that, um you know, signals travel at roughly, rule of thumb, um 15 cm per nanosecond. So, every 15 cm on this cable is going to represent a 1 nanosecond delay and well, that can be a huge problem if you're working at a processor pretty much in a system like this with, you know, the connecting cables and stuff like that.

**Dave Jones:** Um once you start talking um three digits or 100 MHz, these types of systems aren't really going to work anymore. Um so, you know, this one's only working at 10 MHz maximum cuz that was the upper speed of the 8086 back then.

**Dave Jones:** So, these types of systems with the long cables and breaking in order all worked just a treat. But on modern processors working at many many hundreds of MHz, in-circuit emulator design is a real art in itself and uh trying to minimize the uh physical interconnections for various things, even for our bond out chips and stuff like that, you have to be very very careful.

**Dave Jones:** Signal integrity uh becomes a huge deal and uh flight time on the copper cables or any interconnects at all can really ruin your day. It really is uh quite a difficult art to design these in-circuit emulators.

**Dave Jones:** Huge R&D dollars go into these things and they don't sell many of them. So, they're usually pretty darn expensive. And that's the reason why they've put the emulation microprocessor as close as physically possible to the um to the connection pins here is because they really need to uh keep that signal integrity as best they can.

**Dave Jones:** If this emulation microprocessor was inside this box and had to go through all these huge long cables to get there, which is, you know, a physical requirement, you know, this box can't be, you know, inches away from your system, your device under test, or your DUT.

**Dave Jones:** Um you know, it can't be several inches. You've got to have all these buffered cables, so they're all be all buffer circuitry and stuff inside here to drive all these long cables and uh also to drive out to the socket here.

**Dave Jones:** But that's why that's physically kept as close as possible. And on the newer higher-speed systems today with, you know, processors with many many hundreds of MHz, you know, you won't even get this distance.

**Dave Jones:** You'll you know, only get maybe an inch or or the uh circuitry has to be built in to clips which uh specifically go onto the processor or they have to build it on to the die.

**Dave Jones:** So, although this thing is called an in-circuit emulator, it's not actually emulating the microprocessor. It's using the real uh silicon, your real production silicon. Plug it in there, and it just breaks out everything around it allowing you to do full in-circuit emulator uh capability like memory mapping and stuff like that.

**Dave Jones:** Now, let's take a quick look at the uh manual here for those who want to see it. Unfortunately, it didn't come with the uh software like it did uh with the 5 and 1/4 in floppy we got with the uh debugger software, but anyway, uh well, what the heck?

**Dave Jones:** Third uh third edition January 1989 there. So, really, we are talking, but it could have been manufactured uh uh you know, early '90s or something like that. Originally copyright '86.

**Dave Jones:** Microtek International all rights reserved. And let's have a look at some basic specs of this puppy, and uh blah blah blah blah blah. Maybe I'll uh No, I haven't got time to scan any of this.

**Dave Jones:** Sorry. Too hard. I was going to, but um it allows you to emulate um 8086s, 8088, 8087 coprocessor, the NEC V20 and V30. Goes up to 10 MHz external clock.

**Dave Jones:** The emulation uh memory is important. That's the amount of uh static RAM built in as I mentioned because uh uh even with, you know, modern systems with flash uh program memory and stuff like that, you know, they've got a limited uh write cycle or limited uh life in them.

**Dave Jones:** So, really, static RAM uh just allows you to do um infinite and also uh pretty much instant um changing of the uh emulation program memory. Now, it's only got 256K, so I'm not sure what you'd be doing if you um had like if you were debugging or emulating a uh 640K uh system, for example.

**Dave Jones:** I'm not sure if you can You can probably bank it or do something like that. Up to 464 K segments. Um it's got uh seven real-time uh break points, four execution break points, and two bus uh break points, which allow you to get um you know, various things cuz not uh there's a lot of hardware that's actually required to do that.

**Dave Jones:** So, that's why you can't just have an infinite number of uh complex These are often called it uh taps into the address, data, status, and uh some counts as well.

**Dave Jones:** And uh it can do interrupt, I/O read, and uh stuff all that sort of break point stuff. And it's got one external hardware break point as well. And it does real-time uh tracing of the address, data, all the rest of it.

**Dave Jones:** Uh the trace buffer is only uh 2K and 76 bits wide. Uh what else we got? Registers You can display, modify. You can single step. Oh. You can single step through.

**Dave Jones:** Um and uh the time measurement has a resolution of 1 microsecond. You can do cycle steps, trace start stop. Uh all the memory commands you can do, and the various interfaces.

**Dave Jones:** So, there you go. That is a basic introduction. If if there's anything more interesting I haven't actually uh read it yet, but here we go. Here's the system block diagram.

**Dave Jones:** Aha. It tells us what cards we've got in here. We've got our LAM card. Not sure what that The top card is called the EPM card. The middle one is called the EMM, and the bottom one is the uh next one down is the LAM card, and then we've got a CPM card.

**Dave Jones:** So, it looks like we've got four boards in this thing. And they're all going to I'm sure they'll all be uh DIP and through-hole technology. And we'll open up the uh pod as well, but uh the pod I only expect to see uh buffers and things like that.

**Dave Jones:** Perhaps. Bingo. There we go. We've got Logic LAM is Logic analyzer module. EMM is emulation memory module. So that would that was a separate board and the CPM is the control processor modules.

**Dave Jones:** And a quick look at the front. We've got a 5 volt power LED. Everything's going to be 5 volts. No 3.3 volt rubbish in this thing. The emulation program run.

**Dave Jones:** I assume that what EP stands for. Green LED. Green is good. Your program's running. It's got various slave sync outputs master and slave external trigger input and your trace outputs as well which you can connect to your circuit under test.

**Dave Jones:** And then we've got our pod interfaces here. And we've got a funky little recessed reset button. And that's all there is to the front of it. And on the back here we've got a parallel and serial interface which goes off to our um board.

**Dave Jones:** We've got a fan and just AC mains input. That's it. Made in Taiwan, Republic of China. All right. What was that? Like 10 15 minutes of crapping on about in-circuit emulators and stuff like that.

**Dave Jones:** Let's have a look inside this thing. Now, as I said, I reckon it's going to be all through-hole technology. Bugger. We need a uh Let's have a look. Is that a That's a hex.

**Dave Jones:** We need a hex. Nope. Loser. Here we go. Do it by hand. There we go. Um we will find, no doubt, a whole bunch of through-hole circuitry all DIP stuff.

**Dave Jones:** I mentioned this on the Amp Hour radio show this morning. Actually, I um I presume that all the chips will be lined up. Like you can sort of see through the grills on the front a bit, but all the chips will be lined up there in their lines.

**Dave Jones:** They'll be through-hole packages and it'll all be jammed on there. I'm sure probably like a four-layer board each one of them or something like that. Oh, does that come out?

**Dave Jones:** No. All right, looks like we have to There we go. And we've got four boards as we saw in the manual. So, not a hugely interesting teardown. I mean, you know, the more interesting stuff in this is actually how it like maybe the circuitry of how the emulation worked and stuff like that.

**Dave Jones:** So, you have to really go into There we go. Deep technical debt. Ta-da! Yep, there we go. Exactly as I thought. So, there you have it. There's the four boards we saw before.

**Dave Jones:** Nice little retaining clips to pull them out. I'll have to undo the screws there, but on the top here is our emulation programming board. Then we've got our emulation memory module next, and then we've got our logic analyzer module there, which of course has the various trace bits and stuff like that on it.

**Dave Jones:** And then down the bottom is our emulation processor. Uh, no, our CPM control processor module. So, there you go. Let's undo the screws on here and whip this sucker out.

**Dave Jones:** Going to have to I've used a hex driver here, but uh, this is how you designed Oops. Oh, no, it doesn't like that. Oh, not. Maybe I'm using the wrong Maybe it's imperial.

**Dave Jones:** I don't have an imperial that small. Damn it. Bugger. I think someone's had a Someone may have had a hack at those cuz this one work these two over here work fine.

**Dave Jones:** But the other ones don't. Anyway, I'm sure we can get those off with a pair of pliers. Anyway, this is how you designed stuff back then. No large-scale integrate Well, there's large scale integration in the you know various 40 pin dips and stuff, but everything else is going to be either gate array logic or 74 series logic.

**Dave Jones:** And this is how you laid stuff out. This is how you design stuff back in the day, you know? You didn't have Oh, well, you had FPGAs and stuff like that if you wanted to uh wanted to use them or you had PLDs and and stuff anyway that you could certainly use and they those gate array logics I can probably see I think I see maybe some gate arrays on there or

**Dave Jones:** something like that. So, but you design these all in neat rows like that and then you would typically have as we'll see on the board you typically had all all the traces on one layer going in one direction and on the other layer going all the other direction and that's one of the good uses for auto routers back in the day in the CAD software.

**Dave Jones:** You would let the auto router rip. So, you'd lay it out. You'd put a bit of sense and order into the layout of course, but you'd lay them out all nice and neat like that with their individual bypass caps on each chip.

**Dave Jones:** And then you'd tell the auto router go for it and it'd come back. You know, come back at the end of the day and your board would be done.

**Dave Jones:** So, I can get a couple of those out. They're probably held in at the back as well. So, I'm not sure what's No, there we go. We've got one out.

**Dave Jones:** That's neat. I like it. So, we'll have a look at each board in a bit more detail. It's got a daughter board on it. Oh, no. There we go.

**Dave Jones:** This takes a bit of force to pop out. Ta-da! That's our logic analyzer module. And these ones I'll have to get those out with the pair of pliers. And here it is.

**Dave Jones:** And this is a classic example of how you would design something back in the mid to late 80s. You would have you know a whole bunch of 74 series logic.

**Dave Jones:** This is the emulation memory board, of course, the EMM, and you would lay them all out on boards like that, and you'd plug them into a backplane rack-based system like this, cuz you've got all this circuitry, which you obviously can't fit on one board.

**Dave Jones:** There's no, you know, huge large-scale integration and stuff like that, so you lay them out on multiple boards, and very common to lay them out on these with these backplane bus connectors.

**Dave Jones:** Uh you know, you'd see almost every system back in the day, every sort of, you know, processor system that did all sorts of logic stuff like this would be pretty much designed exactly the same way, either a horizontal plug-in system like this or a vertical rack format one or something like that, but yeah.

**Dave Jones:** Classic old school. So, this here is the EMM or the emulation memory module. There it is. They call it the Just have a look at 92. There you go, 9235.

**Dave Jones:** I own a couple of these. Just have a look at the date code of a few of these chips. 9224. So, it looks like this one was manufactured late '92.

**Dave Jones:** There you go. That dates this thing, but it was certainly designed back in 1989. It would have had, you know, a uh you know, probably a 5-year lifetime or something like that before people moved on, but this one actually comes from the Australian Air Force.

**Dave Jones:** So, you know, they have to maintain these old systems. So, you know, there's probably still some people, you know, running these old tools even today because they still have to emulate the old, you know, the old microprocessors like the 8086 and various others.

**Dave Jones:** You know, if you're working on, say, ICBM technology for the military, intercontinental ballistic missiles, they're all based on, you know, '60s technology and stuff like that. So, you know, they still have to keep alive these development tools and that can be a big challenge in itself to maintaining old systems like that, especially in military type things where you have to keep things working for, you know, 10,

**Dave Jones:** 20, even 30 years or so. Crazy stuff. It can get real difficult. So, you know, don't throw out those old floppy disks. And you can see the classic card edge release clips like that.

**Dave Jones:** Absolutely classic. I can remember designing many a board back in the day to slot in there. We've got a metal strengthening bar across here. You'll notice that it's probably held in Yeah, it's held in three locations.

**Dave Jones:** So, there, there, and there. And that just strengthens the board at the back as it plugged in. Because when these, you know, on really big boards, they could actually sag in the middle.

**Dave Jones:** So, when you actually went a common issue back in the day is when you put them in the slide rails like that and you pushed them in, sometimes there'd be a lot of weight on these things, especially if they're, you know, I've done boards like, you know, double this size almost.

**Dave Jones:** And uh and in the middle they can actually sag like that if they don't have one of these strengthening bars and then then the connectors at the back like this don't line up.

**Dave Jones:** So, that can be an issue. So, that's why they've added that metal strengthening bar on the back just to keep it all lined up when you go to plug it in.

**Dave Jones:** Although these these connectors are pretty good. It's pretty, you know, self-aligning all that sort of stuff, but you really wouldn't didn't want to hear that big crunch sound as they sort of self-align when you pushed them in, but there you go.

**Dave Jones:** Attention to detail. Now, as I mentioned, this is a classic layout for a board of the era. This would be a four-layer board. You can actually see by the dark bits in dark bits in there.

**Dave Jones:** It's actually a Well, it's at least a four-layer board. They wouldn't have done it as a three-layer, of course. There'd be ground and power in there. So, two inner layers and they'd probably be very little few if any traces on the inner layer.

**Dave Jones:** It would just be the power plane and all of the routing is done on the top and the bottom layer. And as I said, this was a classic use for uh auto routers back in the day.

**Dave Jones:** You know how I'm not a big fan of auto routers. Well, this is where they came in handy cuz these weren't uh huge, you know, high-frequency uh systems. These are only, you know, 10 MHz, uh 20 MHz, something like that.

**Dave Jones:** With a big ground plane, lots of decoupling, you can easily get away with uh well, you you had to get away with it because you had to make these systems work.

**Dave Jones:** You had to use all these chips, spread them out over large boards like this with uh backplanes, but signal integrity wasn't on on the PCB level wasn't as huge a thing as it is today with uh with all of today's uh you know, high-speed uh serial lines, controlled impedance, and all that sort of stuff.

**Dave Jones:** These things weren't controlled impedance. You just laid it out with one big ground plane. You'll notice they've got decoupling chips on each one, but you'll notice how they're all laid out in nice lines like this.

**Dave Jones:** You would lay them out like that and typically um this is not a good example of uh that one, but then this isn't a particularly good example either. This is the processor, the emulation processor module, but they're laid out in neat lines like that.

**Dave Jones:** And if you didn't have the ground plane, often they would run the ground and power trace between each chip like that and run it across the board. So, you'd have one big uh power bus down the side and then you'd branch the power off along each particular chip like that, especially if you had uh multi-voltages or, you know, something like that.

**Dave Jones:** You'd typically might have a different voltage bus on each side or something like that. And you would route them under the chips. That's why you line them up like that so that you can run those two traces, ground and power.

**Dave Jones:** That's the only thing you'd have running under the chip in that direction like that and you dedicate a particular layer to that direction of running all of those power signals, but they obviously uh haven't done that here.

**Dave Jones:** They've just used a uh a one big power plane. It's all running at 5 V ground and power in there, but each chip they've given a bypass cap on each one, but they've still laid them out in neat rows like that because the routing algorithms, you would you know maybe I don't know if this one was auto routed or not.

**Dave Jones:** May or may not be. Um I've both used auto routers and laid out these types of ones manually as well. We'll flip it over and have a look, but as I mentioned back at the start, these things they're uh typically will dedicate one particular layer to a direction.

**Dave Jones:** So, this bottom layer here, you'll notice almost all of the traces go in this direction this x-axis direction. Here, you know, there's a few traces which sort of you know come down here like that and then go "Ooh, I'm going to go down there like that." But generally, the routing algorithms are quite advanced and they will optimize for these two-layer boards.

**Dave Jones:** In fact, um the CAD packages these days will probably still have the algorithms built in and you tell it that I want to run my traces in that direction on this layer and on the top layer you run them in the other direction there.

**Dave Jones:** So, here it is. All the ones on the top here pretty much all just run in this direction like this and this is why you know, you can't just put your chips anywhere willy-nilly.

**Dave Jones:** You have to actually especially with memory and stuff like this, this is all banked all common address and data lines. So, you're going to put them in um right aligned all the way up like that, and the buses just run directly through them like that.

**Dave Jones:** And absolute classic example of how to lay out one of these uh four-layer 1980s vintage digital boards. So, of course, you did have to put some thought into the layout of this thing, component placement.

**Dave Jones:** As I've always said, PCB layout is, you know, 90% component placement. You do good placement, the auto routing routines can work just fine. And of course, you know, if you had to get a signal from here right over to there, you didn't care how, you know, it might jump across on the bottom layer here, jump up back there, back back.

**Dave Jones:** It'll just, you know, as it's easy to find a route when you first start start laying out the traces, but when, you know, you get to that 90 80 90% routing mark, and well, you haven't got much room left, you really have to jump all over the shop here, but this one is quite efficient.

**Dave Jones:** I mean, they've It's probably put a lot of thought into it and laid it out by hand, because you can't see too many uh vias in there. There's a couple, you know, there's a few, but there's not like, you know, hundreds and hundreds of vias and stuff like that.

**Dave Jones:** So, they really, you know, I'd say somebody has probably manually uh routed this thing and took some pride. But for some complex ones where the signal integrity isn't critical, yeah, just let the auto router rip on these boards.

**Dave Jones:** It's fun to watch. And check out the ancient uh bypass capacitor package there. They've got standard uh 0.3-in spacing on these things designed to integrate and butt right up next to chips for high density in quote marks uh logic designs like this one.

**Dave Jones:** Absolute classic. You don't see packages like that anymore. I'm not even sure if you'd still be able to get that sort of package. And of course, we've got a tantalum here as well in one of these weirdos um you know bullet type packages.

**Dave Jones:** Okay, let's start out and look at each board in a little bit more detail look at some of the technology that's used on here. This is the top board.

**Dave Jones:** We looked at the EPM or the emulation programming module and you can see this is the one is where it connects directly to the pod using this dual height riser IDC connector like that.

**Dave Jones:** It's rather quite neat. Um you know not nothing fancy there at all. It's just a 40-way leave it IDC connector. We've got a couple of couple of dip resistor networks here series resistor networks.

**Dave Jones:** I'm presuming that they're uh uh I don't know. Yeah. Yeah, I think they're series resistor networks there and then we've got some 74LS stuff around here. It's all a lot of this is going to be standards 74LS logic.

**Dave Jones:** So if you want to know what each one of them does by all means go and look up the individual data sheets if you're not familiar with your 74 series logic.

**Dave Jones:** But anyway, they're using LS series logic for presumably around the interface stuff here. We've got some ALS. So we're really going to have a mix of 74 series technology here.

**Dave Jones:** I have no idea what these Sony parts are here. Check it out. Sony CXK5814P. Well, of course the dash 35 on the end of that's a dead giveaway that's some type of memory and I did Google it and sure enough it is a 2K by 8 SRAM.

**Dave Jones:** So very fast SRAM there on the input. Then we go down here and we find 74F series logic. So if you're using moved F stands for fast folks and they are incredibly fast.

**Dave Jones:** They take a lot of um uh current as well. So, you really need a bypass cap next to each one of those. So, and these ones with start stickers on them, there's a couple of them there and uh up there as well, they would be gate arrays.

**Dave Jones:** I'm like a PAL device or a gate array or something like that cuz um when they've got a serial number on them like that, you can bet your bottom dollar that they're programmable.

**Dave Jones:** So, let's peel that off and uh damn. Can't see it. One of those difficult to read ones. Let me try and get in there. Yep, there you go. It's a PAL.

**Dave Jones:** It's not even a GAL. It's a PAL 16R8. Absolute classic. They're just using that for some glue logic there. And if we have a look around the rest of the board here, LS123 up there with some uh large uh traditional radial caps there, but pretty much um 74F series um as far as the I can see pretty much in terms of uh you know, where it's deemed to be uh critical speed.

**Dave Jones:** There we go. We've got a uh Cypress um uh CY7C 122. Once again, it's a dash 15, so that would be a uh memory. I'm not going to bother to go look that one up.

**Dave Jones:** You can uh do that yourself. All 74F series logic driving the uh backplane down in there. And of course, each one of those has to have its own bypass cap cuz those things just gulp the current.

**Dave Jones:** But it looks like 74LS um with the We did have a um ALS up here. Where was it? Yep, there we go. So, we've got a small mix of uh different technology there.

**Dave Jones:** We've got they've chosen to use two 74ALS ones there instead of uh LS or F in that particular circumstance. Looks like some somehow coupled into that uh memory. And down here we've got the classic um it's an NEC branded, but it uh lots of companies made this.

**Dave Jones:** It's the classic 8255 programmable peripheral interface and this is was used on the IBM PC and standardized in part, you know, the Intel architectures and stuff like that, but they're just using it as a uh I think they've just standardized.

**Dave Jones:** They've got four of them here. They've just standardized on those as their um 8-bit peripheral addressable peripheral uh bus interface. I won't go into detail on how the 8255 works if you're not familiar with it.

**Dave Jones:** Um I'll link in the data sheet to it and you can check it out. It's just a a generic way for them to uh address and uh read stuff on data bus uh based systems.

**Dave Jones:** And there's the main clock up there, 24 MHz crystal oscillator. And that's pretty much all she wrote. So, it looks like we've got three combinations um of family on there, F predominantly LS uh second and then ALS as well.

**Dave Jones:** And next up we've got our emulation memory module which contains all the uh mapping memory in here. Once again, they've got some uh GAL stuff GAL or PAL stuff happening down in there, but these are all uh Sony uh CXK58257 uh 70 nanosecond SRAMs are more than fast enough for a uh 10 uh 10 MHz um emulation uh system.

**Dave Jones:** They decided to go with 70 nanoseconds there. Pretty bog standard they use. You could have substituted these with, you know, any one of dozens of brands available at the time.

**Dave Jones:** And what was that? It had 256K uh total. So, there you go. Once again, they've got all 74F series logic all driving that. I guess they determined that LS wasn't uh fast enough for any of that.

**Dave Jones:** All, you know, classic uh 245s and 244s and all sorts of stuff all over the place. Yeah, there's some more 244s and once again, they're throwing in just a couple of ALS, little bank of A ALS ones going down here and uh there is another I'm not sure what that one there is.

**Dave Jones:** Once again, it's another memory it's of sorts. It's got a dash 1 5, so anytime you see like a dash 1 5 on the end, especially in this old stuff, you can pretty much tell that that's a uh speed grade, and that will be uh it usually um dash 1 5 um means that well, that could mean 15 nanoseconds or it could mean 150, depending on the uh technology.

**Dave Jones:** Dash 70 here, I definitely know from experience would be 70 nanoseconds, but uh might try and uh Google that sucker. I'm not sure who that manufacturer is offhand. Well, there you go.

**Dave Jones:** That one is from a company called Pyramid Semiconductor. I'm not sure if they're still around these days, but uh yes, it is a um small uh SRAM. Yes, it is 15 nanoseconds.

**Dave Jones:** Very quick. Uh it's a 256 bits * 4, so it's you know, it's incredibly small. I'm not sure what they're using that for, just some sort of little small uh buffer or fast counter or something like that, perhaps.

**Dave Jones:** But uh here you go. We've got our 8255s again, so that's all our uh generic interface stuff. 74Fs all over the place, 4 8255s, and uh another memory down the bottom there, but yeah, I know.

**Dave Jones:** What can I tell you? Sorry, folks, it's all just 74 series logic. And here's our LAM or logic analyzer module. Once again, that's uh these are the uh trace um outputs here and the various uh sync and uh trigger um inputs here, but this is the logic analyzer module that allows them Oh, there we go.

**Dave Jones:** In power LAM, once again, we've got a uh Ooh, actually, that wonder wonder who or what that is under there. Just curious, cuz that looked like a National Semiconductor, and it is.

**Dave Jones:** There you go. It's a PAL 14 PAL 14L4. Woohoo! State-of-the-art technology, folks, in the late '80s. No FPGAs in this baby. And uh looks like yep, 8255s absolutely everywhere in bucket loads all over.

**Dave Jones:** Once again, we've got uh some more of those um 2K SRAMs there, I think. And yep, a whole bunch. There we go. Whole line of them, in fact. A whole line of SRAMs on the logic analyzer module.

**Dave Jones:** And if we look at the manual, we should be able to find um that is like the probably the trace buffer or something like that. And yep, I was right.

**Dave Jones:** This is the uh trace buffer memory along here because the manual as we uh saw earlier in the video, the manual um states that it's got uh 2K 2048 uh cycles deep by 76 bits wide trace memory.

**Dave Jones:** Of course, these are all uh eight bits each. So, in theory, you need uh nine and a half of these uh chips to make up that trace memory. But, they've got more than that.

**Dave Jones:** These are 2K by uh eight each. So, they've got 2 4 6 8 10 12 14 15 and they've got another one there, 16. But, I don't know how they're uh being used and implemented.

**Dave Jones:** But, definitely the trace buffer and a slightly different mix of technology again. 74S 260s. So, we've got 74S series logic mixed in with our LS and our F all around there.

**Dave Jones:** And we've got an NEC D71054C. Not sure what that is. Um could be another memory. It doesn't have a uh dash grade after that. Once again, these are all um late week uh '91 sort of manufacture.

**Dave Jones:** So, yep, 9223. So, there you go. We've got some more Sony 2K memory uh SRAM there all over the place but Yeah, oh, we got a lead something different.

**Dave Jones:** And last but not least we have our CPM board. No, it's not a control program for microcomputers as in the CPM operating system. It is the control processor module and tada we actually have something different in a genuine I might add check it out genuine 3M text tool socket there beautiful.

**Dave Jones:** I like that. What do we have? We have an Intel tada 80186. Now, there's actually no reason um that I know of why this actually needs to be an 80186.

**Dave Jones:** It doesn't need to be that particular type to emulate this processor because it's not doing emulation. It's just doing control. Basically, so that could have been any processor. They just happen to use an 80186.

**Dave Jones:** They probably use the same thing for their emulators for other brand microcontrollers as well not the 80880806. So, there you go. There's our system ROMs there. So, this just you know it's the main control processor.

**Dave Jones:** It's writing all those 8255 programmable peripheral interface chips on the various other boards and you'll notice that the uh all of the traces on there they've gone all a bit willy-nilly in there.

**Dave Jones:** Look at that. But anyway, I'm not sure what that puppy is there X2212P. It looks like a some sort of custom branded thing. I'm not actually not entirely sure what that thing is but yeah once again some 74LS series stuff surrounding that.

**Dave Jones:** The main clock is 16 megahertz for that system. They've got some memory there and looky down here, we have a Zilog SCC or serial communications controller. I love it.

**Dave Jones:** Copyright 1981. Things ancient, but then they were still manufacturing it more than a decade later in '92. Go figure. And that's running from a 3.68640 MHz crystal. Why that particular frequency, I hear you ask?

**Dave Jones:** Well, it's very common because that is a direct multiple of the serial UART interface. So, if you punch that in, 3.68640 on your calculator, and divide it by a typical UART baud rate, say 19,200, you'll get an exact binary multiple.

**Dave Jones:** So, you can get an exact frequency, and that's why they use that oddball frequency crystal there. It is quite common, but apart from that, folks, that is all she wrote on this.

**Dave Jones:** Sorry, it's uh not terribly exciting at all. There's a bottom board on there, but it doesn't look like there's anything interesting, just a few passives and some resistor networks for the uh um serial and parallel interfaces there.

**Dave Jones:** But, I suspect there'll be a lot of annoyed people if I don't just pop open this 3M Textool socket here. So, here's the bar, and hey, there we go.

**Dave Jones:** Ta-da! And there's our What is that? Like an LCC? Something like that. There it is. Look at that. Gold. Ah! Thing of beauty and a joy forever. And for those keen to see inside the power supply, I don't like doing clean power supply stuff.

**Dave Jones:** We've been looking at all this digital, but ah, nice change of pace. Look at this. Very neatly laid out, quite sparse. There we go. The main controller down there is a TL494, absolute classic, and uh very neatly laid out, heatsunk over here.

**Dave Jones:** You can see the seal pads on the transistors over there, along there. This is like a couple hundred watts. Well, I think this thing takes like 100 watts total or something.

**Dave Jones:** Takes a hell of a lot. But, they've actually gone to a bit of effort. Look, they've folded this case in here, which has the voltage selection switch on the back here, which protrudes from the back.

**Dave Jones:** The cable runs all the way down to the bottom down here. Looks like we have some more protection there. It's the main bridge rectifier. These are the two high-voltage caps.

**Dave Jones:** Couple of main switching transformers, but yeah, it's a power supply. And let's just have a quick look inside the emulation pod here. It just one of them was actually damaged, and there is actually a difference here between This is just the 8086 on its own.

**Dave Jones:** You'll notice it's got more circuitry around here. Lack of relays is a bodged part up in there. I'm not sure what that what that sucker is. We'll have to take a good look at there, but you can note the nice 3M text tool sockets.

**Dave Jones:** Lovely. I mean, I got this whole thing for 99 cents. You've got to be kidding me. Um but, the Yeah, the one with the 8087 doesn't have nearly as much circuitry around here, and it's got three relays up here on the top.

**Dave Jones:** So, I don't know. They're probably switching power or doing something else. Not quite sure what. Resistor network down in there. But, yeah, it's basically a 74ALS 244s, 74ALS 257s.

**Dave Jones:** And, you know, pretty much they're only just basically doing buffering on this board pretty much. So, we got 245s, 244s. So, yep, nothing particularly special. Oh, we've got a ULN2003A um transistor driver there.

**Dave Jones:** So, they and they'd probably be driving the relays actually, because the other board probably you won't find that. You will learn 2003 classic. I know, sorry. There's a uh little relay there.

**Dave Jones:** What am I talking about? It uh No, you don't really find it. It's got some extra circuitry. So, there are some uh differences between these two modules, certainly. So, there you have it.

**Dave Jones:** That's a look at the Microtek MICE or mice 16 8086F in-circuit emulator uh absolutely a classic. At first, well, I'm not sure this particular model, but their first model came out in uh 1981, according to the uh their website.

**Dave Jones:** They're still around, Microtek, and this is still all they do. They do uh in-circuit emulators, but you know, there doesn't seem to be much on their product page. Still, looks like they focus on like Intel and one or two other architectures.

**Dave Jones:** So, there you go. Um go figure. If anyone has any uh further info on this thing, especially uh schematics schematics or service manuals or anything like that, or per heck, even if you work at Microtek, still uh please let us know.

**Dave Jones:** Jump on over to the EEVblog forum and discuss it. And I'll uh whack in some high-res uh photos, as always. Um usually for my teardowns, I also take some high-res photos as well, and they will be on my Flickr account uh website, which is always linked in down below and on the website.

**Dave Jones:** So, hope you enjoyed that bit of retro development in-circuit emulator technology. Brilliant. Classic 1980s. Catch you next time.
