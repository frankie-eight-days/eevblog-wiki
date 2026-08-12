---
video_id: YeNpd-sXaHk
title: EEVblog #476 - Opamp Offset Voltage Measurement
url: https://www.youtube.com/watch?v=YeNpd-sXaHk
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 31, "3": 49, "4": 66, "5": 79, "6": 98, "7": 115, "8": 129, "9": 142, "10": 155, "11": 169, "12": 185, "13": 197, "14": 211, "15": 221, "16": 235, "17": 251, "18": 267, "19": 283, "20": 299, "21": 313, "22": 327, "23": 343, "24": 355, "25": 368, "26": 381, "27": 391, "28": 406, "29": 419, "30": 431, "31": 448, "32": 461, "33": 474, "34": 491, "35": 504, "36": 520, "37": 535, "38": 547, "39": 562, "40": 575, "41": 593, "42": 607, "43": 621, "44": 632, "45": 645, "46": 659, "47": 672, "48": 688, "49": 706, "50": 724, "51": 740, "52": 752, "53": 770, "54": 782, "55": 796, "56": 814, "57": 828, "58": 843, "59": 862, "60": 884, "61": 896, "62": 909, "63": 926, "64": 937, "65": 952, "66": 962, "67": 979, "68": 997, "69": 1018, "70": 1034, "71": 1050, "72": 1063, "73": 1081, "74": 1098, "75": 1113, "76": 1127, "77": 1141, "78": 1157, "79": 1168, "80": 1185, "81": 1202, "82": 1219, "83": 1236, "84": 1248, "85": 1263, "86": 1275, "87": 1288, "88": 1307, "89": 1332, "90": 1352, "91": 1367, "92": 1385, "93": 1400, "94": 1424, "95": 1448, "96": 1465, "97": 1479, "98": 1501, "99": 1516, "100": 1531, "101": 1545, "102": 1556, "103": 1568, "104": 1583, "105": 1600, "106": 1614, "107": 1626, "108": 1641, "109": 1653, "110": 1666, "111": 1680, "112": 1695}
---

**Dave Jones:** Hi, this isn't exactly going to be a fundamentals Friday as you probably expected but I was just running ran across this issue that I thought I'd check out today. So I thought oh, why not turn on the camera and let you have

**Dave Jones:** a look at it as well. So I guess it is kind of fundamental it you know, it comes down to looking at data sheets and measuring things. So you know, it's a fundamental problem that we all have to deal with eventually. Anyway,

**Dave Jones:** what I've got is this analog devices AD8628. It's a really schmicko as it says zero drift single supply rail-to-rail operational amplifier and it's actually a chopper amplifier as I've done a video on. If you haven't seen a video on

**Dave Jones:** chopper amps, I will link that right here down below. So click on that and watch that if you want to. It's one of my much older videos. Anyway, pretty much one of the best zero drift low offset voltage operational

**Dave Jones:** amplifiers you can get on the market and yes, it's got that chopper configuration to get a very low offset voltage. Check out some of the banner specs here. It claims to be the lowest auto zero amplifier noise of presumably any

**Dave Jones:** amplifier on the market. Awesome, super low offset voltage only one microvolts. That will be a typical voltage as we'll see not a maximum voltage and input offset drift. It's essentially zero. Look at it. It's 2.002 microvolts per degree C or 2 nanovolts

**Dave Jones:** per degree C. So once you've once it's got that one micro let's say this particular chip, the one you've got has one microvolt offset input offset voltage then that value of one microvolts is only going to drift by 2 nanovolts per degree C.

**Dave Jones:** Incredibly stable chip. Fantastic. Well, that's one of the reasons I'm using it here. Now, uh it's got rail-to-rail input and output swing. Fantastic. So, you can take the input down to 0 V, or you can take it all the way up to the supply

**Dave Jones:** voltage. The same with the output as well. So, you can utilize the maximum output range. Uh single supply operation. It actually goes down to uh 2 and 1/2 uh V or thereabouts. So, uh perfect for my application. Um high

**Dave Jones:** gain. Yeah, kind of 130 uh dB common mode rejection ratio. All that sort of stuff. Low input uh bias current, 100 pA. Good enough for my application. Uh low power supply current, it's under a milliamp. Good enough. Overload recovery

**Dave Jones:** time, uh it's not bad for a chopper amp. Um no external components, it's all internal. Um all the uh chopper um uh circuitry and stuff all runs internally, and the oscillator is all internal, and all that sort of stuff. As

**Dave Jones:** is typical with uh chopper amps these days. And it's qualified for automotive applications. Whoop-de-doo. But, anyway, I built this um I used this chip, and I discovered a little weird uh problem, well, an issue with it that I wasn't

**Dave Jones:** really expecting. And uh it you know, it took me a little bit of a while to figure out what was actually going on with this thing. I actually mentioned on the Amp Hour a couple of uh episodes ago, actually. Uh if you want to listen

**Dave Jones:** to that. There's a brief description of it on there. And anyway, I thought I would I've I've figured out what the issue is, but I thought I would double-check it by actually building it up uh from scratch again, and actually

**Dave Jones:** verifying that it's the case in various uh scenarios. So, that's exactly what I'm going to do today. So, I thought I'd turn on the camera, and uh give you a look at it. I was slightly off on the

**Dave Jones:** supply voltage there, it's actually 2.7 V to 5 V single supply operation. Now, as with um all op amps, they don't care whether or not you're using them from a dual supply or a split supply subject to input and output uh you know common mode

**Dave Jones:** range and output range and stuff like that. So, it can actually operate from plus minus 1.35 volts. That's like practically you know plus minus a single cell single alkaline cell to plus minus 2.5 volt dual supply. So, an ideal op

**Dave Jones:** amp to be operating from a coin cell or something like that you know if you got a strain gauge or something that's operating from battery. Fantastic device. And apparently the chip combines the benefits previously found in expensive auto zeroing or chopper stabilized

**Dave Jones:** amplifiers. And yes, there can be differences there which I won't go into. As you can see the noise is pretty low too. 0.5 microvolts peak to peak from 0 hertz up to 10 hertz. So, awesome device. It's pretty hard to I think

**Dave Jones:** you'll be pretty hard pressed to get a better device than this. There are lower ones in terms of offset voltage but not um sort of like a combined in terms of offset voltage plus noise plus drift. So, you know, one of the best op amps on

**Dave Jones:** the market. Now, before we have a look at the problem, I'll just look at some of the specs to give you some background on the issue here. Now, these are the electrical characteristics at supply voltage of 5 volts i.e. plus

**Dave Jones:** minus 2.5 volts which was pretty close to what I was working at. I was actually working off three alkaline fresh alkaline cells. So, it was like a 4 1/2 volt supply. Now, the input offset voltage is the thing

**Dave Jones:** that we're concerned with today. This is here are the typical figures for it. Okay, typical figure at 25° C by the way with the common mode voltage by the way smack in the middle there which was how I was basically operating with a split

**Dave Jones:** supply. Now, the offset voltage here the input offset voltage, typically 1 microvolt, and that's the banner spec. But, of course, you don't take the you know, you can't always just take the banner spec. You've got to look at the

**Dave Jones:** maximum value as well. In this case, 5 microvolts maximum. And if you want to take the full temperature range into account, which I don't have to, then it can be as bad as 10 microvolts. That's still pretty low, but you know, it's

**Dave Jones:** order of magnitude worse than the headline spec they tell you on the front page. That's always a trick the trap for young players with these data sheets. If you just read these front pages here, these headline specs up

**Dave Jones:** here, they don't give you all the detail. They're going to lie. It's basically marketing wank up here. Well, they're not Well, they're not going to lie, but they're not going to tell you the whole truth and nothing but the

**Dave Jones:** truth. This is where you have to look in the electrical specifications here. So, this is what we're really concerned with. Input bias current doesn't really concern me really and all the rejection ratio and all that sort of stuff doesn't really

**Dave Jones:** matter. And of course, the drift is so low, you know, 2 nanovolts per degree C that jeez, you don't even have to worry about it. But, not that would come into play anyway, even if it was high, because the lab here is

**Dave Jones:** essentially a fixed temperature. It's only going to vary with the air con on by, you know, plus minus half a degree a degree or something like that. Now, this looks like an identical page, but it's not. It's actually the next page

**Dave Jones:** over, the electrical characteristics now for a supply voltage of 2.7 volts. We had 5 volts before. And once again, common mode voltage 1.35 volts, smack in the middle, and we've basically got exactly the same numbers here. 1 microvolt typical for the input offset

**Dave Jones:** voltage, which is the issue that I had. Now, if you take it if you scroll further through the data sheet, you come to Well, the first thing you come to, cuz they're quite proud of it, is the input offset voltage

**Dave Jones:** here on the X axis. Here we go. It's sort of zero is sort of there. Right about there. And uh this is at 2.7 volts. Let's look at the 5-volt one. There's our zero. Right, right in the center.

**Dave Jones:** There. And our input offset voltage can be plus minus that. With a common mode voltage of 2.5 volts. So, smack in the middle and you get that characteristic bell curve kind of shape in your values. And these are a number of amplifiers.

**Dave Jones:** So, they actually measured, you know, 10, 20, like 80 amplifiers. So, they measured a couple of 100 amplifiers here. And this is the response that they actually got. And yet it's always typical. It's going to be uh when you

**Dave Jones:** get manufacturing process variations like this, you're typically going to get, given enough devices, that bell shaped characteristic response. That bell curve as they call it. So, uh let's, you know, here that most of them are centered around zero. And the most

**Dave Jones:** of them, the bulk, are going within plus minus 0.5 microvolts. So, it's, you know, um around about that 1 microvolt typical figure. Not bad. See, here's the majority of them. Oh, there's there's one 1 microvolt from plus minus one. I

**Dave Jones:** guess they only give 1 microvolt typical. They don't say that's plus minus. Anyway, even at 2.7 volts down here. So, when you vary the supply voltage, which is what we're going to look at later, then you'll notice that

**Dave Jones:** yeah, it's been shifted up a bit. There's our zero point. But still, it's very low. None of them are getting anywhere near that maximum figure of 5 microvolts, right? So, we expect if we bought some of these chips, you know,

**Dave Jones:** odds are, not guaranteed of course, but can be pretty darn certain it's going to fall within there. You know, it's going to be like at least under 2 microvolts, for example. You know, there's a couple of outliers out here, for example, but

**Dave Jones:** gee, you know, you expect it to be pretty close to that typical value of 1 microvolts. And I found when I built this thing up, that wasn't the case. I was getting up to 5 microvolts offset. Hmm. Let's go to

**Dave Jones:** the breadboard. But before we do that, let's take a look at the circuit which we're looking at here. It's the AD 8628 uh op amp. It's a single op amp SO8 uh package. And I've got it set for a

**Dave Jones:** non-inverting gain of 100 here. Oh, it's actually 101 using 1K and 100K. Who cares? Near enough to 100, right? So, um then we're going to have an input offset voltage here that 1 microvolts typical. And of course, that input offset voltage

**Dave Jones:** there is going to get multiplied by the gain of your op amp. That's how it works. It's not just for this op amp. It's for all op amps. It's going to do that. So, let's say that this particular

**Dave Jones:** device that we have under test is has 1 microvolt there. We expect 100 microvolts on the output here or 0.1 millivolts. So, we'll build it up and we see and we'll see if we get it. Of course, I've I've got it just got a

**Dave Jones:** couple of bypass uh caps on here. I've got a split supply. In this case, it can go anywhere from uh well, from 2.7 total um up to 5 volts. Now, what I've done is gone and actually uh assembled this chip

**Dave Jones:** on uh one of my um micro current boards here because it has the same uh configuration. Just allows me to easily do that. I've removed all other uh circuitry on there, the rail splitter, and all that sort of stuff. So, it's

**Dave Jones:** powered from my external bench supply uh positive supply, negative supply, and my uh and there's the ground. And uh that's my output. Now, I've got my output uh voltage on here, and I've got my uh supply rail here. So, it's 5 volts total

**Dave Jones:** across here. So, split is plus minus 2 and 1/2 volts. So, you know, the uh maximum range that this thing can operate at. And if you remember, look at our spec here, typical figure of 1 microvolt offset voltage at and a maximum of five. So,

**Dave Jones:** we'd expect that typical value, remember, based on that bell curve. So, I've got a times well, times 101 gain in here, near enough to 100. And look what we're getting on the output. We're getting 300 odd microvolts or thereabouts, 0.3 millivolts. If you

**Dave Jones:** divide that by 100, that's 3 microvolts offset voltage. And sure, okay, it's within spec, you know, you think, okay, not a problem. So, it's it's within spec. Okay, fair enough, nothing wrong with the chip. Okay, and that's what I

**Dave Jones:** thought the first time. Ah, look, I've just got a bad one. You know, but no, I replaced it. Then I replaced it again, I replaced it again, and no, all of them had around about this same 300 odd

**Dave Jones:** microvolts offset voltage. And I was scratching my head for ages trying to figure out what it actually was. And yes, I've deliberately shown this ground point down here as a star point so that everything is referenced to that. The

**Dave Jones:** input voltage there is referenced directly to there, the output voltage is referenced to there. And that's really going to matter if you've got any significant current flowing through those traces, but we don't with our high impedance, uh, you know, 10 megaohm input

**Dave Jones:** multimeter and stuff like that. So, the star grounding doesn't really matter in this particular scenario, but I've just drawn it there for completeness. And yes, that input voltage pin three, that's that little blue wire looping across there, that's shorted out

**Dave Jones:** directly to there. So, you know, our input So, we're amplifying our VOS, our input offset voltage by 100 basically, and that's what we're getting, regardless of what chip I put in here. And trust me, I've tested quite a few of them. So, now I've got it down

**Dave Jones:** to just this scenario here with the split supply. So, what's going on? Is the typical figure a load of Well, I tried all sorts of things, hacking and slashing my circuit, you know, uh uh I've got something There's

**Dave Jones:** something weird going on the layout. There's something wrong with my power supply, yada yada. I was going poring through the data sheets and everything, until I just thought, "Uh, I wonder what happens if I take the supply voltage down?" And here we go.

**Dave Jones:** Let me wind down the wick, right? And you remember back here, here's the 5-V one. You remember? There it is, 5 V typical figure, 1 µV, 5 µV. 2.7 minimum, 2.7 V typical figures remain the same. So, you expect You

**Dave Jones:** don't expect that offset voltage to change at all, right? Well, let's look what happens when we wind this power supply down. Look at that. It's dropping. It's dropping. It's dropping. Look. Magic, folks. Look what happens when we get down to 2. 7 V. It's bordering on,

**Dave Jones:** you know, it's zero. It's like, you know, it's very low. In fact, it actually went negative, right? And you'll see it. We wind it up a bit, it goes positive again. So, we can actually almost null that out, you know? There it

**Dave Jones:** is, at, you know, 3 V. And that's going to vary with chip. Why is this thing changing with the supply voltage? According to the spec sheet, it shouldn't. The typical figure should be the same. And it's not just

**Dave Jones:** this one chip. I've tried this on many different I many different devices, and it's exactly the same. Now, the thing I actually wanted uh uh, try today, because I've already uh, tried this in my uh, real circuit and um, yeah, I've

**Dave Jones:** I've verified that this is the case. So, what I actually wanted to try today before I turn the camera on is does this do it based on a single supply? Cuz I've got a split supply at the moment and

**Dave Jones:** effectively this uh, point here, this ground point, the reference point is sitting smack in the middle of that supply voltage range, right? So, what I want to do is power this from a a single supply. So, effectively I'm just going to now short

**Dave Jones:** out this ground point to this negative point and only power it from a single supply. So, I got to uh, I won't do this live and I'll blow up my chip if I goof it up. So, let me

**Dave Jones:** reconfigure it. All right, I've reconfigured it now. So, essentially I've just shorted out this point, that uh, ground point to the negative rail and I'm now su- uh, running it from a single supply and uh, let's and here it is, 2.7 uh, volts uh,

**Dave Jones:** minimum supply and we're getting about 73 microvolts out or about divided by 100, 0.7 microvolts offset voltage around that typical figure we expect. Now, let's wind it up and I haven't tried this. Let's see if it increases.

**Dave Jones:** It It is. It's going up. It's going up. Not by a huge amount, though. Look at that. So, we can go up to a maximum supply voltage of 5 volts. So, there you go. It's the fact that Don't Don't want to go over that.

**Dave Jones:** That is its maximum supply. Its absolute maximum is uh, six, but I won't take it there. There you go. It hasn't gone up much at all. So, it's the fact that we're actually running this split supply uh, is the thing that causes the issue

**Dave Jones:** here. When you actually uh, power it from just a single supply, you don't get this offset issue at all. Strange. I don't know why that's the case. And just to show you that it's not that chip, I've actually soldered another one

**Dave Jones:** onto uh one of my micro current boards. So, this doesn't have the uh Maxim chip in it anymore. It's got the uh Analog Devices chip in it. And there we go There we go. Let's take it up to 5 V.

**Dave Jones:** There we go. This one's actually real even higher. This one's uh 400 uh 400 uh microvolts or 4 microvolts offset voltage. And once again, it varies with that supply rail. Check it out. Down to 2.7. There it is.

**Dave Jones:** Where it goes down to incredibly low. Unbelievable. And just to show that uh it's different with the Maxim chip, I've got uh one of my original micro current boards with the MAX4239 in there. And uh it's um let's take it

**Dave Jones:** up. And look, even it up at 5 V, there you go. Now, it's incredibly low cuz this one's typically uh 0.1 microvolts um offset voltage. So, it's actually uh lower than the Analog Devices one, but its drift and its noise is higher and its

**Dave Jones:** bandwidth is lower and all that sort of stuff. But yeah, so there you go. Not a problem on the Maxim chip. Now, just for another comparison, I've got a uh another uh low drift uh auto zero chopper amp

**Dave Jones:** here. It's the Microchip MCP6V 01. It's not quite as good, but it's uh if if either of the devices, but it's not uh bad at all. It's uh typical or its max uh value is plus minus 2 microvolts uh offset voltage. And once

**Dave Jones:** again, they've got a percentage of occurrences versus uh microvolts offset voltage there. And as you can see, you know, that they pretty much um the sample falls within that plus one microvolt. So, we should expect less than 100 microvolts on the output and

**Dave Jones:** there it is. That's exactly what we're getting. Um, if I switch off my supply, of course, it just goes blip and there we go. I switch my supply on. So, we're It's jumping around a bit there, but it's close to zero. We're just getting

**Dave Jones:** some noise there. That's why Actually, this one goes down to 1.8 volts, actually. Let's see if this one varies with supply. There we go. Oh, oh, that Wow, there Oh, there we go. Minus 350. So, this one does vary.

**Dave Jones:** This one is rated from Look, it's here. Where it is, plus 1.8 volts to 5.5 volts. There you go. So, uh that one on the low side there, but once it gets There you go. Once it gets sort

**Dave Jones:** of 2.1 volts there, but sort of at at that uh 2. um 7 volts uh which we were using before for the other ones as a reference, basically zero. So, well within uh spec, of course. We're only talking, you know, 0.1, 0.2

**Dave Jones:** microvolts or something like that offset voltage. And we wind the wick up and no, it's not really increasing. So, it's doing the same as the maximum chip pretty much. It's offset voltage. Pretty con- Oh, no, hang on. No, no, there we go. Pretty consistent

**Dave Jones:** over the voltage range. I mean, uh you know, to get rid of that noise, we could probably like turn on some averaging or something like that. This Microchip one's performing the same as the Maxim one. So, it looks like the Analog

**Dave Jones:** Devices one is something peculiar with that. So, I put my Analog Devices one uh back in here and of course, this is um not using the split uh bench supply anymore. It's uh utilizing the uh split supply on my microcurrent here, but it

**Dave Jones:** doesn't seem to make any difference whether or not I use the split supply the op-amp virtual ground split supply on here, or my bench supply, as you'd expect, really. You wouldn't expect any difference, but there it is. I've got

**Dave Jones:** the average mode on there. And down at 2.7 V, it's, you know, you know, it's very low, very respectable. But let's wind the wick up and up, and we can turn that off. Actually, I'll turn that off. Boom.

**Dave Jones:** There we go. We're getting in our 400 microvolts. There we go. Yeah, that average would have taken some time to uh creep up there. But look at that. There you go. So, there's something with that split supply. Unbelievable. But even going back to our

**Dave Jones:** original one here in um single-supply rail operation, um it still does vary. So, from 2.7, we're getting uh 50 uh sorry, uh 0.54 microvolts offset voltage, and it does actually does actually go up. I mean, you know, it practically

**Dave Jones:** doubles there. Whoops. Practically doubles um over the operational supply voltage range. And just for fun, what I've done is I've actually uh desoldered these uh 0.1 microfarad bypass caps. I'm back to a split supply uh plus minus with the um split ground here, and I've

**Dave Jones:** replaced that with a single cap between the positive and negative supply directly across the chip there. And uh let's have a look at what we get. We're getting about uh 200 uh microvolts or 2 microvolts uh offset voltage there at 5

**Dave Jones:** V, but if we wind that wick down, it drops significantly faster than what it did before. Look at that. Now at uh 4 V, it's sort of, you know, at the level we expect, and it's gone a bit negative.

**Dave Jones:** Look at that. Isn't that interesting? By the way, that was a 330 nanofarad directly across there before. Now, what I've done is just soldered the negative one back in there and I'm just using that. I've got no bypass in the uh

**Dave Jones:** positive rail there. And uh 2.7 and up we go. Look at that. Look at that. And now it's significantly worse at that 5-V rail there. Uh-huh. And now I've soldered in the other cap. Once again, 100n, so I'm back to our

**Dave Jones:** original configuration, 100n, 100n bypass with a split supply and uh this is what we're getting and this that's a 2.7. And we can where Look, we're back to our original configuration, basically. So, there it is. There it is. It's got something to do

**Dave Jones:** with the bypass caps and presumably uh the input I don't know. It's something to do Well, you know, it's probably got something to do with the internal uh operation of the auto-zero uh chopper amp inside this thing. Um you know, I

**Dave Jones:** don't know the exact configuration in there. So, you know, if Who knows, right? Only um Analog Devices could uh tell us that, but uh uh there is a difference when we put in different value caps for the bypass in different

**Dave Jones:** configurations. So, maybe it's got something to do with the input bias currents um to the op-amp, but why that matters when they're both effectively tied down to the same star point like this, um I Gee, I don't know. So, I'd love to give you

**Dave Jones:** an exact solution for this one, folks, but uh unfortunately, I don't. That's as far as I've uh gotten and really um I'm rather perplexed. Maybe there's something uh incredibly simple and it's a well, it's going to may turn out to be

**Dave Jones:** something embarrassingly simple, but I don't know. I just haven't been able to get to the bottom of this uh stupid thing and um it's got something to do with this particular Analog Devices one. The others don't actually uh show this

**Dave Jones:** issue at all. Both the Maxim and the Microchip part don't show it. It's only this Analog Devices and it's still an awesome uh chip, by the way. I'm still going to use it. This is just a really, you know, I'm going to put a regulator

**Dave Jones:** in there. The power supply is not going to uh vary anyway. So, you know, it's not going to be an issue, but I just when I first uh discovered this, I just thought, "What the hell's going on there?" It's rather interesting. So, I

**Dave Jones:** thought I'd at least investigate it. So, it's not a huge deal, but it's just interesting. So, if anyone from Analog Devices is actually uh watching and can shed some uh light on this, please do. If you're got any uh better ideas

**Dave Jones:** yourself, uh leave it in the comments or on the uh EEVblog forum and maybe it's got something to do with the patented, oh yes, there's the problem. They patented the damn thing, um ping-pong operation they call it. It's auto zero

**Dave Jones:** and uh chopping um at the same time in some unique patented configuration. I don't know. Maybe it's got something to do with that. But, it's really really bizarre. And why those uh capacitor values and configurations uh make a difference, the bypass uh

**Dave Jones:** caps, I don't know. In theory, they shouldn't uh really. Maybe it's uh you know, something to do with the um just the input configuration of this chip and the chopping nature and etc. etc. the topology used in this particular analog

**Dave Jones:** device is one cuz I don't seem to get it with the maximum or the microchip part. I don't think I've ever seen anything like this before and well, yeah, it could turn out to be embarrassingly simple. I don't know and I'm probably

**Dave Jones:** just making a dick out of myself but anyway, that's just some playing around with the input measuring the input offset voltage and by the way, if you're wondering, no, you can't just put your multimeter on there and even if it's a 6

**Dave Jones:** and 1/2 digit one and measure your offset voltage on there. It's actually internal generated internal inside the circuitry in there. So, you know, you could have a big blob of solder between those and you know, you're still going

**Dave Jones:** to get this input offset voltage is inherent in the design of all op amps even these ultra low offset ones. In in this case, you know, like the best on the market is you know, 0.1 microvolts or something like that

**Dave Jones:** which is the maximum one I think anyway, typical figure but worst case and yeah, so we learn a bit about worst case and bell curves and all sorts of jazz. So, I hope you found that interesting. That's just me

**Dave Jones:** looking at a few little issues in input offset voltage. So, hope you enjoyed that and if you like well, this really wasn't a Fundamentals Friday. Sorry, it was just a me around but yeah, anyway, hopefully you found it interesting and

**Dave Jones:** if you do like it, give it a thumbs up. Catch you next time.
