---
video_id: VTAwzrKPjeE
title: Nixie Tube Display ESP8266 Wemos D1 Mini Testing
url: https://www.youtube.com/watch?v=VTAwzrKPjeE
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 23, "2": 46, "3": 64, "4": 77, "5": 91, "6": 111, "7": 128, "8": 155, "9": 177, "10": 190, "11": 219, "12": 233, "13": 250, "14": 270, "15": 293, "16": 322, "17": 337, "18": 352, "19": 370, "20": 393, "21": 404, "22": 417, "23": 435, "24": 456, "25": 481, "26": 497, "27": 513, "28": 533, "29": 549, "30": 566, "31": 592, "32": 617, "33": 639, "34": 669, "35": 691, "36": 720, "37": 735, "38": 765, "39": 782, "40": 804, "41": 821, "42": 825, "43": 825, "44": 850, "45": 869, "46": 883, "47": 901, "48": 920, "49": 937, "50": 961, "51": 983, "52": 1004, "53": 1023, "54": 1041, "55": 1063, "56": 1081}
---

**Dave Jones:** Hi, just a second channel video. I'm just playing around with, or about to play around with, hang on, can I even get it there? In the shot, my Wemos D1 Mini thing. Anyway, I've got it hooked up to my logic analyzer here and I thought I'd just try it

**Dave Jones:** because I've written some code to do the things, hook it up to the logic analyzer, make sure that it's outputting exactly, like outputting data before I go actually plug it into my Nixie tube board, which is here. So, yeah, I, you know, it's just worthwhile just checking that before you go plug it in here

**Dave Jones:** and then you've got a bigger systems engineering problem. Well, is there something wrong? Did I goof up the footprint? Did I do? Whatever, wrong before you, you know, or is it my code, for example? So, you've got more than one unknown. So, it's always good to just tackle the one unknown at the time.

**Dave Jones:** And the first unknown is I have not written code for the Wemos D1 Mini before. So, I don't know if my code's going to work and I'm writing to the right pins and there's actually data toggling and stuff like that. So, that's what I thought I'd do here.

**Dave Jones:** My webcam thing seems a bit laggy lately. I haven't solved it. Well, I haven't looked into it. It never used to do this and I don't think I'm sharing the USB bus with anything else, although it may freeze. I've got the Saly Logic.

**Dave Jones:** I'm not sure where it's plugged into. Anyway, anyway, there could be a USB sharing issue there with the webcam. So, it's a little bit jerky, although I don't have my light on at the moment. Anyway, let's get on to it. I've got my Saly Logic Analyzer hooked up.

**Dave Jones:** I've got Dart. I think I've got these pins around the right way. Channel 1 is my data. Channel 2 is the R clock or the register clock, which actually registers, shifts the data out at the end and the third channel there is the D clock.

**Dave Jones:** So, can I, yep, oh yeah, there we go. I'll swap that over to, so it's just near the data. Just a bit of visual thing and where is my schematic here? Nixie tube, well, Nixie tube schematic. Here we go. Yep. Hello, McFly. There we go, so

**Dave Jones:** the Wemos, so D0, D1 and D2 are my data. My register clock and my data clock. So, hopefully, like I've measured like a 3.3 volts is all working on my board. It's all built up, so it should work. I have checked the pin out, so I believe the pin out is right.

**Dave Jones:** I didn't goof it up on the PCB or anything like that. So, hopefully. Anyway, what I wanted to do is not that. Not too concerned with that. I just want to see if I can get the data. So, here we go. Here's my code.

**Dave Jones:** I'm not showing you my YouTube credentials, which is good. Okay, so let's have a look here and right, so what I've done is I've defined some, I defined D0, D1 and D2. The good thing about the Wemos D1 Mini, I believe, is that you can just

**Dave Jones:** put it like the library has the pins in there. So, you just write to the D0 pin using digital write as you would on any Arduino. So, I've set my pin mode, my data, R clock and D clock. So, basically, it just maps D0 into there.

**Dave Jones:** You could just put D0 into that point there, but meh, whatever. It's better to define it up the top here. So, then you can just change it globally, which is much better and no comments on my code, please. I don't want to hear it.

**Dave Jones:** Seriously, not a professional, you know, programmer. Anyway, so I've defined those pins as outputs. It's basically the example that I've showed in the previous video. I'm doing some binary to BCD conversion here. I haven't even checked if that's right yet, and I'm basically writing to my Nixie clock.

**Dave Jones:** So, like, well, I've got a routine called micro Nixie write. So, after it gets, I know this subscription stuff works, so the subscription counter, that works because I've got, I've tested this before, it's in the previous video, but now all I'm doing is basically going subs is equal to the subscriber count and

**Dave Jones:** then... Yes, it's going to be a YouTube subscriber counter. Spoiler alert. And... Where are we? Yeah, I did spoil it for a lot of people. Everyone's guessed it. Right, so what am I doing? Yes, hang on, lost my train of thought. Anyway, so yeah, I just pulsed the D clock and R clock first just to get the pin state correct on power up.

**Dave Jones:** Because I could have just defined the pin state as high. I believe they're active low, so all good, all good. Sorry for the delay in this. I'm just like checking everything before I push the start button over here and yeah, so active low.

**Dave Jones:** So I've got two routines, pulse D clock and pulse R clock. It just goes low and then sets it back high again. Binary to BCD conversion, and then I've just got where it outputs two for loops that output all of my data. I assume I've got it around the right way.

**Dave Jones:** I don't know. I haven't double-checked any of it. Anyway, I just want to see that the pins toggle and stuff like that. I can figure out the details later. So pulse R clock at the end, so I so it should pulse D clock all the time when it's shifting out that data.

**Dave Jones:** How many? Eight times, you know, eight character displays. Oh, I think I forgot. Yeah, I forgot to add in the decimal point output, so I've goofed. Oh, and some, you know, there's no unused ones. Okay, so if you look at the schematic, if you go back and look at the schematic here,

**Dave Jones:** yeah, I've got no unused ones, and here's the advantage of doing this in order. Okay, a lot of people ask, well, why didn't I just pin swap and stuff like that to make my PCB layout easier? You can, if you want to do it that way.

**Dave Jones:** Hey, I've done it that way before, many times. All power to you. But then, when you come to writing the software, then you've got to do this like a pin mapping thing, and it can get really ugly, and I hate doing those. They're, like, I just despise them.

**Dave Jones:** They're a pain in the ass. But yes, it can make a nice efficient PCB layout, and that might be important to you. So I haven't skipped any, but I forgot the decimal point is the first one. So I've done all of these in order, so,

**Dave Jones:** right, I haven't gone willy-nilly. So they're in order, like, decimal point, then digit one, then digit two, three, four, five, six, seven, zero, right? Oh, actually, the zero's at the end, right? I may have that swapped around. Anyway, doesn't matter. It's much easier than

**Dave Jones:** doing a complete pin mapping for all those eight digits. So, this is my entire code for outputting that data. I've forgotten the decimal point, I believe. So, anyway, it's, like, there's bugger all there, right? And if the number, and I've got the routine up here, which puts it into an array called number, and that just contains the digit value.

**Dave Jones:** Okay, so, then that's all there is to my code for outputting that data. So it makes it real easy. No pin mapping at all. But as I said, a few extra lines for the decimal point and maybe the zero backwards. Anyway, enough yapping.

**Dave Jones:** It should output D-clock all the time. D-clock should go all the time, and then at the end of the whole D-clock period, and then there should be some data there based on my subscriber count. So I expect, on my logic analyzer here, the data to

**Dave Jones:** change, and I expect the D-clock to change all the time. But data will only go low when that particular digit's on. So don't expect too many of those. It'll be mostly high for data. And D-clock changes all the time, and at the end of the D-clock period, where it's output the data for all of those chips,

**Dave Jones:** it should then go low for the R-clock. So that's the plan. So here we go. So if I don't expect data, well, just to be say, I was going to say, like the data may not work. I don't know, I may have goofed up my binary routine.

**Dave Jones:** So I'll set the D-clock thing. No, no, no, hang on, no, I'm going for broke. I'm going for broke. All right, so I'm going to set my trigger. So it should be mostly high, so I'm going to set it for low. Okay, so it should

**Dave Jones:** sit there, spinning its wheels, waiting for that data to go low, that data pin to go low. Okay, so what I'm going to do is I'm going to... Oh, sorry. Here we go. Upload. I think I made it. I think I may have already uploaded it, but I'll do it again anyway.

**Dave Jones:** Okay. Okay, right, so it's uploaded and it should be going. Now, so if I start that, waiting for trigger, yeah, that's right, because it will take some time. Oh, hang on, serial. Where's the serial monitor? Here we go. Sorry. Here's the serial. Oh, hello.

**Dave Jones:** Hello, we captured something. We got one. Did we? No, that's... No, what's going on here? Okay. Oh, my time base might have been way out. Okay, so let's go, let's capture. Let's start that again. Oh, yeah, there we go. So it's waiting for the trigger.

**Dave Jones:** It's, look, it's captured a hundred million samples. So it's waiting, but the serial monitor is what we want. Okay, so until it gets to, it won't update this routine, it won't call that write routine until it's actually got some subscriber count data, because you saw, you remember, that call to the NixieTube write routine was at the end of that.

**Dave Jones:** So, let's wait for it, and it should trigger Oh, hey, hello. Yes. Oh, what did I do, set it low? I set it low? It triggered. Okay. No? Okay. Let's... Hey, there we go. So we've got our, there we go. Isn't that neat?

**Dave Jones:** Told you the frequency and the period. That's very nice. So, where's our data? Where's our data? We've got no data. Let me... Okay, so it's continually high. All right, let me try it again. So, I feared that, but I think it should be outputting something.

**Dave Jones:** Even if I goofed up that routine, it should take that subscriber value and at least give me some garbled data. If anything, come on. Anyway, you saw the D clock and the R clock was doing its thing. There. So, yep. Oh, yes. Yes, we got one.

**Dave Jones:** Okay. Yep. Oh, hello. Hello. There it is. Bingo. So it... Yeah, we just had to wait a cycle or something. Trigger cycle. There it is. Beautiful. That is exactly what I wanted to see. That is a win. Okay, so all this gap here, all this dead period right at the start,

**Dave Jones:** that was waiting for the subscriber count routine to kick in and actually return a value. I don't know how that works. It has to poll the YouTube or whatever, and it, you know, so it takes some time. It only updates like once a minute or something.

**Dave Jones:** And then once it's got that subscriber count value, bingo, it calls up the micro Nixie write routine. And I could put them both on the screen at the same time if I really wanted to. Couldn't I? Yes. There we go. So it calls up that routine.

**Dave Jones:** Yeah, here it is down the bottom here. So it sits here and waits until it gets the subscriber count up here, right? And then it calls the write routine, and then once it calls the write routine, it converts it to binary, to BCD,

**Dave Jones:** because we need to take a... the subscriber count is in a binary. So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary.

**Dave Jones:** So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary. So we need to take a subscriber count in a binary.

**Dave Jones:** So we need to then convert that to a BCD value, binary coded decimal, so that we can display that on the Nixie display, so that we can then output that. And hang on. How does this work? Hang on. Yeah, yeah, right. I've got to be over the waveforms to zoom in.

**Dave Jones:** Sorry, I'm not... don't use my Saly logic analyzer much. It's pretty handy. It's good for... These USB logic analyzers are really good for desktop stuff like this, you know? Like, I have a scope here, like in a box, but I'm at the office at the moment, not at the lab where all my gear is.

**Dave Jones:** So when you're just working on little embedded micro stuff like this, you know, you don't want a big scope on your bench and stuff like that. What a... you know, unless you're looking at signal integrity and stuff like that. So this thing works quite well.

**Dave Jones:** It takes up zero footprint. You just plug it in. I'm going to go into my USB hub on the desk here. There's no power plug packs, nothing. It just works. It's great. Anyway, sorry for the lack of content recently. I have been busy with the multimeter stuff and things,

**Dave Jones:** lots of stuff happening and lots of other things happening. So, yeah, I'm a bit of a go-slow at the moment. But, anyway, so we have... So it's, look, it's output some data. So that's what I expect. One, two... One, two, three, four, five, six zeros and I have...

**Dave Jones:** That's correct. That's correct. Six zeros. Six zeros because I have... Because they're not in the correct order because I said I didn't account for the decimal point. So it won't work. So I won't plug it in and show you like it won't do the business.

**Dave Jones:** But that's not what I wanted to test here. I wanted to test that it's output six different digits. My subscriber count is... Six digits because I have 452,371 subscribers. If I had a million subscribers, I don't think I'll ever get there. Didn't even expect to get to a thousand, let alone 10,000 or 100,000 or half a million that I'm...

**Dave Jones:** Well, getting 450,000, I'm getting ahead of myself. Okay. But if I had a million, then I would have an extra one around about there. So, like, yeah. Depending on its exact position would depend on which number it is. So if it's a one, it's going to be closer to over here and et cetera.

**Dave Jones:** So six digits. It's doing something. Excellent. And so it's data clocking. Fantastic. So it needs to... So on the negative edge, that's when it clocks in that bit there. So it's clocking in a one there, a one there, which means digit off. If it's a one...

**Dave Jones:** Because these are... Open collector Nixie... Open collector drivers driving the Nixies. So you have to drive it low. You have to drive the open collector out, open drain output low in order to turn that pixel on, that digit on. So there you go.

**Dave Jones:** Negative edge there, negative edge there. So everything... And then at the end, right at the very end, of course, we get our register clock. Because once we shift that data in, the display hasn't updated. It's in the internal register. And then you pulse our clock low, which then, boom, shifts them all out at once.

**Dave Jones:** Otherwise, if you drive this too slow and it wasn't a registered data output, didn't have a register clock, it was just a live output, you'd see your data rippling across the display as you shifted in your bits. And, you know, if you did it slow enough, you'd actually see the digits, you know, shifting across your display.

**Dave Jones:** So that's what the R clock's for. So that is a win. That is a win. So, beautiful. So it should plug in a few more things in the code and stuff to just get it right. But that's interesting. So there you go. I hope you found that interesting.

**Dave Jones:** Sorry, if you want the happy ending, you want to see the Nixie tube glow, you're going to have to wait for the final video. Sorry. But anyway, I hope you enjoyed that and found that useful and or interesting. Catch you next time. We'll be right back.
