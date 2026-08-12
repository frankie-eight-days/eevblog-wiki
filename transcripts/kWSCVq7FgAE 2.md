---
video_id: kWSCVq7FgAE
title: EEVblog 1445 - How to Simulate an Oscilloscope Probe in LTSPICE
url: https://www.youtube.com/watch?v=kWSCVq7FgAE
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 43, "4": 59, "5": 74, "6": 90, "7": 106, "8": 120, "9": 135, "10": 149, "11": 161, "12": 175, "13": 188, "14": 204, "15": 215, "16": 229, "17": 249, "18": 260, "19": 275, "20": 291, "21": 302, "22": 314, "23": 327, "24": 339, "25": 354, "26": 372, "27": 385, "28": 398, "29": 411, "30": 426, "31": 441, "32": 456, "33": 469, "34": 484, "35": 497, "36": 514, "37": 530, "38": 544, "39": 557, "40": 572, "41": 588, "42": 602, "43": 614, "44": 625, "45": 640, "46": 654, "47": 671, "48": 685, "49": 696, "50": 711, "51": 726, "52": 737, "53": 754, "54": 768, "55": 783, "56": 795, "57": 810, "58": 825, "59": 840, "60": 857, "61": 871, "62": 883, "63": 897, "64": 910, "65": 924, "66": 942, "67": 960, "68": 978, "69": 994, "70": 1008, "71": 1025, "72": 1044, "73": 1063, "74": 1075, "75": 1089, "76": 1105, "77": 1119, "78": 1134, "79": 1148, "80": 1163}
---

**Dave Jones:** Hi, in this video I'm going to show you how to simulate an oscilloscope probe or in this particular case a times one oscilloscope probe because probing of your circuit can be a really important thing. Every time you probe it, doesn't

**Dave Jones:** matter how carefully you try and do it, you are effectively loading down your circuit in a often complex way. Now, I've done an entire video on this a long, long time ago in a galaxy far, far away. Uh what is it? Mysteries of times

**Dave Jones:** one oscilloscope probes revealed. So, I'll link that in up here and down below if you want to watch it and that's where I tell you about of course we've got a probe like this one which has a switchable times one times 10 switch on

**Dave Jones:** it and in times one position spoiler alert it has a very low bandwidth. This particular case about six and a half almost all switchable probes, this one has six and a half megahertz. So, your wiz-bang 100 megahertz 200 meg scope if

**Dave Jones:** you switch this to times one wah wah wah you're only got a bandwidth of six and a half megahertz. The reason I'm doing this is because well, sometimes it can be important and we might see this in a

**Dave Jones:** future video perhaps. So, circuit loading probe loading can be a big thing and system setup and measurement and stuff like that. I won't say any more at the moment because I haven't done my simulation yet. So, what I want to do is

**Dave Jones:** simulate this PP510 Siglent oscilloscope probe switchable you know, a real jelly bean 100 megahertz switchable times one times 10 probe. Now, we're going to be using LTSpice here because not only is it a really good simulator, it's not the

**Dave Jones:** easiest to use but it's really good and it's free from LT. There's lots of support and community out there for it. In this particular case we're using LTSpice because it has transmission line stuff. If you go in and place a

**Dave Jones:** component, it's actually got a transmission line like this, but this is an ideal lossless transmission line. This thing, as you've seen in the video, is not lossless. In fact, it is deliberately lossy. It's deliberately designed to be lossy. And thankfully,

**Dave Jones:** they do have another one called a lossy transmission line. So, this is what we're going to use. And when you actually go and place your lossy transmission line like this, it doesn't just work. And when you open up the

**Dave Jones:** parameter window for this, it's not obvious like how this works at all. It's just not going to do anything on its own. In fact, if you put it in there and try and simulate it, it'll go all your

**Dave Jones:** parameter values are zero and everything else. It's just going to ruin your day. Now, there is actually a handy resource for this sort of stuff. If you go over, there's actually a LT Wiki. And it's got a specific like a usage information on

**Dave Jones:** the lossy transmission line here. And then it's got the spice model parameters, the spice directive as it's called, which we'll use. But here's all the parameters that have to go into it. You can't just set it up in that model

**Dave Jones:** in LTSpice. It has to be included as what's called a spice directive. So, you've got the resistance in ohms per unit length. Because this is a lossy coax cable, it's not just a regular coax cable, it's lossy. It is going to have ohms per unit

**Dave Jones:** length. Because if you get your multimeter out, go and do it right now. If you haven't seen that video, you'll be surprised. Put your probe in the center here, put it on the end, put it in times one, and you don't measure zero

**Dave Jones:** ohms. You measure a couple of hundred ohms. And lossy coaxials are a very cool thing invented by John Kobbe at Tektronix. I don't know when, it was a long time ago. Um but yeah, hats off. Brilliant stuff. A lossy transmission

**Dave Jones:** line. Lossy coax, that's how we get the really high frequency really superb performance in modern passive probes. Anyway, we've got inductance in Henry's per unit length because well, every wire has got inductance in it and G that's conductance in Siemens in one

**Dave Jones:** which is one on ohms. Your multimeter might have a conductance mode but its value is going to be so high it doesn't matter. We're just going to leave that out today. And of course, capacitance per unit length. Then as I said, there's

**Dave Jones:** another parameter length. You can specify the unit length and then there's all sorts of sort of really simulation specific stuff which we're not going to touch here. There's various flags you can set for really more complicated simulations and

**Dave Jones:** stuff like that. Newton Raphson method for time step control and impulse response to keep your impulse response errors low and interpolation when your quadratic fails and stuff like that. Right, this is only if you're on like the bleeding edge of

**Dave Jones:** simulation which you have to touch this stuff. But all we have to do is set the RLC and a length and they show you how to do that here. And this is what's called the spice directive. So we can

**Dave Jones:** actually if you actually copy that over and we go into our LTSpice, this is where you have to start setting it up. But as I said, you can't just enter it in here. It's not going to work. So the

**Dave Jones:** first step is to right click on that and then set up the value is the name of your transmission line because you want it to be something descriptive. So I've put times one probe here. And then we have to go up here and insert a spice

**Dave Jones:** directive. And you can even have like a regular comment like down here oscilloscope input or this spice directive. And we can actually paste that in and then that will go and you put that anywhere on your schematic like

**Dave Jones:** this and that just sets up the directive to the spice engine. This one's labeled my lossy transmission line here but I've done another one. I've named it times one probe here. And the L T R A thing case doesn't matter here. That's the

**Dave Jones:** command to the spice simulator to actually do the lossy transmission line. That's the label you have to put in. And then you simply put in all the parameters that you want. The resistance 210 ohms, the capacitance 83 puff, the inductance 208, and the length

**Dave Jones:** is 1.2 m in this particular case or it's unit lengths. It doesn't have to be meters. So, I'll go into how I calculated these values in a minute, but let's actually go over. We've got our source here. I've just set that up as a

**Dave Jones:** sine wave at a 1 V amplitude, and then I've got a 50 ohm source impedance here, and then it just goes into our transmission line model that we've got here, and then we've got our oscilloscope input. So, we're modeling

**Dave Jones:** our the input to the oscilloscope because we we want to get a We're not just simulating the probe itself. If you did that, then you wouldn't have the oscilloscope input. But I want to model the whole effectively the system

**Dave Jones:** response including the oscilloscope input. And then this 68 ohm and 22.5 puff here is actually the compensation network. I just realized that this one's actually up in the probe here, but some of them down in the base here as I've

**Dave Jones:** explained in that video. So, technically I've got that back to front, but that's just designed to taper the response off. So, anyway, but yeah, I should actually put that up in the other end. Anyway, I'm just going to leave it there

**Dave Jones:** for now. I can't believe I just made that error. Anyway, I don't plan this stuff before I hit record. So, how did I get these values of 210 ohms? Well, I simply measured it. So, it's back to front. So, all the

**Dave Jones:** electrons are going to fall out. It has to be so that my eyes look in the right direction for the screen capture. What do we got? 329 ohms. There you go. So, I need to change that to 329

**Dave Jones:** ohms. Where do we get the 83 pF from? Well, 83 pF as we uh call it, well, it's in the data sheet here. It says in times one mode 85 pF to 120 pF. So, it's within that range. So, let's just call

**Dave Jones:** that an even 100 pF. And then if you divide that by 1.2 m cuz that's the length of this actual uh probe. So, we get a 1-m unit length. Um then we get a value of 83 pF. So, how do we calculate

**Dave Jones:** the inductance of 208 nH here? Well, we already know the cable capacitance of 83 pF here. Um so, let's assume a 50-ohm coax uh for example, the characteristic impedance is equal to square root of uh the L square root of LC. So, simply

**Dave Jones:** rearrange that formula to get L on one side and that works out to 208 nH. Cool. Actually, I'm just going to leave this uh compensation network here uh for now at the um oscilloscope end of the uh probe instead of up here. We might

**Dave Jones:** rearrange it later if we've got time. Now, um let's go simulate this thing. And well, is it going to work? Edit simulation command like this. So, we want an AC analysis like this. We'll just run linear, none of that log

**Dave Jones:** rubbish. Uh number of points, I'll just take 1,000. Um whatever, that's plenty to get like a a uh sweep. Start frequency 1 Hz, uh stop frequency 20 meg because I know the bandwidth of this is going to be about 6.5 meg. And you can

**Dave Jones:** see here how it's added this spice directive here. So, that just you know, it's this GUI interface is just a nice way of using spice, but spice is basically a command line thing that sort of runs in the background. So, and all of your

**Dave Jones:** simulation engines, they use the spice as is backbone. So, it's just up to the GUI interface just to make it nice. So, let's actually run that simulation, shall we? Wha- wha- wha- wha- analysis failed. Matrix is singular. Now, you might

**Dave Jones:** actually see this pop up a lot in your simulations, and not just on LTSpice. It might give you a similar error in another simulation engine. And what this means, the matrix is singular, it's got nothing to do with Keanu.

**Dave Jones:** It has to do with the fact that it thinks there's another part of your circuit which is floating. Basically, there's no like DC bias connection between them. So, you'll have you'll get this sort of error if you're doing a

**Dave Jones:** transformer simulation or something like that. So, just assume this was a transformer, you have a coil here like this, you have another coil on the other side like this, and there's no DC bias to get to the other side. So, the

**Dave Jones:** simulation just chucks a wobbly, and it just can't handle that. It doesn't like it. So, we can actually get around that by adding another ground point on this side over here. Because our ground point for our circuit is on this side, but obviously

**Dave Jones:** the transmission line model, it doesn't like having the other side. It thinks the other side is floating, and it gives you that error. So, if we fix that, we'll find that that should now run. Ta-da! And it does. Check out our

**Dave Jones:** response over here. Let me reformat this. Let's get rid of the phase plot there, cuz that just confuses things, and we'll add a cursor 3 dB there, cuz that's our bandwidth point, our minus 3 dB point, and it's 4 and 1/2 what? 4 and

**Dave Jones:** 1/2 MHz there. So, there you go, the simulation is now working. But, of course, you may not want to simulate with a ground reference point on both sides of the circuit here, cuz you can come a gutser, they can ruin

**Dave Jones:** your day if you're doing larger simulations. It might work for just something like this, that's fine. So, how do we get around that? So, if we delete that ground point, we can actually whack in a resistor here, flip

**Dave Jones:** that around, and we'll put in a high value resistor, make it 1 g ohm, something like that, and that will give a DC bias path, and it won't affect the simulation at all cuz it's such a high value, and we'll find that now, when

**Dave Jones:** we've got that DC bias path, this other side is no longer deemed to be floating in terms of the simulation, and we can run that, and boom, we get exactly the same result. It's just It's It's run again. It just updated then. Um and

**Dave Jones:** Bob's your uncle. So, that's a handy tip if you ever see that error message, uh you know that something's floating, you're going to have to add a DC bias or another ground reference in there to handle it. Now, how do we know this uh

**Dave Jones:** compensation value here of 22.5 pF? Uh once again, go back to the spec sheet here, and it actually tells you the compensation range is between 10 and 35 pF, so we'll you split that down the middle, and you get 22.5, and normally

**Dave Jones:** they have a series resistor in there of normally 68 ohms, but it's not going to make a huge difference. Like, we can lower that to, you know, 1 ohm, and you'll find that this won't really run that again, and yeah, it's like it's

**Dave Jones:** barely changed. It Like, you'll you won't even notice it. So, it's just a basically just a compensation network uh to ensure that the uh response doesn't go higgledy-piggledy at high frequency. It just rolls off and matches it properly.

**Dave Jones:** That's why there's actually the adjustment screw on here or on uh here. It's effectively the same at either end. Uh some manufacturers have it one end, some have it the other. It's like, "Meh." But, that is designed to

**Dave Jones:** compensate to match the input uh capacitance of your scope, and basically give you the like a total system response a flat response, and that's why it's important to compensate your probes. But, in terms of like the bandwidth and stuff like that, it

**Dave Jones:** doesn't have a huge impact. So, let's actually change that to 15 puff, and we'll run that again, and we should see that will change a little bit. There you go, it's uh 4.96 now. So, not a huge difference there. So, what I'm going to

**Dave Jones:** do now is move this compensation network over to the input side to match this specific scope probe that we actually uh have here. Okay, so I'm just going to delete that in there, and then we'll add a resistor in here like this, and this

**Dave Jones:** will be our uh 68 ohm jobbie, and then we'll add a cap uh across there like that. This stuff up here. There we go. So, that's our variable capacitor compensation network, but even it's not actually inside the transmission line

**Dave Jones:** cuz the transmission line starts like the actual coax, the lossy transmission line starts after there's a physical resistor and a physical cap um in there for the compensation network. So, there you go, 68 ohm, 15 puff. I've taken this

**Dave Jones:** out of circuit, so I can leave the components in there. They're just going to do absolutely nothing, and we can run that again, and what do we get? There you go, minus 3 dB at 4.77 meg. So, we're not quite getting the 6 and 1/2

**Dave Jones:** megahertz that we expect out of this thing. So, here's where we come to the practical difference between the compensation network in here in this signal probe. This is another signal probe, but it actually has the compensation network in there if you can

**Dave Jones:** see the hole. This is a 350 megahertz bandwidth one, so this is higher bandwidth. They'll typically have them um at the end on the higher bandwidth ones. The thing about this is that we can uh measure the resistance um from

**Dave Jones:** here to the tip, and that 329 ohms we put in there, um this one actually measures uh 220 or something. But, the problem is when you've got your resistor, your compensation network in here, it's a series resistance. So, you

**Dave Jones:** can't unless you chop your coax, you can't measure your coax. It's going to include this resistor value up here. So, what if I go 329 - 68? It's 261. So, I'm going to change that. Okay? So, here's where we could have come a

**Dave Jones:** cropper if we didn't realize that if you didn't know that there's a series resistor in this top compensation network here. So, let's run that again. Okay, we're getting a higher bandwidth. Will we get our 6 and 1/2 MHz? 5.5. OH,

**Dave Jones:** come on. Hang on, I just realized that the sheet that actually comes with the probe does not have the times one bandwidth on it. So, Siglent data sheet probe series, the PP510 probe 100 MHz. There you go. Oh, it's 6 MHz. I thought

**Dave Jones:** it was 6.5. I read that somewhere else. Um, so, we're actually after a figure of 6 MHz. So, that you know, there's going to be some wiggle room in there, but in theory, we can actually calculate the precise value of the input resistor in

**Dave Jones:** the compensation network because we can physically measure the resistance of this probe and then all we and we know the other parameters of it and then we can just back calculate, we can just iterate the value of that 68 ohm

**Dave Jones:** resistor to actually find what value it is to give us the 6 MHz bandwidth. And interestingly, the compensation range down here, this is actually different. It's 10 to 30, whereas this sheet says 10 to 35. So, uh, let's just go down to

**Dave Jones:** say 12 ohms like that. We'll have to change that to 318 in that case and we can run that again, but what are we going to get? Come on. 6.04. WE GOT ONE. THERE YOU GO. We've just determined that it's likely that this PP

**Dave Jones:** 50 510 probe likely has a compensation resistor in here of 12 ohms and a lossy coax of roughly 318 ohms. Like that because that gives us our response bandwidth that we're after. It gives the nominal data sheet value. So, there you

**Dave Jones:** go. Pretty cool, huh? And of course, you often don't need to go to this sort of level of simulation. You can just like simulate your just using the tip capacitance or the system capacitance as it's called because it takes into

**Dave Jones:** account the probe and everything else. You can just usually just lump it as a tip capacitance element. So, you don't have to go to this detail, but sometimes you might or you might for example want to like model the the actual clip lead

**Dave Jones:** you're in inductive clip lead like this or you might want to have another You might want to model like a transformer coupling into your ground lead like this. If you've got like 50 hertz mains or something or some other magnetic

**Dave Jones:** thing nearby that is coupling into your ground lead, you can like use this sort of simulation to actually see what's going on here. We we could actually delete this oscilloscope input like this and we can run that again and then we

**Dave Jones:** can go whoop. Then we can probe that like that. As you can see, that's going to be a higher bandwidth minus 3 dB. There is 7.8 megahertz if we don't include the oscilloscope input here. So, just the probe itself has a bandwidth of

**Dave Jones:** 7.8 meg, but it's lower when you include the oscilloscope input with its whoop, it's gone off there with its 15 nominal 15. I think it's 15 puff input on the Siglent. Might have checked. Could be 18 or something like that, but you get the

**Dave Jones:** idea. This is how you simulate a oscilloscope probe or a the complete system oscilloscope probe with the ground reference on this side. So, there you go. I hope you found that useful and interesting. If you did, please give the

**Dave Jones:** video a big thumbs up and cuz that feeds the algorithm. And as always, you can discuss in down below. Catch you next time.
