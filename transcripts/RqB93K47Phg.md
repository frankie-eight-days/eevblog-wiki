---
video_id: RqB93K47Phg
title: EEVblog #714 - Metal Detector Reverse Engineering
url: https://www.youtube.com/watch?v=RqB93K47Phg
source: youtube-asr
---

**Dave Jones:** Hi, this is a bit of a catch-up video. It's an old mailbag item from a forum user called X Runner. So, thank you very much, X Runner. I know it's been a long, long time. It's probably been like a

**Dave Jones:** year and a half or something since he sent this in for to the mailbag for a teardown. What is it? One of these handheld metal detectors. One of these cheap-ass Harbor Freight things. It's like $17 on Harbor Freight. It's the

**Dave Jones:** Cen-Tech model 97245. And well, yeah, all $17 worth. And X Runner wanted to see if we can take it apart and explain how it works. So, I thought that would make a reasonably interesting video. We'll hopefully reverse engineer this and have a quick

**Dave Jones:** look at how one of these crusty metal detectors works. Let's go. And there's really nothing to it. Just runs off a 9-V battery here. By the way, I love this. Look, wear ANSI approved safety goggles when replacing the 9-V battery.

**Dave Jones:** You've got to be kidding me. Keep out of reach of children. Well, I shouldn't be allowed to use it then. Read the manual before use and keep it dry. Even though this is supposed to be like a waterproof

**Dave Jones:** wand on the end of it. I don't Yeah. Anyway, you get Well, you get $17 retail worth, really. Anyway, you just turn it on like that. And then it's got a sensitivity adjustment, of course, so you have no presence of no metal if you

**Dave Jones:** want it as sensitive as you can. Just turn it off like that. And then we can whack it over some things. So, you know, it gets within sort of like an inch or so of that screwdriver. And the pliers over here,

**Dave Jones:** this little It's got to get really, really close to that little nut there. And this tiny little screw, it's practically got to be touching. So, it's going to depend on the size of the metal object. And if we go for my

**Dave Jones:** stainless steel drink bottle, yeah, it's a good 2 or 3 in out from that, no worries. So, because that's a massive lump of metal there. And of course, this thing's pretty much going to detect any type of metal. It's not

**Dave Jones:** going to be a real discriminatory type. I I.e. it's not going to be able to detect the difference between gold and aluminum or something like that perhaps. But the whole idea is that yeah, it can detect ferrous and non-ferrous

**Dave Jones:** materials. Ferrous ones for example, you've got iron and the stainless steel that we've got here for example. And the non-ferrous stuff, you're going to have like copper and tin and gold and lead and all that sort of jazz. And

**Dave Jones:** it'll probably do various alloys as well and brass and stuff like that. So, yeah, I don't expect this thing to be very discriminatory. And if we turn the sensitivity all the way down, it still gets within an inch or so.

**Dave Jones:** And woohoo! There we Oh. Yeah, look at that. It's not bad It's not bad range actually for a $17 job. All right, let's crack this thing open and uh see, I think we can just do those screws on top.

**Dave Jones:** And uh the base I think one of the simplest ways to do a metal detector is with you're going to have a transmitting coil and you're going to have a detecting coil on the thing. And then to use

**Dave Jones:** amplitude uh to actually detect the amplitude of the thing so that when you bring it close to metal like that like the two coils There's going to be two coils in here I would be guessing. And then uh

**Dave Jones:** normally they're going to be coupled and then you set the sensitivity of a threshold detector I.e. amplitude threshold detector so that um your circuit remain so that your buzzer doesn't go off. And when you bring metal in close proximity to it, of course,

**Dave Jones:** you're coupling some of the energy from that into here and it's generating eddy currents in there and it's sucking away some of the energy so that um, you're going to have less energy in your detection uh, coil and hence your amplitude is

**Dave Jones:** going to drop. Oh, did I do? No, that one doesn't need to be done, I don't think. And and then it's going to be a simple basically amplitude detector in there that detects whether or not you were it uh, drops so the amplitude on the

**Dave Jones:** coil will drop when you bring something into it. Aha, look at that. Discrete transistor by the looks of it. We've got one job here which is a it's a TL062 by the looks of it and uh, that is all she wrote. So, it looks like

**Dave Jones:** we've got a bit of discrete transistor action happening here. That'll be an oscillator. A bit of hot snot around here. That's a bit how you doing. And um, yeah, that wire that wiring is uh, a bit how you're doing as well. But

**Dave Jones:** yeah, it looks yeah, look, we've got a couple of coils there. Looks like we've got our two coils. So, one will be the transmit coil, one will be the detect coil. Nothing on the other side there and I think it will operate how I just

**Dave Jones:** uh, explained with amplitude level detection. So, yeah, I think we can reverse engineer that and get the schematic for it. And well, you certainly get exactly what you paid for. Your $17 retail at Harbor Freight. So, yeah, mm, couple of transistors and an

**Dave Jones:** op amp and a buzzer and a switch and a bit of hot snot and a pot and uh, Bob's your uncle. Now, as far as this uh, detection wand here goes, we've got both of our coils going into there

**Dave Jones:** around the outside. It looks to be hollow down in there although I haven't put a torch in. I suspect there's nothing else in there, like it's just like an air core and they're uh potentially just uh you know, helically

**Dave Jones:** wrapped around there or something like that. All right, so let's start uh reverse engineering this thing. I've checked that these three transistors here, they're an MPS A18. Off the top of my head, I didn't know what that was, so

**Dave Jones:** I went and got the data sheet for that. Sure enough, um one of them's a genuine Fairchild by the looks of it. The others are just like a generic uh brand, whatever. It's going to be identical. Now, um you've got to be careful.

**Dave Jones:** Transistor pin outs are a real trap for young players. Make sure you get the exact transistor. Don't rely on memory. Don't rely on oh, I think it's the same as something else cuz there's a lot of variation in transistors. So, this one's

**Dave Jones:** great. We've got the pin out for that, so we can work with that and it's just an NPN general purpose um transistor. So, you know, you could replace it with uh pretty much anything. It's pretty Joe Blog's. It's only a 45-V

**Dave Jones:** transistor with 100 mA collector current at maximum. So, yeah, not that terrific. And this part here is uh no surprises for guessing because it's around the battery input. Here's our switch just goes in there to just turn the battery on and off, basically.

**Dave Jones:** Um it's no surprises a 78L05 voltage regulator. So, you don't even uh need the pin outs for that. You know that even if you didn't know the pin outs, you know, look, there's the there's the 5-V output going to uh pin

**Dave Jones:** eight of the op amp there and going over here as well. So, yeah, too easy. You wouldn't even bother drawing that in. And our fourth transistor down here, it's actually a 2N 7000, which is an N-channel MOSFET. So, that's just

**Dave Jones:** driving the uh buzzer. So, once again, don't even need to know the pin out for that because you know it's just a low-side buzzer driver. That's it. Pretty basic. And I checked our detection wand here, looked down there with the torch, and

**Dave Jones:** yes, sure enough, you can tell by the weight of this wire there's a ferrite rod in there. So, both coils are wrapped around a ferrite rod. I did actually measure those coils, and of course, it's exactly what I I

**Dave Jones:** thought. There's going to be one drive coil and one detection coil. So, you know, as a basic thing, we'll just draw in a couple of coils like that. There we go. Effectively got ourselves a transformer. And our metal, of course,

**Dave Jones:** when we put that near it, will affect that and draw some energy away from that. So, whatever we're driving it with here, the amplitude on the detection coil here should actually drop. So, I think that's probably what's happening here is an amplitude detection

**Dave Jones:** type thing. And first of all, I can see that one of the coils there going over to the 5-V output there. So, that would be the drive coil most likely. And then, no surprises for finding this capacitor here, which is 10N.

**Dave Jones:** 10 nano, and that's directly across the coil. Bingo, we've got ourselves an LC tank circuit, and that's what you need to resonate. Now, there's a couple of ways to reverse engineer these This one's pretty simple, so you don't need

**Dave Jones:** any aids, really. You can just sort of go by memory and follow things through and know which ones you've done and which ones you haven't. But if it's a more complex board, some people actually put them in a photocopier and photocopy

**Dave Jones:** both sides and then trace it that way, trace it on paper, so that then you can mark off on the paper which ones you've actually which ones you've actually traced out. Or if you don't care about the board, which in this case I don't

**Dave Jones:** give a toss about, you can get yourself a marker. This is a whiteboard marker, but you can get a permanent marker, and then you can just draw in, yep, I've done that trace there, and turn it over, and I've done, yep, this one's a bit

**Dave Jones:** fat, so it's really annoying, but yeah, I've done those and those. And then you just go through uh trace by trace, looking both sides. It's not tricky here because like there might be the odd trace, you know, running under an IC package or something

**Dave Jones:** like that. But in this case, it's pretty darn easy to buzz those out if you have to. So, that's how we're going to reverse engineer that. I won't bore you with the details. I'll give you the final circuit in a minute. And you got

**Dave Jones:** to be careful you don't get trapped into topologies here. I thought I was getting something that looked like a some sort of diff pair or something with a common resistor going down to here. Turns out it wasn't. That was a complete furphy

**Dave Jones:** following the traces further. Um I found out that well, these are actually grounded right here. So, and then this is across here like this, which then that whoop and that did go up to the plus 5-V rail there, I believe. And then

**Dave Jones:** uh so, that's our midpoint voltage divider there. It's just, you know, my mind was going off somewhere else and it didn't turn out to be once you traced it further. Meh, it happens. And here's an example of where a trace goes under the

**Dave Jones:** chip. Uh pin three of the op amp here, which is the non-inverting input. I can't see any trace on the bottom. I can't see any trace on the top uh that it actually emerges from the chip. Sorry, I can't

**Dave Jones:** I'm not going to bother to show you up close. Anyway, uh hopefully you can follow what I'm saying. So, therefore, by deduction, it must go to one of the other pins of the op amp over here. So, you just get your meter out, buzz it

**Dave Jones:** out. And sure enough, pin three goes over to pin six there. No worries. And I think I've got it, but it's a little bit messy, so I've redrawn it a little bit better. Let's take a look at it. Now, I

**Dave Jones:** think this is correct, but uh please excuse me if it's not 100% correct. I haven't simulated it or anything like that. It's a uh basically a two-transistor arrangement here with, as I said, a ferrite core coupled effectively a transformer. So, this is

**Dave Jones:** the drive coil and this is the sense coil here. I've measured those. I had to take them out of circuit to measure them. Measure them at around about 10 kHz. I should have put that in there. Uh 1.7 mH for the drive coil and 18

**Dave Jones:** micro henries for the sense coils. Now, of course, this thing has to start up in some way. So, it's got to get base current to do that and it does that via uh R3 up here 15K and the sense coil,

**Dave Jones:** you see, can go down there and start that transistor and we can get some oscillation happening here. And then we've got this convoluted arrangement down here. Basically, it looks convoluted, but all it is is basically they've got a series resistor

**Dave Jones:** R4 here and they're smoothing out any oscillation there. Okay, so we're basically getting DC at that point and then they've got Q3 connected as a transistor here and that's a quite a common thing. You you connect the base and the collector

**Dave Jones:** together. Bingo. And then we've got curiously an NTC thermistor in here across a 200 ohm resistor. So, they're trying to temperature compensate this thing in some way and maybe that's why they're using the transistor in there to try and temperature compensate between

**Dave Jones:** the other two cuz you notice that these two transistors here we've got we're going to have our base emitter drop here. We're also going to have the same base emitter drop here. So, it's going to be borderline in terms of actually

**Dave Jones:** driving these transistors. Anyway, then that goes down to VR1, which is a 10-turn trim pot on the board, which adjusts the bias level. So, effectively, this is like a DC bias level for the two bases joined here. And then we've got the sensor trim pot.

**Dave Jones:** That's the one on the front panel, that adjusts our sensitivity. So, we're adjusting a tiny amount of bias. You can see, because this one's in series and then in parallel with this and then in series with this and

**Dave Jones:** it's we're really just tweaking this thing by like half a bee's dick to get the bias correct, which then our sense coil down here, once this thing is oscillating, of course, our sense coil we're going to have a we're going going to have the

**Dave Jones:** oscillator waveform here, but then that's filtered out at this point, which goes into this comparator over here. And I was right in that this thing does actually just measure the amplitude and sense it based on half rail. So, we've

**Dave Jones:** got a 5-V regulator up here. We're just tapping off 2.5 V, smoothing that out a bit. I don't know why they bother with the buffer amp here, but you could have got away with a single op-amp there cuz

**Dave Jones:** it's going into high impedance here and it'd be going into high impedance here. So, you could have just connected that directly to there. Anyway, I don't know. Maybe they had uh dual op-amps in in stock, you know, coming out their wazoo and decided to

**Dave Jones:** use a dual instead of a single. Anyway, uh that sets the bias level. So, this is going to be precisely biased via these components to that half rail. So, it's going to be very very close to the 2.5 V that they've set here. Hence

**Dave Jones:** why they need a voltage regulator regulator in there, the 78L05, which I haven't shown here. Um they need a stable a temperature uh stable value in there. Anyway, then this um op-amp works as a comparator, of course, cuz there's

**Dave Jones:** no feedback on there if at all. There's no hysteresis, either. Um and that just drives the MOSFET, which drives the buzzer. So, it's not like this thing is working uh a lot of metal detectors will work as a beat frequency oscillator. So, they'll

**Dave Jones:** have two separate oscillators and they'll beat against each other at two high frequency like RF-type oscillators, then they'll beat against each other depending on the presence of the metal, and then that will give you an audio tone, which then gets mixed down and

**Dave Jones:** gives you an audio tone out. So, we're not actually we're not doing that here. All we're doing is doing some crude biasing of this oscillator to get a DC level and comparing the DC level. So, I don't know. It's a bit I don't know

**Dave Jones:** whether it's dodgy or clever. I'm not sure. Okay, so I've got my four-channel scope hooked up and I'm probing these points here. I'm going to be probing the two resistors down in here, the emitter resistors, and I'm also

**Dave Jones:** going to be probing the common base between those two, and I'm also going to be probing the output here, which goes into the comparator. So, they're my four points there. So, let's turn this sucker on. I've got no

**Dave Jones:** Whoop, there we go. Let me Let me turn that off. Okay, what we've got here, the yellow and white blue waveforms here, these are the two emitter resistors there and there. Of course, they're not going to be exactly

**Dave Jones:** the same value cuz this one is going to have a much greater oops, sorry. Oh, it went near the scope there. Um it's going to have a much greater load on it because there's no uh resistor up here, whereas this one's

**Dave Jones:** got R3. This transistor Q2 is going to have a higher value um even though the base currents should be basically the same. And then we've got our main oscillator waveform on the bases here. So, these the two common bases, this is

**Dave Jones:** coming from the sense coil here. So, this is this uh dark blue waveform. You can see it's oscillating about 37 uh {point} six kilohertz or thereabouts. Um that's, you know, typical what you'd expect out of this thing. I didn't

**Dave Jones:** expect, you know, megahertz or anything like that. So, that's going to be that value is going to be dependent on our um LC tank circuit here. Now, here's the interesting bit. This purple waveform here is the output of that smooth DC

**Dave Jones:** output going into our comparator there across C2 there. And if we change the threshold, you can only see it changes only a tiny amount and that's at 2 and 1/2 volts by the way. 500 They're all 500 millivolts per division.

**Dave Jones:** They're all at the same DC voltage level. Sorry, I should have mentioned that if it's not obvious on the screen. So, 1 2 and 2 and 1/2 volts there. So, it's just around the threshold voltage of there, of course, which is what you'd

**Dave Jones:** expect. So, that's been trimmed with VR1 and VR2, our sensitivity trim pot, which I'm adjusting now. So, there's not much not much play in that at all. And if we bring in some metal here, there we go. Can see it

**Dave Jones:** see it change, but there's not a huge amount in that. It doesn't change like it doesn't change by much before it calls up the buzzer. So, um and by the way, this buzzer is not solid, so I think our um it's sort of a bit

**Dave Jones:** intermittent between when it So, it must be oscillating here because there's no hysteresis on here. It just goes a bit funny. So, it tends to come and go a bit, but let's put some more metal towards that. So, a big chunk of metal

**Dave Jones:** like these pliers and look at that. We can get our oscillator to stop completely. We can just swamp it that whether or not. It doesn't like that. There's not enough feedback in our sense coil and we're just killing that sucker.

**Dave Jones:** But, of course, it's still going to buzz in that case because of the way that they've got the polarity on the threshold comparator there. Oh, by the way, sorry, I said that they're all 500 millivolts per division. No, the emitter

**Dave Jones:** resistors here are 200 millivolts per division. Sorry about that. That should have been obvious, of course, because it's going to be like 0.6 of a basic meter drop there. So, um what I've got now is I'm now probing the main tank

**Dave Jones:** circuit here, the collector of Q1, and of course because it's not clamped in any way, we're going to get due to the tank circuit, we're going to get voltage amplification here. So, this is 2 V per division, so we're getting 2 4 6

**Dave Jones:** 8 10 V peak to peak there roughly. So, there you go. That's a very interesting and I'm I'm going to say probably a bit crude circuit here. So, I think it might be interesting to try and simulate this

**Dave Jones:** sucker and try and get it going, but yeah, I don't know. It's I think it's a bit dodgy, but it Hey, it works and it sells for $17 retail at Harbor Freight. So, there you go. This is more complex you can get

**Dave Jones:** as I said like a beat frequency oscillator is a normal thing where you get the tone, but this one doesn't have like the audio tone as you actually get closer to the thing. So, it's just designed to be, you know, is there metal there or

**Dave Jones:** not? Yay or nay? Hence the Hence the buzzer down here, which of course is not a tone. It can't change the tone unless this thing oscillates here, which it's not generally supposed to do. It just basically turns the buzzer off or on and

**Dave Jones:** the buzzer just generates its own frequency unless you do something silly here cuz there's no hysteresis. And as I said, this is very crude and non discriminatory. You've seen it in action. It does basically ferrous stuff like steel,

**Dave Jones:** stainless steel. It does non-ferrous like silver for example. There we go. Gold and of course alloys like brass and things like that. So, yeah, it's completely non-discriminatory, but hey, it's as advertised. It's a metal detector. These metal detectors though

**Dave Jones:** needn't be this complex in quote marks. Um they can be as simple as a single uh transistor uh Colpitts oscillator basically. So, yeah, you know, they're incredibly simple. Like if you go buy one of those, you know, professional

**Dave Jones:** $5,000 discriminatory ones for finding gold, I'm sure they're much more complex than this and then this uh crude thing. So, anyway, um it might be interesting to uh try and uh simulate this thing and have a play around with it. I'll leave

**Dave Jones:** that up to uh your experimentation. Hopefully, I've got the circuit right uh cuz the always the risk when you reverse engineer one of these is that you goof something and yeah, Murphy will get you every time. But oh, that's going to be

**Dave Jones:** close anyway. So, I hope you enjoyed it. Thanks to um X Runner um for sending this one in a long, long time ago in a galaxy far, far away. And if you want to discuss it, EEVblog forum link is down

**Dave Jones:** below or leave YouTube comments or leave EEVblog.com blog comments and all that sort of stuff. And remember, if you like it, please give it a big thumbs up. Catch you next time.
