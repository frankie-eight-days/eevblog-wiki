---
video_id: vUvzgZt1Vug
title: EEVblog 1547 (Part 2) - PINGing the Voyager 2 Space Probe!
url: https://www.youtube.com/watch?v=vUvzgZt1Vug
source: youtube-asr
timestamps: {"0": 22, "1": 37, "2": 55, "3": 70, "4": 79, "5": 97, "6": 109, "7": 123, "8": 136, "9": 148, "10": 160, "11": 181, "12": 195, "13": 211, "14": 229, "15": 239, "16": 257, "17": 272, "18": 277, "19": 292, "20": 302, "21": 319, "22": 329, "23": 345, "24": 361, "25": 375, "26": 389, "27": 401, "28": 417, "29": 430, "30": 446, "31": 461, "32": 475, "33": 492, "34": 505, "35": 520, "36": 535, "37": 545, "38": 568, "39": 583, "40": 598, "41": 621, "42": 643, "43": 656, "44": 671, "45": 684, "46": 693, "47": 707, "48": 719, "49": 735}
---

**Dave Jones:** Actually, so we only moved in last week. This is This is the new operations center for follow the sun where we start in November where Canberra will control Goldstone and Madrid antenna during daylight hours and that will rotate so they'll control ours during the night time.

**Dave Jones:** So So we're going to be getting a lot more consoles so it looks nice and airy but it will be filled in the coming weeks. Now uh the teams We have teams of five.

**Dave Jones:** Oh, this is my desk. So it's a new desk. It's It's a very special desk. It's a It has lots of screens. So So essentially this also allows me to interface with our flight systems as well.

**Dave Jones:** Uh so I can from here call up anything on the the other workstations. Uh if if you if you pan around essentially each workstation here So can incorporate uh two antenna.

**Dave Jones:** So we can have one one of our controllers controlling deep space station 35 and 34 at the same time. So it could be Mars, it could be you know, in the case of what we're tracking now, we're tracking uh on deep space station 43 Voyager 2.

**Dave Jones:** And uh so on deep deep space station 34 we're we're tracking wind as well. Uh so as the day goes on we'll we have the Mars rising and I'll I'll show you the schedule that we have.

**Dave Jones:** So So this So this is our tracking schedule at the moment. So you'll you'll hear some noises at the back. They're just doing testing. So everything in green is essentially what's being supported now.

**Dave Jones:** Deep space station 43 is tracking Voyager 2. There was a command uplink as well. And as we just described earlier, so we did the best lock frequency and and transmitted a number of no op commands to the spacecraft as well.

**Dave Jones:** Wind and they were dumping as well. So Wind has two downlink channels essentially modulated on the same carrier, but they have engineering and essentially engine and scientific data. So we have two receivers in lock.

**Dave Jones:** We have a high rate 144 kilobits, and then we have a a lower rate which is just 7 kilobits for the engineering. 36 and 35 are on maintenance at the moment.

**Dave Jones:** And really that sort of sets us up as the day goes on. So we start hitting the Mars missions. Mars rises here, so actually probably in the next hour or so, but it's a little bit longer that we start picking up our first spacecraft on Mars, which is Maven MVN.

**Dave Jones:** And then we start MER 1, so Opportunity as well. So we're still communicate with the with with the rover. And the rover is an unusual one, so on how we communicate with it cuz it uses the relay spacecraft most of the time.

**Dave Jones:** So all the vision that you see is through the the relays. But but we do command directly. And so what we do is we'll send a command sequence and then we listen.

**Dave Jones:** Round trip light time, we we get a happy beep or a sad beep. So at the moment this is showing the Voyager 2. This is a downlink system. And we have 10 downlink channels that we can use and it's a it's a it's a resource so that we can pick for for anything.

**Dave Jones:** So some might need one receiver, some might need two, some possibly might need three. So, this is uh what we're using here. This is down link channel number three.

**Dave Jones:** The signal comes into the IF here. And this is our carry lock. We're in lock. That's great. Gives us a frequency. 8420 MHz. Power on the carrier and negative 159.

**Dave Jones:** So, it's huge. So, that's a big signal level. It it it depends. Uh so, if if you're looking at Maven on the low gain antenna, and even though you you look at at Mars, that could be 10 dB lower.

**Dave Jones:** So, it really depends on the purpose of the spacecraft and and what they're trying to get down. Voyager, as I said, has a a great big high gain antenna.

**Dave Jones:** It has uh a 20 W transmitter, which doesn't seem huge, but sort of uh it it seems to be ample for what we need. Uh so, the 158 is fairly good.

**Dave Jones:** Carrier residual. Now, this is not At the moment, we're not coherent, which means that the the spacecraft is using its USN. It's it's it's an ultra stable oscillator. So, it's its own time reference.

**Dave Jones:** But even over 15 billion kilometers, we're only 183 Hz out. That's crazy. So, so yeah, so predicted, we're pretty well bang on. Uh the one way indicates the mode, so which is essentially non-coherent.

**Dave Jones:** If we were two-way, that means that the spacecraft is turning around our signal, and what we're receiving is reference to our uplink. So, as we raise the uplink, the down link will rise as well.

**Dave Jones:** The two are the two are linked. And the reason why we do that is for Doppler. So, we know if if there's a fixed ratio on the spacecraft, and we're transmitting a frequency, and the frequency we're receiving, if it's not exactly right, it must be the result of Doppler.

**Dave Jones:** And based on that, we can say, "Okay, the spacecraft is traveling at a velocity of x m/s." Signal noise temperature, whoa, it's a hot one, 19 Kelvin. So, that which is a really good That's probably about the standard.

**Dave Jones:** We get about 17 lowest. Uh so, a little bit of cloud, so but not too much. So, 18 Kelvin. If it rained now, uh that would just start to bang bang bang.

**Dave Jones:** Bang bang. So, so that can go all the way up to 130 and to the point where it wipes out the signal. Subcarrier, a little 20 22 and 1/2 K subcarrier.

**Dave Jones:** So, stripped off, the symbols are stripped off. There you go. We were saying we double double the symbols to get the bit rate. So, with the with the encoding method, it's MCD 12.

**Dave Jones:** Symbol SNR is 7, 7.1. Which is about the same as my ADSL modem. Right. So, I'm I'm 3 and 1/2 K away. Yeah. So, symbol to noise ratio that So, we go, "Okay, that's the symbols done." So, this is RF.

**Dave Jones:** By the time we hit our telemetry system, we're converting bits. It gets pumped into MCD, which is a multi-convolutional decoder. And that's the forward error correction we were using.

**Dave Jones:** And suddenly, our symbol SNR of 6.7 turns into 9.83, which is a 3 dB, which is a doubling that we get with that with that uh encoding method. Frame sync here.

**Dave Jones:** So, I say just like any other data, so uh it's packaged up, and there's a frame sync word at the beginning of the packet. So, what this does, it looks for that frame sync word, and said, "Okay, frame sync word, the frame is this length of time."

**Dave Jones:** and just chops it up into packets. And from there, we have the formatter where it's sent over to JPL. Really, so that's about as much as we see as far as the telemetry processing.

**Dave Jones:** We know I'm have we're having blocks leaving. This is our spectrum display here. And so, we're seeing a very tiny Voyager 2 signal sitting in the middle. So, what else we get from it?

**Dave Jones:** So, obviously, the Doppler that we're receiving here is being fed through as well as tracking data. And that track tracking data is as I said used to uh to then velocity as well, subtle changes.

**Dave Jones:** And And when when we're talking about changes, we're talking about uh fractions of hertz. And they're they're being measured. Uh this is our antenna here. Our display, so this is our performance display, so we know exactly where it's pointed.

**Dave Jones:** It gives us an azimuth and elevation, 219 and 53. Uh so, we've we go down and you know, everything is milli-degrees here. So, we're not talking degrees, we're talking milli-degrees.

**Dave Jones:** Uh so, uh in fact, it tenths of milli-degrees. Uh the accuracy, so especially when you start to want to expand, so it's fairly tight uh as far as the bore sight.

**Dave Jones:** The higher freq- the frequency you go, obviously, that the narrower the beam. Uh 43 is different from all the others. It's It's a huge antenna. And And if you look at it, so as far as beam width, if if one edge moves off bore sight by more than a a couple of centimeters, then you start losing it.

**Dave Jones:** So, accu- accuracy is essentially ulti- ultimately what you want. So, we have encoders that give a position. Essentially, they're they're little more than wheels. But then, this one also has an auto collimator as well, which is something quite different.

**Dave Jones:** Parks has one similar. Uh essentially, it's a an hour angle and deck antenna within an antenna. So, sitting up on the top of the instrument tower in between the the elevation axis, there's essentially a robotic arm as an hour angle and deck.

**Dave Jones:** But instead of an antenna dish, it has a laser. So, this 8,000 ton antenna is slaved to essentially a laser. So, which is another level of accuracy again. So, so these are probably with without doubt the most accurate antennas on the planet.

**Dave Jones:** So, and you know, we have dedicated engineers purely calibrating the antenna on a regular basis to make sure it it's it's bang on. Uh monthly. Let's say the the specs, if he's more than two or three millidegrees out, he's chastising himself.

**Dave Jones:** What this does show quite effectively is this is X-band, so it doesn't doesn't show the transmitter. This is our our uh essentially our input to our receivers. It shows the horn here.

**Dave Jones:** What you're seeing there is is a rain blower. It sounds kind of crude. So, considering the hardware we have. But with the with X-band, you do have the issue with water pooling on on the cone window.

**Dave Jones:** So, there's a little blower that just makes sure that that doesn't settle. It comes in and goes into a diplexer. And what a diplexer does is simply allows us to receive and transmit at the same time.

**Dave Jones:** We're not using the transmitter at the moment on the X-band because this is an S-band uplink on Voyager 2. 3C17 It comes through, and then we have a fixed polarizer.

**Dave Jones:** Where essentially the combined downlink is separated to a right-hand circular polarization and a left. Voyager is left-hand circular. So that comes through and goes into our receivers. And that ties in with with our receiver over here.

**Dave Jones:** And that's where it's introduced to the receiver. Why is the power level different on there to what we see on the screen here? Shouldn't be. It shouldn't be. Mine's 152.

**Dave Jones:** Yeah. And mine's 159. Yeah. So Why is it different? I have a feeling so it's all AGC. And I don't think I think what you're seeing there is not exactly right.

**Dave Jones:** So where let's just say I'd assume my system's all right. So we're going to assume that that one is correct. Yes. Yep. Minus 159. Yeah. Okay. 152 I'd be jumping up and joy and I'd think, "Oh my god, it's turned around heading back."
