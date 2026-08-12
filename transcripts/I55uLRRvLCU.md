---
video_id: I55uLRRvLCU
title: EEVblog #235 - Rubidium Frequency Standard
url: https://www.youtube.com/watch?v=I55uLRRvLCU
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 28, "3": 38, "4": 58, "5": 70, "6": 84, "7": 96, "8": 104, "9": 122, "10": 141, "11": 153, "12": 165, "13": 182, "14": 192, "15": 209, "16": 223, "17": 241, "18": 261, "19": 280, "20": 305, "21": 324, "22": 348, "23": 373, "24": 384, "25": 395, "26": 407, "27": 417, "28": 431, "29": 452, "30": 464, "31": 489, "32": 509, "33": 524, "34": 536, "35": 550, "36": 567, "37": 584, "38": 597, "39": 611, "40": 628, "41": 639, "42": 655, "43": 666, "44": 680, "45": 694, "46": 710, "47": 724, "48": 736, "49": 747, "50": 758, "51": 767, "52": 782, "53": 793, "54": 805, "55": 816, "56": 830, "57": 842, "58": 860, "59": 874, "60": 894, "61": 904, "62": 919, "63": 932, "64": 943, "65": 951, "66": 963, "67": 974, "68": 989, "69": 1000, "70": 1013, "71": 1025, "72": 1038, "73": 1055, "74": 1067, "75": 1079, "76": 1091, "77": 1110, "78": 1126, "79": 1139, "80": 1148, "81": 1162, "82": 1175, "83": 1186, "84": 1205, "85": 1217, "86": 1231, "87": 1242, "88": 1254, "89": 1270, "90": 1279, "91": 1306, "92": 1316, "93": 1332}
---

**Dave Jones:** Hey, let's look at what we're taking a look at. What are the more interesting things you can get on eBay and you can build up for your lab? It's a rubidium frequency standard, in this case the FE 5680A.

**Dave Jones:** You can get them pretty cheap on eBay. So, I thought I'd we'd do a teardown, I'd build one up, see how it works, and maybe build it into a little custom case, and hook it up and use it as a lab frequency standard, primarily for my frequency counter, but you can use it for anything.

**Dave Jones:** Let's go. So, what exactly is a rubidium frequency standard? Well, inside this little can, which you can get for about 50 or 60 bucks on eBay, used of course.

**Dave Jones:** Uh you can't buy them brand new for that, not a chance. They're usually, you know, thousands of dollars. But, because these are used in uh cellular telephone towers and things like that to maintain an accurate frequency reference, when they uh you know, discontinue or they decommission those frequency towers, tons of these things are left over.

**Dave Jones:** And you can get them really cheap. And what's inside this can? Well, it's basically an atomic frequency standard. And you've heard of that before. You've heard they're used in GPS satellites and all sorts of advanced communication systems.

**Dave Jones:** Well, uh there are a few ways to actually get an atomic frequency standard. You can use uh hydrogen, cesium, and the other one is rubidium. And that's a very popular one.

**Dave Jones:** Bit of a poor man's frequency standard. This isn't going to match a GPS satellite, not by a long shot, but it's pretty darn good. And it's going to be a super accurate frequency reference for your lab.

**Dave Jones:** So, let's take a look at what's inside it. It's a bit complicated, but stick with me. And here it is. I know it looks complicated, but it's it's not that bad.

**Dave Jones:** And this may not be 100% accurate, so don't about the details, okay? If you want to find the real details, go look them up. But, I'll give you a basic rundown of how a rubidium frequency standard works, shortened to RB, that's the chemical you know symbol for rubidium.

**Dave Jones:** Now, what we have here is what's called a physics package. I love the term physics package because it it has a bunch of physics inside a little metal can that basically does some magic here with some electronics with a frequency lock locked loop, an FLL.

**Dave Jones:** You might have heard a PLL, phase locked loop. This is a frequency locked loop where it basically has an internal oscillator, just a regular crystal oscillator inside your standard.

**Dave Jones:** It can either be a oven controlled one, it might be that or it might be a voltage controlled crystal oscillator, a voltage controlled oven one, or digitally controlled or whatever.

**Dave Jones:** There's several ways to do it. But let's just assume it's a voltage controlled crystal oscillator working at a fundamental frequency which is a multiple of the rubidium transition frequency of roughly 6.834 GHz.

**Dave Jones:** That's the transition frequency of the atoms. If you want to find out the exact details of the hyperfine transition of rubidium, the rubidium atom and all that sort of stuff, you can go look it up.

**Dave Jones:** I won't go into it. Doesn't really matter. But basically the physics package up here helps sir it works as a servo and it servos this amplifier and keeps it locked to the transition of the rubidium atom inside this frequency package.

**Dave Jones:** And then from that, it can just generate your frequency standard out. In this case, 10 MHz is a pretty industry standard reference frequency. And any good lab, if they have a frequency standard, will have 10 MHz output.

**Dave Jones:** And that's what a lot of well, that's what most frequency counters will have an external frequency input for the reference oscillator and it's almost always 10 MHz. So, that's what we're going to get out of our little rubidium frequency standard today.

**Dave Jones:** These are what it puts out, 10 MHz, but it's disciplined around a much higher frequency and intermediate frequency of 50-odd. In this case, it's 50.255 MHz, but other implementations of rubidium frequency standards can use different frequencies and different techniques.

**Dave Jones:** As I said, ADCs and DACs and digital control. But, basically what it does is it um has a discharge lamp up here, which actually this takes quite a bit of power, which these rubidium frequency standards do actually require quite a bit of power to actually operate, you know, in the order of 10 plus watts or something like that.

**Dave Jones:** So, it has a a rubidium 87 discharge lamp. If you want to know what 87 is, go look up your physics textbooks. And it has a resonance cell, which is a little cavity, just a little cavity, which the rubidium gas atoms will be inside there and they get all excited when you apply a certain frequency to them.

**Dave Jones:** And this resonance cell can get upset by external magnetic influence as well. So, it's usually in a mu-metal shielded can so that external magnetic fields don't affect it. And there's some other things that they can do to try and reduce the effects of external magnetic fields as well.

**Dave Jones:** And then, there's a photocell on the output with a transimpedance amplifier to detect the amount of light coming from the discharge lamp. And the whole idea is that when the resonance cell is exactly at 6.834 and there's digits beyond that, which is the hyperfine transition frequency of the rubidium atom.

**Dave Jones:** They all resonate. All the atoms inside there resonate and there's less light going through or it blocks the light going through to the photo cell and that generates an error voltage out of the amplifier and then it can servo that and keep it locked in and they might sweep it by a couple of hundred hertz or thereabouts around the transition frequency from this RF generator here, but that's basically

**Dave Jones:** what it does. It just blocks out hits that resonant point the less light gets through the photo cell and boom and then it can adjust the frequency and it settles down and locks in.

**Dave Jones:** So, that's why these things might take a few minutes or some might even take up tens of minutes to actually lock in and stabilize, but once they do, they're incredibly accurate.

**Dave Jones:** So, it's a basic rundown of a physics package and how a rubidium frequency standard works. Pretty neat. I love it. Magic. So, why does all this frequency stability matter?

**Dave Jones:** Well, I'm glad you asked. Let's take a look at it in terms of say a basic frequency counter and let's take a look at some crystal oscillators. Now, I've got four different types here.

**Dave Jones:** One is your standard quartz crystal which you're probably familiar with one of these little crystal oscillator cans or just one of these little you know, regular quartz crystal oscillators you've used in your projects before and they're pretty darn ordinary.

**Dave Jones:** They're in the order of 10 to 100 parts per million tolerance over over a standard temperature range. Basically, this tolerance table here takes into account temperature basically. So, what what's one part per million?

**Dave Jones:** Well, one part per million is typically specified on the data sheets as 1 * 10 to the power of minus six. 10 to the power of six is a million, there's one part in one million, and so on.

**Dave Jones:** 10 to the power of minus seven, 10 to the power of minus eight. So, these standard quartz crystals are pretty crappy. They're 10 to 100 ppm. And the other thing with any oscillator, whether it's quartz or any anything else, they're all pretty much all of them are based around quartz, whether or not they're temperature compensated or they're rubidium compensated, as we've seen, they're going to have not only a

**Dave Jones:** tolerance over temperature, but they're going to have an aging factor as well. As they get older, and that usually is specified per year, but it can also be specified they can give you additional figures per month and per day as well, because you might want just a very short term to be short term stability over one day, but let's just take a look at some typical figures for a year.

**Dave Jones:** These things not only are they not that great just basically at any one point in time over a year, they're also going to age five to 10 ppm might be a typical figure per year.

**Dave Jones:** So, they're just going to get worse and worse. Now, if you look at a digitally temperature compensated crystal oscillator, that's where it's a regular crystal oscillator, but they've actually measured it.

**Dave Jones:** They've characterized its performance, and they've actually programmed in compensation values over temperature. So, hence digitally temperature compensated crystal oscillator. And they're pretty much, you know, they're going to be like an order of magnitude better.

**Dave Jones:** 0.5 to 5 ppm. One with one ppm aging, order of magnitude better stuff. And then you get onto an oven controlled crystal oscillator. That's where they actually keep a a regular quartz crystal like this at a very specific temperature.

**Dave Jones:** So, the ambient temperature, the temperature in your lab which drifts all the time doesn't matter. So, they they can get very stable in terms of, you know, 0.1 ppm 10 to the power of minus seven over the span of, you know, a year.

**Dave Jones:** That's the aging sort of thing. And the tolerance is pretty darn good, too. And then, you take a huge step up to the rubidium type stuff, 10 to the power of minus 11 we're talking about with 10 to the power of minus nine aging.

**Dave Jones:** Absolutely incredible. And of course, these are crystal oscillators. They come in all different types of manufacturing what's called cuts. They cut the crystal in a different way, you know, SC cut, AC cut crystals.

**Dave Jones:** And that can affect the temperature characteristics and the aging characteristics and the shock characteristics and all sorts of vibration characteristics, everything for these crystals. I won't go into it, but let's take a look at how it relates to a frequency counter.

**Dave Jones:** So, here's a typically good old-school frequency counter. It's a Philips PM 6672. You can pick these up on eBay. Going to have to do a teardown of this one.

**Dave Jones:** And it's got Well, basically, it comes with several different types of oscillator options. When you buy frequency counters like this, whether they're the one hung low cheapies on eBay or they're the good ones, you know, name brand ones like this, then you're going to get different types.

**Dave Jones:** And if you even this a good one like this, if you buy it just with its standard oscillator option, it's just going to have one of these regular, you know, quartz um temperature compensated oscillators in.

**Dave Jones:** It'll be, you know, a good one, a pick of the bunch, but you're still only going to get, you know, five to 10 ppm. Well, what does that How does that translate to how accurate it is on the display here?

**Dave Jones:** Well, let's take a look at it. This is measuring a 10 MHz frequency, okay? So, it's actually displaying not in MHz, displaying in kHz there, but it's 10.000000 MHz.

**Dave Jones:** Now, what's 1 ppm? Well, if it was 1 MHz, then 1 Hz, 1 1 millionth of that, one part per million, it'd be this least significant digit here. But because it's 10 MHz, it's going to be this digit here.

**Dave Jones:** So, if you had a 1 ppm accurate crystal in there, for example, then it would only be accurate to that digit there. So, the least significant digit there is absolutely useless.

**Dave Jones:** Plus you've got aging on top of that, you've got temperature, and all sorts of other stuff. So, you know, if you've only got a 1 ppm crystal, that's not that great.

**Dave Jones:** But typically, you might get a 10 ppm. Oops, you've just jumped up to this digit here. And the last two digits are useless. Not to take into account aging.

**Dave Jones:** So, it's pretty horrible. So, generally, for a frequency counter, this is a regular eight-digit one. You might have a nine-digit one. You're going to want a pretty stable oscillator in it.

**Dave Jones:** So, if you buy one of those, you know, $100 or $80 Wan Hung Low brand frequency counters on eBay, they're just going to have a cheap as crystal in it.

**Dave Jones:** And the last two or three digits aren't going to matter a rat's ass. Now, here's the oven controlled oscillator inside this frequency counter. It's got this option. It's got the specific PM 9690 / 01 option.

**Dave Jones:** And I've had that on. And yeah, trust me, that is actually quite warm. That's why these things can take 10 or 20 W of power just to keep them at a stabilized temperature inside.

**Dave Jones:** And as I said, inside there, they've just got like a a regular crystal in there. But yeah, it's going to be a really stable one. They've chosen it for a really good cut.

**Dave Jones:** But because it's kept at a constant temperature, then uh once you let this thing warm up to temperature, you have to do that with these oven control ones. They've got to warm up to temperature first.

**Dave Jones:** But, once they're there, they're incredibly stable. This one um if you look up the uh spec sheet for it, it's uh you know, got a uh tolerance of in the order of uh you know, 0.1 uh ppm or uh aging of uh 0.01 ppm.

**Dave Jones:** So, pretty darn good. You notice, too, that it's got an adjustment trim pot in there. And uh these things aren't magic, of course. You've actually got to trim them to the correct frequency.

**Dave Jones:** But, once you do that, they don't drift much. So, having that oven controlled oscillator in here with uh 10 to the power of uh minus uh s- eight um aging, then we're talking about the one digit past the least significant digit here in terms of aging, in terms of accuracy.

**Dave Jones:** We're talking about the least significant digit there. So, it pretty much matches the capability that sort of ovenized oscillator matches the capability of a typical eight-digit frequency counter like this.

**Dave Jones:** So, um pretty much, you're going to at least want If you've got a If you've got a good frequency counter even or if you've got a nine-digit uh one, for example, with an extra uh decimal place, you may actually uh well, you at least want a oven controlled uh oscillator uh with that sort of stability and that sort of aging for this.

**Dave Jones:** We're going to blow it out of the park by using a rubidium uh standard. And we can just feed the 10-MHz reference signal in the back, and Bob's your uncle.

**Dave Jones:** And that rubidium frequency standard will absolutely guarantee that uh regardless of uh aging and temperature and all sorts of stuff, what the frequency you get on your frequency counter is going to be exactly correct to Well, it's going to be plus minus one uh least significant digit.

**Dave Jones:** And that can be important for all sorts of niche sort of stuff you work on. Ham radio as well, having an ultra stable frequency source is a big thing in the ham radio circles.

**Dave Jones:** And there's some other timing applications, timing counting applications in the lab where you know, a really good laboratory 10 MHz reference rubidium standard is worth its weight in gold.

**Dave Jones:** And you can buy them for 50 bucks. So, you know, it's well worth building one. So, let's take a look at this one we've got from Frequency Electronics Inc.

**Dave Jones:** eBay is absolutely flooded with these things. So, I'm sure you have no problems getting one for, you know, 60 bucks maybe including postage or there might be postage on top of that.

**Dave Jones:** But these things probably cost thousands of dollars maybe well, maybe not $10,000, but you know, they would have cost several thousand dollars brand new. And they're a brilliant rubidium frequency standard.

**Dave Jones:** This is the FE-56A. There are several versions of it. And they're all used. You won't pick up one brand new I don't think. They're all pulled out of old, you know, GSM cell phone base stations or something like that.

**Dave Jones:** So, pretty much they'll all be second hand. But if you buy from a good eBay seller, they will have actually tested them. Now, this one actually comes with the pin out.

**Dave Jones:** It's got a standard D9 on here. It came with, you know, the D9 connector and a bunch of flying wires there. And pin one is the input and from 15 to 18 volts DC.

**Dave Jones:** I don't know whether or not it can go below or above that, but I'm going to stick within that. It's got two ground pins. It's got a frequency lock output so that you can drive a LED indicator direct.

**Dave Jones:** If you put it in a box, mount a LED on onto there. And I believe it's active low. And that will indicate that it's um, it's warmed up and it's locked in and your frequency output is spot on.

**Dave Jones:** It also requires a second input of uh 5 volts on pin four there and then you've got your RF 10 MHz out and it is actually RF, it's a sine wave um and it's uh 1 volt uh peak to peak into an open load or 0.5 volts peak to peak into a 50 ohm load.

**Dave Jones:** So, uh let's uh power it up and uh see how much power it takes. Okay, let's power this thing up and see what we get. Uh it's got a 15 to 18 volt uh input which I'm measuring the current.

**Dave Jones:** Here I'm using 15 volts on the input and it's got a 5 volt DC input as well uh which I'm measuring the current on the fluke here. So, uh we expect there to be a bit of a uh power spike at power on until it uh settles down.

**Dave Jones:** Um so, it should have it should start up at a higher current and then slowly settle down to a lower current. So, I'll switch those supplies on both at the same time and see what happens.

**Dave Jones:** There we go. Whoop. 1.6 odd amps on the uh 15 volt rail and basically just 100 odd milliamps, just under 100 milliamps on the DC rail and haha we have ta-da, our output signal already.

**Dave Jones:** And there it is and it is 10 MHz at uh 1.3 volts uh peak to peak cuz there's no load on there, no 50 ohm load because if we actually switch on the 50 ohm impedance load, of course it will uh drop down, but there you go.

**Dave Jones:** But uh has it locked in yet? I'll have to um probe the logic output and see how long it takes to lock in, but the frequency has actually um outputted straight away.

**Dave Jones:** Okay, let's try that again. Uh in this case the uh yellow uh channel one waveform is our oscillator output. Uh channel two 1 volt per division, that's our uh lock output.

**Dave Jones:** So, I expect a logic level uh output. I believe it's active low once it's locked, so it should we should uh actually see it jump up. And I'll switch them both on, and we'll time that and see how long it takes.

**Dave Jones:** Bang, it's actually high. There you go. So, it hasn't actually uh locked in yet. So, we're talking 1 2 3 4 5 volts. And boy, there we go. There's some uh something happened to the RF output there, but it hasn't locked in yet.

**Dave Jones:** We should, after a minute or so, we should see that uh green line, the channel two line there, drop to logic low to indicate that it has locked in.

**Dave Jones:** Bang, there it goes. And it's now locked in. And uh what values have we got down here on the meters? We have about .76 uh amps there, .77 amps on the 15-V rail, and uh 90-odd milliamps on the 5-V rail.

**Dave Jones:** So, as you can see, it actually draws a fair bit of power. So, that's almost uh 12 W total power consumption for the device. And it only took about uh 35 odd seconds to lock in, so it wasn't that long at all.

**Dave Jones:** And that case is getting pretty darn warm, too. And uh if we try and attempt to probe that, we're talking, you know, it's well over 40°. I've only had it on for like 5 minutes.

**Dave Jones:** So, these things can actually get quite darn hot, so you wouldn't want to mount this thing in like a sealed uh plastic yeah, jiffy box or something like that.

**Dave Jones:** It'll just get stinking hot. What you want to do is mount one of these in a diecast um alloy uh case or something like that, one of those extruded aluminum cases, or something that uh you can get the heat out of this thing.

**Dave Jones:** I don't know what uh temperature will do to these things uh long term, and well, I don't really want to know, I think. So, um yeah, it'd be much uh I think it'd be very beneficial if you kept these things as cool as possible.

**Dave Jones:** And there you go, we're almost getting 50 degrees. There seems to be a hot spot over this side of the package over here, but it'll Yeah, they get pretty darn warm.

**Dave Jones:** Now, there are a couple of options on this specific model. One is to actually get an RF output separate RF output connector here, and also there's an option to get digital frequency control so that I believe it's like some sort of serial input RS232 type input and you can send commands to it to actually generate a specific frequency from 0 to 10 or 20 MHz or something like that, and that'd

**Dave Jones:** be really nice, but I don't believe this model actually has that. It's just the fixed 10 MHz output, but if you can get that one with the digital frequency control, that would be really nice.

**Dave Jones:** You could turn one of these into a really nice fully programmable lab rubidium frequency generator with keypad and a microcontroller and LCD and you could set the frequency to anything you wanted.

**Dave Jones:** It'd be terrific, but we've only got this fixed 10 MHz one here. Oh, well.
