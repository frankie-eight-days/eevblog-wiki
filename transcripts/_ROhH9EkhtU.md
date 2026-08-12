---
video_id: _ROhH9EkhtU
title: EEVblog #35 2of2 - NiMH and NiCd Battery Charging Tutorial
url: https://www.youtube.com/watch?v=_ROhH9EkhtU
source: youtube-asr
timestamps: {"0": 10, "1": 20, "2": 35, "3": 57, "4": 67, "5": 81, "6": 94, "7": 126, "8": 136, "9": 158, "10": 168, "11": 184, "12": 208, "13": 231, "14": 241, "15": 259, "16": 275, "17": 290, "18": 303, "19": 320, "20": 337, "21": 353, "22": 366, "23": 374, "24": 389, "25": 402, "26": 416, "27": 429}
---

**Dave Jones:** Now, I thought while we're on the topic, we might as well do some basic battery charger theory. So, here we go. Now, the first technique is a very basic one for charging these things.

**Dave Jones:** Nickel metal hydrides and NiCads are typically charged with a constant current. You can actually pulse the current as well, but it's but it's typically a constant current source. And what you can do, the first technique is a timer-based system.

**Dave Jones:** So, you just put the battery in and the microcontroller in there just times uh how long it's been in there charging and then shuts it off. And this is really totally inadequate except for the lowest charge currents because uh you don't know the state of this you don't know how much charge is already in this battery before you put it in the charger.

**Dave Jones:** Now, the two major types of rechargeables, as I said, are NiCad and nickel metal hydride. And I've drawn a charge uh charging graph here. This is a pretty standard chart you'll find.

**Dave Jones:** And this is the two different types. This is the NiCad curve and this is the nickel metal hydride curve. And what it is is it's the charge voltage because it's a constant current, the the voltage across the battery changes with charge.

**Dave Jones:** And this is a 100 0 to a 0 to 100% battery capacity. And this is uh the voltage across the cell when you pass the constant current charge through.

**Dave Jones:** And as you can see, they're two entirely different voltage profiles. So, uh the second technique for determining the end of charge is actually to measure the voltage. As you can see here, NiCad and nickel metal hydride, once they actually reach or just after actually, that's probably slightly out, just after they reach 100% capacity after you've charged them, then the voltage will actually peak and then it will actually start to

**Dave Jones:** drop again. And it's it's much more it's much a bigger drop on NiCads than it is on nickel metal hydride. I've probably drawn that exaggerated. It's probably not quite that sharp.

**Dave Jones:** Now, you've probably heard of negative whoop negative delta V um charge end of charge voltage detection and this is what it is. It's basically measures the change a negative change in voltage between here and here.

**Dave Jones:** So when it starts to go when it measure when the micro measures that the voltage actually starts to go negative i.e. delta a change in voltage delta means a change in voltage.

**Dave Jones:** So when you get a negative change in voltage, it knows, "Okay, the battery's full and I'll switch it off." So that's called negative delta V voltage detection. And it can also be what's called zero delta V which means it may not detect it going down.

**Dave Jones:** It may just just actually detect that it's flattened off like that over time. The third detection method for end of charge is measuring the temperature because NiCad and nickel metal hydride batteries, they both increase in temperature very sharply once once they get to 100% capacity as you can see here.

**Dave Jones:** Now, nickel metal hydride what's called an exothermic charging charging reaction. It means that they actually get hot during their entire charge cycle. Whereas NiCads over most of their range are actually what's called endothermic which means that they don't actually get hot during this charge.

**Dave Jones:** It's only once they get to the end of the charge when when they get build up inside, pressure build up, that that the NiCad actually gets hot as well.

**Dave Jones:** But, they both get hot near the end. So, you can actually use a temperature increase on the cell to detect when you've hit 100% battery capacity. Now, there are actually two different methods of doing temperature cut off.

**Dave Jones:** Now, the first one is called delta T. Okay, it's called delta T temperature sensing. And basically, at the start of the charging, it takes it takes a reading and then it measures the difference or the delta in the temperature over the time.

**Dave Jones:** So, it it'll, you know, once it's increased, you know, 15° or something like that, it'll switch off. Now, that isn't all that reliable in itself because once again, the ambient temperature can actually have an effect there.

**Dave Jones:** The second method of determining uh temperature change is what's called delta T on delta time. Okay, so it basically measures a change in temperature over a change in time.

**Dave Jones:** I E, it measures a slope. It actually measures a ramp like that. So, it this has less effect or ambient temperature has less effect in this technique because it's over a shorter time period like this.

**Dave Jones:** So, this slope here is not as steep as this slope here. I E, it changes X amount of T temperature over X amount of time. And this is a pretty reliable technique.

**Dave Jones:** And it's almost certainly what this Varta one is actually using along with delta uh, minus delta V uh, minus yeah, minus delta V voltage cutoff. Charging a battery is actually usually a three-step, uh, process.

**Dave Jones:** And the three steps are, one is the fast charge as we've explained. Uh, usually it's 1C, but this Varta one obviously uses 4C to get its 15 minutes. The second one is a top-up charge.

**Dave Jones:** So, when it's finished the fast charge, does a chop top-up at a current rate of C on 10 for, I don't know, 10, 20 minutes, something like that, just to top the battery up.

**Dave Jones:** And then, once it's done that, third one is it does a, uh, C on 300 um, charge rate, just a little tiny trickle charge for an indefinite period. It might be 24 hours or 12 hours or something like that.

**Dave Jones:** So, as you can see, this Varta charger obviously uses various techniques to, uh, to stop these batter- to stop destroying these batteries at this massive huge 4C charge rate.

**Dave Jones:** It's as you can as we saw, we took it apart, it's got individual contact, uh, temperature sensors on each cell. It's, um, all my it is all I can guarantee or it's also using, uh, minus delta V, uh, cutoff as well.

**Dave Jones:** And it's probably got a timer in there for good measure, just in case. It's 20 minutes. So, this thing's incredible. But, are you going to get those thousand recharges out of it at 4C?

**Dave Jones:** Not a chance.
