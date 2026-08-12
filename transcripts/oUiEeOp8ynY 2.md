---
video_id: oUiEeOp8ynY
title: EEVblog #316 - More PFANG, More 13GHz Scope, & More Pulser
url: https://www.youtube.com/watch?v=oUiEeOp8ynY
source: youtube-asr
timestamps: {"0": 1, "1": 32, "2": 54, "3": 87, "4": 109, "5": 145, "6": 161, "7": 185, "8": 198, "9": 211, "10": 249, "11": 288, "12": 316, "13": 348, "14": 390, "15": 419, "16": 454, "17": 469, "18": 504, "19": 531, "20": 550, "21": 573, "22": 598, "23": 620, "24": 653, "25": 690, "26": 701, "27": 735, "28": 761, "29": 789, "30": 822, "31": 856, "32": 888, "33": 915, "34": 941, "35": 962, "36": 995, "37": 1023, "38": 1057, "39": 1084, "40": 1092}
---

**Dave Jones:** Hi. No, it's not quite a mailb bag. Oh, I guess it kind of is. There's the real stuff there. Waiting for the mailbag, but uh I just got something from Chris Jones. Thank you very much, Chris. Uh from the ACT Lions in the ACT. I know what this is. Um it's another pulse generator uh device. He uh claims he used some fast uh logic to make a pulser, and he wanted me to try it out. Well, asked if I wanted to try it out on the uh

**Dave Jones:** high-end agyant scope. And let's have a look at the letter. Hi Dave, don't need any of this stuff back. However, I forgot what logic family chip I used and I'd like to know what chip it is in case ever need to build another one. If you feel like doing an extreme tear down after you tested, appreciate finding out what chip it is. All right. Believe the chips mount upside down. So, yeah. Um below is my best guess at the circuit.

**Dave Jones:** I've included an SMA cable in case you don't have one. Well, let's uh give it a go. Runs off 3.3 to um uh 5 volts and uh and there's nothing fancy on the schematic uh at all. Just an input buffer squares it up and then uh feeds it into a four parallel uh inverter drivers from some form of 74 uh series logic family. Uh presumably it's a very very uh fast one to get the incredibly fast rise times and then an output attenuator and uh to the scope. Oh, look

**Dave Jones:** at that. You know, little plastic tub. That's neat. I like that. Very protective. Oh. Okay. Here's the whole kitten kaboodleoodle. Nice. All right. This is his homemade job, by the way. It's not a uh it's not a thing that's hooked up to uh Hey, look at this. Oh, there we go.

**Dave Jones:** Some dead bug stuff. Let's check this out. This will be nice. Beautiful dead bug style in there on the copper um sheet on the bottom. It should be uh really nice low uh inductance and it should work uh reasonably well, I suspect. Now, let's get a real good closeup of the dead bug style construction in here. On the uh right hand side, there's the uh coax, the black coax there uh coming in. That's coming in from the sig gen, hence why it uh you know, it can have like a bit of

**Dave Jones:** uh length on the end of it because it doesn't uh really matter. Signal integrity of that's not that critical at all. But the output is used like a rigid uh coax here. This is actually, you know, it's it's really stiff and rigid.

**Dave Jones:** It's not your regular uh coax at all. And uh it's all and you can see the jumper wires going over there from pin to pin as required. And uh this really should work a treat. So, um Chris doesn't know what the chip is, so um we'll have to uh desolder it afterwards.

**Dave Jones:** He he said uh by all means actually uh destroy the circuit and find out what chip it is cuz he doesn't recall. But of course we'll uh we won't do that first. We'll measure it first and uh then we'll take it apart and see what's in there.

**Dave Jones:** But yeah, you can see one of the see a couple of the surface mount resistors in there. All right. Now, if you go to Wikipedia and uh you look up uh overkill, you will find a picture of this setup.

**Dave Jones:** $140,000 30 13 GHz scope and a $40,000 uh Agyant 8160 Pang pulse function arbitrary noise generator. I think this might do the business. Now I'm just using the uh pulse capability of it here. And look what we're getting out. Uh it's a rather unusual stepped waveform. Check that out. Now on the Pang, what I've set up here is a 1 MHz uh frequency. I'm using uh pulse mode, by the way. You can see that uh pulse is on over there. Pulse with continuous. So this is all the menu

**Dave Jones:** related to the pulse functionality. And it's spot on. 1 MHz. Look at those 12 decimal places. Oh, it's just brilliant. I love it. And um basically, we're outputting a 3.3 volt um uh peakto peak amplitude with a 1.65 65 volt offset load impedance of uh 50 ohms. And uh so that should can obviously go directly into our scope without blowing it up and it'll be perfect drive signal for our uh for our board here for our pulse gen board. And uh but the reason we're getting this peculiar waveform down here

**Dave Jones:** is I believe because of this leading edge and trailing edge capability here. And of course, we can set up a whole bunch of things. We can set up like the P. By the way, the pulse width is 20 nancond. So, it's a one one MHz uh signal repetition with a 20 MHz uh sorry, 20 nancond pulse. And we can set up all sorts of things. Leading edge, trailing edge, which we'll play with, the amplitude, the offset, uh polarity, load impedance, frequency coupling.

**Dave Jones:** We've got pattern setup as well. We can set up bit shapes, and we can edit the bit waveforms. Ah man, fantastic. I love it. But anyway, let's go into this leading edge here. It's currently set to 50% 50%. So, or 10 nanconds. And if you have a look here at the waveform, you'll see that of course it goes sort of, you know, half the time period it goes at one ramp and the other time period it goes on another ramp. So, let's see what happens here if we

**Dave Jones:** adjust our leading edge. Leading edge. Let's adjust the leading edge here. That's 8 ncond. 7. Hey, look at that. Beautiful. So, let's take that all the way down to 1 ncond. That looks like it's our fastest possible thing. Leading edge, trailing edge. Look at that. So, still not sure why we're getting that little little kick there. That's rather uh rather interesting. And we can wind that all the way out. But uh you can see the power of this thing to generate any type of waveform you like.

**Dave Jones:** And we haven't even scratched the surface of this sucker really. So I'm not sure why we're getting that step there again. But we're certainly getting our nice fast input pulse. But then boop. And if you're wondering if the uh leading edge value we've set on our pang 1 ncond is correct. Well, take a look at the rise time there. And uh you can see it's uh there's no averaging. Of course, it'll get a bit more accurate if there was some averaging on there, but it's pretty darn

**Dave Jones:** close to spoton. You wouldn't expect anything less for 180,000 bucks worth of kit, let me tell you. And let's see what happens if we adjust our pulse width. That's our 20 nconds that we had. And if we extend it out, look, we get that we get that hump in there. That camel's hump. I have no idea why it's doing that. And then if we go beyond that's uh so that's 20. Okay. And if we 19, 18, 17, 15. And when we get to 14, 13, 12,

**Dave Jones:** and that's 10 nconds. And then it does that. That's a one that's a two ncond pulse. That's as low as the P fang will go in terms of uh pulse width. But then there's this following pulse over here.

**Dave Jones:** What's going on? Aha, I think I figured it out. Look at this. Continuous mode, which is what we're using, is output one equals channel one plus channel two. So clearly channel two is doing something. So if we go into channel two, aha, pulse width. There we go. And if we get our channel two and we adjust that pulse width on channel two. Tada! There it is. So, channel two is down to four nconds. And then we can bingo. So, we can combine two different channels there. That's

**Dave Jones:** incredibly powerful. And well, I don't know. Somebody's obviously playing around with this before I had it. And uh that's what it's set to. So, um I've got to figure out how to make the output just equal to channel one. And that's the problem with having such a powerful instrument like this is that, you know, really it's uh um it can do so much stuff that if you set it up incorrectly, well, you're you're pretty much uh screwed. So um and you know, it's not like a scope where there's like an auto

**Dave Jones:** set button you can push. Maybe there's a reset to defaults or something like that. Maybe I could do that. Um but anyway, uh let's have a look. We're in the continuous. So we're in continuous menu here. And uh really I need to uh output channel one plus channel two. I need to change that.

**Dave Jones:** Um strobe out. What do we got? Internal threshold. N trigger out. No. Strobe out. No. Trigger route. Oh man. More options than you can poke a stick at. God. And we haven't even scratched the surface of this thing. No wonder it cost $40,000.

**Dave Jones:** And I do really like this graph mode. You can pull up at any time if you're sick of looking at the numbers. Just ah, show me the wave shape. There it is. Look at that. Beautiful. Except in this case, it doesn't show um it doesn't match what we're getting on the scope because it doesn't show the second uh coupled to channel two. So, you know, I'm still trying to figure this thing out, folks. And bingo, folks. I found it. Of course. Duh. You just press the

**Dave Jones:** uh well the out one here brings you into the output uh menu and then down in the output menu. There is Hang on. Let's do it again. I think I thought I had it. I had an output menu here. Anyway, I was able to switch it off and ta we have our single pulse. Ah, beautiful. All right.

**Dave Jones:** Now, we have the ability just to get a normal pulse. We got one nancond rise and fall time. So, you know, let's let's set it to our 20 ncond uh pulse there and uh we'll see what we get out. Let's plug it in uh plug our board in Chris's little board and uh give it a go. And here's the setup. I've got an SMA to BNC adapter and a BNC um sex adapter there going straight into the scope. And uh this is what we're getting out. Um let

**Dave Jones:** me switch the power off. Boom. Yeah, switch the power back on and uh something is going on there and just had a look at his circuit again. And he of course he's got AC coupling on the output. So let's uh short that AC coupling cap on the output and uh give it another try. Well, the AC coupling fixed it, of course, but um we've got the issue of uh the Pang is uh clearly do is um outputting that higher frequency, sorry, the lower frequency signal there on top of the uh high

**Dave Jones:** frequency 20 ncond pulse that we had in there. So, we got to fix that one, too. And that fix was dead easy, of course. I just put it to square wave mode and went, "Ah, be done with it." Here we go.

**Dave Jones:** So, here's our here is our output pulse. There's some ringing. Certainly some ringing there. Some overshoot and then some ringing. So, that's not that great. But in terms of, you know, if we take sort of the average rise time of this thing, we are talking 250 picos seconds. And uh let's turn on some average in here. And if you want to know how to do that on this thing, it's a it's a pain in the ass to use. But you go into setup, then you go

**Dave Jones:** into acquisition, and then enable. Whoop. If you can get it right, you know, you can either use a mouse or the touchcreen. It's crazy. Anyway, 16 averages. There we go. We've cleaned up our waveform a lot. And oh no, now it's Hang on. Well, of course, it's taking, you know, it doesn't know where to take that. It takes the average of that slope there for the uh 90% mark for calculating the rise time.

**Dave Jones:** So 240 you know almost 250 picos seconds there for the rise time and the four times a bit longer. All right. What I've done now is I've taken the output uh directly from the uh TTL chip itself. And as you can see the uh ringing there is uh quite pronounced as that's for a 70 kHz um signal there by the way.

**Dave Jones:** That's 10 kHz down to 1 kHz. And there there you go. Where obviously um all that funny business you see there. I love I love that effect. That's the average in at work. That's the 16 averages doing that. It's really uh really quite fun to play with that. So clearly what we need here is a proper uh output attenuator, proper uh load matching to match the scope and the adapters and everything else. It needs to be tweaked and uh yeah anyway it was fun to play with. And with the uh output

**Dave Jones:** cap shorted, we've clear I' I've dropped this down to a 2 kHz repetitive uh signal. Okay. So, you can clearly see um that we've got multiple uh reflection issues in here. Here's the high frequency stuff all in there. That's at 5 nconds per division. And then we've got the lower frequency stuff which is five microsconds per division. And clearly we need a proper uh matched fully matched output attenuator.

**Dave Jones:** um you know that's a match to our scope input and all our you know the coax and the whole the whole uh business. So you know these sort of things really need to be uh tweaked but they're fun to play with. You could play with these things until the cows come home. It's really fascinating. But here you know we're talking about you know rise time of you know 47 you know 480. So it's under 500 picos seconds. So, you know, it's it's certainly certainly doing the business

**Dave Jones:** in terms of uh uh edge rise time and stuff like that. You just got to tweak the thing to make it work. So, anyway, might have to leave that uh to another video, but uh I h I don't know. I think we should um at least take this thing apart and have a look at what chip it's using. So, let's just try and get another closeup of this before we lift it all off. If you can see the uh corner pin on the right hand chip there is

**Dave Jones:** soldered directly down to the uh plane down there and there's copper uh tape over the top of the chip and you can see the wires going across and then it's got myar on top of that or some other insulating uh wrapper. And uh really is um you know quite a uh quite a piece of work and it's going to be a shame to take it apart really.

**Dave Jones:** But oh well, we have to find out what chip this is. Let's lift it up. And you can also see that classic tombstone capacitor there on its side. That's how you get really low inductance. You solder it directly to the uh copper ground plane there and then have the wire on top of it.

**Dave Jones:** Awesome. Well, I peeled it off and uh there's nothing on the bottom of that chip at all. So, we're going to have to uh uh flip over the other side and take all that copper tape off, I think. And it's a rather interesting uh build, as you can see, with the uh copper tape and then what looks like the myar over the top and then the uh little um enameled wire connecting uh the various inverters in parallel. So, well, I'm going to have to uh snip all

**Dave Jones:** the enamel wire off and then uh desolder the copper tape and lift it all off. All right, we'll try and get this at the right angle to get it on camera. Sorry, it could be a little bit tricky to see these silk screens. It always is, but there you go. It's a Texas Instrument 74 LVC4 AD, I think it is. There it is.

**Dave Jones:** Yep. 74 LVC4 A D. Date code. H, who cares? But there you go. Excellent. Well, I hope you enjoyed that. Thank you very much, uh, Chris. And if you want to, uh, build up your own one, by all means, um, go for it. Give it a try. And uh yeah, it's I think it's all about the uh getting the uh load matching and all that right as of course is obvious with uh signal, you know, really high speed signal integrity stuff like this. And uh as you

**Dave Jones:** can see, it doesn't have to be high speed in terms of frequency. You know, it can be a 1 kohz signal. It's all about the slooh rate, that rising edge, how fast that thing is. And uh yep, if you don't have the correct uh matching on the on your uh transmission line and your output impedances and all that sort of stuff, then or or your attenuators, then you buggered. So, hope you enjoyed it. If you want to discuss it, jump on over to the EUV blog uh forum. And if

**Dave Jones:** you like it, give it a big thumbs up. Thanks, Chris. Catch you next time.

**Dave Jones:** [Music]
