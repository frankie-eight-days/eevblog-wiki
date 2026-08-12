---
video_id: fIEH4-P2nyQ
title: EEVblog 1594 - Inside a Quantum Computer! with Andrea Morello
url: https://www.youtube.com/watch?v=fIEH4-P2nyQ
source: youtube-asr
---

**Dave Jones:** Okay, if anyone can decode what's going on here, Andrea, we'll offer you a job or a position. touch. We'll we'll talk about job opportunities if you can actually decipher what's in there. Let's do it. Hi, I'm here with Andrea Morello, who

**Dave Jones:** you've no doubt seen if a previous video of about quantum computers. We've done a 1 and 1/2 hour We did. It was very comfortable back then in the red velvet lounge in my house, She was lovely. this time is going to be we have to move

**Dave Jones:** a little bit more, but hopefully it's going to be even more exciting because you can see It's actually very lucky. You can see both a uh quantum computer experiment completely open and accessible and a quantum computer experiment all closed up, cold and vacuum and so

**Dave Jones:** on, but functioning so with functioning quantum bits. Right there ready to look at. Awesome. And where are we today? We are in the Fundamental Quantum Technologies Laboratory at the University of New South Wales in Sydney, Australia. Australia for the win. All right, and

**Dave Jones:** you're the head professor here. You're in charge of the group. Yes, yes, I'm the professor of quantum engineering in the School of Electrical Engineering and Telecommunications at UNSW and I'm also one of the key people who have set up the world's first

**Dave Jones:** undergraduate degree in quantum engineering. Fantastic. So we're teaching this this stuff. As I know, well, there's another one in Germany. Yes. And things are popping up in the US, but you know, there's there's a growing consensus that this thing needs to be

**Dave Jones:** addressed because there's a lot of jobs in quantum technology that need to be filled up by qualified people and such qualified people do not grow on trees. Got it. So someone like us need to do something about it. So that's what

**Dave Jones:** So usually it's part of another course. It's usually it's not a dedicated course. It's part of an EE degree, some branch of an EE degree. in the old days people were able to take quantum engineering courses as elective

**Dave Jones:** within an EE degree, or they would come through a physics degree and they would do quantum physics through the physics degree. And then lots of people did physics and EE as a dual degree. So, those people were quite well sorted. And

**Dave Jones:** another really killer degree is, for example, quantum engineering and computer science. Ooh. That, as you'll see in a moment, I mean, as where the money's at. And that's where going to be at. Yeah, yeah, yeah. No, that that's really

**Dave Jones:** killer killer app. Yeah. Got it. So, you're going to show us a real quantum computer, or is this mainly a research rig? What do you think? Well, this is definitely a research rig. Uh look, how can I say this politely? Okay, let

**Dave Jones:** me let me let me just not go out of There there is no truly useful quantum computer in the world. The most advanced, the most useful quantum computers are also still used for basic research, for hardware development, and also though to help

**Dave Jones:** people learn how to program quantum computers. Probably, if you ask me today, what is the most useful application of a quantum computer, is for people to learn how to use them and program them. So, that's kind of where

**Dave Jones:** we're at. In anticipation that the hardware will eventually Exactly. become practical. Exactly. Got it. What we do here is we develop from the ground up, cradle to grave, as I like to say, from the design, the theory, the

**Dave Jones:** nanofabrication, the measurement, the analysis of the data, everything from beginning to end, uh silicon-based quantum computer chips. So, what we have in these uh devices, this one is actually about to be removed. This is a Let me call it a

**Dave Jones:** two-qubit quantum computer. It's a single phosphorus atom and the two cubics are one atom of well, one nucleus of the phosphorus atom and the electron that is bound to that phosphorus atom. That's a two cubic system. In this other

**Dave Jones:** setup, we have an atom of antimony. Antimony is a heavier, bigger atom. It's two rows down from phosphorus in the periodic table. So, it has a bigger nucleus and the nucleus has eight quantum mechanical states. Eight is two to the power three,

**Dave Jones:** that nucleus alone is the equivalent of three cubics. Nice. And then there's the electron makes it four. So, technically, that's a four cubic system. Yep. We've done that. We've covered all this in the previous video, so yep. Awesome.

**Dave Jones:** Here's a look at the hardware. All right, let's look at the hardware. So, if you type quantum computer in a web search, what you will find is something like this. This is not, of course, a quantum computer itself. This

**Dave Jones:** is the refrigerator that cools down the quantum computer chip. The quantum computer chip is actually down there. So, what you see here is a is a copper box which is there to protect uh to shield electromagnetic radiation both

**Dave Jones:** for actual, you know, electromagnetic noise uh reduction, but also to prevent any high frequency photons, which are carriers of energy, from hitting the chip and heating it up. Right? So, the rig itself is called a dilution refrigerator. It's a

**Dave Jones:** refrigerator that uses in fact, it uses quantum quantum physics to reach 0.01° above absolute zero. Wow. That's right. So, maybe we want to take a step back and see how the whole thing sticks together. In the end, this will be a a vacuum

**Dave Jones:** enclosure. You can see the the remaining vacuum cans there at the back, right? They've been just removed. And you can also see those silver-plated shields, right? They're at the white painted. Those are the external vacuum cans. And then the silver-plated

**Dave Jones:** shields, those are radiation shields. So, those are to prevent the warm surfaces on the outside of the refrigerator from radiating hot black body radiation into the inside, which would provide a heat load and make it difficult to cool down the

**Dave Jones:** inside to the temperature we want it to go down to. So, the system works in, let's say, two stages. First, there is what's called a pulse tube cooler, which you can probably hear. This machine is off, but the other one is on. You hear

**Dave Jones:** this That's basically a cycle of compression and expansion of helium gas, which gives a cooling power that allows the plate that you can see if you look from here. So, this plate here can go to about 4° K. So, -269°

**Dave Jones:** C or 4° above absolute zero. So, that is cooled down by let me call it, crudely speaking, the, you know, 10 kW version of the refrigerator you have at home, right? Your fridge at home to keep the food cold also has a little

**Dave Jones:** compressor and a gas, and you hear it going That could turns on periodically. That's right. And this is like the giant version of that using helium gas. The reason it uses helium gas is because helium is the only substance that never

**Dave Jones:** solidifies even at absolute zero temperature. It remains, so it goes liquid at 4.2° K, but it then uh it never solidifies unless you put 30 atmospheres of pressure on that. There's a whole story I could keep you for hours on that, but let's not

**Dave Jones:** let's not get distracted. How do you physically verify it's at that temperature or is it based on the fundamental physics you know it's at that temperature? We have thermometers all the way through and funnily enough those thermometers are just chip resistors.

**Dave Jones:** So a lot of the little surface mount resistors that you use in normal electronics, um they are actually optimized to have a very flat temperature coefficient around room temperature, right? You build an electronic circuit and you want it to be, you know,

**Dave Jones:** temperature stable in case your circuit changes temperature a little bit. And so these um these resistors are made out of some special oxides and they have a temperature coefficient that changes sign. So it the the resistance goes more or less flat around

**Dave Jones:** room temperature, then increases again if you heat them up again, and then increases again if you cool them down. So it's like a it's like a parabola. So if you cool them down to, you know, very low temperatures, you can

**Dave Jones:** take, you know, I just know from memory a 1 and 1/2 kiloohm resistor will go about 20 kiloohm when you are at 0.01° above absolute zero. So there are some absolute calibrations that are done with various melting points. Yeah, yeah,

**Dave Jones:** there's traceability. There's ways to verify that. You calibrate these simple chip thermometers against these other reference thermometers and then you place them at strategic points along the fridge and then you have just a resistance bridge that measures the

**Dave Jones:** resistance. Can we physically see those in here? Yes, they are um here. So they're actually held These are the heaters actually. The thermometers See, they're basically they're just attached to some little copper positive cheap resistors cased into a copper thing and

**Dave Jones:** then attached and then there are these little looms. You see those ribbons? They're basically twisted pairs put it in a loom and then they go all the way up and you connect to this instrument. Let me I'll show you the one

**Dave Jones:** on this rack which is the same. So this thing here is a resistance bridge. It's an AC resistance bridge. So with this thing you can measure the resistance of those little chip thermometers with a power dissipation of order

**Dave Jones:** picowatts. Right? That's important because the cooling power of this refrigerator at the lowest temperature is about 10 microwatts. So you need to make sure that anything else you attach there doesn't start pumping power otherwise it heats up. And so the resistance measurement itself

**Dave Jones:** has to be very very low power in order to in order to be a set up. And then you see That's a copper That's a equalization. That's right.

**Dave Jones:** Exactly. So the the braid is is the loom. So those are the signal wires for the thermometers. But the thing is because they come from room temperature and you know, they are conductive wires. So by the Wiedemann-Franz law, if you

**Dave Jones:** have an electrical conductivity, you also have a thermal conductivity. So you want to make sure and these things are not copper wires. These things are some They're usually um um manganin or constantan. They're some some lousy lousy conductive thing, low

**Dave Jones:** thermal conductivity. That's right. And so at every stage you want to hook them up to a copper post and wrap them around and soak them in uh something called G varnish which is a special kind of It's insulating varnish but it has

**Dave Jones:** some decent thermal conductivity and it's like a good I've used like like a glue. and it thermally anchors the wires at the various temperature stages to make sure there isn't too much heat coming down. And the same is done, as you can kind of

**Dave Jones:** see, uh with the coaxial cables. So, these ones are semi-rigid coaxial cables that are used for the high frequency lines. Yes. And you see they all get broken down at these posts here. And so, there the body of the cable is attached to a to a bulk

**Dave Jones:** bulkhead, and that bulkhead is, you know, gold plated and thermally anchored to the plate, so the cable gets thermalized there. The problem with coaxial cable is that the inner conductor is actually not very well thermally anchored, right? So, that's why you

**Dave Jones:** always give them loops. Because by giving loops, um the Teflon dielectric that's in that's inside will pull when you cool it down. You know, if you've ever tried putting some Teflon cable in a nitrogen vessel, it will shrink a lot. So, this thing

**Dave Jones:** actually pulls, and that that pressure helps a little bit um with thermalizing the cable. And then, uh let me see if I have it here somewhere. Where are we? There should be an attenuator. Uh yes, probably somewhere here. Let me

**Dave Jones:** see what I can see. An attenuator is an RF attenuator. an RF attenuator, that's right. All right. The role of the RF attenuator is to actually thermalize the inner conductor. So, it cuts off some of the high frequency radiation, and it provides a

**Dave Jones:** galvanically conductive path between the inner conductor and the ground, which again, by the same principle, is also a thermal link. So, that the inner conductor gets cooled down a little bit. And then, the other the see the thing

**Dave Jones:** you see here is something we built ourselves, designed and built. It's a filter box. So, this is a box that contains RC filters and LC filters and again serves the job of thermalizing and and filtering away all the high frequency

**Dave Jones:** radiation by the Planck-Einstein relation that the energy is the Planck constant times the frequency of a photon, a high frequency signal carries photons with a lot of energy. So, you want those photons to not be there unless you really need

**Dave Jones:** them. So, everything about doing low temperature experiments is a game of We do need high frequency signals for certain purposes, but where we don't need them, we have to filter them out completely. Got it. Are there any vibrational

**Dave Jones:** problems like triboelectric effects from your tef- from your Teflon coaxials? Oh, yes. I'm glad you asked. I'm glad you asked. We are the world experts on this. Oh, really? Yes, we are. So, um you see these black cables here?

**Dave Jones:** Yes. So, those are um graphite coated. They're black because they're graphite coated. These ones. Yep. They're basically flexible coaxial cables. Mhm. They have um copper-nickel inner conductor, a Teflon dielectric, a coating of graphite, and then a braided copper-nickel outer

**Dave Jones:** conductor, and then very importantly, another Teflon gasket on the outside. So, what happens is this. If you Once you cool down your coaxial cable, the Teflon shrinks, right? Mhm. And so, take a semi-rigid cable like this. Once the Teflon shrink,

**Dave Jones:** the part that's inside the rigid outer conductor can just move around as a result of the vibration caused by that The vibration cryocooler, is that right? Yeah, yeah. And so, we actually analyzed this and we found out that this

**Dave Jones:** is like a noise source with an internal impedance of 100 kiloohm. So, on the high frequency lines, which are 50 ohm impedance matched on all sides, that doesn't matter, right? The voltage resist the voltage division between 50 ohm and 100 kiloohm means

**Dave Jones:** that the signal you get here is basically nothing. But, on the lines that we use to measure the transistor, which is what reads out the quantum bit, the transistor itself is switching between 100 kiloohm and open circuit, and on the other side,

**Dave Jones:** there is a transimpedance amplifier, which some people incorrectly call a current amplifier, but you know what I mean. Yes. We don't, yeah? We're good, right? We know what we're that has a very small input impedance, so that voltage source with 100 kiloohm

**Dave Jones:** input resi- Sorry, internal resistance will put will create a current that goes straight into the input of the transimpedance amplifier. So, we'll see all of that. So, these cables have been designed to kill that problem, and they do so by having, one, the graphite,

**Dave Jones:** which is a solid lubricant, and two, the outer Teflon gasket is like a corset. Ah. It also shrinks, and it keeps it all in. So, we actually we have a whole very detailed paper from a few years ago

**Dave Jones:** where we when we first started using these systems. So, these kind of cryogen-free dilution refrigerators, they're relatively new. In the old days, people used actual liquid helium, like a bath of liquid helium to arrive at 4 Kelvin, and that

**Dave Jones:** means there's no vibrations there. Okay. One of Once we started using these things, that's when a whole hell broke loose, right? So, how do we deal with this? And so, that's why actually we also bought this specific um

**Dave Jones:** vibration isolation setup. This is quite extreme, so you see There it is, Yeah. This is a very solid frame on which rests a very thick aluminum plate on air suspensions. And that's awesome. This is what holds the actual

**Dave Jones:** refrigerator. Then all the components of the pulse tube cooler, the ones that make the noise and vibration, are on a separate frame. Right. Right? Got you. things are decoupled, mechanically decoupled. And then all the pumping lines, there is a pump that circulates

**Dave Jones:** helium gas, they are held on a separate frame that has a 250 kg concrete block, and the lines are cast into the concrete block. Nice. So, if Right? So, if you had to go to another That's the whole thing.

**Dave Jones:** Wow. Funny enough, you can't buy this thing anymore. The company doesn't want to sell it because it's an absolute nightmare to put it together. You have these, you know, half a ton frames, you have to line them up to a millimeter,

**Dave Jones:** right? So, the installation engineers were going absolutely crazy. So, they We were very lucky we managed to get some of those uh models while they were still willing to make them. So, you're not moving labs anytime soon. No.

**Dave Jones:** No. Not these ones, at least. move labs Not these ones, yeah. So, we're running a experiment in there at the moment. And you said that you've got a like I'm here on the lucky day. Yes. Where what experiment are you running?

**Dave Jones:** You're doing groundbreaking research at the moment. Yes, we are. Now, it's uh it's going to be a little bit complicated to show you the actual groundbreaking side of things because it's really quite um it's quite advanced quantum mechanics,

**Dave Jones:** but my student Steve, whom I would like to invite on camera here, he has set up a couple of little scripts to show you how we do the basic um operations on these quantum bits. So, first of all, um

**Dave Jones:** I'd like to dispel this myth, right? People have this idea sometimes of the scientist as, you know, the guy with a white lab coat and the thick glasses there in some dark bunker, you know, handling, you know, little knobs and

**Dave Jones:** stuff. Because there's nothing like that, right? Nowadays, doing an experiment means writing, you know, scripts scripts that control a bunch of instruments, okay? Well, look, you know, there is a there is a there is a part of the job that consists

**Dave Jones:** of, you know, setting up that whole thing, connectorizing, making the device, testing it, connecting all the instrument, you know, making sure everything is calibrated. But once it's all up and running, it's basically run from behind a Python script.

**Dave Jones:** How often do you tweak the set what the physical setup or Uh not often. So, when we find the perfect chip, it may stay in a fridge for a year. Right. There is so much research you can do

**Dave Jones:** research and new science to be done with one prototype chip that it often stays cold for a year. Some have been cold for 4 years. 4 years? Yeah. Wow. Yeah. Wow. Whereas sometimes that fridge, for example, is the one we use for more of a

**Dave Jones:** fast turnaround, so we try something for a couple of weeks and then we just swap chip, but it just depends. Can you cycle them? What happens if you thermally cycle them? Does that cause issues? Can you turn them off or do you

**Dave Jones:** have to leave them They tend to come back. So, if you do a thermal cycle, um what happens is this. These devices are single charge devices, okay? We are We are addressing single electrons and their spins. So, the presence or absence of a single

**Dave Jones:** electron charge within, let's say, 50 nanometers of the charge that we want to look at will slightly change its behavior. So, it just takes one electron to be stuck at a dielectric surface in the vicinity to slightly shift

**Dave Jones:** how this device behaves. But in the end, when we go and look at the spin qubit, the actual object that carries the quantum information, that one is pretty solid. So, the thermal cycle and other electrical, you know, effects will shift a little bit where we

**Dave Jones:** have to go to observe that single electron. But once we have it, it tends to behave the same way because an electron is an electron. We within, you know, there's a subtle case, but yeah. So, maybe I just talk you through this

**Dave Jones:** one. This is a map that was taken just this morning. So, what you see here is in color scale, it says DC voltage. That's the DC voltage that comes out of the amplifier chain, but you can think of this as being the current through the

**Dave Jones:** transistor. Right? So, bright yellow or green means high current. By high, I mean half a nanoamp. Yep. Blue means zero. Dead. And because your sensor is basically a one MOSFET which you guys have modified. So, manufactured. That's right. It's manufactured designed

**Dave Jones:** by us. Uh no, actually no. The electron mobility is not that great. Okay. Yeah, it's is not is not a particular high electron mobility. What makes it special is that instead of being a continuous MOSFET channel, there are two barriers across the

**Dave Jones:** channel that isolate isolate a puddle of about 100 electrons. And then the conduction, instead of being a continuous conduction path between source and drain of the MOSFET, has to go by quantum tunneling through those barrier. So, any electron that

**Dave Jones:** wants to flow through the transistor needs to arrive at the barrier, quantum mechanically tunnel through the barrier into the little parallel of 100 electron, and then tunnel out. But that's based on probability. Yes, but that probability can be

**Dave Jones:** controlled. Ah, that's the secret sauce. Yes, that's the secret sauce. So, that probability can be killed off completely such that there is no current, that's the dark blue you see here, for most situations. And then, as you scan the gate voltage

**Dave Jones:** on the transistor, you will find a situation where basically for an electron to be on that island or not be on that island, there is no energetic difference. So, the electron can be there or not be there, it makes no difference.

**Dave Jones:** And so, that is the only place where you get current because you can get an electron that goes onto the island, and then once it's there, it can escape again. One at a time. And then another electron goes onto the island, stays for a bit,

**Dave Jones:** and escapes again. And by tuning the transparency of those tunnel barriers, we can tune the current we get through. So, we can tune the probability to give us the current that we want. So, this is one of the simple constants

**Dave Jones:** of nature. You know that the electron charge is 1.6 10 to the minus 19 coulomb. What that means is that you have 6.24 * 10 to the 18 electrons per second in 1 amp. Yes. Right? Now, no one remembers that, but

**Dave Jones:** if you're people like us, you do remember that because it means you get 6.24 million electrons per second in a picoamp. Right? So, picoamp of current mean there is 6.24 million electrons per second going through. So, if you want to get a picoamp of

**Dave Jones:** current, we actually want more than that, but just to keep the number simple. If you want a pico amp of current, you need to tune the product quantum mechanical tunneling probability for an electron to come on and off that

**Dave Jones:** island such that there are 6.24 million electrons on average per second that make it through. Got it. Right? So, what you're seeing here, if you just scan this gate along this axis, you see these peaks of current, right? So, every

**Dave Jones:** time you move from here to there, so let's say you go up here, you're going more positive. So, more positive voltage makes it more desirable for an electron, which is a negative charge, to be on that puddle of electrons.

**Dave Jones:** So, every between every peak, you've added an extra electron to the island one by one. You can actually count them. Why are they not uh equally spaced? Consistent, equally spaced. Yeah, because that island is not uh very large. So, if you made a larger

**Dave Jones:** island, they would be perfectly equally spaced. Got it. B- These island is actually small enough that you get a combination of uh classical Coulomb charging energy. So, to to put an electron, a single electron, on a capacitor of capacitance C, you need to

**Dave Jones:** pay an energy e squared over 2c, right? Now, this thing is uh it is a capacitor, right? It's it's a little capacitor plate that has Everything has capacitance. But, in addition, it's also a quantum confinement potential. So, you're getting a bit of a mix of

**Dave Jones:** classical Coulomb charging energy with quantum mechanical level spacing. So, that's why they're not quite completely uniform. There's a lot to unpack in there, but Anyway, the key point I want to draw your attention to is this. Look, for

**Dave Jones:** example, at this point here. This line, you see? Here we've got all these peaks, they all follow each other not quite regularly for the reason we now understand. But then if you move left here, these are two different gates. Like there's

**Dave Jones:** more than one gate around that transistor. There's a few of them. It breaks. The whole pattern breaks and shifts. Right? What's happening there? What's happening there is that as you go left again, the voltage goes positive this way. So as you go more negative on

**Dave Jones:** this voltage, you are making it less desirable for electrons to be there. And at some point, and that point being exactly here, there is one electron somewhere that just pops out of whatever it is and doesn't come back.

**Dave Jones:** So the whole pattern shifts. It goes into the drain. Goes into the drain of the transistor. It just vanishes out. The point is that electron belongs to a single antimony atom that we have implanted into the silicon chip.

**Dave Jones:** So we're putting there an antimony atom. That antimony atom is a group five donor. It's It's an N-type donor, right? When you go to low enough temperature, instead of donating an electron to the conduction band, it holds the electron

**Dave Jones:** there. It behaves like a hydrogen atom. So the nucleus is like a positive charge and the electron is the negative charge that's bound to it. But here is like having an I hydrogen atom in in the middle of some electrodes that

**Dave Jones:** allow you to rip the electron off from that atom. So here, on the right hand side of this break, there is an electron bound to the atom. As you pass to the left hand side of the break, the electron gets popped out

**Dave Jones:** and just vanishes out into the drain. So you dope it with one Yes. Yes, one One that says only one atom in the whole Well, in this particular device, we have about 20 atoms, and you can see there's

**Dave Jones:** more than one of these breaks. All right? So, there's one here, there's one here, there's one here, there's there's a few of them. We actually do have the technology to put one and only one atom. We are right now in the process of

**Dave Jones:** making qubit devices with deterministic single ion implantation. So, that is desirable to have a single It is desirable to scale up. So, for the purpose of early experiments, it's actually quite nice to have more than one because you can kind of find the one

**Dave Jones:** that's in the right spot, you know, that For early experiments, it's actually convenient. Long term, if you want to actually build a deterministic large-scale quantum computer, you want to have one in every spot and nothing else around. else. Yep.

**Dave Jones:** Because it gives you more freedom. Yeah. qubit So, block One in every cell of the array. So, think of the quantum computer as an array of physical qubits like, you know, classical computer chip is an array of transistors that act as, you know,

**Dave Jones:** zero-one switches. So, there you would want to have one at every site. But, for these early sort of prototype devices, it's actually quite convenient to have more than one. But, there's not a lot of them. There's maybe 20 of them in total. This is where the

**Dave Jones:** magic happens, exactly at this corner here. All right. Okay? So, what happens there is that if you were in zero magnetic field, if you set right there at that corner, that electron would have the same preference to be on the atom and be off

**Dave Jones:** the atom. So, you will get the situation that it's actually a random telegraph signal, which many electrical engineers are familiar with. You would have an electron that jumps on and off The electron actually comes on and off that

**Dave Jones:** island of electrons, and then from there it may go away to the drain, but it first got onto the ion. So, it just goes back and forth. It physically goes back and forth? Physically goes back and forth. the probability. We're not

**Dave Jones:** No, no, no. It Well, when you're talking probability, you can actually see it on the screen. We'll see it in a moment. Um you can see when it does so. All right. By the switching of the current in the

**Dave Jones:** transistor. Right? So, when the electron switches on and off, you're basically switching from being in the dark blue. Let's go up here where it's a little brighter. From the dark blue to the green. Right. Right? Which means zero current to

**Dave Jones:** finite current. Now, when does that happen? That's the randomness. And that's why it's called random telegraph signal. It's not a square wave. Right. It's got some randomness in the interval between the switches. it's almost randomly pulse width Yeah.

**Dave Jones:** modulated. Yeah, yeah, yeah. But, there is a there is a time scale, right? So, you have slow random telegraph signal, fast random telegraph signal. So, you can actually show Steve, you want to show? Yeah. Uh I think yeah.

**Dave Jones:** And this is true random. That's true random. No, no, that's true random. That is real random. Yeah. So, what we can do is, okay, we just go to this point and zoom in this point and show a live scan. Okay.

**Dave Jones:** Yeah. Yeah, we can show a live scan right there. Yeah. So, zoom into that area. Okay, so we're just running a Python script at the moment. Yeah. Yeah. So, as you what you can see here, okay, is this line, okay?

**Dave Jones:** And then, okay, you can see the blips, okay? Uh you have the spikes. And this is what Andrew just mentioned. You have the tunneling event of the electron onto the donor of the donor. Right. And this is pretty random where they

**Dave Jones:** happen, right? Also, the duration. Some are a bit longer, some are really short. noticed that. Yeah. So, that's a 2D live scan. This is done reasonably fast. It's just two fast sort of sawtooth waves. Yeah. But, you're doing a research experiment.

**Dave Jones:** Yes. So, this is Let me put it this way. The way we um address and encode quantum information in these spins is by magnetic resonance. Okay? Now, doing magnetic resonance on one spin is actually not harder than doing

**Dave Jones:** it on a quadrillion spins, like what happens to you when you go and take an MRI scan. Yeah, right. So, that technique I'm not saying it's easy, especially when you do it in a refrigerator like this, you know,

**Dave Jones:** there's all sorts of complications, but but the real hard part is to read out a single spin. Right? Right. Once you have read out, once you have a physical access to the to the physical property of the qubit, the rest I'm not

**Dave Jones:** going to say it's easy, but it it's kind of, you know, the floodgates open, right? So, this was this is what we got done in 2010. It was the first spin read out in silicon done right here. Um that really opened the floodgates for

**Dave Jones:** everything we were able to do after that. All right. And you're working on silicon because you think that's going to be the most practical in the future. That's one of the reasons. The other reason is that silicon is a um

**Dave Jones:** semiconductor that is made out of um three natural isotopes, silicon 28, silicon 29, silicon 30. Of which the most abundant is silicon 28 that has zero nuclear spin. So, in where a silicon 29 has a nuclear spin of

**Dave Jones:** 1/2. So, it's actually a slightly magnetic nucleus. Because the quantum information is encoded in the magnetic state of the electron and the nucleus, any other nuclei that carry a spin act as sources of noise. Noise, yes. So, we have access to specially

**Dave Jones:** isotopically purified silicon material where those silicon 29 spins have been almost completely eliminated. So, that gives us a Some people call it a semiconductor vacuum. Ah. Right? These atoms implanted in silicon are really almost the same as being

**Dave Jones:** atoms in vacuum. Despite being in a semiconductor with, you know, gates and nanoelectronics and stuff we can connect to. Do these silicon 29 isotopes, do they cause a problem on regular silicon No. chips? No, it's only for this quantum

**Dave Jones:** Well. Well, well, little curiosity. So, silicon 29 for us is a problem because of its nuclear spin. There has been research, I think, probably about 30 years ago, in the classical semiconductor electronic industry to see whether a purified silicon 28

**Dave Jones:** material without the silicon 29 and the silicon 30 would have better thermal management properties. So, silicon 29 and silicon Silicon 29 not only has a spin, but it also has a different mass. So, if you look at how does heat

**Dave Jones:** propagate through a crystal, um it's I'm oversimplifying here, but it's almost as if as the difference between electricity propagating through a pure metal versus an alloy. Right. Right? So, silicon having three different mass isotopes, the crystal vibrations which carry the

**Dave Jones:** heat are modified and made more complex by the presence of three different mass isotopes. So, it is true that if you have a single isotope silicon crystal, it has a better thermal conductivity. So, in the context of, you know, super

**Dave Jones:** high-density chips, you would imagine, "Oh, that'd be great." It turns out that improvement in thermal conductivity is most significant at low temperatures. I'm going by memory, probably minus 100 Celsius or something like that. At room temperature, it's it's not much.

**Dave Jones:** So, you're talking I'm talking some percent, maybe. Yeah. Like I I Yeah. So, there's no there's no commercial reason to go through the effort of of doing that. But, people looked it up. People actually tried and did experiments

**Dave Jones:** because in principle it does change thermal conductivity. Interesting. of the mass, not because of the spin. We care about the spin. Yeah. And so, when we're reading this information, we put up that live view again. Yeah. Okay. So,

**Dave Jones:** all happening regardless of whether or not you start this script. It's all you're just actually measuring it. Uh no, no, no. So, what's hap- we're always measuring the current. But, what's happening here, the script makes two voltage sweeps on the gate. Yeah.

**Dave Jones:** For example, if I just stop this one, and you can actually see from the pic of scope or this sort of scope. This is what's happening over this board. So, in this case, you don't need to sweep two voltages. Yeah. But, just

**Dave Jones:** okay, sit at the middle point, and then you have the picture there. As I think I was telling you before, if you just sit there, you will see electrons just randomly hopping on and off. Now, this is still

**Dave Jones:** in a place where it's much more often on the atom than it is off. So, it very rarely pops out. But, for the most part, it stays on the atom. So, when you read it out, you've destroyed that information. It's not

**Dave Jones:** Yes. Okay. We haven't actually done read out yet. So, to do the read out, Now, let's see. Do you want to do No, no, no. I'm just I'm just looking at the charge. Well, in a sense, I'm I'm

**Dave Jones:** reading out the charge state. I'm reading out where the charge is. But, there's no useful information That's not my quantum bit. My quantum bit is the spin. So, the spin um is a quantum two-level system. There is a spin down and a spin up

**Dave Jones:** energy level. And we place this thing in the refrigerator at 0.01 Kelvin and in a magnetic field of about 1 Tesla, which is a big magnetic field. The Earth's magnetic field is 50 microtesla to give you a sense.

**Dave Jones:** Uh so, that the energy difference between the spin down and spin up state is more than the thermal energy of anything in its surrounding. Right. Okay? And I don't know if you want to have a look. It's actually over there from the

**Dave Jones:** other setup that's been dismantled. You can see the superconducting magnet that is used to create the magnetic field. Okay. So, that's a big uh It's a solenoid of superconducting wire. It goes superconducting at about uh 10 Kelvin. What's the material makeup of that wire?

**Dave Jones:** This is a niobium uh niobium-titanium. Right. It's a it's an alloy, niobium-titanium. So, it's a big solenoid. It has an inductance of about 10 Henry Mhm. for the electrical engineers among us who know how big that is. It's a very

**Dave Jones:** big inductor. And um it's run by those power supplies there. So, they It takes about with about 100 amps of current, you get about 6 Tesla magnetic field from this magnet. Now, the interesting thing is that because it's a superconductor, you don't

**Dave Jones:** need to keep it powered up all the time. So, you can charge up the inductor to the current that you want, and then there is a superconducting switch that you can use to short circuit the coil, All right.

**Dave Jones:** and then you can turn off the current and that supercurrent will flow on forever. Yes. That's actually what happens at the hospital. When you go to see an MRI machine, you will not see a power supply there. Right.

**Dave Jones:** Someone, the installation engineer, came one day with a rack of power supplies, charged up that magnet, disconnected, and walked away, and went to charge up the next magnet at the next hospital. Got it. Right. And but if they remove the power,

**Dave Jones:** they're screwed. No, if you remove the cooling, if you remove the cooling, you're stuffed. And so, for those of you who are interested, you can go and look for magnet quench on the internet. Magnet quench? Quench, yes. So, magnet quench is what happens when

**Dave Jones:** there is um hot spot along the superconducting wires, such that the wire goes from being superconductor to being a normal resistor. And once you get that, it starts to dissipate, and so, it run it's a runaway process, because it heats, it heats out

**Dave Jones:** the parts of the wire that are next to the hot spot, and that hot spot propagates until the whole wire goes normal. So, you have a 10 Henry inductor charged with, you know, 50 or 100 amp, that is suddenly becoming a normal

**Dave Jones:** resistor. Right. In fact, a fairly like this is not a high conductance wire. Niobium titanium is is an alloy, it's not like copper or gold, you know. And so, there's a huge amount of power dissipation, and it boils off the whole

**Dave Jones:** helium bath in which the magnet is immersed. Right. So, go on the internet, look for magnet NMR magnet quench, and you'll see this thing where the this big puff of cold helium gas blows out, because the whole thing has gone

**Dave Jones:** resistive and blows it up. Got it. That relay that shorts out the superconducting relay that shorts out the coil, Uh-huh. what happens to that if you short it out while it's No, it's actually not a relay, that's the interesting part. All that is

**Dave Jones:** I'm I'm I'm physically thinking No, no, no, yeah, yeah, yeah, no, it's it's a very good Yes, you have a very good question, Dave. It's actually a piece of the exact same superconducting wire put across the inductor. Yeah.

**Dave Jones:** But in normal operation, when you want the switch to be open, you wrap a little resistive wire around that piece of superconducting short to make it go normal. So that thing will be a few ohm resistor, which is in parallel to zero, so nothing

**Dave Jones:** goes through it, right? Whereas if you stop heating it up, then it goes superconducting, so now you have a fully closed zero resistance circuit. Got it. Okay, that makes sense. Yeah, and that's built somewhere in there. There's a little

**Dave Jones:** Yeah. So you will see Yeah, so you see this little thing here? That's the cable that feeds that little heater to turn the switch on and off. Got it. You got some serious ground bonding here. Yes, that's a building ground. It's a

**Dave Jones:** thing Yeah, no, no, no, that's a clean ground. So we want to have all our instruments uh connected to a ground that is separate from all the noisy ground that all the rest of the building runs off. So these are big copper strips that go

**Dave Jones:** to a stake in the ground that's been cast with a special electrically conducting gel and so on. And so all our instruments are on isolation transformer and it's like a star connection to the ground to that clean building ground.

**Dave Jones:** Got it. Just little power hygiene. It is, it is. I mean, of course, this thing is itself a Faraday cage, right? So And then the other thing you've already seen this, you know, we try to shield as well as we can everything.

**Dave Jones:** That's not to say that EMI No, no, you still pick up stuff. These things are so sensitive. You know, you you see things. I'm not I'm not saying that we have complete and utter, you know, EMI protection, but the thing is we also

**Dave Jones:** we need to put signals in, right? So, there are certain experiments where you only have very low frequency signals, and you can people build shielded rooms, like fully shielded rooms, like the whole system is inside a shielded room,

**Dave Jones:** all the cables go through a copper feed-through, and you can do all that. But, we have to run 40 GHz microwave signals into the system. There's all sorts of fast pulses. So, in a sense, the EMI from the environment

**Dave Jones:** is not even the biggest problem given the kind of signals that we pump into the system. So, we try to do the best we can, but, you know, And you have to use the 40 gig odd frequencies due to

**Dave Jones:** uh the value of the Planck constant. Right? So, this is a Yes, absolutely. Yeah, so this is one of my favorite things to uh when I teach my quantum engineering course, you know, I just tell students, there are some

**Dave Jones:** numbers you need to remember like your data birth. One is that one picoamp is 6.24 electrons per second. That's the electron charge. The other one is that 1 Kelvin is 20.84 GHz. Oh, okay. That's the ratio of the Planck constant

**Dave Jones:** to the Boltzmann constant. So, an energy of 1 degree Kelvin corresponds to a photon of frequency 20.84 GHz. And that 1 Tesla is 1.34 Kelvin on a free electron. So, if I put a magnetic field of 1 Tesla

**Dave Jones:** on just a free electron, that energy splitting is 1. 34 Kelvin in energy, and it's 28 GHz in frequency. So, now you know why I need these. So, we normally operate at 1 to 1.4 Tesla. The higher the better. The more

**Dave Jones:** separation you have between the energy levels buying vector microwave sources above 40 gigahertz becomes a very expensive exercise and also the microwave engineering of that is really starting to become to order. You probably couldn't get them off the shelf at that point.

**Dave Jones:** Yes, so it starts to get really challenging. 40 gigahertz is enough. So 40 gigahertz is what? 2 Kelvin in energy? We are at realistically 100 milli-Kelvin, 0.1 Kelvin. So, you know, 40 gigahertz and that corresponds to 1.4 Tesla magnetic field.

**Dave Jones:** So, it's funny how just the ratio of constants of nature gives you the shopping list for what you need to do to run an experiment like this. I don't have that, you know, I don't I don't get to choose.

**Dave Jones:** Those constants of nature are what they are. That's why I need this this beast, right? Yeah. And I think it's important to note that this is not the operating frequency of the quantum process, which is only down in the 1 MHz.

**Dave Jones:** way way slower, yeah. Actually, we might see how fast it goes in a moment. Yes. Okay, let's go back to the We got a little diversion here, but let's get back to Okay, so what we're doing here is this.

**Dave Jones:** We are applying microwave pulses at different frequency. You see the frequency axis here. It goes from 38.6 to 39.2 gigahertz. So, what we do is this. We start with the electron electrochemical potential at a position in that corner where I showed you

**Dave Jones:** before. In a position where only an electron spin down can go on to the atom. Whereas an electron spin up doesn't have any There's not enough energy to populate the spin up level. That's why we go so cold.

**Dave Jones:** If we went warmer, then you would populate both 50/50 probability. That's what the refrigerator is for. At this temperature, we can with almost certainty populate the spin down level, okay? Then, what we do is magnetic resonance. We apply

**Dave Jones:** electromagnetic radiation at the exact frequency corresponding to the energy difference between the spin up and spin down states. And when we hit the right frequency, that electron spin down get excited to the spin up state. Once it does so, it has enough energy to

**Dave Jones:** escape the atom again and give us the blip of current All right. and make the transistor switch. So, what you are seeing here now, this is the scan. Again, you know, bright means high current, blue means low current.

**Dave Jones:** As a function of the frequency, and here we're kind of repeating as we go. So, you see there are some specific frequencies at which you get a bright line. What's happening there is that there is more than one frequency at which that

**Dave Jones:** electron responds. Why is that? Because there's a nucleus attached to it. Ah. So, that nuclear spin, this is in particular, and you'll see it in a moment we populate them all. This is an eight-level nuclear spin. It's antimony

**Dave Jones:** 123. Right. It has a spin 7/2, so it has eight quantum levels. So, it has eight possible orientations. And every orientation of the nuclear spin corresponds to a different effective internal magnetic field that is applied to the electron

**Dave Jones:** that shifts the frequency at which it responds. So, depending on the nuclear spin orientation, we will get a different frequency at which the electron responds. So, you will get you won't get that for the phosphorus one. No, phosphorus get only two.

**Dave Jones:** Ah, two, sorry. Yes, here we get eight. So, that would offer a greater information density. That's right. So, an antimony atom has eight levels instead of two. Eight is 2 to the power three, so it's the equivalent of three cubits in one atom.

**Dave Jones:** So, what Steve is doing here is basically scanning the electron resonance frequency as he flips the nucleus as he goes. So, he can see all the various resonances. They are perfectly even spaced. Yeah, almost per- almost perfectly. Again, for reasons that have to do with

**Dave Jones:** with um They're almost almost perfectly evenly spaced there. Got it. They would be evenly exactly evenly spaced if you went in the limit of infinite external ma- infinite external magnetic field. Got it. Okay. So, if you if you turn the field

**Dave Jones:** lower and lower, you will lose the ability to measure it. But, imagine you could do it, you will see that these things become more unevenly spaced for reasons. Got it. And then they start overlapping overlapping and you can't tell the

**Dave Jones:** difference. Yeah. Well, what happens is that you start to entangle the electron with the nucleus. Ooh. Yeah. Oh, quantum entangled. Quantum entangled. Yeah, yeah, yeah. Okay. know, no, no. Well, we do sometimes, but in this specific case, we want to work

**Dave Jones:** in a regime where, if left in peace, the electron and the nucleus are disentangled. Mhm. So, that the electron acts as a we call it an ancilla. It's an ancilla device to read out the nucleus state. Right. You see, what you're doing here, I mean,

**Dave Jones:** when you think about it, you're actually watching the quantum state of a single nucleus. By seeing at what frequency the electron responds, you know which way this single nucleus of antimony is oriented among eight different possibilities. I just think about it. You know, we we

**Dave Jones:** take it for granted, but you know, think about it for a moment. You you're watching, you know, you're watching a current through a MOSFET, right? And by doing so, you are watching the magnetic orientation of one nucleus. Yes.

**Dave Jones:** And you're getting all this information from the IV curve of a single Not even the IV curve, just for the current. So we we we we set it up at a specific voltage, just the instantaneous current. Because one electron is

**Dave Jones:** is enough to switch the transition on and off. And you can easily measure that cuz it's in the order of seconds. Yes, nano amp. Yes, nano amp. Yes, fine. Off the shelf, yeah. Wow. Okay. No. So the information is destroyed when you

**Dave Jones:** read it out like that. Correct. So all right. So let's let's say Well. Um Let let let me try and put it this way. So let's say I had prepared a quantum superposition of the nucleus being in this state and in that state.

**Dave Jones:** You've set it up that way. I've set it up that way. And then I went to measure at what frequency the electron responds. I will find only one of them. Which means that nucleus, the quantum state of the nucleus has been projected

**Dave Jones:** to the state that corresponds to the frequency at which the electron responded. Right? So given the initial quantum superposition state of the nucleus, there could be two frequencies at which the electron responds. I go and interrogate the electron.

**Dave Jones:** If it gives me a blip at 39.2 GHz, then I know that the nucleus is in the highest spin direction. And so even though before I did the measurement, it was in a superposition of seven half and five half spin

**Dave Jones:** projection, after after I see this blip of current in the transistor, the nucleus is collapsed into that specific orientation. Are you running applications on this quantum computer? No, it's too small. There is no application of any kind at this scale.

**Dave Jones:** At at what scale does it start to become practical? Well, it's a trillion-dollar question. So, um it starts to become practical, depends what application you're looking at. Let Let's say that the earliest applications are probably going to be the ones where

**Dave Jones:** you use a quantum computer to simulate other quantum systems, such as molecules, for example, pharmaceuticals. Right. Right. Yes. So, why can't you design a cancer cure on a computer? Just say, "Oh, you know, this is what the oncologist said I have. I've got

**Dave Jones:** this kind of cancer." Write a Python script that gives me the drug that kills the cancer. You can't do that. Why? Because whatever Even the Imagine that drug exists. Maybe it doesn't, but let's say if it existed, the classical computational complexity

**Dave Jones:** of calculating the behavior of all the nuclei and electron in a reasonably complex molecule is far beyond the capability of even the biggest supercomputer. An interesting factoid, one of the biggest molecules that you can, you know, manageably simulate on a

**Dave Jones:** classical computer is caffeine. Oh, okay. Caffeine is not very big. Look it up. Go and type caffeine molecule structure. It's a fairly simple molecule. And that's because it's a quantum mechanical problem. All those atoms and orbitals and the chemical bonds and how they

**Dave Jones:** interact with other things, such as the cancer cells in a body, is a quantum problem. Right. So, why don't we use a quantum system to understand a quantum problem? That's That's That's the logic of it. So, for that, you'll probably need

**Dave Jones:** I should know this better, but I I'm guessing, okay? Don't call me up on this. Please, don't cancel me online. Um of order some hundred to a thousand very good qubits. Very good qubits. Now difference between a very good and a

**Dave Jones:** crappy qubit? A very good qubit is one that you can run, you know, thousands of operations on without errors along the way. So, what I call a very good qubit is a qubit that can be operated on for thousands

**Dave Jones:** and thousands or possibly more operations without errors. Now, this is very difficult to achieve in the physical world in the practice. So, what people are trying to set up is some redundancy where one bit of quantum information is

**Dave Jones:** encoded not in one, for example, atom but in many of them. And there are some operations and measurement sequences that allow you to both operate and change the quantum information on that encoded qubit, but also detect and correct errors as they

**Dave Jones:** occur. Now, there's an interesting thing about this. The absolute minimum amount of redundancy you need to have to make any kind of quantum error detection and correction is three. Right. Now, how many equivalent qubits do we have in this atom?

**Dave Jones:** Oh, you've got the Three. Right. Right? So, that's why this is really exciting. Okay. There are some very clever colleagues of mine who came up with ideas to encode a what we call a logical qubit, so a qubit

**Dave Jones:** that has enough redundancy to detect and correct errors in a single nucleus. Instead of having to piece together different physical qubits that are spread out across the chip. And you couldn't do that in the phosphorus one. No, there's not enough There's only one

**Dave Jones:** qubit there. There's not enough not enough space. Yeah. to do the same operation as you would with a single qubit. Here we we done antimony we can do it in a single nucleus. Right. But is that going to be more complex to

**Dave Jones:** manufacture? No? No, you just change the mass selector in the ion implanter. Oh, okay. This is exactly the same as a phosphorus device. If you look at them from the outside, they are indistinguishable. So why is anyone working on phosphorus

**Dave Jones:** anymore? Well, um look, it's it's easier at the beginning to do the early experiments. Right. Uh I mean, I have to say we are basically the only group that's doing this, right? So this these experiments are very hard, especially the

**Dave Jones:** fabrication is very very very hard. What we have here at UNSW is really an amazing nanofabrication facility, which is actually part of the national collaborative research infrastructure set up, you know, by the Australian government very very cleverly. It's called the Australian

**Dave Jones:** National Fabrication Facility. So it's actually it's it's a it's um accessible user accessible fabrication facility, but here at UNSW there has been more than 20 years of really focused um investment in getting the specific tools you need to get silicon nanoscale

**Dave Jones:** quantum devices done properly. And this stuff is not easy, it's not cheap. There has to be really a critical mass of people who want to do it, but we have it here. So that's why we're able to make these devices. You can't just wake

**Dave Jones:** up one morning and say, "Oh, let me do this thing." That's right. Okay. But with the phosphorus one it's easier, you can uh smaller groups can muck around The device is actually the same. All right. It's actually the same.

**Dave Jones:** So even making the phosphorus one is hard Right. from a nanofabrication point of view. It's exactly the same. Moving to antimony, the microwave engineering of it, the the in fact the RF engineering of it becomes more complicated, but even that has been made easier in

**Dave Jones:** more recent time by the progress of FPGA waveform generators. We know I don't think we're going to be able to show you this. It gets really complicated. But basically to control this eight-level nuclear spin, you need to have seven radio frequency

**Dave Jones:** uh signals, right? There are seven differences in energy between the eight states. So, you need seven You need a Basically, you need an RF generator that makes seven signals at different frequency. And each one of them completely phase coherent. So, I need to

**Dave Jones:** be able to make a pulse at frequency one, then a pulse at frequency two, then a pulse at frequency three, and then come back to frequency one and be in a perfect phase relation with the first pulse I did a millisecond ago.

**Dave Jones:** That is actually not that simple. But it is becoming possible now with the latest generation FPGA waveform generators. Close. Yeah. Very. So, 10 years ago, it would have been a real pain. Right. Now, you can buy a commercial machine.

**Dave Jones:** It's not It's not off-the-shelf. It's a It's a It's a startup that makes machines just for quantum control. You can buy it and it's already The FPGAs programmed. There are some you know uh code instructions you can use and you

**Dave Jones:** can make all these multi-frequency signals all phase coherent with each other and you can operate this whole large multi-dimensional quantum system like that. Okay, so what Steve is going to show us now is the rotation of a single electron spin.

**Dave Jones:** So, we started in the spin down state and then we apply a burst of microwaves at uh what is it? 39 GHz. And the electron the probability of finding the electron in the up state will oscillate. Remember, it's always a

**Dave Jones:** probability. Yes. Okay? So, we start down. That we can do deterministically. But then we start to make a superposition of down and up that has a heavier and heavier weight of up. Oh. Until it goes all the way up.

**Dave Jones:** Okay. So, it comes back down. It's weighted. Yeah, it's a There are It's a weighted probability. Yeah. Okay. So, this is done by applying a burst of microwaves at approximately 39 GHz and changing the duration of that microwave burst. The longer you

**Dave Jones:** leave it on, the more the electron rotates. So, you can see it going all the way from down to up and back. What sort of period are we talking about? So, we are talking 8 microseconds. 8 microseconds. Yeah. So, this is for a full rotation.

**Dave Jones:** Yeah. And so, what Steve is doing here is just repeating the experiment multiple times. You can see all the traces. And remember, so this is on the vertical scale. I don't know if you can see it on your camera.

**Dave Jones:** It's It says up proportion, which means how many times you get a spin up. Our measurement is binary, classical. We only get a zero or a one. We get zero current or high current. There's nothing in between. So,

**Dave Jones:** how do you know if a spin is pointing halfway between up and down? You repeat the experiment 30 times, and if you get 15 times down and 15 times up, that tells you it was in a superposition of 50/50 superposition of

**Dave Jones:** being up and down. That's effectively what you have to do. Are you controlling the period of that? What How are you controlling that? With the power. So, if you crank up the amplitude of the microwave drive, this thing will oscillate faster.

**Dave Jones:** Got it. Yeah. Right. And that relates to the kind of the effective quantum processing time of a quantum computer. It kind of does, that's right. So, for example, if you want to do to do a not gate Yes.

**Dave Jones:** on the bit, that will take 4 microsecond. Got it. And this so, the clock this will be you can call it a 100 kHz clock speed. But, the advantage eventually will be the parallelness of it. Is the is the complexity. So, you will

**Dave Jones:** use a different algorithm to arrive at the result. And that algorithm will have a much smaller number of steps. So, even though every step individually may be slower because we're running a 100 kHz clock instead of a 2 GHz clock,

**Dave Jones:** if there is an exponentially smaller number of steps to arrive at the results, we'll still get there sooner. Uh then we can do the check nuclear spin. Yeah, so Steve has written a couple of scripts that are already demonstration

**Dave Jones:** demonstration ready. Uh yes, ESR is that equivalent series resistance? No, electron spin resonance. Electron spin resonance. Okay, so you see, this was blue for several shots, and then it switched to orange. Right? So, that's ESR 1 and ESR 2. What

**Dave Jones:** it means is that he was checking all the eight possible frequency at which the electron responds. And for some times it was always this one. Then it switched to this one. And then it switched back back to the blue one. What it means is that

**Dave Jones:** the nuclear spin has switched between two states. I'm amazed that you can do this with just like a current pulse. And and the basic signal is what you see here on the oscilloscope screen. It's just the spikes of current.

**Dave Jones:** That's nuts. Because you know what frequency and timing you're exciting it at, and it doesn't have to be that quick. In the fact it needs to be at the 40 GHz or the 28 GHz due to the fundamental

**Dave Jones:** uh constants, but you're controlling that. Yes, let me go back to something we discussed before, which is why silicon. Right? I told you we can get silicon 28 enriched material that removes the silicon 29 spins that give you noise.

**Dave Jones:** Now, if if I was doing this the same experiment on a natural silicon chip like the ones you have in every phone, this wouldn't work. Because the spin would lose its quantum state quicker than I can address it.

**Dave Jones:** Got it. So, the reason I can take my time and have that clock speed of 100 kHz, so do that rotation in a couple of microseconds, is because that spin knows its quantum state and remains its its precession is

**Dave Jones:** coherent, so the phase of the precession, the frequency at which it processes constant over time scales of hundreds of microseconds. If I did that in natural silicon, it would be in the nanosecond range. Oh, okay. So, it's In theory possible.

**Dave Jones:** It's possible, but very hard, very hard. We made here the very first quantum beating silicon in 2012, and that was in natural silicon, and that was a hero experiment. We had to put a lot of power down to do the things really fast, and

**Dave Jones:** you could barely see the oscillation. Once we move to the isotopically purified silicon, it's paradise. And how does that relate to the magnetic field strength? Uh it It doesn't. It doesn't. The magnetic field strength only tells you at what frequency needs

**Dave Jones:** to be the signal that flips the spin. But you were asking me before about is this a high electron mobility transistor? Many of them are made in 3-5 semiconductor like gallium arsenide, right? People have made spin qubits in gallium

**Dave Jones:** arsenide, but again, they suffered the same problem, in fact, even worse. Gallium arsenide has only isotopes with a spin. Both gallium and arsenic have a nuclear spin. So, in that material, even though from a charge point of view, from an electrical

**Dave Jones:** conduction point of view, it's super clean, you can get this super high mobility transistor from a electrical point of view, from a spin point of view, they're very noisy and very hard to operate. So, we don't we much prefer having a

**Dave Jones:** silicon MOSFET where the mobility is not that great, but the spin properties are fantastic, rather than the other way around. And so again, just just I want to, you know, especially your viewers to sink in what's going on here. You're

**Dave Jones:** just watching. And this thing is literally just counting how many blips we have here, right? This is a counter, renormalized between zero and one. When you see the thing switching, you are seeing a single antimony nucleus spin switching direction.

**Dave Jones:** That's happening live before your eyes. And that's just by counting how many blips you can do. And the other seven or whatever you've got in there? They're all low. You We actually check all of them, you see? Oh, okay.

**Dave Jones:** We're checking all all eight of them. No, I see. I see. Of course. And that's important. There's only ever one of them that's high. Right? You can only ever see it in one quantum state. All the other ones are low, one of them

**Dave Jones:** is high. Got it. Right? Interesting. So, you'll never see two. You want to show the nuclear Rabi? Okay, so now we're doing the same thing we did with the electron before, so to make the electron rotate, now we do it on the

**Dave Jones:** nucleus. Now, here, this is done at a much lower frequency. The nuclear spin has a much smaller gyromagnetic ratio. The gyromagnetic ratio is the frequency at which the spin precesses in a certain magnetic field. So, for an electron spin, that's 28 GHz

**Dave Jones:** per Tesla. One Tesla magnetic field gives 28 GHz. For a nuclear spin, well, it depends on the spin. In fact, every nucleus has a different gyromagnetic ratio, and that's what people use in chemistry to do chemical analysis with nuclear

**Dave Jones:** magnetic resonance. Oh, right. Right? They can tell what's in a molecule by looking at what frequency the spin responds. never looked into it. That makes Yeah, that's a good Every spin has a different gyromagnetic ratio. Antimony has a 5.55

**Dave Jones:** megahertz per Tesla gyromagnetic ratio. So, here it will be running at what? 7 and 1/2 megahertz, more or less? 5.5 Yeah, 5.5. 5.5, sorry. There's a 5.5 timer Yeah, yeah, yeah, yeah, yeah, yeah, that's right. So, let's see. This will take a little

**Dave Jones:** bit longer to run. So, the nuclear spin has an even slower clock speed than the electron for the same reason. Now, what sets that clock speed? Is the So, when we apply that radio frequency or microwave signal to the spin,

**Dave Jones:** we're creating an oscillating magnetic field. The amplitude of that oscillating magnetic field sets the time scale over which the spin gets rotated from up to down. So, if I apply a 1 microtesla oscillating magnetic field at the 39

**Dave Jones:** gigahertz frequency to the electron, yeah, yeah. Right. Uh it's an AM amplitude modulation, yeah, yeah, yeah. Um so, if I apply a microtesla, it will give me a 28 kilohertz Oh. rate at which the electron goes up and

**Dave Jones:** down. So, by seeing that that was at uh was about yeah, 200 kilohertz, it means we were running something less than 10 microtesla oscillating magnetic field at 39 gigahertz. Wow. Right? Okay, got it. Now, with the nuclear spin, because the

**Dave Jones:** gyromagnetic ratio is more than a thousand times smaller, it actually goes much slower. Now, it doesn't go a thousand times slower because being at megahertz instead of 40 gigahertz, we have much less losses along the coaxial line. So, we're

**Dave Jones:** actually able to put a lot more power down. So, it goes about maybe a hundred times slower or so. That's right. Yeah, so this What? excitation signal to flip the nucleus is slow enough you can see it on on a

**Dave Jones:** simple oscilloscope. Why is it multi-level? There it was like a trinary level. Um oh, because what you're seeing, so in the process of doing this experiment, he's not only staying at what we call the readout position, but is also moving the gates

**Dave Jones:** to a different place. And there the current has a different value. Okay. So, basically, what what you want to do here is you want to remove the electron altogether and have the nucleus just there by itself. And as you move around, you see most of

**Dave Jones:** the time it's two levels, but as you move around, you may hit a spot where the current is on halfway through. But you're not doing any readout at that point. Take a video of the bug. Yeah. I think there's a bug in the Probably

**Dave Jones:** the bug in the code. Welcome to Welcome to real experimentation. There's a bug in the Python code.

**Dave Jones:** It happens to the best of us. It happens to the best things. So, this setup here is quite unique. It contains something that we have developed. Um so, we can run two different experiments in the same fridge. Now, remember, to operate a spin quantum

**Dave Jones:** bit, you need a strong magnetic field of about one Tesla, right? So, the device that's down here, you see there is this finger that sticks down and that's such that when you put the solenoid out there, the solenoid is

**Dave Jones:** here, the center of the field is exactly where the device is. right. It's got to be right in right in the center. But actually the coldest point of the fridge is this entire plate here, right? So this is the coldest point and this is

**Dave Jones:** thermally attached to that. Now in here we have a second device where the magnetic field is created by an array of permanent magnets. So we took this uh this is a standard design. It's not invented by us. It's

**Dave Jones:** called the Halbach array. It's basically an array of permanent magnets that makes a very strong and quite uniform magnetic field in the air gap. And then we augmented that with a piece of a soft magnetic material called Supermendur.

**Dave Jones:** It's a soft magnetic material, but it has a 2.4 Tesla saturation um flux density. And so with that array, you can get up to about 1.2 Tesla in a probably 6 8 mm air gap, which is enough for us to put our little silicon chip

**Dave Jones:** and all the bond wires and everything, right? So we can actually run two completely independent experiments, one in the magnetic field created by the solenoid and one in there. Nice. Nice. The other nice thing about this is that

**Dave Jones:** it's incredibly stable. It's actually more stable than the magnetic field of the superconducting magnet. Remember what I said before is that you have this super current that flows with zero resistance forever. Like everything in this world, it's not

**Dave Jones:** exactly true. There is a very slow decay of that. So that magnet, which is a state of the art magnet with a state of the art superconducting um short um it drifts about 40 parts per billion per hour.

**Dave Jones:** Mhm, so very slow decrease. But the quality of our qubits is so good that we actually see it. It's okay. In fact, we are the ones who told the manufacturer how much the drift is. They wouldn't know how to measure it

**Dave Jones:** otherwise. But because our qubits are so stable, we measured it for them. Right? So that's really important for us. This permanent magnet array is actually better than that. It's less than 10 parts per billion. It's great. It's nice

**Dave Jones:** and compact, you know, it's like a very old-fashioned thing to say. It's like big as a pack of cigarettes. Nobody smokes anymore, but you know, that's what it is. And this actually, you can see it's it's even a tunable device. So you see that

**Dave Jones:** there's all the brass box. Do you see this sort of silver colored part here that I'm pointing to? That's the super magnet. You can adjust it. There's a screw there, so you can adjust the air gap. And of course, you

**Dave Jones:** can't do it in situ. You have to do it before you close off, but if you will, you can tune it between .6 and 1.2 Tesla more or less with a reasonable air gap. And so on this fridge, we can fit one of

**Dave Jones:** them, but there are even bigger fridges where the plate is this big. You could put three or four of them. It's completely independent with their own magnetic field and just run the the experiment as as independent parts. Uh there's more

**Dave Jones:** stuff if you like. So we've done the We've got the nuclear control. Remember that little sinusoid that I showed to you before where we were turning the electron from down to up and so on? Here we've done the same, but on the nucleus.

**Dave Jones:** Not from down to up, but just between a pair of states. And you can see it makes another beautiful sinusoid. How How long does it last? This is about half a millisecond. So 500 microseconds for a So it's about, yeah, 100 times

**Dave Jones:** slower than it was before because of the gyromagnetic ratio of the nucleus spin. But, look at the perfection of the sinusoid and how it goes between 0 and 1. The one you saw before didn't go between 0 and 1. We had a little bit of readout

**Dave Jones:** imperfection. This one is almost perfect because the nucleus spin can be read out repetitively. So, we can in Remember how we read the nucleus spin? We interrogate the electron. We ask the electron, "At what frequency do you respond?"

**Dave Jones:** And we can do it multiple times. We can keep asking and build up statistics so that we reduce the errors even more. And you can do error correction at that higher level as well. You don't necessarily have to do it at the quantum

**Dave Jones:** level, is that? So, the error correction involves classical decoding, so to speak. So, you Remember a quantum measurement always gives out a classical bit of information. So, even quantum error correction relies upon cleverly extracting a classical bit of

**Dave Jones:** information from the system and from that result inferring whether you need to do something about your qubit or not, In fact, that's another interesting aspect of useful large-scale quantum computers. They will certainly need to be coupled to some very powerful

**Dave Jones:** classical computers for that purpose, to analyzing real time those quantum error detection signals and apply the correction straight away. So, a quantum computer is not possible without a classical computer. Absolutely not. And And a good one. And a good one. And a good one, too. Yes.

**Dave Jones:** Yes. So, even the IBM ones doing that? All of them. All of them. All of them. Every quantum computer needs to be embedded within a very very very good classical computer. Interesting. So, this is a more old school kind of

**Dave Jones:** refrigerator that uses actual liquid helium to reach low temperatures. So, we have here a vessel that contains 250 L of liquid helium. Helium boils at 4.2° K, which is -269° C. And so, if you fill up this other tank

**Dave Jones:** with some of that liquid helium, you will have in here a whole, you know, bath that is at 4.2° K, -269° C. And then, you can put a stick in there, dunk it in there with your device attached to it, and do some experiments

**Dave Jones:** on that. Now, this is actually it's called a variable temperature insert because it goes to 4.2° K, but it also has a fairly big pump that can pump on a little pot of that helium, so that it goes to

**Dave Jones:** 1.5 K. Kelvin. If you pump on a gas, you reduce the vapor pressure, you reduce the the temperature at which it boils. So, if you follow me here, there should be Yeah. So, this is the insert that goes in

**Dave Jones:** there. So, you remember what you the chip that you saw down at the bottom of the tail in the fridge? The same thing can go in here, so you attach it here. And then, this old stick gets dunked

**Dave Jones:** into that bucket of liquid helium. And then, you can actually pump it to go to 1.5 K, and you can get to 1.5 K in maybe 20 minutes. Okay. Whereas, that guy takes 2 days to cool down. Got it.

**Dave Jones:** All right. Yes. So, here is where we do fast turn around experiments. You want to check something quickly, 20 minutes, you're cold enough to start see things. That single electron transistor will show you that conductance peaks, so you can see that

**Dave Jones:** sort of stuff. Okay. So, if you're experimenting with a new material and you want to Yeah, stuff want to take some statistics, you know, try 10 of them, you know. This one goes to 0.3 Kelvin, 300 milliKelvin, and it uses helium 3.

**Dave Jones:** So, in this little bowl here there are 4 and 1/2 L of gas of helium 3, which is the light isotope of helium that misses one neutron, and it has a lower boiling point and a lower vapor pressure.

**Dave Jones:** And this doesn't use an actual mechanical pump, it uses a sorption pump. So, this thing here, this little pot, is full of activated charcoal. Charcoal has a very high surface area, it's very porous. And when you cool down

**Dave Jones:** something very porous with a very large surface, it tends to absorb uh atoms. So, the way you run this is that you put it in the in the pot where it goes to 1 and 1/2 Kelvin. You close this thing, this is a vacuum

**Dave Jones:** can. So, you close the vacuum there and you pump it, so it's vacuum. This can go colder than the external temperature. And while you cool it down, you apply a little bit of heat to this thing here, so it's about a 50 Kelvin.

**Dave Jones:** Then you stop heating. This thing cools down, and as it cools down, it upso- it sucks up the helium 3 that's in the pot at the bottom. And it pumps on it and it goes to 0.3 Kelvin, and it

**Dave Jones:** stays there for about 2 days until the whole thing has run out. And then you have to restart the cycle. It takes 20 minutes to restart the cycle, and then you got 2 days of 0.3 Kelvin without any mechanical vibration, it

**Dave Jones:** just stays like that. You could also use that, the physics department would use this for experiments on material and other stuff. Yeah, yeah, yeah, yeah, yeah. This is used for Yeah. No, no, they do, they do. They they have things like this. This

**Dave Jones:** one is custom-made to be bigger, so as As seen on the big fridge, we have fairly large chips because of the high frequency lines and the PCBs that we need and so on. And so I asked this company in the UK to build me a setup

**Dave Jones:** that was of the same size so I can accommodate the same boards. I don't want to have to be limited by space here when I then have all the space in the final experiment. And then I can show

**Dave Jones:** you the pumping room if you like. Yes, pumping room, let's go. So the whole refrigerate it's at the back. So the whole refrigeration system relies upon a circulation of helium three gas at very high flow. So there are some big pumps.

**Dave Jones:** And for, you know, comfort and and noise and also interference, we put all the pumps in a back corridor. Oh, here we go. So here is where Oh. the no magic happens. This is where the noise happens. Noise happens, okay.

**Dave Jones:** So this is an old school Roots pump that is used to pump on the liquid helium bath to get to 1 and 1/2 Kelvin. It's an old Roots blower working in in reverse. And over here are the pumping systems of the dilution

**Dave Jones:** fridges. These ones These are a pair of turbo pumps. These are high flow turbo pumps. They circulate the helium three to the big fridge. These ones. Yeah. And then they're backed by a scroll pump down there at the bottom.

**Dave Jones:** That one. Oh, yes. Yeah. And so the helium three gas goes through this pumping system, then it goes through a bucket of liquid nitrogen. Mhm. That's just sort of for for safety. If there is any tiny air leak across the

**Dave Jones:** circuit, the air gets frozen into this liquid nitrogen bucket and doesn't go and clog the system in the fridge. Right. And here are the tanks with the mixture of helium three and helium four. So this is the actual gas that gets

**Dave Jones:** circulated, gets liquefied and dumped into the into the fridge and then just the helium three circulates around. Then when we extract all the gas out, when we warm up the system, it goes into this tank. So, do you make these in the house or do

**Dave Jones:** you buy them in No, this is commercially bought. No, it's These you can buy. Yeah. Companies that specialize in these things. It used to be an artisan thing. When I started as a student, I actually didn't build it myself, but I modified

**Dave Jones:** one that was built by the student before me. So, until, you know, 30, 40 years ago, it was the thing would be the artisan project. Nowadays, there is so much demand for these things because of quantum computing. There are companies that just build it

**Dave Jones:** commercially. Oh, this is the compressor. This is the helium compressor, the thing that does the Yeah, so this is the equivalent of the little motor you have in your fridge at home. Except instead of being this big, it's this big.

**Dave Jones:** It gives you a sense of the Yep. the And this is the chilled water. So, this compressor heats up a lot, so you need to keep it cold with a flow of chilled water. And these are more of the same?

**Dave Jones:** Yeah, that's all the same. Yeah. Okay, simple, right? Okay. replicated. Yes, you're not moving labs anytime soon, that's for sure. Look, sometimes you do it, you know? Sometimes you got to do it. It's These things are on wheels, you know? It's

**Dave Jones:** it's Those ones are hard to move because of the vibration isolation. That makes it really hard. But if you saw the normal one without the vibration isolation, it's actually not too bad. Is it years of refinement to get these

**Dave Jones:** systems reliable, doing what you want, doing precisely what you want? things are commercial now. They work, you know, turnkey. Pretty much. Yeah. All right. In the old days, it was a bit more fidgety, but No, this By now, this is a

**Dave Jones:** established technology, you know? There's still There's still progress. People keep improving little bits and pieces, but the basic technology is is is settled. Okay, so this is the fabrication facility where the silicon quantum chips are fabricated. It's actually only one

**Dave Jones:** part of it. There are other ones, but they're not as easy to see. This one is nicely behind big windows, so I can actually show you inside. So, here we have This is a semi-clean area. I'll show you in a moment the

**Dave Jones:** cleaner area. Here we have some metal deposition systems and various analyses and bonders and microscopes. So, this is where we deposit either dielectrics or metals on top of the chip. And the deposition is normally done after there has been a lithography step.

**Dave Jones:** So, the the typical way in which we would make, let's say, the metallic gates for a nanoscale transistor is by a combination of electron beam lithography, metal evaporation, and lift-off. So, you start from the bare silicon chip, put it on a spinner that spins at

**Dave Jones:** 5,000-7,000 rpm, depending on the details of what you want to do. You put a drop of a resist. We normally use PMMA, polymethyl methacrylate, which is like liquid glass. And then, we put the chip in an electron beam lithography machine, which is

**Dave Jones:** actually over there, so I can show you if you like. So, that's the machine over there. You see a rate 150 direct right. So, that's an electron beam lithography writer. Essentially, what it is, it's a very tightly focused beam of electrons.

**Dave Jones:** Imagine an old cathode ray tube television, but, you know, the $2 million version of that, where the beam has a spot size of 2 nanometers. And you can raster it and scan it across the chip. So, where the electron beam

**Dave Jones:** hits the resist, the resist gets microscopically modified by the electron beam, such that if you then take the chip out and put it in what's called a developer. It's basically a solvent that can dissolve the uh the area that's been exposed to

**Dave Jones:** the electron. You can then remove the the the resist where it's been exposed by the beam. So, you can literally write patterns on the chip with an electron beam, right? So, you just make a CAD file and you write

**Dave Jones:** that pattern. You develop the resist, so you get no resist, so you got a bare silicon or whatever is on top of the silicon exposed. Then you go to the other side where we have the metal evaporators. So, you can

**Dave Jones:** put the chip upside down in, for example, an aluminum evaporator. You evaporate aluminum, so the aluminum coats the whole chip. But where the resist has been removed, it goes straight onto the silicon, whereas everywhere else it goes on top

**Dave Jones:** of the resist that is still there. And then you take it to another kind of solvent that will dissolve all the resist that's left there, so all the aluminum that's on top of the resist floats up, gets lifted off, and you only are left

**Dave Jones:** with the metal that is sticking directly to the silicon. So, that's how you can make those tiny gate structures. So, there's no traditional mask stuff. There is for the larger features. What's the larger features? That's right. So, that is

**Dave Jones:** uh we have a mask aligner. It's actually not here, it's in another room, but so you we still do optical lithography for the micron size features. Uh for the nanometer size features, we need electron beam lithography. Of course, in the semiconductor industry,

**Dave Jones:** people have UV lithography, extreme UV lithography, but we don't have access to that. That's billion-dollars-of-stuff, so. So, you're talking small-scale stuff here, like research This is a research. This is a research information. at all. You couldn't manufacture If we

**Dave Jones:** even came Somebody came to you and said, "Can you commercially manufacture any sort of silicon?" You wouldn't really do it. Well, it depends what you want. So, this is a prototyping facility, really. I mean, it's commercial. I shouldn't speak out of line. It may be

**Dave Jones:** It's It's a facility that can be accessed by users other than members of the university, right? So, there are companies that come here to do uh prototypes and testing. To the best of my knowledge, but I may be wrong. I don't think there's any

**Dave Jones:** commercial company that produces things in here. I'd be surprised. What this place gives you is the flexibility to try a lot of different things, right? And there's a difference between the kind of research I do as an academic

**Dave Jones:** versus the manufacturing of a quantum computer, right? These facilities are great for me because I can do whatever I want. I can change the process. I can tweak it. The reason why you have, you know, 10 billion transistors on a silicon chip

**Dave Jones:** made reliably is because that process is so rigid. Yes. Right? It's so well specified and so rigid. You can't just say, "Oh, let's try something else today." No, right? Right. So, it is just different different demands and different needs in

**Dave Jones:** terms of what you want to do. Is there another research chip manufacturing facility in Australia like this or is this Oh, there's many of them. Oh, right. So, well, so this is called the Australian National Fabrication Facilities. It has nodes in most states

**Dave Jones:** in Australia with many universities. Um the thing that's special here is that because of the 25 years of history of developing silicon quantum devices, we just happened to have a Not happened. We have deliberately accumulated a set of tools that are specifically

**Dave Jones:** chosen for the manufacture of silicon devices. Right. So, there will be other nodes in Melbourne, in Brisbane, in Adelaide, and in Perth that have all sorts of tools similar to these, but they may not have the silicon specific tools that we have. They may

**Dave Jones:** have other things that are specific to some other things they're interested in, right? But, this is financially attached to the University of New South Wales, or it's not? Or are they just using the It It's blended. So, of course, the

**Dave Jones:** space is within the University of New South Wales, but the infrastructure is part It's a national infrastructure, called the Australian National Fabrication Facility. The university gives some in-kind contributions, and there's a whole complicated budgetary way in which this thing is run, but it's

**Dave Jones:** not a university facility as such. So, it's a basically Australian taxpayer-funded facility, really. End user. So, users pay for access to the facility, but there is a subsidy to make it accessible to academics to do the research, you know, without having

**Dave Jones:** exorbitant costs. So, the um those vents on the top, so they're That's laminar air flows. So, if you want to see what happens here, when you enter this especially clean part of the clean room, so there's the mat there, of

**Dave Jones:** course, for the for the dust on your feet. Well, you'll have overshoes, of course. You go in there, you get an air shower. Oh, yeah. Oh, yes, I can see the jets. See that jets? Air shower. Yep. Then you go inside, and once you are

**Dave Jones:** inside, you can see from here there are these grills at the bottom and grills at the top. There is a laminar flow of air that makes sure that whatever speck of dust may come off you actually gets sucked

**Dave Jones:** down instead of It would never go outwards. Right. So, what class clean room is this in terms of filtration? Uh I should know, but I don't remember.

**Dave Jones:** It's pretty good. It's It's uh It's It's It's up there. It's up there, yeah. And the lights, of course, um the That's yellow That's for photolithography. So, there is actually some photolithography going on here. Oh, so they wouldn't ordinarily have

**Dave Jones:** them on like that, or unless It's always on. It's always It's always on, but yeah. Okay, regardless of whether or not you're doing it Yeah, because yeah. So you don't have to exactly. Yeah.
