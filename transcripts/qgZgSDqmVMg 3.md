---
video_id: qgZgSDqmVMg
title: EEVblog 1557 - Micsig SigOFIT Optical Fibre Probe + GaN Experiment
url: https://www.youtube.com/watch?v=qgZgSDqmVMg
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 25, "3": 39, "4": 54, "5": 62, "6": 81, "7": 89, "8": 108, "9": 126, "10": 140, "11": 157, "12": 170, "13": 186, "14": 194, "15": 205, "16": 220, "17": 233, "18": 243, "19": 267, "20": 278, "21": 288, "22": 303, "23": 315, "24": 340, "25": 355, "26": 370, "27": 384, "28": 396, "29": 412, "30": 427, "31": 435, "32": 449, "33": 462, "34": 473, "35": 488, "36": 499, "37": 512, "38": 529, "39": 536, "40": 547, "41": 558, "42": 572, "43": 591, "44": 603, "45": 616, "46": 631, "47": 657, "48": 681, "49": 696, "50": 717, "51": 729, "52": 749, "53": 764, "54": 779, "55": 793, "56": 808, "57": 823, "58": 840, "59": 855, "60": 878, "61": 888, "62": 899, "63": 909, "64": 919, "65": 944, "66": 968, "67": 989, "68": 1014, "69": 1036, "70": 1059, "71": 1074, "72": 1087, "73": 1097, "74": 1115, "75": 1126, "76": 1135, "77": 1146, "78": 1167, "79": 1188, "80": 1207, "81": 1219, "82": 1230, "83": 1245, "84": 1260, "85": 1271, "86": 1287, "87": 1302, "88": 1315, "89": 1327, "90": 1337, "91": 1349, "92": 1361, "93": 1384, "94": 1393, "95": 1407, "96": 1417, "97": 1426, "98": 1436, "99": 1449, "100": 1460, "101": 1475, "102": 1488, "103": 1501, "104": 1513, "105": 1536, "106": 1545, "107": 1556, "108": 1570, "109": 1580, "110": 1598, "111": 1614, "112": 1629, "113": 1640, "114": 1657, "115": 1671, "116": 1682, "117": 1694, "118": 1707, "119": 1717, "120": 1734, "121": 1746, "122": 1756, "123": 1771, "124": 1785, "125": 1795, "126": 1806, "127": 1817, "128": 1829, "129": 1849, "130": 1871, "131": 1881, "132": 1896, "133": 1903, "134": 1919, "135": 1929, "136": 1941, "137": 1955, "138": 1968, "139": 1980, "140": 1989, "141": 1999, "142": 2012, "143": 2022, "144": 2031, "145": 2044, "146": 2053, "147": 2065, "148": 2078, "149": 2087, "150": 2099, "151": 2107, "152": 2115, "153": 2125, "154": 2141, "155": 2154, "156": 2164, "157": 2177, "158": 2191, "159": 2203, "160": 2216, "161": 2228, "162": 2249, "163": 2263, "164": 2272, "165": 2280}
---

**Dave Jones:** Hi, I've got a real interesting video for you today. You know, I've done a lot of videos on oscilloscope probes, passive, active, high voltage, differential probes. I've got a video on how they work and reverse engineerings and teardowns and stuff like that.

**Dave Jones:** But one that I haven't done a video on is one of these new optical fiber probes. And thank you very much Mixig for sending this in, even though I think the label's upside down.

**Dave Jones:** Anyway, check out this. It is their latest optical fiber probe. And this is the fourth and most advanced type of oscilloscope probe and also the most expensive type of oscilloscope probe you can get.

**Dave Jones:** Now, the first type of probe is your regular passive probe, you you know, one to one, 10 to one switchable or times 10 fixed passive probe. They're your general purpose probes, typically up to, you know, 500 megahertz, something like that.

**Dave Jones:** Although there are some very special ones that might be able to scrape it up to one gig, but basically, yeah, not. Um, and the next step up is your active FET probes.

**Dave Jones:** Basically, these are very high frequency probes, very low input capacitance, and they've got an active FET amplifier on the input here. And you can't These are only used for very low voltages and basically single ended or differential, but very high speed stuff.

**Dave Jones:** So, if you want to measure, like, you know, high speed buses with great signal fidelity, your active FET probes, they can go up to, you know, gigahertz, tens of gigahertz even.

**Dave Jones:** So, all your high frequency ones are your active FET probes. And then, your next type, of course, is your high voltage differential probe. And I have done several videos on these, like actually reverse engineering these, explaining how they work and testing them and doing a common mode voltage test and stuff like that.

**Dave Jones:** So, you want to use the high voltage differential probe when you basically want to measure high voltage stuff or things that are raised above signal ground so that like main switch mode power supply high side driving transistors in you know power supplies and stuff like that.

**Dave Jones:** You can't do that with your active probe or your regular passive probe cuz you'll blow up your oscilloscope. I've done a video on that, too. So, yeah, high voltage differential probes an essential bit of kit, but unfortunately these are not high bandwidth.

**Dave Jones:** This is one of the highest bandwidth ones on the market, you know, 70 MHz. You can get you know, 100, but as valuable and as great as a high voltage and essential as a high voltage differential probe is, you should have one if you're doing any sort of mains work or any sort of you know, higher voltage power supply type stuff.

**Dave Jones:** Unfortunately, their common mode rejection ratio can be a problem when you're talking about more modern switch mode power supply designs and really high voltage and and like high energy physics research and doing all sorts of advanced stuff.

**Dave Jones:** This is where you need one of these newfangled fiber optic probes. And thank you very much Mixig for sending this in. These these are state of the art tech and it basically contains the equivalent of a like a high frequency active FET probe.

**Dave Jones:** This particular model from Mixig can go up to 1 GHz, so quite high frequency. The one we've got here is only 200 meg, but they do make models that go up that high.

**Dave Jones:** So, basically is an active FET probe front end like this, but instead of just being connected via a coax and having a common mains earth, this cable here is fiber optic.

**Dave Jones:** There is no metallic conductors in here at all and it gets its power for the head over the fiber optic. So, it's powered from this fiber optic transmitter here and also receiver.

**Dave Jones:** And this plugs into your oscilloscope and it can actually send power over the fiber optic to power the active FET front end like this, but it the then sends the signal back also via the fiber optic in the analog form.

**Dave Jones:** They don't sample, it's all done in the analog domain. So, they transfer power in this direction and they can get signal back in this direction and you get complete galvanic isolation.

**Dave Jones:** In this case, up to 60 kilovolts isolation because you've got no metallic conductors between your oscilloscope and your probe. It's It's almost like magic. So, you get the advantages of the high bandwidth FET with the advantages of the high common mode rejection ratio of your high voltage differential probe.

**Dave Jones:** It's the best of both worlds. But, these are unfortunately incredibly expensive, but these are essential bit of kit as I'll show you in today's video. We're going to do some experiments and it's going to be amazing.

**Dave Jones:** So, there's a couple of other companies that manufacture these optical fiber probes. Please correct me if I'm wrong, but I think the Tech IsoView might have been the first one, the first famous one.

**Dave Jones:** Anyway, but Mixig have now come out with this SigOff probe and it goes anywhere from 100 megahertz up to 1 gig model. So, we've got the 200 megahertz model here, which is more than good enough for the experiments that we want to do.

**Dave Jones:** Now, this is Mixig's comparison between the LeCroy DL Iso, the Tektronix IsoView and Mixig Off. So, always take these manufacturers comparisons with a grain of salt, but anyway, this is what they've got.

**Dave Jones:** It starts Yes, then pretty pricey at 23.99. That's Yankee bucks. But, the Tektronix IsoView for the 200 megahertz one starts at 10,800. So, the one we've got here is 3,700 US dollars as opposed to the 10,800 dollar Tektronix one and the LeCroy DSO is even higher, but that's a higher bandwidth minimum there.

**Dave Jones:** But, the amazing thing about these and the difference between your regular high voltage differential probes and these optical fiber probes is that these have a massive massive common mode voltage range.

**Dave Jones:** The 200 MHz version that we've got here, 106 dB common mode rejection ratio. I've done a video actually demonstrating this. I'll link it in. I won't go through, you know, the nuts and bolts of common mode rejection ratio here.

**Dave Jones:** But, that is absolutely enormous. And it will do that for the full 200 MHz bandwidth. And compare that to Mixig's high voltage differential probe, which is almost identical specs to my EV Blog HVP 70 probe.

**Dave Jones:** And they're great probes. They're great for high voltage use. You know, they've got decent common mode rejection ratio. But, you'll notice at at 1 MHz it's minus 50 dB.

**Dave Jones:** And you go up to 10 MHz it's minus 40 dB. And it just gets worse and worse and worse. So, if you've got a 1 MHz switching power supply, for example, and you're trying to measure the high side of that, as we'll do today in today's experiment, stay around for it cuz it's fantastic.

**Dave Jones:** This 100 dB makes a massive difference. Like game-changing difference. So, we're going to In today's video, we're going to compare this Mixig optical fiber probe to a you know, pretty much one of the best high voltage differential probes on the market.

**Dave Jones:** And watch this blow this out of the water for the specific use case that we're going to look at today. So, we'll have a very brief look at this.

**Dave Jones:** The main advantage of this one over the Te and the Lecroy ones is it's a universal BNC interface. It can plug into any scope 50 ohm output. So, 200 MHz, but they've got models going up to 1 gig.

**Dave Jones:** So, and it's got a built-in calibration mode, which only takes a couple of seconds. Whereas the other models, even though I haven't used them, Mixig claim that they can take up to minutes to to calibration cuz these things drift with temperature and stuff like that.

**Dave Jones:** So, you got to be careful to actually calibrate these things before you, you know, take your your critical measurements. Just so that you're, you know, taking out DC offsets and other stuff.

**Dave Jones:** So, yeah, they've got built-in signal generators in the probe. So, when you press the calibration button, it will actually run a like there's a test generator in here which will generate a signal and then it can test it and it can calibrate for any offsets.

**Dave Jones:** But, you can manually um adjust the offset. Here, it's got a built-in fan. Here, it looks like it sucks in the end from over here. Gets a little bit warm, but it it's a little bit whiny.

**Dave Jones:** It's not hugely loud, but it's notice- noticeable if you're in a quiet lab. But, anyway, yeah. So, this has a power optical fiber transmitter in it to generate to send the power over the optical fiber here.

**Dave Jones:** So, you can't like bend these really sharply. That's why breakable fiber cable warranty void if you bend that sucker. So, yeah, don't go bending your really expensive fiber optic probe cuz you can pay up to 20 grand like the 1 gig bandwidth version of this.

**Dave Jones:** Oh, these are such sexy bits of kit. Wait until you see the demo. And in the box, I've actually got two probes although I think it might only come with one.

**Dave Jones:** I've got a 10:1 probe here. It's an SMA interface. So, it's a flexible. So, that's a 10:1 probe and I've got a 500:1 as well for high voltage use.

**Dave Jones:** Cuz as I said, these are active fit inputs. So, just like your active probe, don't go putting high voltage into this cuz you'll just blow the magic smoke out of your potentially $20,000 probe.

**Dave Jones:** That'll ruin your day. But, with the high attenuation input, they can go up to several kilovolts. No worries. And we could get a nice little desk stand-off so that it isolates it from your bench and I'll demonstrate that later.

**Dave Jones:** Then, we get some MCX uh connectors are because this is an MCX connector interface. It's SMA here, but the actual probe tip itself is MCX. So, yeah, the demo board we're going to use today has an MMCX connector, and well, that causes a bit of problem, but anyway, we'll get around that.

**Dave Jones:** And because the probe is not an active probe interface, so it can go on to any scope, it does need the 5-V USB C here to power it, and it does come with a plug pack and cable to do that.

**Dave Jones:** Now, as I mentioned, this is not a high-voltage differential probe. It does not use a differential probe architecture. I'll link in the video that I've done actually reverse engineering Mixegg's DP1007 differential probe.

**Dave Jones:** I've also reverse engineered the Sapphire HVP 70 as well. So, it is not a differential architecture. It does not have the differential input, this FET input, that goes into a differential amplifier configuration.

**Dave Jones:** It is, as I said, just like a single-ended active high-frequency probe. It's very different to the high-voltage differential probe here. So, let's have a look with a practical example of where you can use an optical fiber probe like this and get the advantage, the huge, massive common-mode reject, almost practically infinite common-mode rejection, well, not infinite, you know, 100-plus dB common-mode rejection ratio of these fiber-optic probes.

**Dave Jones:** And we'll see if we can actually get some advantages like this compared to say a differential probe. Here's the yellow one there is what a differential probe is going to look like when we're going to probe the circuit that we're going to try out in a minute, and that's not the real response because it's got an extremely poor common-mode rejection ratio of a regular high-voltage differential probe.

**Dave Jones:** So, and look, we should be able to get a nice, beautiful response with a fiber-optic probe. Let's see if it's possible. Now, one of the many useful applications for this is in real high efficiency modern power electronics which get like 99 plus percent efficiency.

**Dave Jones:** You used to your regular DC to DC converters get in like you know 85 90% will be a good one maybe into the 92 93% range but the more modern ones especially in higher really higher power really dense brick designs can get over 99% efficient.

**Dave Jones:** The way they do this is using modern MOSFETs called gallium nitride semiconductors or GaNs as we'll refer to them here cuz it's it's like GaN GaN power transistors. Here's an Infineon application note.

**Dave Jones:** So we're going to actually look at one of their cool GaN gallium nitride power transistors here. And one of the advantages if you go look at the topology, we won't go in into detail but it's basically a there's no PN traditional PN junction in your GaN transistor.

**Dave Jones:** So it's basically a planar device which means it basically flows on the surface. It doesn't the current flows on the surface. It doesn't flow into the PN junctions and hence you can get lower conduction resistance of these things which make them more efficient at higher voltages as well.

**Dave Jones:** So they work very differently to a regular MOSFET but we won't go into the details. So here's another substrate diagram of how a GaN device works like this and basically you're going to get like really high efficiency.

**Dave Jones:** So I mean check check this out right? Here's a power factor correction board 2.5 kilowatts in this tiny little form factor like this but look at this. We're getting you know 99 percent plus efficiency on stuff like this.

**Dave Jones:** So you know this is how you can get really dense modern things and you get huge EV chargers and you can get you know a really efficient power bricks and stuff like that because they're using these newfangled gallium nitride and there's other types of modern power transistors as well.

**Dave Jones:** And they're called a high electron mobility transistor as well. So, a HEM T. So, if you hear the word HEM T again, HEM T, something like that, it's just basically, yeah, high electron mobility.

**Dave Jones:** It means more betterer. It means lower on on resistance. And lower on resistance in a switching converter, whatever it is, whether it's power factor correction, it's boost, it's buck, it's whatever you're doing, CPQ converters or whatever, then you're going to get much higher efficiency due to the lower effective on resistance.

**Dave Jones:** Yeah, I know this is marketing blurb for Infineon, but they're one of the leaders in these GaN devices, and they got this cool demo board. But, looking basically use them in the power factor correction circuit, the resonant converter here, and the synchronous rectifier on the output.

**Dave Jones:** So, not only can use them as transistors, you can use them as very effective diodes as well. So, anyway, we are going to be using one of these 600-V CoolGaN, um that's just their trademark thing, but gallium nitride power transistor in a push-pull half-bridge configuration, or a totem pole switching configuration.

**Dave Jones:** We're not going to like do a full converter, but basically, yeah, we're going to use one of these bad boys. It does have a Kelvin connection in here, by the way, for the source down here.

**Dave Jones:** So, anyway, we're going to use one of these application boards, which you can get really cool. Um they only cost about 60 bucks or something like that. If you want to play around with these things.

**Dave Jones:** Two It's got two of these GaN transistors. So, we've got this half-bridge configuration like this. So, we've got one on the top and one on the bottom. So, this is a basically a totem pole output.

**Dave Jones:** And here's the drive circuit for it. And don't worry, it looks a bit complicated. I won't go into all the details, but how you can achieve like 99% plus efficiency with these things is by a carefully driving.

**Dave Jones:** And this is what we want to monitor because so this can go up to 600 volts but today we're due to the equipment limitations are only going to go up to 300 volts and it's basically impossible with a regular probe let alone a regular differential probe to actually measure the gate drive of a high side power transistor like this doesn't matter whether it's gallium nitride or anything else it's just that

**Dave Jones:** gallium nitride is a a modern application for a biggest what you need to measure of course is the gate source voltage like this on a power transistor and that's why we've got this connector here to actually do this but the problem is you can't do that when this source here is switching like hundreds of volts up to like 600 volts or even higher you just can't do that the common mode

**Dave Jones:** is just you get that common mode if you're switching at megahertz for example which high efficiency converters are you've got this huge common mode signal actually bouncing up and down hundreds of volts and your regular high voltage differential probes even the best of the best ones can't handle that sort of thing and hopefully we'll get a demo of that today here's the complete schematic for the demo board that we're

**Dave Jones:** going to use we've got a half bridge gan over here and then we've got these two driver chips have a look at the schematic in a minute but these are actually isolated so there's electrical isolation inside the chips here okay and they're powered from VDD and VSS here and they're powered from this isolated boost converter over here so we've got like 5 volts into the board here and

**Dave Jones:** then it's powers the drive side of the MOSFETs then into a half bridge here we're going to feed in there and here we're going to feed in up to 300 volts and we can vary that to see the effect of the common mode rejection ratio and just to ensure that you don't get what's called shoot through which is both of these transistors turned on at the same time

**Dave Jones:** cuz you don't want to short out your like 300 or 600 V power supply that's capable of like kilowatts or something like you're like, "No, it's going to release the magic smoke." So, what this does is this basically we've got an adjustable there's a little trim pot here and here which you can adjust the off time of the transistor.

**Dave Jones:** So, this basically we've got a 50 ohm input here which you can drive from a signal generator and that will just invert the signal and then add some delay here to ensure that these transistors it's impossible to have both of these transistors on at the same time.

**Dave Jones:** So, you can just adjust the dead time of the gate drive. And then we've got a 500 K load with the capacitors we may not use that today. I'm not actually going to use a load so it's not going to be like an inductive load or it's not going to be a boost configuration.

**Dave Jones:** We're just going to switch these transistors off and on at a fast rate like 1 MHz and we should be able to see the effect of being able to probe cuz this is what we want to probe today.

**Dave Jones:** We want to be able to probe this gate drive because when you're developing these circuits if you can't measure the gate drive is like critical. I won't go into all the details of driving gallium nitride GaN transistors but I'll include some application notes down below if you really want to know about that sort of stuff but it's real tricky.

**Dave Jones:** If you're you know shooting for 99% efficiency you need to get your gate drive right and you need to be able to probe it and you can't do that with even the best high voltage differential probe.

**Dave Jones:** So, we'll try that. You can do the low side down here cuz this is basically ground, right? And there we go it goes through the Kelvin connection there, right?

**Dave Jones:** So, you can measure that gate drive but this high side when this node here if this source is switching by you know hundreds and hundreds of volts at 1 MHz it's going to ruin your day.

**Dave Jones:** So, here's these specific GaN drivers and you can see here there's actually isolation inside the chip here. So, uh yeah, basically you're feeding your PWM signal here, but it basically it's got to go over this electrical galvanically isolated interface, and then you've got another totem pole driver in here to actually drive your transistor here.

**Dave Jones:** And you need one of these driver tip chips per transistor. And the output here not only drives the gate, but it also drives the source as well. And this is why you use these GaN devices in uh really high-efficiency converters, cuz you can really drive them in very specific ways targeted specifically for your application.

**Dave Jones:** So, you've got to provide that isolated supply here for actually driving the GaN transistor. Okay, I'll go through the setup here. We've got our demo board here, and it's raised up with the PanaVise here, and we've also got our optical fiber probe on its little stand.

**Dave Jones:** There's a reason it comes with a stand, because if you've got your board laying on your bench, even though this is a non-conductive bench, and you've got your probe down on the bench as well, you can get increased capacitive coupling.

**Dave Jones:** And it's actually working at the moment, and have a look at the switching waveform here. And watch what happens if I change it down towards the bottom like that.

**Dave Jones:** You'll notice there's much more ringing here, right? So, you've got to keep this up off the ground like that. That's why they supply the stand. And to befit our state-of-the-art optical fiber probe, we've got the no less state-of-the-art Rohde & Schwarz MSO 4 scope here.

**Dave Jones:** So, I'll be operating that remotely. I've got a 5-V power supply here, and that just powers the 5-V in for the board. Let me turn that voltage down. Otherwise, I should be using my takeaway protection container here.

**Dave Jones:** Highly recommended, made in Australia. Thank you very much. We've got the optical fiber probe connected into uh channel one here and I've run a calibration on that. We can just run that again.

**Dave Jones:** Bungo. Um and it's all temperature stabilized and everything. Next on uh channel two here, I've got my uh high voltage uh probe. Probably could get away with a a regular uh times 10 passive uh probe, but just to be on the safe side, I'll use my 100:1 uh probe here.

**Dave Jones:** So, that's on channel two and that's across the uh H-bridge um output and uh the low side. So, effectively uh the ground here. And I've got a 220 K resistor loading here just going between the H-bridge output and uh ground down here.

**Dave Jones:** Um I'm not going to do any fancy uh load today. I'm just going to put something on it just so we have something there. And we can of course uh mains earth common that uh low side because um everything else is uh floating.

**Dave Jones:** So, no problems whatsoever there. We're not going to blow up our scope. Done a video on that. And then either side of here, I've got my uh 300 V high voltage input which we can adjust, which is coming from this Xantrex power supply.

**Dave Jones:** And this is the uh fan noise you can hear here. Um so, yeah, I can just adjust the voltage. I can go up to uh 300 and it it's a 300 V 4 A supply.

**Dave Jones:** I can go up to 311, no worries. And on channel three here, EE blog HVP uh 70 high voltage differential probe coming back in stock uh in September. They've had a uh part shortage.

**Dave Jones:** Anyway, um it's it's an awesome it's probably one of the best in uh high voltage differential uh probes on the market designed and manufactured by uh Sapphire. And we're going to use that to actually probe the exact same point, not at the same time.

**Dave Jones:** Don't do it at the same time, but uh the same point as our optical fiber probe here. Just so that we can show, hopefully, a difference between uh the common mode rejection of an optical fiber probe and pretty much uh the best differential uh high voltage differential probe on the market and how this, as good as it is, is not the tool to use to measure the

**Dave Jones:** high side with a 300 V switching at 1 MHz, which is what we're going to have here. All right, let's control our Rohde & Schwarz scope remotely. I love this via the Ethernet.

**Dave Jones:** The software interface web interface is just fantastic. This is just working as a in a web browser here. So, we can get the full screen or we can turn on the front panel here, whichever we prefer.

**Dave Jones:** Let's go for the front panel. Now, what we've got here is the green waveform here. As you can see, 40 V per division here, so we can go up to 320 V.

**Dave Jones:** This is our H bridge output, okay? So, where I've limited the probe here, so we can go in there and well, we can look look at this. It even shows the transparency.

**Dave Jones:** Look at that. We can adjust the transparency. So, with both of these channels, I've actually bandwidth limited these to the probe bandwidth because well, there's no point going higher than that.

**Dave Jones:** You're just going to get increased noise. So, So, our green waveform here, I've I just turned it on. Enough. It works with no We still get the switching waveform here, the yellow one, with no voltage at all.

**Dave Jones:** I can completely switch off my high voltage supply. We still get the switching waveform. We're still driving the MOSFET, but of course, there's nothing there to switch, okay? So, our output here, so we're currently set at very low.

**Dave Jones:** So, I've set it to 40 V. So, it's just switching off and on. Now, we're generating a signal here. We're generating a 1 MHz uh 5 V P to P, 2.5 V offset, so just a TTL signal in with a 50% duty cycle, and we can play with that later.

**Dave Jones:** So, the channel one here, we let's switch over and we can see the scale here. You can see that it's not much. It's like, you know, 6 7 V peak to peak, something like that.

**Dave Jones:** That's what you'd expect when you're driving the MOSFET, but remember, this is the differential voltage against the gate and the source of that high side power transistor, the one which is currently elevated at Well, it's jumping between 0 and 40 V, okay?

**Dave Jones:** So, it's continually switching at 1 MHz. You can see the schematic up above, the waveform at is at at the source of that high side power transistor. So, we're measuring the gate source voltage.

**Dave Jones:** So, that source is continually swinging, and that is our problem. The greater the voltage, the more your common mode rejection ratio needs to be the higher your common mode rejection ratio of your probe needs to be in order to eliminate any effects of that switching output from that high side gate source measurement here.

**Dave Jones:** So, anyway, this is the classic gate driver waveform. This is exactly what we'd expect. The on period is from here over to here. Yeah, you can see my cursor.

**Dave Jones:** Oh, over to here. And that ringing that we get in here, you'll see this change a bit, but it's not It's not a huge amount, but uh that will be due to that little extra length of coax that we had in there.

**Dave Jones:** If I had the proper little RF adapter in there, then that would likely almost certainly go away, and we get a nicer waveform. But anyway, when the output switches here, we get a little bit of ringing on the output.

**Dave Jones:** That's because of the that longer lead that we used on that high voltage probe. Once again, if I probe that a bit better, we'd tighten up the measurement on there.

**Dave Jones:** But yeah, for the purposes today's experiment, that doesn't matter. All right. So, what I'm going to do now is I'm going to adjust that power supply from 40 V all the way up to 300 and just over 300 V, and we're going to see if that yellow waveform, the gate source voltage, actually changes.

**Dave Jones:** If changing that source voltage and switching between a much higher amplitude actually changes the measurement on that yellow gate source high side power transistor. So, let's adjust it. We're at 40 volts at the moment, and here we go.

**Dave Jones:** Right, we're going to go up, and look, it's basically that yellow waveform is not changing at all. At all. There's a little bit of, you know, switching um stuff, which is changing a little bit, but basically we still get the waveform.

**Dave Jones:** Look, we're all the way up to 311 volts, and it basically that yellow waveform hasn't changed at all. We're still getting proper signal measurement uh fidelity on that waveform.

**Dave Jones:** And that source voltage is switching up and down at a frequency of 1 MHz from 0 to 400 volts, and that optically isolated probe is doing the job, and we're not the basically look it's it look there's no difference at all.

**Dave Jones:** I can't like overestimate how difficult this measurement would be without this optical fiber probe. In fact, let's try it. Let's hook up one of the best high voltage differential probes, and see the difference.

**Dave Jones:** Oh, no. I hit the stupid preset button and screwed all my settings. Damn it. What I've done now is created a reference waveform that channel one switching waveform that we had with the optical fiber probe.

**Dave Jones:** I've saved that as a reference waveform, so that's the white one. So, we'll be able to compare it to the high voltage differential probe, and that's a very good use of those reference waveforms for your scope.

**Dave Jones:** If you've never used them before, this is what they're good for. You'll notice now that we're actually getting so much ringing and crap on that different from that differential probe that like we can't trigger off this.

**Dave Jones:** So, I'm going to have to choose a different source. I'm going to have to choose the going to have to choose the actual output waveform down here. Now, we can see it.

**Dave Jones:** Look at that orange waveform. Okay, we can increase the brightness here. We increase the intensity. Look at this, the orange waveform. Okay, it's the same. It's the same This is the best high One of the One of the best high voltage differential probes on the market, and it just does not like that.

**Dave Jones:** And we're only switching like What is it? 40 V? Less than like 30-odd volts or something like that. Let's Let's actually turn it up and see what happens. So, let's wind it up.

**Dave Jones:** Watch that orange wave form, okay? Look. Look at how bad that's getting. Look at all the ringing. Look at this. Look at this. Why? It is absolutely atrocious. It is awful, okay?

**Dave Jones:** And yeah, the probing's not absolutely ideal, but you're going to get this. You can see that how much of a major problem that is. But let's actually go down, okay?

**Dave Jones:** And we'll go down in frequency. And if we go down to 1 kHz switching frequency, you'll see not really a problem, right? You don't like we can Once again, we can go up to ALL THE WAY UP to 300 V, and you don't notice any change in that wave form whatsoever.

**Dave Jones:** So, the high voltage differential probe is fine at 1 kHz, but as it goes up in frequency, your common mode rejection ratio drops, and then you get all those problems.

**Dave Jones:** And the whole idea of these using GaNs and to get the high efficiency, you got to use the high frequency. So, you can't use the high voltage differential probe to measure it.

**Dave Jones:** You've got to use an optical fiber probe. Cool, huh? So, back at 1 MHz again, you can see that as we like as the voltage gets higher at 1 MHz, okay?

**Dave Jones:** You can't get any proper signal fidelity. Look at it compared to the white reference wave form there that we're getting with the fiber optic probe. This shows that this is the only fiber optic probe for this application that the only game in town.

**Dave Jones:** Sure, you could use some other isolated scope probe to do it, but then you can't The whole idea of doing stuff like this is that you use the one scope to get time reference start measurements on them like multi channels so you can measure the different stuff that's going on and you can't use a high voltage differential probe.

**Dave Jones:** Optic for fiber probe is the only way to do it for this application and for many other like you know high end like physics experiment applications and stuff like that and power and all these power measurement applications that have high frequency high voltage switching stuff like this got to use an optically isolated probe.

**Dave Jones:** That's what your 100 dB of common mode rejection ratio does. It's just it's not a problem. And we can play around with the SigGen here. So let's adjust this duty cycle.

**Dave Jones:** Look, you know like you've got no chance of measuring this with a differential probe. There's just too much ringing let alone at at at higher voltages. All this stuff is just is just going to absolutely dominate.

**Dave Jones:** But if we go back to our fiber optic probe here and we adjust the our duty cycle, right? Look look at how we can still see the fig signal fidelity.

**Dave Jones:** Look, right? You can just see everything, right? Even at like a 1 MHz switching frequency. It's just like it's amazing. And I switched off the external high voltage supply completely.

**Dave Jones:** You can see that on the green waveform there and this is the baseline. I've actually got both the fiber optic probe and the differential probe actually plugged in at the same time.

**Dave Jones:** Don't recommend uh that at you know for a real measurement but you can actually see the baseline ringing there of the differential probe in the orange there. So it you know it it's not too bad.

**Dave Jones:** We can do better if we actually probed it better. But as you saw before once we turned on that high voltage and then it started switching that common mode signal started to swing on the output which caused the gate and source to just keep rising up and down up and down.

**Dave Jones:** Then that's where you call my mode rejection ratio, a poor common mode rejection ratio. And remember, this 1 MHz switching frequency, you don't look at the 1 MHz common mode rejection mode figure, you actually have to look at the higher harmonic frequencies.

**Dave Jones:** That 1 MHz is going to extend to tens of MHz, even hundreds of MHz. So, the probe bandwidth matters. And my high voltage differential probe is only 70 meg bandwidth, by the way.

**Dave Jones:** And these isolated probes, because they're not actually a differential op amp architecture, can actually be faster. They're like an active probe. They can go to a gigahertz, or you know, even higher.

**Dave Jones:** So, yeah, look, it's like that's the baseline. You saw how horrible it just went, purely by having that output switch the gate and source. It's just a huge difference, huge.

**Dave Jones:** So, we'll quickly measure the noise here, and I've set up my scope here. You can see it in the top as 15-bit. So, I've got the HD mode enabled here, 200 MHz bandwidth limit.

**Dave Jones:** So, we're getting 15 effective bits, even though this only is only a 12-bit converter. This is a really schmick scope for doing these sorts of measurements. So, let's have a squeeze here.

**Dave Jones:** And I just want to show you one very nice feature. If I turn the scale down to 1 mV per division, I've turned off the times 10 thing, cuz we don't have the times 10 probe attached.

**Dave Jones:** You notice that these little red markers down here. See them? In the bottom left corner there, next to the vertical scale, they indicate that we're actually over ranging, even though it doesn't look like we're over ranging here.

**Dave Jones:** And I can actually turn up the intensity like this, and you can see it still doesn't look like we're over ranging, but it detects any peak above or below the ADC sample range.

**Dave Jones:** And as long as you get one peak there, it'll like set the red thing there flicker at a rate that you can visually see. It's just to tell you that you're off scale.

**Dave Jones:** So, I can actually go in there and adjust it to 2 mV per division, and we're gone now. So, I just I just wanted to point that out. I did a separate video on this on the second channel a little short and I just really appreciate nice touches like that.

**Dave Jones:** Beautiful. Whoever implemented that. And I just wanted to go 0 to 5 MHz bandwidth here cuz I wanted to show you just these little switching spikes in here at 315 kHz.

**Dave Jones:** So obviously inside this thing there's a switching converter and we're just getting the switching noise out of that. And you can see the harmonics are there. Can I physically drag that level down?

**Dave Jones:** Yes, I can. So we get the extra peaks there. Oh, isn't that nice? Um there are. So we can get the harmonics of that switching frequency. Not a big deal.

**Dave Jones:** I just it's there and I wanted to show you. And the actual noise here we've got our AC noise here. I've done a whole video on that and how you've got to choose that correctly.

**Dave Jones:** So it eliminates the DC offset here and we're getting 782 microvolts over the full 200 MHz bandwidth. And I've now got a 200 Oh, I've now got a 333 MHz span.

**Dave Jones:** You can see at about 200 MHz it starts to fall off because well, this thing only has a 200 MHz bandwidth. So you expect the bandwidth to start falling off there, but that looks pretty good, you know, at around about like 80 minus 80 dBm noise floor or something like that.

**Dave Jones:** So yeah, it's not too shabby at all. But the reason you want this, of course, common mode rejection ratio. Over 100 dB which I'm not even sure I can measure 100 dB common mode rejection ratio here in the lab.

**Dave Jones:** But anyway, it's it's it's huge. You've already seen the benefits. And I see very little drift in this thing either. It's pretty good. So I'll switch on the cal mode now and you'll see it.

**Dave Jones:** Cal mode now. Boom. There we go. That was it. It's quick and then the offset button you can just move it, you know, if you've got a DC offset in there you can trim it like it's looks like it's about like .2 mV per step or something.

**Dave Jones:** It's really quite small. So I'm adjusting that now and you can see that the steps are really quite tiny. So yeah, it's really nice. So there you go. I hope that's given you some insight into what these really advanced expensive probes can do.

**Dave Jones:** Yeah, they're not cheap, but they're the only game in town if you want to actually develop these leading edge high efficiency high voltage high frequency high performance switching products.

**Dave Jones:** And as I said, do like other physics research. And there's all sorts of like physics experiments that you can do. High voltage you know, isolated differential uh stuff. And you need these fiber optic probes.

**Dave Jones:** You need that massive common mode rejection ratio CMRR like 100 dB up to like what is it? 50 60 kilovolts or something like that for you know, physics research.

**Dave Jones:** You wouldn't be using those sorts of voltages for you know, regular electronics stuff. So, really exotic research. But stuff like just designing a high efficiency power brick or you know, the new fangled EV chargers that need massive high voltages high currents and you know, a high frequency switching super efficient converters.

**Dave Jones:** This is the only game in town. So, thank you very much to Mixig for sending this in. This is absolutely brilliant. And hopefully I've given you a good insight into how this measurement is simply not possible with the existing probing stuff.

**Dave Jones:** It It really is the only game in town. It's remarkable. Anyway, as I'll link in like all sorts of application notes and data sheets and all sorts of things down below.

**Dave Jones:** As always, you can just discuss test gear like this over on the EV blog forum. Absolute best place to do it. And if you like the video, please give it a big thumbs up.

**Dave Jones:** And you can discuss down below as usual. Catch you next time.
