---
video_id: VQsoG45Y_00
title: EEVblog 1439 - Analysing Veritasium's Electricity Misconceptions Video
url: https://www.youtube.com/watch?v=VQsoG45Y_00
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 29, "3": 45, "4": 57, "5": 75, "6": 90, "7": 107, "8": 120, "9": 134, "10": 149, "11": 168, "12": 183, "13": 199, "14": 214, "15": 230, "16": 251, "17": 268, "18": 286, "19": 301, "20": 318, "21": 336, "22": 354, "23": 372, "24": 389, "25": 403, "26": 415, "27": 434, "28": 450, "29": 468, "30": 486, "31": 503, "32": 521, "33": 537, "34": 553, "35": 567, "36": 585, "37": 603, "38": 616, "39": 633, "40": 650, "41": 665, "42": 680, "43": 692, "44": 705, "45": 718, "46": 730, "47": 745, "48": 766, "49": 780, "50": 796, "51": 811, "52": 824, "53": 839, "54": 853, "55": 872, "56": 885, "57": 903, "58": 918, "59": 939, "60": 953, "61": 971, "62": 988, "63": 1000, "64": 1015, "65": 1029, "66": 1043, "67": 1060, "68": 1071, "69": 1089, "70": 1102, "71": 1121, "72": 1138, "73": 1151, "74": 1165, "75": 1182, "76": 1196, "77": 1210, "78": 1222, "79": 1236, "80": 1252, "81": 1265, "82": 1277, "83": 1291, "84": 1305, "85": 1319, "86": 1334, "87": 1354, "88": 1370, "89": 1382, "90": 1398, "91": 1411, "92": 1426, "93": 1441, "94": 1453, "95": 1468, "96": 1483, "97": 1501, "98": 1519, "99": 1535, "100": 1551, "101": 1566, "102": 1583, "103": 1596, "104": 1610, "105": 1622, "106": 1633, "107": 1649, "108": 1661, "109": 1674, "110": 1688, "111": 1703, "112": 1716, "113": 1730, "114": 1743, "115": 1755, "116": 1769, "117": 1782, "118": 1799, "119": 1810, "120": 1824, "121": 1837, "122": 1849, "123": 1865, "124": 1881, "125": 1896, "126": 1911, "127": 1927, "128": 1938, "129": 1953, "130": 1970, "131": 1987, "132": 2002, "133": 2018, "134": 2034, "135": 2047, "136": 2061, "137": 2076, "138": 2088, "139": 2103, "140": 2122, "141": 2141, "142": 2156, "143": 2172, "144": 2187, "145": 2201, "146": 2215, "147": 2226, "148": 2238, "149": 2250, "150": 2264, "151": 2281, "152": 2296, "153": 2312, "154": 2326, "155": 2342, "156": 2357, "157": 2370, "158": 2388, "159": 2402, "160": 2418, "161": 2435, "162": 2448, "163": 2462, "164": 2476, "165": 2486, "166": 2501, "167": 2514, "168": 2527, "169": 2543, "170": 2560, "171": 2572, "172": 2585, "173": 2602, "174": 2617, "175": 2630, "176": 2641, "177": 2654, "178": 2669, "179": 2686, "180": 2700, "181": 2713}
---

**Dave Jones:** Hi, all right, I'll do a video on it. So many people have sent me this asking can I comment on this Veritasium video, the big misconception about electricity. So, definitely watch it first. Don't watch my video. Stop this now. Go watch it if

**Dave Jones:** you haven't seen it linked up and down below. So, let's go through it. I'll go I won't go through the whole video, but I'll go through various points in the video and add some commentary and then we'll discuss how he actually gets the

**Dave Jones:** answer that he does and the implications of it. Imagine you have a giant circuit consisting of a battery, a switch, a light bulb, and two wires which are each 300,000 km long. That is the distance light travels in 1 second. So, they

**Dave Jones:** would reach out halfway to the moon and then come back to be connected to the light bulb which is 1 m away. Now, the question is, after I close the switch, how long would it take for the bulb to

**Dave Jones:** light up? Is it half a second? 1 second? 2 seconds? 1 over C seconds? Or none of the above? Spoiler alert, the answer is D, 1 over C seconds. But, technically, this is actually a bit misleading because I

**Dave Jones:** don't know whether deliberately or mistakenly he's left out the units on the one. It's not just one on C, it's 1 m on C. So, to get your dimensional units correct, it should be 1 m on C seconds. And

**Dave Jones:** this makes a huge difference to the answer that we're going to look at because if you don't include the 1 m, those wires aren't 1 m apart as you see here, then you actually don't get this answer, which is actually 1 m on C

**Dave Jones:** squared. And of course, if you put 1 m on C seconds in there, you would then you might have gone, "Aha, it has to do with the distance between the wires." And it does, as we'll see. You have to make some simplifying

**Dave Jones:** assumptions about this circuit, like the wires have to have no resistance, otherwise this wouldn't work, and the light bulb has to turn on immediately when current passes through it. That's fine. But I want you This question actually relates to how electrical energy gets

**Dave Jones:** from a power plant to your home. You know, unlike a battery, the electricity in the grid comes in the form of alternating current, or AC, which means electrons in the power lines are just wiggling back and forth. That is correct. Even if you had a

**Dave Jones:** completely DC power system from source to your house, or in the case of your product, from your battery into your product, you would get the electrons only slowly drift, very slowly, like this slowly, drift from the battery to your source. So,

**Dave Jones:** he's right. They never actually go anywhere. Just to teach this subject, I would say that power lines are like this flexible plastic tubing, and the electrons inside are like this chain. So, what a power station does is it pushes and pulls the

**Dave Jones:** electrons back and forth 60 times a second. Now, at your house, you can plug in a device like a toaster, which essentially means allowing the electrons to run through it. So, when the power station pushes and pulls the electrons, well,

**Dave Jones:** they encounter resistance in the toaster element, and they dissipate their energy as heat, and so you can toast your bread. Now, this is a great story. I think it's easy to visualize, and I think my students understood it. The only problem

**Dave Jones:** is it's wrong. Yes and no. From a physics point of view, yes, it's wrong. From a field theory uh point of view, yes, it'll like electromagnetic field theory point of view, it's wrong. But there's actually nothing wrong with using this kind of

**Dave Jones:** example. But in terms of actual practical engineering, engineers have developed uh lots of tools, methods, and uh laws uh like Ohm's law, Kirchhoff's laws, uh power maximum power transfer theories, transmission line theory, signal theory, all sorts of uh theorems we've developed

**Dave Jones:** to give a more practical insight rather than what's actually happening at the physics level. Who is taught this? Engineers are actually taught all of the stuff he's talking about in this video. In fact, it's fundamental to electrical engineering. Every electrical engineer

**Dave Jones:** knows about electron drift velocity and how slow it is. They know about electromagnetic fields and how the energy, spoiler alert, is carried in the electromagnetic field. And that uh current is actually a movement of charges in the wire, like move charges

**Dave Jones:** electric field uh in the wire. So, it's like we're taught this stuff. So, he's I he's really this he's not talking to engineers. This video is definitely not aimed at engineers cuz there's absolutely nothing new in this video for

**Dave Jones:** anyone who's trained in engineering. themselves have potential energy that they are pushed or pulled through a continuous conducting loop and that they dissipate their energy in the device. My claim in this video is that all of that is false.

**Dave Jones:** He is actually correct. Actually, everything he says in this video is actually correct. The energy, the power, is transported in the electromagnetic field. So, how does it actually work? In the 1860s and '70s, there was a huge breakthrough in our understanding of the

**Dave Jones:** universe when Scottish physicist James Clerk Maxwell realized that light is made up of oscillating electric and magnetic fields. The fields are oscillating perpendicular to each other and they are in phase, meaning when one is at its maximum, so is the other wave.

**Dave Jones:** Now, he works out the equations that govern the behavior of electric and magnetic fields and hence these waves. Those are now called Maxwell's equations. But in 1883, one of Maxwell's former students, John Henry Poynting, is thinking about conservation of energy. Now, if energy

**Dave Jones:** is conserved locally in every tiny bit of space, well, then you should be able to trace the path that energy flows from one place to another. Now, Poynting works out an equation to describe energy flux. That is, how much electromagnetic

**Dave Jones:** energy is passing through an area per second. This is known as the Poynting vector and it's given the symbol S. And the formula is really pretty simple. It's just a constant, 1 over mu naught, which is the permeability of free space,

**Dave Jones:** times E cross B. Now, E cross B is the cross product of the electric and magnetic fields. You put your fingers in the direction of the first vector, which in this case is the electric field, and curl them in the direction of the second

**Dave Jones:** vector, the magnetic field, then your thumb points in the direction of the resulting vector, the energy flux. But the kicker is this. Poynting's equation doesn't just work for light. It works anytime there are electric and magnetic fields coinciding.

**Dave Jones:** Anytime you have electric and magnetic fields together, there is a flow of energy and you can calculate it using Poynting's vector. Correct. To illustrate this, let's consider a simple circuit with a battery and a light bulb. The battery by itself has an

**Dave Jones:** electric field, but since no charges are moving, there is no magnetic field. So, the battery doesn't lose energy. When the battery is connected into the circuit, its electric field extends through the circuit at the speed of light. Correct. At the speed of light. That's

**Dave Jones:** important. This electric field pushes electrons around, so they accumulate on some of the surfaces of the conductors, making them negatively charged, and are depleted elsewhere, leaving their surfaces positively charged. These surface charges create a small electric field inside the wires, causing

**Dave Jones:** electrons to drift preferentially in one direction. Note that this drift velocity is extremely slow, around a tenth of a millimeter per second. But, this is current. Well, conventional current is defined to flow opposite the motion of electrons, but this is what's making it

**Dave Jones:** happen. This is absolutely correct, and every engineer is taught this. There's nothing new here at all. We're taught electron drift velocity. We're talking We're taught that current is actually, uh, the movement of electric charges, um, in the wire, and the We're taught the pointing

**Dave Jones:** vectors, and we're taught the whole shebang. We're taught the Maxwell's equations, the whole kitten caboodle. So, there's nothing new here at all for engineers. The charge on the surfaces of the conductors also creates an electric field outside the wires. And the current

**Dave Jones:** inside the wires creates a magnetic field outside the wires. Correct. So, now there is a combination of electric and magnetic fields in the space around this circuit. Correct. So, according to Poynting's theory, energy should be flowing. And we can

**Dave Jones:** work out the direction of this energy flow using the right hand rule. Around the battery, for example, the electric field is down, and the magnetic field is into the screen. So, you find the energy flux is to the right, away from the

**Dave Jones:** battery. In fact, Now, the problem here is that this is something he doesn't address in in He's talking about the pointing vector going out from the wire. Now, this is the case when you have uh AC. You are

**Dave Jones:** This is electromagnetic radiation, right? This is what happens. This is a big part of practical electrical engineering is designing products so that we can contain the electromagnetic energy in the field surrounding the wire. This is why we have transmission lines, coaxial

**Dave Jones:** cables. This is why we have uh transmission line theory on PCBs, for example. But, at DC and DC steady state, which we're going to take a look at, the pointing vector is actually back into the wire. It's not going out. There's no

**Dave Jones:** electromagnetic radiation at DC. That only happens at AC, anything above DC, basically. And the higher frequency you go Anyway, that's all theory we won't get into. But, at DC, it's actually pointing in. It's not pointing out. So, I'm not going to say that's a mistake

**Dave Jones:** cuz I know what he's trying to get at in this video. All around the battery, you'll find the energy is radially outwards. Energy is going out through the sides of the battery into the fields. Along the wires, again, you can use the

**Dave Jones:** right-hand rule to find the energy is flowing to the right. This is true for the fields along the top wire and the bottom wire. But, at the filament, the pointing vector is directed in toward the light bulb. So, the light bulb is getting

**Dave Jones:** energy from the field. If you do the cross product, you find the energy is coming in from all around the bulb. Now, this is correct because the light bulb is a resistor. It's just a wire that's a resistor. And this will happen

**Dave Jones:** on the wires as well, which he neglects here. And of course, in the example, he assumes that there's no resistance in the wires as well. Because if you've got resistance in the wires, it means that there's a pointing vector going back in

**Dave Jones:** and there's going to be I squared R energy loss in the resistance in the wire and that's what's happening in the light bulb. It's actually there's a lot of pointing vector going in cuz it's a high resistance thing is

**Dave Jones:** dissipating the power in there whereas the wires going to it hopefully low enough resistance they're not dissipating much. Most of the energy is being transferred into the bulb and of course if you use superconductors for the wires then all of the energy there's

**Dave Jones:** going to be no loss in the wires and all the energy is going to be dissipated in the light bulb and if you're powering the light bulb with DC all of the pointing vector is pointing back into the bulb but actually if you power your

**Dave Jones:** bulb using AC some of it is also going out as well being lost as electromagnetic radiation. It takes many paths from the battery to the bulb but in all cases the energy is transmitted by the electric and magnetic

**Dave Jones:** fields. This correct. the fundamental part about this video is that energy / power cuz energy is just power over time so we'll call it power. Power is not transmitted in the wires. Technically at the physics level yes according to pointing theorem is that

**Dave Jones:** the energy is actually transported outside of the wire in the electromagnetic field. That's actually correct. People seem to think that you're pumping electrons and that you're like buying electrons or something which is just so stupid. thinks that. Who thinks that?

**Dave Jones:** For most people and I think to this day it's quite counterintuitive to think counterintuitive. the space around the conductor but the the energy is which is traveling through the field yeah it's going quite fast. So there are a few things to notice here

**Dave Jones:** even though the electrons go two ways away from the battery and towards it by using the pointing vector you find that the energy flux only goes one way from the battery to the bulb. This also shows it's the fields and not the electrons

**Dave Jones:** that carry the energy. I mean, how far do the electrons go in this little thing you're talking about? They barely move. They probably don't move at all. Now, what happens if in place of a battery we use an alternating current

**Dave Jones:** source? Well, then the direction of current reverses every half cycle. But, this means that both the electric and magnetic fields flip at the same time. So, at any instant, the pointing vector still points in the same direction from

**Dave Jones:** the source to the bulb. Correct. exact same analysis we used for DC still works for AC. And this explains how energy is able to flow from power plants to homes in power lines. As I said, the only issue I had with

**Dave Jones:** this is how he didn't really adequately explain DC because DC is actually kind of fun as we'll get into. It's it's not fundamentally different, but engineers think about DC steady state in a different way than we think about um

**Dave Jones:** AC. They are actually quite different things, and the tools that engineers have developed in the way we use them in practical design, it makes a difference whether you're talking about AC or DC. But, as at a physics level, yes, it's all about

**Dave Jones:** the pointing fields. Inside the wires, electrons just oscillate back and forth. Their motion is greatly exaggerated here, but they do not carry the energy. Outside the wires, oscillating electric and magnetic fields travel from the power station to your home. You can use

**Dave Jones:** the pointing vector to check that the energy flux is going in one direction. You might think this is just an academic discussion that you could see the energy as transmitted either by fields or by the current in the wire, but that is not

**Dave Jones:** the case. Actually, it is the case because a huge part of practical engineering is ignoring Maxwell's equations and pointing vectors and like actually in just thinking that the current flows in within the wire instead of the electromagnetic field around it. It's

**Dave Jones:** only when you get to talking about you know, higher frequency cases and stuff like that, then you have to start taking that into into account and it becomes absolutely critical in a lot of cases, most cases actually. And yeah, but

**Dave Jones:** that's not entirely true. Yes, physicists may not think that, but practical design engineers on everyday basis our tools and techniques, there's nothing wrong at all with thinking about current flowing within the wire itself. And people learn this the hard way when

**Dave Jones:** they started laying undersea telegraph cables. The first transatlantic cable was laid Now, I won't go through this whole transatlantic cable thing, but basically what they're talking about here is transmission lines. And this this is not talking about transmitting power like 50

**Dave Jones:** 60 hertz power over the ocean. This is talking about sending signals over a transmission line. So, this was actually the early attempt of engineers and physicists trying to figure out exactly what was going on here and then develop

**Dave Jones:** transmission what we now know as transmission line theory. It's yes, it has to do with the pointing vectors and everything else, but really we're talking about transmission lines here. We're not talking about like 50 hertz power. And that's the one term you

**Dave Jones:** won't hear Derek use in this video. And I think it's probably deliberate. He didn't use the word transmission line. And this as we'll see, this is fundamentally a transmission line problem. The question he's proposed is fundamentally a transmission line

**Dave Jones:** problem. So, yeah, the fact that he left that out, I it just this is what irks engineers. There are all kinds of distortions when they try to send The enormous amounts of distortion. So, what is the answer to our giant

**Dave Jones:** circuit light bulb question? Well, after I close the switch, the light bulb will turn on almost instantaneously in roughly 1/c seconds. So, the correct answer is D. I think a lot of people imagine that the electric field needs to travel from the

**Dave Jones:** battery all the way down the wire, which is a light second long, so it should take a second for the bulb to light up. But, what we've learned in this video is it's not really what's happening in the

**Dave Jones:** wires that matters. It's what happens around the wires. Correct. It's what happens around the wires, and this is why his answer D is totally dependent on this 1 m gap, which is deliberately introduced into the question. Because if he stretched the

**Dave Jones:** these wires out to a circle, uh you know, this huge diameter circle, then you wouldn't get that answer. If you move it to 2 m, the answer is actually a 2 m on C. It's not one on C

**Dave Jones:** anymore. So, his answer is very deliberately tied to the distance between the wires. And this is basic transmission line theory. And the electromagnetic fields can propagate out through space to this light bulb, which is only 1 m away in a

**Dave Jones:** few nanoseconds. That's right. So, he's taken like he is correct. He's telling you the information, but then he's sneakily leaving out the information, the the meters in the equation, um in the actual answer. Like should be 1 m on C. So, he's deliberately leaving

**Dave Jones:** in that out, because then if you if that 1 m on C was in the answer, it'd twig in your head that aha, it has to do with the distance between the cable. And so, that is the limiting factor for

**Dave Jones:** the light bulb turning on. Now, the bulb won't receive the entire voltage of the battery immediately. It'll be some fraction, which depends on the impedance of these lines and the impedance of the bulb. And here's where he starts to imply

**Dave Jones:** transmission lines. When you start talking impedance, you start talking transmission lines like this. So, yeah, I did but he's I think very sneakily left out that deliberate word. So, yeah, I think it's a bit disingenuous to leave that out, but I can understand him not

**Dave Jones:** going into the details because this video is not aimed at an engineering audience. It's just not. There is absolutely nothing new whatsoever in this video for anyone who's learned engineering. So, yeah, it's it's aimed at the general public. So, yeah, I'll

**Dave Jones:** give him a pass. bulb. Now, I asked several experts about this question and got kind of different answers, but we all agreed on these main points. So, I'm going to put their analysis in the description I have not looked at that analysis about

**Dave Jones:** this particular setup. But, I believe they go into transmission lines. We can we can definitely invest the resources and and string up some lines and make our own power lines in the desert. You're going to get called out on it.

**Dave Jones:** I agree. I think you're going to get called out. Yes, he's going to get called out by engineers who think that this question is a little bit sneaky because and the things that you left out of the video

**Dave Jones:** are yeah, important, but everything he fundamentally said in the video is correct. So, I've got to give him props for the video. It is good in that it helps people know about Maxwell's equations, pointing vectors, and how the energy does actually flow

**Dave Jones:** outside the conductor, but there's some details deliberately left out here and it's it's kind of a little bit annoying for us engineers. And because on a daily basis, we don't really have to deal with Maxwell's equations and pointing

**Dave Jones:** vectors. We do most of our practical engineering using the tools and techniques we've developed to make it much simpler and much more practical. We just don't need to think unless we're at high frequencies and other sort of like

**Dave Jones:** extremes, we don't really need to think about energy flowing outside the wire. Having it flow inside the wire is fine. Stick around to the end of the video because I'll show you what Richard Feynman says on the subject and he kind

**Dave Jones:** of agrees with me and other engineers that meh, you don't really like these pointing vectors. Yeah, that's how it seems to be really working at the physics level and it's really interesting and stuff, but you don't really have to use that on a practical

**Dave Jones:** basis and it's fine if you forget that energy flows outside the wires instead of inside the wires. I think it's just kind of wild that this is one of those things that we use every day that almost nobody thinks about or

**Dave Jones:** knows the right answer to. These traveling electromagnetic waves around power lines are really what's delivering your power. But another problem with this video and it's one that irks engineers is that no mention was made of skin effect of cable

**Dave Jones:** for example where the the diameter of the cable matters. He did not mention that at all and that varies with frequency and at DC there is no skin effect. There's no DC there's no electromagnetic radiation going out. But at AC there is and a good part of

**Dave Jones:** engineering is trying to design products to contain this electromagnetic energy which is outside the cables. Take piece of transmission lines or PCB traces which are transmission lines for example. I've done many videos on this talking about how you know, PCB routing

**Dave Jones:** matters. Let's say you have a trace which is going you know, routing across snaking across your PCB like this and you have a big ground plane under for example. Well, the higher frequency you go, the more the energy doesn't the

**Dave Jones:** energy the power isn't actually spread across the ground plane like this or the return current as we talk about in PCB design. It it's not just spread out across the ground plane. The energy actually follows the trace. It actually

**Dave Jones:** follows in the ground plane even though the ground plane is one big continuous sheet of copper. It follows under the trace like this. The rest of the copper doesn't matter the more higher frequency you go. So he's not mentioning practical

**Dave Jones:** aspects like the skin effect and or mentioning at DC that the pointing vector is going into the wire like this and the magnetic fields aren't actually pushing the electrons to the outside. If there was then well at DC we wouldn't be

**Dave Jones:** able to transfer large amounts of power and at AC cuz 50-60 hertz is almost DC. Now we it's not quite but you know it's really low frequency stuff. So there is some skin effect there but it's incredibly low. So none of this is

**Dave Jones:** covered. None of this is even hinted at in the video. In fact the entire video just sort of implies that well the diameter of the cable doesn't matter cuz all the energy flows on the outside. If that was the

**Dave Jones:** case then we wouldn't be able to string all of our megawatts of power down the transmission lines with a you know a tiny little 30 gauge wire or something and that's not the case cuz once again practical engineering and Ohm's law

**Dave Jones:** Kirchhoff's laws and everything else must be obeyed. So there shouldn't be any engineers out there who are amazed at this and yeah and a lot of engineers will call him out because well we just think about things in a different way.

**Dave Jones:** It's the fundamental physics versus practical engineer mindset and this is just like when ElectroBOOM had the big debate with Professor Walter Lewin about uh could Kirchhoff's uh voltage law hold in electromagnetic fields? Anyway, I won't go through the

**Dave Jones:** whole thing, but basically, it's the engineering mindset versus the physicist mindset. And the physics isn't wrong. Um it's absolutely Derek is correct in practically every point he makes in here that the energy is actually transferred, the power is transferred in the

**Dave Jones:** electromagnetic field outside of the wire. But then at DC, it's like question, but ultimately, the physics does hold, and these pointing vectors are where the magic happens with uh the energy transfer. At least that seems to be the case. But there you know, there's

**Dave Jones:** a lot of debate still about this kind of stuff, but nobody has proven that uh Poynting's theorem is wrong. So anyway, let's take a look at how we would solve this actual particular question Derek has uh proposed from an engineering point of

**Dave Jones:** view cuz it's really simple. So, how do electrical engineers solve this sort of problem and show that the light bulb can turn on within a couple of nanoseconds? Well, it's really simple. It's really basic. It's practically engineering 101

**Dave Jones:** really. It's a called a lumped element model. So, we're going to simulate this as a transmission line because this is fundamentally a transmission line problem to electrical engineers and in practice as well. This would have been a transmission line problem. So, we can

**Dave Jones:** model a transmission line, and in this case, show you how the light bulb is able to turn on within a couple of nanoseconds, instantly. Okay, so we've got the model up here. Okay, the wires are a meter apart like this, and it's

**Dave Jones:** half a light second across in either direction. Now, this uh if you've got wires 1 m apart like this, depends on how you calculate it, but basically, this is a transmission line of uh roughly 800 to 900 ohms

**Dave Jones:** characteristic uh impedance. Not that that matters uh for what we're going to do here. It's just like it'll have a nominal characteristic impedance as a transmission line. Okay, so what we've got here is the voltage source, we've got the switch. I have to have a ground

**Dave Jones:** symbol in here, otherwise it won't simulate. We've got our lamp, which I've just put as a 100 ohm resistor here. And then what we do is we simulate our transmission line with what's called this lumped element model. And this is

**Dave Jones:** where we break up the transmission line into fundamental little circuit elements that we know and we can analyze. In the case of a transmission line, you have L's, C's, and R's, resistance, inductance, and capacitance. And you have capacitance

**Dave Jones:** between the line like this. I've just put in one microfarad. Doesn't matter what the values are. There's going to be some capacitance between these wires, even if they're a meter apart. And actually a standard engineering trick question is to calculate the capacitance

**Dave Jones:** between the Earth and the Moon. Um that just comes up. They just like to throw that in as an exam question. And there's going to be capacitance there. So there's going to be capacitance between these wires 1 m apart like this. And of

**Dave Jones:** course wires have resistance as well. But because Veritasium has said we're ignoring the resistance of the wires, I've set the resistance of the wires to zero. Not that it matters for this simulation. And of course every wire, every PCB trace,

**Dave Jones:** every component lead, everything, every conductor in electronics has some form of inductance. So we're going to have an inductor. I put 1 microhenry. The values don't matter, okay? So each unit length of the transmission line that can be a

**Dave Jones:** centimeter, an inch, it can be a meter. It doesn't matter what it is, right? A unit length will have capacitance and series inductance and series resistance, which we're going to have zero. So you put that in your schematic like this and

**Dave Jones:** then you just duplicate it, duplicate it, and you go out to infinite. Well, not quite infinity, almost infinity, a half light second worth of infinity. And you also do it in the other direction as well. And that simulates your

**Dave Jones:** transmission line, but we don't have to do anything more than one element here to show what's going on. But I've just put in two because, you know, it looks a bit better. Now, of course, the end of this transmission line is shorted like

**Dave Jones:** this at each end. So, once we turn that switch on and everything settled down, all the transients are gone away, the current will actually flow all the way through the wire, right through the end bit, and through the lamp, and back for

**Dave Jones:** the half light second or whatever it is, okay? But when you turn on a switch like this, you are doing what's called a transient. And a transient means you've got time at zero and then you've got X time after that. So, we're going to

**Dave Jones:** simulate this in the time domain starting from time zero when we turn on the switch and we're going to see what happens. But I'm actually going to leave these electrically open at the end because at time zero, when we turn that

**Dave Jones:** switch on, the signal hasn't had time to propagate the half light second all the way across, right to here yet. So, when you turn that switch at time zero or time, you know, at one nanosecond or one microsecond or something, it hasn't had

**Dave Jones:** time to get all the way to the end yet. So, it's almost So, as far as the circuit is concerned, as far as the simulation is concerned, as far as the real world transmission line is concerned, this isn't open circuit at

**Dave Jones:** either end. So, that's what I've done. I've kept them open here because we can't simulate it a short enough time to simulate the half light second and everything else. But every engineer knows this stuff, right? It's incredibly basic stuff. Anyway, so let's simulate

**Dave Jones:** this. Let's run it and see what happens. Now, what I'm going to do is I'm going to plot the voltage across the lamp here. So, that's VR1 minus that node minus that node. So, the voltage across the lamp. And we're also going to get

**Dave Jones:** current through the lamp as well. So, we're going to get voltage and current graphs. I'm going to start at time zero. I'm going to simulate this for 100 milliseconds or 0.1 seconds, and I'm going to there's my step time is going

**Dave Jones:** to be 1 microsecond. So, let's go. We're running the simulation and we will get the results from T zero. Bingo. Look at this. At T equals zero here, this is the volts, okay? So, this is the voltage across the resistor. Look at this. It

**Dave Jones:** jumps up to 1 volt immediately. And then it jumps up to 10 milliamps absolutely immediately. And if we zoom in there like this, you can see that it's there it is. There's a transient right at time zero. We can actually get in there finer

**Dave Jones:** than that, and we can see that it's like 2 microseconds, half that in 1 microsecond, it's ramped up right to 1 volt instantly. Within a microsecond, there's a volt across that resistor. Now, of course, this is because we only

**Dave Jones:** simulated at a 1 microsecond period. If we simulated it at 1 nanosecond, we'd see it ramp up in a nanosecond. So, why does it do this? Well, everyone who knows basic capacitor theory knows why. It's because the cable capacitance right

**Dave Jones:** near, as in like right at the switch and the uh lamp here, the capacitance between the two wires that are 1 m apart, remember, they will have a tiny minuscule amount of capacitance, then that capacitor at time zero is a short

**Dave Jones:** circuit. So, it's almost as if there's a short circuit in here like this and a short circuit at the lamp within like 1 m like this. And of course, you won't get 1 volt across the lamp as as Derek

**Dave Jones:** said in the video, you're only going to like it'll they'll they'll only turn on a small amount, whatever that happens to be, due to the circuit characteristics, right? The capacitance across a meter and stuff like that. It's not much, but in theory, it's going to

**Dave Jones:** switch on instantly because it's only like a meter away. Well, as the answer to the question says, it switches on in 1 m divided by C, the speed of light. So, it switches on like within a couple of nanoseconds. And it does that because

**Dave Jones:** of the capacitance of the line. This is basic transmission line theory. There's nothing special going on here at all. This is engineering 101. Every engineer knows this. But of course, what happens after that, we won't go into transmission line theory and like no,

**Dave Jones:** wave propagation and the whole rest of it. We just won't, okay? The fact is, this is how you answer the question and if of how the light bulb switches on almost instantly when you close the switch. Suffice it to say though that

**Dave Jones:** after X amount of time, you will actually reach what's called steady state. And that's when the transmission line doesn't matter anymore, the capacitance doesn't matter anymore, the inductance doesn't matter anymore, because the inductors and capacitors, they only matter for

**Dave Jones:** transient cases or AC cases. For DC, because we've just got a battery, then you're eventually going to reach what's called DC steady state. And that's when it's those inductors are no longer there, the capacitors are no longer there, and all you've got is the

**Dave Jones:** line resistance, and that's it. And then the current will actually flow, will have to flow by definition all the way to the end, to the short circuit, and like that. So, if the lamp wants to stay on for a long

**Dave Jones:** period of time, once it reaches steady state, then yeah, it's got it the current has to flow through the entire loop. It won't flow through the capacitance anymore because nothing's changing. There's no transient circuit, there's no AC. There's not the

**Dave Jones:** capacitor, it's just an open circuit, and the inductors are just short circuits. Once again, fundamental DC circuit theory. Now, the voltages and currents we saw there are by no means close to representative to what you'd actually get in this physical scenario.

**Dave Jones:** And that's not the point. I'm not I don't want to get bogged down in the deep in the quantitative details of what the actual answer is because it doesn't matter. The whole point of this concept is to show how Derek can come to the

**Dave Jones:** conclusion that the answer is D 1 on C seconds, which is actually incorrect dimensionally. Unit-wise, it should actually be 1 m on C seconds. Now, I'm not sure if that was a slip-up or whether or not that's deliberate cuz if

**Dave Jones:** you put in 1 m on C seconds, then that would imply that the answer is related to the 1-m difference spacing between the conductors and it is. This answer does not hold if you actually put this thing, stretch it out into a

**Dave Jones:** circle, for example, because you don't have that initial capacitive coupling between here. You've got to go Well, technically, there isn't some absolutely minute, ridiculously small, half a bee's dick level, but you will not get the answer 1 m on C seconds. You'll get some

**Dave Jones:** other answer, which is faster than going all the way, like right through the whole loop, but it won't be that 1 m 1 on C seconds. So, this is fundamentally set up as a transmission line problem with the 1-m

**Dave Jones:** gap between there to give that incredible answer that stunned everyone. Like, "Oh, how can that how can that be?" It's because they're 1 m apart and there's capacitance between the wires. Of course, you don't have to technically model this as a transmission line. You

**Dave Jones:** can just go, "Okay, there's two wires and there's capacitance." And you can just have the capacitors in there, but ultimately, this is a transmission line problem because it's a step response which generates multiple frequencies using Fourier, of course, because a step

**Dave Jones:** is made up or any uh square wave is made up of a fundamental plus all the harmonic frequencies. I won't go into uh Fourier, but it then it acts as a step response transmission line. And this is exactly what it is, and this is and this

**Dave Jones:** answer only holds if they're a meter apart. So, is it a trick question? Is it disingenuous? Yeah, you could make the argument there, but the whole idea is to give people something that's sort of like shocks them into thinking, "Oh, like wow, how

**Dave Jones:** can this happen?" But I Come on, it's a transmission line. But if he said up front, or if he put the 1 m in there, the 1 m, and said, "Oh, this is a transmission line." Um although he did

**Dave Jones:** mention impedance, sort of alluded to it. But if he mentioned that sort of thing, the game's up, right? To every You don't shock any engineer at all by this. It's just, "Oh, yeah, of course. Duh." So, the response of how this circuit

**Dave Jones:** actually works in practice over the time is actually modeled and will work as a real transmission line. It's just that In in practice, yeah, I put 1 microfarad in here, but in practice, the capacitance is going to be absolutely

**Dave Jones:** tiny, the inductance is absolutely tiny, and the amount of power you get in to the lamp over here, it's naff-all, but it's there. And that's the whole point of this, to show that yeah, it can flow in the electric It can flow in the

**Dave Jones:** fields. The energy can actually flow in the fields. this case, it's like all explained by basic engineering 101, like cable capacitance, transmission line stuff. There's nothing special. You don't have to worry about, you know, pointing vectors and and everything else

**Dave Jones:** and energy flowing outside the wires. It like that's just like hand-waving stuff. Like electrical engineers, this is how they're going to look at and solve the problem practically. So, yes, Derek is correct, and the whole video is essentially correct that energy flows

**Dave Jones:** outside the wire in the pointing vector. It's That's just like the physics of how it actually works. But, here comes the interesting part. You know how I mentioned steady state, okay? When you analyze these sorts of things, you

**Dave Jones:** analyze a trend, you do transient analysis, which is what we just did. But, once all the transmission line settles down, all the waves have stopped going or ringing on the transmission line, everything's stopped and settled down, and you're 10 seconds later or

**Dave Jones:** whatever, right? And that light bulb's just constantly on in decent That's called DC steady state. And this is a different analysis mode. Engineering has all these different types of an analysis. There's transmission line analysis, there's transient analysis, DC

**Dave Jones:** and steady state analysis. These are like fundamentally different things taught in engineering and because there are these different modes. So, once it's all settled down, and as I said, the current the capacitance doesn't matter anymore, the inductance doesn't matter

**Dave Jones:** anymore, the current is flowing all the way out right to the end like that, and it's flowing around the whole thing, everything's steady state, nothing matters but the cable resistance anymore, then you have to ask the question again. Is the power or slash

**Dave Jones:** energy Focus energy is just power over time. Is So, we use the word power. Is the power flowing in the wire itself or is it flowing through the outside the wire in the electromagnetic field? Well, at DC, there is no electromagnetic

**Dave Jones:** radiation. Okay? It's It's DC. Nothing's changing. Nothing's switching. There is It's simply staying put. Now, of course, when current flows through a wire, you use the right-hand rule. When current flows through a wire, you get an electric field around it, but that

**Dave Jones:** electric field is not moving. It is stationary. So, in DC mode, is the power actually flowing through the wire instead of around it like it would during AC and you know, like transient, right? At higher frequencies. Well, the

**Dave Jones:** answer is once again, according to Poynting theorem, is the answer is uh no, still does not flow through the wire because if we go to Feynman's lecture, so you can see in Feynman's notes here that the Poynting vector S is actually going into the

**Dave Jones:** wire. This is steady-state DC, okay? So, it's it's just simply a wire carrying a current. You still got the electric field, which is going uh up like going along the wire in the direction of the current flow, then

**Dave Jones:** you've got the magnetic field pointing out of the wire, but you still have the Poynting vector going back in. And this is like rather academic, but technically the Poynting theorem math still works out that there is still a Poynting

**Dave Jones:** vector going in. And there is argument a lot of people don't actually believe that's uh the case and at steady-state DC it doesn't apply and stuff like that, but like I'm for argument's sake I'm I'm not going to disagree with Feynman,

**Dave Jones:** right? I'm I'm not a physicist. I'm going to say, yes, the Poynting vector is still in there. But Feynman says it down here, you don't need to feel that you'll be in great trouble if you forget once in a while or all the time, as

**Dave Jones:** engineers do, that the energy in a wire is flowing into the wire from the outside rather than along the wire. It seems to be only rarely of value when using the idea of energy conservation to notice in detail what path the energy is

**Dave Jones:** taking. And he says it's not a vital detail, but it's clear that our intuitions are wrong, right? So, I'm going to like I'm going to say, yeah, okay, fine, the energy {slash} power still flows outside the wire in the

**Dave Jones:** point and it actually flows back in, but like I can't think of a single instance in all of practical engineering where this matters. There might be some obscure thing and in physics research and everything else and I'm and if you're

**Dave Jones:** doing the physics, I'm sure, yeah, okay, fine, it works out. But, in engineering, no. Nobody, absolutely nobody thinks about the power at DC steady state that the power is flowing outside of the wire in the pointing field, which is then

**Dave Jones:** going back into the wire. It's just No. So, if it's good enough for Richard Feynman to go meh, it's good enough for me. So, from my practical engineering perspective, I do know, every engineer knows that energy flows outside the wire at high

**Dave Jones:** frequency, right? This is like transmission line theory. This is how wave guides work. This is how a whole ton of stuff in engineering works. And you really do have to understand that. But, at steady state DC, there there's

**Dave Jones:** just no No, the power flows through the wire. And the other thing, of course, is that at DC, there is no skin effect, okay? The pointing goes all the way in to the middle. There is like There's no

**Dave Jones:** skin effect. So, to say to think that the power doesn't flow through the wire is just is just pointless and dumb when you talking about DC. But, once again, technically, I am going to concede that yes, the energy flow even at DC is in

**Dave Jones:** the pointing vector outside the cable. But, I That's just for academic exercises. Nobody Even Feynman just goes meh. So, there you go. Comment down below, and I'm sure everyone will cuz this debate has been raging on since time

**Dave Jones:** immemorial. There's nothing new here. But, to engineers, Derek's video was It was just like meh. Yeah, it's a transmission line. So, what? And a lot of people are going to say, "Yeah, it's disingenuous." But, hey, if it got

**Dave Jones:** people interested in talking about, you know, pointing vectors and how energy flows outside the cable and stuff like that, yeah great. Okay, thumbs up to Derek. And I'm sure there'll also be a ton of people who will take me to task

**Dave Jones:** in the comments down below. Like going into the deep maths of it and and how my model here is wrong but no, but no, sorry. This is how you get the answer here by it being 1 m apart

**Dave Jones:** when it's 1 m apart like this, it's modeled as a transmission line. Engineering 101. If you want to argue otherwise, once again, this is not the only way to look at it, right? A physicist will look at this question very differently to a

**Dave Jones:** practical engineer, but this is how a practical engineer would solve this problem. Right? And derive and well, explain how you can get that answer. And I think it's like the easiest and simplest explanation and it's going to be understandable by every electrical

**Dave Jones:** engineer out there. So, thanks to Derek for putting in that video up. It's fascinating. It sparked a whole bunch of debate. Absolutely fascinating topic and as he predicted in the video and as the professors he talked to predicted, yeah,

**Dave Jones:** he was taken to task over it and well, that's fine, but nothing he said in that video is actually wrong. Pointing, yeah, the energy flows outside the wire. It's the pointing vectors and all that. So, the stuff it's just yeah, especially at

**Dave Jones:** DC. Yeah, nobody thinks that way in practical engineering. So, there you go. Flame away down below. Hope you enjoyed it, found it interesting. Catch you next time.
