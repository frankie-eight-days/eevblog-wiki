---
video_id: JJwxFFpnt0M
title: ATL HDI3000 Ultrasound Machine
url: https://www.youtube.com/watch?v=JJwxFFpnt0M
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 25, "2": 40, "3": 55, "4": 76, "5": 90, "6": 106, "7": 121, "8": 140, "9": 156, "10": 180, "11": 194, "12": 227, "13": 248, "14": 265, "15": 265, "16": 293, "17": 323, "18": 338, "19": 375, "20": 383, "21": 443, "22": 568, "23": 582, "24": 603, "25": 618, "26": 648, "27": 657, "28": 678, "29": 678, "30": 733, "31": 745, "32": 763, "33": 775, "34": 796}
---

**Dave Jones:** Hi. Check out what I scored on eBay. Woo-hoo! It's an ultrasound machine. Check it out. I got it for next to Nick's. Sorry, I can't get this in shot here. It's a bit hard. It's about a mid-90s vintage ultrasound machine. It's an ATL brand, HDI 3000.

**Dave Jones:** And it's not supposed to be working. It's supposed to be like some sort of software fault with it or something like that. But I thought we'd pair it up and have a look. Yes, I'm going to do a teardown of it, but that's going to be quite some work.

**Dave Jones:** I just wanted to see if it actually worked. The thing is, this thing weighs a ton. We had to hire a ute to transport this thing, and to get it back, it weighs about 200 kilos. So to get it on and off the truck, we had to actually take out all the...

**Dave Jones:** the cards, the power supply, the monitor, had to disconnect everything to actually transport it back here. So hopefully it didn't do any hardware damage. I've installed the cards back in their original configuration. It does come with all the probes and everything. Vital if you're going to get one of these ultrasound machines, which you can.

**Dave Jones:** They sell a lot of these on eBay. Anyway, picked it up for next to nothing. So I think it cost more to hire the ute than it did to actually buy this thing. So anyway... Anyway, let's power it up and see what happens.

**Dave Jones:** Fingers crossed. Now just to give you a very quick look at the boards inside this thing, we've got ourselves an analog power supply, a digital power supply. That's all plus 5 volts. We've got a, what they call a master power supply, plus minus 12 volts, minus 5, and a variable one.

**Dave Jones:** Then we've got a disc controller here. It's a magneto-optical disc. I've actually got... It's taped on the back of the unit. I've actually got... One of the, I don't think it's a rigid, I don't know if it's original or not, but anyway, it's got some software for it.

**Dave Jones:** So that might come in handy. We've got a front end controller board here and all these boards, these are all heavily shielded. Look at this, all this RF braiding all down here. They've got PCI, PCI connectors on here and this board here is an analog interface module.

**Dave Jones:** Then we've got a Doppler acquisition board here, and then we've got channel boards. So we've got eight different channel boards. You can physically see they're a bit different here. And these PCI slots down here actually plug into, this is the backboard here, and you can see all the

**Dave Jones:** PCI slots here, that actually plugs into there and bingo, they're your huge custom multi-way connectors for your three ultrasound probes, which I've actually got with this thing. So this screws on here, heavy, heavy amount of shielding, absolutely massive. And that shielding plate was manufactured '94 by 3D manufacturing, I guess.

**Dave Jones:** All right, let's power this puppy up and see what we get. By the way, yes, there is like a processor or some sort of PC in the back. There's like a whole other rack in the back. I didn't show you on the front there, but anyway, fingers crossed.

**Dave Jones:** Let's power this thing up. Pretty sure I've got the boards in all the right slots. Anyway, yeah, let's go. Is it, it's on here. So, yep, let's go. I hear fans. I hear fans. I see a, I see a LED blinky down, down the front on the board, but

**Dave Jones:** don't see anything on the monitor. There's no hard drive beeps or anything like that, but it's certainly powered up. It's very, very quiet. Is that, maybe it takes a long time to boot. Wouldn't surprise me. It's going to be an ancient architecture, probably even based on a previous

**Dave Jones:** incarnation of this. Like this went from the HDI, like there's the HDI 3000, 5000 after this, this is the HDI 3000. It's probably based on technology before that, so it wouldn't surprise me if the processor is pre that, but geez, now it's really taking a long time.

**Dave Jones:** There is a, there is a LED flashing down the bottom there. You can see, I do have the full, like a user manual and field service guide and everything for this. So, all sorts of troubleshooting guides and stuff. So, hopefully, we can do something.

**Dave Jones:** Maybe it's just let the screen brighten us or something incredibly dumb like that, perhaps. Hmm, let me have a feel for it. I don't know if it's going to work or not, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work.

**Dave Jones:** I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work, but I'm going to try and see if it's going to work.

**Dave Jones:** Hang on, there's a standby, there's an off, no, just standby and on. Okay, here we go. Woo! Yes, lights, camera, action. I don't have the probes plugged in. Wow, test pattern, beauty. We have a test pattern. It's booting, it's booting. This is looking real good.

**Dave Jones:** It's got a track ball on it. Wow, I assume now it will take some time to boot. That test pattern might have come from the ROM, or is it part of the OS that when it boots? I can see lead sequencing going through on the power supply down the bottom, but, okay, could take a while.

**Dave Jones:** No, yeah, here we go. Woo-hoo! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic.

**Dave Jones:** Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic.

**Dave Jones:** Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! Yes, HDI 3000, a system diagnostic. Aha! legends on the keyboard. We've got Doppler. I have no idea what these sliders do. They're not even

**Dave Jones:** labeled. But yeah, it's a, you know, a lot of effort goes into designing these things, which is why they cost, you know, I think like new ones cost $50,000 plus or something like that. They're really expensive bits of kit, even back then and today.

**Dave Jones:** But yeah, I wouldn't know how to use it. You've got to be a sonographer. And well, I do actually know a sonographer, so maybe I can get some help on it perhaps. But yeah, hmm, I might have to do RTFM, I think. And just a quick little look at the

**Dave Jones:** back here. Apparently, this is the processor board in here, and it's got like video, all sorts of video stuff, RGB outs, and also it's whatever, E-Net is, some sort of networking thing, serial and audio stuff. As I said, I've got a disc in here, and it's the, one of these magneto-optical jobs.

**Dave Jones:** There you go. Look, you can see the sectors in there, if you look closely at that. That's really, it's really quite nice. I love those things, but they're completely obsolete. So we've got a rewritable magneto-optical disc from Teijin, made in Japan. So a backup.

**Dave Jones:** It's got the serial number, so yeah, backup OS, or something that could come in real handy. But considering that we've got a hardware, it's given it the same, we've got a hardware fault, then yeah, I, yeah, no, I don't think it's the operating system.

**Dave Jones:** I think it's working just fine. And on the back here, we've got, does that tell us when it was manufactured? Made in the United States of America in Bothell, Bothell? In Washington. There you go. And these are all for the printer, I believe.

**Dave Jones:** So this would be all video and audio stuff, which hooks up to the speakers. If you've ever been in for a ultrasound, you'll know. And then there's a couple of cords hanging out here, and the back of the monitor uses like a custom D25 thing for doing the audio and stuff like that.

**Dave Jones:** There you go. is the ultrasound unit. I need to go read the manual. Hey guys, we're down in the bunker car park. Yes, we. There's Dave. And, ta-da, we have our ultrasound machine. And we had to transport it on the ute. And all the boards, unfortunately, to get it up on here, it was

**Dave Jones:** massively heavy. So we had to get all the boards. We hope they're survived. We were too lazy to stick them back in the thing. But anyway, we've got the monitor. That came off separate. And we've got it strapped on here. Worked all right.

**Dave Jones:** They're strapping. There we go. So it, the only thing we're not sure about, we've got more boards in the back of the ute down in there. But yep, now we've got to, because we had to get the weight down to get it off.

**Dave Jones:** And it's like a couple of, I think it's close to 200 kilos fully populated. And so yeah, we'll just be able to lift it off the two of us, hopefully. Hmm. And you'll notice that I use my bag here as an anti-damper mechanism.

**Dave Jones:** Check it out. So that, that sort of, you know, dampened the boards so the vibration on there wouldn't kill them. Anyway, that's, that's kind of like the best thing we could do at the time. Because we didn't know we were going to have to take

**Dave Jones:** boards out. I didn't think when I was going to pick this up that, you know, we'd be carrying, carting bare boards back. But I, oh, you know, I should have thought of that. Anyway. Woo! *sounds of excitement*
