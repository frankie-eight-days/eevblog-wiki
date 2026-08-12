---
video_id: 6M-xXEn1_iI
title: FAILED PROJECT IDEA - 53131A Mod Board
url: https://www.youtube.com/watch?v=6M-xXEn1_iI
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 28, "3": 38, "4": 47, "5": 56, "6": 76, "7": 85, "8": 96, "9": 110, "10": 124, "11": 134, "12": 144, "13": 158, "14": 172, "15": 185, "16": 198, "17": 215, "18": 226, "19": 240, "20": 251, "21": 265, "22": 284, "23": 293, "24": 302, "25": 309, "26": 323, "27": 333, "28": 339, "29": 354, "30": 366, "31": 392, "32": 414, "33": 423, "34": 435, "35": 447, "36": 461, "37": 470, "38": 494, "39": 508, "40": 519, "41": 533, "42": 556, "43": 563, "44": 575, "45": 586, "46": 600, "47": 614, "48": 640, "49": 655, "50": 684, "51": 711, "52": 731}
---

**Dave Jones:** Hi, it's project time. I want to upgrade uh my venerable Agilent, not that Keysight rubbish, uh 53131A universal frequency counter. And this is an awesome bit of kit. It's practically the industry standard uh frequency counter on the market.

**Dave Jones:** It always has been, back when it was HP 53131A, and then Agilent, now Keysight. Um and it's also available as the 53132A, which I'll talk about in a in in a minute is more better.

**Dave Jones:** So, if you want one of the best frequency counters on the market and you're like looking to pick one up second hand, I'd recommend the 132A. And I'll show you why uh in a minute.

**Dave Jones:** But anyway, this is a very cool frequency counter. Seen in this thing quite a few videos over the years. And uh I've also done a VFD to LCD. This is a blue LCD um upgrade for it.

**Dave Jones:** So, I'll link in that video if you haven't seen it. But whilst this unit has an excellent uh 12-digit display, I'll show you in a minute. We can actually get an extra two digits on here.

**Dave Jones:** Um it's actually capable of 15 digits. So, I actually want to modify this, make a little board, and modify this to add three extra digits in here. And you might think there's not space, but I think I've found a really tiny little display where I can add three extra digits to here.

**Dave Jones:** So, I think that'll be a very cool little uh project to do. So, uh this is part one of it. Now, you can see at the moment that we've got uh 10 digits here.

**Dave Jones:** Now, it's actually capable of more because uh as you can see, it's updating, you know, reasonably quickly. It's actually updating at 10 times per second. We can go into the um the gate uh time here.

**Dave Jones:** And the gate time is uh 0.1 seconds. So, we're updating 10 times a second. So, it's actually measuring uh that input and updating. But if we increase our gate time, if we go up to a second, watch what happens.

**Dave Jones:** We go back to the frequency display, and now it's going to update once per second. But boom, we've added an extra digit on the end, like that. And uh you guessed it, if we go up to 10 seconds gate time, so each measurement takes 10 seconds.

**Dave Jones:** This is not including any averaging or anything like that. Um so we go back and we will will have to wait the 10 seconds. Twiddle your thumbs, but trust me, it will come up.

**Dave Jones:** It will come up. Bingo, there it is. We've now got the full 12 digits that this display is capable of, but it only updates uh once every 10 seconds.

**Dave Jones:** But here's the difference with the other model, the 53132A, uh which I don't have here, so I can't demonstrate it, but it is basically exactly I think it's the only major difference between them, but I don't know, leave it in the comments down below if it's not.

**Dave Jones:** Uh but the major difference between the 132A and the 131A that I've got here is that the 132A is 100 times faster at updating. So with the 12 digits here, instead of taking 10 seconds, it would only take 0.1 seconds.

**Dave Jones:** So with that 0.1 second gate time, you actually get the full 12 digits here. So this one's slower, but it's still just as capable. It just takes longer to actually uh get the measurement.

**Dave Jones:** So if you're hunting for one of these used on eBay, try and get the 132A, but I haven't looked at um used prices for these. I don't know how much of a premium there is for the 132 over the 131, but get the 132 if you can.

**Dave Jones:** But apart from that, I believe they're absolutely identical. Both have the 12-digit display and both of them are actually capable of 15 digits. So let's change the gate time back to once per second, and I'll show you how we can actually uh get increased uh resolution on this thing.

**Dave Jones:** You can see on the back here, we've got our regular uh external input. It's got the 10 MHz frequency output. I've done an ovenized um upgrade for this. I'll link in that video if you haven't seen it, where I installed a uh oven-based oscillator.

**Dave Jones:** And it's got a well, a GPIB and an RS-232 output. So so I've connected that RS232 to an old school laptop here, which actually has an RS232 input. Yes, running Windows XP.

**Dave Jones:** All the fanboys go wild. Um anyway, um and what we can do here, okay, you can see that nothing's coming out at the moment. I've set it to 9600 bits per second 8N1 standard, okay, but nothing's coming out.

**Dave Jones:** What we need to do is go into save and print here and hit that again and turn print on. If we turn print on like that, you'll notice, bingo, it's started to spit out exactly what's on the screen there.

**Dave Jones:** It spits out our measurement. And of course, if we uh run uh stop this like we've got it in run mode, for example, if we just do single shot like that, um then we can just take it'll just sit there and then we take a single shot and we'll get another one popped up in within that 1 second uh after that 1 second gate time.

**Dave Jones:** As you can see, we get the exact same uh digits as what we get on the screen. But not only can we do uh like set a gate time, we can actually choose different modes, right?

**Dave Jones:** So, we can get our gate time like that, but we can actually go well, auto like that. So, we're actually in auto mode at the moment. It's spitting it out super quick, but we only get a few digits there.

**Dave Jones:** And if we go back here, we'll see it here, right? We only get a few digits in auto mode. If we go back into gate, we can choose external and we can choose digits.

**Dave Jones:** And if we actually choose digits like this, okay, we can actually choose how many digits we want. Five digits? We want Do we want six digits? Boom. Look at that.

**Dave Jones:** Changes it over there. Seven digits? You guessed it, right? We can go back to our 10 digits, but it's it's really no difference between actually choosing a manual gate time.

**Dave Jones:** But anyway, I won't go into the details of that. But anyway, we can set the number of digits and we can actually go all the way up to 15.

**Dave Jones:** But if we set it to 10 digits here, you can see it's actually 11 digits. It's basically giving us 10 decimal places there for this 10 megahertz. So, yeah, count it there yourself, right?

**Dave Jones:** And we're getting that gate time. We're only updating like once per second. But as I said, if you had the 132A, it'd be 100 times quicker. So, it's going to be a bit tedious in this video to show this.

**Dave Jones:** But if we go up to 11 digits and we wait, I'm now going to have to wait 100 seconds before we actually get another read out here, unfortunately. But this will actually give us an extra digit, an extra decimal place that we could not see on the display.

**Dave Jones:** And I won't bore you with details. I'll come back in 100 seconds. But the unfortunate thing about setting the the number of digits like that is it's actually taken longer.

**Dave Jones:** It's actually taken 100 seconds instead of 10 seconds to actually get to our 12 digits here. You can see that. So, it was better to set the gate time.

**Dave Jones:** So, if I go into gate time and I set that for 100 seconds. Boom. I won't bore you with the details, but let's go into 100 seconds. And bingo, what do we have here?

**Dave Jones:** We have an extra digit. Look at this. And you can see that it's actually rounded that 0.5 there to the one on the display. But it's giving us an extra digit.

**Dave Jones:** And we can actually go all the way to 15 digits on this thing. So, yeah, it's unfortunately. I wish I had the 132A cuz I could show you this uh, real faster.

**Dave Jones:** But if I keep increasing the gate time on this thing, I'm going to get, uh, extra digits out of this right up to 15, uh, the maximum this thing is capable of.

**Dave Jones:** It's a really high, um, precision unit. It's capable of really high resolution. Um, it just takes, you know, a fair amount of time on this model. It's 100 times faster on the 132, but, um, anyway, yeah, there's no reason why I can't just, uh, make a little project that takes the RS232 serial output or the actual digital, you don't want to deconvert RS232, you tap tap inside this thing, um, before it gets to

**Dave Jones:** the actual RS232 level, uh, converter, and get that serial data, read that into a little micro, and then output the extra digits onto an extra little three-digit display that we're going to put in there.

**Dave Jones:** I thought that'd be a real cool little project. So, let's take a look at if we can actually find a tiny little three-digit display to fit in here. Not sure if it's going to be easy to see this, but, oh, yeah, yeah, there we go.

**Dave Jones:** Three Turn if I overexpose the crap out of this thing, then you can see that, well, hopefully. Anyway, um, I've I've eyeballed this, and it looks like I have 15 mm available from the end of that display in there.

**Dave Jones:** You'll have to see the teardown, um, to actually see this, and the end of this window here. So, I've actually got 15 mm to play with there in that window, and if you've seen the teardown, uh, I'll put up a photo here, screenshot, uh, cuz I won't tear it down again right now, um, and you can see that I'll be able to actually fit a little tiny, um, three-digit display

**Dave Jones:** next to this, and it should come through the window here, and it'd be cool if I could get it in blue, but that's a hard ask, but, hey, let's take a look.

**Dave Jones:** All right, I've had this running overnight set to, uh, 15 digit resolution, not the gate time, so guaranteed to give us 15 digits, and what do you know? Look at this.

**Dave Jones:** Let's look at the last digits there of the last one, 3162. If we go over here, three. So, we 162. We've got three extra digits, whole three extra digits.

**Dave Jones:** So, if we had a nice little display on there, we could actually uh display those. But, um I just actually I just thought of something. Because this is doing rounding on here.

**Dave Jones:** I mean, it's not doing it at the moment, but if that was uh 396, for example, if that was 396, then um this would actually display four. And then get the extra digits.

**Dave Jones:** So, Oh, damn. Um Oh. I think that's just scuttled the entire project. Unless we actually tapped into that you would have to tap into that last digit. Oh. It just dawned on me.

**Dave Jones:** D'oh. Um that's I I mean, it's fixable, but I would have to completely and utterly tap into that last digit. And then, um if you didn't have print mode on, then that last digit wouldn't work at all.

**Dave Jones:** So, it's kind like oh uh oh, I might just upload this to the second channel. And that LED replacement display in there, I don't believe that's open source. Um so, it's not like I can just like get the files for it and then just modify the board and then like So, the guy who makes this um LED replacement board, which you need to have in order to get the space to put

**Dave Jones:** the three digits in there. Uh Uh I didn't think this one through before I pressed record, did I? I guess in theory I could actually like blank that digit there if if and only if the software the little software in the micro detected if it was going to actually round that up cuz I think earlier on in the video I cuz I just remembered that we did actually see it

**Dave Jones:** round up. So yeah. So only if it knew it was going to round up it could blank that one and then shift it and show the extra three digits which would actually only be an extra two digits because that one would be blank and then you So you only get the 15 digits if it's not rounded up.

**Dave Jones:** Otherwise it'd be 14 digits extra. You only get the two digits extra. So that's possible I guess but uh now it's just getting It's getting a bit silly. Catch you next time.
