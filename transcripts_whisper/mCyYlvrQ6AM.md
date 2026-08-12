---
video_id: mCyYlvrQ6AM
title: EEVblog #1219 - Don't Trust Switches - Toy Repair
url: https://www.youtube.com/watch?v=mCyYlvrQ6AM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 15, "2": 26, "3": 45, "4": 67, "5": 84, "6": 99, "7": 115, "8": 133, "9": 154, "10": 174, "11": 189, "12": 204, "13": 224, "14": 239, "15": 258, "16": 278, "17": 293, "18": 319, "19": 334, "20": 356, "21": 377, "22": 398, "23": 416, "24": 437, "25": 457, "26": 473, "27": 489, "28": 512, "29": 532, "30": 550, "31": 569}
---

**Dave Jones:** Hi, just a little home repair video I thought I'd show you. Yes, I am still sick as a dog, absolutely terrible, can't do anything. But I am looking at this, and this is one of Sagan's toys. It's one of these speed pipe things.

**Dave Jones:** It's like a little remote control car that goes through these pipes, these tubes that you can click together in different configurations to make them do loops and corners and all sorts of stuff. Kind of reminds me of the Running Man, if you've seen the Running Man.

**Dave Jones:** If you haven't, you must watch the Running Man. Classic Arnie. Check out this case. I thought this was rather interesting. This, look, it's got a PCB pattern on the back of that. I don't think that's a legit pattern, of course. It's one of those fakey fake ones.

**Dave Jones:** But anyway, yeah, it's just got controls like forward and reverse controls, and that's basically it. And it's an infrared thing because the, it's not RF, none of that RF rubbish. Because the tubes are clear, so they can see through. So the little self-contained battery-powered car inside the tubes obviously receives the IR signal telling it where to go.

**Dave Jones:** So, sorry, I've only got my Sony RX100 camera here, so I don't have a good macro lens. But anyway, Sagan was complaining that he thought that Huxley had buggered this. It's obviously like a channel switch, because you can have like two of these in the same tube, like trying to race and catch each other.

**Dave Jones:** And he said that... Uh, Huxley had somehow busted it, and he couldn't move the switch anymore from A to B. And that's why it wasn't working. And one of the, uh, and sure enough, I, like, tried that, and it, and it couldn't, I couldn't budge that switch.

**Dave Jones:** And, you know, I got the knife in there, and, and it just, it didn't make sense at all. And then, I took the first, one of the first things to do is look at the visual cues on here. And you might be able to see that that plastic is a bit deformed.

**Dave Jones:** And melted. Aha! So the next thing you do is give it a bit of a sniff. And, yep, it's got that classic burnt electronics, uh, smell. So something has shorted out. So I opened it up, and sure enough, so I'm going to try and hold the camera with one hand.

**Dave Jones:** And you might be able to see that those wires have shorted together. Not only were the two wires shorted together coming from the battery terminals, but then the black wire. Was also shorted to the back side of the switch, down in there. Sorry, it's hard to show you that, but it was also shorted right down in there.

**Dave Jones:** You might be able to see, I can't get any closer without a good macro lens. So the batteries were completely shorted. So what sparked that, no pun intended, not that you would have gotten a spark, really, um, but anyway, um, yeah, what, like, obviously, the current directly from the batteries, it was shorting them out, and that, and that melted all the water.

**Dave Jones:** All the wires, and it melted to the side of the switch, and you can probably see the switch down in there, is all, is all melted. That AB switch. So yeah, it heated all this up to buggery. Uh, did it short out inside the switch?

**Dave Jones:** Because usually the wires are, you know, pretty good insulation on them. Um, so really, like, of course, one of them could have had a nick, but then, well, the other one would have had to have a nick in the same spot. So that switch is heated up, obviously.

**Dave Jones:** The, uh, the metal body of the switch, and that's melted all the plastic all, all around there on the, on the actual, uh, lever of the switch, the sliding lever there. And then it just melted the wires together as well, and I had to, had to pry those apart, had to get the knife right in there and, and really chop those, really chop those out.

**Dave Jones:** I just had a really hard time separating them, actually, so. So you should be able to see that exposed negative wire there, and how all the insulation is just completely... Just completely melted off that, and then melted into the side of the switch housing.

**Dave Jones:** So ordinarily, the, those switch housings aren't actually electrically connected to one of the, uh, terminals, one of the switch contacts. So they're just floating, um, unless you, uh, on the PCB layer, you put the pins in there. So let's get, wow, check out that switch.

**Dave Jones:** The, the lever contact on there is completely melted off. Embedded itself in the actual, um, in the, these, uh, switch, you know, the top, uh, cap. That is unbelievable. This could have got massively hot. Of course, there's a lot of energy in two, uh, AA batteries.

**Dave Jones:** So, yeah, um, you, you short them out, and, uh, that can, that can really heat up and ruin your day. So, what's going on here? Let's have, I don't know, let's have a look at the, oh, yeah, it all just fell off. Wow, look at that.

**Dave Jones:** let's have a look at the bottom here, aha, yes, the, there you go, the outer, it is electrically connected, so that's what's happened, you can see that the, the two contacts on the two outer pins there, are the electrical contacts for the case of the switch, and obviously, the ground terminal,

**Dave Jones:** oh, yeah, so it's actually grounded, no, so it's negative, so if the ground terminal, yeah, you have to strip the wire to solder it in, so if that made contact with the outer metal case, that shouldn't, that really shouldn't have mattered, what's the chip on there, can't see it, sorry, maybe those

**Dave Jones:** playing along at home can pull the part number off that from a HD screen, so they've electrically connected the case of that switch, so what, so it could have, it could have been an internal contact short, in the switch, would be my guess, because the white wire is sold, you know, is, is significantly

**Dave Jones:** away from that, so obviously, once they, it may be shorted out inside the switch, and then, yeah, I, I would say that's the deal, oh, is the, because really, they aren't power contacts, that's not the power switch, that's the AB signal switch, so it's all logic level stuff, so even if it's shorted out

**Dave Jones:** inside there, you know, the path would have to be through the chip to short out the battery, so that doesn't make sense, oh, power, no, okay, no, no, no, there it is, sorry, I can see it, yeah, it comes from the power switch over here, yes, okay, so the power switch, yep, yep, so that

**Dave Jones:** second pin over there is power, yep, so obviously, that's where it's shorted out, that comes from the power switch over here, aha, there you go, so that's the power switch, and then, yeah, so it's, in all likelihood, chip's okay, and it's just shorted out the battery, so if I clean that up

**Dave Jones:** and just, I don't know, put a new switch in, or, no, I'll just permanently wire it, because we've only got one of the things, so I'll just permanently wire it to channel B, and so I just desolder the switch, I guess, and cleaned all up, and that, hopefully, will work again, hmm,

**Dave Jones:** yeah, I'm not sure if you can see that, but I can certainly see that inside that switch, those contacts are toast, so, yeah, the shorts actually definitely happen inside the switch, and it has to be, that's the obvious conclusion, based on the fact that the power comes in here,

**Dave Jones:** there we go, there's the positive, goes down to the switch, comes out of the switch, goes up that trace there, sorry for my crude finger pointing, goes to the second contact, so that second contact, has shorted out to the external case, which they decided to ground instead of float,

**Dave Jones:** and there's no electrical reason to do that, so you could maybe blame the, I don't know, do you blame the PCB layout person, or do you blame the original designer who specified that, I wonder if that's specified on the schematic, whether or not they showed that those pins were

**Dave Jones:** electrically connected to ground or not, there was no, you know, there's no, like, EMC reason to do it or anything like that, so, yeah, hmm, you're reliant upon the reliability of that switch to prevent shorts. Anyway, I think that's a rather interesting fault, and it can show you how you can really come aguts

**Dave Jones:** by relying on one of these cheap-ass switches they obviously got from whoever was cheapest at the Shenzhen market that day, when they were making this, and it must have shorted out inside, you know, all it takes is a little, you know, a little solder ball, or some other little flake of

**Dave Jones:** anything, or maybe it's just a badly designed switch, and they've completely come aguts, and that's shorted out the batteries, unbelievable, probably the last fault I would have expected in such a product, so if you've seen a similar sort of power, well, in this case, it's a signal

**Dave Jones:** switch, it either, there's a pin on the micro here that obviously either connects directly to ground on this side, or to power on this side, and it doesn't do it through a resistor, through a protection resistor, so it, obviously, if you get a short with inside the switch, it's going to ruin

**Dave Jones:** your day. Anyway, let us know if you've seen something similar in a product. I hope you liked it. Catch you next time.
