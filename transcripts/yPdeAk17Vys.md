---
video_id: yPdeAk17Vys
title: EEVblog #134 - The Maxim Manipulation
url: https://www.youtube.com/watch?v=yPdeAk17Vys
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 32, "3": 51, "4": 65, "5": 79, "6": 94, "7": 108, "8": 120, "9": 133, "10": 149, "11": 162, "12": 175, "13": 188, "14": 204, "15": 217, "16": 231, "17": 245, "18": 257, "19": 272, "20": 284, "21": 298, "22": 312, "23": 324, "24": 337, "25": 355, "26": 370, "27": 382, "28": 394, "29": 409, "30": 424, "31": 436, "32": 450, "33": 466, "34": 483, "35": 499, "36": 510, "37": 523, "38": 533, "39": 545, "40": 558, "41": 576, "42": 595, "43": 612, "44": 626, "45": 639, "46": 653, "47": 667, "48": 679, "49": 692, "50": 709, "51": 723, "52": 733, "53": 746, "54": 760, "55": 774, "56": 787, "57": 802, "58": 814, "59": 826, "60": 840, "61": 854, "62": 868, "63": 881, "64": 895, "65": 907}
---

**Dave Jones:** Hi, welcome to the EEV blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host Dave Jones. Hi, it's industry story time. Now, let me set the scene for you. Okay, we've got a couple of thousand boards going

**Dave Jones:** into production. They've been produced for, you know, quite a long time now. And this is just yet another batch of boards going through. And it's overseas. It's in China. and we get the call back saying, "Hey, there's, you know,

**Dave Jones:** something wrong. These boards don't program properly. What's going on? Can you investigate?" Okay, let's check it out. This is what happened. Okay, basically, it's got a um each board, okay, we've got has what has one of these uh Dallas one wire uh programmable

**Dave Jones:** devices on it. It's a DS uh 252. We'll take a look at the data sheet in a sec, but it's basically a 1 kilobyte uh E squared PROM identification chip. And we put this little chip on pretty much

**Dave Jones:** every board that we manufacture as an ID chip because out of the factory, these are really cool. Out of the factory, it comes with a uh a laser um etched ID in it, which is unique. No two chips have

**Dave Jones:** the same ID. So they're great for individually identifying uh boards, you know, when they were manufactured and uh etc., etc. And um also you can store up to 1 kilobyte um of information in there as well, which is handy for like a

**Dave Jones:** product ID. So we'll have our little product ID tag in there. You know, it'll have the product number and it might have some other info as well. And that's written in at the time of manufacture. and we getting the report back that well

**Dave Jones:** this information wasn't being written properly. It' just be it' write something but then it would read back just all garbage. Can we take a look at it? Okay, let's see what happened. Now, because this was in China and we didn't

**Dave Jones:** have anyone on the ground over there to investigate directly, you start with the usual things. Oh, you know, tell us what part um you've loaded on there. Give us show us a photo. Is it mounted properly? That's what you might think. Okay,

**Dave Jones:** they've, you know, they've programmed the machine properly, they've put it in backwards or something dumb like that or they've accidentally used another part. It happens something like that. But because we knew that the um uh from information that we got that the uh ID

**Dave Jones:** was being read out of the chip correctly by our processor, then we knew, okay, at least there's communication going on there and there's something wrong with the programming process. The info that we program into this chip was just it

**Dave Jones:** was just readback as garbage. It was incorrect. So, we got a photo of the part. It's got DS2502 on it. No problems at all. It's mounted the right way. Everything looks good. No problem at all. And because we could

**Dave Jones:** read the chip device ID, we knew that it was communicating with our processor. Not a problem. It was just reading out garbage. And that was a problem. So, we thought, ahuh, must be something wrong with the programming. Now, this uh

**Dave Jones:** Dallas Semiconductor/Maxim, I still like to call them Dallas Semiconductor cuz I like Dallas parts. I don't like Maxim parts, but the same company, eh, whatever. Anyway, the Dallas DS2502, this is actually a 12vt programmable device. So, normally it operates at 3.3

**Dave Jones:** or 5 volts. But to program the information in there, to write the information in once, you got to provide a 12vt programming pulse. you know, bang for a couple of micros secondsonds before you write each uh data bit. And

**Dave Jones:** we thought, okay, there's some 12vt circuitry on there. Is that the problem? Ah, so you check out all these things and no, you get down to the point where you start ruling out these little uh problems happening everywhere and it

**Dave Jones:** looks like, well, there's something wrong with the chip. What's going on? So, when you start eliminating some of the real basic dumb stuff, you start to get down to the circuitry involved. And this is what basically what we had uh

**Dave Jones:** here because we thought, okay, there's something weird going on here. And we've seen issues before, similar sorts of uh problems and stuff like that. So, we thought there might be something going on here. Now, basically, this is our

**Dave Jones:** DS2502 ID uh chip that we're talking about. It's got a series protection resistor in here. It's got a pull-up resistor to VCC, which it needs cuz it's a one wire uh bus. So, one wire needs a pullup because this all this chip can do is

**Dave Jones:** pull down and it can be parasitic powered. And we'll look at that later. And then it's got a zeno diode for protection because um well, and we've got it going off to an external programming um programming uh header on

**Dave Jones:** the board that you can program the device through. And also there's a 12vt generator as well but I won't draw that on here because we've already checked that and it does generate um its 12vt programming pulse. Now the reason this

**Dave Jones:** uh circuitry here is because it goes off to an ARM processor over here or an FPGA depends what the product is. It goes off to it and um it's got to talk to the device as well as uh being

**Dave Jones:** able to externally program it. Now when you program this thing, you put your board in your test jig or you use some other circuitry to program it, some onboard circuitry in this case, then um it generates a 12vt programming pulse.

**Dave Jones:** So normally it talks 0 to 3.3 volt digital down here and then you'll get a big 12vt programming pulse and if you don't have any protection circuitry that can blow up your processor or your FPGA or your other device which is trying to

**Dave Jones:** talk to it. Now um uh these values actually here can actually load down the line from the uh external programming circuitry. So we thought okay maybe they've loaded a wrong part on here. But we checked all that and it wasn't there was nothing

**Dave Jones:** wrong with it. It all looked quite good. No problems at all. So we had to investigate further. Now, further testing had to wait until we got uh the assembler to send back a sample from the reel cuz they had some leftover parts.

**Dave Jones:** It was meant on one of these reels. And here's the It's on like tape like this. If you can see that the uh there it is there. The uh chips are actually uh embedded in the little tape on the reels

**Dave Jones:** like that. So, they come straight from the manufacturer uh on a reel. So, we had to wait until we got some samples back. And then uh what I did is I actually uh mounted one cuz I didn't want to mount it on the

**Dave Jones:** board under question. I just wanted to directly talk to it with the original uh Maxim um USB programmer, the one wire programmer device that we've got. So soldered it onto a blank board like that with no circuitry whatsoever. It was

**Dave Jones:** just the chip itself. So there could be absolutely no question that any other circuitry on the board was interfering with it. So, I sold it on the board, used the programmer, and here's what I've got. Check it out. I actually

**Dave Jones:** loaded up, right, a good chip first to get a reference. And this is what a good chip looks like on the reel from the factory. It's supposed to be blank. It's supposed to have FFF in all the data

**Dave Jones:** areas. And as you can see, there's a device um ID up there in the uh top leftand corner. It tells you it's a DS25i2. It identifies the chip. No problems at all. So, our system's working. We've got a good bench line to

**Dave Jones:** work with. Now, here is the uh here is one of the chips that they sent back. Brand new chip from the reel. Hadn't been soldered on the board yet. And check out the data dump. Look at it. It's not blank at all. It's got data in

**Dave Jones:** there. It looks like it's corrupted. Bingo. We've found our culprit. Okay. This chip was supposed to be completely blank from the factory. Unless you specifically ask for the manufacturer to actually uh program it for you. That's a service that a lot of manufacturers will

**Dave Jones:** do. You can actually have it programmed that comes on your reel already programmed with the information that you need for your particular product. So bingo, we found our culprit. The chips weren't blank for some unknown reason. Were they just corrupted with ram random

**Dave Jones:** data? Well, we didn't know yet, but we knew that they were supposed to be blank. Now, the problem with these devices is that they're what's called a write once uh E squared PROM memory. So, you're only supposed to write to them

**Dave Jones:** once. That's why they're all come programmed with all FFF. And once you write a bit of data to a zero, an individual bit to a zero, you can't change it back to a one again. So, they're effectively a write once E squ.

**Dave Jones:** You only get one shot at it. If you accidentally write the wrong data on there, you've got to suck the chip off and put a new one on. So, those chips were absolutely useless to them. It's not useless to us. It's not like we

**Dave Jones:** could erase them and then reprogram and that would have solved all their problems. Now, of course, when you look at this data, just the hex dump like that. It looks like it's just well random data, right? Something's gone

**Dave Jones:** wrong with the programming process. Uh you don't know. Um, so I thought rather than delve into the software and trying to debug it and it's in a different country and ah it's all too hard, I thought I'd just translate the uh the

**Dave Jones:** hex data dump into ASI just to see what was going on. So here it is. Take a look. Bingo. It is not random data. There it is in plain ASI uh copyright 1995 Motorola Corp. You got to be

**Dave Jones:** kidding me. Where did this come from? So, bingo, there you have it. We found the culprit. This isn't just random data rand, you know, produced some fault in our programming system. No, these chips came pre-programmed on the damn reel. Okay. With some sort of

**Dave Jones:** Motorola firmware. I've got no idea what Motorola product it's for or, you know, where it came from or how. We still need to do further investigation on that. But clearly we've been given dodgy chips. So how did it happen? Well, as I said,

**Dave Jones:** I've got no idea. We have to do further investigation. So I'm not going to blame Maxim just yet. But I've talked to the purchasing guys. He purchased uh these things directly on the reels. and they're saying that they always buy from

**Dave Jones:** either directly from Maxim or from uh a an authorized component distributor like Digi Key Mouser or somebody like that because we're very careful about this. We've been, you know, bitten by this before in the past. You buy parts from

**Dave Jones:** the gray market and they're fake or something like that. So, there's only a couple of things that this can be. One is that uh they're actually fake gray market chips and they've been uh they've already been pre-programmed for some

**Dave Jones:** other customer or they ripped them off boards and then they've reeled them because it's not like these things they just shove them back in tubes or something like that. You've got to actually reel them um onto original things, put the uh put the tape on them

**Dave Jones:** and all sorts of stuff. And well, you know, it's not hard to do that, but you've got to have the equipment to actually do it. And a lot of the gray market companies, they specialize in doing that. They rebrand the chips and

**Dave Jones:** they actually um and they repackage them and make them look like brand new and you get sucked in. They either don't work at all or they're close or they're pre-programmed with someone else's firmware. So, that's a possibility. Or

**Dave Jones:** the more likely scenario, because we bought them from authorized sources, I don't reckon that they're gray market uh chips. I reckon they've been supplied, here's my guess, from Maxim themselves, directly from the Maximum Maxim inventory, pre-programmed with somebody

**Dave Jones:** else's firmware. I reckon they've programmed them, screwed it up, put them back on the shelf, and sold them to uh to us in this case. So, I reckon that's the much more likely scenario than getting uh gray market chips because

**Dave Jones:** we're very careful where we buy them from. So, we still have we haven't talked to Maxim about it yet. So, you know, it's it's all still out there. We haven't thoroughly investigated. We haven't even got the original reel back

**Dave Jones:** yet, but I just thought I'd share this with you as an experience of it's not I'm not going to say it's common, but it has happened before. I've had issues like this before. So, it's definitely it definitely happens out there and it's

**Dave Jones:** something you got to consider. Now, one of the uh things that you also do is take a look at the chip itself to actually um see. Now, I've got my uh trusty little Xtech MC 108 um portable microscope here. I don't reckon it's

**Dave Jones:** that great for uh soldering to a soldering inspection, but it's brilliant for looking at uh the numbers on top of chips. So, let's take a look at it. Now, let's actually take a look at a good chip. Here is a good chip. And as you

**Dave Jones:** can see, DS2502, and it looks like it's been laser marked, I'd say. You can tell by the really sharp um edges on there. there. And if you actually look at angles under certain lights, you can you can tell

**Dave Jones:** it's laser etched as opposed to some sort of silk screen uh process. Now, the uh plus markup there indicates that it's ROS compliant RO HS. And um now the numbers down the bottom I couldn't find anything on the data sheet uh to

**Dave Jones:** indicate what those numbers are but my guess is that 9 is the year 0927 is the week of manufacturer and D3 I don't know it might be some sort of batch number or um some silicon revision or something

**Dave Jones:** like that. So we we'd have to ask Maxim Direct to actually do that. Now let's let's turn it up a bit. And as you can see the uh the figures are nice and sharp. No problems at all. And here you

**Dave Jones:** go. Here is the faulty chip. Now, as you can see, the um the silk screen isn't nearly as big or the identifying marks aren't nearly as big as they were on the other device. And I think they're still

**Dave Jones:** laser uh etched, I think, but they look substantially different. Um now, as you can see, it's um 08 as well. So, considering these are supposed to be fairly new parts, if that is the year code down here, then we've certainly got

**Dave Jones:** old chips. if it is 26 week um 08 and B2 is different to the other device. Now, you know, that's not telling evidence that it's a fake chip. And I'm not going to claim that it is fake, but um I

**Dave Jones:** guess, you know, only Maxim could tell us uh something, you know, if there's actually an issue there and if the chips are real, but they certainly have been pre-programmed with someone else's firmware. So, there you have it. There's the

**Dave Jones:** problem with the Maxim chip that really it came down to the last possible thing I thought it would have been which was a pre-programmed chip because you just assume that the chips you're going to get from the manufacturer are good and

**Dave Jones:** that happens you know all the time. You basically got to rely on that and there's all sorts of other things that would cross your mind as being um the failure mechanism for something like this before a pre-programmed chip. I

**Dave Jones:** couldn't believe it when I finally saw that copyright Motorola in there. Unbelievable. But hey, that's a real story. There you go. Watch out next time. [Music]
