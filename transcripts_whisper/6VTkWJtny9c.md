---
video_id: 6VTkWJtny9c
title: EEVblog #615 - Prema 6047 Multimeter Followup
url: https://www.youtube.com/watch?v=6VTkWJtny9c
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 53, "4": 69, "5": 85, "6": 101, "7": 118, "8": 134, "9": 150, "10": 166, "11": 183, "12": 207, "13": 227, "14": 243, "15": 259, "16": 276, "17": 296, "18": 312, "19": 324, "20": 340, "21": 352, "22": 368, "23": 384, "24": 400, "25": 420, "26": 437, "27": 453, "28": 469, "29": 485, "30": 505, "31": 517, "32": 538, "33": 554, "34": 570, "35": 582, "36": 602, "37": 618, "38": 631, "39": 655, "40": 671, "41": 687, "42": 708, "43": 724, "44": 740, "45": 760, "46": 776, "47": 792, "48": 809, "49": 825, "50": 845, "51": 861, "52": 877, "53": 897, "54": 914, "55": 934, "56": 954, "57": 975, "58": 991, "59": 1007, "60": 1023}
---

**Dave Jones:** Hi. Just a quick follow-up video on this Prima 6047 classic 1989 vintage, or thereabouts, 7.5 digit precision multimeter. It's like a metrology grade one, you know, really expensive for its day, sort of top of the line. And if you haven't seen the previous video,

**Dave Jones:** the tear-down one of that and a bit of playing around, I'll link that in down below. So check it out. Now I did mention in the previous video that it was slightly, it appeared to be slightly out of calibration. I would have expected it to be better than this, especially on the DC

**Dave Jones:** volts here. And by the way, I figured out how to switch the time here. It was easy, it was this integration button here, and I can switch that down, and it actually, I can switch the number of digits there. So I can go to one second, and then curiously, look,

**Dave Jones:** it's got a nice little countdown timer in here, so it counts the number of digits. So it counts down to when the next measurement interval and does the update. Really quite neat. You can go up to 80 seconds here. Anyway, in the previous video, I mentioned it seemed to be a little bit out,

**Dave Jones:** and I suspected that might be due to the non-volatile RAM up the back here, and if that's lost its memory contents, then that is, you know, that has to be where the calibration constants are stored for this thing. Because these are electronic calibration constants.

**Dave Jones:** There's no calibration pots in here that you tweak or anything like that. The only pots in here aren't pots, they're actually trimmer caps designed for the frequency adjustment on the AC measurement range. So nothing actually to do with the calibration at all as such.

**Dave Jones:** So the calibration constants must be kept in that non-volatile, Dallas, presumably, yeah, Dallas, because they're the only ones who made it back in the day. They were state-of-the-art back in the day. We'll have a look at it. But they must be stored in there, because there's nowhere else to store it.

**Dave Jones:** We've just got an EEPROM, it's a 65C02 processor in there, absolute classic. Nothing else. Constants must be stored in there, there's an internal backup battery in there which has a nominal life of 10 years. And then you basically have to throw the chip out because you can't replace the battery

**Dave Jones:** in the thing. Now this thing, of course, is like in the order of 24, 25 years old. Now I've personally seen these Dallas non-volatile RAMs still working after 20, almost 20 years, I think is the longest I've ever seen. But you know, we're really starting to

**Dave Jones:** stretch it now. They're only guaranteed for 10 years. So really, I'm pretty sure the calibration constants in that are gone. But anyway, what we're going to do is rip that out, have a look at it, and see if it is actually blank, and see if it makes a difference actually taking it out.

**Dave Jones:** Now here's a schematic of the main processor here. And you can see there is the 65CO2. They've drawn it tiny because they've got just the parallel data buses coming in and out of it. So you don't need to show much at all. And they've got the other miscellaneous stuff

**Dave Jones:** that you find in any microprocessor solution based around a 65CO2. There's the EEPROM, there's the main SRAM, and here, U12 here, is the battery-backed Dallas real-time clock chip. And basically what it is, is it pin-for-pin compatible with a regular SRAM chip of the same size, except that it's got a built-in

**Dave Jones:** lithium primary battery in there. It's not rechargeable, it's primary. It's got a guaranteed 10-year factory life when you buy it. I think you can still buy them these days, I don't know, I haven't looked recently. But anyway, somebody in the comments previous video wanted to know how easy was it to remove?

**Dave Jones:** Can you remove these things? Well, yes you can, because once you power the thing off, okay, this is the VCC here, once you remove the power to VCC, it's got internal control circuitry that detects that, and then automatically write protects the memory. So as long as

**Dave Jones:** you guarantee that that power is off, and it's a split second later or something like that, as long as it's off, then you can pull that chip out no problem whatsoever. It doesn't matter whether the write pins float or anything like that. Now you'll notice that there is a calibration switch, this is

**Dave Jones:** on the back of the unit here. My one hasn't been fiddled with, it's still got the cow sticker over that switch. And as you can see, in the calibration protection position, which is up, it's just pulling that pin, it's pulling the not-write pin permanently high.

**Dave Jones:** So nothing can be written to that chip, so you can't overwrite, accidentally overwrite your calibration constants and other stuff, which is stored in there Presumably, on something like this, it's probably only the calibration constants, maybe they're storing like the last used mode or something like that perhaps, but there's not much else in this thing that'll be stored.

**Dave Jones:** And if you get in the back panel and flip that switch of course, then it goes down some of the gated circuitry down here, which can enable the write switch, and you can go into calibration mode via the front panel, and you can set new calibration constants

**Dave Jones:** in there and calibrate this thing. So I'm going to rip that out, and we should be able to read that as a regular SRAM. Let's see if there's anything in it. My guess is it'll be blank. And I'll just get in there and

**Dave Jones:** check the rail. I know it's dead, but you know, this is what you should do, just to be absolutely sure that there's not any residual power left on that rail. It's not, it's dead, so that chip will be thoroughly write protected with the internal circuitry.

**Dave Jones:** So I can now safely simply remove that and whack it in my EEPROM reader to check it. So I'm going to be really mean to this thing, and I'm going to power it up with no chip in there. There it is. It's gone.

**Dave Jones:** So we'll see. If it's just got the calibration constants and it was reading out garbage before and it was happy to read it out, then well, you know, everything's hunky-dory. So let's, so it should power up exactly the same as it powered up before.

**Dave Jones:** Controller 1, it goes through, it takes a few seconds, but oh no, error 8! There you go. No, it obviously writes some data to that. No. No, it writes some data to that SRAM and tries to read it back and there's nothing there.

**Dave Jones:** But hey, we could replace that with a standard SRAM if I've got one. And there's the sucker. Look at the date code. 50th week 1987. And it's supposed to have a phenomenal life of 10 years. So yeah, you can see the outline of the battery in there.

**Dave Jones:** There we go. You can see it if you get the right angle there. There's the lithium coin cell battery, like a CR, you know, 2050 or something, probably stacked up and soldered directly on there. And there's the chip poking out the bottom and fully potted of course.

**Dave Jones:** So you can't really get these things and replace the battery. So if the battery's gone, of course it's an SRAM, so if it has gone, there's no way I can recover the calibration constant out of this thing. Not a chance. And by the way, no, there is no way

**Dave Jones:** that you can measure that battery voltage on the pins. It's purely internal. So all you can do is read out the contents and presumably if the contents aren't blank, then well it's probably got the original contents. But hey, they could have been corrupted if the

**Dave Jones:** battery's marginal or something like that. So I'm going to use my little mini-pro TL866 programmer you've seen in a previous video. Really cheap, these things. Everyone should have at least one of these. I mean, it's like $30 or something. It's incredibly cheap. Now

**Dave Jones:** if we have a look at the software for this sucker, please excuse the crude screen capture here. But look, it already supports the DS1220. We've got the DS1220Y, but that's going to be close enough. I don't know what test there means, but anyway, we're going to select that.

**Dave Jones:** Otherwise we could have just selected any generic SRAM for the same size. Now I'm a bit concerned about the test part of it there. Could be like test mode, as in testing a chip. And look at this test range. Yeah, I don't like the

**Dave Jones:** sound of that. So we don't want to test it. We only want to read the contents out. That's all we want to do. Now let's say we selected one of the other ones here. And of course we could go into standard SRAM if we knew the size.

**Dave Jones:** I haven't looked up the data sheet yet. But no, these are test ranges too. So maybe if we go into standard SRAM down here, let's choose a 6116. No, it's got that test range as well. So I don't want to test a chip,

**Dave Jones:** I want to actually read it out. So here we go. If we, I was in SRAM, DRAM before, I've now gone up into ROM, flash, non-volatile RAM there, and Dallas DS220RW. So there you go, if we select that, bingo, we're not in the test menu anymore.

**Dave Jones:** So yeah, if we accidentally hit that, oops! We could have screwed our chip if it was good. We certainly don't want to do that. So now we can use the existing tools here to actually blank check and then, well no, we don't want to read from chip.

**Dave Jones:** That's what we want. So it shouldn't enable that write line, assuming there's no fault in the programmer, and we should be able to read that contents out. Anyway, there's the data sheet for the chip. Yep, it's the bog standard one back in the day, the 16K non-volatile SRAM.

**Dave Jones:** There you go, 10 years minimum data retention in the absence of external power. And well, it's, you know, if this thing was powered up for long periods of time, then it wouldn't use that, it wouldn't use the battery in there. But of course, you're basically, when you're looking at 10 years, you're talking about

**Dave Jones:** the shelf life of the lithium battery, lithium primary battery in there anyway. So even if you had the power off, it's still probably only going to last 10 years or so. But as I said, I've seen ones last almost double that, but definitely

**Dave Jones:** not guaranteed. Alright, here we go, moment of truth, let's read it in. Yeah, the whole range by default, it tells us exactly the orientation we want. Fantastic, it's all in there, I've made sure it's around the right way, and here we go. Read.

**Dave Jones:** Ta-da! Done. It's, I think it's silly that you have to cancel, but anyway, it is done. And look! We have, we have data! Woohoo, look at that! There is 80, there's lots of 80s in there, but there is all this other data. Now, just to make sure that's not just random

**Dave Jones:** gibberish, what we want to do up here is we want to go up and we want to re-verify that. So it will compare what's in the chip to what it just read in. So, yeah, verify successful, yes, and we can just run that, just run that a couple of times just to

**Dave Jones:** make sure everything's hunky-dory. And let me actually physically take the chip out and put it back in and just verify it again. Yep, so there you go. We have actually successfully read the contents of that, and it is not empty. Well, I'm actually rather surprised.

**Dave Jones:** Now, of course, we can't make heads or tails out of that, what stuff is stored in there, but it looks like it has several sort of blocks of data stored in there. So that'd be all of the calibration stuff, and maybe some other mode things or something like

**Dave Jones:** that, but yeah! Wow! Okay, after what, 24 years or something? That battery looks like it's still good. Well, it's still got something. We don't know if it's actually corrupted the data, but usually these things will go blank. So look what I've dug out of the old junk bin.

**Dave Jones:** A6116, 2k x 8 SRAM, 16k bit SRAM. Should be exactly the same pinout. Let's plug it in, see if the thing boots up without that error message. Because if I'm right, it is actually pointing to the SRAM when it boots up, and if it can't read it back

**Dave Jones:** somehow, then it knows, you know, that error 8 is saying it's an SRAM fault. Alright, here we go, I've got the SRAM installed, it's around the right way. Yep, let's power it up. Controller 1, 2, error 8, no, it's exactly the same. There you go, so maybe it's not reading the

**Dave Jones:** checksum that it expects or something like that. So maybe our original non-volatile RAM is actually good. So I don't know, we'll have to read the manual I guess, see if we can get something on error 8. Bingo, there you go, error 8, error during self-test, it compares, as I

**Dave Jones:** suspected, compares the checksum with the one in the non-volatile RAM, that Dallas chip. So obviously, for this thing to power up previously, that Dallas chip must still have the correct data in there, otherwise it would give you an error 8 every time you boot up.

**Dave Jones:** So hey, the Dallas chip has to be good. Alright, so I'll put the Dallas chip back in and we'll power this thing up again, and it's probably going to come good, exactly like it did last time. So yep, yep, everything's fine. So I,

**Dave Jones:** because it passes, that checksum is stored in that Dallas SRAM, if that battery was flat, then that checksum would be incorrect and you'd get that error 8 message every time you power up. So it must still be good. Wow, after all these years, unbelievable.

**Dave Jones:** 1987, that one is, yeah, 1987, 50th week, 87. Unbelievable. Still going. But of course if you really cared about keeping this thing going, then the first thing you would do, read the contents out of that, save it, and then try and find a

**Dave Jones:** replacement chip that you can reprogram, whack back in there. And yes, I have read in the contents of the ROM as well, that's a 27C256, just your classic type. And yes, I've got that contents and I will upload it into some repository on the net for those who

**Dave Jones:** need it in the future. Always do that with this old sort of gear. Now there's one interesting thing to note about this meter, is that even if this SRAM here does fail, then it's not a problem, because you don't lose the calibration of the instrument, because Prima

**Dave Jones:** have actually programmed the original calibration values at the factory into the EEPROM here. So the manual actually tells you how to recover if your battery fails in here. You can't get your last calibration values of course, unless they rewrite the ROM for you, but you can get the original

**Dave Jones:** factory calibration values. There's a mode, you just flick the switch on the back, you power it up, and it automatically copies the contents over to the new SRAM. Fantastic! And for those of you curious to know, if it's possible to turn the 6047 into the

**Dave Jones:** 6048, i.e. get that 8.5 digit resolution, that extra one digits, well, it might be possible to hack the thing in the ROM to actually do that. That could be a distinct possibility, because the only major difference between the 6047 and the 6048 is the LTC1000

**Dave Jones:** voltage reference. There's some circuitry difference in there, but you might it should, in theory, probably have the same software and just be limited to that 7.5 digits in the firmware for the 6047. So, I've got the ROM dump here, and as you can

**Dave Jones:** see, I've searched for Prima, I've searched for 6047, I've searched for 47, I've searched for 48, and none of it's in there. Basically, it's all just gibberish. I can't find anything, so you would have to disassemble it, disassemble the 65CO2 binary file, and to be able to

**Dave Jones:** try and find that, if there's a bit in there that gets flipped, or something like that. So, I was hoping that, yeah, it'd be as easy as, like, there'd be a string in there saying 6047, and you might change that to 6048, and then the firmware just checks that when it boots up.

**Dave Jones:** But that doesn't look to be the case. Not that easy. So, yeah, not impossible, but I thought I'd give it a shot anyway. And if you're wondering why my room sounds very echoey, here it's because I am actually recording this at home, and we're renovating the house,

**Dave Jones:** and I do actually have my sound-absorbing wall panels in here, but still there is no furniture in this room, so they don't cover the walls 100%. So, really, we're getting some pretty bad echo in here. So, there you go. Anyway, hope you enjoyed

**Dave Jones:** that quick video. Catch you next time.
