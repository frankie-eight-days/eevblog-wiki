---
video_id: JI4b-7vpIDc
title: An Unusual Repair
url: https://www.youtube.com/watch?v=JI4b-7vpIDc
source: youtube-asr
---

**Dave Jones:** Hi, we're going to take a look at a returned BM787BT, the new Bluetooth version I believe it is. Think it's the first returned one I've actually had like failed like a new customer. So, let's have a look at it

**Dave Jones:** and Yeah, no, it's a 786. I thought it was the BT one. Okay, once again, very few returns and thousands and thousands of items shipped. So, let's have a look at it. The batteries are separate. It's it's brand new. I think

**Dave Jones:** it's still got the still got the protective film on it. And because these are the original batteries, let's see if it actually has any batteries. And no, no, we're going to have to install them. Okay. Okay, I double-checked these batteries are good.

**Dave Jones:** So, let's go ahead and put them in. Yeah, as I said, the 780 series very rare that one is faulty. So, uh let's go. And as I like it's like it's brand new. We got it and out of the

**Dave Jones:** box the fault is is that it won't turn on. All the segments turn on like it's going through its self-test which normally lasts like a second or half a second or whatever it is and it just doesn't doesn't turn off. So, that is the

**Dave Jones:** apparent fault. So, let's double-check. Up. Oh, there it is. Already. Yep. Sure enough. Uh it's just staying there. That's interesting. Wow, I wonder because the 786 is reprogrammable. Like the user can't reprogram, but I have I've signed an NDA and I've got the

**Dave Jones:** programmer for this thing. So, I can actually reflash the processor in this. So, I might actually give that a go. But sure enough, I'd never known any Brymen meter to do this actually, let alone the 780 series. So, yeah, that

**Dave Jones:** is that is really odd. So, I think I'll just try and reflash it and see what happens. So, down there, you can see that is the program header J1 down there. Sorry, I'm not allowed to tell you what the

**Dave Jones:** processor is or or show you the programmer that I'm using. It's under NDA. It's only for dealers like myself who if there is a firmware change, we can actually change our stock or in this particular case, um if there's something

**Dave Jones:** potentially wrong, I could um try and reflash it anyway. So, let me plug this in. It's a real small pin pitch. Wouldn't be the first time I've accidentally plugged that in like one pin off or something. So, yep,

**Dave Jones:** there we go. We can do this in the Oh, yep, yep, there we go. Even it's in even if it's in the off position. There you go. That is coming That is on because it just it can bypass

**Dave Jones:** the off switch cuz it has direct power through to the processor. So, I've got my external programmer here. So, let me let me press program and see what happens. I've got actually got the firmware programmed into my programmer.

**Dave Jones:** So, I don't have to hook it up to a PC or anything. So, um Busy. It's erasing. Can't Sorry, can't show you, but it it but it is erasing it. So, it's talking to it. It's talking to the processor.

**Dave Jones:** It's programming. Come on. You can do it. Program okay. Checksum. I I've got a green okay light. Well, let's try it again, shall we? I mean, offhand, I can't see how just reprogramming it would fix this. Seems like it Each unit's tested and

**Dave Jones:** calibrated before it leaves the factory. So, it'd be odd if it worked. But there you go. No? It's fixed. That that is weird, isn't it? The processor just needed a kick up the pants. That is odd cuz as I said, every

**Dave Jones:** one of these is factory tested, factory calibrated of course, so it's got to work before as soon as it's finished the calibration and testing process it goes straight in the box and Bob's your uncle. And it gets shipped

**Dave Jones:** out. So how that happened, I've got no idea. Weird. Um yeah. No, the processor's just done something silly bugger and just overriding that worked just fine. Very quick accuracy check test. This should be 1.4801. I'm just using another meter to compare

**Dave Jones:** with. 1.4800. So it's within one least significant digit of my of another BM 786 that I've just got on my bench here. So yeah, um it's it's calibrated. I'll do a better check than that, but uh that's odd. There you go. Um

**Dave Jones:** that's assuming I test that. Um calibration check that, spot check it on the ranges, that's repaired. That's odd. I don't know. Leave in the comments down below if you've ever seen that. What would cause all those segments to come on? That's like the

**Dave Jones:** processor not I I think when maybe when it goes on, I'm not sure if that's the Is there a high con LCD driver chipset in there? I think Yeah, I just so happen to have a >> [laughter] >> a faulty PCB just lying here. Um scrap

**Dave Jones:** PCB, not sure what for. Yeah, so that's the that's the display um driver up there, the high con HY2613C. Um I'm not sure what happens when you like power that on. Does it just power on all segments? And then the processor

**Dave Jones:** down here has to override that? Yes, they just branded BTC, which is Brymen Technology Corporation, of course. I can only presume that yeah, like the processor just didn't boot for whatever reason and it couldn't send the command to clear the LCD. And cuz I

**Dave Jones:** can't imagine the processor booting up and then sending an LC like a turning on all segments and then kind of failing, but you never know. I I don't know. Cuz I don't believe there's a separate boot loader in here,

**Dave Jones:** like boot loader code and then it executes the program because when we were programming this thing over here, it was override. It was just going on to the direct program pins here. It's not like it's going through like a, you

**Dave Jones:** know, some sort of serial interface. I don't believe there's a boot, although I've never seen the code. Don't have access to it. I don't believe that there's like a boot mode or whatever for it, but you never know. I don't know. That is

**Dave Jones:** weird. So, there you go. Anyway, um that fixed it. Winner, winner, chicken dinner. Great. Repair. Thoughts and comments down below. Catch you next time.
