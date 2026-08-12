---
video_id: xaELqAo4kkQ
title: EEVblog #279 - How NOT To Blow Up Your Oscilloscope!
url: https://www.youtube.com/watch?v=xaELqAo4kkQ
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 30, "3": 46, "4": 64, "5": 77, "6": 89, "7": 104, "8": 122, "9": 137, "10": 153, "11": 166, "12": 180, "13": 196, "14": 212, "15": 228, "16": 243, "17": 252, "18": 264, "19": 278, "20": 290, "21": 308, "22": 325, "23": 340, "24": 356, "25": 369, "26": 383, "27": 395, "28": 408, "29": 422, "30": 436, "31": 453, "32": 471, "33": 487, "34": 503, "35": 519, "36": 531, "37": 544, "38": 559, "39": 573, "40": 580, "41": 596, "42": 609, "43": 623, "44": 641, "45": 657, "46": 674, "47": 691, "48": 707, "49": 728, "50": 747, "51": 761, "52": 774, "53": 790, "54": 807, "55": 822, "56": 840, "57": 854, "58": 869, "59": 887, "60": 901, "61": 915, "62": 934, "63": 953, "64": 966, "65": 986, "66": 1002, "67": 1016, "68": 1031, "69": 1046, "70": 1062, "71": 1078, "72": 1093, "73": 1105, "74": 1117, "75": 1132, "76": 1149, "77": 1166, "78": 1182, "79": 1198, "80": 1213, "81": 1225, "82": 1241, "83": 1258, "84": 1275, "85": 1294, "86": 1311, "87": 1326, "88": 1339, "89": 1353, "90": 1367, "91": 1383, "92": 1398, "93": 1410, "94": 1426, "95": 1441}
---

**Dave Jones:** Hi, I just read a post on the EEVblog forum where somebody was asking about the oscilloscope probes and how they can be potentially dangerous if you hook this ground lead up to the wrong point in your circuit. You can blow up

**Dave Jones:** your circuit, you can blow UP YOUR SCOPE. BANG! And it really is a big trap for young players and I've mentioned it before, but they wanted to know exactly under what circumstances that could happen. If I could do some diagrams to

**Dave Jones:** explain it and things like that. Well, glad you asked. Let's try and sort it out. So, what's actually causing the problem here? Well, it's to do with the fact that the BNC connector, the outside ring of the that metal outside ring of

**Dave Jones:** the BNC connector on almost all benchtop oscilloscopes like this are what's called mains earth grounded. They're mains earth reference. In other words, this metal shell on the outside of the BNC is connected directly via a very low impedance path, dead short,

**Dave Jones:** through to the mains earth on the back of the oscilloscope on the IEC connector and hence through to the mains earth in your system. So, if I've got a power cord, here's an IEC power cord, it's plugged happens to be plugged into the

**Dave Jones:** same power board as this oscilloscope, but it doesn't have to be. It can be on the opposite side of the room, the opposite side of the house or factory or whatever, the mains earth will be common and tied together throughout the whole

**Dave Jones:** system. So, I've got my multimeter here set to ohms. Let's make sure we probe the right thing. I'm going to probe earth, the center earth pin there, and I'm going to probe the BNC. And there it is, 0.9 ohms. It's

**Dave Jones:** effectively a dead short. There's some There's some DC resistance in there, but it's a very low resistance path. Effectively, well, it is a dead short through to mains earth. And that can be problematic, as I'll explain. And, because that outside shell of the BNC

**Dave Jones:** connector is connected directly through to your earth pin here, you're going to get the exact same response on your earth pin. There it is. It's a dead short. Look at that. And, because it's a very low impedance path,

**Dave Jones:** this path is capable of actually carrying a lot of current. If you hook it up to the wrong point, and it can do a lot of damage. This little uh ground attachment lead is probably the weak link in the whole system, because the uh

**Dave Jones:** shield of the uh of the coax going back and the internal connections all going back to mains earth, that's very, you know, very chunky bits of copper in there. But, this is probably the weak system. So, this is going to blow up or

**Dave Jones:** vaporize if you attach this to the wrong point, and you have enough energy in your system. You can blow this probe apart in your hand. Bang! And, just as an aside, on any multi-channel scope like this, be it two or four-channel

**Dave Jones:** like this one, these both of the BNC connectors are shorted together. So, there you go. They're shorted together and through to mains earth. So, if you've got your two probes like this, they're both connected to your oscilloscope, these two grounds are

**Dave Jones:** shorted together. You can't just put these willy-nilly anywhere in your circuit, because if you put them to anywhere that is not the same voltage potential, i.e. both ground or both plus 5 volts or whatever, then, if they're different potentials, you'll short out

**Dave Jones:** that thing. Here's a power supply. I'll show you. If I connect one ground lead to the positive output, another one to the negative, bang! I short the output. That can ruin your day. Don't do it. And, not only that, if that particular

**Dave Jones:** uh point in your circuit that you're shorting out has a large amount of energy in it, and you get a huge current through this by shorting it out, bang! You can blow up your probes, and sparks can fly everywhere, real nasty stuff.

**Dave Jones:** So, let's try and take a look at this and figure it out what's happening on a diagram here. Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. So, what I'm

**Dave Jones:** going to show here is three different scenarios. This is scenario number one, and I'm going to assume a single probe, not the dual probe thing I showed you before. That's a different thing. We're talking about this mains earth

**Dave Jones:** referenced problem. So, what we've got here is we've got our scope, okay? And it's got the BNC connector here, and it's got the IEC mains input connector going down to earth down here. And note the different symbols. This chassis

**Dave Jones:** mains earth symbol here is different to internal ground symbols. That's just in a little aside. It's not really important for the purposes of this, but as you saw with the measurement before, that BNC is shorted directly through to

**Dave Jones:** mains earth, and it's also shorted directly through to the alligator clip on your probe here, or your crocodile clip, whatever you want to call it. Now, here's your widget, your circuit that you're probing. And it For simplicity's sake, let's say it has a positive rail

**Dave Jones:** and an internal ground rail as well, and various points in your circuit that you're probing, okay? Now, let's assume that it's battery powered, or what's called floating. It's completely floating. It is not referenced in any way back to mains

**Dave Jones:** earth. It's just isolated in its own little world. It's not connected to anything else. Now, uh that means in this scenario here, you can connect this alligator clip through to any part of your circuit. It can be connected to ground, could be connected

**Dave Jones:** to your positive rail, or any other part of your circuit, and you won't do any damage at all. Why? Because there's no current flow. There's no way there's no loop here. It's not going to flow anywhere. Current just can't magically

**Dave Jones:** flow down that alligator clip through the circuit unless there's a return path. If you've got a floating system like this, there's no way the current can flow through there. So, you can hook that alligator clip in a floating

**Dave Jones:** circuit to any point in that circuit and you won't do any damage. What you will do is actually put. If you connect it through to this point here in your circuit, then you've mains earth referenced that point in the circuit.

**Dave Jones:** What does that mean? Well, it just means that you've connected it through to mains earth. It doesn't It may not do anything. In most cases, it's not going to cause a problem at all unless there's some, you know, you're working on audio

**Dave Jones:** circuits and there's hum and all sorts of things, but we won't go into it. Pretty much, scenario number one, isolated um widget you're working on, completely safe to hook up the alligator clip or the probe to anywhere else in the

**Dave Jones:** circuit. And because the probe is connected to the tip of the probe is connected to your 1 meg input impedance on your scope. Let's not talk about times 10 probes and things like that. It's a 1 meg resistor. You The worst

**Dave Jones:** you're going to do is put a 1 meg resistor across any point in your circuit. Usually, not a big deal. You certainly can't blow anything up. Not a problem. All right, let's look at scenario number two. Where we've got one of these

**Dave Jones:** isolated mains supplies or a plug pack. We've got our 110 or 240 V mains coming in here and there's no earth pin. We've only got our active and our neutral there and we've got a isolation transformer 50-60 Hz and

**Dave Jones:** there's physical isolation, electrical isolation, between the primary and the secondary winding. So, there's no direct electrical path. There's just a little bit of capacitance, really, but you know, there's no direct electrical connection. So, it's an isolated supply. So, I've

**Dave Jones:** just pictured here it's a, you know, a half-wave bridge rectifier, but it can be a switching power supply, a switching plug pack, or a regular transformer-based plug pack. Makes no difference. If it's got that electrical isolated supply and no

**Dave Jones:** earth no earth connection at all, then it's exactly the same as scenario number one with our battery supply. No different. You can connect your alligator clip up to any point in your circuit, any rail, anything, and you're not going to blow anything up. No

**Dave Jones:** current's going to flow because current can't flow, DC current can't flow through this transformer in any sort of loop at all. Completely safe. Now, these isolated plug packs are pretty easy to spot because they've only got the two

**Dave Jones:** pins on them, active and neutral. There's no third earth pin. Some of them might have a third earth pin just for mounting, or they might have it to connect through to the internal transformer as a safety thing, but they

**Dave Jones:** will still be isolated. And if you're unsure if it does have that third pin, measure it. Take the output here, use your ohmmeter, measure it between the ground pin or both pins just to be sure and the earth pin. If you don't measure

**Dave Jones:** that direct short, then it's an isolated supply. And that can be a switching type or the old-fashioned direct transformer type. And the other type might be one of these switching plug packs. Another dead giveaway, it's only got the two pins,

**Dave Jones:** the active and neutral. It doesn't have the third pin going in there. Now, here's an interesting one. This is my Dell notebook power supply. And as you can see, it's got three pins on the mains input cord, and it certainly has

**Dave Jones:** the earth pin on the connector. So, let's measure it. Let's see what we get.

**Dave Jones:** Look at that. It's 1K. Instead of a direct short, this one, for whatever particular reason, is uh only 1K. And that that's pretty darn low. And that can ruin your day. The I would classify that as quite low impedance. Not as low

**Dave Jones:** as a dead short, of course, but still you wouldn't want to uh go uh probing in such a system with your oscilloscope. If you had your notebook you were trying to repair your notebook and you were powering it from this, then well, you

**Dave Jones:** know, you've got that 1K through to mains earth. I'd be disconnecting this when I worked on it if I had to probe it live and power it directly from its battery so it was completely isolated. Now, let's look at scenario number

**Dave Jones:** three. What's called a mains earth referenced power supply or a mains earth referenced product or mains earth referenced system. It's the same as before. It might have an isolation transformer in there, but it has that third earth connection which shorts out

**Dave Jones:** the secondary side. It's almost always the negative uh line, but you know, it doesn't have to be, but it almost always is. The negative line is shorted out and could be shorted to the primary. So, you lose that isolation there. So, this is

**Dave Jones:** now connected through to this mains earth back here, back at your power point in your house wiring, your office wiring, your lab wiring, whatever. It's all connected right back. And then that is connected through to your negative terminal and your negative

**Dave Jones:** terminal is connected up here. So, effectively your circuit ground is now almost always, once again, it doesn't have to be the negative point in your product, but it almost always is. So, that is not only uh just uh

**Dave Jones:** a common ground inside your product, it's also referenced to mains earth. Now, why is this an issue? Well, look what happens now if we connect this alligator clip up to this positive rail up here. You know how it wasn't a problem before? No current

**Dave Jones:** flowed, no danger whatsoever. Well, what happens now? This positive rail, current can flow through here, through the shield of your BNC, through the oscilloscope, down through mains earth, down here, back through your power board, back into your uh, the lead, the IEC lead coming into

**Dave Jones:** your product, all the way through here, and up through your ground. Bingo! Congratulations, you've just shorted that point there to that point there with a very low impedance connection through that uh, alligator clip, that crocodile clip, and your scope probe. And what happens?

**Dave Jones:** Bang! It blows up. Or, you know, if if this rail up here has a lot of energy, can supply a lot of energy, you can vaporize your earth lead. It can explode in your hand. Real nasty stuff. If it's

**Dave Jones:** a real low energy thing, well, your product might just shut down and it's not inherently like not massively uh, dangerous. If your power supply is not capable of actually delivering a lot of current, then, well, your product you

**Dave Jones:** short out your power rail and it doesn't blow up, but your circuit's not going to work anymore. Okay? So, you want to avoid that. So, that's why when you're probing around with a mains earth reference oscilloscope, like almost all bench uh, oscilloscopes

**Dave Jones:** are, if you're dealing with a mains earth referenced product, be very careful where you put that alligator clip, that crocodile clip in your circuit. Because if it's not at the same point, which is equipotential is the technical term, or the same

**Dave Jones:** potential, equal potential, in there as your ground line, you're going to short out that particular, ever a voltage rail or a signal wire or something like that. It's going to blow up. It'll ruin your day. So, there you go. That's what happens

**Dave Jones:** with a mains earth reference system. Beware. Now, let's have a look at some bench power supplies here. You'll note that any good bench power supply will have three output terminals, positive, negative, and what's usually a green one, which is a dead giveaway,

**Dave Jones:** which they call ground. Okay, it might be called ground. That's actually mains earth back on the mains input lead on this thing. So, normally, if you don't join these together, if, you know, if you haven't joined them together at all,

**Dave Jones:** these power supplies are floating. They're completely safe. You hook up your positive negative like this to your positive and negative terminals, and you can power your circuit, you can probe around, completely safe. But, if you strap these two terminals together, like

**Dave Jones:** on this power supply over here, you see a lot of them will come with one of these straps that allow you to strap the mains earth through to the negative terminal, and that instantly turns that isolated power supply into a mains earth

**Dave Jones:** reference power supply, and the product you're powering, you need to be very, very careful where you probe with an earthed oscilloscope. Now, why would you want to join these together? I won't go into the reasons, cuz it has to do It depends on the

**Dave Jones:** system you're you're actually designing and things like that. So, I won't go into it. But, if they are joined together, and you mains earth reference that, beware. But, I don't think I can leave it there without giving you a bonus one. Number

**Dave Jones:** four, USB products. And it can be other connections as well, not just USB, but USB's a common example these days. Let's say you have your widget and it's battery-powered, okay? It's normally completely isolated and completely safe to probe any way you want with your

**Dave Jones:** oscilloscope, but once you connect the USB lead through to your computer, you're in deep trouble. Why? Because the US ground pin on the USB connector is almost always connected, unless you got like an isolated USB, which are very rare and very

**Dave Jones:** specialized, uh it'll be connected through to the ground point of your circuit in there. And then that lead will go back to your the USB port on your computer down here, which will be connected through to the ground point on

**Dave Jones:** your circuit board and your processor and everything else. But, your uh the ground point in your PC is also mains earth reference. Almost all PCs are, and it goes through to mains earth directly through. And you can measure that. So, bingo, your isolated

**Dave Jones:** product has just become mains earth reference by the mere fact of connecting up that USB cable. And you've got that dangerous loop scenario happening again, and you've got to be careful where you pro- where you connect the alligator

**Dave Jones:** clip or the ground lead on your oscilloscope. If you connect it up here, bang, you've just shorted the whole thing out again. Beware. Now, I know you won't believe me unless I practically demonstrate it, so I will. We've got an Arduino compatible board

**Dave Jones:** here. In this case, it's the Freetronics 11 board. And if you're powering your little Arduino board from your plug your isolated plug pack power supply, remember, no mains earth pin, and you're powering it, then you're completely safe because it's isolated. Or you're

**Dave Jones:** powering it from a battery, completely safe, it's isolated. But, if you take your USB cable here and it's hooked up to my desktop computer here and we plug that in and we power our board. There it is, it's turned on.

**Dave Jones:** We're powering our board from our USB, what happens? We've got our mains cable here. Let's measure mains earth and see what we get. Here's the ground pin on our circuit. Look at that, 9 ohms. There you go, cuz it's got to go through

**Dave Jones:** all dicky stuff in the computer and things like that. It's shorted to mains earth. Bingo. So, your sweet little innocent Arduino board that you thought was isolated has just become a real potential problem. And if you try and

**Dave Jones:** probe around here with your oscilloscope or if you try to probe your circuit or your shield connected onto there with the with the alligator clip on your probe probe and you put it anywhere other than that ground terminal, you're screwed.

**Dave Jones:** You're going to short out the power supply, the Arduino will shut down. It won't blow up your face because the little power supply on the Arduino can't generate, you know, huge amounts of current and and provide a large amount

**Dave Jones:** of energy, but it's going to shut down, short out your power supply. actually damage your power supply on your Arduino or you might damage your plug pack or something else. So, that can be a real issue even if it's battery powered.

**Dave Jones:** You're powering this thing from the battery or from the Once you connect that USB lead up, you've instantly mains earth connected it and you've ruined your day. And don't try this at home. I'll actually demonstrate it. We've got our

**Dave Jones:** Arduino, it's working. There's the LEDs flashing away and it's hooked up to our mains earth reference computer via the USB and if I hook up the ground lead to the ground the earth lead on my oscilloscope up to the ground point on the circuit,

**Dave Jones:** no problem. Still continues to work. I can probe away. Everything's safe. But, if I connect this through to the power rail, the ground lead, watch this. Ready? Don't try this at home. Bang! And you might be able to hear the

**Dave Jones:** computer reboot. Because the device has shut down. I've just I've just shorted out my power supply. Nasty. And if you do that to a high energy circuit, you can blow the thing up. Blow up your scope probe. Nasty.

**Dave Jones:** But, if I do the exact same thing again, powering it from the isolated plug pack, it's not mains earth referenced anymore. So, I can plug my ground lead onto the ground and it's fine, of course. And I can plug my ground lead anywhere else on

**Dave Jones:** the circuit. That's the same point that was causing it to short out before and it doesn't do anything because this board is floating. It's not It's isolated. It's not mains earth referenced. I can put that ground lead on any point in my circuit and it's not

**Dave Jones:** going to affect it. So, what do you do if you've got one of these mains earth referenced products and you can't avoid it being mains earth referenced and you want to probe it safely or you're working on, you know, a high voltage

**Dave Jones:** high energy switch main switch mode power supply and you want to safely probe everything? Well, the way to do it is with a a high voltage differential probe and I'll show you some examples of this. Here's a BK Precision PR 60 uh

**Dave Jones:** probe. We're only talking, you know, 300 and something dollars for these type of probes. And as you can see, it converts the single ended BNC input for the oscilloscope through to an isolated differential probe system like this. So, you can put

**Dave Jones:** positive and negative anywhere in any product at all, mains earth referenced or not, and they and it be completely safe and usually these probes are actually high voltage probes. So they actually have a times 10. So this one's

**Dave Jones:** switchable between times 10 and times 100 attenuation. So it actually replaces your traditional times 10 single-ended oscilloscope probe. But now it's differential completely isolated and they can be isolated to you know several many hundreds of volts or several

**Dave Jones:** thousand volts. In this case common mode plus minus 700 volts and the differential can be plus minus 700 volts as well. And there's other ones. Here's an Agilent one. Same thing. You know, single-ended oscilloscope input through to a differential

**Dave Jones:** probe output. There it is. That's a high 100 megahertz high voltage differential probe. And there's lots of other ones on the market. There's LeCroy one, you know, there's a whole bunch. Yokogawa make them. Every man and his dog makes these high voltage

**Dave Jones:** differential probes. And I highly recommend you pick one up. It should be pretty much a standard kit especially if you're working on switch mode power supplies or something like that. They're a little bit on the expensive side, but

**Dave Jones:** safety first. And there are other ways to get around the issue as well and that is to use a mains isolation transformer like one of the ones shown here. It basically it does exactly what it says. It isolates

**Dave Jones:** the mains 240 volt in earth 240 volt out isolated and that's designed to power your product under test. And it tells you here isolate test equipment like crows or protect switch mode power supplies and things like that. But this

**Dave Jones:** can be used to isolate your oscilloscope so that your oscilloscope is not mains earth reference anymore, but that's not really the recommended way to do it. Your oscilloscope should remain for safety reasons a grounded a mains earth grounded product. So, you

**Dave Jones:** should use the isolation transformer to power your particular product under test. And this can be an essential bit of kit in any test or repair lab. And if you've got a USB product and you want to isolate that, you don't want

**Dave Jones:** your USB cable to cause any issues, then you can get one of these rather an obscure product, a USB isolator. There's not too many of them around, but they basically go it's got a transformer in there with some

**Dave Jones:** high-speed to couple not only the power lines but the data lines as well at full USB speed. These things aren't particularly cheap. They're a fairly fairly niche thing, but it isolates USB in USB out. The output is completely

**Dave Jones:** isolated data and power. So, there you go. I hope you found that interesting. So, just be careful and watch out for mains-earth reference systems next time you're probing your oscilloscope. You don't want to blow up your oscilloscope. You don't want to blow up your probe.

**Dave Jones:** And most of all, you don't want to blow up yourself. So, if you liked the video, please give it a thumbs up and I'll catch you next time.
