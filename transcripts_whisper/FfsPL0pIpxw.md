---
video_id: FfsPL0pIpxw
title: eevBLAB #24 - PCB Wars! Altium Circuit Studio vs Autodesk Eagle
url: https://www.youtube.com/watch?v=FfsPL0pIpxw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 46, "3": 81, "4": 103, "5": 103, "6": 131, "7": 153, "8": 196, "9": 212, "10": 257, "11": 275, "12": 297, "13": 324, "14": 365, "15": 387, "16": 387, "17": 414, "18": 433, "19": 462, "20": 489, "21": 516, "22": 542, "23": 542, "24": 570}
---

**Dave Jones:** Hi, welcome to an EEVblab. I had to mention this because there are two big things that have happened in the PCB design space in the last week or two, and I thought we'd just take a look at them if you're not aware. Now, the first one is, oh, by the way, just ignore that board above me, I'm shooting another video doing a screen capture thing here.

**Dave Jones:** Anyway, two things have happened. The first one is that Autodesk have bought Eagle. They purchased Eagle from Element14 slash Farnells slash Newark, whoever you want to call them. They purchased it for around about 20 million, 22, it's in the 20 millions, something like that.

**Dave Jones:** Because, this came about because Element14 themselves were, slash Farnells slash Newark, were bought by somebody else and, well, yeah, okay, who cares about that? We talked about on the Amp Hour, I'll probably link it in down below. So, Farnells were bought out, and Farnell bought out Eagle a couple of years back, and so they owned Eagle, and the new owner of Farnells, I guess, went, well, we don't want to be in this, you know, PCB design space business, we just want to sell parts and do whatever.

**Dave Jones:** Which is fine, I reckon it's a good choice that they spun off Eagle. Now, they sold it to Autodesk, and Autodesk have a whole bunch of, they've got like circuit simulators, they own a bunch of companies, they're not a 123D thing, and they own Circuits.io, that's right, which is another product.

**Dave Jones:** So, they're actually getting really powerful, they now, the only thing that I'm missing, major thing that I'm missing, is a PCB design tool. So, now, Autodesk have bought Eagle, and a lot of people are worried about what's going to happen, and everything like that.

**Dave Jones:** So, that's change number one, and by the way, I'll link in this Art of Fruit blog, where they did an interview with Matt from, who's an ex-Altium guy, hi Matt, from Autodesk, asking questions about the changes and everything else. And it sounds like it's a reasonably good move, and they're going to, you know, start to improve things in the Eagle space.

**Dave Jones:** So, coincidentally, a couple of days after the announcement that Autodesk bought Eagle, Circuits.io, Altium, this is news number two. Altium, who had this ridiculous mid-tier program called Circuits.studio, that they used to sell through Element14, by the way, they used to sell it for like $3,000, US dollars, I think it was, it was a ridiculous idea.

**Dave Jones:** It was in the no-man's land, it was in the dead band of PCB tool pricing. And I think the number of people who actually bought it, I could probably count on both hands, I suspect. And I think, rumor has it, this was sort of pushed by Element14 at the time, because they had Eagle, they owned Eagle down in the low-end space, and they wanted sort of like a higher-end tool.

**Dave Jones:** So I think they approached Altium, and Altium said, hey, we can do a watered-down version of Altium Designer, let's call it Circuits.studio, and then they sold it exclusively through Element14. And I don't think they sold any of it. Which is, I told you so, because I did a video on this back in number 527 here, saying that anything over $1,000 was basically, you know, no-man's land, nobody would buy it.

**Dave Jones:** It had to be under that $1,000. So what did Altium do? Two days, a couple of days after this announcement from Autodesk and Eagle, bingo, they dropped their prices, slashed it by a third. It is now, check it out, this is the US site, it is now $995, and that's for a one-off thing, it's a perpetual license.

**Dave Jones:** Or you pay $150 maintenance per year to maintain it and get updates, and stuff like that. Brilliant move! That is really aggressive pricing, and for people who think Eagle's cheap, it's not. This now undercuts Eagle. If you have a look at Eagle prices, for their commercial licenses, okay, which is ones guys like me have to use, or anyone in business selling and designing anything you're going to sell, you need a commercial license.

**Dave Jones:** They want $820 here for the schematic and the layout, and you get the auto-router, everything else. Which sounds fantastic, but wah! Look at this, 160x100mm routing area, that's ridiculous! It's great if you want to do a shield, like an Arduino shield or something like that, but anything bigger than that, you have to go up and pay $1,640 US dollars for anything.

**Dave Jones:** I've been saying this on the Ampower and the forum and everywhere else for a long time, the Eagle pricing is ridiculous. It's an absolute joke, because if you want, if you have a single-sided board, a single-sided board with two components on it, one at either side and they're 161mm apart, you need to buy the $1,640 license.

**Dave Jones:** It's just, it's ridiculous. So anyway, Altium have now released Circuit Studio. Now that Element 14 no longer owns Eagle, they aren't setting the price, because if Element 14 sold Circuit Studio, Altium Circuit Studio, at the $995 price point before, nobody would have been buying Eagle.

**Dave Jones:** So now, Element 14 don't own Eagle anymore? Meh! Let's sell Circuit Studio for $995. So I guess Altium's hands aren't tied anymore in regards to the pricing of that. So this is a huge move. Eagle has massive competition now in Altium's Circuit Studio.

**Dave Jones:** Now, of course, Altium didn't listen to me properly, and they released Circuit Maker, which, actually, hats off to them. They made it completely free, no commercial restrictions, anything like that. It's a completely free version, but it's cloud-based, online, must-share your files, all that sort of stuff.

**Dave Jones:** And it didn't really gain the traction that they were hoping for, I don't think. I'm not sure the number of users, maybe they'd like to tell us. But, anyway, I don't think it got the traction that they were hoping for. But, the new Circuit Studio, which, by the way, they, ta-da, gave me a license for, so I now have a commercial license to play with Circuit Studio now.

**Dave Jones:** I'm quite excited. And we can, hopefully, here we go. Oh, hello, there we go. I can now play with Circuit Studio, but that is very aggressive pricing for a thousand, under a thousand US dollars for a commercial PCB tool. Now, there are limits to this.

**Dave Jones:** If we go in here, I think, here we go, miscellaneous technical page, it's one of these too. Anyway, I may not bore you with the details, but Circuit Studio is effectively, uh, Altium, Altium Designer stripped down. So there, um, there is a comparison sheet, sorry I should have had it open before here, but, uh, yeah, there is a comparison between the two tools, and, um, here it is.

**Dave Jones:** Is this it? No. Anyway, I'll post a link down below. There is a comparison between Circuit Studio and Altium Designer, and what things Circuit Studio doesn't include from Altium Designer. Some of them sound okay, some of them sound a bit worrying. So, anyway, I haven't tried it out, uh, fully yet.

**Dave Jones:** I will be doing this in, uh, a future video, absolutely no doubt about that. And, uh, we'll be having a play around with, uh, Circuit Studio and, uh, see how it goes. So I'm rather, uh, excited by that. And so, really interesting news, it could lead to, uh, price wars and things like that in the PCB design space, and that's only a good thing.

**Dave Jones:** By the way, Matt from Autodesk, he is on the EEVblog forum answering questions and, uh, stuff like that. If you want to talk to, uh, Matt about, um, auto, about the new Eagle, and he's listening to feature upgrades and things like that. So I'm not an Eagle user.

**Dave Jones:** Um, I might do maybe a shootout between the two in the future once I get, uh, used to both of them, because I haven't used Circuit Studio before. But it's basically Altium Designer with the ribbon interface, uh, that's used on Circuit Studio. That's the main difference between, uh, that.

**Dave Jones:** But it's, I believe it's based on the Altium Designer code and not the Circuit Maker, uh, code. So it's basically a stripped-down Altium Designer. Anyway, fantastic news, uh, and what people have been waiting for under a thousand bucks for a, um, hopefully professional-level PCB design, uh, tool.

**Dave Jones:** So, yeah, look out for future videos on this. Very exciting, if you want to discuss it, links down below, all that sort of stuff. And, yeah, sorry Altium, I told you so. Catch you next time.
