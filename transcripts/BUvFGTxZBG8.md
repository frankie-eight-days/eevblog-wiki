---
video_id: BUvFGTxZBG8
title: EEVblog #506 - IR Remote Control Arduino Protocol Tutorial
url: https://www.youtube.com/watch?v=BUvFGTxZBG8
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 36, "3": 49, "4": 67, "5": 83, "6": 105, "7": 116, "8": 132, "9": 147, "10": 157, "11": 175, "12": 198, "13": 211, "14": 230, "15": 242, "16": 253, "17": 267, "18": 276, "19": 286, "20": 296, "21": 311, "22": 324, "23": 341, "24": 352, "25": 362, "26": 373, "27": 383, "28": 396, "29": 423, "30": 438, "31": 450, "32": 466, "33": 481, "34": 496, "35": 512, "36": 521, "37": 535, "38": 551, "39": 567, "40": 584, "41": 598, "42": 610, "43": 634, "44": 644, "45": 661, "46": 672, "47": 681, "48": 706, "49": 723, "50": 734, "51": 744, "52": 752, "53": 764, "54": 775, "55": 790, "56": 805, "57": 816, "58": 828, "59": 839, "60": 844, "61": 853, "62": 864, "63": 879, "64": 891, "65": 899, "66": 910, "67": 923, "68": 936, "69": 950, "70": 965, "71": 979, "72": 987, "73": 996, "74": 1012, "75": 1026, "76": 1043, "77": 1052, "78": 1064, "79": 1074, "80": 1085, "81": 1094, "82": 1107, "83": 1119, "84": 1130, "85": 1143, "86": 1156, "87": 1169, "88": 1184, "89": 1194, "90": 1206, "91": 1223, "92": 1232, "93": 1247, "94": 1257, "95": 1271, "96": 1284, "97": 1294, "98": 1308, "99": 1330, "100": 1343, "101": 1361, "102": 1372, "103": 1380, "104": 1393, "105": 1407, "106": 1415}
---

**Dave Jones:** Hi, in a previous video, I showed a very rudimentary hack of one of these infrared learning remote controls and how you could hack in and directly drive one of the buttons which you can pre-program from something like an Arduino microcontroller or anything else.

**Dave Jones:** It could be some other external switch or some other external circuitry and that was incredibly simple and rudimentary hack, but there were quite a few people who wanted to know how to do that directly from a microcontroller like an Arduino for example itself instead of having to hack a remote control.

**Dave Jones:** Why can't we just can we just put an infrared LED on one of the output pins of the microcontroller and transmit the code directly? Well, yes, we can do that and it's not entirely difficult at all.

**Dave Jones:** So, that's what I'm going to show you today how we're actually going to receive a code from my Canon WLD-89 remote control for my video camera here and how we're going to capture that on our oscilloscope and then program it into this Arduino.

**Dave Jones:** Now, there are of course many different ways to skin this cat. I mean, you don't have to use an oscilloscope like we're going to use today. You could use a logic analyzer like this Saleae logic analyzer or you could use the Arduino itself for example.

**Dave Jones:** You can get libraries that actually read in infrared code from an infrared receiver and play it back. We've got a Infra USB dangerous prototypes USB infrared which we're actually going to be using to capture the data, but that can stream it to a PC and then you can analyze the data on the PC and know exactly what it is and you can get all sorts of open source

**Dave Jones:** libraries on the PC to do that. You just hook up an infrared receiver to it and there's you know many, many different ways to do this, but we're going to do it um, old-fashioned way.

**Dave Jones:** We're going to actually uh, get our digital scope and we're going to capture the waveform coming out of the IR receiver. We're going to get the individual bits from it and the timing and then we're going to program that into our microcontroller so that then we can spit out the IR code.

**Dave Jones:** Now, there's two devices you can actually use to receive the infrared code from the remote control. One is just your basic uh, photodiode, infrared photodiode {slash} uh, phototransistor and they can either come in uh, two-lead or three-lead configurations like this one here.

**Dave Jones:** And these are fairly uh, limited devices, but what they allow you to do is to get the actual raw carrier frequency out of the infrared remote control, as we'll see.

**Dave Jones:** But there's also these other three-pin devices which are these uh, proper infrared receiving modules and they've actually got circuitry in there that uh, decode and demodulate the carrier frequency and give you a direct data out and we'll see this on the oscilloscope in a second.

**Dave Jones:** So, um, the good thing about this USB infrared uh, toy, we can actually uh, probe both of these sensors and see the different types of data coming out. Now, the good thing about these little uh, infrared modules is that you pretty much never have to buy them because you should have them in your junk bin because pretty much any bit of uh, surplus consumer gear, for example, I've

**Dave Jones:** got a um, a set-top box PVR, one of those PVR recorders here and if you're you know, any old bit of gear, an old CD player or anything that you salvage will have one of these in it.

**Dave Jones:** Check it out. Rip it out. Reuse it. Not a problem. And just be aware that there are different uh, carrier frequency modules, but uh, the most common type that uh, you're going to deal with is the 38 kHz carrier frequency and we'll actually be able to measure that cuz we'll be getting the raw uh, data, carrier data dir- uh, out of this uh, photodiode here.

**Dave Jones:** Okay, we're going to use our oscilloscope to capture first of all on channel one here. We're going to capture the output data from the IR module. So, this is the one that has the demodulator built in.

**Dave Jones:** It'll take out the carrier frequency, as you'll see, and we'll just get the raw 1 0 data out of it. Now, what you want to do, this is a 5-V one, so you want to set it to 1 V per division roughly.

**Dave Jones:** Let's put it down here. You want to set it maybe 50 ms per division, a fairly you know, slowish time base so we can capture the entire packet and then zoom in later.

**Dave Jones:** And this is where an oscilloscope with a deep memory is going to come in. So, you know, you don't want to use an old-school oscilloscope with you know, 2K of sample memory or something like that.

**Dave Jones:** A nice good deep memory scope, especially if you're capturing more than one packet. So, we'll take a look at that. But here we go. I've got my infrared remote control.

**Dave Jones:** I've got channel one hooked up to the output of that IR module, which you can salvage any bit of gear you want. And I'm going to push my start stop button, which is the one I want to capture.

**Dave Jones:** And bingo, there it is. We've captured that. I had it set to single-shot mode, of course. Triggering is somewhere in the middle there. And let's There it is. And we can zoom in and we can see the data coming out of that.

**Dave Jones:** Bingo, we've captured that packet. Now, look what happens if I do that again. And I press the button for a bit longer. Hold it down for a bit. There we go.

**Dave Jones:** Look, we actually captured five packets there because if you hold down the button, it will continually send the packet. And then your product that you're actually you know, pointing this at can actually decode that you've pressed that button for like 3 seconds or something like that.

**Dave Jones:** For example, like to go into the playback mode on my video camera, I've got to push this button here for like 3 seconds, hold it down, and then it will go into playback mode.

**Dave Jones:** So, it just sits there counting those packet, decodes them, and counts it, and it knows I've pushed that for 3 seconds. Now, as you can see here, the output of the module is normally high, and then it goes low like this.

**Dave Jones:** So, we're getting a zero out of that, but what that means, that zero, is that it's actually receiving uh cuz it's a logic low output when it receives a carrier frequency.

**Dave Jones:** We'll see this in a second when we probe our uh photodiode directly. So, there's That means that the infrared when this is low, when our signal is low, it means our infrared uh LED is transmitting.

**Dave Jones:** So, when we decode this data and program it into our microcontroller, it decodes the ones and zeros, a zero here means switch on the LED at the carrier frequency rate.

**Dave Jones:** And likewise, when we've got a logic one up here, then that means the LED is switched off. It's receiving nothing. Now, what I'm going to do is switch on channel two here, and I've got channel two hooked up to the other the phototransistor down there, which is going to give us the direct uh data from the transmitter here, and of course, we've still got channel one hooked up to our

**Dave Jones:** uh infrared module there. So, here we go. I'm going to press the same button again, and we'll capture that data packet. There we go. So, as you can see, channel two here from that infrared phototransistor, there's a big block there, and what that is is the carrier frequency.

**Dave Jones:** We can zoom in on that. See, it's practically identical and almost lined up, as we'll see. So, let's zoom in on that. So, let's move our position over here and zoom in on that first bit.

**Dave Jones:** It goes low. Bingo! There's our carrier frequency. And if we check out our frequency down here, it's decoded that. There you go, 38.4 kHz. It's going to vary. It's not going to be uh spot on, but it's roughly that 38 kHz carrier frequency.

**Dave Jones:** So, when we program that into our microcontroller, we need our microcontroller to not just go low and turn on the LED or go high and turn on the LED, it needs to generate that 38 kHz carrier frequency for that amount of time.

**Dave Jones:** And you'll notice it's done exactly the same thing over here, exactly the same carrier frequency. And you'll also note that the this blue waveform here is the raw data coming out of our trans infrared transmitter here.

**Dave Jones:** So, you can see that it starts uh transmitting and it takes a few cycles for that infrared receiver module to actually decode that and then give our low output and it extends past there as well, but it's basically the same time period as that uh whole packet there.

**Dave Jones:** So, that's just two ways at looking at the same data. So, it doesn't matter whether you whether you've got just a photodiode, phototransistor, or whether or not you've got one of the proper um infrared receiver modules.

**Dave Jones:** If you've got just got the module here, just assume that the carrier frequency's in there when that's low and when it's high, you get nothing. And if you've got the carrier frequency, uh if you've just got the infrared diode, well, you can just decode it exactly the same way.

**Dave Jones:** And you notice the time of our burst there, we're on 50 microseconds per division is just over 550 microseconds. So, we can get that exact value. It's it doesn't have to be absolutely spot on, but it should be close.

**Dave Jones:** So, we'll measure that as accurately as we can. And I've used both my cursors there and I'm measuring 562 microseconds for that burst. And you'll notice that the dead period there, where it's well, high, but it's actually switched off, is exactly the same 562 microseconds.

**Dave Jones:** Now, you could be mistaken for thinking that these are individual 1010 bits in here and then you've actually got three zeros here because if you actually go in there and measure it, this period here is actually yes, it is precisely three times that length there.

**Dave Jones:** So, you might think it's one and then 000, but that's not the case because I happen to know that this thing looks precisely like the Japanese protocol or sometimes better known as the NEC protocol.

**Dave Jones:** Now, the unusual thing about the NEC protocol is it doesn't have a fixed bit length for both one and zero. It actually changes between those. So, let's take the example of like it's ordinarily high.

**Dave Jones:** So, let's say the start of the bit is here. It goes low for that one. We'll call that one time period there. Then it goes back high like that and that represents a zero, but a one is represented by it going low like that for that one time period and then going high again for three time periods.

**Dave Jones:** It's like that. So, that in there, so that from there to there is a zero and from there to there is a one. So, it's quite unusual, but that's the NEC protocol.

**Dave Jones:** And you don't have to think of it like that, of course. Well, if you're actually programming this into your microcontroller, then you could think of it as you know, 101000 if you really wanted to, but and you could actually program and implement it successfully that way.

**Dave Jones:** But that just wouldn't be the correct way to do it cuz what we're going to find here is that in the total of all this, we're going to actually have four bytes for a total of 32 bits.

**Dave Jones:** Now, of course, to decode that on your scope, some scopes of course have serial protocol decoding, but I have never seen one that actually has the NEC protocol built in.

**Dave Jones:** And if your a scope or your logic analyzer or whatever happened to have a custom protocol decoder for example, then you might just be able to set that up to actually decode it and turn those different time length periods into zero and ones for you and spit out that four byte code that the NEC control code actually has.

**Dave Jones:** But, we don't have that capability here, so we're just going to decode this manually. So, what we can do is go in here after our idle period and that's the start of our first bit there and we can see that that first one is a one because it's one time period with three blank time periods after that.

**Dave Jones:** So, that's a one, one, and then zero, zero, zero, zero. And that's called a pulse length encoding technique. So, we can go in there and just manually decode these.

**Dave Jones:** Not a problem whatsoever and we should get total out of that four different bytes. And I've gone through and manually decoded that and this is what we get. We get our four eight-bit bytes there.

**Dave Jones:** And the first two bytes are the address, so there we go, it sends those, then it sends the command here, and then the inverse of the command like that.

**Dave Jones:** So, you should, if you've decoded it right, this last byte should be an inverse of that one and that's exactly what we see on a bit-by-bit basis. So, now we've got this data, we can program it into our micro.

**Dave Jones:** Beauty. Now, to throw a real spanner in the works, something like the Philips RC5 IR protocol, for example, each time you press the key, it can actually toggle that bit each time.

**Dave Jones:** So, what I'm what I've set up here is I've captured this waveform and there's there I've stored it as a reference waveform here. So, now I'll press it again and see if we get get an identical waveform.

**Dave Jones:** Let's have a look. Does it look identical? It does. So, I'll do that one more time. No, we don't have any toggled bits, so it looks like it repeats the exact same code every time.

**Dave Jones:** You've just got to be careful there. Otherwise, you know, that could really ruin your day and changes the equation on how you're going to write your IR driver and stuff like that.

**Dave Jones:** And here's the source code, the sketch I've written for this. Yeah, I could have just used an off-the-shelf library, IR code library. Some of them are quite simple, some are quite complex.

**Dave Jones:** There are a lot out there that do support the NEC protocol we're actually after. And a lot of them are complete receive codes and do all sorts of stuff.

**Dave Jones:** But I wanted to write my own because, well, that's the spirit of this thing. And as it turns out, it's very, very simple. So I wrote it from scratch.

**Dave Jones:** The source code for this from a link down below the video here. So I'll be very brief on this. I've set up my LED and my infrared LED on a pin.

**Dave Jones:** You can just define which pin of the Arduino you've got. I've got my bit time, 562 microseconds, as we saw on the oscilloscope. And then I define the infrared code that I want to send.

**Dave Jones:** In this case, it's that 4-byte 32-bit code that we reverse engineered from the oscilloscope. So in binary form, I've got it as one big 32-bit word there. So that's all set up.

**Dave Jones:** You can have multiple codes for any command button that you want to send. This one is just the reverse engineered code for my Canon remote control record stop record button.

**Dave Jones:** And then I've got a simple setup routine here that just sets up the pin as an output for the LED. And then it switches the LED off to start with.

**Dave Jones:** Then I've got two simple routines, and that's the entire code right there, just in those two routines, almost fit on that one screen. A couple of dozen lines of code.

**Dave Jones:** The first one is the IR carrier, and that generates 38 kHz carrier frequency. All you do is pass it the time in microseconds that you want the carrier frequency to go for, and then it just goes through a for loop and turns the LED off and on there.

**Dave Jones:** Not a problem at all. Now, it's got a divide that past time by 26 microseconds here because 26 microseconds is roughly the inverse of the 38 kHz carrier frequency that we got.

**Dave Jones:** And then all it does is it sets the turns the LED on for half that period or 13 microseconds and then turns it off for 13 microseconds and it repeats as long as it needs to.

**Dave Jones:** And then we've got another routine which sends the 32-bit code. So, you just pass it the code here as a long 32-bit long value. And then we have the LED generate the leading pulse here as we saw on the oscilloscope.

**Dave Jones:** Nine 9,000 microseconds we turn the carrier on for. That's 9 milliseconds. And then we turn the carrier off for 4.5 milliseconds there. So, it's we've generated our leading pulse.

**Dave Jones:** And then all we do is we go in a for loop here and we send out all of our 32 bits or four bytes in sequence. I'm just doing that using a mask here.

**Dave Jones:** So, I'm just masking the most significant bit and then shifting it one bit at a time at the end of it. That's why I did it as a 32-bit word.

**Dave Jones:** It's just easier that way than say four individual bytes. Saves a few lines of code. And then of course uh we well, we start out by generating the one bit time 562 microseconds the carrier frequency.

**Dave Jones:** And then we have to determine via that masking if our current bit is a high or a low. If it's a high, then of course we have to wait the three bit times dead time to signify a one in the NEC protocol.

**Dave Jones:** But, if it's a zero, then we only have to wait one extra bit time. Very, very easy. And that's it. It just repeats for all 32 bits. And one thing I forgot to mention on the oscilloscope capture is I also noticed a uh stop bit at the end of it.

**Dave Jones:** So, it was actually had a 33rd bit on there, just a stop bit of one bit time. So, I've added that in there at the end. And then I've just got a main routine here.

**Dave Jones:** All it does is calls the setup, defines the pins, and then it sends my infrared code to switch the record mode of my camera on. It waits 5 seconds, and then I send the code to stop recording.

**Dave Jones:** Easy. And no surprises for guessing it didn't work first go. No, it wasn't Murphy's law. As a matter of fact, I kind of expected it to possibly not work first go, and I'll show you why.

**Dave Jones:** So, what I've done is I've hooked up my logic analyzer here because to analyze something like this, we really need to look at that code output. You can do it on an oscilloscope, or but a logic analyzer is easier.

**Dave Jones:** We can capture it here. Now, I've hooked up my Saleae logic analyzer to the LED output. I'm going to sample at 8 MHz here. Uh more than fast enough.

**Dave Jones:** 1 meg samples good enough. And negative uh edge trigger here. So, we'll start this, and I'll press my reset button on my Arduino. I've already downloaded the sketch. And looky what we have here.

**Dave Jones:** We have our code. That's exactly the same as what we saw on the oscilloscope. And if we go in here, we can look at that carrier frequency of the leading pulse there.

**Dave Jones:** And if you have a look on the right-hand side, I can't move my cursor over, but it says the pulse width is 16.8 microseconds, and the frequency is 29.9 kHz.

**Dave Jones:** Nowhere near the 38 uh kHz that we actually need. No wonder it doesn't work. Why? Well, it's uh pretty obvious. And uh those people who are experienced with these sort of things probably already know.

**Dave Jones:** Because in my timing loop here, my IR carrier loop, I've assumed that it's 26 microseconds. Okay, I've rounded that down near enough to generate the loop timing in here.

**Dave Jones:** That's not going to be a a real major issue. The major issue here is this delayed microseconds. You see it's got 13. So, we're expecting to get 13 microseconds delay, but look, we don't.

**Dave Jones:** We get 16.8. So, there's another what 3.8 microseconds or thereabouts added to that. So, it's not 13 microseconds, it's 16.8. Uh why? Because well, let's assume that the delay microseconds routine is fairly accurate, okay?

**Dave Jones:** It's not going to be absolutely, you know, spot on, but it's going to be near enough. What's taking all the time? Well, the only other code in here is this digital right routine.

**Dave Jones:** And this digital right routine does actually take time. In this case, it takes a couple of microseconds to execute. And there's faster ways to do it, but we're just using the digital right routine uh cuz that's the basic way in the Arduino.

**Dave Jones:** So, let's compensate, tweak this thing. I am holding my tongue at the right angle, and let's take that's let's knock that, you know, three or four microseconds off. Let's change that to nine microseconds, and let's upload that.

**Dave Jones:** We've uploaded. We can go back in here. We can start this again. And run run our Arduino's running. Oops, it's already captured it because I've got an auto start routine in there.

**Dave Jones:** And you'll notice that the timing is different. Look at this. 12.75 microseconds now, and we're close to our 38 kHz. We're now 39.4 kHz. And as I said, you don't have to be spot on, but that's going to be near enough.

**Dave Jones:** And as it turns out, this now works. And sorry about the audio and video quality now. I'm at home actually doing this. I don't have my main camera, so I'm shooting on my old compact.

**Dave Jones:** It's night, and well, yeah, it's not going to be very good. Anyway, I have my Canon camcorder here. I've got my Freetronics 11 down here I've got an infrared LED hooked up and pointed to it via a 220 ohm drop resistor.

**Dave Jones:** And if I press the reset button here, it should start recording and then 5 seconds later should send the code again to switch it off. So, let's give it a go.

**Dave Jones:** Bingo, it started recording. And it won't quite go to five because it took a second or two to boom, but there you go. Works a treat. And just a small trap for young players here.

**Dave Jones:** With any sampling system like this, the resolution is going to be dependent upon your sample rate. Now, we're sampling at 8 MHz here and you'll notice that it's over on the right-hand side there it's saying the pulse width is giving us that to three decimal places or 1 nanosecond resolution.

**Dave Jones:** Well, that's obviously complete It's saying it's 12.875 microseconds. It's not possible to get 1 nanosecond resolution on that, but 8 MHz is more than good enough to get the timing requirement for this particular application, but let's resample that at say a lower rate of 500 kHz.

**Dave Jones:** Now, if you invert five let's start that, capture it. And here we go. And if you invert 500 kHz, of course, you get 2 microseconds. You'll notice that there we go.

**Dave Jones:** It's jumping between 2 and 14 microseconds, but it's still showing two decimal places beyond that. That's the software not knowing what it's doing and this might be tricking you into thinking that that pulse width is precisely 14.00 microseconds when it's not.

**Dave Jones:** Your resolution isn't good enough to determine that. In this case, this really isn't quite good enough for this particular system. It's almost in the ball ballpark, but not quite.

**Dave Jones:** Anyway, just be aware of that. Trap for young players. So, that's it. Very, very simple to write your own code, reverse engineer a protocol. You don't even need an oscilloscope.

**Dave Jones:** You can do it using very simple and basic tools, a PC or whatever. So, no complex test equipment required here to reverse engineer that NEC protocol. And, you know, not much work at all.

**Dave Jones:** Very, very simple. So, I hope you enjoyed that. There were lots of stuff involved in this, oscilloscopes, reverse engineering, and then we had a little fail there in our source code and tweaking some logic analyzer stuff.

**Dave Jones:** It's all happening. Fantastic. So, if you like the video, please give it a big thumbs up. And, as always, if you want to discuss it, jump on over to the EEVblog forum.

**Dave Jones:** And no correspondence will be entered into on the source code. Thank you very much. Catch you next time.
