---
video_id: orYJFKQDZLo
title: EEVblog #540 - HP35670A DSA Repair - Part 3
url: https://www.youtube.com/watch?v=orYJFKQDZLo
source: youtube-asr
---

**Dave Jones:** Hi, part three in the HP 35670A DSA repair. Previous two videos will be linked down below if you haven't seen them. Last time we finally found that there were three failed negative voltage regulators in this thing and it still

**Dave Jones:** didn't work. We're getting that ADC gateway error message ADC ASIC on this thing and no, it's most likely as I said before not the ADC ASIC chip itself. It's I think it's like more likely to be something else surrounding the circuitry

**Dave Jones:** in there. So yeah, we're going to have a read of the service manual and poke around at the block diagram see if there's some other stuff we can measure some reference voltages or other things and see what we can come up with and track

**Dave Jones:** it down hopefully. Now I've had a look at the service manual for this thing and that ADC gateway error message is actually measured in there and it basically has to do with the source output on this thing. So this output source here and

**Dave Jones:** what I've done is I've actually measured that. It tells you some you know, basically turn the source on but I did this in the previous video and I was getting nothing out of it. And that's basically what it's telling

**Dave Jones:** you to do and it says well, if that source fails, there's a test point just there just to eliminate that it's the actually the coax not at fault but it's giving me like you know, a fixed like 5

**Dave Jones:** volts output. There's a test point there and if that test point is still faulty not giving your source output signal, then you're going to get your ADC gateway error message presumably anyway and then what does it say? It just says well, this board which is

**Dave Jones:** the A6 board is faulty. It doesn't tell you anything else. It's just like well, sorry faulty board go and replace the board. You know, because we can't get the schematics for this thing and uh nobody's been able to dig up the

**Dave Jones:** schematics anyway. So, the service manual just tells you, you know, eh, that's it. That's the faulty board. So, that's all the service manual get you down to is a board level uh type thing at this sort of stage. So, there's our

**Dave Jones:** source output down there. And uh I don't know, you know, there's nothing obvious around there. So, that ADC uh gate array test, when you actually run that, obviously it's turning on the source signal. And this thing has lots of uh

**Dave Jones:** routing built in so that the source signal can actually switch through to the ADC and it can measure all sorts of stuff. So, as I said, it's most likely not the uh ADC ASIC or uh the ADC failing. It's most likely the source.

**Dave Jones:** Well, we know the source is failing. So, really um that's where we need to have a look. And here's the block diagram for the A5 board. I think I may have mistakenly said A6 before. It's actually the A5 is the analog board. The A6 is

**Dave Jones:** the digital one above it. So, this is the board that it's uh basically telling us is faulty uh with the ADC uh gate array. Presumably, that's it. It doesn't say it. It just says ADC controller, but presumably that's the big uh Actel uh

**Dave Jones:** FPGA uh PLCC chip on there. And uh something in here is uh giving us a problem. Maybe. I mean, here's it Here's all our power supplies, which we fixed last time. You remember we had that uh negative uh five and negative 15 issues,

**Dave Jones:** but they've been fixed. But it could have taken out something else. And what I see here, this looks interesting. Here we go. voltage reference used as the reference for the ADC circuits and two test points. So, let's get in there, measure that. That's

**Dave Jones:** always the first thing. If you can get in there and measure any sort of voltages, reference voltages, power supply voltages, uh you know, DC quiescent voltages or something like that, you should definitely get in there and measure them as a first pass. So,

**Dave Jones:** there you go. Let's have a look at those and I think I can see those on the board here. There they are. Let's give those a whirl. And there's our first one there, -6.5. It's supposed to be as well it's marked

**Dave Jones:** as 6.2, but we've seen this uh before in the previous video where it wasn't as per uh set. I mean, it's suspiciously close to spot-on 6.5. So, uh you know, the exact value may not actually matter the fact that it's

**Dave Jones:** um you know, set to something or they you know, the firmware could have changed or they could have offset it in software or whatever, but 6.5 I'm not going to worry about that at this stage. So, let's measure So, the negative reference is

**Dave Jones:** okay. Positive one. Hello. 3.7 and bouncing around. Well, the whole idea of a voltage reference for an ADC is that it's supposed to be stable is the number one requirement, not necessarily accurate, but stable and that's jumping around like a

**Dave Jones:** jack-in-the-box. So, something has failed. Let's check it out. Now, this is where a schematic would uh come in pretty darn handy. I mean, I have no idea of the layout of this. I mean, here's the uh -6.2 which uh we think is uh fine. Well,

**Dave Jones:** let's just assume it's fine anyway, it's at least stable. So, I'm happy with that, but that +6.2 is the problem there. Now, there's a National Semiconductor chip here, but it looks like it's got one of those pain-in-the-ass HP part numbers on it.

**Dave Jones:** There's an LF uh 356 op amp over here and that looks like maybe it could be involved in uh the uh certainly could be involved in part of the uh offset uh part of the reference uh circuitry there. There's a 4053

**Dave Jones:** analog switch. There's that Raytheon uh chip I was telling you about last time. No idea what that sucker's doing at all, but uh Oh, yeah, we've got to at least track down that part number. I mean, there's nothing

**Dave Jones:** obviously blown around here. There's a couple of diodes here I could maybe check, but yeah, I mean, just there's nothing obvious. So, what do you do? And a couple of seconds on Google brought up a cross-reference for that HP

**Dave Jones:** part number 18260962. It's actually an LF 412 dual low-noise JFET op-amp. So, I don't know. Has that been taken out by our power supply failure plus minus 15 volts? Certainly could have been. Actually, there's something funny going on here. I just realized that I was

**Dave Jones:** measuring the wrong when I had the wires hanging out measuring the wrong one. If I actually probe the negative, well, according to the silk screen, -6.2 volt one, then I'm getting that positive value that we have before. And if I hand

**Dave Jones:** probe the positive 6.2 volt reference, we're getting that minus 6.5. So, it's complete opposite polarity to what's showing on the silk screen. Unbelievable. And it says TP413 is negative. Yep. So, the silk screen matches up to what's on the block

**Dave Jones:** diagram here. So, jeez, I don't know what's going on there at all. You can see how important these voltage reference rails are there. If you have a look at that internal layer, see that dark trace going down there and

**Dave Jones:** flowing through there, through there, probably down into this DAC over here, along there, all up into here, all up into all of these op-amps for all of the channels. And that'll be going all over this shop, all over here. So, these plus

**Dave Jones:** minus references, of course, nothing is going to work at all unless we get these references going. But but how do we go about fixing it? Well, there's no obvious signs of fire. There's no like voltage like a uh you know, voltage reference chip

**Dave Jones:** anywhere here that I can uh see anyway, not around this part. So, um I'm not sure what's uh going on there. But, anyway, um you know, the LF 412 we've got here has basic um you know, high voltage op amps

**Dave Jones:** got like absolute maximum rating plus minus 18 volts, you know. So, if you've got to think, well, if this one failed, then pretty much every other op amp with a similar rating could have failed as well. And they're all over the

**Dave Jones:** shop. Look at them. Just, you know, dozens and dozens of op amps spread all over not only this board, but the other board. So, if the power supply failure did take out this op amp, well, what else has it taken out? But, I guess

**Dave Jones:** there's only one way to find out uh really. I can't do anything else around here without a schematic. We're just uh flying blind. Really, it's probably worth uh sucking that out and uh and putting a a socket in there and putting

**Dave Jones:** in another chip. I don't think I have an LF uh 412 lying around, but another op amp. Uh it'll at least uh test to see if that's an issue. Anyway, there is one thing we'll just do as a matter of

**Dave Jones:** course. We'll just uh take this PLCC chip out and I've got one of these uh PLCC extractors here. If you don't have them, you can get a screwdriver in there and a little flat blade screwdriver in each side and gently lever it up.

**Dave Jones:** Alternate between the two sides like that. But, hey, we've got the right tool for the job here. And we'll push in there.

**Dave Jones:** Grab this sucker and it's out. Then, what you want to do is just get in there and uh just have a look around. Make sure there's no uh corrosion or growth or anything like that, oxidization on the on the pins. They all look uh pretty

**Dave Jones:** good. You put, you know, if you're really fussy you could put some contact cleaner on that uh sucker just for just for kicks, but no, that looks pretty good to me. And physically, the chip near pin one has a little notch in

**Dave Jones:** it and it won't even let you install that the wrong way. So, here's the Here's a little cutout in the socket and it allows us now to fit that in. And you just push down like that and Bob's your uncle. Make sure it's seated

**Dave Jones:** really well. Well, I replaced the op amp. I didn't have an LF 412, but I did have something even better, an AD712, which is, according to the data sheet, an enhanced replacement for the LF412. But I still get, unfortunately, on the

**Dave Jones:** screen the ADC gate array uh error message. So, let's check the test points. That's says the negative on the silk screen, but that's positive 6.5. And negative 6.5 on the test point. So, it looks like we fixed the problem. So, it

**Dave Jones:** looks like that op amp did actually fail, which is rather disturbing because that means if one op amp on the plus minus 15-V rail can fail, yeah, what about the other 30 or something that are on there? And the source output ain't working

**Dave Jones:** either. That's supposed to be 10 kHz at 1 V RMS and we're just getting No, what is it? Oh, actually, um 15 V. There you go, full scale output. So, we've fixed our reference voltages, but we haven't fixed anything

**Dave Jones:** else. I mean, our source still isn't working and we've still got, of course, the over range on channel one and channel two hasn't fixed that, but as I said, I think those are dedicated circuitry uh, for those work independent of that

**Dave Jones:** uh, reference voltage or the analog well, at least the analog-to-digital uh, converter anyway. So, uh, jeez, it's not looking good. So, without a schematic, what do you do? You'd be chasing your tail until the cows come home. I mean, it's not like we're

**Dave Jones:** getting like a classic uh, short inside one of the op amps or something like that and it's drawing excess current and then we'd be able to narrow it down and we'd be able to find any culprits and take them out and stuff like that. No,

**Dave Jones:** it's drawing what seems to be typical power consumption, so we can't go around and find which ones have failed and just on this board, there's probably, you know, 1 2 3 4 5 6 7 8 9 10 11 12,

**Dave Jones:** there's like 15. I don't know, 15 or 16 or more op amps just in here and and then we've got lots of things like uh, ADG switches in here, multi-way and then there's 4000 series switches and there's all sorts of stuff and probably all of

**Dave Jones:** it is running on that plus uh, minus 15-V rail and we definitely know that uh, we've we've found at least one faulty IC on that 15-V rail. I mean, there could be I don't I don't know, right? There could only be like one more

**Dave Jones:** or something like or one other thing, you know, I could be one step away from fixing this thing. Uh, unfortunately, that's where it uh, falls out from underneath your feet because well, Murphy'll get you every time. You just don't know

**Dave Jones:** where to go now. It'd be uh, it'd be a bit easier if I had a schematic. I mean, if I had a schematic, you know, I'd start by looking around another known failure mode, which is the source output

**Dave Jones:** is uh, not working cuz we're getting nothing out of our TP8. There's a um, LP uh, 63 uh, sorry, um, LM 6321 uh, driver buffer there to drive the output, a couple of um, A NE5534s in there and all that. We've got looks

**Dave Jones:** like we've got a analog devices DAC up there and you know a whole bunch of other stuff. So maybe you'd you know, start be Sorry, you didn't see that up there. The analog devices DAC around there, you know, you start be looking around all

**Dave Jones:** this source part of it, but you know, without a schematic, I don't know. I don't start want to be going you know, sucking and seeing if things work. That's ah You can't beat Murphy that way. But I do

**Dave Jones:** see a test point there, DAC output. So that's worth a probe at least. And there we go. That's our DAC output and I can turn the source off and on. There we go. Source off and channel one there and the green channel up the top.

**Dave Jones:** That's 15 volts. That's actually the output on the front panel B and C. So it looks like the DAC's working. I've got just random noise selected there. We can choose a periodic chirp and you can see the data changing. Pink noise. There we

**Dave Jones:** go. And fixed sign. There we go. We can see it. It's uh It's changing there. So looks like our DAC output is certainly doing something at the very least, but we're getting nothing out on our BNC connector here. And as I said

**Dave Jones:** before, when you run the ADC gate array test, it actually turns the source out source on. So let's actually have a look at that. ADC gate gate array test. There we go. And it's generating source signal and then says,

**Dave Jones:** well, you know, ADC gate array failed. Now what I'm doing is I'm actually probing a point further on past the DAC. So we've looked at the DAC. We were getting data out. This is actually labeled low pass filter or there's two

**Dave Jones:** of these. There's low pass first low pass filter and second. So looking at the first one. So we're at least getting data out of our first low pass filter, but I've got my source set to a sine wave at 1 hertz. And of course, you

**Dave Jones:** know, as we saw before that sine wave just looks like it's got a whole bunch of like, you know, you can see that the period is there, but apart from that, it's just I don't even know what that

**Dave Jones:** is. But the frequency is right cuz it's bang on 1 hertz from there to there, 200 milliseconds per division. No worries. Without a schematic, I'm just pushing brown stuff up a hill with a pointy stick, pissing up a flagpole.

**Dave Jones:** you know, what am I going to do? Start sucking out op amps and I think No, this is this is getting ridiculous. I don't know. I got to go away, have a head scratch, and hopefully someone will find a schematic

**Dave Jones:** somewhere which may help, but otherwise, this one is not looking good at all, folks. Um it could be well, not beyond economical repair, but beyond a time repair, really. I mean, to suck out everything, you know. Who knows what's

**Dave Jones:** actually at fault, but it you know, it it looks to be doing the business. Like I could solve this source output issue, right? I could find out what's going on with this source circuitry. Okay, we get our source

**Dave Jones:** working, but who's to say that's the only problem? Odds are, based on what we've seen that this op amp here definitely failed, then well, it's it's not looking good. I expect some more things to be taken out rather than just the source. So,

**Dave Jones:** mm That's it for today. Sorry, guys. Still couldn't fix it. But if you can find a schematic, please let me know. And no, it's not in the service manual. I've had quite a few people email me the service manual. Yes, I've

**Dave Jones:** got it. Thank you. It hasn't got the schematics in it, unfortunately. Catch you next time.

**Dave Jones:** Mhm.
