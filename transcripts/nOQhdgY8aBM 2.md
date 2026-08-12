---
video_id: nOQhdgY8aBM
title: EEVblog #1316 - Quantum Computing for Electrical Engineers
url: https://www.youtube.com/watch?v=nOQhdgY8aBM
source: youtube-asr
timestamps: {"0": 1, "1": 34, "2": 58, "3": 73, "4": 91, "5": 132, "6": 152, "7": 168, "8": 194, "9": 226, "10": 247, "11": 280, "12": 304, "13": 333, "14": 352, "15": 377, "16": 405, "17": 422, "18": 436, "19": 448, "20": 466, "21": 487, "22": 503, "23": 515, "24": 531, "25": 551, "26": 582, "27": 602, "28": 620, "29": 636, "30": 651, "31": 681, "32": 708, "33": 740, "34": 754, "35": 773, "36": 789, "37": 809, "38": 829, "39": 862, "40": 890, "41": 916, "42": 940, "43": 956, "44": 986, "45": 999, "46": 1014, "47": 1033, "48": 1060, "49": 1075, "50": 1102, "51": 1125, "52": 1153, "53": 1187, "54": 1220, "55": 1258, "56": 1272, "57": 1293, "58": 1319, "59": 1341, "60": 1357, "61": 1380, "62": 1408, "63": 1432, "64": 1447, "65": 1463, "66": 1476, "67": 1488, "68": 1518, "69": 1544, "70": 1563, "71": 1591, "72": 1610, "73": 1628, "74": 1650, "75": 1670, "76": 1695, "77": 1728, "78": 1747, "79": 1761}
---

**Dave Jones:** Hi, last week I sat down with Professor Andrea Morello from the University of New South Wales. He's one of the world's leading quantum computing researchers and a fellow electrical engineer. So, I thought we'd uh discuss quantum uh computing, all aspects of quantum computing. The rabbit hole goes super deep on this one, trust me. And uh but do it from an electrical engineering perspective. So, that's where we're going to come from. So, I've got a full 1 hour and 45 minute talk uh with Andrea. It's absolutely fantastic. You've got to go

**Dave Jones:** watch it. It's over on my EEV Discover channel. But, because I've only got limited subscribers over there, I thought I'd put around the first uh 25 minutes or so plus some bonus uh uh teasers at the end as well um for what the full interview is like. So, if you love this content, please go over to my EEV Discover channel to watch the full thing cuz it's absolutely fantastic. So, anyway, on with the show.

**Dave Jones:** If you liked it, give it a big thumbs up, you know, all that sort of stuff. Catch you next time. Hi, I'm here with Andrea Morello who's a quantum computing Sorry, Professor Andrea Morello. Just call me Andrea, it's okay.

**Dave Jones:** From the University of New South Wales uh quantum computing department. Uh well, electrical engineering department really. Technically all the electrical engineers yes, that's the department I'm on. And uh we're creating, you know, the quantum engineering of the future. So, it's all blended together.

**Dave Jones:** And for the benefit of my electrical engineering electronics engineering audience, how would you explain quantum computing to electrical engineers? All right. So, um electrical engineers will know that a classical computer that we use every day and that maybe some of your audience has helped developing, the microelectronics engineers in particular, are built with um the transistors and when they're used for logic, they act essentially as switches that have two states, you know, a low voltage state and a high voltage state. So, that's your zeros and ones in digital logic.

**Dave Jones:** And then you build a processor where you have, you know, a large interconnected array of, nowadays, billions of those transistors. And those are the chips that you use today to do classical computation. So, information is encoded in the electrical state of a nanoscale transistor in silicon.

**Dave Jones:** It's encoded in a in a binary mode. Zeros and ones corresponds to lower high voltages. And then you do logic operations by having essentially the state of a transistor switching or not depending on the state of another transistor. Okay?

**Dave Jones:** A quantum computer is something that retains the binary logic. So, it's still based upon zeros and ones. But those zeros and ones are not the high or low voltage state of a transistor, but they are one of the two quantum states of a suitable quantum mechanical object. Okay?

**Dave Jones:** So, the simplest example one can give is that of an electron that can jump between two atoms. So, in my particular research, I work with, uh, dopant atoms in silicon. Again, hopefully an electrical engineer will have done in their second year electronics some introduction to what a semiconductor device is and how it works. You take a crystal of silicon, you introduce dopants, which can be phosphorus or arsenic or antimony.

**Dave Jones:** using phosphorus though, or antimony? Uh, I am, but also antimony for other reasons that I can go into if you're curious, but Sure. Uh so, they're n-type dopants, okay? Um so, normally that dopant will donate It's a donor. It will donate an electron to the conduction band of um of silicon.

**Dave Jones:** And now imagine you set up your electronic device in such a way that you have two dopants close to each other and just one electron. Right? And you could say, "Okay, I'm going to encode a bit here. I call a zero the electron on the left and a one the electron on the right, okay? It's a system that can have two options." Another possibility, which is the one that I actually work on, is to use the spin of the electron. An electron not only has a charge, but also

**Dave Jones:** has a spin. The spin is the fundamental uh microscopic magnetic dipole of elementary particles like electrons, protons, and neutrons. And so, if I place this electron in a magnetic field, the spin will have two bases quantum mechanical states pointing up or pointing down. So, I can call spin down the zero and spin up the one, for example.

**Dave Jones:** So, I could make digital logic that way. But an electron is not just like a transistor. It is a genuine quantum object. So, again, think of the two atoms and one electron shared between them. That electron doesn't need to be choosing one atom or the other. It can be in a quantum superposition of being on both. Which again, when you say that way, people go all crazy. Oh, this counterintuitive weird world of quantum.

**Dave Jones:** This is actually completely logical, right? If you have two identical atoms and one electron, and the system is completely symmetric, which atom will the electron choose? It's going to choose either. Both. Both. Both. Yeah, or both. The logical, natural answer is that it spreads out across both.

**Dave Jones:** Yeah. Right? So, I never let anyone get away with saying that quantum mechanics is counterintuitive, you know, like It's actually completely logical. You choose both when you have equal equal opportunities and equal choices. So, that means that you can make a quantum bit that is in the zero and one state at the same time.

**Dave Jones:** Yeah. Okay? Now, this is, you know, No. No, that's not entanglement. That's superposition. Superposition. Superposition. Superposition. Entanglement is the next step, and that's where it gets really interesting. Again, for the benefit of our electrical engineering friends, um I quite often get the question from electrical engineers that say, "Okay, so you have this quantum bit that can be in an arbitrary superposition of being between zero and one.

**Dave Jones:** Isn't that the same as an analog circuit? Right? So, if I take an analog analog amplifier that can have an output voltage between zero and five volts, I can have any range of voltages between zero and five volts. So, does that mean I've made a quantum computer? No.

**Dave Jones:** And to see why that is, you need to take it to the next step, which is the entanglement. Right. So, the entanglement is a little bit more complicated, but again, it's you have to think of the the naturality of it. Okay?

**Dave Jones:** So, now let's say that Let me do the example. What do you think is best, the spin or the charge? Spin. Spin. Okay, let's do the spin. familiar with spin. I think everyone else would be more familiar with spin.

**Dave Jones:** Fantastic. Let's do spin, which is my baby. Okay, so now let's say you have two of these electrons close to each other, right? So, they have a spin that, you know, in its simple state can be up or down, but it can also be in a superposition. Okay?

**Dave Jones:** Um let's say that this spin is pointing up, right? And really you can take the classical image that you've seen in all your little geography books when you were a kid of the magnetic field produced by the Earth that makes these lines of magnetic field like these that come out of the North Pole and wind around and get into the South Pole.

**Dave Jones:** Okay? So, if you have a spin pointing up this way, it makes a magnetic field that goes up and then winds back down on the side. Right? What scale are we talking about there? Nanometers. It's It's nanometers. Nanometers, yeah.

**Dave Jones:** Well, I mean, the field spreads out to infinity, but it becomes in infinitely small as you go away. So, you know, to have a significant effect, you need to be nanometers close. Okay, so I got a spin pointing this way, up.

**Dave Jones:** And then I have another spin here, right? So, this spin will be subjected to the magnetic field produced by the first spin. So, on the side, the magnetic field is pointing down. So, this spin will prefer to point this way.

**Dave Jones:** Because that's the lower energy That's the lower energy state of the two magnetically coupled spin. All right? So, this is the preferred orientation for these two. But what if I turn them this way? Then it's equally It's It's It's enjoyable as before, right? Because this is now making a field. They're both happy.

**Dave Jones:** Yep. So, now what is the natural quantum state of these two spins that couple through this magnetic interaction? Is it this one or is it that one? They don't care. They don't care. care. It's the They don't care. It's both. But things are now a little bit more cheeky because now if I ask you in that state where they are at the same time like this and like that, which direction is this pin pointing?

**Dave Jones:** It's going to be always opposite to the other one. Correct. So, if you know one, you know the other. Yes. Hence, why entanglement works. Yes. Is that correct? Yes, it's correct. But, the point is this pin doesn't have a direction of its own anymore. So, if you ask me which way is this pin pointing, the correct answer is nowhere.

**Dave Jones:** Nowhere? Nowhere. Right. And if you actually do the calculation, it's really a simple calculation that I teach in third year to electrical engineers, you can calculate very simply what is the expected value of the spin orientation, and it's zero in every direction.

**Dave Jones:** Right. The spin has essentially evaporated. So, so the number pops out as zero for all directions. all directions. Right. Right? That's why you can't know. Uh So, what that's That's why you have something that a classical system cannot reproduce.

**Dave Jones:** Got it. Right? So, if you now take two analog circuits, and you couple them together, you will always have some voltage you can measure at the output of that Yes. circuit. Whereas, here you can't. You can't. Right? Got it.

**Dave Jones:** So, once you get to entanglement, that's where you really see the difference between classical, you know, continuous variables and quantum quantum systems. Got you. Now, this quantum state here, where they are in the up down and down up state at the same time, constitutes a completely legitimate digital code for a quantum computer.

**Dave Jones:** Okay? So, in a quantum computer with two quantum bits, I can encode four different combinations that are completely legitimate. So, I can have the down down, the up up, the combination of down up and up down where they are opposite to each other.

**Dave Jones:** And then there's another one where they are parallel to each other, but they point nowhere in the equatorial plane. Got it. And that's the extra over Yeah. basic byte like digital byte. Exactly. So, these entangled codes and now and now if you want to tell me which of the four combinations is that set of two quantum bits taking, you need to give me the coefficient of each one of those four combinations.

**Dave Jones:** So, to completely describe those two quantum bits, you need to give me four numbers. Right. You need to give me the coefficient of the down down, the up up, the this one, and this one. And the number is a piece of information.

**Dave Jones:** Yes. So, you need four pieces of information information for two quantum bits. two quantum bits. If I have three, you need eight. If you have four, you have 16. And so you see that the density of information contained in a set of n quantum bits is two to the power n.

**Dave Jones:** Two to the power of n. versus n in a classical computer. Exactly. So, this is why you only need say 300 odd bits or something as an example. 300 odd cubits we're talking about now. This is a is a cubit one bit.

**Dave Jones:** A cubit is one bit. Right. Is there other words other terms for like two bits and three? Um Or is No, but people use the word Q bit. Q bit. bit for a D dimensional system. So, you were asking me before you normally use phosphorus as the dopant where you encode the information.

**Dave Jones:** Actually, I use also use antimony Mhm. because antimony from an electrical point of view is equivalent to phosphorus. It's on the same column of the periodic table, right? But, the nuclear spin of antimony has a spin 7/2, which means it has eight possible orientation of the spin of the nucleus.

**Dave Jones:** So, that becomes an eight dimensional quantum system. So, you have eight possibilities instead of two. So, that's a Q bit with D equal eight. Dimensions equal eight. Is there any other advantage to that apart from information density? Um well, for quantum computing, you would mhm I don't know if I if I can call it an advantage. It's a difference.

**Dave Jones:** One important aspect of quantum computing is how resilient they are to noise. Right. Right. So, quantum states are very fragile. that. Why they're fragile. Yeah, yeah, yeah, yeah. So, if you imagine having Let's say, with an eight-dimensional spin, you it's the equivalent of having three Q bits, right? Because 2 to the 3 is eight. So, one atom of one nucleus of antimony is equivalent to three nuclei of phosphorus.

**Dave Jones:** Yeah. Okay? Equivalent, but it's different because the way they will be subjected to noise will be different. Okay. Imagine you have magnetic field noise. Okay? So, there is a fluctuating magnetic field in the environment. If you have three phosphorus atoms side by side, the magnetic field might be slightly different on each other of them. So, you have noise which may be uncorrelated.

**Dave Jones:** Right. Whereas, in that single nucleus of antimony, the noise is by definition correlated. You know, all the levels see because it's one atom, they all see the same noise. Yes. So, this can be a bad things in certain encodings, it can be a good thing in other encodings, depending on how you run it. So, this is in the subtleties I probably don't want to go into, but it's I wouldn't call it better or worse, it's different.

**Dave Jones:** Okay, but for this uh discussion, we'll stick with the phosphorus atom. the Q-bits, which is the simple thing. Okay. Right. So, can we think of a Q-bit as a storage register? Would that be an accurate Is it Is it a storage element?

**Dave Jones:** It is with one caveat that you cannot clone the information. You cannot make a copy. Can't make a copy. Okay. This is a fundamental theorem of quantum mechanics called the no-cloning theorem. Ah. You can transfer. So, for example, I can encode a bit of quantum information on one phosphorus atom here, and if I have another phosphorus atom next to it, I can transfer the information from here to there. But once I've done that, this one is erased. There is nothing left on this.

**Dave Jones:** Got it. So, it's non-volatile as long as you don't touch it. Yeah. As long as you don't measure it. Yeah, but you can't duplicate it. Okay, you can't duplicate it. Right. Got it. You can transfer it, but you lose the original.

**Dave Jones:** Got it. You only ever have one copy. Excellent. You can copy it, but you lose the original. Yeah. So, most people will think, "Okay, a Q-bit is where we store the information Mhm. that we're going to process in our quantum computer." process on the Q-bit.

**Dave Jones:** Yes. Uh the processing, this is what we need to get into. Okay, before we get into how the processing works, the actual computation, how does the quantum measurement works? Because you affect the state of it by measuring it. Is that correct?

**Dave Jones:** So, this is a hopefully a nice example for our electrical engineering audience. Um so here is where we use actual transistors Right. for the measurement. So the technology that I use is based upon using the dopant atoms as the qubits, the spin of the atom. But the readout device is actually a essentially a modified MOSFET.

**Dave Jones:** Right. So small transistor that we fabricate in our clean room. It's about 50 by 100 nanometers in size. So it's it's small. It's not even as small as the ones you have in the chip in your camera probably, but you know, that's what we can do.

**Dave Jones:** Now that transistor is designed in a way that we can make it very non-linear in its response. So it's not is not acting like a linear amplifier. It's it's a switch that switches from the change in position of even a single electron in its vicinity.

**Dave Jones:** This is actually not as hard as it sounds. Okay? Moving one electron in the vicinity of you know, a 50 nanometer size transistor actually has a significant effect on the bias point of that transistor. It's it's equivalent to moving Let me think. It's equivalent to applying you know, some about a millivolt Oh, I got you.

**Dave Jones:** transistor. Because you're looking at nanometer distance. It's just an electron charge, but an electron charge at that distance has you know, it matters. And then this whole system is cooled down to near absolute zero temperature. So it's you know, the system is extremely sensitive. And so this transition transistor can switch from off to on by simply displacing one electron in its vicinity.

**Dave Jones:** Right. Okay. And then, what we do is something that's called spin-to-charge conversion. Essentially, we make the displacement of that electron dependent on the orientation of the spin. So, the idea is this. And And that probably already answers the question that you may have had for later on, which is why do you need to go to near absolute zero temperature, and why do you need to do all the things you do. So, if you came to my lab, you will see some giant refrigerator that cools to 0.01°

**Dave Jones:** above absolute zero, and you will see a rack of electronics that is full of, you know, high-frequency, you know, microwave generators, and, you know, very sensitive amplifiers, and super quiet voltage sources. And one of the things I like the most when I explain it to the students is that you can look at this whole rack of instruments and refrigerators, and everything is there in there is the result of ratios of constants of nature.

**Dave Jones:** Right. It's the Bohr magneton, Planck constant, and Boltzmann constant. Got it. Given those numbers, you can You can understand why you need that rack of instruments, why you need that refrigerator. So, the idea is this. Um if you take the spin of an electron, and you place it in a magnetic field of one Tesla, one Tesla is a fairly strong magnetic field, okay? So, it's um you know, so, the the Earth's magnetic field in Sydney is about 60 microtesla, I think.

**Dave Jones:** Something like that. So, so, you put a one Tesla magnetic field, which we do either with a superconducting magnet, or with uh we're using nowadays some small arrays of permanent magnets. If you take a strong neodymium magnet, it's actually 1.3 Tesla.

**Dave Jones:** Oh, nice. So, it's actually about right. And so, we make some little arrays and we bolt them to the to the coldest point in this refrigerator. So, an electron spin in a 1 Tesla magnetic field has an energy difference between the spin down and the spin up state that is equivalent to 1.3 Kelvin.

**Dave Jones:** That is why you can't have anything above 1.3 Kelvin because then the thermal noise would be higher. You won't see the difference. see the difference. Now, is this a fundamental will this always be a fundamental limitation of quantum computers or is there some Do you guys have some grand vision to overcome this at like will room temperature Um so, quantum computers ever happen?

**Dave Jones:** is a little more subtle than this. So, Okay. uh Maybe let me just finish explaining how I use the transistor and then I'll tell you how you can do some other things, okay? So, you have this spin. When it's down, it's in the lowest energy state. When it's up, it's 1.3 Kelvin above the lowest energy state in energy.

**Dave Jones:** And in frequency units, so now you divide the energy by the Planck constant, that corresponds to 28 GHz. Right. So, if you come to my lab, you will see a 40 GHz microwave generator because that's what we need. That's given by the Planck constant.

**Dave Jones:** So, you have to excite it at the frequency derived derived by the Planck constant given the magnetic field. How how tight does that have to be? What tolerance on that? Very tight because these spins are extremely coherent, meaning the resolution we have on what is the frequency at which they respond is about 1 kHz.

**Dave Jones:** Oh, okay. This is very very sharp, and that's exactly what we want. Because the uncertainty on that frequency corresponds to an uncertainty on the quantum state as it evolves in time. It's like a clock, right? So, you want to keep track of all the clocks you have in your system. And if the clocks start to go slow or fast, then you lost you lost the relation between the phase of the clocks.

**Dave Jones:** Yeah. So, then we have these we have this spin that can be, you know, down or up. If it's up, it's 1.3 K, which is 120 microvolts for electrical engineers. 120 microvolts above the lowest energy state. And this electron is in the proximity of the transistor.

**Dave Jones:** And when the electron is in the high energy state, it has just enough energy to escape the atom and be sunk into the drain of the transistor. Oh, I thought it got into the gate. No, no, no, no. It goes into the drain.

**Dave Jones:** The gate is isolated. The gate is isolated. So, think of, you know, secondary electronics transistor. You got a source and a drain. You got a silicon oxide insulator, and the gate is on the top. The gate controls the potential, but is electrically insulated.

**Dave Jones:** And then in the body of the silicon, you got the source and the drain. This particular transistor is a little different. It's called a single electron transistor. It's got a little island of electrons between the source and the drain. That's what makes it so non-linear.

**Dave Jones:** But, you know, for the purpose of this discussion, we can kind of forget about it. Just imagine the electron bound to the atom. If it's in the high energy state, can escape into the drain of the transistor and just fly away.

**Dave Jones:** So, now you have a positive charge in the vicinity of the transistor. That positive charge will shift the bias point of the transistor and make it conduct. Uh-huh. And when it conducts, we will give us about a nanoamp of current that we can measure with a sensitive we can measure nanoamp. We can measure it in real time, so you can watch in real time with your eyes the quantum state of a single spin by watching a step in the in fact a blip in the current through a transistor.

**Dave Jones:** So, you can watch it on your oscilloscope as I as a digital waveform essentially. It's just a blip on the oscilloscope that digitizes the output of a current amplifier. Fantastic.

**Dave Jones:** Flipping one bit conditional on the state of the other, but because the other can be made in a superposition, then the flipping is also in a superposition of happening and not happening. And that's how you create entanglement. Don't they use that for the kilogram that you the the sphere the silicon sphere? It's the same same stuff.

**Dave Jones:** stuff. Yeah. Oh, okay. They don't need to. That's the beauty. They don't need to. This is for our engineer friends, you know, there is it it is a genuine engineering problem. There are tolerances like in any engineering design. The the tolerance is not zero. It's finite. It's a quantized nonlinear oscillator. So, imagine you make an LC oscillator an LC circuit, right? It will oscillate at a certain frequency. So, if you just take a capacitor and an inductor and you put it here on your breadboard.

**Dave Jones:** It's a tank resonance circuit. It's a tank resonance circuit. And at room temperature it will have, you know, billions of four microwave photons in it. Now, imagine this circuit resonates at 10 GHz. 10 GHz is the equivalent of half a Kelvin in temperature.

**Dave Jones:** Okay. Right? So, if you now cool down these tank circuit to 20 millikelvin, how many photons are in there? Zero. Are we talking Essentially, it's zero. So, it's an it's an electrical circuit. It's an LC oscillator in its quantum mechanical ground state.

**Dave Jones:** Okay. Is that like D-Wave? How do How How do D-Wave do it? D-Wave does it in a different So, this The example I gave you is what Google and IBM and some others are using. D-Wave does something different. D-Wave uses what's called a flux qubit. So, it's also a superconducting circuit, but you have to imagine it's a loop. It's a loop of superconductor.

**Dave Jones:** Unsorted is important. Oh, so if it was sorted, then of course you'll find it. But if it's unsorted and and the the reason this algorithm is intellectually important is because it's one of the very few where we know mathematically that there is a quantum advantage.

**Dave Jones:** It's amazing. If you look at the form of that equation, it's like the Schrödinger equation of quantum mechanics. Oh. Where the Planck constant Yeah. is the degree of arbitrage. Oh, no. Yeah. It pops out, doesn't it? It pops out. So, the quantum uncertainty we have in the Schrödinger equation in the economics model is the arbitrage.

**Dave Jones:** It's the uncertainty in the in the exchange rates. Mind blowing. Right? You see, my my wild dream is to, you know, have developed the technology to make, you know, quantum bits in silicon, have it all under control, have it, you know, have some deal with some foundry, and we get it all manufactured with the latest equipment, the fanciest technology, and we make a 100-qubit circuit, and you run it, and it works. You make a 1,000-qubit circuit, and you run it, and it works. You make a 10,000 cubic

**Dave Jones:** circuit. Scales. And then eventually it just stops. Yeah, that'd be disappointing, wouldn't it? That would be amazing. That would be amazing. That would be like to actually watch in an ele- in an engineered electronic device a new law of physics.

**Dave Jones:** Oh, it could it could pop out a new law of physics. Electronics engineering, listen to this, my friends. Electronics engineering enabling the discovery of a new law of physics. That's what I work for. That's what I work for.

**Dave Jones:** Wow, there's a Nobel Prize in that one. Yeah. If I'm still alive to get it.
