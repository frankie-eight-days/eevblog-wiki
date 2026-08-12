---
video_id: WPyEFB4cHkA
title: EEVblog 1449 - What Causes Excess Battery Drain? (BM235)
url: https://www.youtube.com/watch?v=WPyEFB4cHkA
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 31, "3": 46, "4": 59, "5": 75, "6": 87, "7": 99, "8": 111, "9": 125, "10": 143, "11": 159, "12": 172, "13": 186, "14": 201, "15": 214, "16": 231, "17": 248, "18": 263, "19": 277, "20": 287, "21": 305, "22": 321, "23": 335, "24": 352, "25": 366, "26": 380, "27": 394, "28": 407, "29": 420, "30": 431, "31": 443, "32": 457, "33": 471, "34": 483, "35": 498, "36": 511, "37": 525, "38": 539, "39": 551, "40": 565, "41": 578, "42": 594, "43": 606, "44": 621, "45": 641, "46": 654, "47": 667, "48": 682, "49": 704, "50": 721, "51": 738, "52": 751, "53": 767, "54": 783, "55": 795, "56": 808, "57": 825, "58": 841, "59": 854, "60": 868, "61": 881, "62": 896, "63": 911, "64": 923, "65": 939, "66": 954, "67": 970, "68": 987, "69": 999, "70": 1015, "71": 1029, "72": 1043, "73": 1056, "74": 1069, "75": 1081, "76": 1091, "77": 1103, "78": 1116, "79": 1128, "80": 1141, "81": 1156, "82": 1171, "83": 1185}
---

**Dave Jones:** Hi, I got an email from a BM235 customer who's had it for quite a few years, but it um started to give a problem where even if it was switched off like this, it would drain the batteries. And he

**Dave Jones:** linked me to an EV blogger forum thread from 2018 where another customer had exactly the same issue. Now, I don't ever recall seeing that thread cuz there's like over 800 posts a day on the EV blog forum. There's a lot.

**Dave Jones:** And I didn't reply to it, so I'm not sure if they contacted me direct or or what. Anyway, this is the first time I've heard about battery drain when it's off like this. Of course, it's got power saving mode after, you know, X amount of

**Dave Jones:** minutes if you leave it on and you do nothing with it, it'll auto switch off auto power off function. And then of course, the microprocessor in it will take some residual power and it's waiting for a button to, you know, wake up and stuff like

**Dave Jones:** that. But in the off position, of course, it should have physically disconnected the switch, but I don't have a schematic for this cuz Brymen refused to release schematics even to trusted dealers like myself. So, yeah, all secret squirrel and everything. So,

**Dave Jones:** let's open this up and have a look inside cuz I don't remember the architecture of the switch and the battery and any other devices in there that may actually cause a drain. So, yeah, there must be something else in

**Dave Jones:** there like a protection device before the switch or something else before the switch that is chewing some residual power. So, let's crack it open. All right, so first of all, let's actually measure the residual current of this in

**Dave Jones:** the off position. We can do that with the BM786 here cuz it's got 10 nano amps resolution here. We don't have to go getting like the micro current or something like that to get anything lower because like a really low power

**Dave Jones:** device will take in the order of like micro amps like a standby thing like a really ultra low power device. Ultra low power micro might operate at like hundreds of nanoamps or something like that. If you get down into like the 10

**Dave Jones:** nanoamp region, then you're like really ultra ultra ultra ultra low power. So, and have a squeeze. Let's up. Get it the right way around. And there we go. There we go. I saw something down in the least significant digit there, but I didn't

**Dave Jones:** see any jump up there. So, obviously there's no capacitance on the input that's like charging up or anything. So, yeah, there's just absolutely nothing there. And if you're wondering about the operational current in voltage mode, there you go. 200 milliamps. And I won't

**Dave Jones:** bother getting the standby consumption. This thing I have to wait till it turns off and then you can't break the thing. You've got to have it permanently wired in. And in any case, the report is that it does it in the off position. So,

**Dave Jones:** let's crack it up. So, my first and best guess to the customer was that, oh, maybe there's like a reverse bias diode protection in there. So, to basically short out the batteries or actually you know, limit them to 0.6 volts if you

**Dave Jones:** actually put the batteries in backwards. And if you've got a diode that does that, then of course diodes will have leakage. And if it's using like a 1N4001, something like that, absolute classic for that application, then they're not low

**Dave Jones:** leakage of course. So, you know, they might take microamps, but they certainly shouldn't take you know, you to drain these batteries within weeks that he's talking about or something. Then you're going to need like in the order of like

**Dave Jones:** you know, hundreds of microamps or milliamps. So, here we go inside and we've got spring contacts here for the batteries and they contact these two points down here. Bingo. I think right off the bat, as I suspected, between

**Dave Jones:** those two contacts, bingo, a power diode that's likely like a 1N 4001 or something like that. And there you go, I was right on the money. It's a 1N 4007. The 4007 is the highest voltage part in that range. The reason they're not using

**Dave Jones:** a 4001 is cuz they probably use it for protection somewhere else. And they're yeah, just reusing that bomb part. From a bill of materials point of view, it doesn't you know make sense to have, you know, high voltage parts somewhere else

**Dave Jones:** and then the 4001 lower voltage one across the battery. You just They're so cheap and yeah, you wouldn't bother having a different bill of materials item just to put across the battery. Of course, the battery only needs low

**Dave Jones:** voltage. So the 4001 would work a treat. But anyway, now I had to go through a couple of dozen data sheets because Murphy says it wouldn't be the first one I opened before I could find one with a

**Dave Jones:** reverse characteristic uh graph like this that actually has the reverse current in microamps versus the voltage the reverse voltage on here. And yeah, I found this one. This is a Fairchild jobby. This is for the through hole part, but it should be identical

**Dave Jones:** for the surface mount variety anyway. And they'll slightly vary between manufacturers, but basically all 1N 4001 4007s pretty much equivalent. So if you don't have one of these graphs, then the only thing you've got to go by is basically

**Dave Jones:** the spec table, which is going to give you the worst case reverse current at the maximum rated voltage. And of course, we're not operating at the maximum rated voltage and or the maximum rated temperature as well. You can see they've got three

**Dave Jones:** different characteristic curves at different temperatures. We're at ambient temperature here. And we're only operating this thing at basically 3 volts here cuz we've got two AA batteries, 3 volts tops. So, this is 10 V and we're already down at 20 nA.

**Dave Jones:** Look, it it just drops off a cliff here. Like, it's it's 10 nA down here at 5 V, you know, roughly. Less than that. This is why we weren't able to measure anything on our BM786. Now, of course, this doesn't mean that

**Dave Jones:** this isn't the culprit. You could very well have a, you know, a faulty diode in there that has excess leakage. So, if you've got this sort of problem, it can be in any multimeter. This is a very common any product, actually, that has

**Dave Jones:** batteries. You might typically have a like a reverse bias diode like this. If you can afford the luxury of the voltage drop, then you put the diode in series with the batteries, but then you get your 0.6-V drop. And on

**Dave Jones:** a 3-V battery, that's pretty crippling. So, you have your reverse bias diodes. There's other ways to protect, but anyway, this is a cheap and simple. And yeah, it could certainly have come a gut to that part. So, if you have see this sort of thing

**Dave Jones:** in a product, excess power consumption, I would potentially look at that. And as I said, like, you should be able to measure that with an ordinary multimeter. You shouldn't need a microcurrent or any other fancy 6 and 1/2-digit meter or something like that

**Dave Jones:** to try and measure the low current. If it's like in the order of microamps, you don't have to worry about it. If you got significant battery drain, it's going to be in the order of like, you know, hundreds of microamps kind of thing or

**Dave Jones:** more. Now, of course, the other thing you might want to look at is any potential contamination around here. You might have you know, have moisture on the board. You might have You might have spilled something some liquid in through the

**Dave Jones:** battery compartment or something like that. So, I'd give it a big good clean with some isopropyl alcohol. And then, you know, just give it a good dry out and see if that makes a difference. But yeah, I don't have the This is not the

**Dave Jones:** customer's unit, so I don't know. Now, that diode might not be the only thing that's in parallel with the battery. So, let's have a close look at the PCB here, shall we? I've got my original teardown photos, which are included in the

**Dave Jones:** manual. I claim it to the be the only multimeter in manual in the world with photos of the PCB in it. So, what I've got is the top and bottom of the PCB here. And as you've seen in previous uh

**Dave Jones:** reverse engineering videos, I've actually uh taken these photos and I've skew corrected them and I've rotated them. So, they're roughly the same. They're not absolutely perfect, but if you focus on say the center of this pin uh down here, if you can see my uh

**Dave Jones:** cursor, then, you know, it does a reasonably good job of aligning these up. So, I've rotated them, flipped them, and cropped them. So, they're pretty much uh lined up good enough so that we can actually flip from top side to

**Dave Jones:** bottom side of the board and trace uh things like this. Now, unfortunately, I just realized um that these photos these would have come from my when I first um got this uh meter. So, I don't know what the revision is. I think it might Is it

**Dave Jones:** chopped off? I don't know. Anyway, this would have been one of the original units. And you'll notice up here, where's the diode? Where's Wally? Um it's not there. Where it you saw it. It was actually wedged it it was actually

**Dave Jones:** put well, my um yeah, Earth and View skills aren't that good. But yeah, they've actually squeezed this on um in future models. I don't know how many years this I can't remember. Um they might have mentioned this change way,

**Dave Jones:** way back. I've been selling this meter for like 6 plus years at least, I think, something like that. So, yeah, anyway, the new meters um in quote marks have the diode in there. But apart from that, I can't really see any other

**Dave Jones:** differences. I'm, you know, uh using the Mark 1 eyeball at the moment. I'll have to get like some new uh photos of this and uh put them up there on my EEVblog Flickr account, which is where I put all my high-res uh photos for stuff.

**Dave Jones:** But yeah, it looks identical apart from adding the diode. Everything up there else looks the same. So, yeah, she'll be right. So yeah, just imagine there's a diode in there, okay? So, this here is our positive terminal. Where else does

**Dave Jones:** it go? Well, there's this giant uh via here, like a test hole, but it's you know, it's actually connected, so it goes down as well. And there's two little uh piddly vias there, and they go down to the bottom side. And you can see

**Dave Jones:** there they are, okay? So, a trace buggers off this way like this, goes up here, we'll follow the money there, and these come down, and this goes across here. Please forgive my crude mouse skills, and this goes off

**Dave Jones:** here. Let's just trace this one here first, okay? So, if we flip to the bottom layer, there it is. Follow the money. Just follow the money. And we're following, following following there, and boom, there it is. That's what I expected. It went through to the

**Dave Jones:** switch contact in there like that. So, the battery is like switched. So, at the moment, the diode is still the only thing that's directly connected across the battery. But aha, what about this one up here, you're saying? Well, let's

**Dave Jones:** follow the money there. Trust in Deep Throat, follow the money. He knows what he's talking about. Anyway, that goes under there. I'm pretty sure there's nothing else under there. That goes along here, and boom, goes to these two

**Dave Jones:** vias down here. Let's switch, there they are there, and this goes around here. Interestingly, they do have the solder mask removed from that. Not entirely sure why. Anyway, it goes to a big hole over here, and that pops up on this

**Dave Jones:** side, and we might have to actually do some zoomy zoom on that. There you go. It doesn't connect to that, but aha, bingo, goes off to actually two capacitors, C24 and C26 there. So, we've got a diode and two capacitors in

**Dave Jones:** parallel with uh the battery even though the switch is off. Uh-huh. Okay, so where do these go? Well, um this goes via an inductor here, which is basically just a short circuit, and then it goes over to uh the current shunt here, which then

**Dave Jones:** goes up to here, and that would be That's our ground. I believe that's our ground um terminal because our fuse comes in over here like this, goes through our high rupture capacity HRC fuse here, goes through the uh 10 amp

**Dave Jones:** current jack like that. So, this here would be ground, and you can tell because they're uh basically doing some star splitting off here, and then that buggers off over here. So, this is uh ground over here. Then, you've got star

**Dave Jones:** grounding as well, so that it's a common point. Mentioned star grounding technique in other uh ones, and then there's another inductor there, and then once more, got some star grounding going off here. They love their star grounding, don't they? And they're

**Dave Jones:** actually doing the same thing over here. So, why do they have um these capacitors across here like this across the battery? What's What's the point? Well, I don't actually um know. I can only presume it's for some uh you know,

**Dave Jones:** EMI compliance thing, but why would you care if it's switched off? I don't know why. I don't know. If you've got any idea, leave it in the comments down below. But, if the thing's switched off, I don't understand having the reverse

**Dave Jones:** bias diode across there. It's to protect it when you uh plug them in. But, even that you could have on the other side of the switch, really. So, yeah, I I don't know the reason why they've got those um caps in

**Dave Jones:** there. I can only presume some sort of EMI compliance thing that they had problems with. Eh. And they've got both of those capacitor there through this inductor to ground, and they've also got this capacitor through um L3 inductor to ground as

**Dave Jones:** well. So, like why they've got two of them short? This one branches off uh somewhere else, okay? They they're taking that uh reference point that ground reference point off via that there, but these inductors are these are just like little very low value like

**Dave Jones:** RFI-B kind of thing. So, you know, it might have some not only compliance issues, but they might uh be to help um RFI interference being picked up by the test leads going into the measurement circuitry and stuff like that, but still

**Dave Jones:** why you need them before the switch? That's what I'm asking. I don't understand that at all. Anyway, if any of these capacitors here develops any sort of leakage um at all, then that leakage is directly across the battery

**Dave Jones:** um from the ground, and I'm sure that this ground point is going to go back to the battery. Here's the ground point here. We'd have to actually uh follow the money all the way, and look, here's these uh star groundings again. Look at

**Dave Jones:** this. They're a real star grounding fanboy, aren't they? Just all these different paths just um sneaking off here. Absolutely incredible. They've got it up here again. Look at this. Like three different star uh ground it that that might be not be ground. It might be

**Dave Jones:** another um voltage potential, but yeah, these are just like and there's another three going off there, and there's probably like a bunch more within the meter. So, they're really um you know, star um reference point star grounding uh

**Dave Jones:** fanboys, which is great design practice um of course. So, here I was just editing in the video, and I thought that that I should measure that because it's not going to be connected. Um yes, the actual uh battery ground here is in a

**Dave Jones:** lot of multimeter designs, most um, yeah, it won't be connected to the actual uh, ground physical ground input here. It's not uh, floating though. I actually measured it uh, with the meter and it's 3K ohms in one direction and

**Dave Jones:** 33K in the other. So, like there's active, you know, stuff in there. But, yeah, basically um, if these caps, but once again, if these caps were actually uh, leaking then they yes, that would actually leak back to the negative

**Dave Jones:** terminal. So, all that stuff is still valid. But, yeah, anyway, we've got a diode and two capacitors across there like that. I can't see anything else that is across the battery. So, to the customer who's got a couple of year old

**Dave Jones:** faulty BM 235, yeah, I'd be looking at those three components. In fact, you could remove them and the meter would still work, um, function and meet spec and everything else. It just won't be um, as maybe RFI protected um, and also uh,

**Dave Jones:** reverse battery uh, protection. You're essentially removing that. I don't know what happened if you were putting the batteries back to front. Just don't do that. But, anyway, you can put new ones in there. So, I would say it's most

**Dave Jones:** likely, come on, your money has to be on these MLCC multi-layer ceramic uh, capacitors. They're, you know, not the greatest things at the best of time and maybe, you know, get some board flex in here. In fact, the meter actually did

**Dave Jones:** have um, video a long time ago. I have to link it in. Actually, in this area, there were actually um, board flex issues and we were getting what breaking in the inductors, weren't we? Or something, the board was flex I can't remember the

**Dave Jones:** exact thing. I'll link in the video. But, yeah, that was happening around there. That's not related to this battery um, issue because even if if these inductors uh break, of course, then well, your grounding's completely ruined or your measurements will be

**Dave Jones:** completely um off. That's got nothing to do with the battery consumption. So, as I said, if you've got any clue why they uh would put capacitors on the on the like the battery side instead of like after the switch, I like cuz it's not

**Dave Jones:** like it's got to uh perform or meet any EMI requirements when it's off. So, I like yeah, why wouldn't you have those after the switch? Maybe it was just like a convenient routing, something like that. And uh maybe uh you know, this is

**Dave Jones:** not uncommon, by the way. The uh PCB layout uh ask me how I know. Circuit designer designed the meter, and then they threw it over, you know, they threw it over the cubicle wall to the PCB layout design engineer, and they went,

**Dave Jones:** "Oh, look, I can't just like it's on the other side of the board. I can't put these things here and get it back here and like all that um sort of jazz." Like, "Really? You want me to Can't I

**Dave Jones:** just put it before the switch?" And they asked the designer, the designer goes, "Yeah, whatever. It'll still do the same thing, you know, if that helps in your layout or something like that." Um uh which you might have to do often in

**Dave Jones:** actual design. You might have to actually compromise um your PCB layout. Uh pin swap pin swapping is another uh thing, right? If you've got your microcontroller pins, your FPGA pins, or something like that, and your routing's not you know, it it it just can't it

**Dave Jones:** last trace it can't go in there. Well, you might swap some of your microcontroller or FPGA uh pins or something like that um just to ease your uh routing, you know. Basically, it's it's got to come back to here. So, you

**Dave Jones:** know, it's it's not a stretch to kind of get it back to there, but then you'd have to come in through the switch and stuff like that. So, yeah, I yeah. Nah, I don't know. So, there you go. I hope you liked that video and

**Dave Jones:** found it useful. If you did, give it a big a thumbs up. And if you've um seen other multimeters that have stuff on the like battery side of the um power switch, then please leave it in the comments down below. I know everyone in

**Dave Jones:** the EV log test equipment forum, largest test equipment forum on the interwebs by the way, yeah they'll know. So they always know. But yeah, that's interesting. I thought it would have been only a reverse bias diode in there. That was my guess,

**Dave Jones:** but no I I reckon there's good money on those as well. I think they're much more likely than the poor old diode up here cuz these you know these one in 4007s usually pretty grunty. So anyway, there you go.

**Dave Jones:** Catch you next time.
