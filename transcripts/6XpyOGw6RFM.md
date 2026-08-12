---
video_id: 6XpyOGw6RFM
title: Rohde & Schwarz RTB2000 Scope Pulse Response
url: https://www.youtube.com/watch?v=6XpyOGw6RFM
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 44, "4": 57, "5": 73, "6": 92, "7": 110, "8": 122, "9": 136, "10": 152, "11": 167, "12": 185, "13": 199, "14": 213, "15": 227, "16": 244, "17": 258, "18": 275, "19": 290, "20": 303, "21": 316, "22": 328, "23": 343, "24": 358, "25": 369, "26": 386, "27": 401, "28": 420, "29": 435, "30": 454, "31": 467, "32": 478, "33": 495, "34": 514, "35": 531, "36": 547, "37": 563, "38": 578, "39": 592, "40": 609, "41": 630, "42": 646, "43": 656, "44": 673, "45": 688, "46": 703, "47": 714, "48": 731, "49": 742, "50": 756, "51": 773, "52": 788, "53": 801, "54": 812, "55": 825, "56": 839, "57": 855, "58": 868, "59": 880, "60": 895, "61": 908}
---

**Dave Jones:** Hi, just a quick video to confirm something for a new EVBlog forum user Mikey 6 in the very lengthy, I don't know god, how many pages is it? It's been going for years, the Rohde & Schwarz RTB 2000 thread on the EVBlog

**Dave Jones:** forum. Anyway, I've got my old RTB 2004. Mine was one of the first batches, I think, something like that. So, I've got got pretty much original hardware. So, well, I can take a look at the hardware.

**Dave Jones:** For those playing along at home, I have got hardware XO3. In fact, I tweeted the other day that the Rohde & Schwarz has by far the best firmware update procedure of any scope. It's so simple, it's so easy. You just stick the

**Dave Jones:** firmware file, which you don't have to register for on the website. You just download it, put on the USB stick. It says before and after. And anyway, anyway, so Mikey posted about how there is a low frequency performance, like

**Dave Jones:** pulse response, a low frequency sort of response of the scope on a basic 1 kHz square wave. So, I thought I'd try and reproduce it here. And I'll put Mikey's original one here. And this is the response I get. I'm I'm at a higher

**Dave Jones:** volts per division. Basically saying that anything over 200 mV per division has sort of like a sloppy sort of like a performance after the initial rise, like this. And sure enough, mine actually seems to confirm that. So, I'm actually

**Dave Jones:** feeding in a 4 and 1/2 V peak-to-peak signal, 50 ohm terminated BNC. I didn't have my in-line terminator. I don't know where it is. But anyway, hopefully that is adequate cuz there's no 50 ohm internal termination on this. But yeah, you can

**Dave Jones:** see that it is kind of sloppy. Let me move that on the line, okay? Right on the line. And I have got 20 MHz bandwidth limit on, so I'll run that in real time for you and I'll show you that

**Dave Jones:** response. And if we zoom in, we can see that is the that is the peak response. I'm sorry about the the screen is very glary on the TV. I did have a matte screen thing, but I haven't put it on. So you can see it's nice, but

**Dave Jones:** it doesn't Yeah, you see how it's just it's a little bit droopy there where it's what 100 microseconds per division. So there's like a good 50 microseconds of droop there before it gets up, but I it looked worse. It kind of looks worse and

**Dave Jones:** a bit more sloppy, I guess you could call it at a longer time base like that, but you know, so like there's no overshoot there, but there's definitely some like definite like low frequency undershoot there. It it is taking time to sort of

**Dave Jones:** like ramp up. And here's the exact same signal on the new HDO 4000 Rigol here and you can see that it is a very nice response. I've got it I'm just adjusting the vertical fine so that it gets higher

**Dave Jones:** volts per division, but there you go. See, some there's some droopiness here. This is full bandwidth though, I believe. So let me You can see the response there. We can turn on the bandwidth limit on here and boom, then

**Dave Jones:** all of that whoop. Hello. All of that overshoot goes away, but then once again, it takes a little bit of time to get up there. What 2 microseconds? It doesn't take the 100 microseconds, but you know, you can

**Dave Jones:** argue that there you go. It's a little bit little bit peaky there. Geez, you know, we're we're faffing around the edges here, but of course this is going to be all of this stuff we're going to be looking at is to do with the linearity

**Dave Jones:** of the end response, the pulse response of the front end cuz designing and attenuator front end to actually give you a good pulse response at both low and high frequencies with like a voltage divider in there that is like it's

**Dave Jones:** pretty you know it's it's not easy. So scopes are going to have different sort of like lower frequency and higher frequency pulse responses even though here when we're talking about you know the rising edge here and then that

**Dave Jones:** little bit inside there that is the high frequency pulse response of that. That's why when we bandwidth limit it, you know, we don't we we cut off all the high frequency ringing response content in there. But anyway, that is the Rigol. So that looks

**Dave Jones:** very nice. And the Keysight here, there you go. It's a bit fuzzier because it's got a well is the bandwidth yeah bandwidth limit off bandwidth limit on. So horizontal we can go in there if we turn the bandwidth limit off then yeah you

**Dave Jones:** can see it start to see the ringing of course that's what you'd expect. And but bandwidth limit off but this is fuzzier so we're probably going to have to turn on some can we put on high res mode? There you

**Dave Jones:** go. We can put high res mode on there. And you can see though the response there once again you know it takes a little bit you know 50 20 microseconds or something to get up there. It doesn't it's you know but

**Dave Jones:** we're down in the pixels there right where where down in the pixels. And the new Tech 2 series this is interesting check it out goes up and then there's a slight dip back down. So it's got a very

**Dave Jones:** different pulse response. That's where the 20 megahertz bandwidth limit there we can turn that off of course and then we can get the full 500 meg and it's the same like actual sort of like lower frequency by lower frequency I mean like

**Dave Jones:** 20 megahertz response. But of course if we zoom in then we're going to see our real high frequency content. And once again, that will bugger off if we turn on our 20 MHz bandwidth limit. But yeah, you can see you can see in here once we

**Dave Jones:** sort of like expand this out. What are we at? We're at 2 microseconds per division now. So, and then you can see it go down. Like you can see like we're sort of like individual pixels here, right? So, only talking a couple of

**Dave Jones:** samples, right? But it does actually drop back down and then goes up a few samples. And then So, there there you go. That's a different pulse response. Again, sort of like a lower frequency pulse response to this 1 kHz signal.

**Dave Jones:** Now, let's see if this changes with different volts per division settings. So, okay. Interesting. I'm now at 500 mV per division and we get like an overshoot on there now. Once again, that's kind of like a couple of pixels

**Dave Jones:** in the other direction. There you go. So, slight overshoot there. Once again, right? This is 50-ohm input terminated, right? 50-ohm source. By the way, I'm using my Rigol DG4162 function gen here to generate a just a basic 1 kHz square wave. So, there you

**Dave Jones:** go. That's interesting. We're getting like a couple of pixely overshoot there. But the Once again, if we go back to the Rohde & Schwarz, let's try a different volts per division setting. Now, I'm at 100 mV per division

**Dave Jones:** and check it out. We're not There's a little bit of it going on there. Well, let me expand that. But that looks pretty good, right? That looks pretty schmick. Uh, maybe maybe you can see some like wobble in there, can you? Like uh, there's a

**Dave Jones:** little bit of like Well, we're talking a couple of pixels here, couple of samples. Yeah, it's just like it's really hard, but you can kind of sort of see the response is a little bit wobbly there. So, this is the setting

**Dave Jones:** that he said it was okay. So, I'm going to go to 200 mV per division and crank it up.

**Dave Jones:** There you go. So, yeah, it it's kind of sort of confirmed to what Mikey saw that there is sort of a a kind of a non-linear um lower frequency response there. Oh, by the way, check this out on the new uh

**Dave Jones:** Tech 2 series. This This has to be deliberate, okay? If I actually uh press the auto set uh button, where is it? Uh auto set down here, then watch what happens to the volts per division. 2.6 2.6 volts per division. It actually goes

**Dave Jones:** to the fine the auto scale auto set function goes to the fine scale of your volts per division. Um I I don't think any other scope I've used has ever done that. I presume that's a deliberate feature like it but

**Dave Jones:** it hasn't even made it like, you know, what why not make it bigger than that? I mean, it's just it seems a bit silly. So, let me set it to say here and then auto set it again and see what happens.

**Dave Jones:** It's gone to 3 volts per division. Three. So, it obviously go and the algorithm auto set algorithm says, "Okay, it must leave at least a division top and bottom somewhere between, you know, like somewhere between maybe the second

**Dave Jones:** division top and bottom. It needs to be in there." And then it selects a fine um volts per division setting. And but of course, you know, like you can just override that of course just by uh going like that again, but like I

**Dave Jones:** I don't know. You're either going to love that or you hate it. Let's have a quick look at the Siglent SDS2354X Plus. Geez, they've got complicated names. Um this one looks pretty good. That's with no bandwidth limit. Uh

**Dave Jones:** how do we go? I haven't used this forever. 20 meg bandwidth limit. There you go. That looks pretty schmick. Oh, no. Hang on. No. Check that out. It's got something at the beginning. There. There you go. Yeah. Yeah, there's a little droopy

**Dave Jones:** droop there. And here's the Uni-T Ultra Phosphor UPO3254E. Geez, imagine trying to remember all these numbers. Um anyway, this one's pretty schmick, isn't it? There you go. Just happens to be really good pulse response, but you know, you change it, you go down to a

**Dave Jones:** different volts per division, and you might get something else entirely. No, just some high frequency overshoot there. That's a 20 millivolts per division. It's giving a decent show for itself. Back to the Rohde & Schwarz again at 10 millivolts per division, and

**Dave Jones:** yeah, you go. You can see it sort of goes There's a little dip, and then it sort of slightly goes up. We're only talking a couple of samples here, but you know, there you go. So, a bit This

**Dave Jones:** is not really unexpected, because as I said, it's quite difficult. We're talking about the pulse response of and the compensation of the attenuation circuit of the front end, the voltage divider and attenuator. And you're going to get And you can potentially get a

**Dave Jones:** different response depending on which volts per division setting you've got, depending on where in the voltage divider ladder it is. If you're right at the top tap, of course, then you're going to get, right, a potentially better response than if you're

**Dave Jones:** getting somewhere other tap down uh voltage divider, and then you're talking about compensating your resistive voltage divider and the pulse response of compensating the resistive divider there. And then you've got low and high frequency compensation, and you know,

**Dave Jones:** all sorts of variables that goes into that. So, if you want to test an oscilloscope properly, you would have to actually test the pulse response with a known good input signal. I've only tested one function gen here, right?

**Dave Jones:** Known good input signal. Um on every single voltage range, and it has to be correctly terminated and everything else. And you'd have to do it with the 50 ohm termination and without the 50 ohm termination potentially. And And then, like, you can try and test the

**Dave Jones:** pulse response of scopes until the cows come home. But the worst one I've ever seen, I think, is the Tekway one. Oh, that was donkey's years ago now. I'll try and put in a screen capture of the pulse response of the Tekway, and it was

**Dave Jones:** just all over the shop. Oh goodness, it was terrible, Muriel. So, anyway, it's something worth you know, inspecting on your own scope. Actually, let me briefly um try and just get another source here, signal source. All right, here you go.

**Dave Jones:** This is slightly different again, is it? This is using the sig gen output on my Keysight 3000 scope. So, the wave gen output there. And you can see that it's kind of like got almost a ringy kind of response

**Dave Jones:** there. Huh. And that's the same signal on the Rigol HDO 4000. Once again, a little bit of overshoot there, but yeah, like, you've got to take into account the signal source and everything else. But there you go. Um a pulse response is

**Dave Jones:** certainly something to uh consider on a scope. But it's worth investigating. It's an interesting phenomenon, and not every scope is perfect. And then, as I said, it can change depending on the volts per division, at what range you're

**Dave Jones:** actually on on your scope. Cuz it can They can have slightly different low and high frequency compensations on each range. And it's not like, you know, there's a little trimmer there like back in the old days. And you used to have

**Dave Jones:** little trimmer pots, right? Um so that you can with your tongue at the right angle tweak the response of each of the resistor divider steps. But even then, like you might have to have multiple compensations for high and low

**Dave Jones:** frequency response. And uh it's it gets really ugly. Um so yeah, just because like, you know, we saw that the Uni-T is spotted on there, it doesn't mean that, you know, it's absolutely exceptional. So yeah, it's not something

**Dave Jones:** I'd worry about too much unless it's absolutely horrific. Um it's just like an interesting quirk of scope front ends and the complexity of trying to implement a voltage divider over a frequency range like this. And ultimately, of course, when you get a

**Dave Jones:** square wave with a rise like that, like you'll never see this distortion on, you know, like a a ramp waveform, for example. It's just It's just moving too slowly. But when you get square wave with a pulse a step response like this,

**Dave Jones:** which has high frequency components in it depending on the slew rate, then the response after that can, you know, do interesting things. And you see, like if we turn the bandwidth limit off, then you can see you start to see the

**Dave Jones:** overshoot and stuff in there. Start to see the ringing and you know, like transmission line effects in there, termination effects and stuff like that. And that's when, you know, at at the high frequencies, like having the difference between having your 50 ohm terminator

**Dave Jones:** here and having an in-line one like really could make a difference. But in this particular case that we've been looking at, it makes no difference at all cuz we're looking at sort of the lower frequency response like the sub-20 MHz

**Dave Jones:** type response here. But there you go. Hope you found that interesting. And if you did, give it a big thumbs up and leave your results for your scope down below. Catch you next time.
