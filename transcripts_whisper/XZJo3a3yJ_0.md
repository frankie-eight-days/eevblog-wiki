---
video_id: XZJo3a3yJ_0
title: EEVblog #96 - The TI LaunchPad MSP430 Development Board
url: https://www.youtube.com/watch?v=XZJo3a3yJ_0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 47, "3": 75, "4": 92, "5": 114, "6": 134, "7": 152, "8": 166, "9": 190, "10": 216, "11": 228, "12": 253, "13": 266, "14": 284, "15": 301, "16": 326, "17": 338, "18": 360, "19": 378, "20": 400, "21": 412, "22": 439, "23": 461, "24": 476, "25": 501, "26": 520, "27": 544, "28": 566, "29": 584, "30": 601, "31": 620, "32": 637, "33": 655, "34": 674, "35": 694, "36": 713, "37": 729, "38": 746, "39": 762, "40": 775, "41": 795, "42": 817, "43": 838, "44": 854, "45": 865, "46": 886, "47": 903, "48": 924, "49": 941, "50": 959, "51": 980}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for another stream of consciousness drive time rant and once again this one is about a post I saw on the forum and then

**Dave Jones:** led me to a whole bunch of other places and it's all about the big, well, there's some buzz anyway going around about the new Texas Instruments TI launchpad development board, development platform. It's basically TI's big push, although they don't, I don't think they actually say it, but it's TI's

**Dave Jones:** big push into the new hobbyist slash hacker slash maker market, the very low cost market to get people into micro entry-level microcontrollers and the new TI value line series of little 16-bit micros, very cheap ones. They claim they start from 25 cents in, I think,

**Dave Jones:** thousand quantity or something like that or it might even be much higher than that, but that's a bit of a crock for starters because that, you know, yeah, you can get, you might be able to get a 25 cent micro in high quantity, but that's only for a half kilobyte flash micro.

**Dave Jones:** It's got no ADC in it or anything like that, I think. Don't quote me on that, but yeah, once again, that's just all that marketing jazz. But anyway, the new launchpad board, it's big, huge selling point is that it's a complete development board and environment, comes with a free trial, you know,

**Dave Jones:** limited software, C software compilers and it's only four dollars and, what is it, four dollars and thirty cents. You've got to be kidding me. And the amazing thing is that's not just for the board either, you know, you think that would just be for the little, the little board, like an Arduino

**Dave Jones:** style board, but it's not. It comes in the proper big box thing, it's got like a little getting started guide, it comes with a USB cable and, you know, and it comes with two micro chips, it's got a little, it's got a little 20 pin socket on the board where you can plug the micro in, it comes

**Dave Jones:** with one of them's already pre-programmed and the others, just a blank one. One is the highest end one, the two kilobyte chip with the ADC and the other one's not with the ADC, I think. And yeah, four dollars and thirty cents and that includes shipping.

**Dave Jones:** You've got to be shitting me, right? TI are obviously doing this as a loss leader to get people into micros and, hey, my hat's off to them and to get a product to market for that price in people's hands for four dollars and thirty

**Dave Jones:** cents is insanely good. So my hat is off to TI. It's, I reckon, it's fantastic. But there's a few problems with that which I'll talk about. Now, are TI making any money on this? Well, clearly no, because if you do the basic math, right, even if they make a hundred thousand of these units and

**Dave Jones:** they make a dollar, let's say they make a dollar clear profit on each one, which they may not be doing, I don't think, I'd be very surprised if they're making a clear one dollar profit on each one. But let's assume they are, that's a hundred thousand dollars.

**Dave Jones:** Now, I can tell you for nothing that it costs them more than a hundred thousand dollars to bring this to market. By the time they, you know, they have a design team, they design it, the marketing people get involved and the, and the, you know, they design all the packaging and they do a couple of spins and they do this

**Dave Jones:** and that and they write the, you know, they write the little onboard programmer firmware and they do the example files, etc, etc. It cost them a lot more than a hundred thousand dollars to bring this four dollar board to market. You can bet your bottom dollar.

**Dave Jones:** So you can guarantee TI are not making any money on it. So they're not in it to make money. So they're clearly in there to, you know, appeal to this new, I've talked about this huge market before, which has sprung up in the last

**Dave Jones:** four or five years from practically nowhere. This hobbyist hacker slash maker market is massive now and I think they realize that. And smart companies, TI seem to be one of them, that the smart companies will know that, you know, you have to get the young people involved in your chips.

**Dave Jones:** You know, even if they're not engineers or they're not students, if they're hobbyists or whatever, it doesn't matter. If you get those people using your chips, then they will, they have a very high probability of sticking with your brand and your chips for the rest of their career because they

**Dave Jones:** they'll often go on to be, you know, engineers of note or working at companies and then they'll bring their chip into the company and so on. And you can make, you know, it's a very long-term vision thing to get something like that. And TI are really trying to hit that.

**Dave Jones:** So thumbs up to TI for that. And it's just fantastic. Now clearly this is being pitched against the Arduino board, which is massively popular. It's selling tens of thousands. It may even be in the hundreds of thousands. I don't know, but it's a huge seller.

**Dave Jones:** Now, by the way, TI have made at least 10 or 20,000 of these. And how do I know that? Because if you look at the Mouser website who they're selling it through for $4.30 plus I think a dollar something delivery or something even through Mouser, which is a bargain.

**Dave Jones:** Mouser have ordered 9,800 and something of them. If you look at their stock, that's on its way. And TI are selling it, I think, direct from their own website as well. Now that means, you know, they've made, you know, 10 or 20, they've made like 20,000 of

**Dave Jones:** these at least clearly off the bat. And I read, you know, without a doubt they are pitching it against the Arduino. And they know it, but they're not going to say that. But they definitely are pitching it against the Arduino. How could you not be?

**Dave Jones:** It's a similar sort of form factor. It's got the programmer built into it, you know, it's got the USB host, it's got the USB interface, but it doesn't have the Arduino style development environment. But hear me out. Now, the, you know, TI will never admit that they're pitching it against that, but that's what they

**Dave Jones:** are. Now, I think they have made a massive, massive mistake by not making their expansion header connector. They've got, you know, a two row single inline expansion header on there, which breaks out all the I.O. and everything. And they've put it in two rows, you know,

**Dave Jones:** on top and below the board, the top and bottom edges of the board, just like the Arduino, but it's not compatible with the Arduino shield system. Now, I think this is a huge, huge mistake because there's a big market out there for all these Arduino shields.

**Dave Jones:** And if TI just, even if they didn't advertise it, if they just, it just so happened to match the Arduino, you know, shield form factor, the pinout, then they could have made use of all these shields. And, you know, companies like, you know, Artifruit and other companies that are developing, you know,

**Dave Jones:** selling and doing all these Arduino shields, there's dozens of them, they could make the hobbyists, the target market, could make instant use of those boards. And I think it's suicide that they didn't include that capability. But I do understand that TI is a big company, they have a

**Dave Jones:** big company mentality, you know, they have that Dilbert-like management system, as all big companies do. And I can certainly understand where, why they didn't do it. I still don't agree with it. Um, but I, I can, I can see where the company, you know, I've worked in big companies, and that's,

**Dave Jones:** that's how it works. And I can just picture some, maybe some poor development engineer in the design, in the development team, at the meeting for the, you know, the design review spec meeting for this thing. And maybe, you know, saying, oh, what if we, you know, nervously puts up his hand, oh,

**Dave Jones:** what if we just make it compatible with the Arduino shields? And then, you know, big debate ensues, and he gets shot down in flames, and he or she gets shot down in flames. And they've learnt their lesson. So I can just picture that happening at the TI design review

**Dave Jones:** meeting, because I'm sure they've considered it, you know, should they make it compatible with the Arduino? And, um, and they obviously didn't. I'm sure they made a conscious choice not to do that for some reason. I'd love to hear why. It'd be the usual big company spin,

**Dave Jones:** I'm sure. But hey, even the launchpad name, right? You know, I'm sure I can just picture the, the marketing meetings, you know, to come up with that, you know, launchpad, oh, it's got pad in it, so it'll be like the new iPad. That's a, you know, it's a big keyword, and a big, you know,

**Dave Jones:** mental driver for people. And then, you know, launch, oh, it launches people into the world of microcontrollers. It launches new people into our product line, and our vision, and our synergy, and strategy, and all that sort of marketing bullshit. And so I found that quite

**Dave Jones:** hilarious, the, uh, the name launchpad. I, I thought, yeah, that's just got, that just smacks of marketing all over it. And, um, yeah, anyway, I think it's a big mistake that it's not Arduino compatible, because if it was, then, um, I'm sure within a couple of weeks,

**Dave Jones:** you'd probably have some nerd out there write, uh, you know, rewrite the Arduino, um, you know, write an Arduino bootloader for it, or something like that, so it's compatible. I'm not sure if that's possible with the, um, with the TI chip they've got on board there, but, um, if, if it

**Dave Jones:** is possible, I'm sure someone would have done it, um, and there's less reason to do that if it's not Arduino, uh, compatible. So, you know, it's, ah, it's a real shame, because I think they really could have, um, given Atmel, who, whose main line of chips is in, in the ATmegas, are in the

**Dave Jones:** Arduinos, and I, I think they could have really given them a big kick up the arse by, hey, look, you know, here's our, uh, you know, Arduino compatible solution, you know, and it's a real shame. Anyway, you know, it's crazy. And the other problem with this Value Line series of chips is

**Dave Jones:** that they're currently, the ones currently available, the ones you can buy are only the maximum, um, code size is two kilobytes of flash, and that's, you know, that's not much. They reckon they've got two other series coming out in this Value Line one, which will go up to 16 kilobytes.

**Dave Jones:** I think there's a mention of a touch, um, you know, a capacitive touch interface as well, and other stuff, but hey, I'll believe it when they're actually, when I can buy them from Mouser and Digikey, otherwise they, they're just vaporware, really. And, you know, so I think it's a bit of a

**Dave Jones:** shame. And the other thing is, the Value Line chips are available in DIP format, okay, which is great, which aims it clearly at the, you know, that hobbyist hacker, easy to use, even professional engineers love DIP, because they can just whack them on a breadboard and use them, you know, having,

**Dave Jones:** you know, I think you still have to have a DIP version, but for their production versions of the chip, they've gone with, um, TSOP and QFN, and I hate those. Why can't they have, these are only like 16-20 pin chips, why can't they have an SO package?

**Dave Jones:** Much easier to use, much easier for people to transition from DIP into surface mount, whereas now they've got to go to, you know, TSOP, I'm not sure what the pin pitch is, but it's a, it's a fine TSOP, uh, TSOP package, and a QFN's

**Dave Jones:** right, just a pain in the arse, and, ah, I don't like it. Why? SO, please, DIP and SO. God, you went with trouble to do a DIP. Ah, so, yeah, I'm not sure they put a massive amount of thought into that one, um, so I don't know who, what part of TI was, was driving that, but anyway, I think that's a big

**Dave Jones:** disappointment too, but, um, yeah, I really, I think it's quite exciting, this launch pad at $4.30. Now, here's the other thing, which brings me on to this. Now, okay, they've met this fantastic price point, brilliant, absolute brilliant, you know, way to market your product and get it in people's

**Dave Jones:** hands for, you know, the price of a cup of coffee, it's incredible, but what happens when you want to buy more of them? Okay, they're only $4.30, but the fact is, it comes with that huge box, okay, well, you know, it comes in a proper box with some getting started manual, I'm not sure

**Dave Jones:** how many pages it is, but, oh, it's just, it's just from a waste point of view, just from an environmental waste point of view, I don't want to get into that sort of stuff, but that pisses me off. Can you just buy the board?

**Dave Jones:** It would have made a lot more sense if TI simply, um, sold the board and maybe, you know, just the board for $4.30 or something like that, and then maybe the entire kit for, with the USB cable and the manual in the box for $9.95 or something like that, but, yeah, I'm not

**Dave Jones:** sure if you can just buy the board, I haven't looked at the TI online shop or mouse or anything like that, so I may be talking out my ass here, but, um, I possibly don't think I am, so it just would have been nicer if they just sold the board, because that's all people want, you know, people

**Dave Jones:** don't, you know, and look at the TI website, they've got this unboxing video, they've got one of the TI guys there unboxing the damn thing, oh, bloody unboxing, it's so iPad geeky, you know, consumer like, it's, it's not what engineers want to see, they don't care what's in the box, they want to

**Dave Jones:** know what the, you know, they want to know, they want just the board and they want to be able to just use the board and they want to know what chips it comes with and all that sort of stuff, unboxing my ass, anyway, there you go, the new TI Launchpad, it's, you know, it's a really

**Dave Jones:** great introduction to the TI MSP430 line of chips, which are a brilliant line of chips, and I think it's going to be very popular, but if they just put a bit more thought into it, had a few more, you know, had bigger balls to say we're going to make it Arduino compatible,

**Dave Jones:** then really, they could have had a massive winner, well, I think they're going to have a winner anyway, but it could have really, you know, help perpetuate that, um, the Arduino kind of hobbyist hacker maker market even further than it's going to, so really good and some bad aspects

**Dave Jones:** at the same time, same with every product, there you go, see you next time.
