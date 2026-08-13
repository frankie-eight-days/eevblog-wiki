---
video_id: sCPfEPSDh40
title: How Badly Can I Screw Up a Home Assistant Install?
url: https://www.youtube.com/watch?v=sCPfEPSDh40
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 32, "3": 44, "4": 64, "5": 80, "6": 96, "7": 112, "8": 132, "9": 152, "10": 172, "11": 192, "12": 216, "13": 240, "14": 256, "15": 280, "16": 304, "17": 328, "18": 348, "19": 368, "20": 392, "21": 408, "22": 428, "23": 452, "24": 472, "25": 488, "26": 512}
---

**Dave Jones:** Hi, there's quite a lot of people on my recent dumpster diving video who recommended that this HP ThinClient, the T630 or the T620 that I got from the dumpster here might be a perfect candidate for the home assistant operating system. And I've been thinking about playing around with that.

**Dave Jones:** Not that I like smart homes or anything like that, but maybe I can do some solar stuff with it. So, I think it talks to solar assistant in that regards. And I'm thinking about installing a second solar assistant which maybe talks to the end phase.

**Dave Jones:** I think that's possible. Maybe combine them together. I don't know. So, I thought I'd just check that out. First thing is to measure the power consumption. Because I don't want the bloody thing drawing, you know, 40 watts or something like that. So, let's actually power it up.

**Dave Jones:** 0.6 watts on standby here. And 16 watts. 15. It's jumping up. I think it jumped to 33 on the start. And this has got windows embedded on it, so it could certainly change depending on the OS. But she's booting. She's booting. She's getting the windows.

**Dave Jones:** And come on. You can do it. 14, 15 watts. I'd want lower than that. Because usually like you run these sort of things on a Raspberry Pi, which are going to be way under this. So I'd want, you know, under certainly single digit wattage.

**Dave Jones:** I want under the 10 watts. But no joy so far. But let's wait. Because Windows has various, you know, dynamic power things. But yeah, I haven't gone into the BIOS of this thing yet and set it up or anything like that. But let's just see what we get for the stock.

**Dave Jones:** Oh, hello. 10. I saw 10 there for a second. This is the, hey, 8. 8. There you have it. So that's just, yeah, once Windows embedded settled down there, it looks like just doing nothing. It's sitting there. Oh, it jumps up to 11 occasionally.

**Dave Jones:** But it's sitting there doing 8 watts. I'll just plug in the ethernet-ies. Oh, 20 watts. Hello. No, it's back down to, yeah, it's back down to 8. There you go. That's not too shabby. A little bit more than a Raspberry Pi is going to take, I think, isn't it?

**Dave Jones:** I don't know. What's the modern one taking? But that's not bad. Okay, so press escape and we get into our boot menu here. We can get system information like this. There you go. Sure enough, T630. Yeah, it's got AMD GX420GI Radeon, 2 gigahertz speed.

**Dave Jones:** We've only got 4 gig of memory. Only when I was a boy. But I assume that's enough. Okay, boot menu. And I have actually plugged in my USB stick down here. I guess I could plug it into the outside, but isn't this like a boot-y

**Dave Jones:** thing? But anyway, it probably doesn't matter. Boot menu, here we go. UEFI, boot sources, yes, that's what we want. Oh, oh, it's not detecting any. Okay, yeah, it doesn't like that, so let me remove that and plug it into, aha, that's better. Yep, I had to plug it

**Dave Jones:** into one of the external USBs. So there you go, SanDisk Competition 1. So that I've already installed. I've, with Balena Etcher, I installed the home assistant. And boom! We are booting, we are in like Flynn. Okay, I haven't installed home assistant before, but I assume, I don't know, all the nerds know what they're doing, and this should

**Dave Jones:** just work for a dummy like me. That's the plan anyway. And there you go, that's only drawing just 8.5 watts there doing the install. So yeah, that looks like it's sort of like nominal base level operating power, which isn't too shabby, really. For a processor that I believe is sort of like more

**Dave Jones:** better than even the best Raspberry Pi going today. We are installing the Hayos, which is the home assistant operating system. And it's taken a while, but yeah, I assume this will just overwrite the 32 gig solid state drive which we've got in here.

**Dave Jones:** Quite a few people said that was plenty enough to run this. It should be, because this I think, what was the binary? It wasn't that big. Oh, look! Excellent! We have a prompt! Home assistant! Joshua? Error unknown! Come on! Seriously? Help games. Help!

**Dave Jones:** There you go! See, the more complicated a system is the more it has to help you out. Unfortunately, look what's happened. The power draw has gone up. 13 watts average, maybe? Just sitting there doing nothing? I don't like that. I'm going to have to maybe get into the biasy thing and see if I can

**Dave Jones:** slow this sucker down, because you know, 14 15 watts, that's a bit much. Well, apparently I'm dumb, because I took the stick out and Windows is still on there. I just assumed that it would have automatically installed onto the solid state drive internally, but nope.

**Dave Jones:** Like it didn't even give me an option to tell me where to install it. So yeah, it's just installed it on the stick. Well, I asked grok and it said at the command line do hardware info so I did that and it just went crazy and gave me all this hardware info

**Dave Jones:** to see if it recognizes the drive, but I assume it will. So I'm supposed to now do OS install and then put the slash dev and then the name of the drive, and it looks like device sda1 but that's the sandisk, that's the 32 gig, okay

**Dave Jones:** excellent. SDA1, let's try that Oh, this command set is specifically designed for home assistant and only works on those systems, it provides an interface to get it, yeah, yeah, OS, install. Why didn't it let me do that? Why? Why? I've got command line access, I'm rooting in, aren't I?

**Dave Jones:** Am I using the correct terminology, kiddies? Eh, what am I doing wrong? It shouldn't be this hard. Really? Could you like add an option when you like install this thing to like select which drive you want to install it on? I don't think that's much of an ask, is it?

**Dave Jones:** Or, do I have to be literal and put ha os install, because yeah, it says usage uh-huh, but I thought we were, I didn't have to put the ha because I was already at the ha prompt, but maybe that's it so ha os install dev slash sda1

**Dave Jones:** let's try that. No, it didn't like that either. I've definitely got that correct I've followed the instructions, at least what I thought I should have to do, it's detected that drive, it's there, it's slash dev slash sda1 slash dev slash sda1 ha os

**Dave Jones:** install. Ah, it tells me ha is not necessary in this ha cli. Yeah, okay, then I can get rid of that like I did before, and nothing. Okay, I had a conversation with grok and it's pretty darn helpful, and it seems to think that I'm trying to install it on a partition

**Dave Jones:** and it needs to install it on the entire drive, so it recommended lsblk, but that didn't seem to work, but it just seems to think that I can do just sda like this, so let me try that. Nope, it didn't like that either.

**Dave Jones:** Done all sorts of things that grok recommended like piping it into less, which should pause the screen, that wasn't supported, so then it said I could like redirect that into a hardware.txt file, it didn't like that, so yeah, what am I doing wrong?

**Dave Jones:** Alright, I'm not going to spend any more time on this now, I'm going to do something more productive. Leave it in the comments. What dumbass thing is dumbass Dave not doing? Catch you next time.
