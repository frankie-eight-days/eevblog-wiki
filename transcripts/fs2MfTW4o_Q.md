---
video_id: fs2MfTW4o_Q
title: EEVblog #38 - LCR Meters, Transmission Lines, and Moving goal posts
url: https://www.youtube.com/watch?v=fs2MfTW4o_Q
source: youtube-asr
timestamps: {"0": 10, "1": 22, "2": 41, "3": 58, "4": 71, "5": 84, "6": 100, "7": 112, "8": 127, "9": 140, "10": 156, "11": 170, "12": 185, "13": 202, "14": 219, "15": 238, "16": 258, "17": 276, "18": 293, "19": 310, "20": 326, "21": 339, "22": 350, "23": 368, "24": 382, "25": 398, "26": 415, "27": 428, "28": 442, "29": 455, "30": 470, "31": 481, "32": 495, "33": 511, "34": 524, "35": 539, "36": 551, "37": 567, "38": 579, "39": 593}
---

**Dave Jones:** I'm going to give you the answer to the hardware puzzle that I proposed a blog or two back. I gave you this board and I said what is it? Try and figure it out. What does it do? And three people

**Dave Jones:** actually came up with essentially the correct answer when you combine their answers together. Trent, Jeff, and Pete uh essentially came up with it. And what it is is um Trent had it spot on. It's a production uh test jig for production

**Dave Jones:** uh seismic sonar cables. And this is a what's called an well, what I called an automated functional tester. And it was designed to be used used in the production environment and also out in the field on the back deck on the back

**Dave Jones:** deck of our seismic survey ships in the middle of the ocean. So, how do you test these things in production? What do you need? Well, basically just because the hydrophone is basically just a capacitor, um what you need is a a

**Dave Jones:** capacitance meter. You need to um also cuz there's just a whole bunch of wiring in them, you need to measure the wire resistance. You need to measure the wire uh inductance sometimes. And because they got twisted pair transmission

**Dave Jones:** lines, you also have to measure the performance of those twisted pair lines. And because uh it's a complex manufacturing process that can get contaminated, you also have to measure the insulation resistance of uh of all the wiring in there. You have to

**Dave Jones:** measure one wire in respect to all the other wires. Jeff was actually spot on when he reverse engineered this top board here and he said it was an LCR meter. And he's right, that's exactly what it is. Well, I called it an

**Dave Jones:** impedance module, but it measures L C and R. Actually, it measures a lot more than that, which we'll talk about. And Pete was also spot-on when he reverse engineered this bottom board here. He says it was a swept uh frequency

**Dave Jones:** uh cable tester, and that's exactly what it is. I call it was a transmission line board. Here it is. Here's the actual test can. Here's the test connector, which plugs into the product under test. This is actually the connector from from

**Dave Jones:** the product itself, and it's just got a serial interface at the back uh which which provides comes from a battery pack and goes to a PC. And you take this off, and it's got There's those headers that uh that go on the board. And the board

**Dave Jones:** what? Slides out of there on these rails. And there it is. There's the other one. There's the slave version of the board. This isn't designed to go um underwater. This is just um so that it's convenient to handle and plug into our

**Dave Jones:** product and and turn the connector and things like that. Let's talk about the LCR meter. There's several ways to design an LCR meter, but the technique I chose for this is the voltage and current measurement technique. Basically, you uh feed a fixed uh

**Dave Jones:** frequency into the device under test, and you measure the voltage and the current and the phases, and from that from those basic measurements, you can calculate everything. And stick with me with it here, but here's the technique behind it and the math as well for those

**Dave Jones:** playing along at home who love their math. Okay? Basically, what it is is you take uh several measurements. This is a standard phasor diagram, okay? And this is the voltage and the current relative to the test waveform at 0° and at 90°. So, you

**Dave Jones:** would take a measurement at 0 and 90 for voltage and current. And the this gives you four values, which we'll call VP, IP, IQ, and VQ. And if you stick those into some formulas, okay, what you get out is in an equivalent circuit of the

**Dave Jones:** series resistance, the RS, and the and the series reactance as well, XS. And with that with just those two values, once you've calculated those, everything else is just a simple calculation. You can do much more than just measure LC and R. You can measure

**Dave Jones:** the quality factor. You can measure the dissipation factor. You can measure the impedance. You can measure the series capacitance, the the the parallel inductance, the series inductance, the parallel capacitance, the equivalent series resistance, which is RS. You can measure the RP, which is the

**Dave Jones:** insulation resistance, basically, and a whole host of things, admittance, impedance, and all sorts of stuff. So, actually, using this voltage and current technique, you can actually get a lot more than just measure LC and R. So, for those who are interested in the actual

**Dave Jones:** block diagram circuitry of the LCR meter, it's basically an XR2206 function gen, which generates a fixed frequency sine wave. There's a There's a driver, and then basically, it goes into three different range resistors. And they're the They're the relays you saw on there.

**Dave Jones:** You can switch in different current ranges, basically. And there's a AD620 differential amp across there. This is to measure the current, okay? So, you'll get I out of here. Whoop. And then it goes into the device under test, the

**Dave Jones:** what's called the DUT. It's a standard industry term. That actually goes through the relay matrix and out through the product 100 m, comes back, and then there's another AD620 differential amp, and that measures the voltage. So, we've got the voltage and current measurement,

**Dave Jones:** and then we've got some zero-cross phase detectors here, which which calculate where the which so the PIC knows where the phase is. And the PIC's got ADCs in it, and it multiplexes them, measures them, and does all those calculations I

**Dave Jones:** mentioned before, and bingo, comes up with an LCR or some other measurement result. Simple. The next module is the transmission line tester, and this is how it works. Basically, you've got a PIC uh controller here, which controls an AD9835 direct digital synthesis chip

**Dave Jones:** running up to 50 MHz. This generates the test uh sine wave at the desired frequency from its steps up to 20 MHz in in various steps. There's a differential driver here, which goes into the device under test. Once again, this is just the

**Dave Jones:** huge relay matrix on the board, goes out of the product 100 m or so, comes back, and then it goes into a differential receiver, which is the EL2142, and this is the AD8131 driver, and then it goes into the AD

**Dave Jones:** 8036 uh clamping amplifier, and this confused a lot of people. It threw them off the track because they thought this is mainly used for video, this clamping amp, but I actually used it as a precision full wave rectifier. So, when

**Dave Jones:** you feed in the sine wave like this, you get out a precision rectified uh sine wave, basically, and then you smooth it out, and you get the peak. So, it's actually a peak detector, and that's fed back to here, so it just

**Dave Jones:** measures the peak voltage that comes out of the DUT, and also does the same thing here for the um stimulus signal. So, the PIC just measures both and calculates the difference, and bingo, that's your attenuation. Simple. Here's the basic

**Dave Jones:** operation of the entire unit. What we have is a Rabbit 2000 uh processor, as you saw, and the reason that was chosen at the time is because it had uh four serial ports on it, so that it could

**Dave Jones:** connect back to the PC via serial port. It could uh and then connect to the LCR meter and the transmission line tester, and the optional uh expansion board up here. So, that's pretty And And it had a fairly, you know, it was fairly grunty,

**Dave Jones:** and it had a nice software development system. So, that's the reason that was chosen. And basically, then you had these plug-in boards, and you had the relay driver chips, those big 40-pin chips. People said they were LED drivers

**Dave Jones:** and things like that. No, they were obviously used to drive all the relays, the 120 odd relays on this thing or something. So, the relay matrix itself is rather interesting. It's got a what's called a high and low bus, which is like

**Dave Jones:** an internal bus, just two wires, and all the relays basically hook into this one bus. Each input line, one through two, well, I think this one had 32 or something, but there was another design which had up to 48 relays.

**Dave Jones:** And basically, you can switch any one of the input signals through to either the high or the low bus. And that's why you had so many relays. And then you could um switch one of the instruments onto the

**Dave Jones:** bus. For those wondering why it's actually a modular design like this, why everything's nicely separated as separate instruments, and there's a separate processor module and all that, and it uses RS-232 to talk to the PC, it's because uh it made development less

**Dave Jones:** risky. Uh I could develop the separate modules, and I could show progress because, you know, there's managers, you know, looking to see progress of this thing. So, I can show them, "Look, yeah, the LCR meter, I've designed that, and

**Dave Jones:** it works." Because it's RS-232 interface, I could test it separately on its own, and and actually show them that it works. Same with the transmission line tester. And uh and that's why it's separate. And for those moving goalposts, just when the design, just

**Dave Jones:** when you think you've finished it, management come along, move the goalpost, and this made it easy to go, "Oh, okay, I'll just design a new uh LCR meter board or a new transmission line board or some other add-on board and it

**Dave Jones:** made it really easy. And the whole idea was actually to fit two of these cans, one at either end, into a suitcase like this with the power supply and the PC and everything that people could just uh take on a plane and take onto the boat

**Dave Jones:** and and actually use it out in the field or use it in some makeshift factory somewhere in Dubai.
