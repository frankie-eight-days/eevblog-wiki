---
video_id: I7ppDNLlEL4
title: EEVBlog #1119 - Designing a 1kV Isolated Oscilloscope
url: https://www.youtube.com/watch?v=I7ppDNLlEL4
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 44, "4": 58, "5": 73, "6": 86, "7": 99, "8": 112, "9": 126, "10": 140, "11": 154, "12": 167, "13": 176, "14": 189, "15": 205, "16": 220, "17": 230, "18": 245, "19": 257, "20": 269, "21": 285, "22": 300, "23": 313, "24": 328, "25": 344, "26": 358, "27": 373, "28": 386, "29": 403, "30": 415, "31": 430, "32": 442, "33": 455, "34": 470, "35": 480, "36": 494, "37": 512, "38": 525, "39": 533, "40": 548, "41": 565, "42": 575, "43": 591, "44": 604, "45": 618, "46": 629, "47": 640, "48": 651, "49": 664, "50": 678, "51": 690, "52": 703, "53": 717, "54": 729, "55": 742, "56": 759, "57": 772, "58": 789, "59": 804, "60": 818, "61": 830, "62": 841, "63": 859, "64": 871, "65": 885, "66": 900, "67": 913, "68": 928, "69": 944, "70": 959, "71": 970, "72": 985, "73": 997, "74": 1014, "75": 1029, "76": 1041, "77": 1056, "78": 1072, "79": 1088, "80": 1100, "81": 1111, "82": 1128, "83": 1144, "84": 1160, "85": 1174, "86": 1190, "87": 1203, "88": 1215, "89": 1229, "90": 1245, "91": 1261, "92": 1273, "93": 1287, "94": 1302, "95": 1314, "96": 1328, "97": 1338, "98": 1350, "99": 1364, "100": 1379, "101": 1392, "102": 1401, "103": 1415, "104": 1430, "105": 1446, "106": 1459, "107": 1471, "108": 1483, "109": 1495, "110": 1509, "111": 1520, "112": 1533, "113": 1545, "114": 1562, "115": 1576, "116": 1586, "117": 1598, "118": 1608, "119": 1620, "120": 1631, "121": 1644, "122": 1655, "123": 1668, "124": 1687, "125": 1700, "126": 1713, "127": 1727, "128": 1737, "129": 1752, "130": 1767, "131": 1781, "132": 1794, "133": 1810, "134": 1824, "135": 1837, "136": 1851}
---

**Dave Jones:** I'm here with Bart from Cleverscope. You've seen before, but we've got a new We have a new product. Yeah, we do. A new Cleverscope. Okay, it's a It's very big and chunky compared to our our old one, which is sitting over

**Dave Jones:** there. Yeah, that's the original That's the original one. Yeah. Yeah. I love the PCB front panel. Yeah, well, that's it. Yeah, the gold edge. Yeah, it's four channels. It's 500 mega samples at 14 bits. At 14 bits. 14 bits and

**Dave Jones:** New Zealand bits bits bits Sorry, I couldn't resist. Yeah, fair enough, too. It's an isolated channel oscilloscope. This is what I'm excited about. It is fully isolated. Each channel is isolated. Each channel has got a kilovolt isolation between itself, the other

**Dave Jones:** channels, and ground. Plus or minus a kilovolt. Beautiful. Hence why we're measuring a motor drive. We are. We're probing the innards of a motor drive. Fantastic. And we're looking at the gate drive and also at the saturation voltage of a

**Dave Jones:** transistor that's inside the gate drive, which is going up and down 320 volts. Yeah, it's all rather noisy. Here is the voltage that's driving the gate. And it's through a little resistor, which goes to the gate itself, which is that

**Dave Jones:** signal there. So, we're looking across a resistor. Nice. Which is going up and down 320 volts in a few nanoseconds. Because you can measure across the resistor because you're isolated and floating. Yeah, we're There's two requirements here. The first is that it's isolated

**Dave Jones:** and floating, and the second one, the very important one, is that it has very high common mode rejection ratio. Yes, what are you talking about? Throw some figures at us. Well, CMRR CMRR, which is how much noise gets into

**Dave Jones:** the measurement from the rapidly slowing signal. It's 100 dB at 50 MHz. At 50 MHz. At 50 MHz. So, you How far does it How fast does it fall off after that? It will carry on pretty linearly after

**Dave Jones:** that. Unfortunately, my little test rig only checks up to 50 MHz. Right. And what's the bandwidth of the what's the actual analog bandwidth? 200 MHz bandwidth. This is a graph of CMRR over frequency. Uh we got to 65 MHz

**Dave Jones:** and this is the 100, so we're actually a bit below 100. Beautiful. Which is not bad. And we can we can uh see the effect the effect of that over here. We have a full bridge. Mhm. There's a We're going to sweep around a

**Dave Jones:** lot. There's a full bridge. And what we're doing I'll point at things. We're looking at this gate here which is connected to a switching node, which is switching between 0, which is the bus, and 500 V. 500? 500.

**Dave Jones:** Nice. And over here is another gate, which is doing the opposite between 0 and 500. And we've also got two probes looking at the actual switching voltage, so you can see what they are. Do not do that with a regular scope.

**Dave Jones:** People I've done a video on how not to blow up your oscilloscope. That's a way to blow up your oscilloscope. That is Trust me. very good way to blow up a lot of stuff. Except if you've got an isolated scope

**Dave Jones:** isolated channel scope like this. Exactly. Yep. So here we have a graph if you can see the connections here. The two red probes are the switch voltages, which are going 500 V. And the two gray probes are connected to the gates.

**Dave Jones:** Got it. And here we can see the the red one is the 500 V and it's switching you can see that it's about 506 V. Uh it's switching in eight or nine nanoseconds. So it's Wait, that is very fast, yeah. And these

**Dave Jones:** signals here are those two gates. Nice. Oh. sitting on top of this the 500 V. 0 to 500 V. Yep. And we can see some uh some uh switching component in there in the in the transitions. We can go and investigate.

**Dave Jones:** Ah. Okay. So here Oh, so we zoomed in. This is a zoomed in view of the Yeah, this is a zoomed in view. So this is looking at that spot there. Yep. So we're looking at that and that.

**Dave Jones:** That looks sharp. There. That looks like a nice Well, that's the but it's not. There you go. No, no, no. It's the gate turning on. This is maybe I But this is the Miller plateau and that's the the voltage level

**Dave Jones:** at which the voltage stops rising because the charge is going into the gate like crazy. Okay, now there is a problem with FETs, which is what this is. These are FETs in that there's a capacitance between here and here and

**Dave Jones:** another one between here and here. And that capacitance acts like a voltage divider and as you raise and the effect of it is that there's it's like a capacitance from the gate down to the negative bus. As you're raising the

**Dave Jones:** voltage and the opposite way around when you're reducing the voltage and that tends to suck charge out of the gate drive. So, this reduction here is a reduction because of the Miller capacitance. Got it. And this pulse here is because the

**Dave Jones:** Miller capacitance is injecting charge back into the gate. Mhm. These can be problematic if your design's no good because if you make this too low, in fact below 4 volts, um it will turn the FET off. Of course, yes.

**Dave Jones:** And if you go Bam, it goes And it's not good. No, no. Same here, if this goes above 4 volts, you start getting a little bit of turn on in the FET. Then you have two FETs on at the same time. Is that a good plan?

**Dave Jones:** You get feed through on your power rail. They short out. You do. They do. Happily, FETs are actually pretty rugged. Yes. And as as they get hotter, their resistance increases unlike IGBTs and so you you are a little safer, but it's not

**Dave Jones:** a good thing to do. The losses go up. Don't do it. But the big pro thing is is that this is almost impossible to measure using any other method. You could buy a Tektronix TVM probe What's that? $13,000.

**Dave Jones:** new fiber optic Fiber optic isolator one? You can use one of these which does the same thing. Yeah. Except a bit noisier. Right. At at the bandwidth At the same bandwidth. What's the bandwidth of that? This is 200 MHz is their lowest cost

**Dave Jones:** one. Only $13,000. And they And they have a GHz one as well which is only $23,000. And it's just a probe? It's just one channel. Just one probe. One probe? That's right. We have four. Yeah. Okay. No other way of measuring this.

**Dave Jones:** Does this come with fiber optic probes? with every probe you need. So we give you four low voltage one switched one by 10 by probes and four high voltage 100 times probes. Nice. And if you really want we can give you

**Dave Jones:** 200 times probes cuz then you can look at 1.6 kV. Ooh. Excellent. Yes. Excellent. But most MOSFET solutions stop at around about 5 600 volts something like that. That's right. But there is There's a lot more technology coming

**Dave Jones:** along. They have things called sick. Uh have you heard silicon carbide fits? silicon carbide fits. Okay. They're rated at 1200 volts. And you know people are starting to use that 1200 volts. I don't think they were around when I

**Dave Jones:** was doing 500 odd volt uh MOSFET design. No. Not at all. They're new. They're new. Yeah, this was like 12 years ago maybe. And they are They are tricky because you can get edge rates down to about 3 ns

**Dave Jones:** horrendously fast. That is ridiculous. Well, then you have to deal with lots of other problems as well of course. You know, any series inductance massive ringing voltages you don't want that. Any EMC issues you might have well they

**Dave Jones:** can be magnified. I get it. You know When you got your 1500 volts switching in a couple of nanoseconds your your EMC's out the window anyway. Exactly. Even even this is a bit fast. I mean you know, 7 to 8 ns or whatever it

**Dave Jones:** was. Yeah, it was 7 to 9 I should say. It's It's pretty damn fast. So that's impressive. So how much does this cost? Well, this one there the we is 9,600 bucks. Yep. Moderately expensive. Yankee bucks. Yankee bucks.

**Dave Jones:** Okay. Yeah, pretty expensive, but we are open to deals. It's a specialized bit of kit. It's a specialized bit of kit, and as I say, you can buy a whole one for less than the price of one tech probe.

**Dave Jones:** Uh are there is there any other competition for an equivalent four-channel isolated scope? No. On the market, no? No, there's no other competition. have an isolated scope, but it doesn't go that far. The the TPS series scopes, they're

**Dave Jones:** isolated, but they're only 300 volts isolation between channels, and their common mode rejection is about 30 dB at 10 MHz. Oh, it's yeah. So, uh 30 dB is is like uh 51 to 50. So, if you're looking at 500

**Dave Jones:** volts, you'd be 10 volts of common mode noise that would be working around here. You wouldn't see that signal with 10 volts of common mode noise. So, that's the big deal. Wow, that's all the difference. Cuz we're down on the scale there, yeah.

**Dave Jones:** Look at the scale. yeah. Look at that. Yeah, that's right. We have 10 volts of noise on there. If I had 10 volts of noise, you'd you couldn't see anything. Wouldn't see it at all. No. Wow. No. Impressive.

**Dave Jones:** And the same goes for differential probes. Differential probes are also used to try and do this job, but they also have terrible common mode rejection ratio at high frequencies. They're great at 50 Hz, Yep. but once you get them up to 10 MHz,

**Dave Jones:** they're useless. This 8 ns second these 8 ns ns slew rates, well, their equivalent bandwidth is 1 over pi tr. So, that's 1 over about 3 * 8, that's 1 over 24, which is about 40 MHz, about. So, that's equivalent to a 40 MHz

**Dave Jones:** signal. So, you have to have pretty good common mode rejection to reject it and not see it in the signal. For sure. Yeah. All right, can we take one of these apart? You going to show us how it

**Dave Jones:** works? we can. You can explain the design and everything. I I can. is the design of it. All right. Oh, no. No, we we We do everything. But we're going to turn off because there's there's lethal voltages in here.

**Dave Jones:** Okay. So, we're unplugging things. And we're going. All right, bud. Tell us about this. Okay. Tell you about this, right. Sorry, I just want to see the isolation slots down in Oh, yeah. Yeah, they're actually Yeah, I can see the slots. Look

**Dave Jones:** at that. Each one is a massive What did you say? A 1,500 V isolation? Yeah, yeah, it's 10 mm, which under the IEC standard is about 8,000 V of real isolation. But in terms of meeting the standard gives you 1,000 V,

**Dave Jones:** you know, category 3. Yep. Yep. So, it's it's pretty good. Uh sorry, we're not going to be able to open the cans tonight. No, we are not. No, no. That's a That's quite a drama opening the cans. All right. Tell us all about it.

**Dave Jones:** Okay, I'll tell you all about it. So, here's These are the four channels. They're isolated from each other. As you can see, there's a fiber optic link here. These are two These These There's actually four fibers in there and they

**Dave Jones:** go at 10 They're They're capable of 10 gigabits per second, but we only run them at five. Right. They're five gigabits per second from here to here and there's two channels one way and two channels back the other.

**Dave Jones:** Hang on. Wait. These things here. See those little wires? Yeah. Yeah, can you zoom in on those? Those Those are Yep, those Oh, there we go. I couldn't see it. Right, the color was a bit different. Yeah, yeah, that's the fiber channels.

**Dave Jones:** You'll find that the blue ones go one way and the green ones go the other. And they're running at five gigabits per second. So, you've got the converter inside the front end. And you're just running the digital I was going to ask, how are you

**Dave Jones:** isolating it digitally or analog? Digitally, because we want to minimize noise to the absolute maximum. And that was the best way That was really the only choice. That is the only choice. That's only choice. The other guys, that's the

**Dave Jones:** Tektronix guys, they do it the other way. They modulate us a signal and send it as light as a modulated analog signal. But, the result of that is that they have much more channel noise than we do. So, we we we wanted to keep the

**Dave Jones:** channel as quiet as possible and the only way to do that is to have as few bits in the way as possible. Yep. That's what we do. So, So, that's a 14-bit ADC. 14-bit 500 mega sample ADC plus some

**Dave Jones:** uh and then this this is the power supply that runs it. Mhm. Now, power supplies are actually really tricky. They are. Um You've rolled your own by the looks of it. We have rolled our own. Now, the the big

**Dave Jones:** one the big issue with this and I'm giving away trade secrets here, Excellent. but it's so much better that everyone knows is is uh that they this power supply here um has very low common mode noise going out into the real world.

**Dave Jones:** It's less than 100 microvolts. Nice. So, it doesn't need bootstrap capacitors to link the input to the output to route the the noise back to the input. Right. Um and it's it's driven with a very symmetrical power switch.

**Dave Jones:** It's It was hard work. It took us a year to design this. to design just the power supply. I can believe it. I can believe it. Bloody terrible. Okay, and then as we carry on, um we you'll notice that we have got two

**Dave Jones:** fibers one way and two the other. Mhm. Well, one of those fibers we use for a clock, a very accurate clock. Mhm. It's a half a half a PPM clock. Nice. That's pretty That's pretty good. Yep. And it's only running at 500 kHz.

**Dave Jones:** And it comes back comes into each device and it's distributed using a uh No, you can't see it. It's on the backside. Um it's used distributed with a very low latency clock. I was going to say, are there any uh

**Dave Jones:** synchronization issues across the channels? There's a lot of synchronization issues across the channels. That's another really hard problem. We wanted to be able to make it so we can use this device for our frequency response analysis system. Yes.

**Dave Jones:** I don't know if you've seen that, but it means that we can do gain phase. got the uh Bode 100. Right. Yep. We do the same as the Bode 100, basically. Right. Yep. But with fully isolated channels. fully isolated channels.

**Dave Jones:** That's handy. So you can go and end a fully isolated signal generator. So Oh, it's isolated. Yeah, you've got the same Same thing. Yeah, that's right. Yeah, you do it in one place, you might as well do it in the other.

**Dave Jones:** Excellent. Yeah, so that means you can inject a signal into the error amplifier in your live power supply Mhm. and measure live things. And the full frequency response of it of your 1,500 V Exactly. power supply. Wow. That's right.

**Dave Jones:** There's nothing on the market that does that, surely. There is nothing on the market that does that. Except this. Quite right. Okay, excellent. Okay, so the we have these clock signals coming back so that the error between channels is about plus or minus 70

**Dave Jones:** picoseconds. Pretty small. Very impressive. Mhm. I wouldn't have thought that would be a necessary requirement on a four-channel scope like this, but when you say frequency response analysis Well, you want very low phase error because if you want to measure things

**Dave Jones:** like inductance or capacitance, you need to have good accurate phase. Indeed. Yes. So the here are the eight There There are two lanes in each direction, so there are eight lanes coming into the FPGA. This is an Area-5

**Dave Jones:** FPGA, so it has eight lanes coming into it. That's a pricey FPGA, is it? It is a pricey FPGA. Very It's got eight 960. That has a lot of balls, that chip. It has a lot of balls. All right.

**Dave Jones:** That's right. It's a It's a very ballsy chip. Tell us about the choice of FPGA. Did you need it for the You obviously didn't need it for the IO count. I did actually because you might notice that this board plugs into this one and

**Dave Jones:** it's using an the equivalent of an Altera daughter board connector. Let's call it that. Oh, yes. Okay, it's their standard connector. It's high bandwidth. And we plan to offer more digitizer boards that you'll be able to plug in.

**Dave Jones:** And one of the digitizer boards we want to provide is a four channel one giga sample per second board. Wow. Which is based on an on on a E2V chip. It needs lots of power lines. Got it. Lots of power lines.

**Dave Jones:** Yep. So, you've got it for the IO plus the transceivers probably. Exactly. And then did you use all the gates or did you like you've got a lot of gates? No, we've got a lot of spare gates because it's upgradeable in the field

**Dave Jones:** and we plan to add more value over time. via the USB interface? Yes, it is. Yep. Yep. So, the we have a supply application so you can just upgrade it as you go. Fantastic. for no extra cost. So, then the other

**Dave Jones:** things down here there's a power supply system which there's lots of power supplies you need for an Area 5 sadly. Yeah, you need like five different rails. Yeah. You know, like 1 V 1, 1 V 1 5, 1 V

**Dave Jones:** 2, 1 V 8. Lots of them. Nightmare. And this is the IO board. And we have a an isolated signal generator 0 to 65 MHz. And you can see here the two isolated transceivers that allow us to get

**Dave Jones:** signals across the gap. We're not actually using fiber for them. These are pretty good. Okay. Low capacitance. Yep. So, that's a matching 14-bit one, is it? It is. It's a 14-bit one and it samples out at 170 mega samples.

**Dave Jones:** Nice. So, it's a little bit slower in sampling out but it still does a pretty good job. Is that full arbitrary capability? It is. It's got a 4K arbitrary buffer. So, it's not huge, but it still can do

**Dave Jones:** quite a bit. Is that done inside the FPGA? No. It's No, the problem we have is Oh, right. isolated. Of course. Yes. So, you've got a little FPGA under there? No, we No, we use an Analog Devices chip, which has an arbitrary waveform

**Dave Jones:** generator built into it. Got it. Yeah, so it's very handy. Terrific. Um and uh that gives us a frequency range of 0 to 65 MHz. Yeah, with very low distortion. So, the whole system is very low distortion. So, we do better than 80 dB

**Dave Jones:** Nice. down, which is not bad. And then here is the USB 3 connection. Um and we're using an FTDI chip there for the for the for the USB 3, cuz it also supports USB 2. But you Do you So, you need USB 3 for the

**Dave Jones:** bandwidth for the data? We have a lot of data coming backwards and forwards. Yep. And we also do streaming. So, if you want to stream to disk, you need you need high bandwidth, especially you got four channels at 14

**Dave Jones:** bits each. Does this have any local storage at all? Is there a 100 or is it like a 100% stream via USB? No, this The USB is far too slow for that. Right. Okay. So, um if you think about it, it's

**Dave Jones:** got 500 mega samples at at 16 bits essentially. Yeah. Okay. So, uh that's like a giga sample. That's four channels. That's four times 16. Mhm. Um let's call that two bytes. Four times two bytes is eight bytes times 500 mega

**Dave Jones:** samples is 4 GB per second. Oh, yes. You cannot get 4 GB per second across a USB link. Bytes, not bits. Bytes. Bytes. Bytes. Yep. Awesome. Yeah, not bad. storage does it have here? It It has It has 64 mega samples of

**Dave Jones:** storage for all the babies here? We are. And there are some on the other side as well. So, we turn it over, we can see another two there. So, that gives us 64 mega samples for every channel. So, there's four mega four channels of

**Dave Jones:** analog and one channel of digit eight channels of digital. How does How long does it take to dump that full memory over to the PC if you use the entire acquisition memory? Uh it If you dump the whole lot over USB

**Dave Jones:** 3, at USB 3 we're getting about 200 megabytes per second. Okay. So, So, we use like 10 seconds or something? something of that order. So, we don't we don't work that way. Right. What we do is we just decimate our 10K

**Dave Jones:** samples Yes. at whatever rate you need to to fit the screen. we saw on the screen before we're getting like real-time updating there. So, it's just a lower sample rate. It's a lower number of samples. Exactly right. Yes. But, you can get the whole

**Dave Jones:** buffer into memory if you want. You just have to wait. And uh and we stream at about 3 to 5 mega samples per second. 5 mega samples per second. And that And that can run for weeks if your hard

**Dave Jones:** drive is big enough. Got it. And we provide the tools so that you can zoom around and do your 50s and protocol decoding and maths and lots of stuff. With the software, can you Does it support like big 4K screens and you can

**Dave Jones:** see the all the full 14-bit Yeah, yeah, it's just Windows. Yeah, it's just just Windows. Just Windows. Zoom it. Not a problem. Yep. This is an SFP socket, which stands for small form factor socket, and it's so that we can plug in an Ethernet module.

**Dave Jones:** Nice. And uh Why why didn't you just put Ethernet on there as like just an Ethernet? Uh because a lot of our users would like to have fiber. Oh, of course. And instead of copper. Yes. And then if we you can see these are the two

**Dave Jones:** sorts of modules. So, this is this is a wired 1 gigabit per second Ethernet module, and this is a fiber one. Yep. Fiber's quite common, you see, and we would have to use up a lot more real estate to

**Dave Jones:** to put both in there. Yeah, obviously can't even with 1 gigabit ethernet, you can't stream the full No. in real time. Can you do it with fiber? No. No, you can't. 4 gigabytes per second Oh, okay. is 32 gigabits per second.

**Dave Jones:** gigabits per second, yeah. 32 gigabits per second. No. No. Fantastic. Even 10 gigabits per second wouldn't do it for you. Who are your main customers for this sort of kit? Cuz it's not cheap. It's, you know, it's $9,000, but it's the only

**Dave Jones:** thing on the market that does the job. That's right. So, our main customers to date are the people who want to who work in power electronics. And power electronics is becoming more and more ubiquitous because it's used in electric

**Dave Jones:** cars. I was going to say automobile manufacturers, they don't want the one. Exactly. So, we we have we have them at Bosch and and and Siemens. And uh and we're we're trying to work with um Delphi and Delco in the states, who are

**Dave Jones:** also making, you know, engine controllers and things like that. So, yeah, the people who use it are people who are mostly into power electronics. Which is part of the green tech movement, which we see as it being a

**Dave Jones:** growing, you know, market. Because you wouldn't buy this as a general purpose scope. No. You just You still sell the old one as like a We absolutely do. That's a general purpose scope. It does all the same things, the frequency response analysis,

**Dave Jones:** the streaming, the maths, all that sort of stuff. But it's not as band with this a lot more. It's about $1,000. About 1,000 bucks, yeah. Yeah, so it's still more Yes, exactly the same software. And you can link the two together if you really

**Dave Jones:** want to. There's some limitations, but, you know, that's how it is. Terrific. Yeah. And this has been out for a while now, but you still sort of always Yeah, yeah, the we This has been out for about a year in the in the format it's

**Dave Jones:** in, but we are bringing out a new and a totally new board set which fixes up doesn't fix any serious deficiencies but makes some things that we wanted to be a bit better. Um any other design any other design

**Dave Jones:** gotchas on this that caused a real headache during development? Uh Was the was the front end an issue or is the front end is it hard to make front end these days or is that easy peasy these days?

**Dave Jones:** No, it's No, it's that's that's probably why we're having a new board for the front end digitizer. Um one of the issues is that if you got a 14-bit converter and your channel noise is only two two LSBs. So, like if

**Dave Jones:** you're looking at 800 volts, you're getting 200 millivolts of channel noise. Um you really want to maintain that over the entire frequency range, don't you? You do. You do. Okay. Now, one of the big issues we have is probes.

**Dave Jones:** Probes themselves are not linear to that degree. They might be good for 1%. So, one part in 100. We want one part in 8,000. So, that means if you're looking at a square wave, we want the top of it to be linear to within one

**Dave Jones:** part in 8,000. Just a milli just just a 200 millivolts actually what we're aiming for on 8 volts on 800 volts, sorry. Um and we found that we could not get that with standard probes. So, what was the solution?

**Dave Jones:** The solution is we're working with Pinpoint who make our probes Yep. and we have modified the probes for them. We have we've changed their probe design. So So, you actually said we can you design it this way and this way?

**Dave Jones:** Well, they haven't done the design. We've done the tweaking. Oh, you've done the tweaking. And we're handing the design across to them to make. That's right. they handed over their base design and you said well and you mucked around with

**Dave Jones:** it and modified Exactly. And in the process of doing that we also had to change our own front end design. Our front end still works perfectly well with the standard probe. But what we've done is we've matched the before the

**Dave Jones:** characteristic of the Pinpoint front end probe front-end the probe with our front-end so they beautifully match across the whole frequency bandwidth and they give us one part in 8,000 linearity. What so what did you have to tweak to do

**Dave Jones:** that? And why don't they do it on standard Well, I know why they don't do it on standard probes cuz they don't have to. They don't have to. No, 8-bit converters, you know? And you've probably got two two bits of LSB

**Dave Jones:** noise as well. It's only one in a hundred is all you need. And if I try and do these sorts of tests with my Tek scope, that I can't even see it, you know? So what So what were the little tricks

**Dave Jones:** that you had to do or is that is that secret secret squirrel? No, no, we we we ripped apart the the probes and and we discovered that we had to add in a couple of little extra capacitors and a little inductor to to

**Dave Jones:** match the poles and zeros that shouldn't have been there. And in our own front-end, we found that when we switch ranges that we weren't having beautiful uh impedance uh keeping the impedances exactly the same. So we have had to add an extra

**Dave Jones:** little switch that switches in a bit more impedance so that both channels are exactly the same. Got it. Now, probe designs are usually um you can either get a top probe compensated up here or compensated down there. Which one did you go with?

**Dave Jones:** Uh this is compensated down here. Oh, right. Um Oh, no, there's Well, there's no there's Yes, it's isolated. Hold on there. No, no, that's right. no trimmer. You can't trim Oh, you can. You can. You have to undo

**Dave Jones:** that label. Oh, all right. Okay, it's under the label. It's on the label. It's like this idea though. It's down there, you know? Oh, okay. I see. It's got a little plastic hoodgemaflickery. All right. So it's it's like that except I I put it

**Dave Jones:** under the label so that people don't twiddle with it. So you had to add the stuff to the probe inside the probe. Yep, inside. Yeah, and no, it's actually down this end. This is where all the action happens.

**Dave Jones:** Yep. Uh anything up here has to then contend with the impedance of the probe coax cable. Of course. And it's much easier to do it on this end. So, that's where we've had to do it. That's right. And then our own

**Dave Jones:** changes are in the front end here. Got it. Yep. Are they allowed to sell that probe to anyone else or is that your own custom? Well, they they could, but it's a little more expensive for them to make.

**Dave Jones:** Mhm. So, um I doubt that they will. That's right. Because it won't match other people's stuff. Yeah, but you can sell it to space on spec, can't You can. You can. You can say this is a way better probe. Yeah.

**Dave Jones:** Well, some of a lot of the scopes are coming out as 10 or 12 bit now. So, a lot of the high end, you know, Keysight and Tektronix and Rohde Yeah, I know, but they say they're 12-bit scopes, but if you go and look at

**Dave Jones:** the actual effective number of bits, it's still down at about eight. It's not terrific, yeah. No, so you know, it's um it's true. They are 12-bit, but the noise is still pretty high. Got it. We we are an order of magnitude better

**Dave Jones:** noise. So, uh yeah. That's terrific. That's life. Awesome. So, then any other really troublesome things that caused you heartache during the development? Um let me think. The front end The front end, yes, there have been lots of hassles in terms of components not

**Dave Jones:** working the way they should work. We started off life using Well, we still are using some analog devices op amps, and the spec for the op amp is that you can power it down. Okay. But, when we powered it down, it

**Dave Jones:** dragged the input to minus 5 volts. Ah. And we didn't expect that. And neither did the designer who I spoke to in Ireland, a woman who said, "No, it doesn't do that." But then when she went and checked it, it does.

**Dave Jones:** Bummer. Wow. The second problem that we had is is that it has a output that you are supposedly able to multiplex. Mhm. So, we have two ranges, the 800 mV plus or minus 800 mV range and plus or minus 8V

**Dave Jones:** range. And we wanted to multiplex between the two ranges and we're going to use two op amps and switch one off and switch the other one on. And I talked to the designer and she said, "Yes, this is

**Dave Jones:** going to work fine. You'll all be fine." We design it. Guess what? It wasn't all fine. No, there was leak through even when it was off. Wow. Okay. So, that that was a problem for us. So, and then uh we've we've discovered the

**Dave Jones:** ADC that we use is actually inside it's two ADCs. They're two two 250 mega sample ADCs and they interleave them. And and they interleave them? They do. And what they don't tell you that on the data sheet? Oh, no, they do. They do. And they have

**Dave Jones:** this engine, they called it an engine, which which tries to get the gain and phase correct so they interleave beautifully. Yeah. But it turns out that they did all their testing only in the RF domain on sinusoidal signals.

**Dave Jones:** And when you put in a non-sinusoidal sinusoidal signal, non- Anyway, when you put in a single-ended signal that may be just the the bottom of an edge, the whole thing turns to custard. Oh. It took us a lot of effort to overcome

**Dave Jones:** that. We we've been working with Intersil to try and fix that. Mhm. And they're not Intersil anymore. No, they're now Renesas. Yes. Yes. They they dropped the name officially. Yes, they have. They're no longer but the guys inside are still Intersil guys.

**Dave Jones:** Yeah, that's right. Yeah. So, that was a little hassley. Yeah. How much total How long did it take you all up to do this from go to woah? Well, I reckon it's been about 4 years, which is huge. Yeah. Yeah. 4 years.

**Dave Jones:** How big is the design team? Three. Is that for working on it full time for three four years? Uh two of them two of them See, one of the guys is doing all the application software and the other one of the other

**Dave Jones:** guys is doing all the hardware and then I do So, FPGA and the C inside this thing here, Yeah. and I don't have full time available, so no. Two and a half. Sure. Well, that's impressive. Thank you very

**Dave Jones:** much, Behnam. All right, it's very nice to see you again. Thanks, mate.
