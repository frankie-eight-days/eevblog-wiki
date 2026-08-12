---
video_id: ILIO5b1BliE
title: Why Use AA's Instead of 9V Batteries in Multimeters?
url: https://www.youtube.com/watch?v=ILIO5b1BliE
source: youtube-asr
---

**Dave Jones:** Hi, I thought I'd answer an EEVblog forum question cuz it's kind of a little bit technical and it involves the 121GW multimeter. The post is from a member called Ixzod. I X O D, something like that. So, thank

**Dave Jones:** you very much for your question. As why doesn't the 121GW multimeter use a 9-V battery? Why does it use four AA batteries in it? Wouldn't 9-V be nicer even maybe two 9-V batteries in series cuz this actually has

**Dave Jones:** a yep, a 15-V diode mode. And it's an interesting question. So, I thought I'd just take a quick look at it now. The what it comes down to is basically battery life of the meter. Yes, I could actually power this from a 9-V battery

**Dave Jones:** if I absolutely wanted to make it as tiny as possible. A 9-V battery or maybe four AAA's, for example, might be an option. In fact, the original design of this meter used four AAA's. And I was thinking about it. Hey, looking at

**Dave Jones:** how much current it was going to take. It was going to have Bluetooth and other stuff and you know, like true RMS converter and I thought hey, you know, battery life is important. I personally value a long battery life in a meter.

**Dave Jones:** So, I said, "Hey, can we actually fit in AA batteries into this thing?" And they came back and they said, "Yep, if we make it about I can't remember what it was a four or five millimeters thicker or something, we can squeeze in four

**Dave Jones:** AAA's instead of four AAA's." So, I went beauty, we'll sacrifice the thickness. And it is a fairly thick meter especially when you put it in the holster, but I think the extra battery life is worth it. Now, let's take a look. Why

**Dave Jones:** can't why wouldn't we use a 9-V battery? Well, the 121GW meter consumes about 5 milliamps or so Um, in normal operation. that's not data logging to the uh micro SD card or anything built in. And that is effectively constant current load

**Dave Jones:** because there's voltage regulators, and I've done this in a video somewhere, but I'll do a simple diagram. Here it is, right? If you've got right? If you've got your battery here, and you've got your voltage regulator here that's giving out In this case,

**Dave Jones:** I've actually got um three voltage regulators inside this thing. One is 4 V, one's 3.6 V, and one is 3.3 V for the internal arm processor in this thing. Anyway, three of them. It doesn't matter whether you have three or just one like this. Okay,

**Dave Jones:** the regulator in here uh there's like the adjust pin, the set pin, or whatever it is. There's basically zero current flowing down there, okay? There's basically zero current. So, all the current that flows and and you've got a fixed voltage on

**Dave Jones:** the load, and the load's doing the same thing all the time even though it's a complex load like a processor, it's doing the same thing all the time. So, a fixed voltage of say In this case, like 4 V for example, uh or 3.3 or whatever

**Dave Jones:** it is, um the load is fixed. So, fixed voltage gives you a fixed current. In this case, it's actually about round about 5 mA for normal operation. So, that 5 mA, if there's no current down there, then you must have

**Dave Jones:** 5 mA coming from your battery. So, it's effectively by the nature of linear when you power your device from a linear regulator like this, it's essentially a constant current load. So, 5 mA constant current from the battery. Now,

**Dave Jones:** if we take a look at a 9 V uh the best one you can get like Duracell Ultra Power without going to lithium or whatever, but the best alkaline one, um let's have a look. They actually have a

**Dave Jones:** graph here of Shame they don't actually show you this is constant current load, okay? Shame they don't actually show you a phi curve for 5 milliamps, but it's going to be in there somewhere and it's probably not going to be

**Dave Jones:** I'm not going to say it's not going to be halfway, but it's going to maybe at a guess you'd have to measure it. It might be 150 hours. Now you'd have in fact in the case of a 9-V battery, I could hook

**Dave Jones:** a 9-V battery onto this and it would work and you would actually get because our the lowest voltage the highest voltage regulator in this is 4 V, so it's an LDO, so it drops out at like 4.1 V or

**Dave Jones:** something. We could actually use go down right to 5 V and use the entire capacity of the battery, 100% capacity of the battery, which would be nice and we might get maybe 150 hours use out of it, but 150 hours

**Dave Jones:** on a modern multimeter is not really good enough. So and that doesn't matter whether you use the and that's the ultra. There's actually really very little difference between the ultra and just the regular copper top. In fact, if

**Dave Jones:** you have a look the yeah, here's their here's their curve over here. It's exactly exactly the same. There we go, 2 milliamps and 10 milliamps. They actually have Uh yeah, it's around about it's going to be the same. It's they're practically

**Dave Jones:** identical graphs on there. So it might be say 150 hours service life. Now the original triple A's, it wasn't too bad. So if we have a look at a regular copper top triple A, let's have a look. Once

**Dave Jones:** again, they have 1 milliamp and 10 milliamp unfortunately, so it's going to be somewhere in between there. It's not going like you might think oh, okay, it's going to be like 5 600 hours or something like that. Uh

**Dave Jones:** sorry, because the dropout voltage is going to be like I think it's 1.05 V or thereabouts. Um so we're like, you know, we're in this region here and if the curve is something like that, let's say it goes to 600 hours and the dropout

**Dave Jones:** curve is here, you're going to we might get maybe 350 300 to 350 would be my guess. I don't know. I haven't actually tried it at 5 milliamps. You'd have to measure it. But which is okay. There's nothing

**Dave Jones:** wrong with that. But I was I wanted and a lot of people asked for by the way during the development of this thing, can it use double A's? I'm sick of these triple A rubbish. I want you know, I use

**Dave Jones:** double A's for everything else. And I thought yeah, I want battery life in this thing. So I'm going to use double A's. So let's have a look at double A's. And let's have a look and surprise surprise, they actually give us a 5

**Dave Jones:** milliamp constant current graph. Sometimes you win. Look at this. And no, you do not get 700 hours cuz as I said, 1.05 volts cut out or thereabouts. And we got like it should get around about 580 hours or thereabouts. Now, we just did

**Dave Jones:** some long-term testing of these and it went for a couple of weeks. We actually had two meters. One was logging SD data due to a software glitch, it kept stopping logging which they fixed now apparently. But anyway, during our

**Dave Jones:** testing, so we didn't get proper testing of the SD card. But the one that just sat on the volts mode for two two weeks or whatever, we actually got a 600 hours and we used these Duracell Ultra Power

**Dave Jones:** batteries. So it was like it was basically bang on to what we expect. Of course it would be, right? And it's going to match this characteristic curve. So we basically got 600 hours. So that's a nominal battery life on a good

**Dave Jones:** quality alkaline cell for this. So I think it was worth it. So we could have powered it from a 9-volt battery. It would have changed the physical design because the 9-volts is actually quite thick when you're trying to include it.

**Dave Jones:** So you'd have to design your your PCB. Well, sorry. I forgot to even show you. Jeez, we've got a mix in there at the moment. It mixes some dead ones that we had and we only had two spares, so we

**Dave Jones:** threw in those just to get it working again. Um the two new ones. Um So, yeah, you could have the 9 volts, but if you whack it in the middle, the thickness is you know, I I think a 9 volts is

**Dave Jones:** actually thicker than a double A, is it not? There you go. We can have a look at the Yes, it is. What is it? You know, let's say 16 and 1/2 mm there. 16 and 1/2 mm. Look at the double A. There you go.

**Dave Jones:** 14 14 mm. So, it's a couple of millimeters thicker for the 9 volt. So, if you powered it from 9 volts, the meter would be as thick or thicker than using double A's. Now, of course, if you smartly design it with sort of maybe

**Dave Jones:** some recess PCB cutouts, but the PCB in this is chock-a-block. So, you know, it really 9 volts wouldn't have made this thing any smaller, really. They did really well designing this to get the four double A's plus the two

**Dave Jones:** uh HRC fuses plus the SD card and everything else in there. So, there you go. Um that wouldn't have saved it. Triple A's would have made it a bit thinner, but as I said, you have you're basically going

**Dave Jones:** to have the battery life. And then when you're talking about logging to SD card, I with our SD card testing, we got I think it was 350 400 hours or something like that, but that wasn't continuous. You have to keep restarting the damn thing

**Dave Jones:** all the time. But anyway, it just comes down to battery life. So, yes, we could have powered it from a 9 volt battery, but like size-wise, it didn't it didn't really help. Um and really get pretty piss-poor battery life cuz remember inside a 9

**Dave Jones:** volt battery, they've effectively got four four A batteries inside. Open one. I've done a video on that. Open up a 9 volt battery. I'll have to link it in. Open it up. There's actually six four A batteries they're called. Not triple A,

**Dave Jones:** not double A, not triple A, but four A battery size. Um you can buy those individually, but they're quite hard to get. Um and there's six of those inside there. So, anyway, and it wouldn't have helped with the

**Dave Jones:** Um also wouldn't have helped with the 15-V diode mode. We still There's a DC-to-DC converter in here. We still would have needed that because even though it might start out at 18 V if you had two of them in series, it would very

**Dave Jones:** quickly under load uh drop to less than 15 V and then you'd have to have a boost converter anyway. So, you know, you might as well get the best um battery life you can with the size, you know, two 9 V is probably not too

**Dave Jones:** dissimilar. And as I said, thicker it's probably similar in area, maybe slightly smaller than the 4 AA's, but it's thicker. So, it really no volumetric advantage. Um but you sacrifice due to the 4A cell nature in there. Um it is

**Dave Jones:** just isn't as good. That you can't store as much energy in the battery. The the like the chemistry just is like it's just a smaller volumetric size to fit the energy in there. So, I Yeah, we could have used 9 V, but it

**Dave Jones:** would have got piss-poor battery life. So, that's why we didn't do it. Um there you go. And we would have to use DC-to-DC converter anyway to get the 15-V diode mode. So, there you go. I hope that answered that question and you

**Dave Jones:** found it interesting. If you did, thumbs it up, even though it's a second channel video. It all counts. Catch you next time.

**Dave Jones:** Oh, by the way, yes. Um this will be available very shortly, but only to Patreon supporters. Anyway, um and forum supporters, at least the initial batch. But yeah, it will be coming for public sale not too distant future. So, yeah.
