---
video_id: xdGQEVdxmQQ
title: EEVblog #1007 - Is a $25 Multimeter Any Good?
url: https://www.youtube.com/watch?v=xdGQEVdxmQQ
source: youtube-asr
---

**Dave Jones:** Hi, we're going to do something a bit different today and probably something you wouldn't think you'd see on the EV blog and that's a review of a cheap ass multimeter. This is the Aning AN8008 multimeter and it sells for $25 US delivered from the

**Dave Jones:** Aning store on AliExpress, which is where I got it from. It's the official one. You can buy it from other stores of how you can even buy it cheaper maybe around $20 or maybe even under that delivered. And there was a bit of talk

**Dave Jones:** about this on the EV blog. It is a new model. Don't confuse it with the AN8002. They've got different models. This is like the the new upgraded more expensive version. And why would I take a look at this? Well, I thought it might be

**Dave Jones:** interesting cuz it's got a couple of low-level modes which are useful for electronics and of course, you know, let's have a look. Okay, a lot of people say that I have a bias against cheap ass multimeters and yes, I

**Dave Jones:** do. I don't like cheap ass multimeters, but I do know that they have their place. You want to you don't want to work on main stuff. You just want to work on some breadboard stuff and and you know, buying a $20, $25 multimeter,

**Dave Jones:** okay, you know, it's probably going to do the job. So, let's have a look and see what you get. Now, the first thing is that it's actually a 10,000 count meter, 9,999, which is better than your usual you

**Dave Jones:** know, 5 or 6,000 count multimeters on the market. You actually get the extra digit. If you're measuring say 7 volts for example, then you're going to get 7.000 instead of going up a range and getting 7.00. You're going to get that extra digit of

**Dave Jones:** resolution. So, right there it's handy. Now, they're going to claim that it's 600 volt cat 3,000 volt cat 2, absolute rubbish of course. You know, don't like these cheap ass multimeters not independently tested at all. You wouldn't trust them any further

**Dave Jones:** than you can throw on from mains to you. So, I don't recommend you uh uh you know test mains with these or any other high energy high voltage uh stuff. But, for simple, you know, hobbyist breadboard uh low voltage type work, it's you know, it

**Dave Jones:** could do the business. Now, you actually get a fair few accessories for your 25 bucks delivered. You get your regular uh probes with the uh shrouds on there. Not that you need bloody those things. They're really annoying. Reasonably

**Dave Jones:** Well, they're actually quite sharp. And they actually got decent uh uh finger uh guards on there. And they're okay. They're only rated to cat two 600 V 10 amp if you believe that. You know, take it with a grain of salt. But, you know,

**Dave Jones:** the actual probe is compact enough. It's it's reasonably nice. These are not uh silicone leads, of course. They're just your regular PVCs, but they feel, you know, reasonably decent. I'm not going to cut one open to see how much uh

**Dave Jones:** copper's in the thing. But, you also get these ones as well. So, you get Look, these little plug-in ones which uh you can get all these accessory spade lugs and things like that. Handy probes and uh and 4 mm banana jacks to go into

**Dave Jones:** there and a bunch of alligator clips and a bunch of screw-on probe tips. So, quite handy for the money. Little manual and uh look at the pouch. Look at the pouch. It's got to be worth it just for that gorgeous pouch.

**Dave Jones:** And out of the box, um it doesn't look like there's a battery in there or it's completely dead. Um well, now the first thing you notice about this thing is it's absolutely tiny. It's almost pocket-like. If we compare it to the

**Dave Jones:** BM235, which is already a small compact multimeter, you can see the the the physical difference in there. In fact, they obviously designed this thing to uh match the size exactly to the Fluke 101. And uh there are photos. I'll

**Dave Jones:** Look, I'll I'll edit in a photo there. But, uh yeah, they are identical sizes uh with height and thickness, apparently, to the fluke 101, but it's it's not a direct competitor, but they just copied the form factor. And the

**Dave Jones:** tilting bail, well, it's you know, pretty crusty. It's like like there's just no heft in this thing. It's so light that, you know, you really have to sort of put down force down onto that to use it and if you can't even press the

**Dave Jones:** buttons with the damn like forget it. We don't want to turn on before we take it apart to do a quick teardown. Little self-tappers in the thing and it you can actually replace the two AA batteries didn't come with it

**Dave Jones:** without taking out the screws, but and that does have a metal threaded insert for that, which is nice, but if you want to replace the fuses cuz both ranges are fused apparently. Yeah, you got to take out the self-tappers. So, let's can we

**Dave Jones:** open it? It's probably got a clip in there somewhere. And we're in like Flynn and that's exactly what you expect in a cheap ass moldy meter like this. We're like the contacts are just yeah, they not even the solid ones just that

**Dave Jones:** like the pressed spring metal going over you know, pretty terrible. 10 amp current shut, but interestingly, look at the fuses. Yeah, both ranges are fuses fused and yes, they are HRC high rupture capacity fuses in quote marks, but

**Dave Jones:** they're absolutely tiny. So, that's a 10 amp job 250 volts not this high voltage rubbish and 200 milliamps down here for the combined volts and milliamp microamp jack down there. So, so right off the bat, I can't see any

**Dave Jones:** protection in here apart from the fuses. Where are the PTCs? Where are the MOVs? They're just not there. Nice little MELF resistors there. You know, I'm a MELF resistor fan boy, but unless the protection devices are on the bottom

**Dave Jones:** side. Uh-oh, what do we have over here? We've got one. There it is, PTC right up there on the other side that of the battery contact right near the chip. So, that's a interesting placement. So, yeah, like a bare minimum input

**Dave Jones:** protection. Where's the fuse? Where Where do you even find those? They're 10 mm by 3 mm by the looks of it. Uh, jeez, like why? MTO5s at least. Thank you. So, the lack of any input protection like MOVs and we've got a single PTC, but

**Dave Jones:** there's no like diode looks like unless it's on the bottom, there's no diode protection for the amps input and stuff like that. Like I just This is why I do not recommend these for anything probing around on the mains or

**Dave Jones:** other high energy high voltage circuits. Just don't. And we've just got our chip on board blob there. I believe it's a High Contac chip set. Then we've got our E-squared prom next to that which holds the calibration and other setup values.

**Dave Jones:** You might actually I think some people on the forum been talking about maybe changing some register settings and stuff like that. Because it's external, you could actually modify that and play around with it, but you know, very interestingly, there's a PCB

**Dave Jones:** contact switch here. I wonder what that one does. Hmm. And there's the voltage reference there. The TO92 package is it looks like a genuine Intersil genuine in quote marks. Could be. Anyway, it's an ICL80 69. It's the DC

**Dave Jones:** ZR which is the 100 ppm version. There is a 50 ppm version. So, you know, it's adequate for a 10,000 count multimeter. Interestingly, they've got the silk screen wrong. They say ICL80 96 instead of 80 69. Oops. And the soldering quality is you know,

**Dave Jones:** meh. It's what you expect in a $20 meter. It's fine. Well, hollow solder joints for your 10 amp current shunt. And your solder joints for your fuses there all manually done, of course. They look dry as a bone, don't they? Wow.

**Dave Jones:** Look at that. But apart from that, that's exactly what you'd expect on the top. And no, there were no additional components underneath for protection or anything like that. Pretty typical range switch implementation. And as for the contacts down in there, yeah, all pretty

**Dave Jones:** standard fare. Hey, switch it on and the first thing you notice is the nice high contrast large digits. I really like them. Um, you know, like you can compare glare and stuff until the cows come home. And it's a little bit glarier with

**Dave Jones:** its curved top on it and stuff. Well, I can probably, you know, get it to like, yeah. Anyway, it's it's it's a pretty good screen. I like it. And I like the big crisp high contrast digits. They're really quite nice. They're It's really

**Dave Jones:** good at most angles. So, yeah, big thumbs up for the screen, that's for sure. Now, the first thing you should have noticed is that, look, 10 microvolts resolution here on the, well, 100 mV range cuz it's, you know, 10,000 count. So, you might

**Dave Jones:** think that's and that is really good, right? That's better than most meters already. But this thing has another one up its sleeve. Put in manual range. Look, it's got a 10 mV mode with 1 mV resolution. It's overloading because

**Dave Jones:** it's, you know, just getting noise on the input. But let's give it a whirl. This is awesome. So, I use my MV106 transfer standard here, 10 mV range. And even my 7 and 1/2 digit Keysight only gives us one digit better than this.

**Dave Jones:** Look, and it's bang on. Basically, 1 mV, 1 microvolt resolution. This is great if you're you know measuring tiny voltage drops across current shunt resistors or something like that. Brilliant. What other meter, let alone a you know a $25 meter, has a one

**Dave Jones:** microvolt resolution? That's crazy. And it's pretty close to being on in the upper range there, too. And that's 90 millivolts and 10 millivolts, bang on. And it's bang on at 10 millivolts on the 1-volt range because it's 9999 count. It's like it's

**Dave Jones:** great. I love the higher count meters. It can be a bit initially confusing if you're used to the regular ones, but there you go. It's It's pretty close like plus It's bang on. And there's 9 volts, not too far off at all.

**Dave Jones:** That's on the 10-volt range. Go down to 1 volt, bang on. Nice. 90 volts is only a couple of least significant digits off. And well, let's go up to three, four, five, six, 100 volts. 700 volts. 800, 900.

**Dave Jones:** 988. There you go. So, that's Yeah, that's pretty close to what a couple of least significant digits there. And we'll just flip that voltage around. Negative. There you go. Don't like the extra zero out there on the Keysight. That's a

**Dave Jones:** bit how you doing? Hmm. Anyway, that's some bang on to the Keysight 7 1/2 digit meter. And I've checked the inverse on other ranges, too, and it's basically like one least significant digit on the negative. And on my AC voltage standard

**Dave Jones:** here, let's have a look at AC cuz AC can do the one microvolt resolution, too. True RMS in quote marks. It's not going to be high bandwidth, just like one or two kilohertz or something like that depending on the chipset. One microvolt

**Dave Jones:** AC true RMS resolution. Look at that. It matches my 7 1/2 inch digit key site. That's just crazy and it's pretty much bang on, too. That's at 1 kilohertz, by the way. True RMS in quote marks, this thing's,

**Dave Jones:** you know, only going to do a couple of kilohertz, but at 1 kilohertz it's bang on. And at 400 hertz, too. Oh, the 1 volt range at 1 kilohertz, we're talking 30 counts out, but what's that in percentage? And that

**Dave Jones:** looks to be a frequency dependent thing cuz it's only 10 9 or 10 counts different at 400 hertz. So, that's on the exactly the same voltage. Yeah, so it you know, it's starting to taper off at a kilohertz. Well, taper off wasn't

**Dave Jones:** the right word. It's starting to gain, but that's common. They can like have a big lumpy gain at the end and then roll off. 9 volts 400 hertz, 9 volts 1 kilohertz is bang on. 90 volts 400 hertz

**Dave Jones:** and 600 volts 400 hertz. 700 volts. The key site might uh Poor little key site's not going to Yeah, overload. There you go. Way and overload on that, too. So, I can't do 1,000 volts uh I can't do up to 1,000 volts AC, but

**Dave Jones:** yes, 700 volts, no worries. Oh, good enough on the resistance, but it's ranged up there. Yeah, near enough. Oh, yeah, it's doing the business. Good enough. It's hanging in there. Not too shabby on the 10 meg range. Unfortunately, that is

**Dave Jones:** the best it can do. It can only go to uh 10 meg. It can't go any higher. It might be a little bit annoying, but I'll give it a pass. And if we have a look at the basic specs here, exactly what you'd

**Dave Jones:** expect from, you know, such a meter. To your typical 1/2% you know, a few least significant digits, 1% on the AC true RMS and stuff like that. DC current you know, it's like you're not going to write home about it, but that's what you

**Dave Jones:** get for 20 bucks. It's fine. And just for completeness, there's the rest of the uh specs. Three times a second screen updating all the rest of the stuff. As for the manual, meh, you know, it's ex- what you expect for a $20

**Dave Jones:** multimeter. It's all in English. And I won't go through and measure the accuracy of the capacitance range. I couldn't be bothered. But the good thing about it is that it's got one puff resolution on the thing. And if you

**Dave Jones:** disconnect it, it actually gives you a true zero result cuz there is no relative function. So, that's a one disadvantage of this meter, which is I would have been really great if it had that. But yeah, like it it zeros out. A

**Dave Jones:** lot of meters don't do that. Very nice. And I'd use my reference capacitor on this thing, but I lost it in the in the middle of a lab cleanup. Oh, you cannot manual range on the capacitance range though. Just it's just completely

**Dave Jones:** disabled. Why? Continuity tester? Can get it to occasionally skip, but that's pretty good. It's latched and it's pretty quick. That's pass. And diode test mode, you are limited by the two double A battery voltage cuz I've got brand new batteries in there. We're

**Dave Jones:** getting 3.28, but that will change as your battery voltage drops. But that's going to be good enough for a white LED. Sweet. Look at that. And that can give out 1.6 odd milliamps. Yeah, good enough to light the LED. And one rather

**Dave Jones:** interesting mode is this digital out. And if you select it, 50 hertz, 100, 200, and there it is there. I mean, it's I Okay, it's 3 volts peak to peak. And obviously they're getting that from the regulator cuz the

**Dave Jones:** battery was like 3.2. But it goes up in like well, once it jumps from 100 1 kilohertz to two. But before that, there you go. I mean, I I don't know. Um but like someone might find a Well, there we go. What did it go

**Dave Jones:** up to? 5 kilohertz. Someone might find a use for that. Who knows? And it's got a frequency counter. Seems to be a bit off. I mean, that's supposed to be 10 MHz, uh you know, half a volt. Um but

**Dave Jones:** yeah, it's not doing it. So, but it's but below that, no problems whatsoever. I mean, 65, 2.6 meg, there you go. Bang on. It's just at the Well, there we go. Sorry, at the higher frequencies, uh it's not terrific, but up to a couple

**Dave Jones:** of meg, it's fine and dandy. And it seems to need about 150 mV peak to peak to get anything. Actually, it just seemed to be the uh lower amplitude that was a problem there. At a higher amplitude, 8.5 V peak

**Dave Jones:** to peak, yeah, it's bang on at almost the full 10 meg range. Not too shabby on the 1 mA range. Look at that. This had me stumped for a few seconds. Look at this. It's generating 9 mA, and I

**Dave Jones:** thought I could just go to the mA range. It's only for the voltage jacks on the share with the microamp range. And so, it it gives you just some crap uh value there on the input. Ah, there we

**Dave Jones:** go. Now we're talking. Hang on. Oops. There we go. Ah, that's not great, is it? Now, check it out. Uh on the microamp range, okay, 100 microamp range at 10 nA resolution. Fan-freaking-tastic. Once again, a great meter for like uh you know, low value um

**Dave Jones:** precision electronics stuff. Well, when I say precision, I don't mean accurate, you know, like Anyway, it can go down to relatively low currents. But look at the ranges that we've got, okay? So, we've got a 100 microamps. And then we've got one 1,000 microamps,

**Dave Jones:** which is 1 mA. But then if we go over to our milliamp range here, so our highest was one So, we had a 1 mA range, but where is our 10 mA range? We've only got 1,000, so we don't have 10 mA

**Dave Jones:** or 100 mA. We've only got like a Now we've only got the one amp. Oh, what it like it's Oh, no. And sure enough, if you go to the manual, there's the fine print. There's the two micro amp ranges. A

**Dave Jones:** thousand 100 micro amps and a thousand micro amps, but then it jumps up to 100 milliamps. So, you miss your 10 milliamp and 100 milliamp ranges. Like they're Ah, that's practically a showstopper. And look, it's probably going to be

**Dave Jones:** accurate enough, but like I like it's getting to the point where I'm not going to bother to generate the the higher currents. I have to get other gear and like I don't want to forget about the backlight for all you backlight fanboys.

**Dave Jones:** There you go. It's not too shabby at all. So, it works all right. One thing with this, like auto If you go into manual range like that, then I'm not sure how you actually get like back to auto without switching on the

**Dave Jones:** thing and it like I get it like you got to change ranges or whatever. It's fine. Actually, I kind of like that backlight. And I just measured the battery current around about 1.7 milliamps on there. So, you can do the calculations for two

**Dave Jones:** double A's to get your battery life. Shouldn't It's going to be okay. So, there you have it. That's the ANENG, if I'm pronouncing it correctly. Let me know if I'm not. AN8008. I could go into more detail and measure the true RMS

**Dave Jones:** bandwidth and measure all sorts of stuff, but that's that's enough for a little more than enough for a little $25 or you know, sub $25 meter. And well, it's not too bad. It's got some useful ranges on here. It's you know, it's going to

**Dave Jones:** survive a a few knocks and things like that. And for the price, I mean, you get all the accessories and stuff with it. The leads may not be the best quality or whatnot. And the input protection don't go use this on mains or other high

**Dave Jones:** energy circuits, but for sub $25 multimeter, I love some of the low ranges on this thing. It really is quite neat. Seems to, you know, vastly exceeds its accuracy specs, at least the one-off unit I've got here. It could vary, but you know,

**Dave Jones:** it's got a half-reasonable little reference in there. The build quality is okay, but you know, I like it it's as good as you can expect. If you're after a twenty-five dollar dollar multimeter, you can do worse than this little thing, I suspect.

**Dave Jones:** Anyway, hope you enjoyed that look at a twenty-five buck multimeter. It is what it is. Okay, you could say it's an excellent meter for its twenty-five bucks. There, I said it. But the lack of the current ranges is terrible. Those,

**Dave Jones:** you know, real sweet spot stuff where you want that. That's almost a showstopper. I love the ten thousand count, but jeez, the missing current ranges there, what is it, a ten milliamps and a hundred milliamps? Oh my goodness.

**Dave Jones:** What a What an oversight. Why have they done that? Crazy. Anyway, hope you liked that video and you know, I'm not necessarily uh think that all twenty-five dollar multimeters are crap. It is what it is. It's You get more than more value than

**Dave Jones:** your twenty-five bucks in this thing. It really is, you know, it would serve you quite well. It's rather cute, fun little meter. Anyway, I'm not going to give it like a thumbs up or anything. I can't bring myself to do that for a

**Dave Jones:** twenty-five dollar multimeter, but you know, for twenty-five bucks, it probably beats um probably most other ones on the market. I don't know. Especially for its little compact size. It's cute. Anyway, if you liked the video, give the video a big thumbs up. As

**Dave Jones:** always, discuss it at the EEVblog forum down below or the comments. Catch you next time.

**Dave Jones:** Mhm.
