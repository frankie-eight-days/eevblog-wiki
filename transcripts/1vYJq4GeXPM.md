---
video_id: 1vYJq4GeXPM
title: EEVblog #971 - Zero Standby Power TV - BUSTED!
url: https://www.youtube.com/watch?v=1vYJq4GeXPM
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 33, "3": 49, "4": 62, "5": 75, "6": 89, "7": 103, "8": 117, "9": 135, "10": 150, "11": 166, "12": 182, "13": 196, "14": 213, "15": 226, "16": 241, "17": 257, "18": 274, "19": 287, "20": 303, "21": 320, "22": 334, "23": 349, "24": 363, "25": 379, "26": 399, "27": 416, "28": 431, "29": 443, "30": 459, "31": 468, "32": 481, "33": 497, "34": 513, "35": 528, "36": 543, "37": 558, "38": 571, "39": 591, "40": 604, "41": 621, "42": 638, "43": 655, "44": 675, "45": 686, "46": 699, "47": 712, "48": 725, "49": 739, "50": 751, "51": 766, "52": 786, "53": 801, "54": 816, "55": 831, "56": 848, "57": 862, "58": 880, "59": 894, "60": 908, "61": 927, "62": 946, "63": 961, "64": 979, "65": 994, "66": 1011, "67": 1022, "68": 1037, "69": 1057}
---

**Dave Jones:** Hi, you know what I hate? Marketing You know what I hate worse? When it comes from a university who should know better. Uh, here we go. Let's take a look at the University of Bristol's pioneering chip that extends sensors battery life. A

**Dave Jones:** low-cost chip that enables batteries in sensors to last longer, in some cases by over 10 times, has been developed by engineers from the University of Bristol. Uh, boy. Okay, right off the bat we have some batterizer type marketing here. In

**Dave Jones:** some cases by over 10 times. Anyway, let's give it a go. Dr. Bernard Stark and colleagues in the Bristol Electrical Engineering Management Research Group, sounds awesome, um, have developed a voltage detector chip that requires only a few trillionths of a watt, picowatts

**Dave Jones:** for those playing along at home, to activate other circuits. The research research group are providing samples of their chip to companies to use, which will enable engineers to design sensors that continuously listen without using power from a battery or mains. The

**Dave Jones:** result is smaller batteries or a battery life that is extended in some case by years. The voltage detector can also eliminate standby power. Exa- For example, the team have demonstrated a TV with no continuous draw of power during

**Dave Jones:** standby by using a voltage detector that is powered up at a distance directly from the infrared signal of a standard TV controller. Sounds awesome. So, what they've actually developed here is this UBM 20 voltage detector IC. It looks

**Dave Jones:** like a little five-pin SOT23. Great, I love it. And the device is sensor driven, it requires no power supply, instead it uses power from a sensor signal to wake up. So, it's basically an energy harvesting, uh, type thing. And

**Dave Jones:** once again, here they are touting this television with zero standby power like it's going to save the planet. So, right off the bat I'm going to say that I love ultra low power devices and researching the new devices, new parts available.

**Dave Jones:** This is fantastic. So, nothing against the chip whatsoever. I think they've done a really nice job here. Typical applications perpetual uh sensing event driven sensing uh Internet of Things grown. But, okay. Um it's a nice little chip. 0.65 V input uh threshold and

**Dave Jones:** trigger extremely low quiescent current of 5.4 pF at 1 V. That's picoamps for those playing along at home. And the output uh leakage open drain current is only 100 pA. So, that's really quite nice. And basically, here it is. You've got energy

**Dave Jones:** harvesting input, in this case RF, but it could be infrared, it could be uh you know, motion, vibration, whatever it is. Um and basically, it gives you an open drain output to then further trigger a power uh switch here, which then can

**Dave Jones:** turn your um widget off and on, be it a TV or, you know, a little Internet of Things thingamabob. Okay, let's watch their promotional video. our daily lives, electronic devices with sensors help us to stay healthy and safe.

**Dave Jones:** background. In this video, we show a way of reducing the power consumption of these devices, in some cases by over 90%. 90%? to be done with smaller, more convenient devices. Sounds good. device uses power to do two things:

**Dave Jones:** listen and react. Yep. Both require power. They do. Some devices use most of their energy to do the listening. Hang on. What? case would be an earthquake Most? 99%? Throwing out a decent number there. detector that listens for a quake for

**Dave Jones:** years and then reacts by recording the tremor that lasts just a few seconds. So, you've got to be careful what you're talking about here. Are you talking about an earthquake detector that just sounds a claxon alarm when, you know,

**Dave Jones:** the building starts shaking? Or you're talking about uh earthquake monitoring, seismic monitoring equipment, in which case they need to be running all the time continuously because you want to see what happened before the event. And what about little tremors and things like

**Dave Jones:** that? You want to be continuously monitoring. But hey, they do mention earthquake detectors, so 99% of the battery is wasted. But the question to ask here is how long does the battery last? I'm glad you asked. An earthquake alarm, here it is. You go

**Dave Jones:** into the frequently asked questions. It's got a 5-year battery life from a 9-V battery. Here's another one which works off a lithium battery. It's also got a 5-year battery life. So, where is this BS about This is their big example

**Dave Jones:** of something that, you know, it wastes 99% of the battery power. Yeah, it might, but it gets 5 years. So, it's not like you can put their whiz-bang new chip in there and all of a sudden get a 500-year

**Dave Jones:** battery life. Good luck finding one of those. Our team at the University of Bristol, with government support, have developed a method of eliminating keep-alive power drain using minute, insignificant quantities of energy from the event that the device is waiting for. This energy

**Dave Jones:** switches a mains- or battery-powered devices exactly when needed. Five picojoules of energy and only around half a volt are enough to create a turn-on signal. This is so little that many sensors can provide this without requiring a power supply.

**Dave Jones:** Sure, it certainly can. power being used from the battery, the system is alive and listening. So, they've made out that you waste a ton of battery capacity just by listening. And, you know, listen doing the sensor thing, reading the sensor,

**Dave Jones:** and just waiting for something to happen. And hey, that's true, but let's look at the practicality of this, shall we? Let's have a look at some low-power microcontrollers that you might typically hook a sensor onto and how long they last. So, in a typical

**Dave Jones:** application for a CR2032 coin cell battery, tiny little thing with a modern low-power micro, using a wireless sensor network application here where it, you know, powers up for a brief period and and does stuff and then goes to sleep

**Dave Jones:** just waiting, sensing, doing the sensing. It's shelf life of the battery, 10 20-year type stuff when it's just, you know, turning on and doing stuff. So, what problem are they actually trying to solve here? Because it's certainly not

**Dave Jones:** your typical sensor application battery life, even with Bluetooth transmitting, you know, every 5 seconds or whatever. You're still going to get a couple of years battery life from a tiny CR2032 coin cell battery. It's just marketing BS. If you think your product or project

**Dave Jones:** might be better if it had no keeper life power drain, then please get in touch. Marketing 101. Just include everything, like this will solve all your problems. Goodness. Demo of a TV that consumes no standby power. Today we want to show you television

**Dave Jones:** that uses absolutely no power in standby. Absolutely no power in standby. We're measuring the power going into the television. And the problem with your normal television is That's all right. when it's sitting like this in standby, it is using on average six double A

**Dave Jones:** batteries per day just to sit there waiting 24/7 to listen to see if you're going to press your remote. You can see our television uses absolutely no power. So, there are zero amps flowing into this television. It's magic.

**Dave Jones:** I'm going to turn it on for you. It's draw zero and then turns on. You can see the power increasing and you can see it starting up. There we go. Woohoo! Too bad it's all smoke and mirrors So, what we're going to do today is

**Dave Jones:** we're going to show this television in public, see if people like it. Hopefully it'll work. And then we're going to bring it back to the lab and we're going to do a teardown, show you what's inside this box, show you how

**Dave Jones:** Teardown. So, in other words, they're going to take it out to the gullible public and with their smoke and mirrors demo, they're going to get the public to react to oh my god, this is fantastic. It's going to save the world. It's got zero

**Dave Jones:** standby power. Yeah, right. Let's go check it out. Well, that uses that uses power. That's still using power when I turn it off. Well, no. No, it's completely off. So, the clever thing is is it's completely off. No power being used.

**Dave Jones:** No power? It still wakes up. It still wakes it up. That guy's going on Let me have a look. Good on you. Dude. Dude. See that box? No, no, no, no. You passed it. See that box down in front of you?

**Dave Jones:** See that wall wart? That's our That's the receiver. Yeah, sorry. No, no, no. Look further back. Look further back. Follow on the cord. So, there's no trickery There's no trickery. The energy from that LED actually actually wakes that up and

**Dave Jones:** wakes the system up. The energy from the LED from the remote control LED wakes it up. It's clever. He likes it. He's sold. So, let's rewind that a little bit and see what's going on here. You'll notice that down here,

**Dave Jones:** there's their little receiver box, which we'll see a teardown of at the end and they'll show us the schematic. And this is a DC powered TV, hence why they have this external plug pack. It's taking the AC in and it's generating 12 V. And

**Dave Jones:** you'll notice that they've got their current meter, their ammeter here in series with the 12 V line. So, yes, they've switched off the 12 V output of the plug pack and of course the TV is drawing nothing cuz

**Dave Jones:** it's not getting that 12 V input. But, these plug packs aren't magic. Where's that 12 volts coming from? The Oompa Loompas in Willy Wonka's chocolate factory? Drawing zero power? Give me a break. So, how much quiescent current do these plug packs take? Well,

**Dave Jones:** I've got one for my monitor here, which runs on a 24 V DC monitor. Please excuse my power meter. It looks like something's happened to the LCD just on the line that we actually need it, but it's 300

**Dave Jones:** mW there. Um, which is, you know, fairly significant, but that's watts. If we switch over to VA here, apparent power, it's 4 VA, right? So, depending on where you live, you don't have to pay for that apparent power. Commercial companies

**Dave Jones:** generally do, but that mean but the system, the energy distribution and generation system still has to be designed to generate that 4 watts just for this little plug pack when it's got no load. And here's another one for my camcorder, 1 and 1/2

**Dave Jones:** VA, 200 mW. This one here's horrible at near 7 watts and 15 VA. You've got to be kidding me. And they know this. They deliberately chose that 12 V DC so that they could eliminate the AC plug pack

**Dave Jones:** from their demo and wow people. Oh, look, isn't it wonderful? So, right there it is complete and utter marketing They're claiming that this TV has zero standby power when there's standby power in the plug pack. The plug pack doesn't magically go to zero power.

**Dave Jones:** And of course, they're not going to tell you about other stuff like other signals in the environment that could potentially turn it on. This guy here is clever. He actually asked about what does it pick up the other infrared and

**Dave Jones:** stuff like that and depending on the sensor, the earthquake sensor or whatever. Like, where do you set the threshold against false triggering that choose more power versus sensitivity and all that sort of stuff. And no, no, it's just

**Dave Jones:** it's going to have a niche application, but try to make it broad application appeal. It's not going to work. I was going to tweet it. Obviously. Let's have a look inside the box. Ta-da! When you press on button.

**Dave Jones:** We have a schematic. So, let's have a look what we've got here and it's exactly what you'd expect. The infrared receivers here, they've got to stack them in series to get extra voltage out of this thing that receives the LED

**Dave Jones:** the energy from the LED in the remote control and that generates at least the 0.65 volts turn on trigger threshold at the input here and then the output shorts down to ground like that cuz it's an open drain output. But of course,

**Dave Jones:** open drain outputs aren't magic. You can't just magically switch the mains with that. You can't just magically switch the 12 volts. So, what they've got here of course is they're going to have a MOSFET here or a solid state

**Dave Jones:** relay, whatever you want to use to switch the 12 volts. And notice that you've got to have a pull-up resistor here. This has to go to a voltage. In this case, it actually goes over to the 12-volt input here and then they've got

**Dave Jones:** their current meter inside here. So, they're actually measuring the current flowing through there like that after the mains plug pack. But you've got this mains plug pack, you've got current quiescent current being consumed in that 12-volt plug pack. They're being

**Dave Jones:** massively deceptive. So, there's a very good reason why they did this on a 12-volt TV and they didn't do it on a 230-volt, 240-volt, or 110-volt mains TV and actually switch the mains input and have true zero standby power is

**Dave Jones:** because it's very difficult to do that. You've got to have the pull-up here in order to enable that. You've got to have a high enough current solid state relays. And if you do get a solid state relay to try and switch the mains, if

**Dave Jones:** you get a SCR based one, of course, these ones actually require a significant amount of input current. Look, 15 milliamps in this kind of case. And sure enough, you can get some MOSFET solid state relays and stuff like that

**Dave Jones:** chin, but they're typically quite low current applications. Like this one's only 60 volts. Like either they're high voltage low current or they're low voltage higher current. And it's not magic. And of course, you're going to have to have this pull-up resistor here.

**Dave Jones:** You've got to have a supply coming from there tapped off and it to power the pull-up to enable your relay. But hey, to be fair, they do recognize this and mention it in the data sheet. So sure, this thing's going to have a bunch of

**Dave Jones:** niche uses. I'm sure it might be you know, it might even be reasonably but as the universal panacea for standby powering TVs and every other consumer product, no. It's not magic. It's an open drain output. They don't work magically. You've got to have that

**Dave Jones:** power to switch it on. And high power devices like TVs, they're another ball game. And if equipment manufacturers want to develop a TV that takes, you know, bugger all standby power, they don't need your chip. They just need to

**Dave Jones:** put you know, some extra effort and some money into actually designing it this way using something like this TI chip, which is designed to have a separate wake up here and actually detect when the TV wakes up or

**Dave Jones:** when the product wakes up and then whoop, switch the power through. And it draws like, you know, tens of five, 10 milliwatts or something in standby. They don't need your energy harvesting whizbang widgety thing. It's just not needed. But hey, you know, that's not

**Dave Jones:** what your investors want to hear, right? Now, just to be fair, their widget is doing something here because the TV itself here is actually going from taking X amount of standby because it will have its own standby power in addition to the

**Dave Jones:** quiescent standby supply of the plug pack here. So, what he's doing something, it's reducing that to zero, but using this as like your prime demo for selling this So, I'm sorry, but your chip is not going to be useful to the

**Dave Jones:** likes of TV manufacturers and other mains powered products like that because that's not where the losses are. They don't need a zero input power five picowatt, you know, harvesting the energy from the infrared light to be of use. The losses are elsewhere in the

**Dave Jones:** power supply and other places. It's really of main application for sort of niche, you know, a small sensor type low power energy harvesting stuff. So, this is a ridiculous demo, and I think you know it. We hope you like our standby free

**Dave Jones:** television. No, I didn't. It was a smoking mirrors, just very deceptive. You should be ashamed. These guys know that what they're doing is, you know, a pretty deceptive. Deliberately chose the 12 V DC so that you could show to people, and

**Dave Jones:** probably investors, and I believe they got government grants and stuff for doing this research and things like that. So, they've got to show the results, and then, of course, the marketing department of Bristol University, or I assume they've got,

**Dave Jones:** well, you know, something like that, takes a marketing spin takes over, and oh, yeah, we can apply this to everything, every single product in the world. Like, no. Okay, you developed a nice little chip. Hats off. I like it.

**Dave Jones:** But, please just stop with the marketing BS. Uh unbelievable. So, anyway, I hope you found that interesting and informative. And whenever you see starts in marketing headlines like that, just stop and think a bit, analyze it, and you'll find yeah, they're usually

**Dave Jones:** exaggerating things. Anyway, catch you next time.
