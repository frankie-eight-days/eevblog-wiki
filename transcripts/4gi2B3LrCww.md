---
video_id: 4gi2B3LrCww
title: EEVblog 1521 - CMRR Full Edit
url: https://www.youtube.com/watch?v=4gi2B3LrCww
source: youtube-asr
---

**Dave Jones:** Hi, in this video I'm going to explain what common mode rejection ratio is and actually how to measure it in this particular case of a high voltage differential probe here, but it doesn't have to be a high voltage differential

**Dave Jones:** probe available on the EV blog store by the way, discount coupon code down below, doesn't have to be a probe like this, any differential amplifier circuit be an op amp or a discrete transistor one, it will have a common mode

**Dave Jones:** rejection ratio. So, let's have a look at it. We're going to measure it with the brand spanking new Rohde & Schwarz uh four MXO 4 series scope here, 12-bit jobby, because oh, why not? It's beautiful. So, the common mode rejection

**Dave Jones:** ratio of a differential amplifier, in this case a differential probe, as the name suggests, is just the ratio of the differential gain of the amplifier divided by the common mode gain of the amplifier. And what is differential and

**Dave Jones:** what is common mode? Well, a differential amplifier measures the difference between uh two inputs here. There base essentially is no ground reference. It is a differential signal, and a differential amplifier will have a a gain of that differential signal.

**Dave Jones:** That's its job. If your differential amplifier has a gain of 10 and you put 1 volt differential across here, it doesn't matter where it is in the circuit, it's a differential voltage, doesn't matter about the ground reference, it'll multiply that by 10,

**Dave Jones:** and that's its differential gain. Now, you divide that by the common mode gain. Now, what is the common mode gain? Well, instead of the differential voltage across here, it is an external voltage applied to both of them at the same

**Dave Jones:** time. So, in this particular case, okay, we've got these long leads here, and we could have like external uh either capacitive coupling or EMI coupling into the probe like this. So, they're basically getting onto the probes in the same way. And this is why

**Dave Jones:** the wires are twisted like this. And if you're measuring a differential signal, it means any external noise or interference will actually in should, in theory, um apply to both uh wires at the same time. So, it's an external reference. In

**Dave Jones:** this particular case, referenced to the grounded output of our differential probe. So, the job of a differential amplifier is to amplify the difference between its positive and negative input while rejecting all of the signal or much of the signal as it can that is

**Dave Jones:** applied commonly to both of these wires. So, that's why it's a common mode rejection ratio. So, in theory, your differential amplifier should have an infinite common mode rejection ratio. It just measures difference here and rejects everything else. It has no gain

**Dave Jones:** at all of any common mode signal being picked up by both wires. But, in practice, uh no, that's not going to happen. Just the design of the amplifier itself and most importantly, the matching of the input uh resistor uh network in here.

**Dave Jones:** And I've done a teardown um of a high-voltage differential probe down like this. I'll link it in up here and down below if you haven't seen it. And just the matching between the resistors on here is um like pretty much

**Dave Jones:** determines the common mode rejection ratio of this probe. Because usually, like the op-amps used inside here, they're usually pretty good. They're going to have like a rejection ratio of like, you know, over 100 dB or something. Whereas, the resistor divider

**Dave Jones:** drops that down to like 40 or even less. Now, a product like this HVP 70 differential probe, it'll typically have a common mode rejection ratio figure measured at various spot frequencies. Maybe, if you're lucky, you might get like a response uh curve of common mode

**Dave Jones:** rejection ratio because it's going to vary depending on the frequency. So, it's going to change. So, they typically, here's the uh values for this HVP uh 70. And it gives us four spot values there. And the ratio, you can

**Dave Jones:** see, is, you know, like at 10 MHz, minus 40 dB. And it is usually given in a dB figure, but it doesn't have to be, because it's just a ratio. So, you could just use the ratio figure. And the

**Dave Jones:** interesting thing about this is that the common mode rejection ratio is, as I said, the differential gain divided by the common mode gain. And that actually comes out at a positive value. So, why is the data sheet negative? Well, it's

**Dave Jones:** kind of there's no like standard for this kind of thing. So, you just sort of have to like understand that when you're talking a negative number, in this particular case, minus 60 dB uh common mode rejection would be better than

**Dave Jones:** minus 40 dB. But if you had it if you specify it as a positive one, as you might get on, say, a uh op-amp data sheet, here's an example, uh you would get a the higher the value is going to

**Dave Jones:** be better. So, that positive or negative thing, just a little trap for you young players, just be aware of that. Right, so how do we measure the common mode rejection ratio and verify the common mode rejection ratio of this probe?

**Dave Jones:** Well, what we've got is a our differential input like this. First thing you want to do is, as I said, you want to twist the wires like this so that any uh external noise is equally picked up on both. And then, you need a

**Dave Jones:** signal generator. In this particular case, this uh new Rohde & Schwarz MXO 4 can go up to 100 MHz, so very nice. So, we can actually measure the 100 MHz uh this one's got a bandwidth of 100 MHz

**Dave Jones:** this mixed mode jobbie, which we'll measure as well. And then, we want to feed the output of the sig gen into a 50-ohm terminated load so that uh we don't have any transmission line issues whatsoever, no reflections causing

**Dave Jones:** problems. I've done videos on that and how you can goof that up in noise measurements and stuff like that. So, I'll link in that video up here and down below if you uh haven't seen it. So, here I'm using an external 50 ohm uh 2

**Dave Jones:** watt termination, a series termination, even though the scope has a built-in uh 50 ohm termination, but if you look down here, you could actually come a cropper because this is only like got a half watt rating. It's less than 5 volts RMS.

**Dave Jones:** Just, you know, you don't want to blow up your scope when you do something like this cuz you want to use a high as high a voltage as uh possible. In this particular case, we could do it cuz

**Dave Jones:** we're less than 5 volts RMS, but in this particular case, I'm just showing you it's better to use a high-rated uh external uh terminator just so you don't blow up your really expensive, beautiful, shiny scope. And then, we're

**Dave Jones:** just uh tapping off right across this uh 50 ohm terminator load here. So, here's the negative uh terminal and here's the positive terminal. So, what we want to do is connect both of these inputs together, short them together, and

**Dave Jones:** connect to the positive input like this. Why the positive input? Because it means that we're applying a voltage relative to the output here cuz the output is ground referenced like this. So, we're actually uh referencing it to the

**Dave Jones:** output. So, we're effectively feeding that signal generator voltage into both of these leads, i.e., a common mode signal relative to the grounded output. Because if you remember, all the grounds on your scope are all common. So, this is the input signal and the output and

**Dave Jones:** they're uh effectively joined. They're common. So, what happens if I just connect one of these to here? Well, you saw it. The green signal's our output, the uh yellow is our input there, and our green signal we it's actually going

**Dave Jones:** to give us an an output. Here it is here. It gives us a nice, clean output like that, okay? So, our differential uh probe is cuz this one's just flapping around in the breeze, right? Doing nothing. And you'll see that just jump

**Dave Jones:** all over the place there and if I touch it, look at that. Like we're picking up all sorts of crap, right? But and you'll get the same exactly the same thing if you connect the negative up like that,

**Dave Jones:** right? The exact same thing will happen cuz this is a differential amplifier. It it doesn't care. Um it just you're just unbalancing that input. But if you connect both of them on like that to the same point, then bingo, we've got a

**Dave Jones:** really small signal. So this probe isn't perfect. It's got a common mode rejection ratio. So there you go. It's there's a signal being amplified even though that input is completely shorted. And you'll notice that goes away if we

**Dave Jones:** don't connect up to that, okay? There's our ground there, so we've just got like the inherent noise of that amplifier and it doesn't matter what I do to the probes here, but this one if we hook it back up, you'll notice if I start

**Dave Jones:** playing with those probes, right? Things start happening, okay? Like, you know, it starts like being influenced because like we've got these long leads here. That's why a differential probe with like like really shorter leads is better, but these have them most probes

**Dave Jones:** have them built in though unfortunately. So what happens if I untwist those leads like this and so we're going to get the same signal, but we have potentially have more variation. Check it out. You actually get huge differences like if I

**Dave Jones:** like take my hand away from that, right? you can get large differences like that. So if you don't twist the leads and keep that common mode signal, right? You can completely screw up and come a cropper on your

**Dave Jones:** measurement, whether it's a probe or whether or not it's a differential amplifier op amp or discrete transistor circuit, whatever it is you're measuring. Yeah, the signal conditions you're measuring here cuz we're talking about very low level signals, it's

**Dave Jones:** really important. Now that I've explained what we're doing and I've shown you the setup here, there's no reason to look at this anymore. So, I'm going to actually go over to a remote desktop view and uh we'll do a direct

**Dave Jones:** screen capture of this. It'll be just nicer and because I can. Ah, isn't this schmick? Look at this. Ethernet remote control. It's got a built-in web browser, so we can just go to the IP address and bam, we're in. So,

**Dave Jones:** we can actually we can do some like configuration and file manager stuff, but let's just go to full screen here and we can either get the uh with the front panel or just the screen like this, but we'll include the front panel,

**Dave Jones:** so my ugly mug's not covering too much. So, channel one, the yellow one, that's our uh sig gen there. We've got uh 1 V per division, 50 MHz bandwidth cuz you do want a uh bandwidth limit and this

**Dave Jones:** scope actually has some cool software bandwidth uh limiting options in it um which might see later. And uh one one big ohm uh input uh DC coupled, DC or AC, it doesn't matter. And channel two also the same uh 50 MHz uh bandwidth

**Dave Jones:** here, 500 microvolts, but uh yeah, we've No, let's just leave it on uh 2 mV there, shall we? Now, you can see we've got a real fuzzy wuzzy waveform here. Now, of course, this is a uh 12-bit scope. You don't necessarily need a

**Dave Jones:** 12-bit scope for, you know, this particular application that we're doing uh right here, but 10 or 12 bits more betterer, but we can actually go more than this. So, you can actually see up here up the top it's telling us uh to

**Dave Jones:** just that's the basic 12-bit uh but we can go higher because if I get my ugly mug out of here, we can see that I've got a HD mode down here, a high definition uh mode and we can actually

**Dave Jones:** set that on Whoop. There we go. We instantly set it on and you'll notice that our 12 bits went to 16 bits up here. And notice and watch it watch this. This is really cool, right? You notice how um history mode up here. See

**Dave Jones:** that number history? It's taking half a million um history samples, not histogram, but history uh samples. That's what the history button down in the bottom uh corner here, is. Now, if we turn this off, it'll reset that and

**Dave Jones:** look at how quickly it captures. Boom! Look at that, right? A million A million waveform captures um just in a couple of seconds there. This scope's actually capable of 4 million waveform capture per second, and you might see

**Dave Jones:** this in an upcoming uh review video. Leave it thumbs up down below. Comment um yeah, I have already done an unboxing video. I haven't edited it yet. There were delays, but And then if we turn that off, it'll go back to 12 bits.

**Dave Jones:** Boom, half a million like that. So, yeah, it's really quick. Really schmick. So, let's turn HD mode on there. But before we go ahead with that, I'll just mention the uh signal gen here. Now, uh you want this to be as high a amplitude

**Dave Jones:** as possible because the output signal that you're actually trying to measure um that common mode signal is really low. So, the higher the input signal, the better. So, I've gone up to the maximum uh amplitude here of uh 5 V

**Dave Jones:** peak-to-peak here, and uh we've got a frequency of 10 MHz because that's just the uh uh you know, a typical figure we've got in the data sheet which we want to try and uh verify. So, we want to clean this up a bit more, so let's do

**Dave Jones:** some averaging. So, we'll go up to the uh acquisition up here, and we're actually uh in sample mode, so we'll go down here to average mode, and then boom, we can do like 40 averages, something like that. We can take the uh

**Dave Jones:** time base out a bit like that. You notice how it gets a little bit like chunkier when it goes I guess that's a feature. So, we've got a decent number of signals. You can see that our average there we've got 40 averages there, and

**Dave Jones:** uh that's just cleaned that up a tad. can see how we are dealing with the wobblies down here cuz as I said, the test setup is everything. So, if you can shield it and keep the leads short and

**Dave Jones:** uh make sure that they're twisted and everything else, it's going to be uh better. But let's see if we can uh use this to get our uh figure. So, what we need now is to compare the input signal

**Dave Jones:** to the output signal. That'll give us our common mode rejection ratio. In this particular case, uh Uh, you saw on the data sheet that it's actually negative here. So, at 10 MHz it's minus 40 dB here. So, we want to flip that around

**Dave Jones:** here to give the output divided by the input. Now, to measure this uh, ratio between input and output, we can either measure the peak-to-peak value or the RMS value. Doesn't matter. RMS is, you know, it's better, it's more accurate. But, you

**Dave Jones:** might think that we use this RMS value here. And uh, that 1.4 mV like that. But, I've done a video on this where that RMS value, that includes any DC offset component. So, that's not quite what you want. So, let's go into the

**Dave Jones:** measurement menu here. Unfortunately, they don't have it in the basic category. You've got to go down to the what the vertical there. There you go, standard deviation AC RMS. I've done an entire video on that. So, we want channel

**Dave Jones:** one. We should be able to drag that to like a trash bin or something. I should be able to right click on that and actually delete. You know, the user interface, come on. But, I can actually go in here

**Dave Jones:** like this. I can double click on that and I can choose specific type AC RMS like that. I do like how every menu here you can actually set the transparency with the slider bar there. That's kind of like really groovy. And you see how

**Dave Jones:** in this menu here it does actually have a trash can down here. But, it's like and then you've got to select which one you want to trash can but I can't like no, no, no. You know, well, you either

**Dave Jones:** like that or you hate it. So, let's actually get a few waveforms on screen here so it's a bit more accurate. And once again, we can turn the statistics on there. Come on. Can't double click to get into the menu.

**Dave Jones:** By the way, one little thing I wish they had is that where is the the signal generator's on? Why is that not on the screen somewhere? It should be somewhere. Look look look at all the dead space down here. I shouldn't have

**Dave Jones:** to go into the sig gen here to actually see that that's uh 10 MHz there. It should be on the screen somewhere. Please, Rohde & Schwarz, add that. See, they've got all the other channels here that when they're not on, they're over

**Dave Jones:** here, right? But the sig gen's on, so the sig gen should actually pop up over here as one of the boxes to tell you what that the sig gen is A on and B what the settings are. I got I mean, it's just

**Dave Jones:** inconsistency there. Oops, I had the uh wrong bandwidth there, so we have to use the 50 MHz uh bandwidth here cuz we're measuring 10 meg 20 meg is a bit close to the frequency. You want to be a bit

**Dave Jones:** more than double above like that. So, you know, 50 is 50 is not a bad value. So, we get our confuser out here and we look at the RMS value here. Don't be confused by Remember how I mentioned

**Dave Jones:** standard deviation before? You got to watch my standard deviation video. The standard deviation here is not referring to the AC RMS. It's referring to the standard deviation of the standard deviation AC AC RMS signal. So, it's like it is very confusing. So,

**Dave Jones:** yeah, don't come a cropper there. Anyway, so we need to uh get our confuser out and uh 883 microvolts. So, I or 882 microvolts. We won't get any more precision than that. Uh divided by our input because we want

**Dave Jones:** a negative uh number. So, 1.75 V. Then we want to take the log of that uh and then multiply that by 20, not 10 cuz this is a voltage. So, we get minus 65 minus 66, basically. Hmm. That doesn't sound right.

**Dave Jones:** Cuz our spec over here says minus 40 at 10 MHz. Why is it way, way better? Way, way better. Hmm. Because this CMRR is what's It's input referred. It's referring to the input of the actual uh amplifier in this case inside the uh

**Dave Jones:** probe here before it gets gained up by the amplifier. Now, if you noticed in the video before, we're in the uh 10:1 division ratio setting. So, there's a gain of 10 in there. So, we have to account for that uh gain of 10 in here

**Dave Jones:** in our dB figure. Now, you know, a good data sheet, they should actually specify that and tell you exactly what it is. Now, this is a good marketing trick because marketing can make the common mode rejection figure sound a lot better

**Dave Jones:** just by saying, "Oh, that's input referred." instead of like output referred or you know. So, just don't get caught by that, okay? So, in this particular case, uh our times 10 uh probe over there, times 10 of course in

**Dave Jones:** dBs is 20 dB. And times 100 would be 40 dB. Times 1,000 would be 60 dB. Cuz of 20 dB for each order of magnitude step like that. I've done a video on dBs. And that's just a cool nature of uh dBs. So,

**Dave Jones:** we have to actually add on uh 20 dB to that. So, um 66 minus 66 dB becomes minus 46 dB. So, yes, it does actually meet that specification. So, it beats it by 6 dB actually. Not too shabby.

**Dave Jones:** But, this is only a typical figure. So, you know, yeah, but we're actually doing better than that. So, let's repeat this at 1 MHz. So, it should get better by about uh 10 dB. So, got this 46 here.

**Dave Jones:** Maybe we'll get 56, will we? Let's see. So, we want to go to 1 MHz on our sig gen there. And we do want to change the lower the bandwidth of our input here. So, we'll go in there and we'll just

**Dave Jones:** drop that down to say 20 meg there. So, you know, reasonable margin, but you don't want to be too high. And then we've got to change the time base. Otherwise, we won't get enough waveforms on there to give us a reasonable

**Dave Jones:** value. So, there you go. 423 microvolts divided by 1.8 volts there. Uh and log * uh 20 = -72. Yep, there you go. Um so, you subtract or add 20 dB to that. So, it's -52. So, there you go. This typical spec is

**Dave Jones:** -50. We're getting -52. Yeah, comes out. And let's try 20 kHz, shall we? I think it's come out at -52 dB. It's basically the same as what it was at 1 MHz. So, um our situation has not improved. So,

**Dave Jones:** why is it a good 8 dB outside of spec there at 20 kHz? Don't know. Um I can't think a reason why. So, what I'm going to do here is I'm going to go into acquisition, and I'm going to change the

**Dave Jones:** band with the acquisition bandwidth. Now, here's a cool feature of this Rohde & Schwarz scope. We can actually define a software bandwidth, and we'll see later how cool this is. Let's set say 100 kHz like that. Boom! Look at that.

**Dave Jones:** So, we can now software clean that up really schmick, really nice. So, we can set any arbitrary software bandwidth limit on there. So, you put but the hardware over here, you can see it's put it down here as 100 kHz, okay?

**Dave Jones:** It's overridden the bandwidth of the hard the hardware bandwidth of the front end, which is 20 MHz. Now, it's overridden that, and it's put it down the bottom corner here, and it's put it on the channel as 100 kHz. So, so yeah,

**Dave Jones:** hardware bandwidth 20 MHz, effective bandwidth 100 kHz there uh because we've put in a software filter like that. So, that's cleaned that up very schmick and it is slightly dropping there, but you know, like 404 405 microvolts divided by 1.79

**Dave Jones:** log * 20. Um we're still and you add on the 20 dB minus 52. 9, so yeah. Doesn't meet the spec. But if we try and measure it down at 50 hertz here, which is supposed to be minus 80 dB, so I

**Dave Jones:** generally like it it's 20 dB increase over 20 kilohertz. You can see that yeah, it's it's gone to nothing. Again here, 500 microvolts per division and there's nothing there. I mean, we can take that figure and punch it into the

**Dave Jones:** calculator, but like there's just nothing there. We're basically measuring the RMS value of the noise at this point. Anyway, you can see the process there. That's how we can measure the spot frequency. Now, how can we get a plot over frequency? I'm glad

**Dave Jones:** you asked. We can do this using if we go into apps here, ta-da, one of the things it's got is FFRA or frequency response analyzer. So, let's open this bad boy up and yeah, we can get a plot of this over

**Dave Jones:** frequency and we can also get phase as well. So, we're going to put our stop frequency in here of 10 megahertz and start frequency. Yeah, we can actually start down at that 50 hertz figure. Yeah, we can't actually measure

**Dave Jones:** that. So, points per decade, I don't know, let's just have two points. This is not like total cuz you can have total in there. Just two points per decade like that. Whoop, value out of range. Why? Looks like the minimum we can have

**Dave Jones:** is actually 10 points per decade. That's kind of well, it's a lot. So, we set up our input is channel one, our output is channel two, 50 hertz to 10 megahertz. Amplitude as you once again, you want the maximum uh amplitude and we're good

**Dave Jones:** to go. So, we should be able to now hit run on this. Now, watch down in the bottom corner down here as it's adjusted, it's set to AC and then it's adjusting the range all in real time. It's adjusting that and you can see it's

**Dave Jones:** slowly pro plotting here. It's only a small it's got a table and thing we could we could zoom that later if we really wanted to. Okay. But, 50 Hz 100 Hz, right? It's down in the noise. Anyway, here it comes. Here

**Dave Jones:** it comes. 10 kHz. So, it's starting to get out of the noise there. And we can adjust the range in a minute to actually see that and boom, we are done. So, can we actually make that whoop down

**Dave Jones:** like that? So, we can make that a bit bigger. Now, I don't think there's anything in here that allows us to set the offset there. be in advanced. Maximum phase measurement delay off uh real resolution bandwidth, no. Delay

**Dave Jones:** time, no. So, we can't like add in Maybe we can do some maths on that, but I'm not seeing it. Anyway, just remember that we have to add 20 dB onto these figures here. So, you can see that you

**Dave Jones:** know, around about 5 MHz there, it does really you know, it starts to sort of like uh you know, common mode rejection ratio gets worse. The higher that is the worse it is and you can see that the the red plot here is

**Dave Jones:** the gain. We're not too That doesn't matter for our common mode rejection ratio, but if we actually extend the bandwidth on that, we should be able to actually see a phase reversal. Anyway, we've got our table here. So, let's

**Dave Jones:** actually go to our 10 MHz. So, at 10 MHz here, you can see minus 64 which is minus 44.95. So, yeah, that is better. I can't remember what we got before. Is that more better at the 1 MHz? So minus 71 is

**Dave Jones:** minus 51 dB there. So yeah, that meets the spec of minus 50 as we saw before. And at 20 kHz, 22 near enough, it's minus 71. So minus 51. Once again, yeah, we just don't have the ability to

**Dave Jones:** measure that low really. So it's kind of like the maybe the limitations of the hardware measurement hardware that we've actually got here. We're just We're just not getting that. So if we go up to the full bandwidth here, 70 MHz of this

**Dave Jones:** probe, let's rerun that again and see what we get. I'm not going to go low frequency this time. So I'll start that at uh 100 kHz, shall we? So it's auto ranging each time it actually takes these samples, which is really quite nice. So

**Dave Jones:** it's maximizing its dynamic range there. And it's also adjusting its bandwidth as well. You'll see that the Yeah, just jumped from 1 to 2 MHz, 3 MHz, see? So it's actually software adjusting that bandwidth. This is really cool. This is a very good

**Dave Jones:** frequency response analyzer. So we're looking for the phase response to actually uh reverse here. Oh, yep. There it is. There it is. Hey! That's totally expected. Totally expected. That's a normal amplifier behavior. Not just a differential amplifier, it's

**Dave Jones:** normal amplifier behavior. So expected that. But once again, phase doesn't mean anything here. But you can say that yeah, up it right up to 70 MHz, it's minus 41, which is minus 21 dB. So it's a fairly sharp rise after, you know,

**Dave Jones:** once once you get above that 10 MHz, that's why they don't give you a figure up at 50 meg or 70 meg. They Once again, marketing just you know, stop at 10 MHz. I know it's my probe, but I didn't make

**Dave Jones:** this data sheet. It was done by the manufacturer Sapphire, who's a Taiwanese manufacturer of probes. They're excellent, by the way. Um, they make some of the, you know, Rohde & Schwarz, um, LeCroy rebadge them and a whole bunch of other companies rebadge our

**Dave Jones:** sapphire probes. They're really good. Unfortunately, this video's been long enough, so I'm going to leave this, uh, Micsig, uh, probe. I'll leave that to a, uh, second channel video and I'll show, uh, the results from this one. So,

**Dave Jones:** that's how you measure common mode noise. I hope you found that, uh, interesting and informative and it's not often done. You just take it for granted from the, uh, data sheet, but if you want to verify this, you design in your

**Dave Jones:** own amplifiers, doesn't have to be differential probe, could just be any differential, uh, amplifier, um, or even like a regular, you know, op amp, regular amplifier. You might have the common mode rejection, uh, ratio. By the way, um, it's, uh, you

**Dave Jones:** know how I mentioned the resistor dividers are the main contributor to that. If you try and actually build up a circuit to measure the common mode rejection ratio of your op amp, for example, you've just designed a new op

**Dave Jones:** amp, you know, you work at Analog Devices or whatnot and you want to measure the common mode rejection ratio, well, it's going to dominate via the resistors there, but you can actually do a technique, maybe I'll do a second,

**Dave Jones:** leave it in the comments if you want to, uh, see a video, um, showing where you can actually, uh, eliminate the resistors in the circuit, um, from the measurement and you can just get the pure, uh, common mode rejection ratio of

**Dave Jones:** the amplifier. You can do this using a difference, a step difference in the power rail voltage. So, that's also how you can, uh, do it as well. So, it's just an interesting, uh, tidbit, but there you go. Common mode rejection

**Dave Jones:** ratio. If you enjoyed it, give it a big thumbs up. As always, discuss it down below and subscribe to EE blog too and my Odyssey channel where there's exclusive videos over there. If you want to see a couple of these, I think I've

**Dave Jones:** got two exclusive videos of the Rohde & Schwarz oscilloscope, why it's actually been delayed, um, cuz we had to actually, uh, swap it. So, anyway, exclusive videos over on my Odyssey channel. Uh, if you want to have a look

**Dave Jones:** at what happened, uh, there, but yeah, this is really sweet, um, scope. So, yeah, uh leave leave it in the comments. Do you want to see a teardown or do you Do you want to see a feature review?

**Dave Jones:** It's got so many features, but I can show you some of the uh really cool stuff in this. It's going to be good. So, anyway, catch you next time.
