---
video_id: GRRvGj8OT_A
title: EEVblog 1604 - BEWARE! Multimeter Burden Voltage
url: https://www.youtube.com/watch?v=GRRvGj8OT_A
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 26, "3": 38, "4": 48, "5": 59, "6": 73, "7": 89, "8": 99, "9": 110, "10": 120, "11": 139, "12": 161, "13": 178, "14": 190, "15": 201, "16": 215, "17": 224, "18": 240, "19": 257, "20": 269, "21": 283, "22": 290, "23": 309, "24": 322, "25": 335, "26": 348, "27": 361, "28": 371}
---

**Dave Jones:** Hi, let's talk about burden voltage in multimeters and it's something you might not be aware of. Now, I've done videos on this in the past, but I haven't done a short concise video to show you what burden voltage is and the you can really come a gutter using your multimeter, any multimeter.

**Dave Jones:** Every single multimeter on the market is going to have a problem with burden voltage with measuring current. So, let's demonstrate this. I've got my power supply here outputting 1 V.

**Dave Jones:** I've got a 100 ohm resistor directly across it. Ohm's law, of course, current equals on resistance. So, 1 V divided by 100 ohms gives you a current of 10 mA and that's exactly what we're reading here, 10 mA.

**Dave Jones:** No problems whatsoever. But, watch what happens if I break my circuit and insert my current meter in series cuz that's what you have to do with a multimeter measuring current.

**Dave Jones:** You have to put it in series either on the top here or the bottom here. It makes no difference. So, let's disconnect our circuit and plug it in and see what happens.

**Dave Jones:** 9.8 mA. What's going on? Is there something wrong with this meter? No, in fact, this is an excellent and quite accurate meter and even the power supply over here is now reading exactly the same.

**Dave Jones:** It's dropped from 10 mA to 9.8 mA. What's going on? Well, this is what we call burden voltage in a multimeter, but basically, what's happening here is every multimeter is going to have a some resistance between the current jacks.

**Dave Jones:** This is made up of the not only the value of the internal fuse, which has a resistance, but also the current shunt resistor, which is dropping the voltage, which is used by the multimeter to actually measure the current.

**Dave Jones:** So, what you're doing now is you're broken your circuit and you've put your multimeter in series. That multimeter has an extra resistance in it and it can be quite significant.

**Dave Jones:** Now, in this particular case, we don't know what the value is in here, although we could calculate it or we could measure it, but for the purposes of this video, we don't care.

**Dave Jones:** But, the fact is we've put an extra resistance in series with our circuit. We've completely changed and disturbed our circuit under test. And anytime you use an instrument to measure something, you've got to be aware of the impact that that measuring device, in this particular case a multimeter on current range, is having to your circuit under test.

**Dave Jones:** So, Ohm's law, once again, our current flowing through our circuit is 1 V the 1 V hasn't uh changed over here, but the total resistance has. It's not just 100 ohms anymore, it's 100 ohms plus that what we call a shunt resistance inside here is uh which we call RS here, it's RS, the shunt resistance, plus R1, which is 100 ohms.

**Dave Jones:** So, it's something over 100 ohms, which means uh we're going to get a value less than 10 mA, and that's what we're getting here. So, every multimeter is going to have this, and if you're not aware of the impact uh the shunt resistance in a meter can have on your circuit under test, then you're going to come a cropper.

**Dave Jones:** The reason it's called burden voltage, it kind of has to do with uh the fact that uh let's, for example, say you had a 5-V uh power supply over here powering your circuit, you put your current meter uh in series, and you're measuring the current.

**Dave Jones:** Well, that multimeter could easily drop, say, 0.3 V, for example. It can be quite high. It can be up to like a volt on some multimeters. It can get quite high.

**Dave Jones:** And that means that your circuit is no longer now getting that 5 V, it's getting less than, say, the 4.75 V, which is your typical lowest threshold voltage of say a TTL circuit, for example, and your circuit could stop working.

**Dave Jones:** So, your multimeter is a burden on your circuit. So, that's why it's called burden voltage. But, check this out. What if I change from milliamp range over here to microamps?

**Dave Jones:** We should still be able to measure that 9.8 mA, but what? Look, we're getting 4,960 microamps, which is 4.96 milliamps, and that's what we're getting over here, 4.96. Why is it now changed again?

**Dave Jones:** It's because the shunt resistance inside your multimeter across your terminals, or the burden voltage, is going to change with the current range that you actually use. So, microamps is going to have a much higher resistance internally than what your milliamp range does.

**Dave Jones:** And likewise, if we switch over to the amps range here, okay, insertion error, we have to switch back to here, and bingo, we're now actually back to our 10 milliamps.

**Dave Jones:** Does that mean that our amps jack doesn't have a shunt resistance in it? No, it actually does. It's just much, much lower than your milliamp or microamp range. But look, we've traded off our resolution here.

**Dave Jones:** We don't get as many digits as we got when we were actually using the milliamps. So, go over to milliamps, you can see that we're actually getting three decimal places.

**Dave Jones:** Over here, we're only getting two, basically two decimal places after the milliamp range there. So, we've lost some resolution, but we're now not impacting our circuit as much cuz this shunt resister is much, much lower on the amps range, but it's not zero.

**Dave Jones:** If you actually go and put 10 amps, try it on your multimeter at home, put 10 amps through your amps jack, and actually, you can put a second multimeter, this is why you should have two multimeters, second multimeter across here, and you can actually measure the burden voltage yourself.

**Dave Jones:** And this problem with burden voltage in the multimeter, which as I said, can be like up to a volt or something like that, several hundred millivolts to a volt at full scale reading, and it's going to change depending on your current through there, by the way.

**Dave Jones:** It's why I developed the microcurrent. It's basically got It's still the same, it's a shunt resister, but it's got a times 100 amplifier in there. So, in theory, it's the shunt resistance is 100 times lower, but it's still not zero.

**Dave Jones:** And that's why I also built that into my 121GW multimeter here. I think it's the only meter on the market that has a low burden voltage. It's basically got a micro current built in, the little amplifier.

**Dave Jones:** But, even with this meter, the burden voltage is still not zero. It's just lower than a regular multimeter. So, there you go. Burden voltage. Just be aware of it.

**Dave Jones:** Can be a real trap for your own players. Catch you next time.
