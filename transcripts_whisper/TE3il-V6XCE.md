---
video_id: TE3il-V6XCE
title: This is NOT a repair video
url: https://www.youtube.com/watch?v=TE3il-V6XCE
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 36, "3": 48, "4": 64, "5": 76, "6": 96, "7": 112, "8": 124, "9": 140, "10": 161, "11": 173, "12": 193, "13": 213, "14": 233, "15": 245, "16": 261, "17": 282, "18": 298, "19": 318, "20": 338}
---

**Dave Jones:** Hi, on my second channel, and you should subscribe over there, it's where I dump all the unusual stuff, is this DS418 NAS drive. I had a hard drive fire, and in that video I mentioned that this dumpster TP-Link switch that I've got here,

**Dave Jones:** well, it's died. Well, at least half of it has. Because I have lots of ports in my lab here, and they're all locked up here, and I've been wondering why some of them haven't worked lately. You know, I've been shooting videos trying to test stuff out, and like, I thought,

**Dave Jones:** oh, you know, bad cables and, you know, things like that, all sorts of settings and stuff like that. Well, I do believe that this entire block of eight Ethernet ports is dead. This, all this block here works just fine, and I do need that many.

**Dave Jones:** I've got like, you know, two coming from that NAS drive alone. I actually bound and bind those together to get, like, faster transfer speed, and I've got a whole bunch of other, you know, computers and printers, and when you add everything up, like,

**Dave Jones:** eight ports just, you know, it doesn't quite cut the mustard. So, yeah, something's happened with this. So I thought I'd rip this thing out and take it apart and see what's what. Let's see if we can repair this dumpster switch, which I've had for probably five years.

**Dave Jones:** It's been incredibly useful. Like, there's no fan in it, it's all passive, it's very nice, and it's worth the treat. It's a one gig bit switch. So, let's check it out. Okay, here it is. It's a TP-Link TL-SG1016, for those playing along at home.

**Dave Jones:** 16-port gigabit Ethernet switch. And, as I said, this entire port here seems to work, but this one doesn't. I'm just getting no activity LEDs whatsoever over here. So, yeah, and no functionality. And as I said, like, it's all passively cooled. It doesn't get hot.

**Dave Jones:** I haven't measured the power consumption, but I don't, well, that's the fuse. But, yeah, there's no fan in the thing. I rather like it. I got it from the dumpster, and it's been a very reliable gigabit Ethernet switch. So I'd like to repair it if I can.

**Dave Jones:** And the interwebs, which I had to access on my phone, because I now have no internet in my lab, says that this takes about 19 watts. So, let's crack it open and have a look what's inside. That should just pop off. Ta-da! Ooh!

**Dave Jones:** That one's smaller than that one. There you go. So that's interesting. But, I spy with my little eye, straight off the bat, a power supply section, presumably for this one. And another one over here, just by their physical locations, says that that one is going to supply

**Dave Jones:** here, and this one's going to supply that. So, you know, that, like, right off the bat. I mean, obviously, this main one over here, I reckon they're in parallel. I reckon that's just, like, 12 volts in, and that's it, I'd say. But, yeah, there's not much in there, is there?

**Dave Jones:** Um, that's... that's it. Great. So, yeah, most likely power supply. But, you know, it could be the chippy. But there's not much else. And the first thing is the visuals. There's the good power supply, which I'm presuming must be good, because it powers this puppy here.

**Dave Jones:** And, yep, they are vented capacitors, which means they have electrolyte in them, and the magic smoke can escape. But they look good. So, just go over to the other one over here, which looks identical. Oh, no, no, no, it does have... no, they're not identical, because this has got a single

**Dave Jones:** SO8, big inductor, and two surface-mount trannies here. This one has just two SO8s, and no surface-mount trannies. So, yeah, they're very different. One could be 5 volts, one could be 3.3, perhaps. I don't know. Just, I thought, by the physical location of them, that, yeah, this would power this, and this would

**Dave Jones:** power this. Although, that could still be the case. We'll find out. First of all, it's time for some takeaway protection, just so that I don't accidentally touch that part of the power supply, because live heat sinkies and stuff like that, trap for young players.

**Dave Jones:** Anyway, they've got it powered up, and of course, like, there's no indicator LEDs on the front when you've got nothing plugged into it, so that's annoying. I'd have to plug something functional into it, dammit. Thankfully, I do have an Ethernet scope here, so I just

**Dave Jones:** power that on. You can see, random port here, got a green LED, you know, change it to anywhere else, green LED comes on, change it to over here, green LED comes on. Uh, uh, uh, uh, beulah, beulah, that wasn't supposed to happen. I'm sure that wasn't happening before.

**Dave Jones:** Okay, it's making an absolute fool out of me. Great. Now let's just measure some voltages here. Measure the output of the inductor there, which will be across these two low ESR output caps. You can tell because they're green, sorry you can't see that, but.

**Dave Jones:** 1.2 volts. 1.2 is a standard rail. The silkscreen's not marked in any way, so yeah, you just have to go, well, 1.2 is a standard rail that you get for like a high-density VLSI ASIC like this, so yeah, no wuckers. And let's try this one over here.

**Dave Jones:** 3.3, of course, you know, you're going to need 3.3 for almost everything these days, so no surprises for finding 3.3 volt and 1.2 volts in there, so yeah, along with the fact that those LEDs are lighting up, I've just goofed this. I've just, maybe I've got

**Dave Jones:** some other, I do have maybe a cabling problem, and I've just come a gutter. This is embarrassing. Oh well, you won't see this video.
