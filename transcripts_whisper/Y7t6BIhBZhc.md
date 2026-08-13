---
video_id: Y7t6BIhBZhc
title: High Frequency Active FET Probing DEMONSTRATED
url: https://www.youtube.com/watch?v=Y7t6BIhBZhc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 42, "3": 54, "4": 66, "5": 82, "6": 94, "7": 114, "8": 138, "9": 154, "10": 166, "11": 186, "12": 202, "13": 218, "14": 234, "15": 250, "16": 270, "17": 290, "18": 306, "19": 326, "20": 338, "21": 358, "22": 374, "23": 390, "24": 402, "25": 422, "26": 434, "27": 446, "28": 458, "29": 474, "30": 486, "31": 498, "32": 510, "33": 526, "34": 542, "35": 558, "36": 574, "37": 590, "38": 610, "39": 622, "40": 638, "41": 654, "42": 666, "43": 682, "44": 698, "45": 714, "46": 730, "47": 742, "48": 758, "49": 778, "50": 790, "51": 806, "52": 822, "53": 838, "54": 854, "55": 870, "56": 890, "57": 910, "58": 926, "59": 946, "60": 962, "61": 990, "62": 1010, "63": 1030, "64": 1046, "65": 1062, "66": 1078, "67": 1094, "68": 1110, "69": 1134, "70": 1150, "71": 1166, "72": 1190, "73": 1210, "74": 1226, "75": 1238, "76": 1254}
---

**Dave Jones:** And our next probe, guaranteed to get every engineer all excited. Oh, it's the ActiveFET probe. And they always come in impressive cases like this, and this, and this. Right? You never just, oh, get like a little probe in a packet, whatever. No, they always come in beautiful cases like these.

**Dave Jones:** Let's take a look at them. So here's a very typical active probe, or the ActiveFET probe, or just FET probe, because they've all got FETs right at the input here that actually amplify the signal before it comes in. So they have active amplifier electronics inside the head, as opposed

**Dave Jones:** to your passive probe here, which is just basically a bit of a resistor and a bit of coax, and the amplifier is inside the scope. Well, in this case, the amplifier's up here, which means that they have to actually be supplied by power.

**Dave Jones:** And it's very common for them to actually be powered from the oscilloscope under test. And look at these lovely little pogo pins. And you usually buy them from the manufacturer of the oscilloscope, because they've got their own interface. This one is your Agilent Keysight.

**Dave Jones:** So those probes not only give it power, but they also, you know, tell it what type of probe it is and things like that. Your signal doesn't actually come out on these pins. This is just power and other data. Your signal, of course, goes into your input to your scope.

**Dave Jones:** So it's just, that's a regular BNC, but it just plugs in. It's all captive and they usually have a little lever in there to clamp on the front of your scope. So these things are usually very pricey. You know, they start in the 4-digit category and

**Dave Jones:** go up to like 5 digits. And this one here is a 2 gig bandwidth probe, 10 to 1 divider ratio, 1 meg input impedance. And this Siglet one here, active probe, it's 1 gig with 1 megohm and 1.2 picofarads. But you might think, well, okay, this is 1 gig, well,

**Dave Jones:** so is this. What's the difference? Well, the difference is, remember, this is like practically the world's best passive probe. 3.9 puff. This one, 1.2 puff. And that's the difference. You remember our formula before. Capacitance is the thing that matters at high frequency. And in the case of this Siglet active probe compared to this

**Dave Jones:** Tektronix one, both are 1 gig rated probes, but because it's only 1.2 puff, it's 132 ohms at 1 gig, whereas the passive probe is 40 ohms at 1 gig. So that can make a heck of a difference to the signal that you're actually

**Dave Jones:** measuring. That load is going on the line that you're trying to probe. So the lower the capacitance, the less you're going to load your line. But if you are talking DC, then the passive probe's still better. That's 10 meg at DC. These are only a meg.

**Dave Jones:** So you'd use an active FET probe over your passive probe when signal integrity at high frequency really matters. Well, A, these can go higher. This is actually the fastest pass in 10 to 1 passive probe you can get at 10 meg. And as I said, this thing with a resistor will,

**Dave Jones:** you know, if you build it right, will actually outperform this. And these can actually go up to 10 gig. So, yeah, anyway. So the only solution, basically, for above 1 gig measurement is either an active FET probe or a resistive probe. That's it.

**Dave Jones:** And if you're wondering, this Agilent 1 is 1 puff input capacitance. And this one here, haven't measured it, but it'll like it probably on beyond par. Something like that. In the order of a puff. Half a puff, maybe. So the great thing about active FET probes is they can actually

**Dave Jones:** go beyond 10 gig and beyond the performance of a simple resistive probe like this. So if you're on the bleeding edge of measurement, you're really going to be wanting an active FET probe. So pretty much, as a ballpark, maybe anything over 500 meg, you want to

**Dave Jones:** either be using an active FET probe or a properly built and characterized resistive probe. And, like, it can cost you more money to actually characterize this than to simply buy the already characterized active FET probe. And basically, these single-ended active probes pretty much stop at a couple of gigahertz.

**Dave Jones:** Anything over that, then you start talking a fully differential probe. But not high voltage like we looked at before. These would be low voltage differential probes. High speed, low voltage. But the one downside with these things is Murphy can get really expensive. Like, these probes can cost thousands of dollars

**Dave Jones:** even into the 6-digit range. And their huge Achilles heel is the maximum input voltage. In this case, max input is 20 volts peak. Okay? Seriously, you go over that, and this probe will blow up. You'll probably find eBay's filled with, like, oh, this FET probe

**Dave Jones:** yeah, sold as is. I would not be buying a sold as is FET probe off eBay. Just saying. We've got one from Caltech Electronics here. This one's a little bit more robust. We're talking 40 volts peak here. It's a 2-gig probe. Once again, 10-to-1.

**Dave Jones:** This one's higher input capacitance though. 3-puff. But as you can see, this one, you can get, like, generic ones. You don't have to get these ones designed for your specific scope. You can get these cheaper ones that just plug into your like, any scope, and they're just actively powered, once again,

**Dave Jones:** from just the USB port on the front of your scope. Nice. And as I showed before, these things always come with, like, all these accessories. Let's take a look at them, because they're very interesting. So these are the ones that come with the Caltech probes.

**Dave Jones:** You've got beautiful little ultra tiny mini grabbers there. You've got little ground and probe pins like that. Spare ones, because you're going to be using them all the time. Plus you've got, like, little pins like that. They can plug into headers. And often, on your designs, when you're, if you know you're going to be

**Dave Jones:** probing, like, really serious designs, maybe on a prototype board, you don't necessarily need it on a production layout, but on a prototype board, you're trying to get it working, you're measuring your high-speed DDR bus or whatever, then you might have dedicated test points on there, even dedicated

**Dave Jones:** connectors for these high-speed probes. And the Siglent ones, once again, you get all these, like, spare tips, because you're going to be going through them like there's no tomorrow. You might even want to directly solder the tips into your circuit so that you can physically remove your probes.

**Dave Jones:** The most interesting kit comes with the Keysight one. Once again, you've got a little tube with all the little pins in there. Geez, they don't give you many, do they? A bit of a tight arse, a real expensive probe, yet ultra-tiny mini grabbers once again.

**Dave Jones:** Like, these things are just super, super tiny. And then you, like, plug into there, and give you all sorts of other little adapters like that. And the most interesting thing is, they give you copper pads like this, and they actually give you a bit of a chart here on, you know, some of the different probe

**Dave Jones:** connection techniques. And this is not the video to go into really high-frequency probing techniques, of course. But you can, look, you can plug directly into the head with some long leads like that, and that'll give, like, you know, 500 meg bandwidth here, they're

**Dave Jones:** saying. Or, you know, you can get a rigid probe tip with offset ground like that, so it plugs in. And I love this Keysight head, it's got little LEDs on there that just light up so you can see where you're actually plugging your probe

**Dave Jones:** into. Very nice. And then you've got a spring tip with ground blade like this, and that'll give you, like, 2 gig bandwidth. And then you've got a copper pad which you can solder onto your circuit, and that will give you, like, a flexible ground point.

**Dave Jones:** So, you know, often it's very difficult to apply pressure to, like, both of these points at the same time without one of them sliding around. Well, if you solder in, like, a large ground pad like with that copper tape that they supply, then, you know,

**Dave Jones:** you don't have to worry about your ground probe sliding around, or you do have to keep an eye on it, because Murphy & Shaw will just slide off and short out one of your other pins and something on your expensive $100,000 prototype board.

**Dave Jones:** Trust me, I've worked on $100,000 prototype boards, and if you blew that up, yeah, you're going to be having a bad day. But once again, you know, that might be a slightly reduced bandwidth to, you know, this technique over here, which is going to provide

**Dave Jones:** a lower inductance path, so it's going to, you know, you're going to get better performance at something like that. And then you've just got, you know, if you want to put just pin headers on your board for various test signals, and then little short cables which run over

**Dave Jones:** and just plug into your probe tip. So all these different solutions for probing. And you can even invent your own, and as I said, a lot of designers will solder on like coax connectors directly onto the board and things like that. So you can plug on your own probes, your own resistive probes, or active

**Dave Jones:** FET probes, or whatever it is you're doing. So active FET probes, you can think of those as the Rolls-Royce of oscilloscope probes, really. They're very nice, but as I said, you know, roll your own with a bit of RG174 coax, and well, you can get similar performance if you do it well enough.

**Dave Jones:** But, oh yeah, these can't be beat. If you've got the money. And these probes will usually require 50-ohm termination on your scope, although this CalTest one here, it actually, well, it comes with a 50-ohm terminator. Look at that, 2 gig, 50-ohm in series

**Dave Jones:** inline terminator, 2 watts. Oh, that's very nice. But this one actually lets you use it with a 1 meg input impedance scope, just so you know 50-ohm termination. And it gives you an actual attenuation setting of 5 times. So that's, you know, better for like

**Dave Jones:** low signal measurements. Nice. Okay, let's give you a probing example here. We've got a Raspberry Pi 3 for those playing along at home. And we're going to probe one of the memory pins on the bottom here. I don't care which one, I've just picked one at random, we're getting a signal on it.

**Dave Jones:** So I'm using the 2 gigahertz active probe here, the N2796 overkill for what we're doing. Well, overkill for this scope anyway, because this is a 500 megahertz bandwidth scope. So this active FET probe, more than good enough for measuring the bandwidth that we've got here.

**Dave Jones:** So I'll use this long lead here for my ground. I'll put it on the ground pin of the connector there, because that's just very convenient. For those who care about such things, you can actually see what point I'm probing. Where is it? I think it's there.

**Dave Jones:** Jeez, I can barely see that. This is where, you know, magnification comes in. Okay, I'm probing A point there. I don't know what it is. I don't care. There it is. There's our signal. It's made up of a whole bunch of stuff. But basically, you can see, look, it's got some undershoot here.

**Dave Jones:** It's got a little bit of ring in there. It's got a little bit of ring in there. I'm going to hazard a guess that that's going to be due to our long ground lead there, right? So that is our thing. But we've got actually higher

**Dave Jones:** frequency stuff in here. Look at this. Oh, I just happened to capture one there. Look at this. It goes down, up. We're at, what, 10 nanoseconds per division. We're almost as fast as we can get here with this scope. But this actually does have

**Dave Jones:** some really fast pulses in here. There's something, you know, the bus is switching. It's doing whatever. I don't know what point we're probing. Check that out, right? There you go. Because that looks very sinusoidal, we're talking about that's our sine x on x interpolation there.

**Dave Jones:** So this is like, once you see that, you know, okay, we're beyond the bandwidth of our scope here. These signals are just too fast. But anyway, let's just go back to here. Okay, so we'll just try and capture that sort of like the most frequent one there.

**Dave Jones:** There it is. Got it. Okay, so I'll store that. Right, so what I'm going to do now is I'm going to actually change the ground into this. Instead of having this longer lead, I'm going to go for one of the shorter little adapter, ground adapter pins we've got

**Dave Jones:** in there. And it looks like there's a little bypass cap. I've determined that this right-hand side is the ground. So that's very convenient because that's right next to the point that I want to test. Otherwise, as I showed before, you might have to install one of those copper

**Dave Jones:** pads or something. You might have to scrape away some of the ground here or something like that, and maybe put the copper tape over the top of the chip or something like that. Or you'd have to scrape away some other ground point somewhere

**Dave Jones:** or, you know, soldering a little contact loop pin or something like that. So here it is. I've got my little adapter. Careful, because you can stab yourself with these little bastards. There we go. So we have this little now ground pin, which can sort of like, you know,

**Dave Jones:** pivot around like that. And anyway, that will make better contact. And this will be a higher frequency probe because it's a shorter inductive path. So let's try that. Will require the tongue at the right angle, and probably some magnification here. Okay, I've got my ground point, and I've got my

**Dave Jones:** probe point. Pan up, pan up. Okay, let's have a look. I've changed my digitizer. Definitely getting 5 gig samples per second. And I saved my reference waveform. So let's single-shot capture that. See if we can get it. No. There we go. Got it.

**Dave Jones:** Now I can actually adjust that waveform there to show you. There you go. So the orange one I've got there is the reference waveform, and this new yellow one is the one that we just probed. And there you go. It is like, it's of course like

**Dave Jones:** the same wave shape. You can see it's got the longer ground wave one. The orange one has some extra undershoot there. And comes back and takes more time to come back up like that. And the one up here got some extra wiggle wiggle wiggle yeah on the top there.

**Dave Jones:** Some overshoot. And so, you know, there are differences in probing right there. But at the moment, this is the loading of the line with a 1 picofarad, 1 puff active probe which costs a couple of thousand dollars. Okay, now I'm going to use my

**Dave Jones:** 500 megahertz passive probe here. It's the N2843. It's 11 picofarads, okay? And yes, I've compensated this. You compensate it with your probe compensation on the front. So everything's hunky-dory. I'm using my low inductance, high frequency ground probe attachment. So that's equivalent to what we had before.

**Dave Jones:** So we should get, because we've only got a 500 bandwidth scope here, then the bandwidth of the probe isn't really going to matter that much. Hold my tongue at the right angle, and probe this. I think I got it. But here's the interesting thing.

**Dave Jones:** I've changed the reference waveform to my low inductance short ground one before, so the orange one is the best we could get with our active probe. So the exact same ground point, basically the same ground length, and you can see that, well, you know, our wave shape's the same, but

**Dave Jones:** look. Look at this. It's a much higher level down here, okay? This is 200 millivolts per division, so it's like you know, 50-odd millivolts higher there, and it's actually lower down here, our yellow waveform there. So, you know, although we can see, like, the wave shape and everything up here, it's like

**Dave Jones:** when the bus is loaded differently, because that's what this little, you know, ramp up here is going here. I don't know the architecture of the Raspberry Pi. It doesn't matter. But I know there's something happening with there. And down here, we're actually seeing a larger drop

**Dave Jones:** across the bus here, which is interesting, isn't it? You know, there's significant differences here. This wasn't the exact example I wanted to show. I just, like, it's a random example, but you can see the difference here between a 500 meg passive probe and effectively, because of the bandwidth of the oscilloscope,

**Dave Jones:** a 500 meg active probe. They load down the circuit differently. And I know you want to see it. Okay, let's compare Dave's dodgy homemade resistive probe here with a 1K resistor in the tip. We'll give that a burl. Got a 50 ohm terminate that, but scope can do that, no worries.

**Dave Jones:** Tongue at the right angle, tongue at the right angle! Fix that! Oh! Oh, check this out! This is absolutely fan-freaking-tastic! Now, what we've got here, the orange waveform, of course, is our reference active FET waveform. That's a $2,500 active FET probe. Yes, it is compensated, because you do still have to compensate them, and it

**Dave Jones:** stores it internally, because it knows the serial number of the probe, etc. And the yellow one is Dave's do-it-yourself, couple-a-buck resistive probe! Look at this! What's going on here? Well, it's obvious that what's happening at this point right here is that the bus is actually

**Dave Jones:** going open, or something. I don't know the exact architecture of what's the pin I'm actually probing, but it doesn't matter, right? It's going open, and because the probe is 1 meg DC resistance, look at that! Basically, it's not going to discharge. Maybe if we got a longer time period, it'd eventually do

**Dave Jones:** a similar, eventually discharge, or whatever. But you see that the bus has actively changed. But because we're now loading this bus down with a 1k resistor, or a 1.05k resistor, because we've got the 50 ohm terminator as well, it, boom! This is an R, this looks like

**Dave Jones:** for all the world, and it is an RC discharge curve. So there you go. What's that, you know, 10 nanoseconds per division? I don't know. You can work that out, whatever, for those playing along at home. But you can see how the resistive probe actually completely changes

**Dave Jones:** the circuit that you're actually measuring. So, sure, the signal integrity is excellent. Let's take a look at this, actually. If you have a look at the bottom here, you can see that both of them undershoot almost exactly the same. But you remember how I

**Dave Jones:** said that the resistive probe can actually be more tolerant of longer ground leads. I think they're both about the same length. I think they're practically near identical. Remember how I said it can be more tolerant on these than active FET probes. This might be an example

**Dave Jones:** of this, because this is not some controlled experiment. This is just something I slapped together willy-nilly, and this is the result that we actually got. This is fascinating, right? They both undershoot exactly the same, but the active FET probe, the orange one, actually, look, it

**Dave Jones:** overshoots again, and it takes much longer to recover than the resistive probe. Look at that! So, this could be an example of where this cheap-ass, do-it-yourself resistive probe is actually outperforming this $2,500 active FET probe in terms of signal integrity. But, once again, this is not a completely controlled

**Dave Jones:** experiment. But this is what you can actually get. But, of course, the limitation is that it loads it down much more. 1K as opposed to 1 Meg, right? There's a huge difference there. And you might know, what's the difference between this load? You know, look, it's dropping

**Dave Jones:** with the 1K. Is that the effect of the 1K load over here? If we actually measure that, because remember, it's a divide-by-21 probe as opposed to the active FET probe, which is divide-by-10. So, if we actually set up our cursors here, and I've set them precisely

**Dave Jones:** to the same ground point here, our resistive probe is, we're getting 55 millivolts there. So, if you get your confuser out, 55 millivolts times 21, which is our probe, 1.155 volts. And this is a, looks like it's a 1.2 volt bus. So, it's, like, it could, like, it's maybe 50 millivolts under, but we have to measure

**Dave Jones:** the other one, actually. So, for just that, we're talking about 60 millivolts there. So, it's actually precisely 6 divisions there. And we were on 200 millivolts per division, so that's precisely 1.2 volts. So, the resistive probe is actually measuring 50 millivolts less, and that could be

**Dave Jones:** the load, the extra loading of the 1K load. Once you, you'd have to check out the driving strength of the driver actually used in this, which is the, whatever arm micro is used on the Raspberry Pi or whatever. We can see that it's basically 50 millivolts

**Dave Jones:** under. So, that could be, like, an extra 50 millivolts drop caused by the loading of the probe. That sort of seems to be the case. But, once again, this isn't exactly a, you know, really proper setup controlled experiment. And, by the way, no,

**Dave Jones:** this is not just a, like, a freak capture where you know, the bus did something different than before. This happens every single time, no matter how many times I capture this. The 1K probe is definitely, totally different to the active FET probe here.

**Dave Jones:** And you can see, obviously, the bus was floating there, and then it went, boom! No, I'm going to go actively low.
