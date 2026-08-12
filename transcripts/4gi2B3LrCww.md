---
video_id: 4gi2B3LrCww
title: EEVblog 1521 - CMRR Full Edit
url: https://www.youtube.com/watch?v=4gi2B3LrCww
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 35, "3": 53, "4": 71, "5": 84, "6": 99, "7": 108, "8": 130, "9": 153, "10": 164, "11": 182, "12": 195, "13": 209, "14": 224, "15": 239, "16": 254, "17": 277, "18": 290, "19": 302, "20": 312, "21": 329, "22": 340, "23": 347, "24": 363, "25": 371, "26": 384, "27": 403, "28": 416, "29": 429, "30": 440, "31": 449, "32": 464, "33": 474, "34": 486, "35": 504, "36": 520, "37": 535, "38": 552, "39": 569, "40": 580, "41": 590, "42": 610, "43": 626, "44": 641, "45": 656, "46": 670, "47": 678, "48": 692, "49": 705, "50": 716, "51": 723, "52": 739, "53": 753, "54": 767, "55": 774, "56": 786, "57": 794, "58": 808, "59": 822, "60": 838, "61": 853, "62": 863, "63": 878, "64": 888, "65": 899, "66": 912, "67": 920, "68": 931, "69": 947, "70": 958, "71": 969, "72": 979, "73": 997, "74": 1015, "75": 1029, "76": 1046, "77": 1058, "78": 1077, "79": 1088, "80": 1098, "81": 1109, "82": 1123, "83": 1134, "84": 1145, "85": 1157, "86": 1173, "87": 1189, "88": 1203, "89": 1215, "90": 1224, "91": 1244, "92": 1254, "93": 1280, "94": 1297, "95": 1312, "96": 1322, "97": 1343, "98": 1356, "99": 1364, "100": 1381, "101": 1401, "102": 1410, "103": 1421, "104": 1433, "105": 1447, "106": 1459, "107": 1468, "108": 1480, "109": 1493, "110": 1507, "111": 1524, "112": 1534, "113": 1545, "114": 1554, "115": 1568, "116": 1582, "117": 1599, "118": 1610, "119": 1619, "120": 1628, "121": 1647, "122": 1666, "123": 1687, "124": 1698, "125": 1707, "126": 1717, "127": 1725, "128": 1736}
---

**Dave Jones:** Hi, in this video I'm going to explain what common mode rejection ratio is and actually how to measure it in this particular case of a high voltage differential probe here, but it doesn't have to be a high voltage differential probe available on the EV blog store by the way, discount coupon code down below, doesn't have to be a probe like this, any differential amplifier circuit be an op amp or a discrete transistor

**Dave Jones:** one, it will have a common mode rejection ratio. So, let's have a look at it. We're going to measure it with the brand spanking new Rohde & Schwarz uh four MXO 4 series scope here, 12-bit jobby, because oh, why not?

**Dave Jones:** It's beautiful. So, the common mode rejection ratio of a differential amplifier, in this case a differential probe, as the name suggests, is just the ratio of the differential gain of the amplifier divided by the common mode gain of the amplifier.

**Dave Jones:** And what is differential and what is common mode? Well, a differential amplifier measures the difference between uh two inputs here. There base essentially is no ground reference. It is a differential signal, and a differential amplifier will have a a gain of that differential signal.

**Dave Jones:** That's its job. If your differential amplifier has a gain of 10 and you put 1 volt differential across here, it doesn't matter where it is in the circuit, it's a differential voltage, doesn't matter about the ground reference, it'll multiply that by 10, and that's its differential gain.

**Dave Jones:** Now, you divide that by the common mode gain. Now, what is the common mode gain? Well, instead of the differential voltage across here, it is an external voltage applied to both of them at the same time.

**Dave Jones:** So, in this particular case, okay, we've got these long leads here, and we could have like external uh either capacitive coupling or EMI coupling into the probe like this.

**Dave Jones:** So, they're basically getting onto the probes in the same way. And this is why the wires are twisted like this. And if you're measuring a differential signal, it means any external noise or interference will actually in should, in theory, um apply to both uh wires at the same time.

**Dave Jones:** So, it's an external reference. In this particular case, referenced to the grounded output of our differential probe. So, the job of a differential amplifier is to amplify the difference between its positive and negative input while rejecting all of the signal or much of the signal as it can that is applied commonly to both of these wires.

**Dave Jones:** So, that's why it's a common mode rejection ratio. So, in theory, your differential amplifier should have an infinite common mode rejection ratio. It just measures difference here and rejects everything else.

**Dave Jones:** It has no gain at all of any common mode signal being picked up by both wires. But, in practice, uh no, that's not going to happen. Just the design of the amplifier itself and most importantly, the matching of the input uh resistor uh network in here.

**Dave Jones:** And I've done a teardown um of a high-voltage differential probe down like this. I'll link it in up here and down below if you haven't seen it. And just the matching between the resistors on here is um like pretty much determines the common mode rejection ratio of this probe.

**Dave Jones:** Because usually, like the op-amps used inside here, they're usually pretty good. They're going to have like a rejection ratio of like, you know, over 100 dB or something. Whereas, the resistor divider drops that down to like 40 or even less.

**Dave Jones:** Now, a product like this HVP 70 differential probe, it'll typically have a common mode rejection ratio figure measured at various spot frequencies. Maybe, if you're lucky, you might get like a response uh curve of common mode rejection ratio because it's going to vary depending on the frequency.

**Dave Jones:** So, it's going to change. So, they typically, here's the uh values for this HVP uh 70. And it gives us four spot values there. And the ratio, you can see, is, you know, like at 10 MHz, minus 40 dB.

**Dave Jones:** And it is usually given in a dB figure, but it doesn't have to be, because it's just a ratio. So, you could just use the ratio figure. And the interesting thing about this is that the common mode rejection ratio is, as I said, the differential gain divided by the common mode gain.

**Dave Jones:** And that actually comes out at a positive value. So, why is the data sheet negative? Well, it's kind of there's no like standard for this kind of thing. So, you just sort of have to like understand that when you're talking a negative number, in this particular case, minus 60 dB uh common mode rejection would be better than minus 40 dB.

**Dave Jones:** But if you had it if you specify it as a positive one, as you might get on, say, a uh op-amp data sheet, here's an example, uh you would get a the higher the value is going to be better.

**Dave Jones:** So, that positive or negative thing, just a little trap for you young players, just be aware of that. Right, so how do we measure the common mode rejection ratio and verify the common mode rejection ratio of this probe?

**Dave Jones:** Well, what we've got is a our differential input like this. First thing you want to do is, as I said, you want to twist the wires like this so that any uh external noise is equally picked up on both.

**Dave Jones:** And then, you need a signal generator. In this particular case, this uh new Rohde & Schwarz MXO 4 can go up to 100 MHz, so very nice. So, we can actually measure the 100 MHz uh this one's got a bandwidth of 100 MHz this mixed mode jobbie, which we'll measure as well.

**Dave Jones:** And then, we want to feed the output of the sig gen into a 50-ohm terminated load so that uh we don't have any transmission line issues whatsoever, no reflections causing problems.

**Dave Jones:** I've done videos on that and how you can goof that up in noise measurements and stuff like that. So, I'll link in that video up here and down below if you uh haven't seen it.

**Dave Jones:** So, here I'm using an external 50 ohm uh 2 watt termination, a series termination, even though the scope has a built-in uh 50 ohm termination, but if you look down here, you could actually come a cropper because this is only like got a half watt rating.

**Dave Jones:** It's less than 5 volts RMS. Just, you know, you don't want to blow up your scope when you do something like this cuz you want to use a high as high a voltage as uh possible.

**Dave Jones:** In this particular case, we could do it cuz we're less than 5 volts RMS, but in this particular case, I'm just showing you it's better to use a high-rated uh external uh terminator just so you don't blow up your really expensive, beautiful, shiny scope.

**Dave Jones:** And then, we're just uh tapping off right across this uh 50 ohm terminator load here. So, here's the negative uh terminal and here's the positive terminal. So, what we want to do is connect both of these inputs together, short them together, and connect to the positive input like this.

**Dave Jones:** Why the positive input? Because it means that we're applying a voltage relative to the output here cuz the output is ground referenced like this. So, we're actually uh referencing it to the output.

**Dave Jones:** So, we're effectively feeding that signal generator voltage into both of these leads, i.e., a common mode signal relative to the grounded output. Because if you remember, all the grounds on your scope are all common.

**Dave Jones:** So, this is the input signal and the output and they're uh effectively joined. They're common. So, what happens if I just connect one of these to here? Well, you saw it.

**Dave Jones:** The green signal's our output, the uh yellow is our input there, and our green signal we it's actually going to give us an an output. Here it is here.

**Dave Jones:** It gives us a nice, clean output like that, okay? So, our differential uh probe is cuz this one's just flapping around in the breeze, right? Doing nothing. And you'll see that just jump all over the place there and if I touch it, look at that.

**Dave Jones:** Like we're picking up all sorts of crap, right? But and you'll get the same exactly the same thing if you connect the negative up like that, right? The exact same thing will happen cuz this is a differential amplifier.

**Dave Jones:** It it doesn't care. Um it just you're just unbalancing that input. But if you connect both of them on like that to the same point, then bingo, we've got a really small signal.

**Dave Jones:** So this probe isn't perfect. It's got a common mode rejection ratio. So there you go. It's there's a signal being amplified even though that input is completely shorted. And you'll notice that goes away if we don't connect up to that, okay?

**Dave Jones:** There's our ground there, so we've just got like the inherent noise of that amplifier and it doesn't matter what I do to the probes here, but this one if we hook it back up, you'll notice if I start playing with those probes, right?

**Dave Jones:** Things start happening, okay? Like, you know, it starts like being influenced because like we've got these long leads here. That's why a differential probe with like like really shorter leads is better, but these have them most probes have them built in though unfortunately.

**Dave Jones:** So what happens if I untwist those leads like this and so we're going to get the same signal, but we have potentially have more variation. Check it out. You actually get huge differences like if I like take my hand away from that, right?

**Dave Jones:** you can get large differences like that. So if you don't twist the leads and keep that common mode signal, right? You can completely screw up and come a cropper on your measurement, whether it's a probe or whether or not it's a differential amplifier op amp or discrete transistor circuit, whatever it is you're measuring.

**Dave Jones:** Yeah, the signal conditions you're measuring here cuz we're talking about very low level signals, it's really important. Now that I've explained what we're doing and I've shown you the setup here, there's no reason to look at this anymore.

**Dave Jones:** So, I'm going to actually go over to a remote desktop view and uh we'll do a direct screen capture of this. It'll be just nicer and because I can.

**Dave Jones:** Ah, isn't this schmick? Look at this. Ethernet remote control. It's got a built-in web browser, so we can just go to the IP address and bam, we're in. So, we can actually we can do some like configuration and file manager stuff, but let's just go to full screen here and we can either get the uh with the front panel or just the screen like this, but we'll include the front panel,

**Dave Jones:** so my ugly mug's not covering too much. So, channel one, the yellow one, that's our uh sig gen there. We've got uh 1 V per division, 50 MHz bandwidth cuz you do want a uh bandwidth limit and this scope actually has some cool software bandwidth uh limiting options in it um which might see later.

**Dave Jones:** And uh one one big ohm uh input uh DC coupled, DC or AC, it doesn't matter. And channel two also the same uh 50 MHz uh bandwidth here, 500 microvolts, but uh yeah, we've No, let's just leave it on uh 2 mV there, shall we?

**Dave Jones:** Now, you can see we've got a real fuzzy wuzzy waveform here. Now, of course, this is a uh 12-bit scope. You don't necessarily need a 12-bit scope for, you know, this particular application that we're doing uh right here, but 10 or 12 bits more betterer, but we can actually go more than this.

**Dave Jones:** So, you can actually see up here up the top it's telling us uh to just that's the basic 12-bit uh but we can go higher because if I get my ugly mug out of here, we can see that I've got a HD mode down here, a high definition uh mode and we can actually set that on Whoop.

**Dave Jones:** There we go. We instantly set it on and you'll notice that our 12 bits went to 16 bits up here. And notice and watch it watch this. This is really cool, right?

**Dave Jones:** You notice how um history mode up here. See that number history? It's taking half a million um history samples, not histogram, but history uh samples. That's what the history button down in the bottom uh corner here, is.

**Dave Jones:** Now, if we turn this off, it'll reset that and look at how quickly it captures. Boom! Look at that, right? A million A million waveform captures um just in a couple of seconds there.

**Dave Jones:** This scope's actually capable of 4 million waveform capture per second, and you might see this in an upcoming uh review video. Leave it thumbs up down below. Comment um yeah, I have already done an unboxing video.

**Dave Jones:** I haven't edited it yet. There were delays, but And then if we turn that off, it'll go back to 12 bits. Boom, half a million like that. So, yeah, it's really quick.

**Dave Jones:** Really schmick. So, let's turn HD mode on there. But before we go ahead with that, I'll just mention the uh signal gen here. Now, uh you want this to be as high a amplitude as possible because the output signal that you're actually trying to measure um that common mode signal is really low.

**Dave Jones:** So, the higher the input signal, the better. So, I've gone up to the maximum uh amplitude here of uh 5 V peak-to-peak here, and uh we've got a frequency of 10 MHz because that's just the uh uh you know, a typical figure we've got in the data sheet which we want to try and uh verify.

**Dave Jones:** So, we want to clean this up a bit more, so let's do some averaging. So, we'll go up to the uh acquisition up here, and we're actually uh in sample mode, so we'll go down here to average mode, and then boom, we can do like 40 averages, something like that.

**Dave Jones:** We can take the uh time base out a bit like that. You notice how it gets a little bit like chunkier when it goes I guess that's a feature.

**Dave Jones:** So, we've got a decent number of signals. You can see that our average there we've got 40 averages there, and uh that's just cleaned that up a tad. can see how we are dealing with the wobblies down here cuz as I said, the test setup is everything.

**Dave Jones:** So, if you can shield it and keep the leads short and uh make sure that they're twisted and everything else, it's going to be uh better. But let's see if we can uh use this to get our uh figure.

**Dave Jones:** So, what we need now is to compare the input signal to the output signal. That'll give us our common mode rejection ratio. In this particular case, uh Uh, you saw on the data sheet that it's actually negative here.

**Dave Jones:** So, at 10 MHz it's minus 40 dB here. So, we want to flip that around here to give the output divided by the input. Now, to measure this uh, ratio between input and output, we can either measure the peak-to-peak value or the RMS value.

**Dave Jones:** Doesn't matter. RMS is, you know, it's better, it's more accurate. But, you might think that we use this RMS value here. And uh, that 1.4 mV like that. But, I've done a video on this where that RMS value, that includes any DC offset component.

**Dave Jones:** So, that's not quite what you want. So, let's go into the measurement menu here. Unfortunately, they don't have it in the basic category. You've got to go down to the what the vertical there.

**Dave Jones:** There you go, standard deviation AC RMS. I've done an entire video on that. So, we want channel one. We should be able to drag that to like a trash bin or something.

**Dave Jones:** I should be able to right click on that and actually delete. You know, the user interface, come on. But, I can actually go in here like this. I can double click on that and I can choose specific type AC RMS like that.

**Dave Jones:** I do like how every menu here you can actually set the transparency with the slider bar there. That's kind of like really groovy. And you see how in this menu here it does actually have a trash can down here.

**Dave Jones:** But, it's like and then you've got to select which one you want to trash can but I can't like no, no, no. You know, well, you either like that or you hate it.

**Dave Jones:** So, let's actually get a few waveforms on screen here so it's a bit more accurate. And once again, we can turn the statistics on there. Come on. Can't double click to get into the menu.

**Dave Jones:** By the way, one little thing I wish they had is that where is the the signal generator's on? Why is that not on the screen somewhere? It should be somewhere.

**Dave Jones:** Look look look at all the dead space down here. I shouldn't have to go into the sig gen here to actually see that that's uh 10 MHz there. It should be on the screen somewhere.

**Dave Jones:** Please, Rohde & Schwarz, add that. See, they've got all the other channels here that when they're not on, they're over here, right? But the sig gen's on, so the sig gen should actually pop up over here as one of the boxes to tell you what that the sig gen is A on and B what the settings are.

**Dave Jones:** I got I mean, it's just inconsistency there. Oops, I had the uh wrong bandwidth there, so we have to use the 50 MHz uh bandwidth here cuz we're measuring 10 meg 20 meg is a bit close to the frequency.

**Dave Jones:** You want to be a bit more than double above like that. So, you know, 50 is 50 is not a bad value. So, we get our confuser out here and we look at the RMS value here.

**Dave Jones:** Don't be confused by Remember how I mentioned standard deviation before? You got to watch my standard deviation video. The standard deviation here is not referring to the AC RMS.

**Dave Jones:** It's referring to the standard deviation of the standard deviation AC AC RMS signal. So, it's like it is very confusing. So, yeah, don't come a cropper there. Anyway, so we need to uh get our confuser out and uh 883 microvolts.

**Dave Jones:** So, I or 882 microvolts. We won't get any more precision than that. Uh divided by our input because we want a negative uh number. So, 1.75 V. Then we want to take the log of that uh and then multiply that by 20, not 10 cuz this is a voltage.

**Dave Jones:** So, we get minus 65 minus 66, basically. Hmm. That doesn't sound right. Cuz our spec over here says minus 40 at 10 MHz. Why is it way, way better?

**Dave Jones:** Way, way better. Hmm. Because this CMRR is what's It's input referred. It's referring to the input of the actual uh amplifier in this case inside the uh probe here before it gets gained up by the amplifier.

**Dave Jones:** Now, if you noticed in the video before, we're in the uh 10:1 division ratio setting. So, there's a gain of 10 in there. So, we have to account for that uh gain of 10 in here in our dB figure.

**Dave Jones:** Now, you know, a good data sheet, they should actually specify that and tell you exactly what it is. Now, this is a good marketing trick because marketing can make the common mode rejection figure sound a lot better just by saying, "Oh, that's input referred." instead of like output referred or you know.

**Dave Jones:** So, just don't get caught by that, okay? So, in this particular case, uh our times 10 uh probe over there, times 10 of course in dBs is 20 dB.

**Dave Jones:** And times 100 would be 40 dB. Times 1,000 would be 60 dB. Cuz of 20 dB for each order of magnitude step like that. I've done a video on dBs.

**Dave Jones:** And that's just a cool nature of uh dBs. So, we have to actually add on uh 20 dB to that. So, um 66 minus 66 dB becomes minus 46 dB.

**Dave Jones:** So, yes, it does actually meet that specification. So, it beats it by 6 dB actually. Not too shabby. But, this is only a typical figure. So, you know, yeah, but we're actually doing better than that.

**Dave Jones:** So, let's repeat this at 1 MHz. So, it should get better by about uh 10 dB. So, got this 46 here. Maybe we'll get 56, will we? Let's see.

**Dave Jones:** So, we want to go to 1 MHz on our sig gen there. And we do want to change the lower the bandwidth of our input here. So, we'll go in there and we'll just drop that down to say 20 meg there.

**Dave Jones:** So, you know, reasonable margin, but you don't want to be too high. And then we've got to change the time base. Otherwise, we won't get enough waveforms on there to give us a reasonable value.

**Dave Jones:** So, there you go. 423 microvolts divided by 1.8 volts there. Uh and log * uh 20 = -72. Yep, there you go. Um so, you subtract or add 20 dB to that.

**Dave Jones:** So, it's -52. So, there you go. This typical spec is -50. We're getting -52. Yeah, comes out. And let's try 20 kHz, shall we? I think it's come out at -52 dB.

**Dave Jones:** It's basically the same as what it was at 1 MHz. So, um our situation has not improved. So, why is it a good 8 dB outside of spec there at 20 kHz?

**Dave Jones:** Don't know. Um I can't think a reason why. So, what I'm going to do here is I'm going to go into acquisition, and I'm going to change the band with the acquisition bandwidth.

**Dave Jones:** Now, here's a cool feature of this Rohde & Schwarz scope. We can actually define a software bandwidth, and we'll see later how cool this is. Let's set say 100 kHz like that.

**Dave Jones:** Boom! Look at that. So, we can now software clean that up really schmick, really nice. So, we can set any arbitrary software bandwidth limit on there. So, you put but the hardware over here, you can see it's put it down here as 100 kHz, okay?

**Dave Jones:** It's overridden the bandwidth of the hard the hardware bandwidth of the front end, which is 20 MHz. Now, it's overridden that, and it's put it down the bottom corner here, and it's put it on the channel as 100 kHz.

**Dave Jones:** So, so yeah, hardware bandwidth 20 MHz, effective bandwidth 100 kHz there uh because we've put in a software filter like that. So, that's cleaned that up very schmick and it is slightly dropping there, but you know, like 404 405 microvolts divided by 1.79 log * 20.

**Dave Jones:** Um we're still and you add on the 20 dB minus 52. 9, so yeah. Doesn't meet the spec. But if we try and measure it down at 50 hertz here, which is supposed to be minus 80 dB, so I generally like it it's 20 dB increase over 20 kilohertz.

**Dave Jones:** You can see that yeah, it's it's gone to nothing. Again here, 500 microvolts per division and there's nothing there. I mean, we can take that figure and punch it into the calculator, but like there's just nothing there.

**Dave Jones:** We're basically measuring the RMS value of the noise at this point. Anyway, you can see the process there. That's how we can measure the spot frequency. Now, how can we get a plot over frequency?

**Dave Jones:** I'm glad you asked. We can do this using if we go into apps here, ta-da, one of the things it's got is FFRA or frequency response analyzer. So, let's open this bad boy up and yeah, we can get a plot of this over frequency and we can also get phase as well.

**Dave Jones:** So, we're going to put our stop frequency in here of 10 megahertz and start frequency. Yeah, we can actually start down at that 50 hertz figure. Yeah, we can't actually measure that.

**Dave Jones:** So, points per decade, I don't know, let's just have two points. This is not like total cuz you can have total in there. Just two points per decade like that.

**Dave Jones:** Whoop, value out of range. Why? Looks like the minimum we can have is actually 10 points per decade. That's kind of well, it's a lot. So, we set up our input is channel one, our output is channel two, 50 hertz to 10 megahertz.

**Dave Jones:** Amplitude as you once again, you want the maximum uh amplitude and we're good to go. So, we should be able to now hit run on this. Now, watch down in the bottom corner down here as it's adjusted, it's set to AC and then it's adjusting the range all in real time.

**Dave Jones:** It's adjusting that and you can see it's slowly pro plotting here. It's only a small it's got a table and thing we could we could zoom that later if we really wanted to.

**Dave Jones:** Okay. But, 50 Hz 100 Hz, right? It's down in the noise. Anyway, here it comes. Here it comes. 10 kHz. So, it's starting to get out of the noise there.

**Dave Jones:** And we can adjust the range in a minute to actually see that and boom, we are done. So, can we actually make that whoop down like that? So, we can make that a bit bigger.

**Dave Jones:** Now, I don't think there's anything in here that allows us to set the offset there. be in advanced. Maximum phase measurement delay off uh real resolution bandwidth, no. Delay time, no.

**Dave Jones:** So, we can't like add in Maybe we can do some maths on that, but I'm not seeing it. Anyway, just remember that we have to add 20 dB onto these figures here.

**Dave Jones:** So, you can see that you know, around about 5 MHz there, it does really you know, it starts to sort of like uh you know, common mode rejection ratio gets worse.

**Dave Jones:** The higher that is the worse it is and you can see that the the red plot here is the gain. We're not too That doesn't matter for our common mode rejection ratio, but if we actually extend the bandwidth on that, we should be able to actually see a phase reversal.

**Dave Jones:** Anyway, we've got our table here. So, let's actually go to our 10 MHz. So, at 10 MHz here, you can see minus 64 which is minus 44.95. So, yeah, that is better.

**Dave Jones:** I can't remember what we got before. Is that more better at the 1 MHz? So minus 71 is minus 51 dB there. So yeah, that meets the spec of minus 50 as we saw before.

**Dave Jones:** And at 20 kHz, 22 near enough, it's minus 71. So minus 51. Once again, yeah, we just don't have the ability to measure that low really. So it's kind of like the maybe the limitations of the hardware measurement hardware that we've actually got here.

**Dave Jones:** We're just We're just not getting that. So if we go up to the full bandwidth here, 70 MHz of this probe, let's rerun that again and see what we get.

**Dave Jones:** I'm not going to go low frequency this time. So I'll start that at uh 100 kHz, shall we? So it's auto ranging each time it actually takes these samples, which is really quite nice.

**Dave Jones:** So it's maximizing its dynamic range there. And it's also adjusting its bandwidth as well. You'll see that the Yeah, just jumped from 1 to 2 MHz, 3 MHz, see?

**Dave Jones:** So it's actually software adjusting that bandwidth. This is really cool. This is a very good frequency response analyzer. So we're looking for the phase response to actually uh reverse here.

**Dave Jones:** Oh, yep. There it is. There it is. Hey! That's totally expected. Totally expected. That's a normal amplifier behavior. Not just a differential amplifier, it's normal amplifier behavior. So expected that.

**Dave Jones:** But once again, phase doesn't mean anything here. But you can say that yeah, up it right up to 70 MHz, it's minus 41, which is minus 21 dB. So it's a fairly sharp rise after, you know, once once you get above that 10 MHz, that's why they don't give you a figure up at 50 meg or 70 meg.

**Dave Jones:** They Once again, marketing just you know, stop at 10 MHz. I know it's my probe, but I didn't make this data sheet. It was done by the manufacturer Sapphire, who's a Taiwanese manufacturer of probes.

**Dave Jones:** They're excellent, by the way. Um, they make some of the, you know, Rohde & Schwarz, um, LeCroy rebadge them and a whole bunch of other companies rebadge our sapphire probes.

**Dave Jones:** They're really good. Unfortunately, this video's been long enough, so I'm going to leave this, uh, Micsig, uh, probe. I'll leave that to a, uh, second channel video and I'll show, uh, the results from this one.

**Dave Jones:** So, that's how you measure common mode noise. I hope you found that, uh, interesting and informative and it's not often done. You just take it for granted from the, uh, data sheet, but if you want to verify this, you design in your own amplifiers, doesn't have to be differential probe, could just be any differential, uh, amplifier, um, or even like a regular, you know, op amp, regular amplifier.

**Dave Jones:** You might have the common mode rejection, uh, ratio. By the way, um, it's, uh, you know how I mentioned the resistor dividers are the main contributor to that. If you try and actually build up a circuit to measure the common mode rejection ratio of your op amp, for example, you've just designed a new op amp, you know, you work at Analog Devices or whatnot and you want to

**Dave Jones:** measure the common mode rejection ratio, well, it's going to dominate via the resistors there, but you can actually do a technique, maybe I'll do a second, leave it in the comments if you want to, uh, see a video, um, showing where you can actually, uh, eliminate the resistors in the circuit, um, from the measurement and you can just get the pure, uh, common mode rejection ratio of

**Dave Jones:** the amplifier. You can do this using a difference, a step difference in the power rail voltage. So, that's also how you can, uh, do it as well. So, it's just an interesting, uh, tidbit, but there you go.

**Dave Jones:** Common mode rejection ratio. If you enjoyed it, give it a big thumbs up. As always, discuss it down below and subscribe to EE blog too and my Odyssey channel where there's exclusive videos over there.

**Dave Jones:** If you want to see a couple of these, I think I've got two exclusive videos of the Rohde & Schwarz oscilloscope, why it's actually been delayed, um, cuz we had to actually, uh, swap it.

**Dave Jones:** So, anyway, exclusive videos over on my Odyssey channel. Uh, if you want to have a look at what happened, uh, there, but yeah, this is really sweet, um, scope.

**Dave Jones:** So, yeah, uh leave leave it in the comments. Do you want to see a teardown or do you Do you want to see a feature review? It's got so many features, but I can show you some of the uh really cool stuff in this.

**Dave Jones:** It's going to be good. So, anyway, catch you next time.
