---
video_id: _D_fi_ck9Vo
title: EEVblog #901 PART 2 - RPi 3 Photoflash WiFi Problem
url: https://www.youtube.com/watch?v=_D_fi_ck9Vo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 37, "3": 57, "4": 79, "5": 101, "6": 117, "7": 133, "8": 157, "9": 177, "10": 193, "11": 211, "12": 227, "13": 247, "14": 263, "15": 279, "16": 299, "17": 323, "18": 343, "19": 367, "20": 383, "21": 399, "22": 415, "23": 431, "24": 447, "25": 463, "26": 479, "27": 495, "28": 511, "29": 527, "30": 543, "31": 563, "32": 579, "33": 599, "34": 615, "35": 639, "36": 659}
---

**Dave Jones:** Hi, this is just going to be a quick follow-up video to my previous one on the Raspberry Pi 3 photosensitivity issue, because quite a few commenters asked, and I think rightly so, that it might have been caused, this lock-up issue when you use the photo flash on a camera

**Dave Jones:** on the Wi-Fi module here on the back, which is a new issue which wasn't on the Raspberry Pi 2, that it might have been caused by, you know, some people saying like EMP. It's basically magnetic coupling from the large amounts of current in the photo flash here onto the board.

**Dave Jones:** So it may have been an electrical coupling interference issue rather than photosensitivity of the bare die on the bottom here. So that's a fair enough comment, because the photo flash on here, there's a charge capacitor inside here, a photo flash capacitor, which charges up with a massive amount of energy

**Dave Jones:** and then dumps it very, very quickly into the photo flash bulb here. And there's wires running up the sides here like this, like the capacitors inside the camera, and the wires running up here, this means there's a big loop area here. And what this loop area means is that any corresponding loop area on the board,

**Dave Jones:** you can get effectively magnetic transformer coupling, loosely coupled, from this into this. You've got a high discharge current, very quick, that can generate EMF in loops inside here, primarily power supply loops and other things. Some people might have said the antenna, but the antenna's not actually a loop as such.

**Dave Jones:** Anyway, we won't get into the details of that. I thought, yeah, that's a fair enough comment. Let's actually test it now. What I've got is, I'm just pinging here to 8888 and you can see that our time there is, you know, 20-odd milliseconds or something like that.

**Dave Jones:** Occasionally it jumps up to 30 or something like that, and that's just fine. Now I've got some black electrical tape over the bare die Wi-Fi chip down here, so let's use our flash and see if we can see any variation in that ping time.

**Dave Jones:** No, nothing whatsoever. And let's try it a few times, just for good measure, just to show that it wasn't luck. And for reference, I've got this about 10 centimeters away, actually 11 centimeters away from the actual chip itself. Now, I won't do anything different except physically remove the black electrical tape,

**Dave Jones:** so our bare die Wi-Fi Bluetooth chipset is now exposed. Exactly the same camera position, all the same settings, and bingo, we got the thing to lock up. Now, oh, there, no, no, there we go, it actually recovered. I was going to say, I saw this a couple of times,

**Dave Jones:** it did actually recover. You see it went up to 95 milliseconds there, and, but I had to reshoot this video by the way because I lost all my data because of, don't ask, the memory card issue. Oh, there we go, a thousand milliseconds, and before I got it straight away, but it was actually

**Dave Jones:** 10 centimeters away before, so I'll do that. But anyway, that is confirmed, it is a photo flash issue, and not, I'll put it back, there we go, so we've moved a bit closer. It is, that is definitely confirmed, it is a photo flash issue, photosensitivity issue with the bare die,

**Dave Jones:** the energy at particular frequencies is getting through that die, and let's try it again now, see if I can get a complete lockup. I have actually had it recover like that, that you saw before, but then I have actually had it completely lock up, hopefully it'll do it this time,

**Dave Jones:** where it just does not recover at all, and it completely times out, and we get no more internet. And I think maybe it's going to do that this time. So there you go, that is definitely confirmed, it is not any sort of electrical interference coupling issue,

**Dave Jones:** definitely photosensitivity of the die, absolutely confirmed, and we'll actually start to see some messages. There we go, no buffer space available. So we've completely locked up our internet, didn't recover, it's no good, you have to reboot the board. And no, it doesn't matter

**Dave Jones:** how close I have it here, I've got it like 3 centimeters away now, it's right up its clacker basically, and we can there we go, we can flash that thing, and it does absolutely nothing with the electrical tape in place, it's completely opaque, we take

**Dave Jones:** the electrical tape off, and this puppy is going to lock up, guaranteed. Bingo. Confirmed. And there were also several people who wanted me to use the demessage command, is it? Or whatever it's called, I don't know, I've never used it before, with the slash W follow option, so wait for new

**Dave Jones:** messages, basically. So let's actually try that. Here we go. And I don't know what all that means, it's all Wi-Fi, chipset, Bluetooth, data, whatever, anyway, it's waiting for a response. I'll just put the tape over that, and flash it. We're back at like 11 centimeters distance or anything,

**Dave Jones:** nothing, and take this off, and there we go and we got absolutely nothing out of that whatsoever. Let's go down a bit more, so we're closer, so we definitely know that it's going to lock up, and nope, we didn't get anything out of it whatsoever.

**Dave Jones:** Sorry. And we will see that that is definitely dead. There we go. So of course that's going to be exactly the same issue for the U16 power supply chip on here, just like on the Raspberry Pi 2. There was basically no reason to suspect it wasn't.

**Dave Jones:** Now, sorry to anyone who watched my previous video, seemed to be quite a lot of people, bit of an uproar really, got the impression that I was making out that this was somehow like a really big deal, and it's not. I thought that was

**Dave Jones:** pretty obvious from the video that you had to have it so close that it's an unrealistic scenario, and that Raspberry Pi seemed to possibly, I don't know, we need confirmation from them, maybe purposely tried to fix the U16 issue by putting that black

**Dave Jones:** coating on the top from the Raspberry Pi 2. Because it wasn't really a big deal for the Raspberry Pi 2 either, it was one of those niche things that if you use this exposed board and you know, for an art installation or something, and somebody came up and took a photo flash

**Dave Jones:** photo of the thing, then yeah, it might reset and shut down. In any case, it wasn't a big deal back then because the fix was easy and the odds of it happening to your average person are borderline zero, but it now has a black coating

**Dave Jones:** on, it's probably an order of magnitude better, i.e. less sensitive to that reset issue on that chip. As you saw in my previous video, it had to be like, you know, an inch or two away, right up its clacker in order to, you know, for it to reset

**Dave Jones:** and be an issue. And I thought that was pretty obvious, okay? I didn't, sorry if you got the impression that I made out that it was a big deal. It definitely isn't. I just did it as a follow-up video to the previous one, because nobody had tested the Raspberry

**Dave Jones:** Pi 3 that I could find anyway, to see if this was still a potential issue or not. Regardless of how small the issue is academically, it is quite interesting and potentially hey, I don't know the output of the flash on this camera if you had

**Dave Jones:** a big speed light thing on your digital SLR or something, and you happen to have the bottom of your board exposed like this with the bare Wi-Fi die, and you were relying on the Wi-Fi or Bluetooth or whatever, and it could remotely be

**Dave Jones:** an issue that you might have to take into consideration. But most people will not have to worry about it. It's basically a non-issue, it's just interesting and I thought it was worthy just to point it out to people that, you know, potentially that issue

**Dave Jones:** might exist, regardless of how small it is. Anyway, the fix is easy black electrical tape, blue tack, some sort of, you know, anything opaque basically and non-conductive some sort of silicone or something, it doesn't matter, whack it in a case as most people do.

**Dave Jones:** It's not a big deal. So sorry if you got the impression that I was making out that it wasn't. Anyway, hope you found that interesting definitely confirmed it is a photoelectric issue on that Wi-Fi chip. Still a small problem, and hey, Raspberry Pi

**Dave Jones:** don't have to fix it. It's a low-cost, non-for-profit board, I'm totally aware of that, and you know, no big deal. It's just an interesting video. Anyway, I hope you found that confirmation interesting, and I haven't done extensive tests with exactly how far the Wi-Fi, but you saw it was interesting that it sort of

**Dave Jones:** impulsed the Wi-Fi and upset it a little bit, and then it actually recovered and got the ping. I don't know if there's any other issues, I don't know if Bluetooth did fail doing that or whatever, but you know, I mean the odds of it being that EMP thing were quite low

**Dave Jones:** I think, because the chip designers, for example, they're gonna like this chip, they would have been basically concerned about any, you know, interference to it on the power supply and things like that. That's where they would have concentrated, but like the million-odd transistors inside this thing, or how many it is, and how many

**Dave Jones:** and which ones get affected by the photoelectric effect from this flash here at particular frequencies, practically impossible no predict, protect against or something like that. So, you know that's just the thing with these bare dies. A lot of people ask why do they make these packages if they're photosensitive?

**Dave Jones:** Well, it applies to all bare dies like this, and because they're basically chip-scale packages, they are really, really incredibly small. And these packages are what make your mobile phone and other ultra-miniature products these days possible. If you put them in standard epoxy packages and everything, they're bigger, and maybe

**Dave Jones:** only a little bit bigger, but all that space, extra space adds up. So they're, you know, that's just the thing with these things. A bare die is technically photosensitive. It's nothing new. It's a very well-known phenomenon and that's, you know, usually they go into cases, the mobile phone

**Dave Jones:** case or whatever, and they're not exposed to anything, so they're just fine. So there's nothing wrong with these chipset packages, they're not bad design, they're just exposed die. That's the nature of the beast. Anyway, hope you found that follow-up video interesting. Catch you next time.
