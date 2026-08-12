---
video_id: Ij6r6uXr2Mo
title: Flashing the eMMC on a Raspberry Pi CM4 Compute Module
url: https://www.youtube.com/watch?v=Ij6r6uXr2Mo
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 54, "3": 82, "4": 113, "5": 123, "6": 140, "7": 162, "8": 177, "9": 190, "10": 205, "11": 237, "12": 258, "13": 274, "14": 293, "15": 313, "16": 342, "17": 362, "18": 380, "19": 397, "20": 417, "21": 436, "22": 454, "23": 477, "24": 498}
---

**Dave Jones:** Hi, just a quick follow-up VIDEO ON THE RASPBERRY PI Compute Module. You will see that I have a, well, it's not a new one. It's out of the other unit that I have, uh, which unfortunately, uh, like it's an old engineering sample and, uh, it doesn't have the latest, it doesn't have the software properly, uh, set up for it.

**Dave Jones:** So, I'm going to reflash this board because the Raspberry Pi Compute Module, uh, doesn't have an SD card built in. It's got eMMC memory, uh, built into it. And hopefully, we're going to use my little WaveShare, um, CM4 Nano B board here. Apparently, it is capable of, uh, booting, of operating the USB-C input and as a remote, um, update drive thing and we can install, um, override the new flash Raspberry Pi flash OS and then, uh, Peter from AERL will be able to remote log into this and then set it up,

**Dave Jones:** uh, properly. So, hopefully, yes, I'm aware of That's what happened to the, uh, thermal pad on the, uh, processor there. It's a bit crusty. But anyway, um, let's plug this thing in and see what we get, shall we? So, you remember we're getting like 7 W on the 41 and when we removed the biggest, it was just overloaded. That board was just cactus. So, let me show you this one and we'll be able to view, I've got the HDMI output here. We'll be able to view that as well. There you go,

**Dave Jones:** it's only drawing a watt when it boots and There we go. Um, there's the Raspberry Pi OS and it's, let me turn that off. It's booting. There we go. No wackers. I have no idea what, I assume that's all regular Raspberry Pi stuff. And then, it's got, uh, Tailscale though. Is that normally part of the uh, Raspberry Pi OS? And then we've got the login, um, and unfortunately, yeah, it's not set up and the login doesn't work properly. And anyway, so, I'm going to nuke this sucker, nuke it from orbit.

**Dave Jones:** It's the only way to be sure. Yeah, and then Peter will be able to remote log into this and then set it up for the AER battery uh, gateway function that it's used for. So, 1.2 W, there you go.

**Dave Jones:** That's more like it. Okay, that's more like it. Of course, the processor is just sitting there idle at a boot. It'll take substantially more if you're actually, you know, playing Doom on the thing or something. Okay, so I've downloaded latest Raspberry Pi installer here. Should be really easy.

**Dave Jones:** Now, we can actually set this this WaveShare Nano B board has a boot switch which allows us to enter USB-C boot mode. So, that is so it appears as a drive. I believe the EMC memory there appears as a drive and the image you can just you can just flash it to the internal memory which is on here. Where is it? There or whatever. One of those.

**Dave Jones:** So, you can install it directly on there. This board does have a micro SD slot there which you could use if you were using this adapter board, but we're not. We're programming the compute module, putting it back into the embedded product, the AER gateway.

**Dave Jones:** So, we need to program the onboard memory and not use that flash. So, anyway, let's plug that in, shall we? And in boot mode. So, we've got to turn boot mode on. I think boot mode just like straps one of the pins to ground.

**Dave Jones:** I'm not sure which one. I I think. Don't quote me on that. So, let's plug that in. There you go. We are running. And okay, it's only 0.4 W in boot mode. So, you can see that's using significantly less power in boot mode.

**Dave Jones:** So, it has It looks like it has gone into boot mode. No worry. Choose device. Raspberry Pi 4. Ah, the compute module 4. Okay, yes. All right, so it it's identical. It makes no difference. Okay, I didn't know that. Never programmed a compute module before. We want I guess the latest Raspberry Pi OS. Don't want legacy or anything else. No, don't want any of that weird stuff. Debian Bookworm. Okay, storage. It's not appearing as a drive. Exclude system drives. Um no.

**Dave Jones:** We don't don't want to override our system drive, so it's not appearing. Okay. So, aha, paste the RTFM. Um yeah, it doesn't do it this automatically. I need to do I need to install the Raspberry Pi boot installer, which is then mounts it as an actual drive. That's why it's not showing up.

**Dave Jones:** Uh for Windows users, install I just googled it, and this is what showed up. So, this goes to the official Raspberry Pi Yep. Okay. Set up. That should I should be able to download that. Raspberry Pi USB boot setup. Yep.

**Dave Jones:** Yep, whatever. Some of life away. Yeah, USB boot, and I assume we'll have to reboot after this. Don't know. Should read the RTFM more, shouldn't I? Installing drivers. Okay. So, it doesn't just magically appear as a Windows drive. And I guess, with hindsight, yeah, that's fair enough.

**Dave Jones:** I'll tell you what, it's taking its time. Ooh, that's flashing at me as if Okay, I'm at a prompt. Does it now work? Do I have to do anything? Do I have to put in any any any penguin commands? No, it's still going. I was fooled.

**Dave Jones:** Yeah, I guess it's trusting the major progress bar up the top. But it it was sitting there at a prompt as if it wanted me to enter something. Well, there we go, complete. I've still got it plugged in, so I'm not sure if you're supposed to leave it plugged off or plugged in. Anyway, uh next Do I Oh, no, I've got to run it, right? Choose storage. No, I think I assume I have to run it. Yeah, here it is here. Raspberry Pi boot. Okay, so I've got to run that,

**Dave Jones:** I assume. I've got to run that. Loading. Sorry, you're not seeing that. What? Here we go. Cannot open. Oh. Well, well. Well, what happened there? Uh boot Oh, yes. Yes, there's a problem with this drive. Yes. Yes, it showed up.

**Dave Jones:** There you are. Boom. We're in like Flynn. Boot FS, boot file system. BCM 2711. Yep. There we go. That's all the files on the internal Yeah, that that that appears as a drive. So, now it should pop up as a drive here and it does.

**Dave Jones:** There you go. I've got the 8 gig version. There you go. That wasn't hard. Just had to RTFM. So, choose our device. I've got a Raspberry Pi 4 compute module. Choose OS. We want just a 64-bit port. And choose storage. We want that.

**Dave Jones:** And next. Would you Would you like to apply OS customization settings? No. Don't care. Uh Peter just told me to install like a blank install on there and then he can um uh remote into it. All existing data and OS will be erased. Are you sure you want to continue? Yes.

**Dave Jones:** All right. Cool bananas. Uh you need to format the No. No, that's a Windows thing. No. No, don't get sucked into that. I wonder what would happen if you tried to do that at the same time. Something very bad, I'm sure. Anyway, I'll get back to you when this is done.

**Dave Jones:** All right, we are programmed. I'm going to put that out of boot mode again and plug this in and boom, it's booting. Can we see anything? Yes. Yes, we are booting. Ha. And this should be a different boot process to what we had before.

**Dave Jones:** Still drawing a watt. There you go. So, the unit for those playing along at home, a watt seems to be the nominal value for Oh, no, it's up to 1.8 now when it's booting. Welcome to the Raspberry Pi desktop. Oh, okay. Yeah, so this is definitely a new new installation. Yeah, it's just going to go to the desktop. Silly me. It's not going to I don't think it's Well, yes, it's sure.

**Dave Jones:** Welcome to the Raspberry Pi desktop. Powered blah blah blah. Oh, I may actually have to connect a keyboard and do something here. Anyway, there you go. I won't bore you with the rest of the details, but that is a new compute module flashed and so I should be able to get back on track. I love that. It's done it'll work.

**Dave Jones:** Good enough for Australia. Anyway, there you go. We'll leave it at that. Comments down below. Catch you next time.
