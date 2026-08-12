---
video_id: 11-AQ_E1fz8
title: Siglent SDS1000X-E Serial Decoding
url: https://www.youtube.com/watch?v=11-AQ_E1fz8
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 28, "3": 37, "4": 55, "5": 70, "6": 86, "7": 103, "8": 113, "9": 126, "10": 135, "11": 147, "12": 159, "13": 171, "14": 189, "15": 202, "16": 212, "17": 221, "18": 234, "19": 250, "20": 269, "21": 281, "22": 293, "23": 306, "24": 321, "25": 334}
---

**Dave Jones:** Hi, uh just a sneak peek at the new uh unreleased Siglent SDS 1202X E series. It's not available in the 1102, only comes in 200 meg, and a lot of people have asked about the serial decoding in this thing.

**Dave Jones:** So, I'll just give you a little uh sneak peek here. Now, I've actually um the great thing about the scope is that serial decoding is free. It is no optional extra, no hacking required.

**Dave Jones:** You get I squared C, SPI, UART, CAN, and LIN. I'm only going to play around with the uh UART here right now. There's uh two different uh decoders, uh one and two.

**Dave Jones:** I believe it's similar to the previous uh series Siglents, it's just included uh free. And of course, you can set up the uh signals, but unfortunately, unlike the Keysight 1000X series, you cannot use this third channel here.

**Dave Jones:** Uh so, it's not, you know, two plus one channels or two and a half channels. Um even for the SPI, for example, if you go in here into the SPI, so, you've chosen SPI, uh you know, clock clock can only be channel one or channel two, right?

**Dave Jones:** My so, channel one, channel two. So, you've only got the ability to do the uh of course, the chip select, of course, you can uh actually choose the uh a clock timeout here, so you don't actually need the third channel for the chip select.

**Dave Jones:** So, that's yeah, that's good, right? So, you can still use it as a rudimentary SPI uh analyzer, but yeah, you do not get that third channel, and no, you cannot display the external trigger like you can on the new Keysight 1000X series, um which is better in that regard.

**Dave Jones:** So, if we actually go back to UART here, I've actually got a I'm feeding in a 1 meg uh 1 megabit signal. Here it is. So, I've got custom baud rate.

**Dave Jones:** So, all of their all of the baud rates, I've got custom here. Now, ordinarily, I took me a little bit to figure this out. Um but like there's the velocity control on this thing is not the best, right?

**Dave Jones:** So, um it'll take you forever if you started from 100,000 and had to go up. The only way I was actually able to get to that is you actually press it like that.

**Dave Jones:** And the good thing is is that it actually does come up with a keyboard here. It's not touchscreen, but it's you know, it it works reasonably well. So, you can just go 1 M whoop 1 M like that.

**Dave Jones:** Uh little bit fiddly, but then it jumps to 1 meg. So, you know, that's all right. It's usable. Now, um so, it can at least do speeds up to 1 meg.

**Dave Jones:** I don't readily have anything available faster, I don't think. But anyway, so it can actually do up to 1 uh meg eight data bits um odd parity uh two stop bits and that's it that is correct.

**Dave Jones:** That's what it's supposed to display um asterisk uh IDN. Um so, that's all hunky-dory. Uh but well, there's one good thing about this is that they claim it does serial decoding on the entire memory depth, which is 14 meg and that's uh comes standard with the scope.

**Dave Jones:** But uh unfortunately, it seems to be be a bit slow. I'm in normal uh mode at the moment. Here we go. I'm in normal mode um and it's of course displaying that IDN.

**Dave Jones:** And uh but oh, well, and of course, it'll do it in single shot, you know, everything's hunky-dory, right? Um yeah, so we can like single shot like that and then go in.

**Dave Jones:** No no problems whatsoever, right? So, it's okay. You know, it's doing the business. It's not the most detailed um display I've seen. I don't think you can expand it.

**Dave Jones:** I don't think you can actually make it bigger. So, it's a little bit you know, squinty to actually read the font on there, but uh anyway, uh Uh, normal mode, you know, it's doing the business, but look what happens when you go into auto mode.

**Dave Jones:** It's there, right? So, you're seeing the waveform, but it's not Well, you saw it. It'll occasionally pop up like that. So, it's they claim to have real-time decoding in the zinc FPGA hardware in this thing.

**Dave Jones:** Uh, well, they claim I think they claim. Uh, I have to double-check. Uh, hardware decoding, but look, I mean, you know, you're seeing it on the screen. Obviously, it's not triggering uh, properly cuz we haven't set off, you know, the whole time or whatever um, for this thing to Well, to be able to trigger in auto mode, but you're seeing the waveform, and it's not it's not decoding that.

**Dave Jones:** Just very occasionally will it actually pop up and do that. But, of course, if you put it in normal mode with the correct trigger, but you see, it actually took uh, like a second or something to actually decode that.

**Dave Jones:** Look, one one. It takes like a second. So, obviously, it's got to read the entire 14 meg memory, and that's great, but that takes time. So, if you're after real-time serial decoder, it's probably not going to do the business.

**Dave Jones:** So, at the moment, I've only just started playing around with this. I've only uh, tried the UART one, but yeah, it's, you know, yeah, it's And of course, you can choose the different um, uh, formats there, and you can get a uh, list as well.

**Dave Jones:** There you go. You can pop up with a list for you list uh, fan boys there, but yeah, it's There's good points and there's bad points. I mean, this is a real budget uh, scope, but at least it can do one meg uh, UART serial.

**Dave Jones:** It does decode on the full memory, but yeah, not real time. Few little user interface. Um, you know, it it it's not the most detailed, but it doesn't support the external channel, which is a real bummer, but eh, it's free.

**Dave Jones:** So, beauty. Anyway, hope you found that useful. Catch you next time.
