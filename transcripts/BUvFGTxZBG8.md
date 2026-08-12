---
video_id: BUvFGTxZBG8
title: EEVblog #506 - IR Remote Control Arduino Protocol Tutorial
url: https://www.youtube.com/watch?v=BUvFGTxZBG8
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 31, "3": 46, "4": 64, "5": 77, "6": 94, "7": 105, "8": 120, "9": 132, "10": 147, "11": 162, "12": 177, "13": 191, "14": 206, "15": 220, "16": 232, "17": 246, "18": 258, "19": 270, "20": 283, "21": 293, "22": 308, "23": 324, "24": 339, "25": 352, "26": 364, "27": 378, "28": 393, "29": 406, "30": 425, "31": 438, "32": 453, "33": 468, "34": 482, "35": 498, "36": 512, "37": 524, "38": 535, "39": 551, "40": 563, "41": 578, "42": 595, "43": 610, "44": 627, "45": 641, "46": 657, "47": 669, "48": 685, "49": 700, "50": 714, "51": 730, "52": 744, "53": 756, "54": 769, "55": 784, "56": 800, "57": 818, "58": 833, "59": 844, "60": 855, "61": 871, "62": 886, "63": 901, "64": 915, "65": 926, "66": 942, "67": 959, "68": 977, "69": 990, "70": 1001, "71": 1019, "72": 1034, "73": 1046, "74": 1057, "75": 1071, "76": 1084, "77": 1096, "78": 1113, "79": 1126, "80": 1143, "81": 1159, "82": 1179, "83": 1192, "84": 1204, "85": 1220, "86": 1234, "87": 1250, "88": 1264, "89": 1278, "90": 1292, "91": 1304, "92": 1320, "93": 1337, "94": 1353, "95": 1370, "96": 1382, "97": 1397, "98": 1413}
---

**Dave Jones:** Hi, in a previous video, I showed a very rudimentary hack of one of these infrared learning remote controls and how you could hack in and directly drive one of the buttons which you can pre-program from something like an

**Dave Jones:** Arduino microcontroller or anything else. It could be some other external switch or some other external circuitry and that was incredibly simple and rudimentary hack, but there were quite a few people who wanted to know how to do that directly from a microcontroller

**Dave Jones:** like an Arduino for example itself instead of having to hack a remote control. Why can't we just can we just put an infrared LED on one of the output pins of the microcontroller and transmit the code directly? Well, yes, we can do

**Dave Jones:** that and it's not entirely difficult at all. So, that's what I'm going to show you today how we're actually going to receive a code from my Canon WLD-89 remote control for my video camera here and how we're going to capture that on

**Dave Jones:** our oscilloscope and then program it into this Arduino. Now, there are of course many different ways to skin this cat. I mean, you don't have to use an oscilloscope like we're going to use today. You could use a logic analyzer

**Dave Jones:** like this Saleae logic analyzer or you could use the Arduino itself for example. You can get libraries that actually read in infrared code from an infrared receiver and play it back. We've got a Infra USB dangerous prototypes USB infrared which we're

**Dave Jones:** actually going to be using to capture the data, but that can stream it to a PC and then you can analyze the data on the PC and know exactly what it is and you can get all sorts of open source

**Dave Jones:** libraries on the PC to do that. You just hook up an infrared receiver to it and there's you know many, many different ways to do this, but we're going to do it um, old-fashioned way. We're going to actually uh, get our digital scope and

**Dave Jones:** we're going to capture the waveform coming out of the IR receiver. We're going to get the individual bits from it and the timing and then we're going to program that into our microcontroller so that then we can spit out the IR code.

**Dave Jones:** Now, there's two devices you can actually use to receive the infrared code from the remote control. One is just your basic uh, photodiode, infrared photodiode {slash} uh, phototransistor and they can either come in uh, two-lead or three-lead configurations like this

**Dave Jones:** one here. And these are fairly uh, limited devices, but what they allow you to do is to get the actual raw carrier frequency out of the infrared remote control, as we'll see. But there's also these other three-pin devices which are

**Dave Jones:** these uh, proper infrared receiving modules and they've actually got circuitry in there that uh, decode and demodulate the carrier frequency and give you a direct data out and we'll see this on the oscilloscope in a second. So, um, the good thing about this USB

**Dave Jones:** infrared uh, toy, we can actually uh, probe both of these sensors and see the different types of data coming out. Now, the good thing about these little uh, infrared modules is that you pretty much never have to buy them because you

**Dave Jones:** should have them in your junk bin because pretty much any bit of uh, surplus consumer gear, for example, I've got a um, a set-top box PVR, one of those PVR recorders here and if you're you know, any old bit of gear, an old CD

**Dave Jones:** player or anything that you salvage will have one of these in it. Check it out. Rip it out. Reuse it. Not a problem. And just be aware that there are different uh, carrier frequency modules, but uh, the most

**Dave Jones:** common type that uh, you're going to deal with is the 38 kHz carrier frequency and we'll actually be able to measure that cuz we'll be getting the raw uh, data, carrier data dir- uh, out of this uh, photodiode here. Okay, we're

**Dave Jones:** going to use our oscilloscope to capture first of all on channel one here. We're going to capture the output data from the IR module. So, this is the one that has the demodulator built in. It'll take out the carrier frequency, as you'll

**Dave Jones:** see, and we'll just get the raw 1 0 data out of it. Now, what you want to do, this is a 5-V one, so you want to set it to 1 V per division roughly. Let's put it down here.

**Dave Jones:** You want to set it maybe 50 ms per division, a fairly you know, slowish time base so we can capture the entire packet and then zoom in later. And this is where an oscilloscope with a deep memory is going

**Dave Jones:** to come in. So, you know, you don't want to use an old-school oscilloscope with you know, 2K of sample memory or something like that. A nice good deep memory scope, especially if you're capturing more than one packet. So,

**Dave Jones:** we'll take a look at that. But here we go. I've got my infrared remote control. I've got channel one hooked up to the output of that IR module, which you can salvage any bit of gear you want. And

**Dave Jones:** I'm going to push my start stop button, which is the one I want to capture. And bingo, there it is. We've captured that. I had it set to single-shot mode, of course. Triggering is somewhere in the middle there. And let's There it is. And

**Dave Jones:** we can zoom in and we can see the data coming out of that. Bingo, we've captured that packet. Now, look what happens if I do that again. And I press the button for a bit longer. Hold it down for a bit. There we go.

**Dave Jones:** Look, we actually captured five packets there because if you hold down the button, it will continually send the packet. And then your product that you're actually you know, pointing this at can actually decode that you've pressed that button

**Dave Jones:** for like 3 seconds or something like that. For example, like to go into the playback mode on my video camera, I've got to push this button here for like 3 seconds, hold it down, and then it will go into playback mode.

**Dave Jones:** So, it just sits there counting those packet, decodes them, and counts it, and it knows I've pushed that for 3 seconds. Now, as you can see here, the output of the module is normally high, and then it goes low like this. So, we're getting a

**Dave Jones:** zero out of that, but what that means, that zero, is that it's actually receiving uh cuz it's a logic low output when it receives a carrier frequency. We'll see this in a second when we probe our uh photodiode directly. So, there's

**Dave Jones:** That means that the infrared when this is low, when our signal is low, it means our infrared uh LED is transmitting. So, when we decode this data and program it into our microcontroller, it decodes the ones and zeros, a zero here means switch

**Dave Jones:** on the LED at the carrier frequency rate. And likewise, when we've got a logic one up here, then that means the LED is switched off. It's receiving nothing. Now, what I'm going to do is switch on channel two here, and I've got

**Dave Jones:** channel two hooked up to the other the phototransistor down there, which is going to give us the direct uh data from the transmitter here, and of course, we've still got channel one hooked up to our uh infrared module there. So, here we

**Dave Jones:** go. I'm going to press the same button again, and we'll capture that data packet. There we go. So, as you can see, channel two here from that infrared phototransistor, there's a big block there, and what that is is the carrier

**Dave Jones:** frequency. We can zoom in on that. See, it's practically identical and almost lined up, as we'll see. So, let's zoom in on that. So, let's move our position over here and zoom in on that first bit. It goes low. Bingo! There's our carrier

**Dave Jones:** frequency. And if we check out our frequency down here, it's decoded that. There you go, 38.4 kHz. It's going to vary. It's not going to be uh spot on, but it's roughly that 38 kHz carrier frequency. So, when we program that into

**Dave Jones:** our microcontroller, we need our microcontroller to not just go low and turn on the LED or go high and turn on the LED, it needs to generate that 38 kHz carrier frequency for that amount of time. And you'll notice it's done

**Dave Jones:** exactly the same thing over here, exactly the same carrier frequency. And you'll also note that the this blue waveform here is the raw data coming out of our trans infrared transmitter here. So, you can see that it starts

**Dave Jones:** uh transmitting and it takes a few cycles for that infrared receiver module to actually decode that and then give our low output and it extends past there as well, but it's basically the same time period as that uh whole packet

**Dave Jones:** there. So, that's just two ways at looking at the same data. So, it doesn't matter whether you whether you've got just a photodiode, phototransistor, or whether or not you've got one of the proper um infrared receiver modules. If

**Dave Jones:** you've got just got the module here, just assume that the carrier frequency's in there when that's low and when it's high, you get nothing. And if you've got the carrier frequency, uh if you've just got the infrared diode, well, you can just decode it

**Dave Jones:** exactly the same way. And you notice the time of our burst there, we're on 50 microseconds per division is just over 550 microseconds. So, we can get that exact value. It's it doesn't have to be absolutely spot on, but it should be

**Dave Jones:** close. So, we'll measure that as accurately as we can. And I've used both my cursors there and I'm measuring 562 microseconds for that burst. And you'll notice that the dead period there, where it's well, high, but it's actually

**Dave Jones:** switched off, is exactly the same 562 microseconds. Now, you could be mistaken for thinking that these are individual 1010 bits in here and then you've actually got three zeros here because if you actually go in there and measure it,

**Dave Jones:** this period here is actually yes, it is precisely three times that length there. So, you might think it's one and then 000, but that's not the case because I happen to know that this thing looks precisely like the Japanese protocol or

**Dave Jones:** sometimes better known as the NEC protocol. Now, the unusual thing about the NEC protocol is it doesn't have a fixed bit length for both one and zero. It actually changes between those. So, let's take the example of like it's

**Dave Jones:** ordinarily high. So, let's say the start of the bit is here. It goes low for that one. We'll call that one time period there. Then it goes back high like that and that represents a zero, but a one is represented by it going low

**Dave Jones:** like that for that one time period and then going high again for three time periods. It's like that. So, that in there, so that from there to there is a zero and from there to there is a one.

**Dave Jones:** So, it's quite unusual, but that's the NEC protocol. And you don't have to think of it like that, of course. Well, if you're actually programming this into your microcontroller, then you could think of it as you know, 101000

**Dave Jones:** if you really wanted to, but and you could actually program and implement it successfully that way. But that just wouldn't be the correct way to do it cuz what we're going to find here is that in the total of all this, we're going to

**Dave Jones:** actually have four bytes for a total of 32 bits. Now, of course, to decode that on your scope, some scopes of course have serial protocol decoding, but I have never seen one that actually has the NEC protocol built in. And if your a

**Dave Jones:** scope or your logic analyzer or whatever happened to have a custom protocol decoder for example, then you might just be able to set that up to actually decode it and turn those different time length periods into zero and ones for

**Dave Jones:** you and spit out that four byte code that the NEC control code actually has. But, we don't have that capability here, so we're just going to decode this manually. So, what we can do is go in here after our idle period and that's

**Dave Jones:** the start of our first bit there and we can see that that first one is a one because it's one time period with three blank time periods after that. So, that's a one, one, and then zero, zero, zero, zero. And that's called a pulse

**Dave Jones:** length encoding technique. So, we can go in there and just manually decode these. Not a problem whatsoever and we should get total out of that four different bytes. And I've gone through and manually decoded that and this is what we get. We

**Dave Jones:** get our four eight-bit bytes there. And the first two bytes are the address, so there we go, it sends those, then it sends the command here, and then the inverse of the command like that. So, you should, if you've decoded it right,

**Dave Jones:** this last byte should be an inverse of that one and that's exactly what we see on a bit-by-bit basis. So, now we've got this data, we can program it into our micro. Beauty. Now, to throw a real spanner in the works, something like the

**Dave Jones:** Philips RC5 IR protocol, for example, each time you press the key, it can actually toggle that bit each time. So, what I'm what I've set up here is I've captured this waveform and there's there I've stored it as a reference waveform

**Dave Jones:** here. So, now I'll press it again and see if we get get an identical waveform. Let's have a look. Does it look identical? It does. So, I'll do that one more time. No, we don't have any toggled bits, so

**Dave Jones:** it looks like it repeats the exact same code every time. You've just got to be careful there. Otherwise, you know, that could really ruin your day and changes the equation on how you're going to write your IR driver and stuff like that. And here's

**Dave Jones:** the source code, the sketch I've written for this. Yeah, I could have just used an off-the-shelf library, IR code library. Some of them are quite simple, some are quite complex. There are a lot out there that do support the NEC protocol we're

**Dave Jones:** actually after. And a lot of them are complete receive codes and do all sorts of stuff. But I wanted to write my own because, well, that's the spirit of this thing. And as it turns out, it's very, very

**Dave Jones:** simple. So I wrote it from scratch. The source code for this from a link down below the video here. So I'll be very brief on this. I've set up my LED and my infrared LED on a pin. You can just

**Dave Jones:** define which pin of the Arduino you've got. I've got my bit time, 562 microseconds, as we saw on the oscilloscope. And then I define the infrared code that I want to send. In this case, it's that 4-byte 32-bit

**Dave Jones:** code that we reverse engineered from the oscilloscope. So in binary form, I've got it as one big 32-bit word there. So that's all set up. You can have multiple codes for any command button that you want to send. This one is just the

**Dave Jones:** reverse engineered code for my Canon remote control record stop record button. And then I've got a simple setup routine here that just sets up the pin as an output for the LED. And then it switches the LED off to start with. Then

**Dave Jones:** I've got two simple routines, and that's the entire code right there, just in those two routines, almost fit on that one screen. A couple of dozen lines of code. The first one is the IR carrier, and that generates 38 kHz carrier

**Dave Jones:** frequency. All you do is pass it the time in microseconds that you want the carrier frequency to go for, and then it just goes through a for loop and turns the LED off and on there. Not a problem

**Dave Jones:** at all. Now, it's got a divide that past time by 26 microseconds here because 26 microseconds is roughly the inverse of the 38 kHz carrier frequency that we got. And then all it does is it sets the turns the LED on for

**Dave Jones:** half that period or 13 microseconds and then turns it off for 13 microseconds and it repeats as long as it needs to. And then we've got another routine which sends the 32-bit code. So, you just pass it the code here as a long 32-bit long

**Dave Jones:** value. And then we have the LED generate the leading pulse here as we saw on the oscilloscope. Nine 9,000 microseconds we turn the carrier on for. That's 9 milliseconds. And then we turn the carrier off for 4.5 milliseconds there.

**Dave Jones:** So, it's we've generated our leading pulse. And then all we do is we go in a for loop here and we send out all of our 32 bits or four bytes in sequence. I'm just doing that using a mask here. So,

**Dave Jones:** I'm just masking the most significant bit and then shifting it one bit at a time at the end of it. That's why I did it as a 32-bit word. It's just easier that way than say four individual bytes.

**Dave Jones:** Saves a few lines of code. And then of course uh we well, we start out by generating the one bit time 562 microseconds the carrier frequency. And then we have to determine via that masking if our current bit is a high or a low. If it's

**Dave Jones:** a high, then of course we have to wait the three bit times dead time to signify a one in the NEC protocol. But, if it's a zero, then we only have to wait one extra bit time. Very, very easy. And

**Dave Jones:** that's it. It just repeats for all 32 bits. And one thing I forgot to mention on the oscilloscope capture is I also noticed a uh stop bit at the end of it. So, it was actually had a 33rd bit on

**Dave Jones:** there, just a stop bit of one bit time. So, I've added that in there at the end. And then I've just got a main routine here. All it does is calls the setup, defines the pins, and then it sends my

**Dave Jones:** infrared code to switch the record mode of my camera on. It waits 5 seconds, and then I send the code to stop recording. Easy. And no surprises for guessing it didn't work first go. No, it wasn't Murphy's law. As a matter of fact, I

**Dave Jones:** kind of expected it to possibly not work first go, and I'll show you why. So, what I've done is I've hooked up my logic analyzer here because to analyze something like this, we really need to look at that code output. You can do it

**Dave Jones:** on an oscilloscope, or but a logic analyzer is easier. We can capture it here. Now, I've hooked up my Saleae logic analyzer to the LED output. I'm going to sample at 8 MHz here. Uh more than fast enough. 1 meg samples good

**Dave Jones:** enough. And negative uh edge trigger here. So, we'll start this, and I'll press my reset button on my Arduino. I've already downloaded the sketch. And looky what we have here. We have our code. That's exactly the same as what we

**Dave Jones:** saw on the oscilloscope. And if we go in here, we can look at that carrier frequency of the leading pulse there. And if you have a look on the right-hand side, I can't move my cursor over, but it says the pulse width is 16.8

**Dave Jones:** microseconds, and the frequency is 29.9 kHz. Nowhere near the 38 uh kHz that we actually need. No wonder it doesn't work. Why? Well, it's uh pretty obvious. And uh those people who are experienced with these sort of things

**Dave Jones:** probably already know. Because in my timing loop here, my IR carrier loop, I've assumed that it's 26 microseconds. Okay, I've rounded that down near enough to generate the loop timing in here. That's not going to be a a real major

**Dave Jones:** issue. The major issue here is this delayed microseconds. You see it's got 13. So, we're expecting to get 13 microseconds delay, but look, we don't. We get 16.8. So, there's another what 3.8 microseconds or thereabouts added to that. So, it's not 13 microseconds, it's

**Dave Jones:** 16.8. Uh why? Because well, let's assume that the delay microseconds routine is fairly accurate, okay? It's not going to be absolutely, you know, spot on, but it's going to be near enough. What's taking all the time? Well, the only

**Dave Jones:** other code in here is this digital right routine. And this digital right routine does actually take time. In this case, it takes a couple of microseconds to execute. And there's faster ways to do it, but we're just using the digital

**Dave Jones:** right routine uh cuz that's the basic way in the Arduino. So, let's compensate, tweak this thing. I am holding my tongue at the right angle, and let's take that's let's knock that, you know, three or four microseconds off. Let's change that to nine

**Dave Jones:** microseconds, and let's upload that. We've uploaded. We can go back in here. We can start this again. And run run our Arduino's running. Oops, it's already captured it because I've got an auto start routine in there. And you'll

**Dave Jones:** notice that the timing is different. Look at this. 12.75 microseconds now, and we're close to our 38 kHz. We're now 39.4 kHz. And as I said, you don't have to be spot on, but that's going to be near enough. And as it turns out, this

**Dave Jones:** now works. And sorry about the audio and video quality now. I'm at home actually doing this. I don't have my main camera, so I'm shooting on my old compact. It's night, and well, yeah, it's not going to be very good. Anyway, I have my Canon

**Dave Jones:** camcorder here. I've got my Freetronics 11 down here I've got an infrared LED hooked up and pointed to it via a 220 ohm drop resistor. And if I press the reset button here, it should start recording and then 5 seconds later

**Dave Jones:** should send the code again to switch it off. So, let's give it a go. Bingo, it started recording. And it won't quite go to five because it took a second or two to boom, but there you go. Works a treat.

**Dave Jones:** And just a small trap for young players here. With any sampling system like this, the resolution is going to be dependent upon your sample rate. Now, we're sampling at 8 MHz here and you'll notice that it's over on the right-hand

**Dave Jones:** side there it's saying the pulse width is giving us that to three decimal places or 1 nanosecond resolution. Well, that's obviously complete It's saying it's 12.875 microseconds. It's not possible to get 1 nanosecond resolution on that, but 8

**Dave Jones:** MHz is more than good enough to get the timing requirement for this particular application, but let's resample that at say a lower rate of 500 kHz. Now, if you invert five let's start that, capture it. And here we go.

**Dave Jones:** And if you invert 500 kHz, of course, you get 2 microseconds. You'll notice that there we go. It's jumping between 2 and 14 microseconds, but it's still showing two decimal places beyond that. That's the software not knowing what

**Dave Jones:** it's doing and this might be tricking you into thinking that that pulse width is precisely 14.00 microseconds when it's not. Your resolution isn't good enough to determine that. In this case, this really isn't quite good enough for this particular system. It's almost in

**Dave Jones:** the ball ballpark, but not quite. Anyway, just be aware of that. Trap for young players. So, that's it. Very, very simple to write your own code, reverse engineer a protocol. You don't even need an oscilloscope. You can do it using

**Dave Jones:** very simple and basic tools, a PC or whatever. So, no complex test equipment required here to reverse engineer that NEC protocol. And, you know, not much work at all. Very, very simple. So, I hope you enjoyed that. There were lots

**Dave Jones:** of stuff involved in this, oscilloscopes, reverse engineering, and then we had a little fail there in our source code and tweaking some logic analyzer stuff. It's all happening. Fantastic. So, if you like the video, please give it a big thumbs up. And, as

**Dave Jones:** always, if you want to discuss it, jump on over to the EEVblog forum. And no correspondence will be entered into on the source code. Thank you very much. Catch you next time.
