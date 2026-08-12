---
video_id: E1IqcGcZKHE
title: RPi CM4 Compute Module FAILURE Part 2: Thermal Boogaloo
url: https://www.youtube.com/watch?v=E1IqcGcZKHE
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 30, "3": 41, "4": 59, "5": 76, "6": 88, "7": 103, "8": 119, "9": 133, "10": 148, "11": 161, "12": 174, "13": 184, "14": 198, "15": 209, "16": 222, "17": 234, "18": 246, "19": 257, "20": 276, "21": 295, "22": 312, "23": 325, "24": 336, "25": 348, "26": 366, "27": 378, "28": 390, "29": 401, "30": 414, "31": 428, "32": 444, "33": 457, "34": 475, "35": 497, "36": 514, "37": 527, "38": 538, "39": 554, "40": 579, "41": 597, "42": 612, "43": 625, "44": 649, "45": 665, "46": 680, "47": 695, "48": 710, "49": 726, "50": 741, "51": 755, "52": 780, "53": 795, "54": 818, "55": 846, "56": 860, "57": 873, "58": 887, "59": 900, "60": 913, "61": 929, "62": 943, "63": 954}
---

**Dave Jones:** Hi, just another follow-up video on this uh failed Raspberry Pi compute module 4 here and how the Ethernet chippy, this broadcom jobby down here looks like it's failed and it's getting redot. Ernie Bernie. Um now a few people asked uh

**Dave Jones:** does it actually do the same thing outside of the carrier board which I had it on this little carrier board here and the answer is yes at it does and I can show you that right here. So, I've got

**Dave Jones:** it on the um this is the AERL gateway that it came out of uh that it failed. This is for my solar battery if you haven't seen it. So, let's actually plug this sucker in. And you can see it's Oh,

**Dave Jones:** hello. There you go. It's drawing eight and a half watts. And my fingers on the Ethernet chip. Yep. Yep. Yep. Yep. Yep. Yep. Ernie Ernie Bernie. Ernie Bernie. Um, yeah, that Ethernet chip is just mega hot. And the

**Dave Jones:** processor, I can leave my finger on the processor and it's okay. So, yes, hot hot. So, let me disconnect that. Okay, so the answer is yes, it does get hot. There's no way. Um, if you look at the spec sheet for this thing, they

**Dave Jones:** actually boast this is low power. It's uh like a one watt maximum for one port, and this is a one port chip, I think. Um, so yeah, at at most full speed going like the clappers, it should be uh

**Dave Jones:** drawing less than a watt or a watt maximum. So, um, yeah, there's something wrong. And I've got another gateway uh identical to this and it draws 2 and a half watts. Um, so yeah, 8 watts is definitely wrong. Okay, so uh yes, that

**Dave Jones:** is a problem. So, what I thought I'd do is let's get this thing out. God, I hate these. They're really I you always think you're going to damage the damn things um with these little delicate delicate connectors on them. So anyway, uh there

**Dave Jones:** we have it. There is our compute module and that that's the bottom of it. Nothing doing there. And on the top side, oh it's upside down. All the electrons are going to fall out. Uh there is our Broadcom chipset. for those

**Dave Jones:** playing along at home who haven't seen the first one. It is a Broadcom BCM 5421 there. So, there we go. Um, so what I thought I'd do, uh, a couple of people suggested this and I thought I'd probably do it last time and I thought,

**Dave Jones:** yeah, it's, um, just for shits and giggles, um, I'm going to desolder that thing and, um, see if the power drawer goes back to normal and then see if we actually get a see if this thing still boots and we get a HDMI output cuz like

**Dave Jones:** who like I I have actually tried it like like I have actually connected a HDMI onto here when it's drawn the seven watts and five watts, six watts or whatever it was doing before and I get no HDMI. MI output from it. Um, and that

**Dave Jones:** was the problem. So, let's see if we can get some hot air on that desolder. I mean, the board's gone. I mean, it's it's obviously failed. There's obviously faulty. There's something wrong with the silicon in there. Like, it's it's not a

**Dave Jones:** bypass cap around. Is that a little bypass cap there, right? It's it's not that um something. There's the crystal for it on the bottom. 25 megahertz there. Right. It it is not these caps that are getting hot. In fact, I can Oh,

**Dave Jones:** no. I can't power it up because to power it up, you got to power it up through these bottom connectors and then all of these components are gone. Like you can't access them anymore. Um, yeah. No, it's it's not that the chip is getting

**Dave Jones:** directly hot. So, it should not do that. So, it has failed. So, this compute module is dead ski, but I don't know. There's a small chance that, you know, this could be loading down the DC power supply over here, which is trying it. I

**Dave Jones:** don't know, which gets red hot as well. it actually gets hotter than this because it wasn't designed to draw like you know the 5 watts or whatever into that poor little um Ethernet chip. So that could be dragging that down which

**Dave Jones:** could be stopping the processor from booting. So it's quite possible that if we remove that we'll get no Ethernet functionality but we might actually uh restore this um to being used. I mean it it does actually have the Wi-Fi module

**Dave Jones:** but this unit doesn't have the uh doesn't use the Wi-Fi. It actually uses the Ethernet connection. So, I don't think that's going to um solve my problem with the uh uh gateway here, but anyway. Okay. So, let's see if we can

**Dave Jones:** desolder this. Get some flux on there. That should help out. Sorry if this is blocking the view. I tried to use my nozzle. That's not blocking anything. No, it's not liking that. Rather tough. Don't have to put a preheater on the

**Dave Jones:** bottom. Wow, that's nuts. All right, let's try a bigger tip. Bigger tip, slightly higher temperature and bigger airflow. Let's see what we get. Come on, you can do it. Wow. Going to try it on its side. Oh, there we go. Got him. That's the

**Dave Jones:** trick. Yeah, big thermal pad on the bottom of that. Yeah, there it is. That's why that that sucker took a bit of work there. And the uh the bypass caps come off. Now, it looks a bit ugly, but that's just the uh flux. Now, it

**Dave Jones:** doesn't look like Yeah, we haven't lifted any pads and we can just go around with some solder. We can just lift that up. You can see a bit of wiggle wiggle wiggle there on the trace. That's uh just some uh length matching

**Dave Jones:** with the trace next to it. That cuz that's obviously a differential pair. And there is that little pesky thermal pad on the bottom. So, it took a bit of extra work that was going right through to the ground plane in the middle.

**Dave Jones:** There's probably a whole bunch of vas on there, is there? They're all Well, no. No, just around the outside. Oh, yeah. There's probably a whole bunch in the middle there. Can you see them? Yep. Yep. A whole bunch of thermal vas. And

**Dave Jones:** uh they're going right through to the inner ground plane. Um and I assume that's electrically connected to ground. I haven't checked the data sheet. I think it's NDA actually the data sheet. Anyway, little pesky QFN package there. really with a big ther big ass thermal

**Dave Jones:** pad. Really annoying. I mean, it it does dissipate even though it's low power. It does dissipate a watt. So, you know, which is significant and they want to get rid of that. So, yeah, that was just a little bit annoying. Nothing else near

**Dave Jones:** it uh came off. No, none of those resistors, they're still in place. And that little eightpin jobby over there, it's all fine. That little SO 23 is just fine. That bypass uh No, that's No, probably not a bypass cap. There's

**Dave Jones:** probably some sort of set resistor or something like that. I don't know. Some mode select or something like that which we don't care about cuz chip's not there anymore. And all that heating. Did that take anything off the bottom? No.

**Dave Jones:** Nothing fell off the bottom. Winner winner chicken dinner. It was stopped by all that ground plane in there. And that is cleaned up a bit better. Not absolutely perfect there, but uh good enough for Australia. And you can see

**Dave Jones:** like there's no shorts on any of those pins because we care about that. We don't. Oh, what is that? What is that black thing down there? No. No, that's just some crud. More crud down here. No, nothing, burger. But, uh, that came off

**Dave Jones:** very, very nicely. Very happy with that. Put some more isopropyl on that. Give her another scrub. Not on here. Tongue at the right angle. All right. So, that's hunky dory. Let's uh let's take that out of there and

**Dave Jones:** we'll power it back up. put it back into this board so that we can get a HDMI output from it hopefully. And I do, even though I haven't tested this, I do actually have an HDMI uh connect output

**Dave Jones:** uh connected. I will have in a second connected into my Blackmagic ATM switcher. And I can pull that up on channel five here. So, got nothing at the moment, but uh let's power it up. So, that's seated in the connector properly. Let's power

**Dave Jones:** it up. See what we get. Oh, 4.6 watts. It's less. It's less. Okay. So, obviously that's not going to get hot anymore, which is um wonderful. Um yeah, the power supply is a bit Ernie Bernie. Uh let me see if

**Dave Jones:** I get anything. No, no, I'm getting nothing on the HDMI. nothing out. So, no, I think that's a uh that's a loser all round. Um you know, we we could have like damaged our power supply or something. Still delivering 5.1. I guess

**Dave Jones:** we could measure on there and measure some power rails maybe. But yeah, that's that's just too high. But you saw it before like we were getting what six or something, six and a half. And then we put on the other one seven. But let's go

**Dave Jones:** for the measurement we did in the first video. uh we were getting like six. So there was a good couple of watts going into that chip. That's why it was getting hot. That's more than it's stayed double more than double maybe

**Dave Jones:** even triple it stated um consumption. The processor is doing something. The processor is getting that's you know it's 40°. Yeah. Yeah. It's about 40. My finger starting to act as a heat sink now. Not getting anything out of that though

**Dave Jones:** unfortunately. Zippity doodah. Let's measure this power supply. I don't know the pin out of this at all, so I'm just guessing. But if you measure across the caps, you should get something. Nothing. Nothing across the cap. 2 negative.2. Could have it back to

**Dave Jones:** front. Zero. All right. No, I think the uh Yeah, the power supply is gone. Not surprising. um because the overload on the Ethernet chip uh which is a definite known fault could have caused um an issue with the DC toDC converter. So So

**Dave Jones:** that's why she's come a gutsa. Although if we're getting no voltage out of it, why uh why is our processor getting warm ski? Because that that's getting reasonably reasonably hot now. Not quite as hot as the Ethernet chip, but still

**Dave Jones:** annoyingly hot. Sorry you can't see it. I'm just using the zoomed into probe here, but we we're are getting we're getting 5 volts on those caps there. So, we're getting our 5volt input, but we're getting uh zippity doo on the output.

**Dave Jones:** What what was getting hot there? Oh. Oh, that Wi-Fi module. That Wi-Fi module [Applause] Bernie Bernie. Um what? Oh, yeah. This is one one very sick puppy. Aha. Hang on. Come on. Come back. I swear this was jumping around like a

**Dave Jones:** jack rabbit just like I tried to tell you about in the first video. Come on. Yeah. Look look look. It's jumping like it's it's shorting out the it's shorting out the thing. It's Yeah. And there's overload on my battery

**Dave Jones:** pack. Oh yeah. Yeah. N. This is one sick puppy. So, there you go. Unfortunately, um answer to that question uh by removing that Broadcom chip. No, we didn't fix it. No, this is one sick puppy. It's gone has something

**Dave Jones:** gone drastically wrong. Maybe the DC toDC converter failed cuz I I assume it's like 3 5 volts in to 3.3. Um I don't know. Haven't got a schematic for the um Do they ever release a schematic for it? Anyway, I or some people have

**Dave Jones:** reverse engineered it or something like that. I think it's supposed to be a 3.3 volt output, is it? So, now the Wi-Fi module is getting hot. Um, I think yeah, maybe it failed internally and wasn't regulating at 3.3 volts or whatever

**Dave Jones:** lower voltage it is and it and it 5 volts out on that rail and fried everything. Maybe that can be my only conclusion why seemingly everything on this board is now getting Ernie Bernie. Um, yeah. Anyway, so much for that.

**Dave Jones:** Catch you next time. Oh, update. I was uh just about to edit uh this video. I thought I was done. I read the comments from the previous one. Thank you very much, Joe 5721 or 57 something. Put up his comment. Um

**Dave Jones:** noticed in the video that there was maybe a little blowhole in the Broadcom chip and Sean like here's a photo from like screenshot from the previous video. I noticed it in a couple of seconds of the clip. Thank you very much um Joah

**Dave Jones:** for pointing this out. And sure enough, look, look at that. It looks like a little blow hole. Is that where the magic smokes escaped? Let's get some isopropyl on that. And I can give that a scrub there. It's still there. It's still there. Look

**Dave Jones:** at that. Yeah, that is a divot. I'll get my get my sharp probe here. Yeah, I I can feel this is not feeler vision, but trust me, I can feel that. I can feel that. That is a blow hole. And that was

**Dave Jones:** there before. That's not due to the desoldering. That was there before I did that. So, Whoa. Oh, whoa. Have you ever seen a chip do that? Look at that. Oh my goodness. What's going on now? You maybe is that from heating up

**Dave Jones:** during my reflow? But Oh. Oh, wow. I'm literally digging. Seriously, I'm like, what? What the heck? It feels as though I'm digging down into that chip. Whoa. Copper. We have copper. Oh, come on. Cleaned it up again. And yeah, look. Yeah, you can see down

**Dave Jones:** in there. You can see a bit of a glimmer, can't you? Yep. Yeah, I do believe that is the blow hole. That is the blow hole. How this thing um got this way, like how it actually blew, I

**Dave Jones:** don't know. Look. Oh, is that side of the chip gone away there as well? But any well yeah anyway okay it looks like we might have softened it up from the reflow maybe but uh anyway yeah it was

**Dave Jones:** definitely there before I did the reflow there was that blow that looks like a blow hole in the um chip there and yeah the magic smoke's escaped and everyone knows the magic ingredient in every component is the magic smoke. Luckily I

**Dave Jones:** make a re and they they have a refill can available for the magic smoke that you can actually put back in there. Unfortunately, that IBM Magic Smoke rare as hens teeth these days. Don't have any here in the lab. Otherwise, I'd be able

**Dave Jones:** to refill this thing and uh we'd be able to resolder it. So, yes, that has failed. And uh some people wanted to see the bottom of the ARL board as well. Um it is not that. And there you go. Pulse

**Dave Jones:** magnetics. Um looks fine. There's no issues there. Um the Ethernet cable's not outside. Somebody asked that. Um it's just in the roof going from my router in the roof over to the well, you know, like a space um to uh the garage.

**Dave Jones:** Yeah, it's nothing to do with this board. It's got the proper magnetics on there. So, no worries. So, yeah, I don't know how we got a blow hole in that chip. And the blow hole obviously like took probably took out um my yeah that

**Dave Jones:** is my theory is that yeah the excess current in here just like maybe took out the DC toDC converter and we've got all sorts of problems and then probably like 5 volts on the output and then it took

**Dave Jones:** out every it's probably taken out everything else. So yeah, that board has completely comes. Um but thank you very much Joah for uh pointing out that blow hole in the chip. Well done. My viewers spot everything.
