---
video_id: R2dGKcMtAvg
title: EEVblog #77 - Rigol DS1052E DS1102E Oscilloscope Hack Update
url: https://www.youtube.com/watch?v=R2dGKcMtAvg
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 38, "3": 54, "4": 70, "5": 87, "6": 106, "7": 120, "8": 140, "9": 161, "10": 182, "11": 200, "12": 242, "13": 261, "14": 276, "15": 300, "16": 319, "17": 369, "18": 391, "19": 415, "20": 432, "21": 451, "22": 480, "23": 501, "24": 517, "25": 533, "26": 563, "27": 578, "28": 595, "29": 610, "30": 625, "31": 641, "32": 658}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, just a quick update on the 100 MHz Rigol DS1052E hack. Now, I reported on the forum that

**Dave Jones:** a user has contacted me and said that they're actually there's a new version of firmware 2.04 that apparently fixes the issue about the it no longer lets you mod the scope with those simple serial commands. So, what I thought I'd do

**Dave Jones:** is actually upgrade the firmware because the user actually reported that if you do it with an earlier version of firmware, if you do the hack with an earlier version than 2.04, when you upgrade the firmware, it'll actually stick. And that if you do happen to buy

**Dave Jones:** a a new model oscilloscope with 2.04 or greater firmware, you can actually downgrade first, do the upgrade, and then re-upgrade and to 2.04 or later, and the firmware should stick. So, I thought I'd actually give it a go and see if it

**Dave Jones:** works. Okay, just before we do the upgrade, let's just check the rise and fall time here, 3.5 nanoseconds, as you can see. So, that's a 100 MHz bandwidth. Now, we'll just go in and we'll check the firmware version, system info. There it

**Dave Jones:** is. I'm currently running 2.01 SP1, and it's a DS1102E. All right, let's update the firmware and see what happens. I've got a memory stick here with 2.04 firmware on it, and plug it in and let's see what happens. Whoa, detect a

**Dave Jones:** lower version software. Upgrade or not? I don't think it's supposed to say that, so I'm not quite sure what's happening there, but oh well, I'm I'm pretty sure I've got the right files on there, so let's give it a go. Choose okay and

**Dave Jones:** this could take a while. Yep, there we go. 2.04 firmware. So, it has actually upgraded. But, um it yes, it looks like as soon as you finish the USB stick, you've just got to re-power. So, let's double-check that again.

**Dave Jones:** System info and yeah, it's still a DS1102E and I've got 2.04 firmware. There you go. But, just because the model number's there doesn't mean it is actually a 100 MHz. Let's go back and check it, shall we? Run and yep, we're still 3.5

**Dave Jones:** nanoseconds. Still 100 MHz. So, the mod does stick when you upgrade the firmware. Okay, we've got firmware 2.04 installed. Now, let's see if we can change it back. Asterisk, IDN, question mark. 010 Okay, we've got firmware 2.04. Let's see

**Dave Jones:** if we can change it. Colon info model Let's see if we can change it back to DS 1052E.

**Dave Jones:** And we'll try and change the serial number, too. Info serial DS 1BD this time. 11 0 800915 and and 010 and we'll re-power the scope and see if it's changed anything. Okay, power up the scope. And no, it's still two Well, it's still

**Dave Jones:** 2.04, but let's go in and check the serial number. System info. No, DS1102E. No, it's still the uh E Oh, yes, it did change. It allowed us to change the serial number. See, it's changed to E D, but it didn't let us change the model

**Dave Jones:** number. The model didn't stick. And as you can see, even with the changed serial number, it's still a 100 MHz scope. All right. Now, let's see if we can change the firmware back to 2.02. It's currently 2.04. I've got 2.02 on the

**Dave Jones:** memory stick. Let's plug it in. And detect a lower software version upgrade. Okay. Okay, it's done. It says update successful, please restart. So, let's restart. Disconnect the memory stick. Boot up. And we're 2.02 SP 2. So, the uh

**Dave Jones:** downgrading the firmware does actually work. Let's go into system info. There it is. It's still 1102E, and the serial number is still the D version. We've got 2.02. Okay, let's see if we can downgrade this model. Let's try it again. *IDN

**Dave Jones:** ? 010 Rigol Technologies 2.02 : INFO MODEL DS 1052E 010 And let's change the serial number as well. INFO SERIAL space DS 1 E D 110800915 010 and that should stick. And you can see I haven't re-powered this yet. It's instantly changed over to

**Dave Jones:** DS1052E. So, if you have it on that screen, it actually um changes that instantly. But, let's try and restart it.

**Dave Jones:** Okay, utility. System info, bingo. We're back to a DS1052E. Uh firmware version 2.02. So, it's confirmed that 2.02 SP2 firmware still lets you modify the model number. And of course, just to confirm that really is 50 MHz, there you go. The rise

**Dave Jones:** time is back to normal and we can only go down to 5 ns per division. So, it's definitely the 50 MHz mode. Okay, sorry. I forgot to press record here, but I have just uh changed it back, done the same procedure, DS1102E,

**Dave Jones:** and I changed the serial number back. And if you can see here, it's instantly reflected on the scope here, DS1102E. So, we're back to normal there. Let's re-power it.

**Dave Jones:** And let's see what happens here. Utility uh system info, Bingo, we're back to DS1102E and the firmware version is the serial number's changed, sorry. And let's try and probe that signal again.

**Dave Jones:** And run. And bingo, 3.5 nanoseconds, 2 nanoseconds per division. We're back to the 100 MHz model again. Okay, so we've gone from rev 2.01 to 2.04. We've shown that the firmware sticks. We've gone back to rev 2.02 showing that you can change that you can

**Dave Jones:** revert back to a previous version and that you can change the model number. And now I've got the 2.04 on the memory stick again and let's go and put our scope back to the latest version. Once again, it says lower version, so I don't know

**Dave Jones:** what's going on there, but anyway, it's definitely 2.04. Choose okay and here we go. Okay, there it is. I must have missed that message last time. Up data succeeded. A bit of Chinglish there. Please restart. So, let's restart it, take out the

**Dave Jones:** memory stick and bingo, 2.04. And utility. Let's go in. System info, it's stuck again, DS1102E. So, the mod has stuck, 2.04 and let's measure that signal one more time just to make sure we do really have 100 MHz bandwidth.

**Dave Jones:** And yes, we do. There we go, 3 nanoseconds rise and fall time and the time base goes down to 2 nanoseconds. Perfect. So, there you go. That goes to show that you can, even if you got the new

**Dave Jones:** firmware, you can downgrade the firmware to the old one, at least 2.02 SP2 or lower, and you can do the mod, and then you can re-upgrade the firmware to at least 2.04. I can't guarantee that's going to work on future versions, but

**Dave Jones:** 2.04 works, and the mod sticks. So, even if you get a new firmware one from Rigol, you should be able to downgrade it. Now, that doesn't mean Rigol are going to fix this hole again in the future. Who knows? But, it certainly

**Dave Jones:** works for 2.04, that's for sure. So, there's not a problem at all. Now, there was actually 2.04 hasn't actually been seen in the field yet, at least I've got no reports of it. But, Rigol have been giving 2.04

**Dave Jones:** to various customers. Anyway, so they have There's reports that they have actually stopped stopped distributing the scope for a little bit until they could upgrade the firmware in all the units. And there were actually reports that Rigol have

**Dave Jones:** known about this for a long time, way before it was done on this blog. Apparently, some people in in China knew about the the hack and were actually doing it well before then. So, Rigol have have known about it for quite

**Dave Jones:** some time, but they haven't really done much about it until it gained popularity. But, yeah, it still works. There you go. You can downgrade the firmware, make the mod. Easy.
