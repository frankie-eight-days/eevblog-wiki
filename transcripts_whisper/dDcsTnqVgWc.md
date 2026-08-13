---
video_id: dDcsTnqVgWc
title: EEVblog #901 - Raspberry Pi 3 Photoflash Problem
url: https://www.youtube.com/watch?v=dDcsTnqVgWc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 17, "2": 35, "3": 50, "4": 66, "5": 83, "6": 102, "7": 124, "8": 142, "9": 163, "10": 182, "11": 207, "12": 223, "13": 239, "14": 255, "15": 284, "16": 300, "17": 313, "18": 322, "19": 336, "20": 352, "21": 367, "22": 383, "23": 406, "24": 424, "25": 439, "26": 455, "27": 472, "28": 489, "29": 506, "30": 526, "31": 538}
---

**Dave Jones:** Hi. In a previous video, I took a look at the Raspberry Pi 2 here and how it was susceptible to the photo flash from a typical camera like this, one of these high-intensity Xenon flashes. The power chip on here, this tiny little thing down in here,

**Dave Jones:** was like a bare flip-chip die, and you could actually, the high-intensity photo flashing, possibly the UV from this, actually penetrated the chip itself and caused the whole Raspberry Pi to reset. And it was a big problem, and everyone made a big thing about it.

**Dave Jones:** But I just got one of these new-fangled Raspberry Pi 3s, and I thought, well, have they fixed the problem? Because I haven't heard anything about it. Now, the power circuitry around here looks pretty darn close to identical, I think it is. But the chip, I'll show you a close-up in a second,

**Dave Jones:** they've actually changed the chip on here. It's still a flip die like this, with the balls on the bottom, but the top looks to be coated in some sort of black material or something like that. So possibly they've fixed that on this thing,

**Dave Jones:** because they were well aware of the problem. But anyway, I decided to flip the new Raspberry Pi 3 over, and of course the new functionality on the Raspberry Pi 3, as well as being a bit faster and everything else, it actually has Wi-Fi and Bluetooth integrated on here.

**Dave Jones:** And look what's on the bottom. A bare die, yet again for the Wi-Fi chipset. Aha! Is this one photosensitive as well? Let's take a quick look at the Raspberry Pi 2 again. Have a look at the culprit down here, there it is, smack in the middle.

**Dave Jones:** U16 there, you can see that is a bare silicon die. Now let's take a look at the one on the Raspberry Pi 3. There you go, you can see it is significantly different. It's got this black sort of coating on the top. I mean it's still bare die around the outside by the looks of it,

**Dave Jones:** but they have put a coating on the top of this thing. So there was much theory about how the light was actually penetrating, and one of them was it can, the UV can actually penetrate directly through the die itself. So maybe just putting that coating on the back is enough.

**Dave Jones:** But they've got a bare one over here by the way, this is for the, this looks like ESD protection? Anyway, I don't believe that one's photosensitive, but on the back of the new Raspberry Pi 3, here it is. There it is, Broadcom BCM43438.

**Dave Jones:** That's combined Wi-Fi and Bluetooth chipset. And you can see bare die, you can see those brush marks right across the back of the die. So, aha! And that's a big ass die too. All right, let's try and photo flash the original power supply U16 in there,

**Dave Jones:** and see if we can get the reset problem that we actually got before. So I'll get right up its clacker here, and can't get much closer than that. And yep, still susceptible. Look at that, wah, wah, wah, wah. Let's try that again, oh I don't know, 15 centimetres away maybe?

**Dave Jones:** No, it's all right, you really have to get right up its clacker. Let's see if I can duplicate that. And I'm sort of at an angle as well, no, no, couldn't get it this time. But you saw it, I got it the first time, that was my first ever attempt.

**Dave Jones:** Oh, yep, there we go, you really have to get close. So it is much improved from the Raspberry Pi 2, where you know, you could get it from like half a metre away sometimes. Let's see if we can flash the Wi-Fi chipset on there.

**Dave Jones:** I've got it connected via Wi-Fi at the moment, you can see there's no Ethernet connected. And I'm playing my previous video, so hopefully it should start up. So hopefully it should stop or freeze or anything if we do something to that Wi-Fi chipset.

**Dave Jones:** Try it again. Nah, still playing. Come on, there we go, flash. And still going is it? Nope, nope, nope, I think we have killed our Internet connection. Google.com, nope, it's not that slow. Bingo, one flash, granted we were very, very close to that,

**Dave Jones:** and it appears that you do have to be quite close to it, but hey, it's still susceptible. You really have to get quite close to it in order to flash it. There we go, I think we're, yep, we've killed it. We've killed it again.

**Dave Jones:** So you've got to be, like, for this particular camera, this particular photo, flash intensity, whatever it is, I don't know, it might be variable. Depends on the current camera settings or whatever. But it's still susceptible, and of course it doesn't lock up the CPU.

**Dave Jones:** The CPU still works, I can still do stuff. I can go in here and do things, I can do this, I can do that, I can do that, I can do that, I can do that. And of course it doesn't lock up the CPU.

**Dave Jones:** The CPU still works, I can still do stuff. I can go in here and I can load up my, you know, load up Boink or do whatever that I've got this thing doing, and I can do that, but it just, it kills the internet connection.

**Dave Jones:** It kills the Wi-Fi connection on this thing. Probably kills Bluetooth as well, because it's the integrated Bluetooth chipset, so almost certainly kills that as well. But of course the thing is, the chip's on the bottom of the board, so it's less susceptible if you have it sitting down like this.

**Dave Jones:** The light would have to reflect back under the board, and it depends, you know, it doesn't sit completely flush because it's got pins sticking out, things like that. So there's maybe enough gap under there. So we'll try that, we'll just get, maybe, you've got to use something reflective.

**Dave Jones:** This mat's not probably good enough, but I can just use some white paper under there like that, and we'll see if we can flash it that way. Alright, let's give it a go. It's under this corner here, so we'll try and sort of get some reflected light back down like that.

**Dave Jones:** Come on, let's give it another flash, just for good measure. And can we jump forward on our video? Yep, no worries, we haven't killed it. So the odds of reflecting under there, board practically zero, I think. So I thought I'd just check to see if there's any extra latch-up current

**Dave Jones:** when the Wi-Fi chipset gets flashed. It's drawing, like, roughly 2 watts, or thereabouts, you know, 0.4 amps or so before. And let's try afterwards. And that's afterwards. Nope, there's no SCR latch-up in the chip, so it's not going to blow up or, you know,

**Dave Jones:** pull excess current and destroy itself or anything like that. So that's just fine. So there you have it. The Raspberry Pi 3 is still susceptible to this photo flash problem. Here's an article on the Raspberry Pi blog itself from, like, almost a year and a half ago now

**Dave Jones:** explaining what the photo flash problem is, and Peter Ungan originally found it and showing the current waveforms and the latch-up and the bare die and, you know, everything else and how the photo flash, you know, and links to videos of how photons over a certain energy

**Dave Jones:** can penetrate the die and everything else. And they've been well aware of this, yet they haven't fixed the problem. Although it looks like they might have attempted to because that U16 voltage regulator chip is now... looks like it has some sort of black coating on it or something like that,

**Dave Jones:** but it's still effectively the same package and it's still susceptible. Not as bad as the Raspberry Pi 2. Granted, you have to get really up close, start using exactly the same camera I had before. So that's much less susceptible, but it's also susceptible to the Wi-Fi as well.

**Dave Jones:** I have not done extensive tests to actually get the exact distance and things like that with different cameras. I'll leave it up to other people to do that or Raspberry Pi to investigate themselves, but you can lock up the Wi-Fi and presumably the Bluetooth as well with the same issue.

**Dave Jones:** So there you go. Hope you enjoyed that. Catch you next time. Hi. How many of you have one of these lying around? A Raspberry Pi. Hey, it's a cool little Linux computer, you know, and it's super-duper cheap. But there's probably a lot of these lying around doing nothing,

**Dave Jones:** just going to waste. So I thought that was a bit of a shame. So I thought, hmm, I've got a couple of these lying around the lap. What can I do with them? Can I do anything useful? I know. Let's look for aliens.

**Dave Jones:** Why? Because aliens.
