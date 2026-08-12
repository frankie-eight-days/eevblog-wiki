---
video_id: qE-SwtYQM6E
title: Tektronix 2 Series Oscilloscope Pattern Generator
url: https://www.youtube.com/watch?v=qE-SwtYQM6E
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 30, "3": 48, "4": 61, "5": 80, "6": 96, "7": 108, "8": 124, "9": 138, "10": 157, "11": 173, "12": 186, "13": 200, "14": 221, "15": 234, "16": 247, "17": 260, "18": 273, "19": 285, "20": 300, "21": 311, "22": 326, "23": 340, "24": 355, "25": 373, "26": 392, "27": 401, "28": 413, "29": 431, "30": 451, "31": 468, "32": 486, "33": 499, "34": 514, "35": 528, "36": 540, "37": 557, "38": 573, "39": 589, "40": 605, "41": 617, "42": 631, "43": 645, "44": 656, "45": 670, "46": 687, "47": 701, "48": 716, "49": 731, "50": 745, "51": 763, "52": 783, "53": 799, "54": 817, "55": 836, "56": 852, "57": 867}
---

**Dave Jones:** Hi, just a quick follow-up video on the Tektronix 2 Series scope. They finally sent me some new firmware which enables the digital Oh, there we go. Firmware's upgraded. The digital pattern generator and also the digital inputs on the

**Dave Jones:** analog inputs apparently. So, wait. There we go. This is much better firmware upgrade process than what was previously. I think when I first did it it was I still had beta firmware and it didn't even have a splash screen or anything. So,

**Dave Jones:** the splash screen was very nice. So, apparently I've now got the capability to generate a serial pattern from a CSV file which you can presumably put on your USB stick. So, that's really cool. So, I'm going to check it out. Let's go. No, I

**Dave Jones:** do not wish to connect my interwebs to the scope just yet. So, we'll cancel that. So, now let's try and see where this will be. I'll hit the digital button there. It must say features not not enabled. To enable you must

**Dave Jones:** purchase. I thought they said it would be enabled. That's rather annoying. Okay, so let's go into utility over here. Let's go into Maybe we can get a demo. Maybe we can get a serial bus demo. They did give me an RS232 CSV file.

**Dave Jones:** So, maybe we can try that. Oh, that's just going to No, that's just going to do all that internally. Unfortunately, no, we don't want that. It's cool, but but no. Aha, here it is down here. AFG and PG

**Dave Jones:** now. So, we've got pattern generator. So, we've got the arbitrary waveform generator and our pattern generator. There you go. And we've of course we've got the the four bits on here. So, those top four pins, they'd be ground there

**Dave Jones:** and the four channel pattern gen which is a very handy feature by the way. If it Let's see what it can it do continuous and burst as well. So you could have like burst packets presumably. What is the board rate go up

**Dave Jones:** to? Do we Can we Is there any what's what's what's the limit? Come on. The velocity control could be better on this. I expected I expected better. Oh, we're going over a meg. Oh, there we go. There we go. We're

**Dave Jones:** getting some velocity now. Wow. 4 5 meg. That's handy. Come on. You can do it. 10. 8 25 25 megabits per second. Nice. Now I just had a look at the Excel file the demo that they gave me and I'll put it

**Dave Jones:** up here and it literally is just the four columns with the pattern generator information. So like there's no scripting or anything else. It's like you can have just an Excel file. So it's really easy to do. Any dummy can do it

**Dave Jones:** but it doesn't seem to have any more like it'd be nice if they had some sort of like scripting ability to sort of like generate you know like a compiler kind of thing to generate patterns. Anyway, we can choose the file

**Dave Jones:** here. Can we choose the USB stick? Okay, so I should be able to select file. No. Have to do load. Going to do load. Plug my stick in. See if it or maybe I had to do that before.

**Dave Jones:** No, there we go. It's detected E drive. Ta-da. CSV file. Awesome. And now I load. Do I? Is it loaded? That's a bit That That user interface is a little bit convoluted. What? Can Is it loaded or not?

**Dave Jones:** I'M NOT SO I ASSUME it's loaded. Okay, that's just I I don't know. Do you think that's how it should work? I I just think that's a bit weird. Anyway, there you go. Yeah, 5 volts, whatever, 25 megabits

**Dave Jones:** per second. Um let's just go continuous. Just see what it generates. So, I can like drag that down the bottom or something. And uh helps have a probe. Yeah, the glare on this screen isn't great, is it? Um

**Dave Jones:** It's Yeah, bloody gloss screens. Really annoying, but uh I like you can get like matte overlays. I do actually have one. It's down in the dungeon. I have to see if it fits actually fits this screen actually. Um bought it for another

**Dave Jones:** scope, but it might fit in this one. Um I can't figure out how to turn the uh demo off. Like I can turn the display off like that, but it doesn't I just want to like kill it. I'm not sure what

**Dave Jones:** the deal is there. Anyway, it does seem to be set to RS-232 trigger now. Um so, that's a good thing. But uh anyway, so yeah, I could have just selected that anyway. If you're you know, this is your

**Dave Jones:** regular edge triggering, you would select bus. And of course, you would select RS-232 is the only one. Um and you want to start uh on trigger, so okay. And the bus we actually want No, we do actually want the bus on. This is

**Dave Jones:** how we'd actually do it. Like we could just use it in normal scope mode, of course. In fact, I might do that if I can figure out how to get rid of this thing. Aha, I forgot how to use it. Delete bus

**Dave Jones:** one. There it is. Just hold down. And wish to delete it. Yes, I do wish to delete it. Um and I'm currently Wait, I don't want waveform view anymore. Why is that still there? Ah, bugger it. I'm getting desperate.

**Dave Jones:** I'll hit the auto set button. This is what happens when you're not familiar. Well, there we go. Um that is uh not looking like a square wave to me. Oh, duh. That explains it. Times one scope probe. There you go. Oh, there's

**Dave Jones:** your problem. I've done a video on that with the um times one um scope probes and uh how they have a lower bandwidth Uh oh. oh my levels way off now. Hang on I put I push position center.

**Dave Jones:** Why doesn't it center? Push to center. Why is it not doing that? Um what's going on here? But I I should be able Look, it goes down to the bottom. Why is it not centering? That's weird. Sorry, I don't use this

**Dave Jones:** scope on a daily basis. But Come on. Center. Oh, what? I mean it's got the center position marker up here at 21.95 volts. What's going on? All right, I I must be really really dumb. Yeah, there's my ground level.

**Dave Jones:** Okay? So it's not like it has some huge offset voltage or something. Let's auto set that again.

**Dave Jones:** There we go. It's auto set. So what the what what was the deal there? Okay, it works now. It works fine. I I got no idea what that was. If if you got any idea, leave it in the

**Dave Jones:** comments, but there you go. There's our waveform. That doesn't seem to be RS232E to me. Oh, I've got the wrong channel. I got the wrong channel. Looking at the XL file, yep, it does that. I the XL file is specifying 10101010.

**Dave Jones:** And channel four, there we go. So that was just a like a clock essentially working as a clock output. Yeah, but there is our RS232. And we should be able to decode that. But unfortunately, I don't have the digital license. They

**Dave Jones:** said I did on this scope, but it looks like I don't. Yeah, there you go. Firmware base firmware perpetual license ultimate bundle includes source and serial options. Aha, I found that I do have the license for the using the

**Dave Jones:** analog input. I was going to use the digital probe with the thing which is the 6316. But yeah, you need the digital license for that, but you don't if you using the analog input. You don't need that specific license. So anyway, so I can

**Dave Jones:** turn on the bus here and I can select RS 232. You got spy and you got I squared C and LIN and all sorts of the CAN bus and all sorts of things there. And its maximum data rate is 15 megabits

**Dave Jones:** per second. So I've had to lower the data rate to 15 megabits per second on the pattern generator. No worries. One annoying little thing. I wonder why it didn't work and then I discovered that the threshold was 0 volts by default. So

**Dave Jones:** I yeah, no. Why can't you set that by default to like one division of what your current scale is or something like that. Anyway, there you go. Decode format. You can see that it's decoded hex here. I don't want that. I want

**Dave Jones:** ASCII so that we can read it. But those who Oh, it's done that in real time. It's done that in real time. Hang on. Hang on. We've got dot dot dot. Hang on. I'll single shot capture that. I'll burst

**Dave Jones:** that puppy again and why is it showing dot? Yeah, it's getting S for the stop bit there. One cool feature here is that the custom baud rate here it it readjusts this in real time. So I can actually like I've captured the

**Dave Jones:** waveform, right? But the display will change and update. So if I go outside of the timing threshold, there you go. You saw the data update there. So it's updating each time. It's resampling. Then when it gets out of

**Dave Jones:** tolerance for the baud rate, it whoa whoa starts to change a bit and then it goes all wonky. There you go. That's pretty neat. And bingo, I've turned on my event table here and you can see EE Vblog. There it is there. I

**Dave Jones:** can, you know, single shot capture that and trust me, yeah, that is EE Vblog. I can drag that window down. Yep, there we go. EE Vblog EE Vblog EE Vblog. Um because it's easier to use the event table when you've got like a long bit of

**Dave Jones:** data like this cuz they're not displaying. Like I can change the horizontal and of course the text the ASCII text actually turns up in there, but I don't like like when you go to a smaller scale like this one that's not

**Dave Jones:** that small. You could have changed the font and like put it above. Like you could have a a smaller font and put it above like that cuz there's just, you know, there's plenty of room in there to actually put, you know, the ASCII you

**Dave Jones:** know, even at that scale there's enough room to put the characters above there. So I just wish they did that rather than, you know, you have to actually, you know, zoom into a certain level and, you know, like that and then, you know,

**Dave Jones:** they've got this nice big bold font in there which is absolutely fantastic, but, you know, then when you zoom out you've just you've just lost it and you have to have your event table up. I don't know. Just a small thing, but

**Dave Jones:** anyway, there you go. It works. Cool bananas. Um and yeah, I did confirm that it looks like I don't have the MSO license installed. They thought I did, but I don't. So I can't use the Logic Pro, but yeah, I can use the analog

**Dave Jones:** input sources no problems whatsoever. So there you go. They've added this capability of the pattern gen up to 25 megabits per second, which is really nice and the arbitrary function gen I think isn't it up to 50 meg? I think. It

**Dave Jones:** can go up to well, let's go that 50 meg. Can we go to 50 meg? Yes, we can. Look at that, but we can't No, I think I think that's the limit, is it? There we go. No, 50 meg maximum. So, you

**Dave Jones:** know, really nice capable function gen. Now, nice capable four channel pattern gen. Very handy to be able to actually just you know, put ones and zeros in onto into a CSV part file, put into a USB stick, and Bob's your uncle. You can

**Dave Jones:** output test patterns for you know, you can sim emulate anything really. So, that's really quite neat. I like that. So, they did promise us to do this when they released the scope. So, it's been released for quite some time now, but they did actually

**Dave Jones:** they they came through on their promise and the pattern gen seems to work. I'm going to try this again at the full speed actually. So, if I go into the pattern gen and bit rate What was it? 25 meg and let's go into

**Dave Jones:** the bus down here and 25 also. 25 meg enter Okay. Oh, no, 15 meg. That's right. So, the analog bus decoding lags behind what the pattern gen can do, but of course if you use the digital input it would be

**Dave Jones:** much faster. It's just the analog capability there. So, I can change that to 15 meg and let's see if we can repeat that. Can we? Whoop. Whoop. Whoop. Whoop. Whoop. It's not working now. I've got a signal integrity issue. There

**Dave Jones:** you go. Works at 1 meg. Doesn't seem to be working on the extremes. Let's try 10 meg. No, it's not working at 10 meg either. So, yeah, that could be a signal integrity thing. Oh, oh, there we go. I just lost my uh

**Dave Jones:** table. Single shot capture. No, see it it looks pretty good. I got you know, that should that should do the business, I would have thought. Um a 5 meg maybe? Okay, it looks like we're good on EV blog there. Yep, okay. So, for somewhere

**Dave Jones:** between 5 and 10 meg, it seems to crap itself. So, I don't know why. Um the waveform integrity looks pretty good. So, I don't know, is that some sort of software limitation or something maybe? I don't know. Um tech might want to get

**Dave Jones:** back to me on that one. Anyway, that is a very cool feature and what There we go, we got our table back. There we go, EV blog. Nice. Yeah, pattern gen, very handy capability. I you know, you'll probably see more and more scopes

**Dave Jones:** getting a pattern gen. Like, you know, the older Rohde & Schwarz ones have them, but I like the ability of this just to you know, a CSV file and just four columns of ones and zeros. Great stuff. Anyway, catch

**Dave Jones:** you next time.
