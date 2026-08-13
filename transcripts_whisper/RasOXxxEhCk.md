---
video_id: RasOXxxEhCk
title: Jackery Battery Bank FAIL Investigation - Part 1
url: https://www.youtube.com/watch?v=RasOXxxEhCk
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 35, "3": 45, "4": 65, "5": 81, "6": 101, "7": 116, "8": 136, "9": 152, "10": 167, "11": 187, "12": 197, "13": 212, "14": 233, "15": 253, "16": 273, "17": 304, "18": 319, "19": 334, "20": 354, "21": 374, "22": 395, "23": 410, "24": 425, "25": 445, "26": 460, "27": 481, "28": 506, "29": 526, "30": 546, "31": 566, "32": 587, "33": 607, "34": 632, "35": 647, "36": 668, "37": 688, "38": 703, "39": 724, "40": 744, "41": 759, "42": 780, "43": 795, "44": 810, "45": 841, "46": 856, "47": 876, "48": 891, "49": 911, "50": 932, "51": 942, "52": 962, "53": 977, "54": 997}
---

**Dave Jones:** Hi, just a quick video. I've got a battery bank here that's failed. It's a Jackery Joby, so they're supposed to be a decent brand. And I've had no problems with it until recently. It's got power delivery output, so I use it for, you know, little portable soldering irons and all sorts of other power delivery

**Dave Jones:** stuff. And so that's in and out, so you charge it through there. It's also got standard USB output as well. And there you go, there's the various specs for those playing along at home. And it's just died. So this is the 260 PD model.

**Dave Jones:** Probably quite a few years old now, but you know, it's not absolutely ancient. I use it for, I've got Velcro on the back, so this actually attaches to the Velcro on my tripod so that I can power stuff out in the field and things like that.

**Dave Jones:** And there's 4 LEDs in there, and it does not have any charge, and it will not accept any charge, and it will not do anything. So I'm going to crack it open. Let's go. I assume that the panels come off somehow. So start at the arse end.

**Dave Jones:** No, maybe not start at the arse end. Let's start at this end perhaps. There we go. Whoa, hello. Already lost a bit of my spudger. Yeah, it doesn't like that at all. Alright. It's going to be a fight. No, there's definitely more to it than that.

**Dave Jones:** Alright, going to have to get a bit medieval on its arse. I can see it, it's thin. I actually saw daylight. Oh, it's pretty close. Alright, there's clips and stuff. It may not come out intact. There's got to be a trick to it, right?

**Dave Jones:** Did these all the time. You would have it down pat, but no. Just a pro tip, you do want to use a plastic spudger for these because you don't want to go inserting a metal spudger inside a power bank. Probably not a good idea.

**Dave Jones:** Yeah, I don't know. I might have to get a stiff metal. That's what she said. Seriously, I'm like right in there. It's just like plastic clips, you can see them. But you've got to like do them all at once. Do I have to pry both sides

**Dave Jones:** at once? I wouldn't have thought so. So it looks like the bottom side there doesn't have, like the plastic goes in further than the top side. Oh man. Really have to get medieval on its arse in a minute. Because this is just ridiculous.

**Dave Jones:** I can understand that these things have to be robust because they get, you know, thrown around in packs and what not. Hey! Okay, that was it. You really had to get leverage in there. Wow. I didn't break it though. I didn't break it.

**Dave Jones:** Look, you can see an inductor in there. It's got some snot on it. And I assume that yeah, there's more plastic on the bottom. So this isn't, it's not going to slide out really. There's a thermistor down there. It's going off. So that's measuring the pack temperature.

**Dave Jones:** Yeah, this is supposed to be a decent brand, Jackery. So I'm a bit disappointed that it's failed. I think I paid a reasonable amount of coin for it. So that's the bottom of the PCB. So they've got the leads on the bottom of the board.

**Dave Jones:** Oh, okay. Right, yeah, look, look, they've got a hook. Really annoying. But I thought I, like, got past, yeah, no, you've got to get past those. You've got to, yeah, okay. So there's no clips on the bottom. It's just those two clips on the top.

**Dave Jones:** Right, I think now with that knowledge, I would be able to do this better now. So once you know, you know. But there's some sort of like, they put like celastic or something at the end of it? But once again, that would have snapped by now.

**Dave Jones:** I need one of those old school medieval stretching racks. It's almost as if there's like celastic in there holding it back. Like, because it's stretching, like, and then there's something that pulls it back. Oh, hello, got it. Yeah, there you go. Pliers for the win.

**Dave Jones:** Here we go. Ta-da. And no, there's no celastic. Really? Looks pretty good. A, it has the correct number of cells in there, and they're probably good. They're probably good cells. Let's have a look. Look, see, can we see the, can we see a brand?

**Dave Jones:** ICR 18650. Okay, here we go. They've got a, an EVE is the brand, by the looks of it. And that's the data sheet. So energy very endure. Energy very endure. I love my energy to endure. So they're the cells used inside 26V. Yep, yep, so that's exactly what we've got here, as you can see, 26V.

**Dave Jones:** Alright, so let's measure. Are they in series or parallel? Because, yeah, like the K8 wire goes over to here, so that doesn't make much sense, and it looks like that's connected to that. So it looks like they might, they're at least, I can see a bar going across there.

**Dave Jones:** Can I see? Yeah, I can see one going across there. Yeah, I think they're all in parallel. Got a boost converter in here, obviously, to get up to 5 volts and the power delivery and everything else. 3.58! That's bang on! That's basically an operating, nominal operating voltage of a lithium-ion cell.

**Dave Jones:** I can get down there. I can measure that and that. It's exactly the same. Something has died in the ass here. Can we see any obvious failures? Any blowholes? MOSFET-y action down there. Let's look at, I mean, you know, it could be a dodgy, dodgy joint on there.

**Dave Jones:** Connector. That looks pretty clean, doesn't it? Yeah, that looks pretty okay, doesn't it? Can't see what chip it uses down in there. Okay. Got some current shunt resistors there. They look fine. Everything looks fine. Like, so yeah, that'd be for current sensing of the,

**Dave Jones:** because here's from the battery, right? Two parallel 10 milliampere resistors. So I was at 5 milliohms, and, oh, so I was an inductor. Can we see a chippy number down there? But everything looks okay, doesn't it? An SW6124. It's a total solution for power delivery

**Dave Jones:** for bi-directional fast-charge power bank. It's a highly integrated power management IC. It integrates 4 amp switching charger, 18 watt, yeah, which matches the spec of this. Synchronous boost. It's got power delivery and all the, and quick charge and all the requisite standards. Fuel gauge and power controller.

**Dave Jones:** It's simple, so it does, it even does those lead readouts. Probably got, like, 4 lead outputs or something. Yeah, turnkey for high efficiency. So, yeah, if you're designing a battery pack, this is exactly what you get. So yeah, it does the business, and there is the internal.

**Dave Jones:** So, yeah, we've got the external. FET, which we saw in there, didn't we? So we saw some FETs in there. Yeah, as I said, they've got the 4 pins there for the lead, lead, so 5. They're only integrating 4 here. It's got a flashlight.

**Dave Jones:** So yeah, basically, there it is, about 5 milliohms. There we go, we saw the 5 milliohms, the 2 10 milliohms in parallel there. So the battery goes in there, it's, yeah. Okay, we've got the big-ass external inductor, and Bob's your uncle. So these are going to be battery protection.

**Dave Jones:** So they're in the low side, the battery there. Saw those in a recent tear-down, or no, a recent repair, like answering a Twitter question. So one of those kinds of things. And yeah, that's about it. So that's it. So, you know, it could be, like, those gone, or something.

**Dave Jones:** They're in parallel. I don't know why they have 2 of them. Well, obviously, for the current power capability. But yeah, so who knows, right? What's an ME-F7? I don't know. That 8205A there looks like a MOSFET? Like you can tell by the, you know, the, you know, the, you know,

**Dave Jones:** large pins in there, and yeah, there's not much else doing. There you go. Bob's your uncle. JSCJ, or JCET, take your pick. Jiangzhou Jingjing Electronics Co. It's a dual jobbie. That's why that was, we were showing over here that, yeah, 2 of them.

**Dave Jones:** So that's all making sense. And there doesn't look to be any issues there at all. So does anyone want to hazard a guess as to where the fault lies? I have to feed in some external voltage and start seeing if it gets through or not.

**Dave Jones:** My PCB's coming gutsy here. Look at that. She's a bit, a bit janky. So, yeah, put that back down. No whackers. And external battery bank. It's not even staying on. So, presumably, there's nothing getting in there. PC doesn't get any blub blub blub when I plug it in.

**Dave Jones:** LED display over there. So anyway, there should be voltage going into that now. Okay, so we've got ourselves 3.58. Well, it might be coming to guts her because our battery negative there is on the other side. So let's take, do we have a convenient ground?

**Dave Jones:** We'll just take this ground point here, shall we? So that's our input ground, our input reference. So input referred, as you'd call it. 5 volts. There you go. No whackers. So we've got our 5 volt in. And in relation to that, we've got 4.3 volts out.

**Dave Jones:** There you go. So, that 4.3 volts should be enough to do the business. So, it's not easy to probe stuff under there to get the oscilloscope, like physically, get the oscilloscope probe under there and stuff, because this inductor's not gonna, she's not gonna

**Dave Jones:** bend out easily. I think the likely culprit here is this battery protection. It's not like, I don't think, sorry, I'm probably not gonna be able to repair this because like, I'm not gonna be able, I'm not gonna like, well, I might. If I can find out what that part is,

**Dave Jones:** I could order it, I guess. But, right off the bat, I'd be guessing that they are going to be able to repair this. So, right off the bat, I'd be guessing that they have failed. Now, there is a chance that if I actually

**Dave Jones:** disconnect the battery and reconnect, like, it might be in some like latch-up state, or something like that. So that's actually worth a shot, I think. Without, you know, going deeper, I'd say physically, let's just physically remove the power from the battery, and we can do that conveniently

**Dave Jones:** with the terminal up here. So if we physically remove the voltage from the thing, I would, I'd be tempted to do that first, just to see if we can give it a kick in the pants. It might be in some latch-up state that's just, these

**Dave Jones:** protection devices have kicked in and they go, we don't want a bar of it. But they're not faulty. Well, you know, they haven't failed. And, yeah, so let's go in there, wet my sponge, that's what she said. Alright, so let's melt that, there we go.

**Dave Jones:** And, let's put it back, see if that made a difference. No. External, no. That didn't help, but that was worth a shot. Okay, so I'm not having any luck on the ME-F7 with battery protection or anything like that. Yeah, so they're a 6-pin wide-body

**Dave Jones:** jobby, so maybe you can do some parametric search for package, or something like that. Because, you know, when you've got a rather unusual package like that, you might be able to narrow it down that way. So, I'm on the digi-keys here. Multifunction, battery protection,

**Dave Jones:** 2400 of them. Can we search for package? 6-pin power WD-FN shift highlight, all the 6-pin jobbies. Let's see what we've got here. Well, it doesn't look like it's that, so we can go back and have a look, right? So it's actually got two, like, the separate pins on each side, it's not one wide pin.

**Dave Jones:** Okay, so you can rule that out. You want the wide pin, Although, you know, the same device could be available in multiple packages, of course. Then, it might not be available on your digi-keys. You might have to search your LCSCs or something else.

**Dave Jones:** So, and then you've got to assume that they've got the right photo and, you know, like, everything else. All the traps for young players of trying to find stuff like this. Yeah, nah, that's not gonna work. Yeah, they all seem to like that wide pin, don't they?

**Dave Jones:** Seems to be all the rage with the kiddies. And we get into the ones that don't have a photo. So, yeah, I'd say that's a WFDN, which is wide format DFN package. We can go for DFN6 on LCSC. There's lots of them. And they do actually have the chip size on there, so that's pretty handy.

**Dave Jones:** There you go, like, we've got wide jobbies, something like that. So, unfortunately, the markings on top are the problem, right? So, unless you can luck upon that, I don't think you'll find it in, like, a decoder or something like that. I mean, let's just choose this random one.

**Dave Jones:** Let's just choose this random jobbie here. You know, thermal pad on the bottom, six pins, right? If we go back over, okay, yeah, the two at the top, right? So that's a standard pinout. So there's probably a whole bunch of them like that, and that's the internal

**Dave Jones:** diagram for those playing along at home. Anyway, our problem here is that let's go back to the videotape, and I'll probably just We know the cells are good, okay? So I'm going to, I've had this left off for a while. Let me just reconnect that in there.

**Dave Jones:** So the problem is, like, these MOSFETs should be on under, like, all regular circumstances, because it's a cell protection device designed to protect cells. So they will, so the MOSFET will open in case of, you know, any sort of issue with the cells.

**Dave Jones:** We know the cell voltage is good, right? So if we actually measure the voltage across there, and we've got 3.5, which is the they're open, right? They're, well, it's going to measure exactly the same. They're open. So, looks like our MOSFETs have opened up.

**Dave Jones:** And they're doing their job of protecting the cell, protecting the cell from what? I don't know. The cell is fully charged. So, unless we can figure out I'm going to call it quits there for today. I just wanted to make this a quick video.

**Dave Jones:** Can somebody please, you know, you might be able to put any, like, generic equivalent in there, perhaps? You know, should be able to, I guess, right? Can, yeah, leave it in the comments down below if you know what those jobbies there are, because they have a lot of experience

**Dave Jones:** And leave your thoughts and comments down below about anything else, if you've spotted anything, but I can't spot anything. And we get, you know, we feed in 5 volts, we get it in, it goes through the MOSFET there. So, you know, assuming the control is good.

**Dave Jones:** It should, the cell's fully charged, which, yeah, last time I used it I left it in the fully charged state. So, yeah, it should be fine. Anyway, there you go, quick second channel video. Thoughts and comments down below, please. And maybe I could do a second video replacing that, once I have some

**Dave Jones:** further info. Anyway, hope you found that interesting. Catch you next time.
