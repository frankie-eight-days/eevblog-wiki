---
video_id: XRyDyOANQhc
title: Guest Video: The Defpom - Fluke Calibrator Repair
url: https://www.youtube.com/watch?v=XRyDyOANQhc
source: youtube-asr
timestamps: {"0": 12, "1": 26, "2": 35, "3": 45, "4": 63, "5": 68, "6": 80, "7": 93, "8": 102, "9": 113, "10": 122, "11": 131, "12": 141, "13": 154, "14": 179, "15": 203, "16": 220, "17": 233, "18": 245, "19": 258, "20": 267, "21": 280, "22": 288, "23": 303, "24": 311, "25": 320, "26": 328, "27": 339, "28": 352, "29": 364, "30": 381, "31": 410, "32": 433, "33": 452, "34": 468, "35": 480, "36": 501, "37": 515, "38": 529, "39": 552, "40": 565, "41": 591, "42": 610, "43": 625, "44": 646, "45": 656, "46": 676, "47": 692, "48": 706, "49": 717, "50": 731, "51": 741, "52": 760, "53": 777, "54": 789, "55": 809, "56": 822, "57": 837, "58": 859, "59": 869, "60": 886, "61": 898, "62": 909, "63": 921, "64": 935, "65": 953, "66": 965, "67": 974, "68": 985, "69": 1002, "70": 1016, "71": 1028, "72": 1037, "73": 1042, "74": 1050, "75": 1061, "76": 1075, "77": 1085, "78": 1097, "79": 1110, "80": 1118}
---

**Dave Jones:** Hello everyone. I'm the Defpom. First name Scott. Hopefully Dave chooses this video for his guest spot while he's away on holiday. And uh I thought I'd just tell you a bit bit about me and about my channel and what I do.

**Dave Jones:** Um This unit here is one of the things I'm working on currently. I do a lot of prepare videos mostly on test equipment. Um I do do some review reviews as well on new gear.

**Dave Jones:** I've done some reviews of Siglent in the past. Um you might have seen those. Um also anything else sent to me as well. I do mailbag videos, things I've purchased and and so on.

**Dave Jones:** I also do CB repair work and I've done a little bit of videos on that. Um but mostly mostly what I do these days is test equipment repairs. So if you're interested in you know seeing me fixing test equipment stuff then carry on watching and check out my channel.

**Dave Jones:** So this is one of a piece of gear I'm working on right now and I've had it in my possession for quite some time now for a few months.

**Dave Jones:** And it's been a bit of a pain. I think every single board in it has a fault. Every board is faulty. I think it's a parts unit which has been used for good parts for other ones.

**Dave Jones:** This is a Fluke 5200A AC voltage calibrator. Um and I'm working through the repairs on this and I'm just going to go through and show you a bit on troubleshooting at the moment and just doing some diagnostic work.

**Dave Jones:** So it's going to be a little bit technical but not overly so. I'm not a hugely technical person. I'm very much you know out there and unplanned videos I just sit here and just speak and go through it.

**Dave Jones:** I don't have a script or anything like that. So hopefully you don't mind me falling over my words a little bit, things like that. So this is what I'm working on and um I've been working through the cards.

**Dave Jones:** I've already got two cards repaired but I'm still doing some more diagnostic work. Um I've already repaired the power supply, we've repaired all that, and done some substitutions and so on.

**Dave Jones:** Um so I was going to show you this. If you want to see more about this particular repair, um I've got a series on my channel of repair so far up to date.

**Dave Jones:** Um and there will be more as well as I progress through it. Um but hopefully this is a little sample of of, you know, what you might get to see if you come to my channel and have a look and uh hopefully subscribe and so on.

**Dave Jones:** So hopefully Dave chooses me. Otherwise it will never see light of day. Okay, so to start off with, I should explain what's going on here. Now this board here is the oscillator and it isn't oscillating.

**Dave Jones:** All right, so what's supposed to happen is it's supposed to have a phase uh change as it goes through each amplifier stage on this board. It's supposed to go 380° on the first stage, 90°, and 90° again to get 360° or thereabouts, um which is then controlled electronically by the control board, oscillator control card, um which then fine-tunes that frequency, allows for any changes on the front panel controls,

**Dave Jones:** and so on. Um that's the theory, all right? But the oscillator doesn't work. So what I'm actually doing is injecting my own oscillator signal into the unit um at the input, which is then passing through the stages, and then I can actually test each stage that way with an artificial injection of a of a signal, um which at least proves that each stage is working.

**Dave Jones:** I've done this previously in the another part of video, um another section I've done, which showed the gain of each amplifier, which is about 40 times gain. Um so those are actually working, you know, at least I know as far as amplification goes, but not as far as phase.

**Dave Jones:** Um and that's where I'm thinking the issue is now why it's not oscillating is because if the phase is wrong, then it won't oscillate because it's out of phase with itself, and so it doesn't generate an oscillation.

**Dave Jones:** Um but it's quite a complicated little setup they've got going on here. Um It goes across two different cards, which is influenced by a third card, which is fed by my fourth card.

**Dave Jones:** So, it's a case of eliminating which part is causing um the problems and and trying to prove which bits work, which which which bits don't. Um so, it's a it's a pain.

**Dave Jones:** And um it's been a long process. So, hopefully this video is a little bit interesting for you. Um I doubt I'm going to actually achieve anything in this video.

**Dave Jones:** I'll be I don't think I'm going to fix anything today cuz it's it's a lot to go through. And um but hopefully you find it interesting. All right. So, I've got my uh test set up here.

**Dave Jones:** Now, I'm using the new SDS 1104X E scope, which I've been reviewing recently. And um I was playing around with it still cuz it's four channels and it's convenient.

**Dave Jones:** And um I've got this hooked up onto the oscillator uh control board. Well, oscillator board, sorry. And what I'm trying to measure here is the phase in between each oscillator stage.

**Dave Jones:** Um it's supposed to change phase as it goes through. Now, I'm actually having a bit of trouble measuring the first stage um between the input and the and the output of the first stage.

**Dave Jones:** Um so, I'm going to have to probably come back to that, but for now, I can move on and test the other stages and see if they look right.

**Dave Jones:** Okay. So, let's move the camera down. I'll show you what I've found so far. Okay. So, I've taped off on the inputs and stuff on this card now, so I can actually measure the phases on each stage.

**Dave Jones:** So, this is the input for my oscillator. This is the output of the first stage, output of the second stage, output of the third stage, right? So, you should be able to see the phasing from each one.

**Dave Jones:** Now, if I zoom in slightly, you should be able to see it a little bit better. Um so, you can see 1 to 2 is almost 90°. Depends on the frequency as well.

**Dave Jones:** So, if I actually adjust the frequency on the Fluke, um these phases will change slightly. Now, it's at say 89°. Phase between 2 and 3 should is actually -87.

**Dave Jones:** So, it's actually 270° out in theory, but actually it's almost in phase with the first one. Um 3 to 4 I sorry, 2 to 2 to 3 is those two.

**Dave Jones:** So, phase 3 is actually in phase with the first one pretty much. And phase 4 is at 19°. All right, so phase 4 is actually 270°. Now, it says -86 cuz obviously it thinks it's going around, but the issue here is that this first difference here between the input and the output of the first stage is supposed to be a 180° phase difference.

**Dave Jones:** Not 90°, according to the manual. So, that's probably why it doesn't work properly. All right. So, I've tested each stage and each stage is amplifying and doing things it's supposed to do, but that's why I wanted to come and check the phases because um if this isn't right, then it throws the whole thing out.

**Dave Jones:** So, say this first stage here is supposed to be 180°. It's supposed to invert the input. It's not doing that. Um so, I found that quite interesting. Um and these other two stages are supposed to be 90° out from each other.

**Dave Jones:** But, what I've got here is 90°. 270°. And it's like 270 again, effectively, but it's yeah. It's not doing what you think it should do. So, yeah, it's a bit of a pain.

**Dave Jones:** Um I need to investigate this first bit here cuz it's supposed to be inverting the input. That's what's supposed to happen. Okay, so this is the circuit diagram for the oscillator board.

**Dave Jones:** Now, these phases I'm looking at on the scope. Now, this is the input here, TP2. I'm measuring at TP3 for channel two, and TP5 for channel three, and TP7 for channel four.

**Dave Jones:** So, this first stage here is supposed to be 180° inversion. And this stage here is supposed to be 90° inversion. This is supposed to be 90° inversion. So, well, phase diff phase change.

**Dave Jones:** Um and that's not what's happening. This phase here with this stage here is not doing 180°, it's only doing 90. Now, this has some other aspects along with it.

**Dave Jones:** Um there's a summing amplifier out here, which is in parallel with the device. Summing amplifier in, summing amplifier out, they go to the um oscillator control board. And um it gets a bit more complicated, certainly, but they actually have a capacitor across it, which is used to tune this response.

**Dave Jones:** Um There's also an oscillator to zero here. Um I've tried adjusting that, it didn't seem to change anything, but um so, let's just look at the summing amplifier out and summing amplifier in.

**Dave Jones:** Let's see what those do. Um those are on the control PCB, which is here. Now, they Um are here, so I'm going to fight in over here. And so I'm going to fight out.

**Dave Jones:** So, those pass through. Now, this is going through this network here. Um which goes back into here. And into here. This This box. All right. So, let's go back down to the next page.

**Dave Jones:** And this is that box. So, amplifier in is here. And so I'm going to fight out is where? It's also labeled as H. So, I should look for that, too, shouldn't I?

**Dave Jones:** Um H, there we go. There. All right. So, oscillator control in this is a level control. All right. So, um I did find some faults. I think I replaced some capacitors somewhere in this part of the circuit.

**Dave Jones:** Where was it? Over here. I think I replaced these caps here, I think it was. So, there was an issue with this particular board. This I'm suspicious of this circuit here.

**Dave Jones:** I think something in here isn't right. Um So, this is supposed to come uh out of this device here, go to the amplifier, feed through the amplifier, come back, and go across this stuff here.

**Dave Jones:** So, it's all amplifying DC amps and stuff here, as well. So, this is supposed to be um providing some amplification, and it's probably affecting the oscillator. Now, there's other stuff here that you can see there, too.

**Dave Jones:** Now, you got these various capacitors which are being switched in as well by these relays. These were part of the quadrature amplifier and the oscillator amplifier. Those seem to be working okay.

**Dave Jones:** Those look about right. So, I'm pretty confident these capacitors here were working okay and that all these relays here were working okay, as well. Um I've done individual testings for everything.

**Dave Jones:** Um and I've actually eliminated the phase lock circuit by not having it turned on. It disables that part of the circuitry. So, um just trying to figure out exactly which part is causing problems now, which I believe is in this amplitude control circuit here.

**Dave Jones:** Um because it doesn't seem to be doing the right thing. It's a bit of a tricky process cuz it's all one big loop and um it's it's a bit of a pain.

**Dave Jones:** Now, there's actually a bit in the in the diagnostics here somewhere. See if I can find it. Um theory of operation functional block diagram is it here somewhere? Here we go.

**Dave Jones:** This is it. All right, so what I was actually hoping to try today was to try and do a bit of a shortcut here. Now, the oscillator assembly I know does oscillate.

**Dave Jones:** Now, this is So, you got this shows us phase shifts of 90°, 90°, 90°, okay? So, that isn't phase shifting like it should be. But, that is controlled by this summing amplifier in.

**Dave Jones:** All right, it's from the oscillator control assembly. So, um this may or may not be working correctly. But, is that because there's no amplifier control from here? Now, I've actually measured this test point here at at uh connection 51, pin 51 on the card.

**Dave Jones:** And that's reading 0 V. So, and it's supposed to be between -15 V and 0 V. So, if it's 0 V to me says it's fully out of one range.

**Dave Jones:** So, and that's without the amplifier installed cuz that's blown. All right, so everything's blown. Reference assembly is fixed. I've already repaired this and I'm I'm 99% sure this card is is good now.

**Dave Jones:** Um but uh I would want to actually want to originally inject my own voltage here in pin 51. But I had some other complications going on um with the wire ties reference voltages together cuz it uses reference power supply which is linked to AC to DC converter through this cable here.

**Dave Jones:** Um which has a negative reference. Which then gives the correct power supply output from the main power supply cuz it checks the reference voltage first and it's all tied together that way.

**Dave Jones:** So, it's a bit complicated and involved. I might still go that route yet though. So, I actually want to inject a negative voltage here and see if it corrects the frequency here.

**Dave Jones:** Um it probably won't. It's supposed to be for amplitude control. But if this has completely skewed off, it may be trying to do something else. Um so, the phase lock circuit when it's turned off, it disables it.

**Dave Jones:** All this isn't used, so that's not used. Any of this isn't used. That doesn't matter. All right, all this stuff doesn't matter. So, it eliminates a whole bunch of circuitry.

**Dave Jones:** Um so, all it's really doing here is looking at this roll off here and this this tuning here. All right, so 360° tuning. That capacitor there could be bad, right?

**Dave Jones:** 66, for example. Um the range selections work. So, uh yeah, this this unit's been a bit of a pain, so it's been a long journey. All right, so it looks like I've had a bit of success with this.

**Dave Jones:** I'll just try changing some adjustments on the oscillator control board um on the off chance that they're just completely out of whack cuz someone's been playing with them. And I turned them a little bit and I see oscillation got really unstable with my um my own supplied oscillator signal.

**Dave Jones:** It was jumping all over the place, and that's interesting. As though there's conflicts between oscillations. So, I removed my my injected signal and um I now have an oscillation going on here.

**Dave Jones:** Um and that is from the oscillator board. So, the oscillator board is now oscillating. And if I change ranges, then it does all its range changes just fine. Okay?

**Dave Jones:** Let's bring this up a bit. So, there we go. It's 1 MHz, give or take a little bit. All right. And um so, yeah, it's doing everything it's supposed to do now.

**Dave Jones:** Let's bring it back down. Obviously, I've got channel one connected right now. Uh so, that's on 1.1. So, I'll put it down to 100. So, yeah, roughly 100 Hz is starting your frequency, but I'll have to figure out how I tune the frequency itself.

**Dave Jones:** But, um it's working now. The oscillator board is actually oscillating. So, it looks like it's due to incorrect adjustments on the oscillator control board. So, um I don't actually know what adjustments do.

**Dave Jones:** I haven't gone through that procedure of of calibrating that board yet. But, um where the adjustments are right now, it makes this board oscillate. So, at least now I know this board can oscillate.

**Dave Jones:** Uh fun, fun, fun. So, I'm going to leave it at that for now, and um I think that's probably a good enough example of the sort of things I do.

**Dave Jones:** Um Don't forget this is all sort of thrown together in a little bit of a rush cuz I've only got like a day to get this video into Dave.

**Dave Jones:** So, yeah, I've been on holiday and stuff like that. So, yeah. So, now I can be sure that that board is actually capable of doing what it's supposed to do.

**Dave Jones:** It is oscillating at roughly the right frequencies. So, I'm confident that that can do it. It's probably an issue on the control board itself. Um So, we'll we'll have to work through that one in a different video.

**Dave Jones:** But, um hopefully you get an idea of what I would do and um the repair and playing around. So, this scope here is um a loaner from Siglent um for I've done a review on this on this scope, a usage review.

**Dave Jones:** And um I'm just playing around with it for this, you know, cuz it's convenient to set up right here. My own scope's at the back there. Uh but, uh All right.

**Dave Jones:** So, don't forget to pop by my channel if you get a chance and have a look and if you're interested in following the repair process on this. Um and what I actually do to finally calibrate this properly cuz it's got some adjustments on here.

**Dave Jones:** I don't know what I do yet. I've got to go through all that. But, uh I've got the full manual. I just need to uh go through the process now I've confirmed that the board can actually oscillate by itself.

**Dave Jones:** That's the biggest step cuz I've been trying to get this to work to some degree for a couple of weeks now off and on, you know, just trying bits and pieces.

**Dave Jones:** But, uh I'm pretty confident that but that board there is okay now. So, one more down. Thanks Dave for the opportunity and good luck.
