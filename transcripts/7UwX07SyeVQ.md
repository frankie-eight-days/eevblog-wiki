---
video_id: 7UwX07SyeVQ
title: EEVblog #852 - Multimeter Mass Turbulence
url: https://www.youtube.com/watch?v=7UwX07SyeVQ
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 22, "3": 36, "4": 53, "5": 67, "6": 81, "7": 96, "8": 110, "9": 122, "10": 137, "11": 153, "12": 171, "13": 184, "14": 196, "15": 212, "16": 225, "17": 240, "18": 254, "19": 271, "20": 285, "21": 298, "22": 310, "23": 322, "24": 338, "25": 352, "26": 369, "27": 382, "28": 400, "29": 428, "30": 447, "31": 462, "32": 484, "33": 500, "34": 515, "35": 535, "36": 559, "37": 592, "38": 615, "39": 629, "40": 648, "41": 662, "42": 679, "43": 692, "44": 708, "45": 724, "46": 737, "47": 754, "48": 770, "49": 784, "50": 797, "51": 811, "52": 823, "53": 835, "54": 847, "55": 861, "56": 874, "57": 891, "58": 905, "59": 921, "60": 934, "61": 956, "62": 972, "63": 986, "64": 1004, "65": 1020, "66": 1032, "67": 1044, "68": 1058}
---

**Dave Jones:** Hi, I thought it'd be interesting to take a look at a typical three and a half digit or 6,000 count multimeter and see how accurate these things are out of the box by getting not just one of them,

**Dave Jones:** but by getting a whole bunch of them. And I just so happen to have a whole bunch of these new EEVblog meters here in the lab. And before I ship them out, I thought I would just hook them up to

**Dave Jones:** my reference generator here and see how close they are on various ranges across a whole spread multimeters. Granted, they are all part of the same shipment. They're all cali- manufactured at the same time on the same run. They were all

**Dave Jones:** calibrated at the same time. But that's the interesting point. How close can a typical factory calibration on a meter like this actually be? Is it plus minus one least significant digit? Is it half its spec? You know, this is like 0.3% DC

**Dave Jones:** volts typical, which actually gives a reasonably wide spec in terms of counts. Plus there's the number of counts as well. I've done a video on this explaining that sort of thing. And how close is it to its absolute, you know, to an

**Dave Jones:** absolute reference standard? So I thought we'd get like 50 odd multimeters or so and actually measure them. And I'll go through I won't bore you with all the details, but I'll actually take as many multimeters as I've got here,

**Dave Jones:** all from the same batch, and actually measure them on various ranges, see if we can get the data. Could be interesting. Let's go. Hey, check this out. Look, amazing. Symmetrical multimeter stacking, just like the Philadelphia Mass Turbulence of

**Dave Jones:** 1984. Unbelievable. No human could stack multimeters like this. So if we actually have a look at the specs of a typical three and a half digit multimeter like this, I say three and a half digits, it's actually 6,000

**Dave Jones:** count. I've done a whole video on that, which I might have to link in here if you haven't seen it that explains counts and resolution and counts and all that sort of stuff. Anyway, typically for the DC voltage range here,

**Dave Jones:** uh for the 60 mV to the 6 V, we're looking at 0.3% plus two digits there. So, that's actually uh 0.3% of the actual reading, and that'll tell you over here on the electrical specs is given as plus minus a percentage of the

**Dave Jones:** reading plus number of digits. So, if we actually have a look at that, the meter could actually read and still be within spec. Let's say you had uh you're measuring 5 V on the 6 V range, for example. Just with the plus minus

**Dave Jones:** 0.3% accuracy figure, it could read anywhere from uh 4.985 V to 5.015 V and still be within spec for a precise 5 V input. And that's not taking into account the extra the plus two digits here, which you have to add on to the

**Dave Jones:** least significant digit over here. And so, it could display anywhere between that figure. But, how close is it actually going to be? Not just on one meter, cuz that really doesn't tell you much. Uh it doesn't effectively doesn't tell you

**Dave Jones:** anything. You've only got one data point. But, if we can get, say, 50 multimeters or something, then hey, that can give us a good indication. I've never actually done this on a bulk lot of meters. But, of course, a meter like

**Dave Jones:** this is actually or should be actually uh calibrated at the factory. It's actually software adjusted, so they will uh feed in the the reference uh voltage generator in here and actually uh program the exact figure in there. Or, that's what they

**Dave Jones:** should do. In back in the old days, they'd get the tongue at the right angle and tweak a little pot inside, but modern multi-multimeters like this one don't have pots. They're all uh software configurable. So, when you measure 5 V,

**Dave Jones:** it should be spot on in theory, of course. But, of course, this changes with the temperature and, you know, age and other characteristics. So, it'll be interesting to measure a whole bunch of these and see what we get. But, of course, as with any

**Dave Jones:** measurement system like this, even if it's bang on, as I like to say, and we feed in 5.0000 V, which I'm capable of doing with my lab gear here, a precisely known value, it could still be plus minus one digit

**Dave Jones:** here, and you always expect that from the converter. That's just inherent in the converter itself. So, yeah, you know, if it's 5.001, for example, you wouldn't worry about that until you would say that they're all bang on. When when you start talking

**Dave Jones:** .002 or .003 or something like that, then you can start saying, "Yeah, it it's starting to be different to the other meters." Oh, but still, it's it's definitely going to be within spec. I know that for sure. So, what I'm going

**Dave Jones:** to use is my Advantest R6142 programmable uh voltage and current generator, so we can do DC voltage and DC current. I also have an AC voltage uh generator. I have a resistance standard. So, I'll try and do um as much as I

**Dave Jones:** won't do all the ranges. Um obviously, this thing can only go up to like uh you know, 11 V maximum, I think it is. Um so, you know, can't I'm not going to test like the 1,000 V range, but hey,

**Dave Jones:** anyway, I won't go quite to full scale. This is a 6,000 count meter. I'll drop it back by one and just give a nice familiar uh voltage reading of 5 here. And yes, I've let it warm up and I've

**Dave Jones:** confirmed it with my uh Keithley meter above it and other stuff. So, no drama. Let's uh plug this puppy in and see what we get. But, I won't bore you with all the details of all the rest of them. Bang, 5.000, but

**Dave Jones:** as I said, there we go. .001, right? Not concerned. Plus minus one least significant digit. So, I'm I'm to see how close they all are. I pretty much expect them all to be within a couple of least significant digits because that's

**Dave Jones:** effectively what this plus digit on the end is saying. They're, you know, fairly confident that it's going to be the exact figure they calibrated it at plus two digits, basically. So, you know, I expect it to be within that. It's 24°.

**Dave Jones:** No, sorry. 20 Sorry. 22° here in the lab and, you know, it would have been similar temperature to what they calibrated at. So, I expect them all to be pretty darn close like that. It could actually be a really incredibly boring

**Dave Jones:** result. Sorry ahead of time. In fact, I think it will be. Hmm. Well, that's a few multimeters, 40 to be precise. I can't explain it, but there's something very therapeutic about doing this. Oh, yeah. So, I've got my handy banana plug lead.

**Dave Jones:** Here I go. Ah, goodness. The things I do. Now, let's repeat that same thing, but with 50 mV. So, I've changed to the millivolt range here and we are, you know, 50 mV is quite low. So, you know,

**Dave Jones:** not all multimeters have a 50 mV range, but hey, let's have a look. This one's bang on 50.00. Ah, 50.00. Geez. Liking the millivolt range. Anyway, I am recording all these. Actually, the millivolt range so far is ridiculously

**Dave Jones:** ridiculously spot on. So, I think what they must be doing is calibrating the millivolt range and relying on the resistor divider uh to get the other ranges. Ah, there we are. It's getting It's got It dropped out. There's a little bit of excess

**Dave Jones:** charge there. So, these are all spot on 50.00. This is insane. So, yeah, this is just uh This is crazy business. So, that's what they must be doing. That's why we saw some variation on the readings before, 499 497 from basically 4 uh 4.997 up to

**Dave Jones:** 4.5, basically. So, uh just some tolerance on the Is this still the divider? But, these are all Jeez, that's ridiculously bang on. That's just crazy. Oh. Oh, is that one one least significant digit out? Oh, no. And now

**Dave Jones:** for the resistance standard, I'm using my Weinschel precision reference standard. If you have to ask the price, you can't afford it. So, yeah, I don't think we're going to question the accuracy. 9.99, let's go. Now, of course, one of the problems with

**Dave Jones:** a 10k standard on a 60k uh range is that, well, you know, you're only got uh two decimal places here. So, you know, I expect it to be like and it is. It's like 999998 at worst. They're all going to be Yep,

**Dave Jones:** there we go. 10. Well, that came in not too bad from 998 up to uh 10.00. Now, it's time for current. So, I'm going to use a 50 milliamps and, well, this one was bang on 50. So, let's uh

**Dave Jones:** let's start there. Here we go. Oh, goodness. I'm going this way and then back that way for those who are playing along at home. 49.99, here we go. 49.99 Oh, boy.

**Dave Jones:** Well, that current is a very crazy tight spec, the only one was 9994998 down here. So, but only a two I'm sorry, three least significant digit spread there, very tight on current. Okay, one last thing I'm going to check is AC cuz that's not typically

**Dave Jones:** tested. So, I've actually got an AC voltage standard here and EDC just like my EDC DC reference standard up here, which is the best standard I had in the lab. I didn't need to use that for today's purposes because we're not only

**Dave Jones:** looking at a 0.3% class instrument. Anyway, this AC voltage standard, I forget the spec, but it's more than good enough. I set it for 5.00000 V at 60 Hz. So, that's I believe smack bang in the middle of its most accurate range. So, 5

**Dave Jones:** V, let's give it a bell. Currently getting 5.002 and I have actually confirmed it up here and I've given it a little bit of a tweak to be closer there. I've turned some averaging on. And I won't bore you

**Dave Jones:** with the time lapses of all these, but I probably expect God, helps if I have to go select all the ranges. I'm not going to use the the VFD, which is the variable frequency drive, which is the which is the filter in there. As

**Dave Jones:** you can see, it doesn't get the resolution. So, hey, that one's bang on. So, won't bore you with another time lapse. Well, I was actually quite surprised by the AC spec here. It was really tight. I mean, the highest was

**Dave Jones:** five uh double 0 3 up there and there, but most of them were pretty almost bang on, you know, 5 double 0 1 or uh 5,000 spot on. And um the spec, by the way, for um AC range uh 50 to 60 hertz is the

**Dave Jones:** uh tightest response. It's uh 0.7% plus three digits. So, it's easily We Well, it's within Well, actually, yes, it's within No, four digits. It's within the four digits. Uh let alone the 0.7%. So, balls in the in. So, there you go.

**Dave Jones:** That's the final data table uh for this thing. Just some spot checking on various uh ranges here. And it is, as you can see, it was well within the spec of this thing um which was uh by the

**Dave Jones:** way, the resistance um spec there was uh typically 0.3% Uh there we go. Yeah. Uh Actually, on the 10k range it uh up to 0.5% uh plus three digits. But, you can see, you know, it did pretty darn well because

**Dave Jones:** they uh calibrate these things might not necessarily on every range, as I said. I actually haven't asked uh Brymen what they actually how they actually calibrate this thing. But, as you can see, the the best range, by far, was the 50 mV one. And also,

**Dave Jones:** it'd be the same for the 500 mV one, too, I would think. Cuz what they're doing is they're calibrating it on the mV scale, and that's very typical. And then uh actually relying on the resisted divider to do the rest. So, that's why,

**Dave Jones:** you know, when you start getting out to the 5-V range, you're a little bit out. Um I was very impressed by the current. Actually, that was uh really uh spread on that was really good. And the AC, very surprising, as well. I would

**Dave Jones:** have expected a larger spread on the AC, but didn't see it at all. So, I'm actually quite impressed by this. But, this is typical of even uh you know, relatively low cost meters like this one because they do have software

**Dave Jones:** calibration and I'm too lazy to go in there and you know put this data into a spreadsheet and you know maybe get some binning and things like that. It's there's not enough spread in there really to get a huge amount of this

**Dave Jones:** useful data. All we want is the min max spread on each one. You can calculate the percentage. It's much better than the specs. That's all we care about. So they can actually software calibrate these things I believe but I'm not sure

**Dave Jones:** of their exact procedure. I can't find a cal like a some meters have like a cal menu when you you know hold a button down and turn them on for example. So I'm not sure of the procedure for this

**Dave Jones:** one or whether or not they're just relying upon a the voltage reference which I believe is inside the chipset for this one and the and the precision of the resistor networks that they plug into these things. Whether or not they

**Dave Jones:** do individual cal on each one, I don't know. As like manufacturers different manufacturers going to be different, different models are going to be different, all that sort of stuff on how they calibrate them. Actually that wasn't a really fair test with the 10k

**Dave Jones:** resistor here cuz it was as I mentioned it was much lower down in the range so the error becomes a greater percentage because purely from the ADC count, the resolution. So what I've got is my IET decade resistance box here. It's not

**Dave Jones:** a standard as such but I'm able to uh select 50k so we can use the same order as before and bam, I've tweaked it until it's good enough. So I'll repeat that. And there we go. We actually got a

**Dave Jones:** bigger spread on the actual number of digits. We got a differential of nine between the highest and the lowest number, nine least significant digits but because it's much higher in the range when you calculate the percentage, it's a lower percentage uh, or IE, you

**Dave Jones:** know, a tighter tolerance than what we got for the, uh, 10 K one here purely because we're, uh, closer to full scale on the 60 K range than we were with the 10 K resistor also on the same 60 K

**Dave Jones:** range. And just for kicks for all you Uni-T fanboys out there, I'll just try my, uh, UT61E. And, uh, hmm, 49.84 K. Yeah, not that terrific, is it? Is that within spec? Hmm, 0.32% hmm, yeah, I think it I actually

**Dave Jones:** probably is just within spec, is it? And that same 50 mV, uh, range we were bang on here with before. Woo, I might have drifted by 0.1 mV. Um, yeah, we're a little bit low there, but, uh, still within spec, I believe, but,

**Dave Jones:** yeah, significant different. Anyway, a sample size of one. And I would show you my Fluke 17B, but I kid you not, it has failed. And no, it's not the contact on the banana plugs. I've tried the probes which come with it, shorted

**Dave Jones:** out. It does nothing. What the? And it doesn't even read the millivolts, either. It's absolutely useless. It's dead. Maybe a repair video. And just for kicks, there's the older, uh, Brymen BM257. Oh, look, alpha bees dig up. And of course,

**Dave Jones:** the venerable Fluke 87 is bang on. Well, I'm telling you what, here's another Uni-T and, uh, hmm, not too good at all. But, as you can see, well within the quoted spec, and that's not unusual, uh, these days. It

**Dave Jones:** was different back in the day with the tweaking the, uh, pots in the things, but, you know, usually even your cheaper multimeters are pretty good these days. So, anyway, hope you found that interesting. I just thought I had these

**Dave Jones:** meters. I've never really had a chance to do this, so, hey, why the hell not? Anyway, if you enjoyed it, please give it a big thumbs up, discuss it down below, all that sort of jazz. You want to support me, Patreon links down below.

**Dave Jones:** I've got new EV blog newsletter you can sign up to. Uh by the way, if you wanted to know about this meter, people on the newsletter and uh Patreon uh and supporters, they actually found about this and it's um currently practically

**Dave Jones:** sold out. So, sorry, there's not going to be another batch until uh April, is it? Yes. Hm. Catch you next time.
