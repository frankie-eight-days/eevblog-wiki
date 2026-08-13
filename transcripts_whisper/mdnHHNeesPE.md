---
video_id: mdnHHNeesPE
title: EEVblog #771 - Electronic Safe Lock Powerline Attack Part 2
url: https://www.youtube.com/watch?v=mdnHHNeesPE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 33, "3": 53, "4": 69, "5": 85, "6": 101, "7": 121, "8": 133, "9": 149, "10": 157, "11": 173, "12": 189, "13": 201, "14": 217, "15": 233, "16": 249, "17": 269, "18": 289, "19": 309, "20": 325, "21": 345, "22": 361, "23": 377, "24": 393, "25": 405, "26": 421, "27": 437, "28": 453, "29": 469, "30": 489, "31": 509, "32": 529, "33": 549, "34": 561, "35": 581, "36": 597, "37": 617, "38": 629, "39": 653, "40": 673, "41": 689, "42": 713, "43": 729, "44": 749, "45": 773, "46": 797, "47": 817, "48": 841, "49": 873, "50": 889, "51": 913, "52": 929, "53": 945, "54": 965, "55": 985, "56": 1001, "57": 1013, "58": 1029, "59": 1049, "60": 1065, "61": 1077, "62": 1093, "63": 1109, "64": 1125, "65": 1145, "66": 1169, "67": 1189, "68": 1209, "69": 1225, "70": 1245, "71": 1261, "72": 1281, "73": 1305, "74": 1325, "75": 1357, "76": 1373, "77": 1393, "78": 1413, "79": 1437, "80": 1453, "81": 1481, "82": 1505, "83": 1525, "84": 1545, "85": 1561, "86": 1573, "87": 1589, "88": 1605, "89": 1617, "90": 1637, "91": 1649, "92": 1661, "93": 1677, "94": 1689}
---

**Dave Jones:** Hi, this is just going to be a quick follow-up video to a previous one I've done doing some basic power line analysis attack on one of these Legard digital safe locks. This is a CMI basic safe made in Australia. And click here if you haven't seen the previous video, because it's got lots of detail

**Dave Jones:** on various things. So I thought we'd do just a quick follow-up video just looking a little bit more detail in exactly what's happening here on the power line for this particular lock. Let's go. Now as per the previous video, we're doing nothing fancy here at all.

**Dave Jones:** We've just got a 10 ohm resistor in series with the 9 volt battery on this Legard digital lock here. We've just got a standard x1 scope probe. You don't want to use x10 because you're just attenuating a very low level signal. We don't really need the

**Dave Jones:** bandwidth, you know, to get 5-10 MHz bandwidth on a x1 probe is certainly adequate. And on the scope here, we actually want to set this up for you'll notice all the noise and stuff and crap, all sorts of things we're picking up. So we want

**Dave Jones:** to put on some high res mode there, just so we clean up that signal. Now the first thing I want to check, we were doing single shot capture before with like the first button press. So we were checking for any vulnerability on the first button press to see if it

**Dave Jones:** was good or bad, to see if it was actually doing see if we could see any differences on the power line of how the processor inside here, inside the safe, actually detects the first key press. And we really couldn't find any vulnerability on that first key press.

**Dave Jones:** So we're going to do subsequent key presses now and see what it does at the end of entering in all six digits. Now the first thing I want to check is actually, we want to go into instead of regular single shot capture mode, what I want to do is

**Dave Jones:** I want to change the time base. I want to go into roll mode here. So the thing rolls across like that, and we'll be able to see, if I press a button, we'll be able to see the transitions happening in real time. Now, this is the interesting thing.

**Dave Jones:** Let's take a look at this. Now when we press the button here, as you saw, we were getting signal excursions which actually went off scale here, and that's fine, because we want to look at more of the fine detailing here. So we're at 1 millivolts per division

**Dave Jones:** at the moment. Sorry, it's a bit difficult to get this shot. I'm trying to get the lock and the scope in the same shot. I've had to turn my lights down here so that they didn't wash out the screen, because we've got the white here.

**Dave Jones:** It's all it's actually reasonably difficult to shoot this thing cleanly. But anyway, we've got roll mode, so we can continuously see it. So what we want to do now, you can see that it's basically nothing there. 1 millivolt per division, we're getting no noise.

**Dave Jones:** The processor inside the lock, well in the inside of the lock, it's not on the outside here, it's on the inside as we saw in the previous video, is shut down, it's sleeping, it's just waiting, doing nothing, waiting for that key press to interrupt it,

**Dave Jones:** wake it up from its sleep mode, and start up. Now, watch this. If we press a button, it doesn't matter what button it is okay, so it could be 7. The code for this one, by the way, is 1, 2, 3, 4, 5,

**Dave Jones:** 6. It's a 6 digit code, and if we enter the code as I said last time, incorrectly more than, I think, 3 or 4 times, it'll actually lock us out for like 5 or 10 minutes. So that's a very useful security feature that these

**Dave Jones:** locks use. So you can't just brute force them, even if you know what 6 numbers they are in the combination, you can't just brute force it. But let's push it, and watch what happens. Okay, now you see it was clean there, but look, we're getting

**Dave Jones:** some ripple on there. Now that is obviously the processor has not shut back down. The processor's still going, boom, look at that. You can see that it's shut down. So if we actually, I can time that so let's actually do that again, here we go, and

**Dave Jones:** let's time that, and see how long it waits for the next key press. And if that key press doesn't come along, 7, 8, 9, 10, there we go, 10 seconds. So if you don't press a second key within 10 seconds, it'll shut back down and

**Dave Jones:** reset that key sequence. So there's a potential for an attack sequence there, if we could detect individual key presses, as I said, it has lockout mode, but only if you go through all 6 digits. So if I go 1, 2, 3, 4, 5, 7

**Dave Jones:** incorrectly, okay, that's one incorrect key press. If I do that another couple of times, then it will lock us out permanently. And that count resets if I do the correct key sequence here. Okay? So in theory, if there was a way to exploit and detect the correct keys in that sequence, you would actually

**Dave Jones:** have quite a, you would have an infinite number of shots at it, provided that you waited for that 10 seconds to exit that key sequence and reset that timer. You wouldn't get hit by that entry delay thing that they've built into the lock.

**Dave Jones:** So that's a potential way in. It doesn't mean we're going to find anything, and I've actually verified that by doing that like 10 times in a row now, and it does not lock me out. So I effectively get unlimited attempts at doing not only the single digit, but also up to

**Dave Jones:** 5 digits. As long as I don't go to that 6th digit within the 10 seconds between each period, then it'll time out and I get infinite number of shots at it. So yeah, that's a potential way in, perhaps, if there is any powerline vulnerability on

**Dave Jones:** this thing. Okay, so what we want to do now is compare the first and second key presses to see if they're different. So here we go, we've waited the 10 seconds, so this will be a first key press, I'm going to trigger, I've changed it back to single shot capture

**Dave Jones:** mode, YT mode, it's not rolling anymore. And I've set the negative trigger level down here, so that we're capturing, this is the beep pulse which we established in the previous video, that's the physical beep in there. It does all the processing before that.

**Dave Jones:** Now that's what happens if you press the first button. Now we can actually store that waveform as a reference, just like we did last time. So I can go into my reference menu here, and I can go save, we can save that, bingo, there we go.

**Dave Jones:** So now we can recapture that and make sure that's exactly the same again. So let's do it. Don't know, I can't remember what button I pressed last time, but look, it's identical, we get this, the processor seems to wake up here, seems to

**Dave Jones:** shut down, maybe do something, well they're the processor ticks that we saw last time, that noise, you see how we had the consistent ticks like that? Anyway, so it's powered up, it's doing something, it's processing and then it's going into that beep. So it's exactly the same, regardless

**Dave Jones:** of which button we press. I think this is more detailed than what we got last time. So I can repeat that again with the number zero for example. And now this is rather interesting, I press zero there, and that's what I got. Zero seems to be different

**Dave Jones:** to all the other numbers. If I wait the ten seconds which I've waited, okay, because I've been yapping on here, I press any number here, I don't know, five, right? Then we get exactly what we got before. And I can do that, I've gone through off camera here and I've

**Dave Jones:** checked them all, and they all do exactly that same thing, except zero. So we can do number nine for example, okay, I think we've waited our ten seconds, bingo, we get exactly the same waveform. But if we wait that ten seconds again and do zero, zero seems to be special, so I'm not sure

**Dave Jones:** because the program mode for this, you normally have to press star and then the sequence and stuff like that, so I'm not sure why zero first is producing a different result. Not sure what the deal is there at all. So I just slowed the time base down by one notch, and

**Dave Jones:** let's try zero again. It's no, it's exactly the same, but for some reason it doesn't trigger on it properly. Yeah, it doesn't, even though my trigger level like right down here, it shouldn't trigger on it, maybe there's some extra noise in there from number zero, I'm not, I don't know, but it seems very

**Dave Jones:** consistent, so it could, I might just put that down as some sort of triggering type thing. Anyway, it's exactly the same wave shape, I mean if I go like that and shift that over like that, bingo it's exactly the same. Now here's the interesting

**Dave Jones:** one that we want to get, okay, if we do number four like that, okay that's our first key press, doesn't matter what key it is, it's no different, so there's no vulnerability on the first key press. We do the second one within ten seconds, bingo, look what we get.

**Dave Jones:** This sort of like a processor, regular processor noise that we saw before, okay, but it's different, we don't get this pulse here before, and I've actually expanded this time base right out, and as we saw in the roll mode before, these ticks just go on forever and they're exactly the same.

**Dave Jones:** They keep going for ten seconds because it's powered up. So there's only something different here and here, like that. So I can save that waveform as well. Actually what I'm going to do is I'm going to do the correct sequence here, and I'm

**Dave Jones:** going to store the correct sequence for the second digit. So I'm going to go one, re-trigger the scope, two, okay, so that is the correct digit. Uh-huh! Okay, so we now have our white reference waveform there, that was the first digit, and then

**Dave Jones:** the second digit, which was the correct digit, is now this green waveform. So now I'm going to do the same, I'll go one and then I'll go three, which is an incorrect sequence, and see if there's any difference. So let's give that a go.

**Dave Jones:** One, and then single shot capture again, and three. Bingo! It's different! That's interesting. So now we can save that one again, we can enable reference three here, and let's give it a different color, let's give it a light blue here, and we can

**Dave Jones:** actually save that as reference channel three. So now we have three waveforms saved there, the white one is the first keypress, the green one was the second correct sequence keypress, and the light blue one, which is different to the light green one, and that's interesting, is the incorrect

**Dave Jones:** sequence. So I'm going to see if that's exactly repeatable with the correct one, but like instead of one and three, I'll go like one and eight, or something like that, and see if it matches that new light blue waveform. So here we go,

**Dave Jones:** one, single shot, and like seven, lucky seven, shall we? Bingo! It matched the blue waveform for the incorrect sequence. That's fascinating. Oh, we might be getting somewhere! So now what I want to do is capture a correct sequence again, but instead of having one and

**Dave Jones:** two, for example, I'll get it further on in the sequence. So I might get, say three and four in the correct sequence, and it should you know, if the theory is right about there being a vulnerability of the power line on here, in the way it

**Dave Jones:** actually processes a sequence of numbers, correct and incorrect, then it should match the green one and not the light blue one. So let's give that a go. So one is the correct number, okay, so I'll just go like one, two, three, single shot capture, four.

**Dave Jones:** Whoa! It's not quite following the green, is it? It's not quite following it. Look, it's different again! That's a bit of a... I was hoping for that to be the same, but you can see it's lower amplitude here, it's higher amplitude on this one, it's...

**Dave Jones:** okay, let's try. Yeah, that one's higher amplitude, that one's lower, so that's fascinating. So let's try that again for a different sequence further on. It could be because it's got more numbers to process and that sort of jazz. So let's try the next one up, let's try

**Dave Jones:** well, it's... well, we... no, let's try four and five for example. So one, two, three, four, single shot capture, five. Ah, bingo! That one matches the green, so it might have been some anomaly or something like that. I can try the other ones, but it matches.

**Dave Jones:** So that yellow one, as you can see, that yellow one matched the green one, so if it's a correct sequence, it's one waveform. If it's an incorrect sequence, it's another waveform! Oh! That's got... that's got powerline vulnerability written all over it. I'll just try that sequence three and four again.

**Dave Jones:** Three, single shot capture, four. Yeah, it's... it's definitely different! That's... that is fascinating! Hmm... let's try two and three. So one, two, single shot capture, three. It matches the green one! So what's different about three and four? Off the top of my head, it doesn't seem to have any

**Dave Jones:** real significance, but I could be wrong. Now I just wanted to re-verify that the correct sequence, digit sequence, was repeatable. You know how I captured the green waveform before with one, two? Well, it doesn't seem completely repeatable now. It seems to be like one of two types.

**Dave Jones:** You can see the yellow waveform I just captured. Now I'll do it again, okay? So here we go, I'll do one, single shot capture, two, and occasionally it'll match the green one, but often it doesn't. So I... like, it is not repeat... like sometimes it's repeatable, I'll get it like three times in a row, other times

**Dave Jones:** it's not. And it's... so it's not like there's some sort of random function in there, or you know, some sort of randomness in the software because it seems to be like one of two different scenarios. So let's see if I can get it again.

**Dave Jones:** There we go, got it, right? But we can actually try that again. Let's wait our 10 seconds, so I'll just jab her on for another little bit. And that's got to be 10 seconds, surely. So let's try it again. One, two... Hey, it matched it!

**Dave Jones:** Not down here it didn't. So it's... yeah, it's really not 100% reliable, but there is definitely something there at least. So let's put aside that randomness there and say that we have found a vulnerability here where we can find two correct digits in the sequence like this, i.e.

**Dave Jones:** we can identify which is a good two digits in the correct sequence, and which is two digits in an incorrect sequence. Well, to find just the two digits, we have to try all the combinations. So we've got to go 1-1, 1-2, 1-3, 1-4, all the way up to

**Dave Jones:** 1-9, and then 1-0, of course, because it can be the same number in the same sequence. So you've got to try 1-1, and of course you can't do more than 5 at once. So you'd have to do 4 and then stop, you'd have to wait the 10 seconds for the timeout, and do the next one.

**Dave Jones:** And then if you haven't found it, well you've got to go through all the sequences. You've got to go 2-1, 2-2, we can go all the way through to 2-0, and then once again, at each, after you've tried two of those you've got to wait the 10 seconds.

**Dave Jones:** Then you'd have to go 3-1, 3-2, blah blah blah, and all the way, you'd have to try every single sequence just to get two digits in sequence like that. And you might think, okay, well you can calculate how much time that's going to take you, but

**Dave Jones:** which two digits is it? It could be these two, it could be these two, it could be these two, these two, or these two up here. You don't know. So really, even if there is a genuine vulnerability there, it's like, it's pointless to try and exploit that via a brute force attack like this.

**Dave Jones:** It's just, you know, you should be there forever. You're better off just bloody drilling into the safe. And those math nerds can go through the and work out, you know, how much time it would take you if you've only got two attempts like this, and it can be any two digits in the six

**Dave Jones:** digit sequence, and the average amount of time it's going to take you, so you know, you could be rotten luck, could be having a real bad day, Murphy could be right on your arse, you know, and it might take to the last digit to get the bloody thing.

**Dave Jones:** So, you know, ah, man, it's just horrible, but any math nerds want to do the math on that? Go for it. Right, so there may or may not be something there. I think we like, I think we may have actually found something, but anyway, let's

**Dave Jones:** go on and see what happens if we, ah, see if there's any extra processing at the end of the six digit sequence like that. Let's see what, ah, if we can find anything there. Alright, let's do the correct sequence. One, two, three, four, five,

**Dave Jones:** single shot, six. And you heard the double beep there, that means the correct sequence, so we can store that as our correct sequence waveform. Here's just a little annoying thing with the Rigol, when you're saving reference waveforms like this, look, you can enable

**Dave Jones:** all of these reference channels, right? Up to ten reference channels. How many colours have you got to choose from? That's it. You've only got five colours. Wah. And the other annoying thing is it doesn't tell you your currently selected colour there either. It tells you your currently selected, ah, reference

**Dave Jones:** waveform there, but you know, how about your current colour? Geez. How hard is that? Anyway. Saved. Alright, so that's our stored correct six digit sequence that opened the lock. Now we'll do an incorrect sequence. One, two, three, four, five, single digit, seven. Hey, look at

**Dave Jones:** that! Wah, that's interesting. So once again, I think we've been duped by the time base there, so let's actually try that again. I'll just do the correct sequence just so I don't accidentally lock myself out or anything dumb like that, okay? So now we'll do the incorrect sequence

**Dave Jones:** again. Five, and single shot capture, and seven. So we're at a slower time base now, so then we can scroll, we can now move that back, because we've got the detail to do that now. And, ah, that's where it starts. So it's got

**Dave Jones:** yeah, look, it's got a funny little, funny little jaggy there, and it doesn't line up in time well, actually I'm not going to say it doesn't line up in time sequence, because it does if you align the start there, that certainly lines up, but look, that's different, okay?

**Dave Jones:** That is definitely different. Now I'm going to end up like a completely incorrect sequence now, okay? So I'll actually stall that one as reference five. The other annoying thing about the Rigol is this selection control here is incredibly touchy, and like you only have to just breathe on it.

**Dave Jones:** You fart halfway across the room and the thing moves. And also when you go to press the button like this, you can often cause it to move just before you press it. It's just, it's really, yeah, it's very touchy. They need to do

**Dave Jones:** something about that. Oh, bloody hell, it selected the wrong color I wanted orange, and it didn't do it. Oh, it's, what's it done? Arrgh! Alright so our orange waveform in there is the correct one, okay? In the correct sequence, and that white slash grey

**Dave Jones:** one there is our incorrect sequence. Let's verify that incorrect sequence again. So I'm going to go just, I don't know like, eight two, three, four, five single shot, and two. I don't know something like that. There we go, yep. Hang on, no this has gone back up here

**Dave Jones:** instead of going back down there like the other one so something, once again, that's yeah, that's changed. We've got this huge spike there, which we didn't it didn't go all the way back up before, it sort of started going down there. So it looks like there's some sort of difference

**Dave Jones:** between the, between, you know, like a close number, and one that's not perhaps. Hmm. Alright, so let's do one that's say halfway in between one, two, three six, five four. Ah, that one's identical see, this is like the non-repeatability like I've seen before on the other one when we're checking for two digit

**Dave Jones:** sequences. Seems to be something happening there again perhaps, because look, it's matched that grey, that white one we had before when we did one, two, three, four, five and then seven, and now we did one, two, what did we just do? One, two, three, six, five, four, or something.

**Dave Jones:** And it's an identical waveform, but there is a difference. So let's do the repeatability again. One, two, three, four, five, seven. Let's try that again, and it should match the orange waveform. So oh, I don't need a single shot capture of that. One, two, three

**Dave Jones:** four, five, single shot seven. So there you go, it's exactly the same again. So let's keep going, let's just run another sequence, shall we? I'd better do, actually, damn it. Oh, I locked myself out! D'oh! Ah, people were probably screaming at me there.

**Dave Jones:** Yep, I did three in a row and locked myself out. D'oh! Okay, let's do the repeatable correct sequence again. I've waited my ten minutes or whatever for the time out. Ah, that was embarrassing. One, two, three, four five, single shot, six. Boom. Yeah, that's good, it matches.

**Dave Jones:** So, I'll just shuffle that across. The Rigol's a bit, not hugely responsive to the vertical, ah, the horizontal position control. It's a bit, ah, once again a bit touchy, you get some overshoot there, it's really annoying. But yeah, it matched that orange waveform that we had before.

**Dave Jones:** So bingo! Um, let's do it one more time, just for kicks, shall we? Five, single shot sequence, six, safe opens, and wah, no, see? Look, it's shuffled that, look, that's low amplitude, this is high amplitude. So it seems to it seems to randomize, perhaps.

**Dave Jones:** Like, like not completely random, but it seems to, like, as I saw before, it does seem to change. It's not entirely repeatable, and I'm not sure what the deal is, whether that's a deliberate decoy in the firmware. Because on a well-designed product like this, they'd be aware of powerline attacks, and you'd expect them to

**Dave Jones:** possibly build in some randomness, or, you know, to do some tricks in firmware to actually, ah, you know, to mask that sort of thing. So yeah, perhaps that's what they're doing. So, like, even if there is a vulnerability there well, you know, once again, like the two-digit sequence before

**Dave Jones:** what does that, how does that help us? Not much at all. So really, that's all I wanted to, ah, check for today just once again, a very basic, ah, powerline analysis with a, you know, as simple as you can get with a 10-ohm dropper resistor in series like that, and just a

**Dave Jones:** scope probe and just a scope doing that. You know, yeah, you can get better tools for the job like this, like the chip whisperer, which I had, and things like that. You can really gain it up and see the noise and get averages and do, you know, get the

**Dave Jones:** data out of the noise and all sorts of things. So I just wanted to, once again, I'll probably still get complaints of people, oh, I didn't go far enough but anyway, that's all I've got time for now. I've got to head off and finish

**Dave Jones:** assembling my X-Carve live. Now, by the way, we're about to switch that on live, but you won't know this because this video will be is not going live, so, eh, too bad. So yeah, we found a couple of interesting things there, and there might be some sort of vulnerability there

**Dave Jones:** but, you know, it doesn't seem consistent, which is really annoying, and as I said, even if you, even if there was a vulnerability there, once again go through the math of how many, if you did the, had to do the whole six digits even if there was a vulnerability there

**Dave Jones:** with the, like the three attempt ten minute lockout, it's just, you know, so you have to do it some other way. So I think just the way I've been doing it, the simplistic approach, it seems reasonably you know, it seems reasonably safe. Ha!

**Dave Jones:** Pun intended. But yeah, no, it doesn't mean this thing is not vulnerable. I mean, if you use much more advanced powerline attacks and things like that, people have talked about like seeing the, maybe the I squared C bus for this keyboard, if it's like an I squared

**Dave Jones:** C bus, might be in parallel with the one at the back. Nah, you know I pretty much don't even have to test that. This is one of the best locks on the market, this Legarde one, as I said before, and if it was that vulnerable

**Dave Jones:** and if it was that vulnerable that you could read the code out of the E square prom and she was hooked onto the same bus as the keypad then yeah, that would be a well-known exploit. So you know I don't think they're that stupid.

**Dave Jones:** Anyway, that's all I've got time for today. I'd love to do some, maybe I might do a video with the chip whisperer, some more advanced stuff and things like that. So this is just very simple, so please don't complain that I haven't gone far enough.

**Dave Jones:** I know I haven't gone far enough, it's just, once again, just wanted to do some simple tests and we did actually see some differences there, so I'm actually quite impressed by that. We did actually make a bit of progress even if it's pointless.

**Dave Jones:** But I hope you found that an interesting video anyway. If you liked it, please give it a big thumbs up. If you want to discuss it, EEVblog forum, YouTube comments, I try and read them all. Catch you next time. EEVblog
