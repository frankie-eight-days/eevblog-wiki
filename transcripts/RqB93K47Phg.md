---
video_id: RqB93K47Phg
title: EEVblog #714 - Metal Detector Reverse Engineering
url: https://www.youtube.com/watch?v=RqB93K47Phg
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 21, "3": 40, "4": 52, "5": 67, "6": 73, "7": 86, "8": 94, "9": 111, "10": 125, "11": 136, "12": 147, "13": 159, "14": 177, "15": 196, "16": 207, "17": 221, "18": 234, "19": 253, "20": 270, "21": 284, "22": 292, "23": 303, "24": 315, "25": 325, "26": 336, "27": 346, "28": 355, "29": 369, "30": 379, "31": 389, "32": 401, "33": 414, "34": 427, "35": 437, "36": 449, "37": 464, "38": 473, "39": 491, "40": 502, "41": 520, "42": 533, "43": 554, "44": 575, "45": 587, "46": 594, "47": 606, "48": 624, "49": 637, "50": 647, "51": 658, "52": 669, "53": 681, "54": 697, "55": 711, "56": 727, "57": 742, "58": 755, "59": 779, "60": 793, "61": 807, "62": 833, "63": 845, "64": 861, "65": 870, "66": 883, "67": 900, "68": 911, "69": 929, "70": 940, "71": 951, "72": 966, "73": 983, "74": 993, "75": 1009, "76": 1018, "77": 1031, "78": 1048, "79": 1060, "80": 1064, "81": 1079, "82": 1091, "83": 1108, "84": 1118, "85": 1132, "86": 1142, "87": 1153, "88": 1169, "89": 1183, "90": 1199, "91": 1214, "92": 1224, "93": 1237, "94": 1254, "95": 1274, "96": 1292, "97": 1301, "98": 1308, "99": 1318, "100": 1330}
---

**Dave Jones:** Hi, this is a bit of a catch-up video. It's an old mailbag item from a forum user called X Runner. So, thank you very much, X Runner. I know it's been a long, long time.

**Dave Jones:** It's probably been like a year and a half or something since he sent this in for to the mailbag for a teardown. What is it? One of these handheld metal detectors.

**Dave Jones:** One of these cheap-ass Harbor Freight things. It's like $17 on Harbor Freight. It's the Cen-Tech model 97245. And well, yeah, all $17 worth. And X Runner wanted to see if we can take it apart and explain how it works.

**Dave Jones:** So, I thought that would make a reasonably interesting video. We'll hopefully reverse engineer this and have a quick look at how one of these crusty metal detectors works. Let's go.

**Dave Jones:** And there's really nothing to it. Just runs off a 9-V battery here. By the way, I love this. Look, wear ANSI approved safety goggles when replacing the 9-V battery.

**Dave Jones:** You've got to be kidding me. Keep out of reach of children. Well, I shouldn't be allowed to use it then. Read the manual before use and keep it dry.

**Dave Jones:** Even though this is supposed to be like a waterproof wand on the end of it. I don't Yeah. Anyway, you get Well, you get $17 retail worth, really. Anyway, you just turn it on like that.

**Dave Jones:** And then it's got a sensitivity adjustment, of course, so you have no presence of no metal if you want it as sensitive as you can. Just turn it off like that.

**Dave Jones:** And then we can whack it over some things. So, you know, it gets within sort of like an inch or so of that screwdriver. And the pliers over here, this little It's got to get really, really close to that little nut there.

**Dave Jones:** And this tiny little screw, it's practically got to be touching. So, it's going to depend on the size of the metal object. And if we go for my stainless steel drink bottle, yeah, it's a good 2 or 3 in out from that, no worries.

**Dave Jones:** So, because that's a massive lump of metal there. And of course, this thing's pretty much going to detect any type of metal. It's not going to be a real discriminatory type.

**Dave Jones:** I I.e. it's not going to be able to detect the difference between gold and aluminum or something like that perhaps. But the whole idea is that yeah, it can detect ferrous and non-ferrous materials.

**Dave Jones:** Ferrous ones for example, you've got iron and the stainless steel that we've got here for example. And the non-ferrous stuff, you're going to have like copper and tin and gold and lead and all that sort of jazz.

**Dave Jones:** And it'll probably do various alloys as well and brass and stuff like that. So, yeah, I don't expect this thing to be very discriminatory. And if we turn the sensitivity all the way down, it still gets within an inch or so.

**Dave Jones:** And woohoo! There we Oh. Yeah, look at that. It's not bad It's not bad range actually for a $17 job. All right, let's crack this thing open and uh see, I think we can just do those screws on top.

**Dave Jones:** And uh the base I think one of the simplest ways to do a metal detector is with you're going to have a transmitting coil and you're going to have a detecting coil on the thing.

**Dave Jones:** And then to use amplitude uh to actually detect the amplitude of the thing so that when you bring it close to metal like that like the two coils There's going to be two coils in here I would be guessing.

**Dave Jones:** And then uh normally they're going to be coupled and then you set the sensitivity of a threshold detector I.e. amplitude threshold detector so that um your circuit remain so that your buzzer doesn't go off.

**Dave Jones:** And when you bring metal in close proximity to it, of course, you're coupling some of the energy from that into here and it's generating eddy currents in there and it's sucking away some of the energy so that um, you're going to have less energy in your detection uh, coil and hence your amplitude is going to drop.

**Dave Jones:** Oh, did I do? No, that one doesn't need to be done, I don't think. And and then it's going to be a simple basically amplitude detector in there that detects whether or not you were it uh, drops so the amplitude on the coil will drop when you bring something into it.

**Dave Jones:** Aha, look at that. Discrete transistor by the looks of it. We've got one job here which is a it's a TL062 by the looks of it and uh, that is all she wrote.

**Dave Jones:** So, it looks like we've got a bit of discrete transistor action happening here. That'll be an oscillator. A bit of hot snot around here. That's a bit how you doing.

**Dave Jones:** And um, yeah, that wire that wiring is uh, a bit how you're doing as well. But yeah, it looks yeah, look, we've got a couple of coils there. Looks like we've got our two coils.

**Dave Jones:** So, one will be the transmit coil, one will be the detect coil. Nothing on the other side there and I think it will operate how I just uh, explained with amplitude level detection.

**Dave Jones:** So, yeah, I think we can reverse engineer that and get the schematic for it. And well, you certainly get exactly what you paid for. Your $17 retail at Harbor Freight.

**Dave Jones:** So, yeah, mm, couple of transistors and an op amp and a buzzer and a switch and a bit of hot snot and a pot and uh, Bob's your uncle.

**Dave Jones:** Now, as far as this uh, detection wand here goes, we've got both of our coils going into there around the outside. It looks to be hollow down in there although I haven't put a torch in.

**Dave Jones:** I suspect there's nothing else in there, like it's just like an air core and they're uh potentially just uh you know, helically wrapped around there or something like that.

**Dave Jones:** All right, so let's start uh reverse engineering this thing. I've checked that these three transistors here, they're an MPS A18. Off the top of my head, I didn't know what that was, so I went and got the data sheet for that.

**Dave Jones:** Sure enough, um one of them's a genuine Fairchild by the looks of it. The others are just like a generic uh brand, whatever. It's going to be identical. Now, um you've got to be careful.

**Dave Jones:** Transistor pin outs are a real trap for young players. Make sure you get the exact transistor. Don't rely on memory. Don't rely on oh, I think it's the same as something else cuz there's a lot of variation in transistors.

**Dave Jones:** So, this one's great. We've got the pin out for that, so we can work with that and it's just an NPN general purpose um transistor. So, you know, you could replace it with uh pretty much anything.

**Dave Jones:** It's pretty Joe Blog's. It's only a 45-V transistor with 100 mA collector current at maximum. So, yeah, not that terrific. And this part here is uh no surprises for guessing because it's around the battery input.

**Dave Jones:** Here's our switch just goes in there to just turn the battery on and off, basically. Um it's no surprises a 78L05 voltage regulator. So, you don't even uh need the pin outs for that.

**Dave Jones:** You know that even if you didn't know the pin outs, you know, look, there's the there's the 5-V output going to uh pin eight of the op amp there and going over here as well.

**Dave Jones:** So, yeah, too easy. You wouldn't even bother drawing that in. And our fourth transistor down here, it's actually a 2N 7000, which is an N-channel MOSFET. So, that's just driving the uh buzzer.

**Dave Jones:** So, once again, don't even need to know the pin out for that because you know it's just a low-side buzzer driver. That's it. Pretty basic. And I checked our detection wand here, looked down there with the torch, and yes, sure enough, you can tell by the weight of this wire there's a ferrite rod in there.

**Dave Jones:** So, both coils are wrapped around a ferrite rod. I did actually measure those coils, and of course, it's exactly what I I thought. There's going to be one drive coil and one detection coil.

**Dave Jones:** So, you know, as a basic thing, we'll just draw in a couple of coils like that. There we go. Effectively got ourselves a transformer. And our metal, of course, when we put that near it, will affect that and draw some energy away from that.

**Dave Jones:** So, whatever we're driving it with here, the amplitude on the detection coil here should actually drop. So, I think that's probably what's happening here is an amplitude detection type thing.

**Dave Jones:** And first of all, I can see that one of the coils there going over to the 5-V output there. So, that would be the drive coil most likely. And then, no surprises for finding this capacitor here, which is 10N.

**Dave Jones:** 10 nano, and that's directly across the coil. Bingo, we've got ourselves an LC tank circuit, and that's what you need to resonate. Now, there's a couple of ways to reverse engineer these This one's pretty simple, so you don't need any aids, really.

**Dave Jones:** You can just sort of go by memory and follow things through and know which ones you've done and which ones you haven't. But if it's a more complex board, some people actually put them in a photocopier and photocopy both sides and then trace it that way, trace it on paper, so that then you can mark off on the paper which ones you've actually which ones you've actually

**Dave Jones:** traced out. Or if you don't care about the board, which in this case I don't give a toss about, you can get yourself a marker. This is a whiteboard marker, but you can get a permanent marker, and then you can just draw in, yep, I've done that trace there, and turn it over, and I've done, yep, this one's a bit fat, so it's really annoying, but yeah,

**Dave Jones:** I've done those and those. And then you just go through uh trace by trace, looking both sides. It's not tricky here because like there might be the odd trace, you know, running under an IC package or something like that.

**Dave Jones:** But in this case, it's pretty darn easy to buzz those out if you have to. So, that's how we're going to reverse engineer that. I won't bore you with the details.

**Dave Jones:** I'll give you the final circuit in a minute. And you got to be careful you don't get trapped into topologies here. I thought I was getting something that looked like a some sort of diff pair or something with a common resistor going down to here.

**Dave Jones:** Turns out it wasn't. That was a complete furphy following the traces further. Um I found out that well, these are actually grounded right here. So, and then this is across here like this, which then that whoop and that did go up to the plus 5-V rail there, I believe.

**Dave Jones:** And then uh so, that's our midpoint voltage divider there. It's just, you know, my mind was going off somewhere else and it didn't turn out to be once you traced it further.

**Dave Jones:** Meh, it happens. And here's an example of where a trace goes under the chip. Uh pin three of the op amp here, which is the non-inverting input. I can't see any trace on the bottom.

**Dave Jones:** I can't see any trace on the top uh that it actually emerges from the chip. Sorry, I can't I'm not going to bother to show you up close. Anyway, uh hopefully you can follow what I'm saying.

**Dave Jones:** So, therefore, by deduction, it must go to one of the other pins of the op amp over here. So, you just get your meter out, buzz it out. And sure enough, pin three goes over to pin six there.

**Dave Jones:** No worries. And I think I've got it, but it's a little bit messy, so I've redrawn it a little bit better. Let's take a look at it. Now, I think this is correct, but uh please excuse me if it's not 100% correct.

**Dave Jones:** I haven't simulated it or anything like that. It's a uh basically a two-transistor arrangement here with, as I said, a ferrite core coupled effectively a transformer. So, this is the drive coil and this is the sense coil here.

**Dave Jones:** I've measured those. I had to take them out of circuit to measure them. Measure them at around about 10 kHz. I should have put that in there. Uh 1.7 mH for the drive coil and 18 micro henries for the sense coils.

**Dave Jones:** Now, of course, this thing has to start up in some way. So, it's got to get base current to do that and it does that via uh R3 up here 15K and the sense coil, you see, can go down there and start that transistor and we can get some oscillation happening here.

**Dave Jones:** And then we've got this convoluted arrangement down here. Basically, it looks convoluted, but all it is is basically they've got a series resistor R4 here and they're smoothing out any oscillation there.

**Dave Jones:** Okay, so we're basically getting DC at that point and then they've got Q3 connected as a transistor here and that's a quite a common thing. You you connect the base and the collector together.

**Dave Jones:** Bingo. And then we've got curiously an NTC thermistor in here across a 200 ohm resistor. So, they're trying to temperature compensate this thing in some way and maybe that's why they're using the transistor in there to try and temperature compensate between the other two cuz you notice that these two transistors here we've got we're going to have our base emitter drop here.

**Dave Jones:** We're also going to have the same base emitter drop here. So, it's going to be borderline in terms of actually driving these transistors. Anyway, then that goes down to VR1, which is a 10-turn trim pot on the board, which adjusts the bias level.

**Dave Jones:** So, effectively, this is like a DC bias level for the two bases joined here. And then we've got the sensor trim pot. That's the one on the front panel, that adjusts our sensitivity.

**Dave Jones:** So, we're adjusting a tiny amount of bias. You can see, because this one's in series and then in parallel with this and then in series with this and it's we're really just tweaking this thing by like half a bee's dick to get the bias correct, which then our sense coil down here, once this thing is oscillating, of course, our sense coil we're going to have a we're going going to have the

**Dave Jones:** oscillator waveform here, but then that's filtered out at this point, which goes into this comparator over here. And I was right in that this thing does actually just measure the amplitude and sense it based on half rail.

**Dave Jones:** So, we've got a 5-V regulator up here. We're just tapping off 2.5 V, smoothing that out a bit. I don't know why they bother with the buffer amp here, but you could have got away with a single op-amp there cuz it's going into high impedance here and it'd be going into high impedance here.

**Dave Jones:** So, you could have just connected that directly to there. Anyway, I don't know. Maybe they had uh dual op-amps in in stock, you know, coming out their wazoo and decided to use a dual instead of a single.

**Dave Jones:** Anyway, uh that sets the bias level. So, this is going to be precisely biased via these components to that half rail. So, it's going to be very very close to the 2.5 V that they've set here.

**Dave Jones:** Hence why they need a voltage regulator regulator in there, the 78L05, which I haven't shown here. Um they need a stable a temperature uh stable value in there. Anyway, then this um op-amp works as a comparator, of course, cuz there's no feedback on there if at all.

**Dave Jones:** There's no hysteresis, either. Um and that just drives the MOSFET, which drives the buzzer. So, it's not like this thing is working uh a lot of metal detectors will work as a beat frequency oscillator.

**Dave Jones:** So, they'll have two separate oscillators and they'll beat against each other at two high frequency like RF-type oscillators, then they'll beat against each other depending on the presence of the metal, and then that will give you an audio tone, which then gets mixed down and gives you an audio tone out.

**Dave Jones:** So, we're not actually we're not doing that here. All we're doing is doing some crude biasing of this oscillator to get a DC level and comparing the DC level.

**Dave Jones:** So, I don't know. It's a bit I don't know whether it's dodgy or clever. I'm not sure. Okay, so I've got my four-channel scope hooked up and I'm probing these points here.

**Dave Jones:** I'm going to be probing the two resistors down in here, the emitter resistors, and I'm also going to be probing the common base between those two, and I'm also going to be probing the output here, which goes into the comparator.

**Dave Jones:** So, they're my four points there. So, let's turn this sucker on. I've got no Whoop, there we go. Let me Let me turn that off. Okay, what we've got here, the yellow and white blue waveforms here, these are the two emitter resistors there and there.

**Dave Jones:** Of course, they're not going to be exactly the same value cuz this one is going to have a much greater oops, sorry. Oh, it went near the scope there.

**Dave Jones:** Um it's going to have a much greater load on it because there's no uh resistor up here, whereas this one's got R3. This transistor Q2 is going to have a higher value um even though the base currents should be basically the same.

**Dave Jones:** And then we've got our main oscillator waveform on the bases here. So, these the two common bases, this is coming from the sense coil here. So, this is this uh dark blue waveform.

**Dave Jones:** You can see it's oscillating about 37 uh {point} six kilohertz or thereabouts. Um that's, you know, typical what you'd expect out of this thing. I didn't expect, you know, megahertz or anything like that.

**Dave Jones:** So, that's going to be that value is going to be dependent on our um LC tank circuit here. Now, here's the interesting bit. This purple waveform here is the output of that smooth DC output going into our comparator there across C2 there.

**Dave Jones:** And if we change the threshold, you can only see it changes only a tiny amount and that's at 2 and 1/2 volts by the way. 500 They're all 500 millivolts per division.

**Dave Jones:** They're all at the same DC voltage level. Sorry, I should have mentioned that if it's not obvious on the screen. So, 1 2 and 2 and 1/2 volts there.

**Dave Jones:** So, it's just around the threshold voltage of there, of course, which is what you'd expect. So, that's been trimmed with VR1 and VR2, our sensitivity trim pot, which I'm adjusting now.

**Dave Jones:** So, there's not much not much play in that at all. And if we bring in some metal here, there we go. Can see it see it change, but there's not a huge amount in that.

**Dave Jones:** It doesn't change like it doesn't change by much before it calls up the buzzer. So, um and by the way, this buzzer is not solid, so I think our um it's sort of a bit intermittent between when it So, it must be oscillating here because there's no hysteresis on here.

**Dave Jones:** It just goes a bit funny. So, it tends to come and go a bit, but let's put some more metal towards that. So, a big chunk of metal like these pliers and look at that.

**Dave Jones:** We can get our oscillator to stop completely. We can just swamp it that whether or not. It doesn't like that. There's not enough feedback in our sense coil and we're just killing that sucker.

**Dave Jones:** But, of course, it's still going to buzz in that case because of the way that they've got the polarity on the threshold comparator there. Oh, by the way, sorry, I said that they're all 500 millivolts per division.

**Dave Jones:** No, the emitter resistors here are 200 millivolts per division. Sorry about that. That should have been obvious, of course, because it's going to be like 0.6 of a basic meter drop there.

**Dave Jones:** So, um what I've got now is I'm now probing the main tank circuit here, the collector of Q1, and of course because it's not clamped in any way, we're going to get due to the tank circuit, we're going to get voltage amplification here.

**Dave Jones:** So, this is 2 V per division, so we're getting 2 4 6 8 10 V peak to peak there roughly. So, there you go. That's a very interesting and I'm I'm going to say probably a bit crude circuit here.

**Dave Jones:** So, I think it might be interesting to try and simulate this sucker and try and get it going, but yeah, I don't know. It's I think it's a bit dodgy, but it Hey, it works and it sells for $17 retail at Harbor Freight.

**Dave Jones:** So, there you go. This is more complex you can get as I said like a beat frequency oscillator is a normal thing where you get the tone, but this one doesn't have like the audio tone as you actually get closer to the thing.

**Dave Jones:** So, it's just designed to be, you know, is there metal there or not? Yay or nay? Hence the Hence the buzzer down here, which of course is not a tone.

**Dave Jones:** It can't change the tone unless this thing oscillates here, which it's not generally supposed to do. It just basically turns the buzzer off or on and the buzzer just generates its own frequency unless you do something silly here cuz there's no hysteresis.

**Dave Jones:** And as I said, this is very crude and non discriminatory. You've seen it in action. It does basically ferrous stuff like steel, stainless steel. It does non-ferrous like silver for example.

**Dave Jones:** There we go. Gold and of course alloys like brass and things like that. So, yeah, it's completely non-discriminatory, but hey, it's as advertised. It's a metal detector. These metal detectors though needn't be this complex in quote marks.

**Dave Jones:** Um they can be as simple as a single uh transistor uh Colpitts oscillator basically. So, yeah, you know, they're incredibly simple. Like if you go buy one of those, you know, professional $5,000 discriminatory ones for finding gold, I'm sure they're much more complex than this and then this uh crude thing.

**Dave Jones:** So, anyway, um it might be interesting to uh try and uh simulate this thing and have a play around with it. I'll leave that up to uh your experimentation.

**Dave Jones:** Hopefully, I've got the circuit right uh cuz the always the risk when you reverse engineer one of these is that you goof something and yeah, Murphy will get you every time.

**Dave Jones:** But oh, that's going to be close anyway. So, I hope you enjoyed it. Thanks to um X Runner um for sending this one in a long, long time ago in a galaxy far, far away.

**Dave Jones:** And if you want to discuss it, EEVblog forum link is down below or leave YouTube comments or leave EEVblog.com blog comments and all that sort of stuff. And remember, if you like it, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
