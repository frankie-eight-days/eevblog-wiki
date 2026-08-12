---
video_id: XRyDyOANQhc
title: Guest Video: The Defpom - Fluke Calibrator Repair
url: https://www.youtube.com/watch?v=XRyDyOANQhc
source: youtube-asr
timestamps: {"0": 12, "1": 25, "2": 36, "3": 50, "4": 65, "5": 75, "6": 90, "7": 101, "8": 112, "9": 124, "10": 135, "11": 146, "12": 160, "13": 178, "14": 194, "15": 207, "16": 222, "17": 238, "18": 254, "19": 269, "20": 285, "21": 299, "22": 313, "23": 324, "24": 334, "25": 346, "26": 364, "27": 383, "28": 402, "29": 421, "30": 438, "31": 460, "32": 477, "33": 499, "34": 519, "35": 538, "36": 556, "37": 575, "38": 605, "39": 624, "40": 648, "41": 667, "42": 686, "43": 703, "44": 716, "45": 730, "46": 745, "47": 769, "48": 786, "49": 804, "50": 822, "51": 843, "52": 859, "53": 875, "54": 893, "55": 905, "56": 923, "57": 937, "58": 949, "59": 967, "60": 982, "61": 998, "62": 1016, "63": 1031, "64": 1042, "65": 1052, "66": 1065, "67": 1077, "68": 1089, "69": 1101, "70": 1113, "71": 1126}
---

**Dave Jones:** Hello everyone. I'm the Defpom. First name Scott. Hopefully Dave chooses this video for his guest spot while he's away on holiday. And uh I thought I'd just tell you a bit bit about me and about my channel and what I

**Dave Jones:** do. Um This unit here is one of the things I'm working on currently. I do a lot of prepare videos mostly on test equipment. Um I do do some review reviews as well on new gear. I've done some reviews of

**Dave Jones:** Siglent in the past. Um you might have seen those. Um also anything else sent to me as well. I do mailbag videos, things I've purchased and and so on. I also do CB repair work and I've done a little bit

**Dave Jones:** of videos on that. Um but mostly mostly what I do these days is test equipment repairs. So if you're interested in you know seeing me fixing test equipment stuff then carry on watching and check out my channel. So this is one of a piece of gear I'm

**Dave Jones:** working on right now and I've had it in my possession for quite some time now for a few months. And it's been a bit of a pain. I think every single board in it has a fault. Every board is faulty.

**Dave Jones:** I think it's a parts unit which has been used for good parts for other ones. This is a Fluke 5200A AC voltage calibrator. Um and I'm working through the repairs on this and I'm just going to go through

**Dave Jones:** and show you a bit on troubleshooting at the moment and just doing some diagnostic work. So it's going to be a little bit technical but not overly so. I'm not a hugely technical person. I'm very much you know out there and

**Dave Jones:** unplanned videos I just sit here and just speak and go through it. I don't have a script or anything like that. So hopefully you don't mind me falling over my words a little bit, things like that. So this is what I'm working on and um

**Dave Jones:** I've been working through the cards. I've already got two cards repaired but I'm still doing some more diagnostic work. Um I've already repaired the power supply, we've repaired all that, and done some substitutions and so on. Um so I was going to show you this. If

**Dave Jones:** you want to see more about this particular repair, um I've got a series on my channel of repair so far up to date. Um and there will be more as well as I progress through it. Um but hopefully

**Dave Jones:** this is a little sample of of, you know, what you might get to see if you come to my channel and have a look and uh hopefully subscribe and so on. So hopefully Dave chooses me. Otherwise it will never see light of

**Dave Jones:** day. Okay, so to start off with, I should explain what's going on here. Now this board here is the oscillator and it isn't oscillating. All right, so what's supposed to happen is it's supposed to have a phase uh change as it goes through each

**Dave Jones:** amplifier stage on this board. It's supposed to go 380° on the first stage, 90°, and 90° again to get 360° or thereabouts, um which is then controlled electronically by the control board, oscillator control card, um which then fine-tunes that frequency, allows for

**Dave Jones:** any changes on the front panel controls, and so on. Um that's the theory, all right? But the oscillator doesn't work. So what I'm actually doing is injecting my own oscillator signal into the unit um at the input, which is then passing through

**Dave Jones:** the stages, and then I can actually test each stage that way with an artificial injection of a of a signal, um which at least proves that each stage is working. I've done this previously in the another part of video, um another section I've

**Dave Jones:** done, which showed the gain of each amplifier, which is about 40 times gain. Um so those are actually working, you know, at least I know as far as amplification goes, but not as far as phase. Um and that's where I'm thinking the

**Dave Jones:** issue is now why it's not oscillating is because if the phase is wrong, then it won't oscillate because it's out of phase with itself, and so it doesn't generate an oscillation. Um but it's quite a complicated little setup they've got going on here. Um

**Dave Jones:** It goes across two different cards, which is influenced by a third card, which is fed by my fourth card. So, it's a case of eliminating which part is causing um the problems and and trying to prove which bits work, which which which

**Dave Jones:** bits don't. Um so, it's a it's a pain. And um it's been a long process. So, hopefully this video is a little bit interesting for you. Um I doubt I'm going to actually achieve anything in this video. I'll be I don't think I'm going to fix

**Dave Jones:** anything today cuz it's it's a lot to go through. And um but hopefully you find it interesting. All right. So, I've got my uh test set up here. Now, I'm using the new SDS 1104X E scope, which I've been

**Dave Jones:** reviewing recently. And um I was playing around with it still cuz it's four channels and it's convenient. And um I've got this hooked up onto the oscillator uh control board. Well, oscillator board, sorry. And what I'm trying to measure here is

**Dave Jones:** the phase in between each oscillator stage. Um it's supposed to change phase as it goes through. Now, I'm actually having a bit of trouble measuring the first stage um between the input and the and the output of the first stage. Um

**Dave Jones:** so, I'm going to have to probably come back to that, but for now, I can move on and test the other stages and see if they look right. Okay. So, let's move the camera down. I'll show you what I've found so far.

**Dave Jones:** Okay. So, I've taped off on the inputs and stuff on this card now, so I can actually measure the phases on each stage. So, this is the input for my oscillator. This is the output of the first stage,

**Dave Jones:** output of the second stage, output of the third stage, right? So, you should be able to see the phasing from each one. Now, if I zoom in slightly, you should be able to see it a little bit better.

**Dave Jones:** Um so, you can see 1 to 2 is almost 90°. Depends on the frequency as well. So, if I actually adjust the frequency on the Fluke, um these phases will change slightly. Now, it's at say 89°. Phase between 2 and 3 should is actually

**Dave Jones:** -87. So, it's actually 270° out in theory, but actually it's almost in phase with the first one. Um 3 to 4 I sorry, 2 to 2 to 3 is those two. So, phase 3 is actually in phase with

**Dave Jones:** the first one pretty much. And phase 4 is at 19°. All right, so phase 4 is actually 270°. Now, it says -86 cuz obviously it thinks it's going around, but the issue here is that this first difference here between

**Dave Jones:** the input and the output of the first stage is supposed to be a 180° phase difference. Not 90°, according to the manual. So, that's probably why it doesn't work properly. All right. So, I've tested each stage and each stage is amplifying and doing

**Dave Jones:** things it's supposed to do, but that's why I wanted to come and check the phases because um if this isn't right, then it throws the whole thing out. So, say this first stage here is supposed to be 180°. It's supposed to

**Dave Jones:** invert the input. It's not doing that. Um so, I found that quite interesting. Um and these other two stages are supposed to be 90° out from each other. But, what I've got here is 90°. 270°. And it's like 270 again, effectively, but

**Dave Jones:** it's yeah. It's not doing what you think it should do. So, yeah, it's a bit of a pain. Um I need to investigate this first bit here cuz it's supposed to be inverting the input. That's what's supposed to happen.

**Dave Jones:** Okay, so this is the circuit diagram for the oscillator board. Now, these phases I'm looking at on the scope. Now, this is the input here, TP2. I'm measuring at TP3 for channel two, and TP5 for channel three, and TP7

**Dave Jones:** for channel four. So, this first stage here is supposed to be 180° inversion. And this stage here is supposed to be 90° inversion. This is supposed to be 90° inversion. So, well, phase diff phase change. Um and that's not what's happening. This phase

**Dave Jones:** here with this stage here is not doing 180°, it's only doing 90. Now, this has some other aspects along with it. Um there's a summing amplifier out here, which is in parallel with the device. Summing amplifier in, summing amplifier

**Dave Jones:** out, they go to the um oscillator control board. And um it gets a bit more complicated, certainly, but they actually have a capacitor across it, which is used to tune this response. Um There's also an oscillator to zero here.

**Dave Jones:** Um I've tried adjusting that, it didn't seem to change anything, but um so, let's just look at the summing amplifier out and summing amplifier in. Let's see what those do. Um those are on the control PCB, which is here.

**Dave Jones:** Now, they Um are here, so I'm going to fight in over here. And so I'm going to fight out. So, those pass through. Now, this is going through this network here. Um which goes back into here. And into here. This This box.

**Dave Jones:** All right. So, let's go back down to the next page. And this is that box. So, amplifier in is here. And so I'm going to fight out is where? It's also labeled as H. So, I should look for that, too,

**Dave Jones:** shouldn't I? Um H, there we go. There. All right. So, oscillator control in this is a level control. All right. So, um I did find some faults. I think I replaced some capacitors somewhere in this part of the circuit. Where was it?

**Dave Jones:** Over here. I think I replaced these caps here, I think it was. So, there was an issue with this particular board. This I'm suspicious of this circuit here. I think something in here isn't right. Um So, this is supposed to come

**Dave Jones:** uh out of this device here, go to the amplifier, feed through the amplifier, come back, and go across this stuff here. So, it's all amplifying DC amps and stuff here, as well. So, this is supposed to be um

**Dave Jones:** providing some amplification, and it's probably affecting the oscillator. Now, there's other stuff here that you can see there, too. Now, you got these various capacitors which are being switched in as well by these relays. These were part of the quadrature

**Dave Jones:** amplifier and the oscillator amplifier. Those seem to be working okay. Those look about right. So, I'm pretty confident these capacitors here were working okay and that all these relays here were working okay, as well. Um I've done individual testings for

**Dave Jones:** everything. Um and I've actually eliminated the phase lock circuit by not having it turned on. It disables that part of the circuitry. So, um just trying to figure out exactly which part is causing problems now, which I believe is in this amplitude

**Dave Jones:** control circuit here. Um because it doesn't seem to be doing the right thing. It's a bit of a tricky process cuz it's all one big loop and um it's it's a bit of a pain. Now, there's actually a bit in the

**Dave Jones:** in the diagnostics here somewhere. See if I can find it. Um theory of operation functional block diagram is it here somewhere? Here we go. This is it. All right, so what I was actually hoping to try today was to

**Dave Jones:** try and do a bit of a shortcut here. Now, the oscillator assembly I know does oscillate. Now, this is So, you got this shows us phase shifts of 90°, 90°, 90°, okay? So, that isn't phase shifting like it should be.

**Dave Jones:** But, that is controlled by this summing amplifier in. All right, it's from the oscillator control assembly. So, um this may or may not be working correctly. But, is that because there's no amplifier control from here? Now, I've actually measured this test point here

**Dave Jones:** at at uh connection 51, pin 51 on the card. And that's reading 0 V. So, and it's supposed to be between -15 V and 0 V. So, if it's 0 V to me says it's fully out of one range.

**Dave Jones:** So, and that's without the amplifier installed cuz that's blown. All right, so everything's blown. Reference assembly is fixed. I've already repaired this and I'm I'm 99% sure this card is is good now. Um but uh I would want to actually want to

**Dave Jones:** originally inject my own voltage here in pin 51. But I had some other complications going on um with the wire ties reference voltages together cuz it uses reference power supply which is linked to AC to DC converter through this cable here.

**Dave Jones:** Um which has a negative reference. Which then gives the correct power supply output from the main power supply cuz it checks the reference voltage first and it's all tied together that way. So, it's a bit complicated and involved.

**Dave Jones:** I might still go that route yet though. So, I actually want to inject a negative voltage here and see if it corrects the frequency here. Um it probably won't. It's supposed to be for amplitude control. But if this has completely skewed off,

**Dave Jones:** it may be trying to do something else. Um so, the phase lock circuit when it's turned off, it disables it. All this isn't used, so that's not used. Any of this isn't used. That doesn't matter. All right, all this stuff doesn't

**Dave Jones:** matter. So, it eliminates a whole bunch of circuitry. Um so, all it's really doing here is looking at this roll off here and this this tuning here. All right, so 360° tuning. That capacitor there could be bad, right? 66, for example.

**Dave Jones:** Um the range selections work. So, uh yeah, this this unit's been a bit of a pain, so it's been a long journey. All right, so it looks like I've had a bit of success with this. I'll just try

**Dave Jones:** changing some adjustments on the oscillator control board um on the off chance that they're just completely out of whack cuz someone's been playing with them. And I turned them a little bit and I see oscillation got really unstable with my

**Dave Jones:** um my own supplied oscillator signal. It was jumping all over the place, and that's interesting. As though there's conflicts between oscillations. So, I removed my my injected signal and um I now have an oscillation going on here. Um and that is from the oscillator

**Dave Jones:** board. So, the oscillator board is now oscillating. And if I change ranges, then it does all its range changes just fine. Okay? Let's bring this up a bit. So, there we go. It's 1 MHz, give or take a little bit. All right.

**Dave Jones:** And um so, yeah, it's doing everything it's supposed to do now. Let's bring it back down. Obviously, I've got channel one connected right now. Uh so, that's on 1.1. So, I'll put it down to 100. So, yeah, roughly 100 Hz is starting

**Dave Jones:** your frequency, but I'll have to figure out how I tune the frequency itself. But, um it's working now. The oscillator board is actually oscillating. So, it looks like it's due to incorrect adjustments on the oscillator control board. So, um I don't actually know what

**Dave Jones:** adjustments do. I haven't gone through that procedure of of calibrating that board yet. But, um where the adjustments are right now, it makes this board oscillate. So, at least now I know this board can oscillate. Uh fun, fun, fun. So, I'm going to leave it

**Dave Jones:** at that for now, and um I think that's probably a good enough example of the sort of things I do. Um Don't forget this is all sort of thrown together in a little bit of a rush cuz I've only got like a day to get this

**Dave Jones:** video into Dave. So, yeah, I've been on holiday and stuff like that. So, yeah. So, now I can be sure that that board is actually capable of doing what it's supposed to do. It is oscillating at roughly the right

**Dave Jones:** frequencies. So, I'm confident that that can do it. It's probably an issue on the control board itself. Um So, we'll we'll have to work through that one in a different video. But, um hopefully you get an idea of what I

**Dave Jones:** would do and um the repair and playing around. So, this scope here is um a loaner from Siglent um for I've done a review on this on this scope, a usage review. And um I'm just playing around with it

**Dave Jones:** for this, you know, cuz it's convenient to set up right here. My own scope's at the back there. Uh but, uh All right. So, don't forget to pop by my channel if you get a chance and have a

**Dave Jones:** look and if you're interested in following the repair process on this. Um and what I actually do to finally calibrate this properly cuz it's got some adjustments on here. I don't know what I do yet. I've got to go through all that.

**Dave Jones:** But, uh I've got the full manual. I just need to uh go through the process now I've confirmed that the board can actually oscillate by itself. That's the biggest step cuz I've been trying to get this to work to some

**Dave Jones:** degree for a couple of weeks now off and on, you know, just trying bits and pieces. But, uh I'm pretty confident that but that board there is okay now. So, one more down. Thanks Dave for the opportunity and good

**Dave Jones:** luck.
