---
video_id: O4xERdjPZHg
title: EEVblog #1111 - World's First Microcontroller & Electronic Game
url: https://www.youtube.com/watch?v=O4xERdjPZHg
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 24, "3": 34, "4": 48, "5": 61, "6": 79, "7": 93, "8": 113, "9": 134, "10": 147, "11": 169, "12": 190, "13": 202, "14": 213, "15": 222, "16": 241, "17": 265, "18": 277, "19": 288, "20": 304, "21": 315, "22": 323, "23": 331, "24": 342, "25": 360, "26": 369, "27": 386, "28": 398, "29": 411, "30": 421, "31": 434, "32": 447, "33": 453, "34": 465, "35": 482, "36": 497, "37": 504, "38": 527, "39": 538, "40": 549, "41": 560, "42": 581, "43": 591, "44": 601, "45": 614, "46": 625, "47": 635, "48": 650, "49": 662, "50": 675, "51": 685, "52": 702, "53": 714, "54": 729, "55": 739, "56": 749, "57": 763, "58": 775, "59": 789, "60": 802, "61": 815, "62": 824, "63": 836, "64": 849, "65": 870, "66": 886, "67": 896, "68": 924, "69": 933, "70": 951, "71": 966, "72": 977, "73": 989, "74": 1002, "75": 1014, "76": 1022, "77": 1032, "78": 1043, "79": 1053, "80": 1067, "81": 1087, "82": 1100, "83": 1115, "84": 1124, "85": 1144, "86": 1155}
---

**Dave Jones:** Hi, it's video number 1111. You know what that means? It's the end of four-bit counting. We're flipping over to the fifth bit. Well, we would be if we actually counted EV blog episodes in binary, but we don't.

**Dave Jones:** Meh, details. It's video number 1111. So, I thought we'd take a look at the world's first microcontroller, which just so happens to be a four-bit microcontroller, none of this eight-bit rubbish.

**Dave Jones:** And to go along with it, I thought we'd take a look at the one of the world's first electronic games to use a microcontroller. The Merlin. Check it out.

**Dave Jones:** Who remembers the Merlin? Fantastic. Came out in 1978. The Merlin was released in 1978 along with the famous Simon game as well, which is a much simpler game. They basically came out the same time.

**Dave Jones:** And whilst technically they weren't the first games on the market to use a microcontroller at the time, they were the two games that became massively popular because of their functionality and their low price bracket.

**Dave Jones:** The Merlin and the Simon were about $25 US at the time. Some companies were even selling it at close to its cost price of around about $20 US. And both of them just so happen to use the world's first microcontroller, the Texas Instruments TMS 1000.

**Dave Jones:** So, let's take a look at it. The Merlin actually was the best-selling toy in 1980, selling 2.2 million units. It was phenomenally popular. I had one of these as a kid.

**Dave Jones:** It was absolutely remarkable. I was just amazed that a computer inside like a toy. There's a computer in here. Cuz you got to remember, this is 1978. And whilst like 1977, the year before, was famously the year that the Commodore PET came out, the Apple II, the Tandy TRS-80 Model I.

**Dave Jones:** So, you know, computers were out there, the Atari 2600 uh video game, of course, came out, but these were relatively expensive items. So, you know, people knew what computers were, but to get a computer in a toy that cost like 20 to 25 dollars was mind-blowing.

**Dave Jones:** The Merlin was actually developed by Bob and Holly Doyle, who formed an independent game company a few years earlier along with Holly's brother, Wendell Thomas, and they were contracted to Parker Brothers.

**Dave Jones:** At the time, Parker Brothers said, "Hey, we want one of these electronic games." In fact, they had actually developed an earlier game to this called Sector, or it's what they wanted to call it was Sync the Sub, and it came out slightly before the Merlin, I believe, but then, you know, it wasn't hugely popular because it it didn't it really only appealed to certain niche market, whereas they wanted something that would

**Dave Jones:** every kid would want for Christmas. And so, they said, "Hey, give us your game ideas. What have you got?" And they developed the Merlin and showed them a prototype, and they went, "Yep, let's do that." And they had a lot more games than the six games in one that came with this, and there was a bit of you know, toing and froing over what games would be included in this, but

**Dave Jones:** this was more popular, I think, than the Simon cuz the Simon was basically a one-trick pony. It just did, you know, a simple memory type flashing light game. This actually had six games built in.

**Dave Jones:** Remarkable. So, Bob and Holly Doyle were both Harvard astrophysicists, and Wendell Thomas, he was actually a computer scientist from IBM. So, they went, "What do we do? Let's make games.

**Dave Jones:** There's got to be money in games." And sure enough, come certain night in 1978, there was. So, both the Simon and the Merlin used the world's first four-bit microcontroller.

**Dave Jones:** None of this eight-bit rubbish. Four-bit TMS 1000 processor. In fact, the Merlin uses a slightly higher memory version of that, the TMS 1100. And curiously, the microcontroller didn't actually come out in 1977 or 1978 when these made their Well, the first electronic games to use them made their appearance.

**Dave Jones:** It actually came out in 1974, basically 4 years earlier, but it it took those 4 years for the game industry to catch on and go, "Hey, we can use these microcontrollers in electronic toys, and they only cost a couple of dollars per chip, and they can sell a $20 item." Cuz as you'll see in the teardown of this thing, the microcontroller is does practically everything in this.

**Dave Jones:** So, they could really got to get their bill of materials cost down because the microcontroller had everything built in. It had the RAM, the ROM, and the IO. Everything you wanted, and that's all you had to use.

**Dave Jones:** A single microcontroller could do everything. And the rest of it was just some LEDs and some molding and cases and stuff like that, and you could sell it for like 25 bucks at retail.

**Dave Jones:** Crazy. Of course, we take that for granted now where you can buy a farting novelty gadget for $1 delivered on eBay, but back in 1970 uh eight, it was a huge deal, and everyone was amazed that you could get a computer inside a toy.

**Dave Jones:** So, here it is, and it really is a funky form factor. What I loved about this was the fact that it had these membrane touch uh keys, which I had no idea what membrane touch keys.

**Dave Jones:** Didn't even know the name for it back when I was a kid, but I thought it was just magic that you could just touch these. Like they didn't feel like a real button.

**Dave Jones:** For the time, it was absolutely magical. And the fact that there was an LED behind each one of these, and you could press the button and see the LED at the same time.

**Dave Jones:** IT'S LIKE, "WOW, HOW DID THAT WORK?" ANYWAY, um the form factor was uh designed, I believe, to be like a familiar uh at the time, like a like a phone handset.

**Dave Jones:** And apparently, um the they did show that yeah, it was a sort of, you know, kind of like a familiar form factor to people. It did have a DC jack or a battery eliminator on the side, and there was a power switch which, uh, confusingly, was not labeled at all.

**Dave Jones:** And, of course, it's got a, uh, what looks like a 57 mm speaker up in the top here. And, of course, like, you might think, "Well, why does it need such a big speaker?

**Dave Jones:** Like, I've got a speaker in my phone." Yeah, well, that's modern. Um, you know, electromagnetic speaker technology. Back then, it was like, "Yep, we're going to just use a paper cone, off-the-shelf 57 mm driver." And they just designed it around that.

**Dave Jones:** None of this buzzer, you know, piezo, uh, buzzer rubbish. Nope, genuine speaker. So, basically, it was just a two-part molding case. Of course, you have to get the, uh, price point down for these games are plus the, uh, back, uh, door as well.

**Dave Jones:** But, apart from that, a two-part molding, very large self-tappers, ooh, into plastic. I hate that snap. I hate it. But, whoop, yeah, there it comes out complete with the plastic on it.

**Dave Jones:** Ugh. So, it looks like it's got a couple of plastic clips at the end. All right, so let's open this up, and it should just Oh, we're in like Flynn.

**Dave Jones:** Check it out. Oh, hello. And, yeah, classic 1970s single-sided PCB, uh, construction, as you'd expect. Uh, just a phenolic-based, uh, PCB. Of course, that's done to, uh, get the cost down.

**Dave Jones:** You don't want any of that double-sided PCB rubbish, not in a consumer product. Um, and even today, you'll still find that a lot of consumer goods, you know, white goods, TVs, and things like that, use single-sided PCBs.

**Dave Jones:** Cuz it gets the cost down. And you can see that there's not much in here. There's the micro, uh, controller, as we'll take a look at, which was absolutely revolutionary for the day.

**Dave Jones:** It was so incredible that they actually got the price down. And they did it with the micro controller, but also did it with various other aspects. Actually, take a look at the rest of it here.

**Dave Jones:** There's our membrane keypad up our membrane keypad under there. They've got another Look at this, a complete molding like this. Another So, what's that? Like four moldings. They got the upper case, the lower case, this LED which is also used as the LED diffuser, and the back panel.

**Dave Jones:** So, there's four plastic moldings like that. But, the other thing about it is that you'll notice that the LEDs actually go into moldings on there not only to uh diffuser, but also to hold it in place so that you don't need any screws inside this thing.

**Dave Jones:** There's just the two screws to hold it together cuz getting that price point down is not about not only about putting it in the microcontroller with nothing else on there.

**Dave Jones:** There's just going to be some LEDs and a switch and that's basically it. The batteries are probably just power not even a voltage regulator in there, I doubt. So, they're just powering it directly from the batteries and not only to get the component uh bill materials cost down, but also um assembly time as well cuz the more screws you have if you have to put four screws in here to screw this board down,

**Dave Jones:** that's going to take uh time and time cost money. So, they do away with that with the big plastic molding. It makes sense. They needed sort of, you know, that anyway really to uh to get the diffusing on the LEDs.

**Dave Jones:** You could have used the internal diffusing on the LEDs, I guess. Um you know, the dome top on them just like that and you know, it might not been as as good, but you know, it still would have worked.

**Dave Jones:** Anyway, they got down. They figured they have to do that molding anyway, so might as well make that. Now, let's have a look at the There we go. There's our membrane keypad.

**Dave Jones:** And when I tore apart this as a kid, I thought this was absolute magic. I didn't know how it worked. I'd never seen a membrane uh keypad before. So, it rather than the uh conductive uh you know, like carbon of the day, this I I presume it's like some form of like silver or silver alloy, something like that.

**Dave Jones:** And they've got an inner sheet here, which is the separator, which just insulates the two like that because there's no insulation on these traces. They're all exposed. So, you need that inner one.

**Dave Jones:** Of course, these cost practically nothing, especially in like the inner sheet. So, the separators, and that's how they get the button. You just press down on that. Doesn't require much force, and that was magical.

**Dave Jones:** And of course, you could have the cutouts so the LED shines through. And at the same time as the LED shining through, there you go. You can just make contact just with those keys like that.

**Dave Jones:** Brilliant. Took them four revisions to get it right, though. Rev D. And is the PCB a Rev D as well? I don't know what that part number means. Anyway, you can see that uh Look at this.

**Dave Jones:** This has to be the world's largest solder mask expansion. Look at that. I mean, that's just incredible. None of this solder mask between pins rubbish that you get these days.

**Dave Jones:** They just didn't need it. This is all wave soldered. You can just tell by the the uniformness of the joints. And they obviously didn't have a problem with you know, bridging between pins or anything like that.

**Dave Jones:** But you know, they went to the effort to put the solder mask on there. And solder mask expansion around the flat flex connector as well. But apart from that, I mean, there's not much There's not much on here at all.

**Dave Jones:** Let's flip it over. And they didn't even bother with screws for the speaker as well. Just some double-sided sponge tape on the top and like a you know, a reasonably tight fit designed into there and just stuck on the top.

**Dave Jones:** Nice. But you can see No, there's no form of regulation or anything like that. The mic is powered directly from the batteries. Do they have a What's We've got one cap in there?

**Dave Jones:** It's like they wouldn't need that for decoupling. And another cap here. RC oscillator. and there's the brains of this thing, the Texas Instruments TMS1100. Of course, the TMS1000 was the world's first, uh, microcontroller.

**Dave Jones:** Um, what defines a microcontroller is that, as opposed to a microprocessor, is that a microprocessor needs external memory, RAM and, uh, program memory as well. Whereas, a microcontroller has those built in.

**Dave Jones:** Nowadays, you think of microcontrollers as having built-in analog-to-digital converters, you know, timers and serial UARTs and all that sort of stuff. But, back then, it was, you know, like, to have that sort of stuff, they didn't really have those, uh, peripherals back then.

**Dave Jones:** But, just having the RAM and the ROM integrated, in this case, it's a mask ROM. None of this reprogrammable rubbish. Flash wasn't invented yet. E-squared PROM wasn't invented yet.

**Dave Jones:** Um, and maybe they had a windowed version of this, like, like, for development, that would have cost a lot of money. But, this one would have cost them a dollar or two each.

**Dave Jones:** And, but they were mask programmable, one-time programmable. And, there's a more modern PIC microcontroller, and you can see the pin pitch difference there. So, you know, it's not your standard 0.1 in pitch, much finer.

**Dave Jones:** That was, you know, pretty advanced stuff for 1970. And, we've got a diode in there as well, or as I called them at the time when I was a kid, diodies, because I'd never heard anyone say the word diode before.

**Dave Jones:** So, you know, that's what I called them. Anyway, we've got a cap in there, ceramic jobby. What value? 100? Is that 100 n or 100 pF? This one looks like manufactured in Korea in the 8th week, 1980.

**Dave Jones:** It's a modern one. And, that matches the date code here, 5th week, 1980. In Singapore. I don't know why yours in Singapore. Singapore manufactured chips back then. It's quite common.

**Dave Jones:** So, here's our 100 pF cap on the back here. And, if you're follow the money from this pin here, let's go around. Always follow the money. Right into the basement car park at midnight.

**Dave Jones:** It's where all you find get all the good info. So, that's actually pin 20, which is the VSS or ground pin, and that goes over to the the switch the ground there.

**Dave Jones:** And you can see that the two oscillator pins 18 and 19 are actually shorted out. So, I didn't but do believe it's actually using the internal oscillator. But, it's also got a power on needs a power on reset.

**Dave Jones:** So, maybe that's what this chip this cap over here is doing. Plus the diode is part of that reset circuit, too. And because I know you want to know what the clock rate is, well, let's have a look.

**Dave Jones:** 340 kHz. Nice. Ah, screaming. And we'll just capture the speaker here. Ta-da! There we go. Wow, look at that. Ha-ha. And check this out. If we have a look at the original design patent for this thing, um there's three names on there.

**Dave Jones:** Bob Doyle, I don't know who Arthur Venditti is, but apparently Samuel Kelman was a designer at Parker Brothers, and apparently he's responsible for the futuristic design of this thing.

**Dave Jones:** And look, isn't it great? You can see that it's like it's very like Star Wars, you know, droidy kind of look. I just I love this. Anyway, it's just a design patent.

**Dave Jones:** It's not a actual patent for the game. The from the engineering staff at Texas Instruments Incorporated, and they show the die. Love it. Copyright 1976. And we can see here that the TMS 1100 is basically pin-for-pin compatible with the original TMS 1000, but it's got even though it's a 4-bit processor, it's actually 2K by 8 ROM and 512 bits of RAM, as opposed to I think it's half

**Dave Jones:** that in the original. Now, we can see just the internal uh block diagrams of how it works and it's a microcontroller cuz it has the built-in RAM and ROM.

**Dave Jones:** But, you'll see it's got nothing else. It's got no newfangled ADCs, no even simple UARTs or anything like that. There's many variants of this uh 1000 family. Some of them had higher voltage capability, open uh source and open drain outputs as well for driving uh you know, Nixie tube displays and all sorts of other stuff.

**Dave Jones:** And the standard instruction set for those playing along at home contains two two chapters of 16 pages each. Each page contains 68 8-bit words, etc. etc. But, it was a 4-bit processor even though it used an 8-bit uh instruction word.

**Dave Jones:** There's not exactly a lot of uh instructions here. It's It's okay. It does the business, you know, it's similar to any sort of like a modern uh PIC processor or anything like that.

**Dave Jones:** Similar, I think it's 40 odd uh uh in instructions or something like that. All the instructions actually executed in six clock cycles here. Um as you can see, there's the six clock cycles and it's split up into multiple phases.

**Dave Jones:** So, quite complicated phase clocking internally. But, yeah, I don't believe you have to really worry about that sort of stuff, but heh, stand to be corrected. And here's all the different uh variants on there.

**Dave Jones:** I thought it probably more than that in the end. But, uh as you can see, the TMS1100 here, uh nominal power supply 15 V. But, obviously operating at uh well below that cuz we're operating 6 V directly from the batteries.

**Dave Jones:** It has no problem doing that. But, uh to be operating at the higher voltages means it was fully compatible with like 4000 series CMOS logic and stuff like that.

**Dave Jones:** Very nice. Um nominal at 15 V, 105 mW. So, the processor wouldn't have been drawing uh much at all. Most of the power would have been coming from the LEDs.

**Dave Jones:** The LEDs weren't hugely efficient uh back in 1978. So, that's why they're a bit piss-weak on there. I remember back when I used it though, pretty piss-weak LEDs. They weren't very bright at all.

**Dave Jones:** So, maybe they're trading off some brightness with battery life. And the output drivers are more than capable, I think 10 to 15 milliamps each. They're more than capable of driving the LEDs directly.

**Dave Jones:** And if you want to see their development environment, here it is. They got a flowchart of how it all worked. There was a simulator apparently. And the Doyles actually developed this on an Intel development system.

**Dave Jones:** Don't know exactly which one, but it's probably would not be too dissimilar to the one that I just found at the computer museum warehouse closing thing. And apparently that was worth 25 grand at the time that development system just to develop for your microcontroller.

**Dave Jones:** Like crazy. And this is rather interesting. The instruction program will logic array. It's got a PLA in or a PLD basically. And they give this example of a BCD to seven-segment decoder here.

**Dave Jones:** And they're the fuse mappings in order to map the outputs like that. To have that built into a micro, that's pretty cool. And it's a very basic micro. Like there's no interrupts in this thing at all.

**Dave Jones:** So, all the logic would just be sequential. That'd be it. So, can you imagine what sort of effort would be required to hand code a game like this in assembly?

**Dave Jones:** They did well to get these six games into that 2K words. Awesome. Anyway, I hope you enjoyed that look at the Merlin 1978 four-bit processor technology. Oh, I I was going to like do some video actually just playing the games on this thing, but I won't include it here.

**Dave Jones:** Probably include that over on the second channel. Link at the end. So, you want to check out EVblog 2 to see that. Anyway, if you liked it, please give it a big thumbs up as always.

**Dave Jones:** Discuss down below. Catch you next time.
