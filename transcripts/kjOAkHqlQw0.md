---
video_id: kjOAkHqlQw0
title: EEVblog 1614 - Circuit Design TIP: Crystal Oscillators
url: https://www.youtube.com/watch?v=kjOAkHqlQw0
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 23, "3": 31, "4": 44, "5": 60, "6": 72, "7": 85, "8": 95, "9": 114, "10": 125, "11": 136, "12": 145, "13": 154, "14": 163, "15": 181, "16": 190, "17": 201, "18": 218, "19": 228, "20": 237, "21": 249, "22": 258, "23": 268, "24": 283, "25": 303, "26": 313, "27": 326, "28": 336, "29": 347, "30": 364, "31": 375, "32": 389, "33": 401, "34": 418, "35": 429, "36": 439, "37": 451, "38": 467, "39": 474}
---

**Dave Jones:** Hi, just a quick circuit design tip. Thank you very much to uh Cyber City uh Circuits for actually prompting this one. He started a discussion on uh Twitter. I'll link it in down below, but that's what prompted this.

**Dave Jones:** So, as you probably know, any active chip needs some sort of oscillator to actually run it, and you get that from a crystal like this, either just an individual crystal or from an external crystal oscillator.

**Dave Jones:** But, it's very common for of course microcontrollers or any sort of chip. In this particular case, we've got DTMF uh tone generator, but it doesn't matter. It's just an example.

**Dave Jones:** Um they've got two crystal pins, X1 and X2 here, where you connect your two-pin crystal. It can be an HC49 package like this, either SMD or through-hole. It can be the larger uh size uh HC as well.

**Dave Jones:** And you've also, no doubt, know that you usually have to add two load capacitors on here, onto the one onto the X2, one onto the X1 pin. And that can actually be quite annoying cuz technically, you can't just whack a uh value in there.

**Dave Jones:** It might work, but technically, you should actually calculate those values based on the particular crystal that you're using and the load resistor value cuz sometimes uh like old-school circuits, they didn't have a load resistor built in.

**Dave Jones:** We'll see that in a minute. Uh this particular one uh does, but old-school circuits might actually have a typically a 10 meg resistor across there. So, this is actually quite a high impedance circuit.

**Dave Jones:** And like a parasitic capacitance around the circuit can be a problem as well. If you get leakage on the board, contamination, uh grime, dirt, and dust, all sorts of things.

**Dave Jones:** And if you don't calculate these capacitor values properly, you might find that uh it works in your prototype circuit, but when you get into production with temperature and other uh you know, lots of other variations, especially if you're changing like the source of your crystal, for example, you're purchasing a part and oh yeah, I'll get this uh 3 4 MHz crystal, no worries.

**Dave Jones:** I'll just get it from the uh cheapest source possible. It might have different characteristics which throw out your low capacitor values and might find that your circuit doesn't oscillate as well as you intended.

**Dave Jones:** Here's an experiment you can do at home. Use your oscilloscope with a switchable times one probe, put it on your times one probe and try and probe your X1 pin here.

**Dave Jones:** See how you go. So, adding an oscillator like this to your do dad is common as mud. Now, of course, this can have some issues. You've got three components, right?

**Dave Jones:** These components take up board space. You know, these aren't small. For example, the capacitors you can make them really small, but you know, you're usually you're using bigger parts and they all take up room.

**Dave Jones:** And as I said, because it's a high impedance circuit, you got to have some clearance around there. You can't just run high frequency signals willy-nilly, you know, near your X1 line here, for example.

**Dave Jones:** You might come a gutser. And that's why sometimes you might actually even see a guard trace circuit going from ground around these pins so that it stops leakage into this high impedance, you know, relatively unstable I'm here all week circuit.

**Dave Jones:** But what if I told you that practically any chip that has these two crystal pins on it, you don't have to use just an external crystal with the low capacitors.

**Dave Jones:** You can actually replace this circuit with an external dedicated crystal oscillator. Or, if you happen to have the frequency available from some other part of your circuit, you can use that, too.

**Dave Jones:** Bonus. You're now down to one bill of materials item. Usually more expensive, granted, but hey, it might save you some PCB footprint space, it might save you some design headaches because you're buying an already dedicated and characterized and working crystal oscillator.

**Dave Jones:** And of course, they come in all flavors and varieties, but you can get them really small. Look at this, 2 mm by 1.6 mm. Oh, crikey, right? Absolutely tiny stuff.

**Dave Jones:** Yeah, they might be more expensive, but they're pretty schmick. So, how does this magic work? I hear you ask. Well, here's the particular uh chip in question, but it doesn't matter.

**Dave Jones:** All chips with the X1 and X2 crystal pins work basically the same way. This just happens to be a DTF uh tone generator uh chip, really old school stuff, and it's got the internal crystal resonator oscillator.

**Dave Jones:** It's actually got the oscillator circuit built in. And if we scroll down the data sheet, they actually show you the internal circuit for this. So, here's how it works.

**Dave Jones:** As I said, almost every chip with X1 and X2 crystal uh pins is going to work the same way. They have an internal inverter like this connected between the X1 and the X2 pins.

**Dave Jones:** So, what does that make X1? It makes it a digital input. Aha! You can just shove your crystal oscillator or any other uh signal you can get from anywhere else in your circuit that you can generate, you can just shove that straight into X1.

**Dave Jones:** No worries. And this X2 pin is usually uh just goes off internally inside your chip and powers whatever circuitry inside your chip, powers your microcontroller or whatever. So, X2 isn't actual digital output pin, and you can actually use that uh to drive other external circuitries.

**Dave Jones:** In fact, it's an inverted signal from your X1. So, if you just happen to need an inverted uh clock for somewhere else in your circuit, you can actually pick that off X2.

**Dave Jones:** Just uh be careful of any load uh requirements on there, but usually it can drive something. Now, there are actually some chips that will actually have the load capacitors actually built in, and you don't actually need them externally.

**Dave Jones:** In this particular case, it shows that aha, they might be in there, but uh you don't get a free lunch. If you go down further in the data sheet, it shows that you actually need the uh external load capacitors.

**Dave Jones:** But, there are some that won't need any external load capacitors. They're kind of handy. You might find that in say a low-power uh real-time clock uh uh, for example, with a 32.768 kHz watch crystal.

**Dave Jones:** And you'll notice that this one actually has the 10 meg load resistor here actually internal with an internal switch, which is actually connected to the enable pin. So, when you disable the chip, it opens up this circuit, so there's no feedback resistor here, and it disables the oscillator.

**Dave Jones:** But, trap for young players, for this particular chip, doesn't mean it happens on other chips, but this particular, uh, chip, it actually the enable pin also will turn on this MOSFET, which will short out your X1 pin to ground.

**Dave Jones:** You don't really want to do that with an external crystal oscillator. Just be aware of that. So, there you have it. Hope you found that interesting. You do not need to use an external crystal and the load capacitors.

**Dave Jones:** You can replace it on practically any chip with an external crystal or some other external clock that you've got from some other micro. And as I said, you could use that for maybe for even synchronization, uh, purposes or stuff like that.

**Dave Jones:** And it's almost always on the X1 pin, but just double check that. Anyway, in the particular case of, uh, Cyber City's circuits here, wanted to know why, uh, 3.579545 MHz, still remember that from a kid, it's the, uh, color burst frequency crystal.

**Dave Jones:** In this particular case, used also used for DTMF, uh, decoding as well. Why are they so big? So, he wanted to He's using this chip, uh, and he wanted to actually replace it with a smaller oscillator.

**Dave Jones:** And sure enough, like you can go over here and you can get a tiny little, uh, 3.579545 MHz crystal oscillator like this, you know, 2.5 mm by 3 mm.

**Dave Jones:** No worries. Yeah, you're going to Oh, 43 cents. Looks like they're under 30 cents in volume. That's not too shabby. So, of course, external crystal oscillators like this have advantages.

**Dave Jones:** You might be able to get a different package. You might be able to might be using it in some other products, so you can reuse it or whatever. And when you're forced to, like your chip has just the, uh, X1 and X2, uh, pins on it for a regular crystal, you can just override that and feed it into X1 no worries usually.

**Dave Jones:** So, there could be lots of reasons why you might want to use this particular circuit trick here. And hope you found it interesting. If you did, please give it a big thumbs up.

**Dave Jones:** As always, discuss down below and let me know if you like short little circuit tips like this. Catch you next time.
