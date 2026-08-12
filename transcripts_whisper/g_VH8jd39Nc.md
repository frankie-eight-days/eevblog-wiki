---
video_id: g_VH8jd39Nc
title: EEVblog 1533 - How To Estimate Product Battery Life
url: https://www.youtube.com/watch?v=g_VH8jd39Nc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 38, "3": 51, "4": 73, "5": 85, "6": 100, "7": 115, "8": 140, "9": 155, "10": 169, "11": 183, "12": 203, "13": 218, "14": 235, "15": 253, "16": 270, "17": 292, "18": 308, "19": 320, "20": 335, "21": 348, "22": 367, "23": 384, "24": 401, "25": 414, "26": 435, "27": 451, "28": 461, "29": 482, "30": 494, "31": 514, "32": 530, "33": 542, "34": 558, "35": 572, "36": 592, "37": 608, "38": 626, "39": 638, "40": 658, "41": 674, "42": 688, "43": 706, "44": 718, "45": 736, "46": 751, "47": 766, "48": 786, "49": 804, "50": 826, "51": 839, "52": 856, "53": 869, "54": 886, "55": 900, "56": 920, "57": 934, "58": 952, "59": 966, "60": 990, "61": 1007, "62": 1027, "63": 1046, "64": 1064, "65": 1083, "66": 1096, "67": 1111, "68": 1127, "69": 1148, "70": 1167, "71": 1188}
---

**Dave Jones:** Hi, somebody on the EEVblog forum asked what is the battery life of the BM786 multimeter? And, well, the answer is I don't precisely know. And, of course, it depends on the type of batteries you're using in it, of course. The specs in the manual are just that it is just the current consumption, i.e.

**Dave Jones:** 8 milliamps in most normal functions, 10 milliamps in AC plus DC. So, anyway, I thought we'd actually measure that and then actually look at how you would estimate the battery life of a product if you can't simply plug the batteries in and leave it on and have a timer there, you know.

**Dave Jones:** If you've got something that's got hundreds of hours battery life, then, you know, that could be a problem. Sometimes you want to get a nice quick estimation of a battery life. So, let's see how we do that. And I'll link a video up here and down below if you haven't seen it.

**Dave Jones:** It's from my second channel from quite a few years ago on why. 121 GW multimeter uses AA batteries instead of 9-volt batteries. And that has some interesting stuff in it, if you're interested. So, the BM786, it uses three AAA batteries like this in a quite unusual vertical battery configuration like that.

**Dave Jones:** It's got a spring and terminal down there, which makes it a real pain in the butt to get in there and actually measure. So, we could, of course, skip this measurement and just use the datasheet value. But let's double check to see what brought...

**Dave Jones:** ...the power consumption is. They say 8 milliamps. Well, let's actually measure it. Put some tape in there, just a temporary thing like that. And there you have it. On DC volt mode, it's 5 milliamps. It's not 8 milliamps, so it's less than we thought.

**Dave Jones:** Three AAAs, of course, a nominal 4.5 volts. We can actually go above that. And it's going to stay the same current. And it should stay the same current when we drop it like this. Let me explain why. Let's go to DaveCat here, and I'll show you how this particular load, i.e.

**Dave Jones:** this multimeter, actually works. It's going to have a linear regulator inside. None of that switching regulator rubbish. It might have multiple linear regulators, but for the purpose of this discussion, it doesn't matter. We've got our battery over here, okay? And then we've got our current draw from the battery, which is what we just measured, that 5 milliamps or so.

**Dave Jones:** And then we've got current, which goes into the load, which is all the circuitry for the multimeter. Now... Of course, the load can switch, and you can have, like, you know, pulse currents and all sorts of things. But a multimeter like this is, like, a fairly consistent 5 milliamp load there, as you saw.

**Dave Jones:** So this linear regulator, of course, is going to have a little bit of quiescent current. It's called down here, which is why I've labeled it IQ like this. But generally, that's in, like, the microamp region or something like that. Whereas your load is in the milliamp region.

**Dave Jones:** So as a rule of thumb in electronics, anything more than, like, two orders of magnitude. So, you know, 101, 100th of something. You can pretty much rule it out. That's, like, 1% error. Doesn't matter. And if you get lower than that, well, it, you know, it just becomes insignificant.

**Dave Jones:** So you can rule out IQ. So for a linear voltage regulator, and this is something you should know as a basic building block thing for regulators like this, is your output current, your load current, is equal to the input current. So effectively, because the linear regulator is a fixed voltage across essentially a fixed load,

**Dave Jones:** you're essentially getting a fixed... a fixed current, or a constant current, essentially. So as you'll see in a minute in the battery data sheets, we're drawing from the battery essentially a constant current load. If you're using a linear regulator, that's what you got.

**Dave Jones:** Switching regulators, very different thing. Anything with changing loads, very different again. But in this case, we've got essentially a simple constant current load, which makes things really easy when we're trying to estimate battery life, as we'll see shortly. Just as an aside, the reason I'm using this Roden Schwartz NGA 100 power supply is because it's the only power

**Dave Jones:** supply I've got here that has a real low current mode. It's got, like, precision measurement capability, ideal for measuring low current devices like this. As you can see, it's got one microamp resolution there, which is absolutely incredible. And I can actually go in there and modify that to, like, a fixed high range, for example,

**Dave Jones:** and you'll see that even in the 2 amp range, it can get 10 microamps resolution. Terrific stuff. Not all power supplies have this, and if your power supply doesn't, very likely, then you'll have to add a multimeter in series with the output to measure the current.

**Dave Jones:** And here is where you can come a gutter, because here's where burden voltage becomes a big problem. And this is why I developed, specifically, the microcurrent, so that it minimizes the burden voltage of your multimeter. Because the absolute last thing you want when you're trying to measure the voltage dropout point of your product over here,

**Dave Jones:** because we have to adjust this 4.5 volts until we get down to where, you know, the low battery warning comes on, or the product stops working, so we need to know what that voltage is precisely. So I'll illustrate the problem here. You've got your power supply, you've set it to precisely 4.00 volts, okay?

**Dave Jones:** And then, but it doesn't have an accurate current meter, so you have to put an external multimeter in here, and the current shunt inside the multimeter has a resistance, and that's going to have a voltage drop when the current flows through it. It's just simple Ohm's law.

**Dave Jones:** So depending on the current range you choose in the multimeter, depends on which value shunt resistor you have, you're going to get a voltage drop when you pass current through your device under test. Now, if you're at very low currents, it may not matter, right?

**Dave Jones:** But then you don't get the resolution on your current range on your multimeter like you might want. So you might think that you're at 4.5 volts battery, and that's where you see your battery dropout sign come on, but you're actually, it's like 3 volts, or 3.5.

**Dave Jones:** Some multimeters can have like a 1 volt burden voltage on them, or more. Now, of course, to overcome this, you can put in a second digital multimeter in here, and you can actually measure the voltage actually right at the input terminals, but you're going to need

**Dave Jones:** two multimeters for that. As I said, always have two multimeters. So just be careful, you can really come agutza with that, and your measurements won't be accurate. Now, you could, of course, have a low burden voltage multimeter like the 121GW, but there's not many on the market that have low burden capability, but it

**Dave Jones:** just be aware, just because it's low burden, it's lower than a regular multimeter, but it might not be low enough for your particular requirements. Just be aware of that, read the manual, know what your burden voltage is. And for those playing along at home, in AC plus DC mode here, we're measuring about 9 milliamps.

**Dave Jones:** And if you want to know what happens if I turn the backlight on, there you go. Backlight, it's a killer! 42 milliamps! Anyway, let's measure and then estimate the battery life of this product, without having to time the thing. So we'll take that as 5 milliamps.

**Dave Jones:** And we start out at the maximum voltage there, 4.5 volts. It could go above that, but, you know, it won't stay that far for long. For alkaline batteries, for example, if you're using lithium, it could go higher. But as I said, we can actually go in there, and if we adjust the

**Dave Jones:** voltage, 5 volts, for example, there you go. It's still only going to be drawing 5 milliamps, because as I said, it's a constant current load. Then, now lower this until our battery icon comes on, or however you determine that your product stops working.

**Dave Jones:** Now just be aware, there may be some lag on the time it takes for the low battery symbol to come up. So, I know it's not going to be 4 volts, so there's no need to muck around there. So it's going to be somewhere below that.

**Dave Jones:** There we go. I saw it come on there at 3.5 something, so at 3.6. Oh yeah, 3.58. Now there could be some hysteresis here. when it actually switches back off, but there doesn't really seem to be. Yeah, so let's definitely say 3.58 volts

**Dave Jones:** there, okay? And we're going to assume that the meter is still accurate just at that point where it comes on. Now, of course, you could go into more advanced stuff, like actually measuring the performance of your instrument, but that should have been part of your design

**Dave Jones:** process, rather than just, you know, like estimating the battery life, which is what we're doing here. Now, 3.58 divided by 3, get the confuser out, that's a smidge under 1.2 volts, so we definitely aren't extracting all of the energy from these AAA batteries, because I've done a ton of

**Dave Jones:** battery videos, and I'll link in the playlist down below. And batteries do contain usable energy right down to 0.8 volts, but in products like this, that use a linear regulator like this, or multiple linear regulators then, so yeah, it is common to waste

**Dave Jones:** some energy in your batteries like this. And that's just an unfortunate side effect of a product like a multimeter, that you don't want to have a switch in power supply in here, because that can screw things up. You know, this is a precision measurement device.

**Dave Jones:** So the last thing you want in this is a switching converter to power your like, dual-slope A to D inside this thing. You know, precision measurements, nah, yeah, no thanks. So it's common in products like multimeters like this to sacrifice some of the energy in the batteries

**Dave Jones:** for measurement performance. And, uh, simplicity. So let's look at some data sheets. Let's just take a Duracell UltraPower AAA here, and we know we've got a constant current load here, and this will go into the different, uh, varieties. And sure enough, look at this!

**Dave Jones:** Constant current graph. They've got two constant current graphs here, but wah, wah, wah, wah. Murphy's Law, wouldn't you know, they've got 1 milliamp and 10 milliamps. They don't have 5 milliamps. And as you can see, there's quite a large discrepancy between these. So you could actually, like, try and guesstimate it, like,

**Dave Jones:** by sort of matching that, but like, it's probably not gonna be in the middle. It's more likely to be, like, further over to here. It's gonna be a non-linear thing, going from 1 milliamp here to 10 milliamps here. And then, as I mentioned, there are different

**Dave Jones:** load types. Like, if you had a DC to DC converter in your product, for example, then, all things being equal, it's essentially a constant power. thing. But of course, it has to do with the draw, like the efficiency of your DC to DC converter over the load range, and all sorts of things,

**Dave Jones:** right? But essentially, if you've got a DC to DC converter, you'd be looking more at the constant power graphs than you would for the constant current graphs. Now, unfortunately, we can't just use Ohm's Law and, you remember, the voltage is dropping like that.

**Dave Jones:** So yeah, it's not the correct thing to use. And also, a thing to note that is these, all these things will not only depend on the manufacturer of the battery, they'll depend on the batch of the battery, they'll depend on the type of the battery,

**Dave Jones:** they'll depend on the chemistry of the battery, and they'll depend on the temperature as well. And you can see here, for the same draw, they assume it's, like, constant power draw. Look, there's quite a difference in service hours from, like, 3 hours up to 9 hours here

**Dave Jones:** of battery life from minus. 10 to 21 degrees. So that's only a 30 degree. Well, 30 degrees is a lot of temperature differential, but that is a huge difference in battery life. 2.5 hours to 9 hours just for temperature. Right, so we go over to an energizer over here.

**Dave Jones:** Well, they've got a milliamp hour capacity here, continuous discharge at a constant discharge current. So constant current, but, wah, only 25 milliamps. That doesn't help us. We need 5 milliamps. And then down here, on the industry standard tests, these are actually a resistive load.

**Dave Jones:** 5 ohms, 24 ohms. They've got one down here, which is a constant current, 250 milliamps. They've got another one, which is 50 milliamps down here. But they're, like, milliamp hours per day and stuff like that. So, yeah, nah, it's not what we want.

**Dave Jones:** Now, of course, if we want the ultimate battery life in a product like this, we would use a lithium primary battery. Check it out, our discharge profile. We don't get 5 milliamps. We only get 1 milliamp and 10 milliamps. But look at the differential, right?

**Dave Jones:** In these graphs, unfortunately, it's not rendering. My PDF viewer is not there. It didn't render that properly. I found a bug in Drawboard PDF, which is a software I use. A lot of people actually ask me which software I use. Anyway, you can see that it is

**Dave Jones:** somewhere between these two lines here, right? And as you can see, the longer up you go, the more battery you discharge, there's essentially no difference between 1 milliamp and 10 milliamp draw, essentially. So we're essentially good to go. We can accurately use this.

**Dave Jones:** So where did we determine? It was just under 1.2 volts, if you remember, per cell. You remember, we've got three cells in series. So we were 3.58 volts divided by 3. So you can see, down at 1.2, if we extrapolate that over here, you can see that we're

**Dave Jones:** really extracting pretty much the absolute maximum energy out of a lithium battery. Beauty. We're not wasting any, as we'll see that we will. in an alkaline. So, yeah, fantastic. So let's just call that, like, 1,200 milliamp hours. So we get the confuser out.

**Dave Jones:** 1,200 milliamp hours divided by 5 milliamps there. 240 hours of battery life for the BM786 on using these lithium primaries. So that's going to be reasonably accurate. And temperature should have lesser effect on these as well, which is one of the advantages. Do they actually have

**Dave Jones:** a battery life? And you can really see, look at this, you can really see the ESR just, like, go through the roof right there. This is how batteries die. Their internal series resistance just suddenly goes, and, yeah, and it just doesn't give you the volts

**Dave Jones:** anymore. Like, well, you're talking Kirchhoffs now. And they do have a nice graph over here. And as I mentioned before, that non-linearity, right, they actually show you. They use a log graph here. This is constant current here. So 2, 3, 4, 5, and

**Dave Jones:** 5. So 5 up there. Yeah, we're talking about that 240 odd hours we were talking about before. So, you know, that line's a bit rough and ready. But, yeah, you can get an estimate from that. And, yep, they give us a temperature effect on capacity for

**Dave Jones:** constant current. Unfortunately, only at 25 milliamps there. But you can see that 25 milliamp is the thick one there. So at the lower currents and 5 milliamps, that'd be, like, flat as a tack, right? So there's effectively no change, you know, in the

**Dave Jones:** battery life over temperature with these lithiums. But that's what you expect. That's why you pay a huge premium for them. Anyway, we want alkaline or manganese dioxide or zinc manganese dioxide here for those playing along at home. So let's go to the Energizer again.

**Dave Jones:** But this is the Energizer Max. You can see that this Energizer Max data sheet is significantly different. It's got milliamp hour capacity and then constant power performance, constant current performance here. Whereas before, we got, like, these industry standard tests so the Max version is, you know, significantly different data

**Dave Jones:** sheet. We do have constant current performance. What do we got here? Well, lowest value we've got is 10 milliamps here. So 5 milliamps is off the graph. So our 1.2 volts cut out, you can see how all of these manufacturers, like, even the

**Dave Jones:** same manufacturers can give you totally different curves. You know, you've got to be able to interpret all these different types of graphs. This one gives you a characteristic curve of voltage here, like this, approximately. So, you've got against the discharge in milliamps and giving you the service hours so we would

**Dave Jones:** have to extend this graph right up here like this to try and get our 5 milliamps here but as I said it's a logarithmic scale anyway so we do know the figure is somewhere above a hundred and should at least do that so we can go to it like a

**Dave Jones:** Philips brand here I don't give us anything oh let's try the Germans Varta shall we discharge type load five arms 24 once again this industry standard stuff here that's all they got let's go for a Panasonic jobby shall we and once again we've got like significantly different characteristic we've got load

**Dave Jones:** in milliamp like this is real old school like they've like plotted this like on an actual pen plotter or something but once again the five milliamps that we want if we extrapolate that up the curves don't go that far once again is the end voltage per cell so we're looking at the 1.2 volt curve

**Dave Jones:** here so yeah like eyeballing that it's somewhere between a hundred and fifty hours and 200 hours I'd say it's not more than 200 hours like we've got nothing that's absolutely precise yet then we've got this Panasonic alkaline handbook here once again you can see that they stop at 10 milliamps here but

**Dave Jones:** you know once again 1.2 volts this is the lowest curve here I don't know that's a bit how you're doing in that five milliamps go up there like that and yeah we're talking a hundred and eighty hours so as it turns out on that same EEV blog forum thread which I'll link him down below for the

**Dave Jones:** BM 786 Joe Smith following his videos down below you know does multimeter destruction multimeter extensive multimeter testing that's pretty much all he does on his channel he measured a hundred and eighteen hours on the BM 786 I you know it's like a hundred and eighteen is like is down here I can't

**Dave Jones:** see a tail in off like that but as I said huge discrepancy temperature battery type battery brands slightly different electrochemistries between manufacturers all sorts of things apparently some people have measured like eight milliamps on the BM 786 so it seems to be some variability in the

**Dave Jones:** actual meter itself so anyway it looks like it's easily gonna get a hundred hours we could split it say a hundred and fifty hours something like that I think mine at five milliamps will actually last probably a hundred and eighty hours something like that I can do another

**Dave Jones:** follow-up video leave it in the comments down below if you want me to do that anyway there's like more you can do to this and obviously nothing beats actually putting it in the product itself especially if you get any sort of pulse currents and as it turns out that rodent Schwartz power supply I just

**Dave Jones:** press the log button there it is like the five milliamps because you can see just in DC volts mode there's not really a huge discrepancy in the current there and I think most other modes will probably similar when it flashes the backlight and stuff like that backlight seems to be you know a major thing but

**Dave Jones:** easily get 240 hours for those energizer lithiums over here but as I've shown you in many other videos the voltage that you set over here for it like the minimum dropout voltage for your product that determines how much energy you actually waste and in this particular case the energy you have to extend this

**Dave Jones:** all the way down to there all the way down to zero volts down here this just drops off like a rock here but all of this under here is the energy the area under the curve is the energy so all that energy is wasted so compare the area of that compared to the area under

**Dave Jones:** this side of the curve here and that's how much energy you're wasting in alkaline batteries where you don't waste that in the energizer lithium ones you saw there is no area under the curve right you wasted practically nothing of that battery it's it's fully discharged so your batterizer ain't gonna extract your 800% it's not

**Dave Jones:** gonna extract an extra 8% really so I hope you enjoyed that video and found it useful if you did please give it a big thumbs up as always discussed down below catch you next time
