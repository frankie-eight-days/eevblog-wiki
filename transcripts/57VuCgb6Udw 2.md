---
video_id: 57VuCgb6Udw
title: EEVblog 1392 - No temp probe? No problem!
url: https://www.youtube.com/watch?v=57VuCgb6Udw
source: youtube-asr
timestamps: {"0": 0, "1": 28, "2": 40, "3": 59, "4": 90, "5": 103, "6": 140, "7": 166, "8": 196, "9": 224, "10": 245, "11": 271, "12": 303, "13": 334, "14": 350}
---

**Dave Jones:** Hi, just a quick 2-minute tech tip video to do with multimeters and a feature you may not have known about with your multimeter and one you probably won't find in the manuals. Hmm, I should update my manuals to actually include this. Um, if you've got a multimeter with a temperature functionality, most, you know, any decent multimeter is going to have measure temperature with a what's called a K-type uh thermocouple. They come in different types, but almost all multimeters use K-type thermocouples.

**Dave Jones:** Has to do with the composition of the metal that's used for the uh two wires in here. I've done a whole very extensive tutorial video on thermocouple. So, I'll link that in up here and down below and at the end.

**Dave Jones:** Check it out. Anyway, you might know that uh some more advanced multimeters like this 121 and this Keysight uh 1272A might actually have an internal temperature sensor that actually tells you what the internal temperature is of the multimeter. And of course, if we're good on uh temperature mode at the well, it's to do explain that in a minute.

**Dave Jones:** But, if you plug in your K-type thermocouple, of course, then it measures the external temperature on the thermocouple. And of course, if I touch that, boom, it goes up like that. And likewise over here, we plug it in and it goes from overload to measuring uh the external temperature there. But, what if you've got a multimeter that doesn't uh have that internal uh temperature readout display like this one or this one or countless other multimeters that will not measure just the ambient temperature. Can be handy to measure the

**Dave Jones:** ambient temperature sometimes. So, how can you do it? And you forgot your temperature probe. Of course, you can just plug in your temperature probe and Bob's your uncle, all right? But, if you forgot or don't have your temperature probe handy, how can you measure it?

**Dave Jones:** Aha, it's easy. All you've got to do is plug your probes in and short them out like that. There is your ambient temperature, believe it or not. And yes, this should work with uh practically any multimeter that it measures temperature. There it is, 24.5. We can now measure the ambient temperature of the room without a thermocouple. Brilliant. Now, there are some oddball meters like this Fluke 17B that will actually measure the ambient temperature or it will try to do Look, I rub my hands over there and it's it's

**Dave Jones:** all over the shop, but it doesn't show open like other meters including other Flukes like this. And you can do exactly the same thing though. You can plug that in and it's all over the shop. And we do that and bingo, short out probes, we've got our ambient temperature. This one's reading a bit high, don't know why. So, why does this work? Well, there's a very specific reason for this and I've gone through that in my extensive thermocouple tutorial video, but it has to do with

**Dave Jones:** the Seebeck effect and how thermocouples work. In this particular case, when you short it out like this, we actually read 0 mV, but every multimeter that measures temperature like this using K-type thermocouples must have an internal temperature sensor somewhere, be it built into the multimeter chip set or it could be like an external little sock 23 temperature sensor or whatever. It's got to measure it internally even though it doesn't display it. And by shorting out the probes like this, you are basically you know, shorting out the input so it

**Dave Jones:** generates 0 V like that and therefore it defaults to the ambient temperature it's measuring with the internal temperature sensor. And this is either done with like a a lookup table or with like a polynomial function and watch my tutorial video, it won't go into the details. So, when you short out the probes like this, it basically thinks that the external temperature probe is at the K-type probe is at ambient temperature. So, that's what it displays. So, this is why your meter can often do weird things if you got it on

**Dave Jones:** temperature and just have your probes flapping around in the breeze like this. It's fine if you short them out cuz it's measuring like in the order of you know, microvolts. And there are differences in meters like you know, this one once again it's got dual readout measures the internal temperature and of course if we plug that in, it'll work just fine and dandy.

**Dave Jones:** And other ones like this Tektronix for example, it's a little bit out and you'll notice I'm putting my finger near the thing. I'll rub my feet on the carpet. Oh, 54. It's just like yeah, it's all over the shop like that. But of course if we plug our probes in like that and we short it out, it should get to the ambient temperature. Although that one's going a bit high. Hmm. And this should work with any meter on the market cuz anything as I said that uses

**Dave Jones:** K-type thermocouple must have an internal temperature sensor cuz that's the only way that it can accurately measure and compensate for the K-type thermocouple like is designed to be used with these meters. You can't do it any other way. And just to prove that this is a legit thing and it is measuring the ambient temperature and not just some you know, pre-programmed internal offset or something like that. I've got it inside my thermal chamber here and as you can see it's pretty darn close to that internal temperature. Just be aware

**Dave Jones:** of the thermal lag cuz the temperature sensor is inside the plastic case and inside a rubber holster and all sorts of things. So yeah, there will be a quite a significant temperature time lag there before the ambient temperature gets inside the meter. So there you go. I hope you might find that little tip useful one day. And as I said, go check out the extensive thermocouple tutorial video I'll link in because it there's a lot of trick and a lot of science that goes into the materials in the K-type

**Dave Jones:** thermocouples and the algorithms and lookup tables that multimeters have to follow to in order to actually get accurate temperature readings using these dissimilar metal thermocouple probes. It's really interesting stuff. If you like it, give it a big thumbs up.

**Dave Jones:** Catch you next time.
