---
video_id: 7v-P75MOZ5o
title: EEVblog #1228 - Do Digital Scopes Have REAL Verniers?
url: https://www.youtube.com/watch?v=7v-P75MOZ5o
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video, which I'll link at the end of down below, if you haven't seen it, we looked at the advantages of using the vernier control on your oscilloscope. This is when your signal might be too big to display on your

**Dave Jones:** screen like this, and therefore you're not able to it's outside the ADC range of your uh a converter front end, and it can't do measurements on that. And if you turn it down like this, you're wasting a lot of

**Dave Jones:** your analog to digital converter range on there, and you may not get as good a resolution or accuracy on your uh automated measurements and things like that. So, you would what you do is you hit the vernier control like this,

**Dave Jones:** fine adjustment mode, it says variable down there on the scope, and you can bring it so the waveform's just within full scale range like that, and you take advantage maximum advantage of your analog to digital converter range, all

**Dave Jones:** those eight bits that you've got available. If you've got a fancy pantsy scope, 10 bits or whatever. So, that's just a handy little tip to get that, but a lot of people ask the valid question, do these modern scopes, when you

**Dave Jones:** actually put it in vernier mode like this, that is this just like a software trick? Does it actually do the vernier adjustment? Does it actually change the gain in the hardware on the front end? And hey, let's answer that

**Dave Jones:** question right now by doing a teardown and some probing to find out if a modern scope like this Siglent SDS 1104 XE actually does do real hardware gain control just like the old school analog scopes. So, we showed in the previous video that the

**Dave Jones:** you can the results you actually get from doing this do seem to be real. So, it does seem to be uh you know, doing something useful, but is it actually doing that in the hardware or is it some sort of you know,

**Dave Jones:** software trick and then it's it's giving you some extra, you know, warm and fuzzy software resolution where it really shouldn't be there. Well, there's only one way to find out. Let's tear down a scope and probe up its clacker. Right,

**Dave Jones:** so I have actually taken apart this poor victim Siglent 1104 XE and I have probed right up its clacker and we can actually see and probe the waveforms of the vertical gain amplifier front end. But, let's take a quick look at the

**Dave Jones:** tear down of the front end of this thing and see what actually, if there is a digitally variable adjustable gain type circuit or chip in there. All right, so let's take a look inside the front end here. This is from my tear down photos.

**Dave Jones:** I'll have to link in the tear down video if you haven't seen it. This is the bottom side of the analog front end. It's shielded as you can see. There's just a bunch of and diodes on there and a bunch of passives. Not much

**Dave Jones:** else. So, it ain't there. But, if we have a look at the top side here and comes in on the left, that's the BNC there and it's got the requisite relays and some trimmer caps we can tweak it. But, if we have a look at some

**Dave Jones:** of the chippies in here. This one up the top is a 74 HC595 serial to parallel interface so that they can they don't have to have all the lines coming from the main controller over to the front end. Anyway, what

**Dave Jones:** we're interested in is this one here. Look at this. 8370. That's an Analog Devices 8370. Let's have a look. Here it is. And a low frequency to 750 MHz digitally controlled VGA. That's not video graphics adapter. That's a variable gain amplifier.

**Dave Jones:** And it's got programmable low and high gain, less than 2 dB resolution. Uh so, you can adjust from -11dB to +17dB gain, two different uh ranges, 6dB to 34dB. So, I can go to -11 to +34dB gain. And it's a differential input,

**Dave Jones:** differential output. And as you can see, it's got an adjustable preamp here and adjustable uh transconductance, which is uh the gain here. And it's you know, claims to be have like precision uh gain range. And it's got a serial 8-bit

**Dave Jones:** digital interface, which we're going to tap into to see. And that's that's basically all it is is it's a digitally controlled or digital gain controlled amplifier. Perfect for differential ADC drivers and oscilloscopes and stuff like that. I'm surprised they don't actually

**Dave Jones:** have oscilloscope there as one of the uh functional things for it. Anyway, a low-cost digitally controlled variable gain amplifier that provides precision gain control, uh low noise, excellent distortion performance, wide bandwidth, uh for modern receiver designs, etc., etc. And here's the magic word, a

**Dave Jones:** vernier 7-bit transconductance stage provides 28dB gain range at better than 2dB resolution and 22dB of gain better than 1dB resolution. So, you can the software can potentially adjust the gain of the front end that goes into the ADC

**Dave Jones:** in 1dB resolution step. So, as you adjust that vernier, that fine control, in theory, if the software supports it, it can adjust this, but we won't know until we actually measure it, whether or not it's actually sending the codes

**Dave Jones:** using the vernier. It's obviously going to be using uh these particular uh different gain stages for the different fixed millivolt ranges, you know, 1 V per division, 100 mV per division, 10 mV per division, etc. It's going to be switching all those ranges,

**Dave Jones:** but does it do it on the vernier? It's more than capable with this chip. Theory of operation is fabricated with the 25 gig silicon bipolar process for those playing along at home, and we're seeing the block architecture. This

**Dave Jones:** transconductance stage is digitally programmable gain, and this is quite complex, actually, how it has different performance characteristics depending on the particular range that you're in. Less than 1 dB resolution, less than 2 dB resolution. It's got two different

**Dave Jones:** gain stages, and then a programmable transconductance amplifier inside that. And the gain's actually load dependent, too, for those playing along at home. But here's the digital interface. It's a simple 8-bit digital interface. It just accepts a single word

**Dave Jones:** here. By the looks of it, that's it. There's a latch signal that goes low. When that does, it has a clock and just a data stream on the input starting with most significant bit to least significant bit. So it looks like you

**Dave Jones:** only feed in the 8 bits, and that's it. You can configure all the gain stages. There's a typical example and here is the gain code that we're interested in. I expected to find like a table of like okay, this is 1 dB

**Dave Jones:** for each bit or whatever, but it's actually a formula here, which you got to put in. The total gain is the gain code with the vernier plus a pre-gain most significant bit. And it actually, you know, it comes out at

**Dave Jones:** X amount X.XXX amount volts per volt. So obviously, you've got to calibrate these ranges in software, and that's what Siglent would do at the factory or you could do in some sort of user calibration or something like that.

**Dave Jones:** But once you've done the fixed ranges, then the other ranges would be known steps, so you wouldn't have to recalibrate that. But yeah, that's what it does. You just put in the value of your register. The first most significant bit is whether or not

**Dave Jones:** you're in the high gain range or the low gain range, but after that it's a seven-bit or 128-step uh gain stage. So, yeah, it's more than capable of doing this. So, let's uh hook up the uh scope and see if it actually

**Dave Jones:** does adjust the gain of this thing in the vernier stage. Right, so now comes probing this thing. Unfortunately, uh it's a bit of a pain in the butt cuz it's a 0.65 mm TSOP package and that's, you know, too small to get your

**Dave Jones:** traditional like uh easy hooks in there on the individual pins like you can on a regular SO package, so that's not going to cut the mustard. And if you just got the one probe, of course, you can get in

**Dave Jones:** there and touch it just if you hold the uh tongue at the right angle, but then if you slip, you got to short the pins out. And you can potentially use like a uh like a stand like this, one of these

**Dave Jones:** uh flexi stands, and you can put your probes in here like this, and you can muck around, and you can precision locate them on there, but then they spring back, but they, you know, you can do that kind of thing, but then the

**Dave Jones:** problem is we've got to operate the controls. So, even the most minute uh thing in this, let alone getting three of these probes on there, that's just going to be a complete no-show. So, we've got no option but to actually uh

**Dave Jones:** solder some wires onto there, and then you put some uh strain relief on here cuz usually those joints aren't going to be that strong, especially like it's really difficult to get in there. And the so, you know, the joints might be a

**Dave Jones:** bit how you doing, but as long as they're touching, so we just take the stress off those, then we just have some uh flywires coming out we can touch with our regular probes, uh either scope probes or logic analyzer probes. Beauty.

**Dave Jones:** I've got uh three signals. Channel one's data, channel two's clock, channel three is the latch signal, and I've got it set up for normal triggering here. You don't want it in auto mode because then you'll just uh continually get your signals and

**Dave Jones:** you don't want to always be single shot capturing this. So, you want normal mode so that you can run it and then every time you get a signal like this, bingo, it triggers like that and we can see it

**Dave Jones:** over here. So, every time we change our volts per division setting, we will get a Yeah, uh you can see it change a little bit over there, but every time we change it, we will get a new trigger over there and

**Dave Jones:** ordinarily, it's not actually triggered and I'm actually triggering from the uh latch signal. So, when it goes negative, that's the only time that the data is actually valid to that particular chip. So, you can see here that there's

**Dave Jones:** multiple packets of uh data and clock here, but only one of them is going to be accepted by that chip when that latch goes negative. So, that's the one we want in there. You can see it. It stays

**Dave Jones:** uh low for a long period of time, but it's only sending one little packet of data to that particular chip. The reason uh there's all this other uh stuff which we uh ignore over here. In fact, let's go right out on the time base. Seven

**Dave Jones:** different packets there every time we change the volts per division setting. So, it must be updating all of the different channels even though we're only changing channel one. So, that may not be the smartest thing to do in software, but

**Dave Jones:** the uh chips that aren't latched will just ignore this. So, obviously, there's multiple chips on that same bus and that's how you do it. That's why you got the uh latch line. So, I'd say it's uh Yeah, it's probably sending out data to

**Dave Jones:** all the uh chips and that just saves uh lines, of course. So, and you don't have to have a a discrete set of uh lines going to each chip. So, there it is. There's our data. There's our clock

**Dave Jones:** going into that chip and if I then change the volts per division, you can see our data is definitely changing. So, that's it. Sorry, you can't see it on the screen. Take my word for it. 10 volts per

**Dave Jones:** division. 5 volts. 2 volts. 1 volt. 500 millivolts. 200 millivolts. 100. 50 millivolts. 20 millivolts. 10 millivolts. 5 millivolts. 2 and 1 millivolt. Oh, no, we get a 500 mic. You can see that there's no difference. And now I actually switching between 1

**Dave Jones:** millivolt and 500 microvolts per division. You can see that there's absolutely no difference in the data whatsoever. So, we're not getting any extra gain there. All we're doing is software magnifying that in software. So, it's not a true 500 microvolt scale.

**Dave Jones:** Um what we want what we want to know is, okay, the data changes. I don't care what the data is, okay? It's in there. It's choosing uh the particular register settings as we change the uh millivolts per division. It's choosing one of those

**Dave Jones:** fixed gain settings that it's actually uh calibrated for um which will match the range of the analog uh to digital converter as best it can. But, what we want to do is if we press the vernier here, what happens? So, I'm going to put it

**Dave Jones:** fine adjustment mode. Oh, yeah. 494. You see it's updating every time Oh, 482. Look at that. It's jumping. It's changing. It's changing. So, it's definitely doing something. It it really is changing that data. It Oh, actually every step. I don't

**Dave Jones:** think it's actually repeated a step, has it? So, it looks like it's increasing probably like a 1 dB gain uh for each time we adjust that vernier. That's interesting. So, to know what the exact range is, you'd have to decode the

**Dave Jones:** data here. There are some combinations of uh code where it doesn't change at all. Like I'm flipping between those two there and this data is exactly the same. So, it's obviously gone, "Well, I don't need to change the range." There you go,

**Dave Jones:** for that one there as well. Now, I initially thought this wasn't actually counting up in binary and that was strange because the formula is the gain bit, which is the first one here, which is always zero by the looks

**Dave Jones:** of it when we're in the vernier. You'll notice how that those some I just changed it by one vernier position. You notice how it actually had this extra pulse here. This is actually nothing, but that's not going to count because it

**Dave Jones:** only registers the data on the positive edge here. Is so, the most significant bit, which is the first one, is always zero. So, therefore, it's always in low gain mode. So, the rest of the So, you can ignore that if that just start pops

**Dave Jones:** up. It might just be a quirk of the software algorithm that they're using. That's very common. There's nothing wrong with that as long as the data's valid when that clock signal comes along. So, if I adjust that vernier

**Dave Jones:** again, sorry it's jumping around cuz there does seem to be a bit of variable time in there. Once again, I'm not sure why that's doing the real-time operating system the scope has to do stuff. I guess Okay, so let's start at this one

**Dave Jones:** perhaps. We've got 1 1 1 1 there. So, we've got four ones and then we've only got the one one at the end. So, it skips through the 1 0. Then we've got 1 0. So, if you look at those four bits there, it

**Dave Jones:** went from 1 1 1 1 to 0 0 0 1. Now it's 0 0 1 0. And if we keep going, 0 0 1 1. So, it is See, it is Yeah, it is kind of counting up. Yep, and that's what you'd expect

**Dave Jones:** because it needs to increment a little bit again each time. I'm actually surprised that it sort of like fine compensates the range almost every turn of that vernier. That's That's really quite remarkable. I expected much coarser, you know, gain control than

**Dave Jones:** that. And of course, you rely on the gain and they can't individual There's no way at the factory they've individually calibrated the gain on each one of these vernier steps. So, they only do it on the particular course

**Dave Jones:** sequence like this. They So, they just calibrate each one of those ranges and then you're relying on the fine software steps, the accuracy of the steps within side the variable gain amplifier itself to give you your calibration on your

**Dave Jones:** fine vernier control. And there's nothing wrong with that. That's exactly what I expected. So, there you go. I hope I answered that question is do modern digital oscilloscopes actually have digital vernier control in there? Do they actually adjust the gain? And in

**Dave Jones:** the case of the Siglent, the answer is yes, it does because it's got a pretty funky variable gain amplifier in in there designed for just such a vernier control. But, not every digital scope is going to have this. Like the Rigol, for

**Dave Jones:** example, I can't find in the front end of reverse I had done a whole video which you can see at the end. It's really cool video of how to how to do reverse engineering essentially. And I reverse engineered the front end of the

**Dave Jones:** Rigol DS1054Z and it doesn't have such a variable gain amplifier, but it does have some digital gain control with inside the analog to digital converter chip itself. But, yeah, that's not as good as this. So, effectively, I don't think the Rigol

**Dave Jones:** does it, but the Siglent does. About other scopes, I have a look at the teardown. Leave it in the comments down below. Well, I've done various teardowns of various oscilloscopes over the years. You can go look over my high-res photos

**Dave Jones:** on my EVblog Flickr account. You'll be able to see the front ends for yourself of various scopes and see if there's a variable gain amplifier in there. See, there you go. Um it's not just a software thing. It's actually doing real

**Dave Jones:** hardware gain. So, there are advantages to making your waveform, using your vernier control, and making your waveform as large as possible when you do measurements cuz it's got more bits of the analog-to-digital converter to work with. And the gain

**Dave Jones:** inside the variable gain amplifier is going to take care of your right calibration for you. Remember, um scopes like this are only a percent, you know, 2% accurate, stuff like that on their vertical. So, not not a huge amount of

**Dave Jones:** absolute accuracy, but hey, once your ranges are calibrated, you can actually do comparative measurements and things like that and get the resolution. And if you use more of your ADC range, then you're going to get more bits to play

**Dave Jones:** with and it's going to give you a more accurate, in quote marks, measurement. Anyway. Hope you like that. If you did, please give it a big thumbs-up and as always, discuss down below. Catch you next time.
