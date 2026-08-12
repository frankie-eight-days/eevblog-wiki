---
video_id: qo0mizb3CE8
title: EEVblog #1094 - Casio FX260 Solar II Calculator Tritium Nuclear Battery Experiments
url: https://www.youtube.com/watch?v=qo0mizb3CE8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 37, "3": 52, "4": 70, "5": 82, "6": 100, "7": 115, "8": 127, "9": 151, "10": 172, "11": 187, "12": 202, "13": 217, "14": 232, "15": 253, "16": 274, "17": 292, "18": 313, "19": 331, "20": 349, "21": 364, "22": 385, "23": 403, "24": 418, "25": 439, "26": 460, "27": 472, "28": 493, "29": 511, "30": 532, "31": 547, "32": 562, "33": 583, "34": 598, "35": 619, "36": 640, "37": 661, "38": 682, "39": 706, "40": 724, "41": 745, "42": 760, "43": 775, "44": 796, "45": 814, "46": 832, "47": 850, "48": 868, "49": 889, "50": 904, "51": 922, "52": 940, "53": 952, "54": 973, "55": 988, "56": 1009, "57": 1027, "58": 1042, "59": 1060, "60": 1081, "61": 1102, "62": 1114, "63": 1132}
---

**Dave Jones:** Hi, in the previous video we took a look at this Casio FX-260 Solar II calculator, did a review and tear down of that, I'll link that in if you haven't seen it, but we saw that it had a spare pad in there with potentially a spare reservoir

**Dave Jones:** capacitor, because this is only solar powered and it does operate for a little bit, but eventually it will actually die on you. So it does a reasonable job, but I thought maybe we could actually hack it, add in some extra reservoir capacitors and see if we can actually get that working a bit better

**Dave Jones:** potentially, maybe probe some signals around. Let's take a look at it. And by the way, for those people who suggested that this pattern in here was like a carbon fiber, and this front panel might actually be carbon fiber, I don't think it is.

**Dave Jones:** It's just designed to look like that. I think it's just you know, like embossed kind of plastic or whatever you call it, giving it that cubit type carbon fiber look. But I doubt it's carbon fiber on a $9 retail pocket calc. So here's the inside,

**Dave Jones:** there's not much to it, there's a blob, there's a couple of passives around here, there's the solar cell, and there's the LCD. So what we're interested in are these passives here, and you might be able to see that there's an unpopulated capacitor there.

**Dave Jones:** And it looks to be in parallel with this one next to it. And that looks like it's probably the reservoir capacitor for the power rail coming from the solar cell. So the charge on that determines how long it's going to last when you remove light from the

**Dave Jones:** solar cell. Now one thing I was curious to try, I've got this tritium nuclear battery here, which I got from NerdRage who sent this to me. I'll have to link in his video at the end of this. I've always been meaning to do something

**Dave Jones:** with this, and I will eventually. So I thought I'd try it. It's got these tubes with tritium in them, and they glow in the dark. It's almost pitch black here in the lab, and my camera's gained up and you can see all the noise and crap.

**Dave Jones:** I just wanted to see if this was enough to actually power the unit. And well, unfortunately, on, on, it ain't. So we're not going to get a nuclear-powered battery anytime soon. Now I believe this one which he made and sent to me, he did actually fully

**Dave Jones:** characterize this, and you'll have to watch his video to get the performance graphs. The peak power out of this was I think 1.2 microwatts. So obviously yeah, that's not good enough. Bummer. Anyway, what we're interested in is that little capacitor down there, and you can see that

**Dave Jones:** the C107 there is in parallel. You can see the traces going across. So like it buggers off in there, and of course it's going to this like ground, what looks like a ground over here. But we need to measure that, and then it goes into these

**Dave Jones:** three caps here, and no, they're probably charge pump caps, because they go in and out of the chip like that. These ones are three going to ground, so maybe there's some decoupling for the LCD driver for the divider or something like that perhaps.

**Dave Jones:** But anyway, I think my theory's right, this is the reservoir cap, and we should be able to add another one in parallel. Like I'll try and find the biggest, like what is that, no 805 ceramic, the biggest or even, you know, jam a 1206 on there

**Dave Jones:** or something. See if I can find like a, I don't know, how high do they go these days, these newfangled ceramics, like 100 mic or something probably. So let's just buzz this out, let's go from the negative over here, and it doesn't go all the way through, you can see it sort of like snaking around

**Dave Jones:** there. And anyway, let's just buzz it out, see if that actually goes to the negative side here, and yep, confirmed. Oh, got to have sharp probes. There we go, no wuckers. So that's ground. Next, let's see if there, that's going in there as well, let's see

**Dave Jones:** if this goes to the positive side. No, it doesn't. Okay, so there's something else in the way of that solar cell. That's interesting. Hmm. So although that doesn't connect directly across the solar cell, still makes sense that that is the reservoir cap. In fact, what we can do is actually suck that out

**Dave Jones:** and see if it still works. But let's, before we get medieval on its arse and start heating the bastard up, let's just probe some signals. So flip the solar cell, all the electrons are going to fall out, let's just measure our battery oh, battery, our solar cell voltage, there you go, 2.75

**Dave Jones:** that's alright, no wuckers. And let's go on the other side of this cap here. See what we get. Oh, 2.86 I may have moved that, so 2.86, let's not move anything. Oh no, there we go, yep. So it's exactly the same voltage on there, so that's pretty much

**Dave Jones:** confirmed that that is the reservoir cap. As you'd expect, it's the biggest cap on there, it's connected through to ground, it's got to be the reservoir cap. But because it doesn't actually connect directly through to there, then ah, 24 ohms, there you go, there's probably

**Dave Jones:** some like internal, let's put it the other way ah, yeah, well no, there you go there's some sort of switch in that there's probably some MOSFET switch or something in there doing that. Okay, I've sucked it out let's measure that baby, how about

**Dave Jones:** what have we got, yep, 24 ohms let's measure that baby, how about, what have we got yeah, couple of mic, 16.8 mic yep, that's a reservoir cap if there ever was one let's see what we've got, well let's see if it works without it first

**Dave Jones:** let's have a look, does it? should, and it does but, cover it up, shouldn't last very long yep, there you go, so for those playing along at home, you can actually calculate probably what value cap, like how much longer it's going to last, if that's 16.8 microfarads

**Dave Jones:** and it starts fading pretty much straight away, oh maybe, I don't know you could kind of ballpark that how much better, anyway, I'll see what value caps I've got I'll whack two of them in there, how much height we got I don't think we've got a problem in the back of our case here

**Dave Jones:** look at all the nice ridges in there, that's holding in, you can see the marks on there, holding in the solar cell that pad there's holding the LCD in place very nice, they've got all the struts in there for rigidity, whatever you want to call the damn things

**Dave Jones:** and we should have no, yeah, we should have no shortage of room in there, it should be in that void in there actually she'll be right, this'll do the business passive components for energy harvesting that's exactly what we want, AVX kindly sent these into the mail bag, you may remember some time back

**Dave Jones:** voltage is never going to be an issue in this case 1 mic, 10 mic, 2.2 mic, 47 mic they're a 1206 we can still put those on and they drop back out, they go up in voltage no, oh man we've got some super caps in there, look at that

**Dave Jones:** if you put the room in there, you could put like a small tantalum or something like that, they're too big they're not going to fit on the pad, or you could bodge them in, but you know, meh. But this could be more interesting, look at this

**Dave Jones:** the mobile sample kit, not only have we got tantalum but we've got niobium oxide niobium? That's near enough oxide solid electrolytic caps, check out this bad boy, a size S package sort of like equivalent of a 0603 type size 100 mic at 6.3 volts

**Dave Jones:** now we're talking, ESR isn't going to matter but yeah, these are designed for like mobile phones and stuff like that, but 100 mic again no wuckers, look at that, tiny little tantalums tantalum or ceramic in this particular case isn't going to matter, but oh wow

**Dave Jones:** 220 at 4 volts, now we're going oh, it's tempting to put those bad boys on there, we're going to get 440 mics on there, oh I think we're talking now yeah, more capacitance. Now here's an example where case size matters, they're both 220 microfarad

**Dave Jones:** right? But look at the ESR, 3000 milliohms or 3 ohms or 150 milliohms for these ones, and they're both, there's not much in the voltage, you know, yeah these are going to be smaller because of the smaller voltage but look at the size difference, these are D size

**Dave Jones:** tantalums as opposed to these cute little S size jobbies down there, and they're both the same capacitance, look at that, but that's what the larger size gets you, not only can it get you higher voltage well, it's a trade-off, but also gets you much lower ESR as well.

**Dave Jones:** But in this particular application, ESR doesn't matter a rat screw them, these things should last forever, but the trade-off is that it could actually, like, change the startup, because that cap will take time to start up. So you can't put like an infinite amount of capacitance in there

**Dave Jones:** with low ESR, because it'll just suck all the energy from the solar cell, effectively short it out, and it'll take too long to power on. So there's going to be a trade-off in there, this may not start up straight away. And that is what a soldering iron burn

**Dave Jones:** looks like. Just... don't ask. Alright, I only soldered one on there because it didn't quite fit, it was just easier to angle one across. So let's have a look. Ta-da! It works. Okay, let's see how long it works for. Here we go. 69 factorial.

**Dave Jones:** That's given it a heck of a workout. Poor little processor. She's still going and going. It's like the Energizer bunny which then became the Duracell bunny in a stroke of reverse marketing. Um, yeah, it's doing much better than what we had before. It's kicking some serious butt.

**Dave Jones:** Here we go, it's starting to fade now. Oh, yep. Still, yeah, it's gone. Basically it lasted about 2 minutes. But that's a decent upgrade. And this is interesting, if I actually put this on current and short out the solar cell we basically don't...

**Dave Jones:** oh, no, it wasn't doing it before. Anyway, let's switch it back. Notice the LCD's actually, it's coming back there because we've got some charge building back up on that cap after we shorted that puppy out. So, please excuse the beeping, but let's short the cap out

**Dave Jones:** directly, shall we? There you go. You can short it out directly, and that sucker still works. That's interesting. I found an interesting mode on the EEVblog meter too. If you actually apply some... do something on there, get some current flowing, it actually it overrides the insertion

**Dave Jones:** alarm, the probe insertion alarm. Interesting. But basically, shorting out that cap doesn't stop the processor working. That's fascinating. Okay, so let's try this. Flip the solar cell up, we're at .2 volts, so it's obviously not going to be enough to operate it. See how quickly it turns on.

**Dave Jones:** Ready? See? There you go, there's your prob... it takes a second or two... what was that? Maybe two seconds to turn on? I don't know. So, yeah, you could argue that 220 microfarads might be a bit too much. The trade-off there is, you know, you've got to wait longer for it to

**Dave Jones:** power on, and that's going to be more annoying than any benefit you get from the solar cell. But really, if you're operating this thing, as you saw in the previous video, operates under 20 lux of light anyway. So, you know, we're just doing this for shits and giggles, really.

**Dave Jones:** And for those who want to know what current we're talking about, 50 microamp range here. It's charging up the cap, of course. There we go, don't worry about the negative. Oh yeah, there you go. 35 microamps. Something like that. No wuckers, no wonder we couldn't

**Dave Jones:** power it from that nuclear battery. Alright, it's scopadope time. Let's have a looky here. We've got 5 capacitors here. I'm going to probe the bottom one here, and we expect this to be a charge pump. Ta-da! 150 hertz, you can see that in the bottom left corner there.

**Dave Jones:** That's the next one up. Lower amplitude as well. We're on 500 millivolts per division by the way, so that's the 2.5, so that's full scale. That's half scale. Next one up, nothing. It's got a bit of ripply on there, and yeah, a bit of ripple on it.

**Dave Jones:** So yeah, they're probably bypassed for the LCD ladder. And that one's, ooh, right up the top. So right up the top, 1 volt per division. There we go. So that's the high, oh, there we go. 1, 2, 3 and a half volts, so there you go.

**Dave Jones:** Oh, ignore the man behind the curtain there. And for those who are curious to see the LCD drive levels, well, here's one of the segments over here. There you go. Operating at 31.35 hertz. And if we get one of the multiplex pins. Let's try and get lucky, punk.

**Dave Jones:** There we go. There's a multiplex pin. The reason that was dicking around is because of our trigger level I think was right on there. There you go. There's our multilevel DC or multilevel bias for our multiplexed LCD. Is that another one there? There you go.

**Dave Jones:** Neat. Three levels. Standard multiplexed LCD driving. And for those who are wondering, no, I can't find any sort of like you know, pin strap jumper or anything like that to enable the NF model, the no-fraction, which doesn't, which has the button there, but it actually

**Dave Jones:** doesn't have anything printed on it. So I can't actually see anything. Unless anyone can see anything else and you know, pointed out to me had a look around and I can't see anything, so maybe there's some sort of programming that goes on through

**Dave Jones:** the pins or something at the factory. Perhaps. I don't know. But there doesn't seem to be any obvious jumper or pin strap to hack the NF model into the standard model. So I hope you enjoyed that little follow-up on the FX265. I hope you enjoyed that little follow-up on the FX260

**Dave Jones:** solar there, just adding some capacity so that the thing doesn't turn off. Beautiful. Well, it can last for two minutes. There's not much penalty in terms of the turn-on time there. But if it bugs me I might lower it to like 100 mic or

**Dave Jones:** something like that. But that's a reasonable upgrade you're going to want to do to your own calc anyway. So if you liked it, please give it a big thumbs up. As always, discuss down below. Catch you next time. But wait, there's a bonus.

**Dave Jones:** We're going to do a quick teardown of the Casio FX991EX which is basically their top of the class, class whiz that's basically their top-of-the-line non-programmable scientific calculator. Does graphene spreadsheets and the whole, like I've done actually a video in an original mailbag from a long

**Dave Jones:** time back, but I've actually split that out, put it over on my EEVblog2 channel, so I'll link that in at the end of the video here. Anyway, let's open this thing. And by the way, this is fantastic value. The $2.60 is only like $9 US, this is

**Dave Jones:** under $20. So like basically double the price for like 10 times the capability. Absolutely phenomenal. So do yourself a favor and pick one up. Ta-da! There you go. We're in. Ooh! A tronie. I haven't seen a tronie before. Sounds dodgy, doesn't it? Anyway,

**Dave Jones:** that's interesting, they've got metal on the back of there. That's not for shielding purposes, that's for that'd be like a stiffening backplate I would be guessing for that LCD module. Anyway, that's going to have chip on board because we've got a tape bonding attachment here

**Dave Jones:** It's just a hot, hot tape bond on there. And so they're going to have a chip on board chip on tape driver up there because clearly there's not enough segments to drive all that. So that's going to be, in fact that could be like a PCB

**Dave Jones:** in its own right, really. So anyway, there's our storage cap. Done a little cut out there. No wuckers. And it's not much else is there? Once again it's just the black blob. And that's pretty much all she wrote. But once again, yeah fiberglass PCB in there.

**Dave Jones:** No wuckers. And that's, and you can see, actually see the membrane under there like that. There you go. But yeah, I won't take that off, but does the LCD pop out? Hang on, let me show you that. It looks like the glass is embedded

**Dave Jones:** the aluminium backing plate, yeah that's factory fitted. That's the back plate for the LCD. It comes like that. Yeah, for stiffening purposes and probably adds a little bit of heft to it as well, which is you know, probably what you want. So they might have, actually they might have specified that.

**Dave Jones:** Hey, you know we've got this reasonably big calculator, you know, don't want it to slide around on their desk, you know, probably should have used rubber baby buggy bumpers on the bottom instead of these little plastic nipples. Nothing worse than a plastic nipple.

**Dave Jones:** Jeez, there's no fun in that at all. And they went oh let's maybe add some, they specified let's add some heft or something like that, but it could have, you know, who knows. But that's just a guess. Anyway, there you go. That's inside the FX-991EX.

**Dave Jones:** Catch you next time. ♪♪♪ ♪♪♪ ♪♪♪
