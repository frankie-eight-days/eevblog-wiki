---
video_id: CaxzxEB44Vs
title: EEVblog 1745 - Continuity Tester Spectral Probing
url: https://www.youtube.com/watch?v=CaxzxEB44Vs
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 46, "3": 84, "4": 109, "5": 128, "6": 159, "7": 185, "8": 204, "9": 217, "10": 232, "11": 255, "12": 275, "13": 303, "14": 333, "15": 362, "16": 390, "17": 405, "18": 443, "19": 475, "20": 508, "21": 540, "22": 560, "23": 593, "24": 605, "25": 623, "26": 640, "27": 669, "28": 699, "29": 725, "30": 740, "31": 757, "32": 781, "33": 798, "34": 830, "35": 842, "36": 854, "37": 872, "38": 884, "39": 918, "40": 945, "41": 976, "42": 1005, "43": 1024, "44": 1046, "45": 1062, "46": 1093, "47": 1125}
---

**Dave Jones:** Hi, I'm down here in the bunker with a follow-up video to one a very quick one I posted on the EVblog 2 channel about the new stock BM2257 multimeter available on the EVblog.store. Down below, I'll even put a coupon code in the description so you can get a discount. Got brand new stock, no worries. Anyway, this new stock actually has a new firmware version 2506 as opposed to 2503, which is the original release one. And basically, the only major difference between these releases is that they've changed the

**Dave Jones:** continuity frequency in the thing. So, let's go over here. We'll go into continuity. I'll turn the backlight on cuz it's a gorgeous orange, and we should be able to hear the difference. Here's the original one. There you go.

**Dave Jones:** That is supposed to be 2.5 kHz, and the new one is supposed to be 2.7 kHz. And sure enough, it does sound a higher frequency. Now, I asked Brymen, why did they make that change? And they said, "It's to make it a bit louder." And well, to my crusty old ears, it doesn't necessarily 2.7 kHz in the the new firmware version doesn't sound as loud as the loud, in quote marks, as the 2.5 kHz version here. Presumably the same buzzer, they're just driving them in different frequency, of course, which

**Dave Jones:** is why they can change it in firmware. It's just a piezoceramic uh transducer, not a piezoceramic buzzer. A buzzer is a piezoceramic transducer that has a built-in oscillator. So, you just give it 3 V or whatever, and it just buzzes at its own internal frequency. But a piezoceramic transducer is just the transducer on its own. You need the external drive to make it go. So, that's what's going on here.

**Dave Jones:** So, yeah, it doesn't sound louder. I think we're going to have to bring out the big guns here. Thankfully, I've got a beautiful new bit of kit that's just going to do the job perfectly here. Thank you very much, Cry Sound. You might have seen them in a recent video.

**Dave Jones:** Yes, I haven't reviewed it yet. It's that acoustic imaging camera. Very cool bit of kit. But, they also sent this in because they make more than that acoustic imaging camera. Oh, look at this. It's a Bobby Dazzler. Always wanted one of these. Thank you very much, Cry Sound. We've got the calibration chart for the 1/2-in free-field microphone here. There's the response for those playing along at home. Beautiful. It's got your uh you know, your volts per pascals and everything. Um and we've got a sound level meter. But, it's not just any

**Dave Jones:** sound level meter. It's a class one sound level meter. And there are various classes, and class one is the best. It's the measurement instrument grade uh one that you take on site, you know, and you want to measure your noise out in the field or something that it's you know, over above some limit. Um that's what you need a class one meter for. They're way more accurate and uh more betterer than the regular like uh class two ones.

**Dave Jones:** There it is. Class one. Oh, winner winner chicken dinner. Got a tripod mount. We've got a replaceable microphone on the thing. The capsule is Oh, no. That's just the top. >> [laughter] >> That's just the top part of it. You can't actually get the Oh, you have screwed off down here.

**Dave Jones:** Yeah, you can't actually get different uh capsules for it for different uh ranges and different uses and stuff like that. So, there it is there. Look at that. That's a Bobby Dazzler. Anyway, so that is very specifically calibrated.

**Dave Jones:** It's got some numbers on there. Sorry, very hard to see this. Type something or other. And individually serial numbered. And that's what the calibration certificate is going to be for. It's going to be for that specific measurement microphone.

**Dave Jones:** So, this is a proper industrial measurement bit of kit. I'll put the link in down below. I'll put the They're not particularly cheap. You can't get like class one meters for under like, you know, four digits. So, yeah, anyway, we've got a just a USB cable and there's nothing else in there. Oh, anyway, comes in a nice Pelican type case. Winner, winner, chicken dinner.

**Dave Jones:** So, we're going to do some acoustic measurements today, which is why I'm down here in the bunker. There's a reason I'm in the bunker because it's the quietest place that I've got. It's quieter than my dungeon, definitely with that I've got stuff running down there all the time and there's all sorts of cars running around and all sorts of things, but the bunker is literally an underground bunker.

**Dave Jones:** Underground car park bunker, but it's underground. So, it's pretty quiet in here and I've just if you see my EV blog two video, I can now just had this installed, I can now switch on and off not any various lights, but also the ventilation fan in here. So, it's very quiet with no ventilation fan. So, this won't be a comprehensive review of this bit of kit, but yeah, I just want to do some measurements to see if I can do it without a proper acoustic test

**Dave Jones:** chamber, if I can do it down here in the bunker, if it's low noise enough. And you can see that the foam here it's got a split in the middle because that is exactly where the microphone is going to be because when you're doing acoustic measurements, you do them at a specific distance. So, if you've seen a specification for fan noise, for example, it might be, you know, 45 dBA, we'll go into that in a minute, dBA waiting at 1 m. They'll specify a distance. So, you want to take your

**Dave Jones:** distance from your from that center line, which is where your microphone is to your device under test. And for you film aficionados, I know you want to see it, so here it goes. Woah, beautiful. All right, let's switch this sucker on and it's got all sorts of Oh, yep. Here we go. Haven't showed you this. It's got LAN interface. It's got SD card because it can do data logging and it's got internal rechargeable battery but USB and all sorts of stuff.

**Dave Jones:** I haven't tried the measurement PC software or whatever it is for it yet but cry sound measure sound better. But yeah, can't believe I've got now got a class one microphone. Thing of beauty. Joy forever. Um yeah, I can't go through all the features on here but we yeah, we can do like calibration. We can SLM is sound level meter so that's just you know, your regular sound level meter. You can get statistics and we'll definitely use our FFT here but like if I go into the sound

**Dave Jones:** level meter for example, that will just give us well, not just a basic sound level meter. Here we go. You can hear me talking actually if I shut up for a second. We're looking at LAF which is A-weighted.

**Dave Jones:** Shut up, Dave. 33. That is higher than what I was hoping for. So, yeah, even in the bunker down here, it's not as good as I was hoping for. Anyway, the noise floor of this thing is like 18 dBA or something crazy like that. Anyway, we've got L stands for loudness. So, we've got that's LAF. So, A-weighting, we've got C-weighting and we've got Z-weighting as well and then then the A-weighting frequency max and can change all these parameters. You can go into content here and you can actually set up

**Dave Jones:** what what things you want in the various positions. So, we can change any one of those for example like if for SPL sound pressure level, we can set it for any one of these parameters. It's just it it it's super comprehensive. This is a very professional bit of kit. But the The between A-weighting, C-weighting and Z-weighting down here is basically how they filter the response. A-weighting is you know, the one you'll be most familiar with as I said, like fan specifications, noise specifications for instruments, like a loudness thing,

**Dave Jones:** usually A-weighted. That means it's it's filtered to match kind of like the frequency response of the ear cuz the ear is not very linear. So, yeah, it's and designed for like lower noise type stuff, not really loud stuff. have to really loud stuff, then you want a C-weighting there and it has different filtering for different I won't go into the specific details, but if you're doing instrument measurement calculations, you want a flat frequency response, not all this filtering rubbish, you want your Z one here. So,

**Dave Jones:** let's shut up again. And you can see that Z was down there around about 70 or thereabouts. So, yeah, we're going to be working with the A-weighting today because that's what it sounds like to your ear because it's what we care about when we care about loudness in quote marks, how loud is this thing louder than the other one at the different frequency. We want to use A-weighting. All right, so I've set it up on a tripod here and I've put it 1 m away there and it's on the tilting

**Dave Jones:** bail like that cuz that's how you'd typically have it. And I know some people will fuss over this. The 1 m, I've actually put it whereabouts the buzzer is on the actual PCB. It is up the top end of the PCB. Anyway, as long as we're consistent, good enough for Australia.

**Dave Jones:** So, as you can see, I've probably got down to about 33 dBA reading there, just the ambient noise. Now, I was hoping for better than that cuz I know this bit of kit is capable of doing that. So, there's actually going to be low frequency noise here in the lab due to like some you know filtering outside in the car park which is opposite the concrete well the besser block wall behind me here and that's filtering into here and we can see that if we go to our FFT.

**Dave Jones:** So you can see on our FFT there that it was down in the low end and you can hear me talk at the moment but we can't actually zoom in on this. Touch screen's a little bit often can't get it right.

**Dave Jones:** Not sure what the deal is. Anyway, we can press the button there and we can zoom in and then so we've got a narrower frequency range here and that's actually up to 60 hertz there. You can obviously see that even though I'm talking there's not much energy in my voice at 60 hertz.

**Dave Jones:** So we can actually sweep along until we start seeing where my voice see how low my famously low voice can go.

**Dave Jones:** I can actually get down to well whatever that was. I can get down to 150 hertz there. But as you can see there there's a good lot of low frequency noise there like you know below like 60 hertz or somewhere like that and that's what's contributing to that general A weighted sound pressure level reading that we were getting there. So if I want anything better I'm going to have to design and build my own acoustic test chamber and it's going to have to filter if I want to use it here

**Dave Jones:** it's got to filter out that really low frequency noise. So if you get got any good ideas on how I can physically construct that especially to filter out like you know that sub sort of like 100 hertz kind of frequency stuff. It's going to have to be like really thick acoustic stuff to try and you know deaden all that sound out. Have you got any ideas how I can construct one of those apart from completely refitting the whole bunker, please leave it in the comments down below cuz I'd love to do a project

**Dave Jones:** build for just a you know a fairly rudimentary. It's got to be like a meter long so that you know you can test at the standard 1 meter length. I'd love to build like a portable kind of thing or you know something that I can even have semi-permanent down here in the bunker. But anyway, that's where my problem is. So let's go up to 2.5 kHz, shall we? All right, so it's supposed to be around 2.5 kHz here. I'll measure the old one so let me flip that around and

**Dave Jones:** switch in on the 2.5 kHz, the older firmware. Oh, it's 2.7. What? Supposed to be 2.5. It's actually the same. And there's the other one, 2.7. No.

**Dave Jones:** Come on. There it is. 2.92. Okay, it's a bit different to what they told me but uh around 58.2 uh DBA waiting for the new one.

**Dave Jones:** No, that's a good 9 dB louder there for the older one. I thought my ears weren't going crazy. The older one is at the lower frequency is louder. It's louder than the new one. So busted. I'm going to have to go back to Brymen and go show them this video and the measurement doesn't lie. It's at 1 meter. Trust me. There it is there.

**Dave Jones:** Um so I'm not sure what the deal is. And she ain't no sine wave. Look at that. Look at those harmonics. Well, they told me that the old one was 2.5 kHz. Um it's not. It's 2.7 and the new one, here we go.

**Dave Jones:** Yeah, we're not measuring it at distance anymore. Just getting it on camera. Whoop. It is definitely 2.93 kilohertz. So, there you have it. That's very interesting. There um it doesn't seem to be louder, this new one. In fact, it seems to be a bit softer. So, I bet some people's hearing might be different. There's some people might say, "Well, I know I like that higher frequency uh buzzer much better." Leave it in the comments down below. I'll give you a listen to it. Here's the new one

**Dave Jones:** using the internal uh good internal road mic on my camera. And we'll compare that with the older one.

**Dave Jones:** Let us know which one you think's better in the comments down below. And because this is a high frequency uh well, relatively high frequency thing. Um to to trust me, I come from the seismic industry, underwater seismic industry.

**Dave Jones:** 200 hertz was high frequency. Um the anyway, um it's going to vary um like, you know, depending on the orientation of the product as well. But, I had the uh product in the same orientation. But, I'll just try something different. I'll have it at uh say 20 cm here like this.

**Dave Jones:** And, you know, whatever that is, it doesn't matter. I'm just trying something different. And here we go. This is the uh old one.

**Dave Jones:** 65.4 dB, new one. 63.8. So, not as dramatic a difference. What we had 9 dB different um before, which was very dramatic. That was at 1 m. And then you got the acoustics of the room and everything else. Um but, by having it in a different orientation and closer in a different angle and everything else, um it is still lower. So, there you have it. Thoughts and comments down below. And as I said, if you got any idea how I can build myself a good low like a low frequency

**Dave Jones:** acoustic chamber, um I I love to make that a a build a project as long as it's not too expensive or too complicated. So even leave it in the comments down below or even more better, link down below is the specific EV blog forum thread. I have one for each video, so I'll link that in down below and please comment on there and we can discuss the build of an acoustic test chamber, which would be very cool.

**Dave Jones:** So like I'd love to be able to do like fan noise measurements for example on oscilloscopes and other products and you've got to have a good acoustic chamber. As you saw here with this frequency response, it's all like all low frequency stuff, which even down here in the bunker which sounds reasonably silent, but if I shut up for a minute and concentrate, I can actually kind of hear that low frequency content. It's all right down there at that 60 hertz range.

**Dave Jones:** It's all right down there at that 60 hertz range, which isn't my voice and that's the kind of frequency response you'll get from, you know, air conditioning ducts and things like that cuz they're very long wavelength stuff. I think I measured my lab the air conditioning duct in my lab once and it was like 115 hertz or something like that. So yeah, but anyway, this is a very cool bit of kit. Thank you very much Cry Sound class one meter, which I think the I'll put up the specs here. I'll overlay

**Dave Jones:** them. It's very capable of doing even the lowest low noise fans like virtually silent fans. I should be able to measure as long as I've got a good enough acoustic test chamber that filters out that low frequency noise. So and of course when you got fans, you know, it is a pretty low frequency kind of thing.

**Dave Jones:** So yeah, got to have a good acoustic chamber. I thought the bunker would be better, but nah, it's not. Eh, anyway, can't win them all. Hope you found it interesting. If you If you please give it a big thumbs up. As always, discuss down below. Thank you very much Crysound. I'll link their products down below. They're great. They don't just make sound level meters and that cool acoustic imaging camera, either.

**Dave Jones:** Catch you next time. OH, I TOTALLY FORGOT TO measure what difference it makes now that I've got the switch that can turn off the ventilation fan in here. So, let me shut up.

**Dave Jones:** 34-ish. All right, ventilation fan coming on. Yeah, that's a good 10 dB louder. There you go. You might not be able to hear it much on camera, but it makes a difference. I can definitely hear it. Check out that FFT response, too. Wow, big difference.

**Dave Jones:** There's some more higher frequency content up there in the 500-600 Hz region. 1400 Hz there. There's some stuff.

**Dave Jones:** Yeah, it's kind of like all over the shop. It's like there's no specific like frequency tone, I guess, coming from the ducting. It's just a generally broader peak just down there at the lower end. Hmm.
