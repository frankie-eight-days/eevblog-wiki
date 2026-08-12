---
video_id: DMXiD3dKYJc
title: EEVblog #778 - Oscilloscope Vertical Confusion
url: https://www.youtube.com/watch?v=DMXiD3dKYJc
source: youtube-asr
---

**Dave Jones:** Hi, this is a quick beginner tutorial that answers a question from a new user called never die on the EV blog at forum. And I actually see this one quite a lot. When they get an like one of

**Dave Jones:** these modern digital oscilloscopes for the first time, they read the data sheet. Oh, it's capable of going down of 1 mV per division. One division on the screen equals 1 mV. That's its lowest setting. But, when they they might take

**Dave Jones:** the thing out of the box or they're playing around with it and they might find that well, they can't get that setting. It only goes down to 10 mV per division. What's going on? Now, if we take a look at the Rigol DS1054Z here,

**Dave Jones:** one of the most popular beginner oscilloscopes, you'll notice that it's got a vertical attenuation setting that goes anywhere from 1 mV per division all the way up to 10 V per division. But, sometimes what can happen, you either

**Dave Jones:** get the oscilloscope out of the box or you've been playing around with it and you might see that you can't actually get that value. Now, here it can actually go to different readings. It can go up to 100 V like this, but more

**Dave Jones:** importantly, what the questioner asked is that it he could only go down to 10 mV per division. And it doesn't matter whether he's got his probe set to times 1 or times 10. It makes no difference. He can't get down to 1 mV per division

**Dave Jones:** that he wanted. He wanted to measure low-level signals and he can't do it. So, what's the problem here? Well, to an experienced oscilloscope user, it's really easy and obvious, but to the beginner, not really so much. Let's have

**Dave Jones:** a look. If we actually go into our channel 1 vertical menu here, then you'll notice that the probe setting is at times 10 and that is the problem. You just go in here, hit that, and you go to

**Dave Jones:** times 1 because if you're using a times 1 probe, that's what you need to hit. And bingo, it drops from 10 mV per division down to the the of 1 mV per division. That's all it is. So, for this

**Dave Jones:** volts per division setting here on your oscilloscope to be correct, you must ensure that your probe setting here actually matches what you switch on here. If you have it on times one, you use times one. If you go and then switch

**Dave Jones:** that to times 10, you have to go in here and switch it to times 10. Otherwise, your vertical reading here is not accurate at all. You're going to be an order of magnitude out. Now, the important thing to remember here and

**Dave Jones:** what confuses a lot of people is that your the input to your oscilloscope, all those ranges, those different selectable vertical ranges from 1 mV per division to 10 V per division, they do not change. They are fixed in the hardware.

**Dave Jones:** They got physical amplifiers and attenuators in there to do that. When you actually go in here and change this probe setting, all it's doing is it's a software function that just changes the multiplier down here. So, if we put it

**Dave Jones:** to times one, it's 1 mV. If we put it to times 10, it's like that. If you've got a times 100 probe, like a real high voltage probe, or if you've got a times 1,000 probe, for example, you can go in

**Dave Jones:** here and the minimum you can go down to is 1 V per division. And the highest you can go up to is an insane 10 kV per division. Of course, this oscilloscope is not capable of 10 kV per division. You need one of those

**Dave Jones:** real proper high-end professional high voltage probes. But it allows you to just to set that manually. So, it allows you to use any type of custom probe at all, including amplifiers as well. If like in the case of a typical switchable

**Dave Jones:** times one times 10 like this, times one of course the signal just goes straight through. Times 10 is actually a misnomer. It's actually a divide by 10 probe. It's got a 9 meg resistor in here, 1 meg input impedance. It actually

**Dave Jones:** divides your attenuates your signal by a factor of 10. So, the 10 times that it actually shows on the probe here. Um, that's like a think of that as a reminder to set it to 10 times here on

**Dave Jones:** your probe uh setting on your menu. But, if you had an external times 10 amplifier, for example, you would set it to .1 uh probe like that. So, you've actually got an an external amplifier that's amplifying your signal, and you'll get

**Dave Jones:** the correct setting down here. It's all to do with software, nothing to do with the hardware range of the input here at all. And that's one of the limitations of cheaper oscilloscopes like this Rigol DS1054Z. It doesn't have what's called auto probe

**Dave Jones:** detection interface around here. So, the software in this oscilloscope does not know that you've changed that setting, that you've added in a divide by 10 divider. So, it has no way of knowing that you've flicked that switch. So, you

**Dave Jones:** have to set this manually. And it has this weird error message that says parameter limited here. And that's just a little quirk of the Rigol oscilloscope, by the way, if you wanted to know that. It just means that you've

**Dave Jones:** reached the bottom limit of your setting here. So, that's another question they ask. It's nothing to worry about at all. I don't like the way Rigol do that. Higher-end and more expensive oscilloscopes like this Keysight 3000X series will actually have what's called

**Dave Jones:** an auto probe interface around the connector down here. Now, this will automatically detect the particular type of probe you got and automatically change that probe setting, that times one, times 10, or whatever particular type of probe you use. It'll auto detect

**Dave Jones:** it. So, if you've got a matching probe for the oscilloscope here, you'll notice that it's got this little tiny pin in there, which when we plug it into here will actually make contact with that gold ring around the outside there. And

**Dave Jones:** this actually contains a resistor in it, and it will actually be able to measure that you've hooked on a particular different type of probe. And and different probes can have different uh, mechanisms. Some probes even are intelligent and they can use like an I

**Dave Jones:** squared, uh, C type thing and things like that. Uh, a digital identification method. But watch this, okay? It's currently set for a probe of one to one, okay? This is channel one. So it thinks there's, because there's no probe

**Dave Jones:** attached, it knows that it's going to be, or it assumes it's going to be a times one probe. But if we plug in this matching probe, watch this change up here instantly. Bingo. Look. Times 10. But of course you have to use the proper

**Dave Jones:** matching probe for this particular type of oscilloscope. If you try and use this Rigol oscilloscope probe, it doesn't have that pin on there. So if you actually go and plug that in, look, it just stays at, uh, one to one probe, a

**Dave Jones:** times one probe, because it doesn't know that you've plugged in anything special. And if we get another advanced oscilloscope like this Tektronix 3000 series, you'll notice it also comes with a pretty fancy looking probe. This is a 1 GHz one. And once again, it's got that

**Dave Jones:** detection pin on there, plus the circle actually surrounding. Now as I mentioned before, this Tektronix probe is actually one of these smart probes. It's actually, uh, got a communica- single pin communication system there, even though there's all these extra pins

**Dave Jones:** around here. These are supplying for external power for different types of probes, but there's actually a, uh, chip in there that contains the serial number, and you can actually transfer the settings for this particular probe from one channel to the next channel. So

**Dave Jones:** if we actually plug this in here, you'll notice that we're 1 mV per division. We plug it in, it says a times 10, uh, probe. Of course, it doesn't actually, uh, tell you that on there, but all professional, uh, oscilloscope probes

**Dave Jones:** are times 10 only. So I'll explain that in a minute. Now if we plug that in, it go- it knows that it's a times 10 probe, so it goes up to 10 mV per division. That's now our absolute minimum. We

**Dave Jones:** can't go any lower than that, but you'll notice that it's now got a serial number detected in here. It knows its attenuation is times 10, and it actually tells you that here that you can actually store the compensation results

**Dave Jones:** for this particular probe, and then it'll move it from channel to channel. So, you don't have to actually re-compensate the probe every time you're moving your probes around. It's actually a terrific feature. Now, although this is not guaranteed, if we

**Dave Jones:** take our Keysight probe here, it does have our detection pin, and we actually plug this in, will it actually change? Yes, it does. It changes to the 10 mV per division. So, it knows you've plugged in a times 10 probe. So, if we

**Dave Jones:** take our cheap ass Rigol probe, which doesn't have the times 10 um tip on there, then we plug that in, and we're still at 1 mV per division. So, in that case, we have to actually uh go into here, into our probe setup, and

**Dave Jones:** we have to set our attenuation uh manually here with uh There we go. With the control knob, we have to go up there. A little bit fiddly to times 10. And this isn't just a trap for young players, either. Even experienced

**Dave Jones:** engineers can get caught out like this. If you're using these switchable times 1 times 10 probes, it's so easy when you're just handling these or moving them around on the bench to bump that uh that switch on there. And and it's not

**Dave Jones:** really immediately visually obvious that it that there's anything wrong there. And it doesn't matter what oscilloscope you use this on, uh there is no way to actually detect that you've got times 1 or times 10 there unless you use a

**Dave Jones:** proper professional probe. But, you'll notice that the professional probes never ever have this switchable times 1 times 10 on there. And there's a good reason for that. And click here if you haven't seen it. I've done a separate

**Dave Jones:** video on why these uh probes, times 1 times 10 probes, particularly in the times 1 position, uh actually quite poor. Unless you're using them to get the you know, for really low-level signals, they're actually their bandwidth and performance

**Dave Jones:** is quite poor in the times one position. So, click here if you haven't seen that video. And the other thing the forum user asked about is why is there so much noise on the lowest one millivolt per division setting? Even if I disconnect

**Dave Jones:** the probes here. Look. There Look, it's pretty horrible like that. Once again, I've done a video on that. So, click here if you haven't seen that and I explain why this is the case. Noise floor on oscilloscopes and also why digital

**Dave Jones:** oscilloscopes can actually appear noisier than old-school analog ones as well. I've got two videos on that. So, click here if you haven't seen them. I recommend it. So, unless you're working on low-level stuff, I don't recommend these switchable times one times 10 probes.

**Dave Jones:** They can be a real pain in the butt. You can get easily caught out having the wrong scale factor here. Happens to professionals all the time. You just miss it. Annoying. Anyway, I hope you found that useful. If you did, please give it a big

**Dave Jones:** thumbs up on YouTube cuz that always helps a lot. I think the thumbs in the other direction on YouTube. If you want to discuss it, go on over to the EV blog forum. Catch you next time.
