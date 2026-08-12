---
video_id: S0TZMivVzVk
title: EEVblog #16 - CMOS SCR Latchup Tutorial
url: https://www.youtube.com/watch?v=S0TZMivVzVk
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 36, "3": 61, "4": 88, "5": 97, "6": 107, "7": 128, "8": 141, "9": 154, "10": 173, "11": 184, "12": 203, "13": 215, "14": 237, "15": 249, "16": 264, "17": 276, "18": 293, "19": 306, "20": 328, "21": 346, "22": 357, "23": 370, "24": 385, "25": 403, "26": 420, "27": 436, "28": 453, "29": 468, "30": 486, "31": 501, "32": 512, "33": 534, "34": 541, "35": 559, "36": 570, "37": 584}
---

**Dave Jones:** Welcome to the AEV blog. I'm your host, Dave Jones, and this is episode number 16. I'm going to talk about a major problem in electronics design that you've almost certainly come across, you know, given enough time, but you may not be aware of exactly what's happening or exactly what the actual process is.

**Dave Jones:** And it's to do with every almost every CMOS chip on the market. And it's called the problem the issue is called SCR latch-up or simply latch-up or CMOS latch-up.

**Dave Jones:** It goes under various names, but you know, we'll call it SCR latch-up. And it's a real issue and a real trap for young players. Now, what SCR latch-up is is it is an inherent problem in the actual construction of all almost all CMOS devices.

**Dave Jones:** And well, you know, practically most chips on the market these days are CMOS in in some way, shape, or form. So, it's a it's a real issue. And what SCR latch-up can do is it's a is it's a fault condition that can actually short out your power rail within your chip a where parasitic transistors inside your CMOS device between the power rails actually short out.

**Dave Jones:** So, a transistor at the top transistor down the bottom, they short out and it shorts out your power rail. And it will latch like that, hence the name, like an SCR.

**Dave Jones:** It latches up. These two transistors latch on and it'll short out your power rail. And in a lot of cases, it'll destroy your chip. There are many causes for SCR latch-up.

**Dave Jones:** It can be that you're simply over driving the inputs or the outputs. You're actually forcing them above or below the power rails, and that can actually cause it. Or another thing which can cause it is bad grounding technique on your actual circuit design.

**Dave Jones:** And another major cause can be hot plugging. If you plug in your chip or plug in a board or something like that into a circuit that's already powered, then that can cause latch-up, too.

**Dave Jones:** Now, I'm going to actually attempt to explain what how SCR latch-up actually works and what's actually happening inside the chip. Now, I know it looks a bit complex, but stay with me.

**Dave Jones:** It's not that bad. It actually comes down to a pretty simplistic thing in the end. Now, this top half here, what this represents is it actually represents the physical construction of the CMOS die, the actual CMOS wafer, and this is the substrate material, right?

**Dave Jones:** This is the top of the actual silicon, and this is the substrate material, and these here are the input and output um FET circuits etched onto the device, okay?

**Dave Jones:** Now, these uh work normally. These are the actual here, these are the actual FETs which actually form the circuitry of the chip. But what can actually happen, well, what actually does happen in CMOS devices is that due to parasitic effects.

**Dave Jones:** Now, this is what SCR latch-up is all about. It's about parasitic effects. These um transistors and and resistances I'm going to explain here, they're not actually designed into the chip.

**Dave Jones:** They're just a byproduct of the CMOS manufacturing process, an unwanted byproduct which is very difficult to avoid. So, that's why most CMOS chips are going to have this parasitic circuit in here, and it's to do with the um the you know it's to do with the physics of actually constructing the device.

**Dave Jones:** So I won't go too much into that because you know you have to sort of know about CMOS construction techniques and things like that. I'm sure you can look up lots of references if you're really interested.

**Dave Jones:** But what happens is this there's a parasitic circuit which forms in the substrate material here. And what it is is it's effectively two transistors like this and some bulk uh resistance like this.

**Dave Jones:** You've got two bulk resistors, two transistors, we'll call them Q1 and Q2 and they actually form like this. I won't explain the detail here. It's going to be more it's going to be clearer down here in a sec.

**Dave Jones:** But these form a parasitic circuit between ground as you can see ground over here and your positive supply rail we'll call V+. Okay? Now this is all happening inside the silicon substrate material.

**Dave Jones:** It's really got nothing to do with the circuit design which is on top here. So it's pretty much irrelevant about what type of chip or circuit it actually is and this can be the input or the output circuit.

**Dave Jones:** So these are input or output FETs. And this substrate circuit here becomes an equivalent circuit if you tidy it up, an equivalent circuit that looks like this and you've got two transistors here like this and your power supply rail V+ and ground.

**Dave Jones:** Now I'll explain how SCR latchup actually works. Now if this circuit here actually looks kind of familiar to you it well it should because it looks exactly like an SCR silicon controlled rectifier.

**Dave Jones:** Right? It looks It's It's effectively exactly the same circuit. Okay? But, it's the same It's an SCR connected between your power rails. And that's why it's called SCR latch-up.

**Dave Jones:** Because in an SCR, once you Once you trigger the gate, this thing latches on. And if you've got an SCR between your positive and negative power rails, you know, bang.

**Dave Jones:** You know? You've got a real problem on your hands. So, this is how it actually works. If you take one of your your input or your output here, let's say you take this P input above this power rail, okay?

**Dave Jones:** You You know, this power rail might be 5 V, and if you take this input here one diode drop above this power rail, so once this input gets to greater than 5.6 V, then this transistor will trigger via this resistor here.

**Dave Jones:** Okay? It'll go through here and through this bulk resistance R1. And that will turn on this transistor. And once this transistor Q1 turns on, bingo. It will uh turn on Q2 as well.

**Dave Jones:** And that's it. That's all that happens if this input goes above this power rail by 0.6 this transistor latches on and this one latches on and bingo, the whole thing's latched and you've got current from V+ through to ground.

**Dave Jones:** And that's it. SCR latch-up. And it can also happen with uh the other input. If you take it below ground by, once again, 0.6 V, then this transistor will latch on through R2 here.

**Dave Jones:** It will actually latch on. And once Q2 is turned on, um sorry, it won't latch on. It'll turn on. So, once Q2 is turned on, then that will in turn turn Q1 on.

**Dave Jones:** And bingo, it'll latch like that. So, if your input or output of your um CMOS device goes above the power rail by 0.6 or more volts um thereabouts, then you're going to get SCR latchup.

**Dave Jones:** And it can ruin your day. That's a real pain in the butt. And that's how it works. So, how do you prevent SCR latchup? I'm glad you asked. I've got a list of things you can do to help prevent it.

**Dave Jones:** First one, proper grounding. Make sure you have use proper star grounding techniques and you know, just proper grounding. But that's probably a an whole blog in itself. Proper decoupling.

**Dave Jones:** Make sure you decouple your chips properly. Otherwise, that can cause SCR latchup issues, too. Um three, you can current limit your power supply. If uh you can put a series resistor in in series with your um the power supply of your chip, and that won't prevent SCR latchup, but it will prevent you actually destroying the chip from excess current.

**Dave Jones:** Um but that has an issue um for high frequency performance. So, it's really only for low frequency or DC parts like a DC op amp or something like that.

**Dave Jones:** Um and the fourth one is the traditional uh actual approach is um clamping diodes. You use clamping diodes on your input with an input series resistor, and that will clamp your input to um not more than 0.6 volts, so you can't get SCR latchup.

**Dave Jones:** And also, you should clamp the um outputs of the device as well, especially if you're driving inductive loads. Um inductive loads are a real problem, so uh make sure you clamp the outputs.

**Dave Jones:** And that's how you prevent SCR latchup. So, I hope you learned something with that. You know, SCR latch-up is a real trap for young players, and it's important to design your stuff properly to prevent SCR latch-up.

**Dave Jones:** If you want really rugged designs that actually, you know, actually don't blow up in the field or blow up in the lab even. Just remember it. SCR latch-up. Keep it in mind next time you're designing stuff.
