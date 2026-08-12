---
video_id: Z9itl1M75_Q
title: EEVblog #1077 - Dumpster PC Repair
url: https://www.youtube.com/watch?v=Z9itl1M75_Q
source: youtube-asr
timestamps: {"0": 0, "1": 25, "2": 35, "3": 46, "4": 60, "5": 77, "6": 86, "7": 95, "8": 106, "9": 119, "10": 129, "11": 141, "12": 158, "13": 171, "14": 182, "15": 194, "16": 204, "17": 219, "18": 236, "19": 247, "20": 260, "21": 274, "22": 286, "23": 297, "24": 313, "25": 337, "26": 352, "27": 372, "28": 387, "29": 399, "30": 411, "31": 425, "32": 442, "33": 459, "34": 474, "35": 488, "36": 498, "37": 512, "38": 521, "39": 530, "40": 552, "41": 563, "42": 576, "43": 584, "44": 599, "45": 607, "46": 617, "47": 639, "48": 649, "49": 663, "50": 677, "51": 686, "52": 698, "53": 720, "54": 737, "55": 749, "56": 767, "57": 784, "58": 796, "59": 807, "60": 820, "61": 832, "62": 870, "63": 881, "64": 893, "65": 906, "66": 916, "67": 928, "68": 941, "69": 956, "70": 965, "71": 981, "72": 990, "73": 1005, "74": 1022, "75": 1036, "76": 1050, "77": 1066, "78": 1083, "79": 1091}
---

**Dave Jones:** Hi, just a dumpster dive and follow up. Uh this Dell Optiplex 990 which I found in the dumpster. It was Dell's top of the line office 900 series you know slimline PC Intel Core i7 in here and I had a quick look in a previous video where I scored two which the other one was a HP one which had an i5 something or other in it with like a

**Dave Jones:** pass mark of like 7000 or something like that. I'm currently actually using that. I put upgraded graphics card in it and currently using that as my main lab capture video capture PC here.

**Dave Jones:** So, I thought I'd have a look at this one and one thing I didn't take a look at last time was the actual processor inside this thing. It turns out it's actually an i7.

**Dave Jones:** I I won't show you the if you can't read that, sorry, but it's an i7 2600 which has a pass mark rating of like 9000 or something. It's like oh 8000, sorry.

**Dave Jones:** 8200 or something. It's pretty darn good and I've also got this motherboard up here as well which has the exact same socket 2011 i7 2600 processor in it. Um as well as in the really kick ass case here.

**Dave Jones:** Look at all the drive bays, fantastic. But unfortunately, I think there's something wrong with that motherboard cuz it doesn't seem to power up. I've tried different power supplies and everything and the power supply is hiccup.

**Dave Jones:** So, I think it might have some sort of remove the CPU, remove everything. I I think there's some sort of issue with that. Anyway, I thought we'd just take a look at it.

**Dave Jones:** I've well, this one I have opened up the power supply. So, let's take a squeeze at that. So, the symptom with this PC is that it just simply wouldn't switch on.

**Dave Jones:** So, of course you instantly suspect the power supply. This is actually a Delta power supply. You can see that in there and you know, top quality power supply works, looks really well designed and manufactured.

**Dave Jones:** Look at all the gunk in there for the stuff and there's a fuse down in there. There it is and I've scraped away. It's all heat shrunk, which is fantastic.

**Dave Jones:** So I couldn't actually probe it unless I took the board out. That's a bit much. So I just scraped away access to the top and bottom terminals there and we can get in there and measure that cuz that's well, the first port of call really.

**Dave Jones:** But yeah, I like the supply. Looks well designed, well manufactured, but you'd expect that in a top of the line Dell office PC. Okay. Let's go in there and ta-da!

**Dave Jones:** That is yep, that's blown. There you go. But why is it so? I mean, is it was it just some sort of power on surge or something like that that caused, you know, fatigue in the fuse, caused an issue like that?

**Dave Jones:** That's possible. Or is there some, you know, major fault somewhere that blew the fuse? Only one way to find out. Replace it, power it back up. If it blows again, you know there's something else.

**Dave Jones:** Wow, this is actually quite difficult to get out. And they've got some sponge under there. Look at that. Don't like it's not really insulation, so I'm not sure what the deal is there.

**Dave Jones:** But anyway, look at all this. It's just like this was all wired in place after the fact. I don't think that's a connector in there. I think that's hard wired in.

**Dave Jones:** So that's a real pain in the ass to service. Jeez. Looky what we have here. Look at that. That looks like it's had the snot blown out of it.

**Dave Jones:** Aha! Well, there's your problem. Wow. Two capacitors. They're Are they like high voltage ones? I don't know, but they've they're really gone to town. No wonder the fuse blew.

**Dave Jones:** So, maybe I've done videos on this before. Ceramic capacitors can fail short and cause a real problem, but I'm going to get like clean that out, sort of scrape it out and suck those off.

**Dave Jones:** Nothing like sucking off a dead capacitor. There we go, got them out. That doesn't look pretty, does it? Is there a trace running I think there's a trace running under between them.

**Dave Jones:** That's interesting. Anyway, I'm pretty sure that these suckers have overheated and melted some like most likely shorted out. Of course, the power delivers in there, they heat up, and it's melted some of that foam underneath them.

**Dave Jones:** Not a big fan of that foam. Now, we don't directly know what the voltage of these caps are, but we can have a look at the placement here. And you can see this uh trace going off here.

**Dave Jones:** They've got a like a star grounding point here going off. There's actually looks like two of those going off those star grounding points to elsewhere way up in the circuit.

**Dave Jones:** And this one here, look at this. It looks like it's directly connected there. Bit hard to see on my camcorder screen. I'll confirm that by buzzing it out, but that looks like it's directly across a big filter cap on the top.

**Dave Jones:** Aha, is that the main DC filter cap? If so, that would explain why we blew the snot out of the uh 1206 ceramic capacitor there cuz it would have been like a high voltage like 400 V cap, and any direct fire in that, bam, it's directly across that rail, it's going to take out the uh fuse, definitely.

**Dave Jones:** So, yep. And sure enough, yep, it's the main filter cap there, and yes, it's a uh 150 mic 420 V job. So, there you go. They would have been high voltage ceramic caps.

**Dave Jones:** I don't have in my junk bin. I don't have such high voltage 1206 ceramic caps, but because it's basically just some you know higher frequency lower impedance stuff across the main filter cap there, we can simply leave that out and it should still work.

**Dave Jones:** And as for the one next to it, well, follow the money. That goes up to there. What's that between there and there, perhaps? Uh no, you're probably screaming at me cuz you're watching in high def and I'm watching in the on the camcorder screen.

**Dave Jones:** No, these two caps are in parallel and that's actually not connected to the main filter cap there. It's actually connected to there. So, I need to follow the money and see where that goes.

**Dave Jones:** Deep throat time. Just follow the money. Okay, so it looks like that bugger's off under the hot snot down in there. Bugger's off to that IC there, that pin over there.

**Dave Jones:** So, I look, I don't know. I'm not going to pull out a try and reverse engineer it or pull out a typical schematic or whatnot. So, yeah, I'll just choose you know the highest voltage cap I've got to hand and whack it in there.

**Dave Jones:** And thanks to AVX who sent in this kit among many others. I've covered these in a previous mailbag with the flexible termination on these things, automotive grade, fantastic. Let's just go for a 10 nanofarad 200 V 0805.

**Dave Jones:** 200 That's I think more than overkill, but anyway, so we'll just solder a couple of those back on and she'll be right. Well, hopefully. Actually, I suspect that only one of these may have failed because I the other one, well, one of them there measures 33 n.

**Dave Jones:** There it is. Um that one is still good. So, yeah, I suspect that uh well, our 10 amps probably that's all I've got in that uh high voltage. This one I use as higher voltage uh one as possible.

**Dave Jones:** But, I think yeah, we've only got the one fire there, and uh the other one next to it is it's pretty much fine and dandy. There's just a recap of the uh soft termination system there that uh prevents PCB warping uh from cracking the uh ceramic cap.

**Dave Jones:** Here it is. Check it out. It's a proper ceramic job uh 6.3 amps. So, yeah, um we might be able to get those end caps off and uh actually stick it back in.

**Dave Jones:** Reuse those, can we? Hmm. Well, check it out. My junk bin came through. I just so happened to have exactly a 6.3 amp um uh ceramic HRC fuse. Beautiful.

**Dave Jones:** And better yet, those end caps come off. Fantastic. I'll stick them back on. I can solder this sucker back in. Can even put some heat shrink on it. Check it out.

**Dave Jones:** Like a bought one. All right, there's only one way to find out this is any good. Let's plug it in. Uh there's no power switch on this one. There's a green LED on the back.

**Dave Jones:** There's some sort of uh reset overload. So, if it goes bang, Oop. No green light. Aw. What what what what? Now, I don't think it's actually worth pursuing that uh power supply troubleshooting any further in terms of uh you know, an effort for value uh output.

**Dave Jones:** But, um I'm curious to know if this motherboard actually works. So, I think I might just whack on an external power supply onto it. Uh we can just lift that out.

**Dave Jones:** Slide out that. Access the power. Of course, it's got uh it's it's basically a um standard-size motherboard. So, we can if the motherboard works, we might be able to transplant it into a different case.

**Dave Jones:** But, the Dell ones, if you want to get the exact Dell replacement uh power supply, it's pretty expensive, like 70, 80 bucks or something. I'm not going to spend that on uh this machine.

**Dave Jones:** But, I could either transfer the motherboard out, if it works, into another case, which I've got, which supports the uh same size motherboard, or potentially maybe um you know, hacking uh some other sort of uh slimline power supply into there.

**Dave Jones:** But, it won't like go into the nice because it's got like a nice clip railing system here that you push down on that, and it slides out, and all that sort of jazz.

**Dave Jones:** But, you know, if we can just stick it in there or something, tie it down. How are you doing? Bit of hot snot? She'll be right. So, I've got this other uh dumpster PC.

**Dave Jones:** It's a Compaq uh Presario. It's an i5 something. It's not uh very powerful at all. Um and let's power it up. Hey. CPU fans coming on. By the way, it only it it was missing the uh two pins down the bottom, down there on the uh power connector, if you can uh see that.

**Dave Jones:** But, uh no, it's it's powering up. Well, the fan's coming on. It's good sign. Power supply's not hiccuping. All right, let's give it a burl. Do I see something flicker?

**Dave Jones:** Dell. Haha, there you go. Motherboard works fine. F12. Thing that we got. We're in like Flynn. There is it Oh, we got 8 gig of RAM. No wackers. And there it is, the i7 2600 at 3.4 gig.

**Dave Jones:** Sweet as. Well, I don't really want to uh transplant the motherboard out of this into the Compaq Presario case. I really don't like that case. It's like the tower cases are damn, so over them.

**Dave Jones:** I really like these uh slimline ones here, especially if in in the lab, you know, slide them under the bench, you can put like trays and stuff, slide them under.

**Dave Jones:** Really, uh they do work quite nice. Actually, I I another look on uh eBay, and it turns out that all the uh cheap ones actually have the cable uh coming out the side here.

**Dave Jones:** They have the fan on the end, and the cable like coming out here somewhere, and it's only like a really short power supply cable. So, it's even though they advertise it as compatible with the Optiplex 990, which is what this one is, but this one needs this massive long power cable coming all the way over here, not to mention the uh the super long um extra 12-V one going over

**Dave Jones:** here as well. And um yeah, so unfortunately, this one seems to be a fair bit rarer and more expensive. Aha! I remembered I might actually have an old Dell down in the bunker, so I took a trip down, dug through the dumpster PC archives.

**Dave Jones:** Sure enough, um we've got this um Dell Studio, I don't know, something or other. Whatever it is, anyway, it's an Intel Core 2 Duo. Fantastic, it's an E uh 7400.

**Dave Jones:** So, you know, not exactly great, but check out inside, that looks very similar power supply. Not identical, it's the cable's not quite as long. Here, it just goes down into there, but maybe that will reach and that'll fit.

**Dave Jones:** We can botch it in. Hmm, let's give it a go. Studio Slim 540S for those playing along at home. Well, check it out, they're near identical. The only major difference is the one that uh came out actually um has the cable coming out the bottom here.

**Dave Jones:** And there we go, there it is again, the D250 something or other, and this is the one we got inside the old uh slim one. And well, it's even got the like the correct indents.

**Dave Jones:** It should just uh clip in. Beauty. Let's give it a go. Ha! It clips in. It's not as solid as the other one, but put the screws in the back, she'll be right, no worries.

**Dave Jones:** Um that won't be able to snake right around there like it did last time, but no wackers. I can take that over the top there. She'll be right, no worries whatsoever.

**Dave Jones:** Ah, it's a Bobby dazzler. Look at that, and power cable reaches. That is a winner winner chicken dinner. Ha, even the three screw holes line up. Sometimes you'll win.

**Dave Jones:** Beautiful. All right, here she goes. Yeah, come on. Beautiful. There you go. We have a working Core i7 2600 machine in a nice Optiplex 990 uh case. Of course, I'm going to have to get a GT 1030 uh graphics card for it, one of those slim uh low profile things, but that and this fan is pretty silent on that uh power supply and that as well, so

**Dave Jones:** that's fantastic. By the way, I'm not sure if I ever updated you on uh this uh previous one that I found in the dumpster. It's a Core i7 3770S.

**Dave Jones:** It's actually I believe it's the most powerful one I've ever uh found in the dumpster. Slightly better than the i5 I'm currently running as my uh lab PC. I think it's a pass mark of like 8800 or 9000 or or something like that.

**Dave Jones:** There we go for those playing along at home. Um and it works a treat. Um it had like a fan issues, but I reset the BIOS and did uh all sorts of stuff, and it is a very very nice machine.

**Dave Jones:** And it's um and the fans go like they a bit noisy when they start up uh for 10 seconds, but then they uh shut down. Damn things near silent.

**Dave Jones:** A 3770S. So, I now have three working dumpster slimline machines. One and i5, which I'm using as a lab PC, and all of them are like over 8,000 uh pass mark.

**Dave Jones:** And a 3770 um just unbelievable what people are throwing out. And as it so happens, it was real handy to keep that uh old Core 2 Duo Dell machine as well.

**Dave Jones:** I got the perfect power supply out of it. Unbelievable. Sometimes you just win. Like if you bought the I could sell these on eBay for I don't know, probably $250, $300 each um Australian, something like that.

**Dave Jones:** And they just toss them out. But wait, that's not all. I didn't want to do this as a separate video. It wasn't really worthy, but let check out this BenQ or BenQ uh monitor.

**Dave Jones:** It's a GL2450. It's a 24-in uh full HD monitor with all the bells and you know, one of those uh newfangled LED backlit ones. Um what a score to go along with the uh things.

**Dave Jones:** And it seems to be working just fine. I've only It looks a bit fuzzy at the moment. I'm using uh VGA output at the moment, but uh it looks to be in pretty good nick.

**Dave Jones:** It's a bit dusty, but it even comes with Uh Still got the sticker on the back. Beautiful. So there's some pretty amazing finds from the uh dumpster in recent times.

**Dave Jones:** Three working i7 machines, monitors. This is not I think I got another monitor fairly uh recently. And like some of them are crap, but occasionally you get like decent ones like a 24-in um LED backlit one like this model here.

**Dave Jones:** Unbelievable. And for those who uh always ask, yes, I do find this stuff in the dumpster. It is a corporate office complex. You have to be an owner. It serves several big corporate uh office buildings here.

**Dave Jones:** There's dozens and dozens of uh high-tech companies here and they just throw out, you know, office PCs like this are a dime a dozen to them and monitors when they upgrade and other sorts of stuff and they just toss them out.

**Dave Jones:** Usually, almost always, working in some sort of condition. So, yeah, it's fantastic. So, yes, this is not a public access dumpster. It's specifically for the use of um the companies in this corporate business park.

**Dave Jones:** And sorry if these machines are better than the one that you're using now cuz I know there's a lot of people who are absolutely amazed by this and they go, "Well, I wish I could have a 3770, you know, with an 8 or 9,000 pass mark or something like that." And yeah, sorry.

**Dave Jones:** It's just the culture we live in. They throw this stuff away. Unbelievable. Anyway, if you liked it, please give it a big thumbs up and as always discuss down below.

**Dave Jones:** Catch you next time.
