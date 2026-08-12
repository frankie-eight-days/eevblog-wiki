---
video_id: qUeK7pHe0rI
title: EEVblog #748 - How Do Transistors Work?
url: https://www.youtube.com/watch?v=qUeK7pHe0rI
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 27, "3": 39, "4": 51, "5": 63, "6": 75, "7": 88, "8": 104, "9": 119, "10": 133, "11": 146, "12": 160, "13": 174, "14": 189, "15": 207, "16": 222, "17": 242, "18": 260, "19": 275, "20": 289, "21": 304, "22": 318, "23": 334, "24": 348, "25": 362, "26": 376, "27": 391, "28": 405, "29": 421, "30": 438, "31": 449, "32": 462, "33": 475, "34": 494, "35": 509, "36": 526, "37": 539, "38": 558, "39": 574, "40": 591, "41": 606, "42": 621, "43": 636, "44": 657, "45": 671, "46": 688, "47": 702, "48": 715, "49": 733, "50": 746, "51": 764, "52": 780, "53": 796, "54": 809, "55": 823, "56": 834, "57": 850, "58": 862, "59": 878, "60": 893, "61": 909, "62": 921, "63": 934, "64": 947, "65": 965, "66": 980, "67": 995, "68": 1018, "69": 1036, "70": 1050, "71": 1067, "72": 1084, "73": 1098, "74": 1111, "75": 1124, "76": 1138, "77": 1151, "78": 1167, "79": 1182, "80": 1198, "81": 1215, "82": 1236, "83": 1255, "84": 1268, "85": 1283, "86": 1298, "87": 1318, "88": 1331, "89": 1348, "90": 1368, "91": 1376}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at how transistors work, not at the circuit design level, but more at the physics silicon level. Let's go. Now, we're going to take a look at two different

**Dave Jones:** types of transistors cuz they are physically different in how they operate at the silicon level. One is the bipolar junction transistor, your BJT, the other is your field effect transistor or a FET. Now, we're actually going to look

**Dave Jones:** at a particular type of FET, the MOSFET in this uh case cuz there are many different types and well, that's probably best left to a different video. Now, regardless of whether you have a BJT type or a MOSFET, they going to work

**Dave Jones:** in your circuit configuration pretty much exactly the same. We're going to look at the NPN type and the N-channel type only here today and you should be familiar with these at the circuit level. If you put a positive voltage on

**Dave Jones:** the base, then you're going to get current flowing through your base emitter junction there. It's going to turn your transistor on and your output voltage here is going to go to 0 V. It's going to be pulled down. And if you

**Dave Jones:** don't have any base current, then it's going to go positive by nature of the pull-up resistor, the transistor's going to turn off. So, it's acting as a basic switch. And your MOSFET in particular, an enhancement mode MOSFET, which I

**Dave Jones:** might go into a different video on, if you put a positive voltage on the gate here, it's a voltage driven device as opposed to a current driven device in your BJT. So, they are physically different beasts. But if you put a

**Dave Jones:** positive voltage on your gate here, it does exactly the same thing. It turns your transistor on and your output voltage goes down. If you ground your gate like that, then by nature of that, you're going to turn your transistor off and your pull-up is

**Dave Jones:** going to take your output voltage high. It works like a switch exactly the same way as a BJT. But transistors can be also used as amplifiers as well. That's their other job. So, you can put your uh, wave in here and get a much bigger

**Dave Jones:** sine wave out here. There's actually amplification involved, power amplification, not just voltage amplification. You can do the same thing on your MOSFET as well, but you got to buy some, right? So, they can be used as switches or amplifiers, and there's

**Dave Jones:** different circuit configurations, which we won't go into. What we want to look at is the physics level side of it, how it actually works on the silicon itself. To do that, we're going to have to go to atoms. So, welcome to the world of

**Dave Jones:** atoms, and we won't go into deep detail, but it's just important to know what's happening here. Stick with me, not as complicated as you might think. Now, uh, transistors, of course, and silicon chips made out of, ironically, silicon,

**Dave Jones:** as the name suggests. But, and silicon is a semiconductor, but on its own, it's not very useful. It, it's not an insulator, it's not a conductor, and it doesn't conduct very well at all. It's pretty useless on its own. So, you have

**Dave Jones:** to do what's called doping the silicon, i.e., adding an impurity to it to make it more useful. And we can, uh, create two different types of, uh, doped silicon. We can create N-type and P-type. You've probably heard those

**Dave Jones:** before, NPN, PNP transistor, PN junction diode. That's what it stands for, N-type and P-type doped silicon. So, in a nutshell, pun intended, the outer shell, or the valence shell, of a silicon atom contains four electrons like that. And

**Dave Jones:** you can make, join up silicon atoms like this into a big matrix. They actually form a very nice big, uh, matrix, where potentially you can actually conduct current through. But, as I said, on their own, not very good. But, if you

**Dave Jones:** dope silicon with a little bit of phosphorus, phosphorus is very similar atom, but it's got five electrons in its outer shell. So, if we have a phosphorus atom in here, they actually join up and and fit into the silicon matrix very

**Dave Jones:** nice, except because it's got five electrons here, there's one free electron. Beauty, that electron is free to float wherever it wants throughout the matrix. So, bingo, we've got an extra electron that's free to go all the way through and conduct current with.

**Dave Jones:** But, we also need a matching type called N-type. So, what we can do is we can get the element boron, and we can dope the silicon material with a boron atom. A boron atom, very similar, but it contains only three electrons in its

**Dave Jones:** outer valence shell here. So, when it fits into the matrix of the silicon like this, it's doped in there, then there's three only three electrons like that instead of the five that we had here. So, four of them joined up, and we

**Dave Jones:** had one free. In this case, we've only got three, and there's what's called a hole left over. There's a space where there is no electron. So, we've actually created a free hole, and that hole is allowed is then also

**Dave Jones:** allowed to move throughout the matrix, and that's what we can use to conduct the current through a PN junction through a transistor. Let's take a look. Now, they call it N-type for negative because it's got a an electron in a free

**Dave Jones:** electron in there, and they ironically call P-type the positive type, but these names are a bit of a misnomer because the the material itself is still a neutral charge because it's got the same number of protons and neutrons

**Dave Jones:** in the atom itself. So, it's it's actually a neutral charge, but it's the hole, the free hole, that actually conducts the current through the material. So, a hole in a P-type uh here is just really the absence of an

**Dave Jones:** electron, but in semiconductor materials, you can think as of both the holes and the free electrons as being the charge carriers through the material as opposed to just a regular metal where it's pretty much just the electrons that

**Dave Jones:** are actually carrying the charge current. Semiconductors, uh it's a bit of a different story. I won't go into deep deep detail, but just think the holes can actually move as well and carry the charge current. So, let's first take a

**Dave Jones:** look at the BJT. Now, I've shown it stacked in this configuration. Actually, when you actually uh physically build up on a semiconductor in what's called a planar format, which is how I've shown this uh MOSFET here, when you physically

**Dave Jones:** build it up, it's actually physically tipped over, but it's easy to explain in this orientation. Stick with me. Now, we've got our base, our emitter, and our collector of our BJT transistor. And you'll notice in here it is, base,

**Dave Jones:** collector, emitter down here. And we've got two N-type materials here, which are what's called heavily doped uh we we saw before. So, very heavily doped material, so very low resistance, you can think of it that way. Now, uh then it's got a

**Dave Jones:** P-type uh doped material in here that's electrically connected to the base. And then on top of that, we've got uh sandwiched between uh our base P-type and our collector N-type is another N-type, but it's like lightly doped. And we'll see the reason

**Dave Jones:** for that in a minute. So, you can think of that lightly doped region, still N-type, but it's a bit higher resistance. So, there's a higher resistance layer and a lower resistance layer on top of it. Now, you'll notice

**Dave Jones:** that in a BJT transistor, we've just got a PN junction like that. Here's the two electrical contacts, P and N. It's exactly like a diode. That's why it's actually drawn like a diode there, and you can actually use a transistor as a

**Dave Jones:** regular PN junction diode. No problems at all. It functions the same way. And this is how it works. If we don't apply any voltage to the base here at all, we just put these two materials physically uh sandwich them together, then what we

**Dave Jones:** end up with is all the free electrons in the N-type material, they actually gather and fill the holes on that side, and then the holes from the P-type material, which we'll show as positive here, because the holes are effectively

**Dave Jones:** positive, right? Then they form on this side. So, the electrons and the holes naturally gravitate towards the barrier here, and they swap polarity effectively like that, forming what's called a depletion region. In this case, because it's the base-emitter, it's the

**Dave Jones:** base-emitter depletion region. And the depletion region is actually effectively just like a now a lack of any charge carriers. It's a barrier that stops any current flowing through your PN material from your base to your emitter. So, basically, nothing conducts if there's

**Dave Jones:** no positive voltage on the base here. And you're familiar with that in how your basic transistor circuits work. Now, of course, we come to our uh our our typical diode curve here, which you should be familiar with. Once

**Dave Jones:** we get to about 0.6 V is the threshold voltage, it doesn't conduct any current until we get to around about that point. And then, once we get above 0.6 V, it starts to rapidly conduct up like that. So, as the base-emitter voltage rises

**Dave Jones:** like this and goes up like this, uh the depletion region in here gets narrower and narrower and narrower until it flips back and overcomes the effectively like the threshold voltage here. Once it gets to 0.6 V, then it

**Dave Jones:** flips back, then we can start getting our electron flow. Here's our little electrons, they start flowing in that direction like that. Remember, electron flow goes from negative to positive. That's electron current flow as opposed to conventional current flow.

**Dave Jones:** So, that's our base-emitter junction. We haven't done anything with our collector yet, it's just been sitting there unconnected. Let's now connect it up. Or let's not actually. When it's unconnected, uh the same thing happens. We've got a P and an N junction here.

**Dave Jones:** Because it's lightly doped or heavily doped, it doesn't really matter. We get exactly the same thing here. We get our negative electrons there and our positive uh holes building up on this side, and we get a collector-base depletion

**Dave Jones:** region. Exactly the same thing. So, no current flows from collector to emitter cuz there's that depletion region. No current can flow through it. It's effectively stopping it. But, if our collector voltage here goes up and reaches a certain threshold,

**Dave Jones:** while our base-emitter is also um uh biased, then we get the depletion region getting depletion layer in collector-base getting smaller and smaller smaller, and and then it flips over and bingo, we can now get boom, electron flow from emitter through

**Dave Jones:** to your collector. Now, here's the magic of how a transistor works and how we get the current gain that we uh are used to. Like a small amount of base current here can lead to a large uh collector-emitter

**Dave Jones:** current here. So, it actually works as an amplifier. How does that work at the physics level? Well, let's take a look. Assume that our base is positively biased like that, our collector is now positively biased at some hot large uh voltage. Now, this is

**Dave Jones:** where our heavy and our light doped material comes in. The lightly doped material, cuz it's effectively higher resistance. So, because we've got a low-resistance material here and a higher-resistance material here, which is going to be a very thin layer, by the

**Dave Jones:** way. This lightly much thinner than what I've shown here. This is low resistance. This is effectively high resistance. So, the voltage between the collector and the base here, most of it is going to be dropped. There's going to be a higher

**Dave Jones:** voltage differential in this lightly-doped material, i.e. right in the region between the P and the lightly-doped N-type material. And because that has a high voltage threshold, something magical happens. And the magic goes like this. There's going to be holes that are

**Dave Jones:** So, holes are positive. They're going to be flowing through the P-type material in like this and electrons are going to be flowing the other way. It's going to be a small amount of current. But because this is so all this N-type

**Dave Jones:** material at the bottom is so heavily doped, it's got all these excess electrons, and there's only a few little holes flowing through like this when electrons flow from the N material. So, electrons flow from here up into here, there's millions of them, but

**Dave Jones:** there's only like a few of the holes coming over. So, where do the rest of all these excess electrons from this heavily-doped N-type material go? Well, they go bingo, straight up like that. Because this is a higher potential uh

**Dave Jones:** differential voltage in this region here, it attracts all of those electrons, those excess electrons. So, we've got a lot of electrons flowing from emitter to collector here, and it just a smaller amount of much fewer electrons flowing from emitter to base.

**Dave Jones:** So, bingo, that's how the magic happens inside a transistor, and you get current gain, a large amount of current uh from emitter to collector. Or if you want to think about it in conventional current terms, the current flows from collector

**Dave Jones:** down to emitter, and a small amount so a small amount of base current flowing in here and a super large amount of current flowing from collector through to emitter. And that's determined by the beta or the gain of the transistor. And

**Dave Jones:** that's how to And that gain is controlled by like all the physical construction of of the lightly doped material and how thin it is and all that sort of stuff, the physical construction inside the transistor. So, that's the

**Dave Jones:** magic of a bipolar junction transistor. Let's move on now to our MOSFET, in particular a MOSFET, not a JFET or and a depletion mode MOSFET, for example. This is going to be what's called an enhancement mode MOSFET. How it actually

**Dave Jones:** works. Now, it's physically constructed quite different and operates quite different. As I said, this one is a current-controlled device. You've got to actually feed some base current in. As you might know, a FET or a MOSFET, be it

**Dave Jones:** a J, whatever type of FET it is, is a basically a voltage-driven device. You put a voltage on the gate and you can get current to flow in the transistor. There is no effectively no gate current, a voltage-controlled device. So, the way

**Dave Jones:** the MOSFET works in what's called a planar form here, this is how it's physically constructed on the silicon. We've got a P-type substrate base. It's of course P-type doped. And then we've got our N-type doped. You can think of them as like a

**Dave Jones:** physical channel or whatever. It doesn't really matter how you physically think of them, but there's two N-type nodes here. So, the one is the source and one is the drain. And then we've got an insulator on top here. And that's usually like an

**Dave Jones:** oxide layer. There's a few different ways to do that, but just think of it like a complete insulating layer. That's why it's physically shown as, you know, there is no direct electrical connection between the gate and the drain or the

**Dave Jones:** source because it is completely insulated. And then on top of that, they've just got a metal contact which is your gate material and there's also a metal contact on the drain and the source n-type materials as well. So,

**Dave Jones:** apart from that physical difference of no electrical contact whatsoever, it kind of starts to work in a similar way. Let's have a look because we've got an n and a p-type material. If we've got nothing connect no voltages connected,

**Dave Jones:** the transistor's just sitting there, then exactly the same thing happens here. Our our electrons gather in this material and our holes from our p-type gather on the other side and we form our depletion region in there around both of those.

**Dave Jones:** So, obviously, if we've got two depletion layers here and here, then no current can flow from source to drain. I eat the transistor is switched off. There's no conduction at all. But, here's the magic of how it works and the name gives it away, field

**Dave Jones:** effect transistor. It works based on an electric field. Now, if we put a positive voltage on the gate here, it doesn't have to be very high like couple of volts depends on the type of transistor, then what we've done here is

**Dave Jones:** we've given it enough electric field here to overcome this barrier here, our depletion region barrier, and then we can have the electrons that were in the n-type material here that's heavily doped n-type material can actually flow along here because this whole gate is

**Dave Jones:** like the whole thing is directly across there between overlapping the two n-type materials, it forms a channel in there where the electrons can flow and bingo, we've turned on our switch based on just an electric field here. There is no

**Dave Jones:** current flowing in or out of the gate because of this oxide insulating here. So, it is a field effect device uh turned on and off by an electric field or a voltage on the gate. And naturally, the higher the gate voltage,

**Dave Jones:** the more you increase that gate voltage there, then the wider this channel becomes, and you can get more charge carriers flowing through, holes and electrons, and current flow from your source to your drain, like that. And your transistor turns on. Bingo. Very, very

**Dave Jones:** simple, but as I showed, it's physically a different type of operation to the uh BJT type uh transistor. And the because there is no gate current uh flowing in there, it's insulated, well, that's an usually an advantage in electronics.

**Dave Jones:** That's why MOSFETs are more popular than BJTs these days for most things. So, yeah, your iPhone or whatever, all your processing, all your digital switching, all that sort of stuff is all done with um effectively um enhancement mode

**Dave Jones:** MOSFETs, exactly like we see here. And here's an interesting little animation I got from Wikimedia Commons. You can see the graph on the left here, that's the uh gate voltage going up to 0.6 V. You can see the black marker, it

**Dave Jones:** starts off at zero there, goes up, and you can see the channel effectively turning on in this electron density map on the right-hand side. This is a 3D electron density map. It's awesome. I don't know how they actually uh got

**Dave Jones:** this, but it's fantastic. And you see, as it goes up and reaches a threshold voltage, in this case of about 0.45 uh V or thereabouts. This is a real low gate threshold voltage uh nanowire MOSFET, it's called. And you

**Dave Jones:** can see the electron channel then just like just sort of bang, there it goes. Fantastic. And of course, you keep increasing the uh gate voltage, as I said, then your uh conduction channel gets wider and wider, and more electrons

**Dave Jones:** can flow, higher current. And you may have heard that MOSFETs and CMOS devices, complementary metal oxide semiconductor transistors, they're susceptible to static electricity. If you touch the pins, you can zap them and destroy or damage the chip. How does

**Dave Jones:** that happen? Well, it's easy. This very thin insulating oxide layer in here, that's what gets damaged. If you come in with your finger and touch your gate in there, zap, you can zap straight through that insulator, actually blow a hole in

**Dave Jones:** that insulating layer, and that's going to ruin your day, really. And these insulating layers incredibly thin. We're talking like you know, nanometers, you know, kind of thickness in there with these things. Incredibly tiny. Now, you may have heard of Moore's law, of

**Dave Jones:** course, and how chips and transistors, these types of MOSFETs, which are used to build modern processors and modern chips, are getting smaller and smaller and smaller. A current process node node technology, you might have heard, for example, 20 nanometers. What does

**Dave Jones:** that mean? Well, it means the distance between here and here, this a channel in there, that is your 20 nanometers in there. What does that translate to? Well, a silicon atom is about 0.25 nanometers in diameter, effectively. So, there's effectively

**Dave Jones:** only 80 um atoms in there wide between there. So, you can see how ridiculously small feature sizes these are and how Moore's law, in as we traditionally think of it, is pretty much coming to an end. You know, you can't get much smaller before

**Dave Jones:** this doesn't become an insulator anymore. It doesn't become a barrier. The electrons will just jump across and they can tunnel through. You can get a little, you know, we get to the point where quantum effects and quantum tunneling comes into it. I won't go into

**Dave Jones:** the details of that, but yeah, we're really sort of pushing the limits of Moore's law. We can't physically make these much smaller before we run into lots of real major problems. And these distances in here and also the thickness

**Dave Jones:** of the oxide insulating layer in there determine your operating voltages of your FET. So, you may have heard of like a 20 V maximum FET for example. Well, that's going to be determined by your particular manufacturing technology inside the FET itself. That's going to

**Dave Jones:** determine your maximum operating voltages. So, there you go. That's how BJTs and MOSFETs work at the semiconductor level itself. And I hope I've explained that adequately. There are sort of many different ways to sort of explain this. You can go into real deep into the

**Dave Jones:** physics and the manufacturing technology of it. This is just a general overview good enough. If you know this, then you pretty much know how these trade and can appreciate how these transistors actually work on the silicon level. And

**Dave Jones:** I've only covered NPN and N-channel devices here, but you can think of PNPs and P-channel MOSFETs as being basically the opposite of what's here. It's It's not quite They do operate a bit differently. They have negative gate voltages for example, but but JFET

**Dave Jones:** N-types can have negative gate voltages well, and I can probably do a separate video on that, but there are physical differences and also operational and parametric differences between PNPs and P-channel and N-channel devices. So, but pretty much it's basically the

**Dave Jones:** opposite of what we got here. So, if you like Fundamentals Friday, please give it a big thumbs up on YouTube cuz that helps a lot. And if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** Links down below. Or leave YouTube comments or blog comments. Catch you next time.
