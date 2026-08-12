---
video_id: _ROhH9EkhtU
title: EEVblog #35 2of2 - NiMH and NiCd Battery Charging Tutorial
url: https://www.youtube.com/watch?v=_ROhH9EkhtU
source: youtube-asr
timestamps: {"0": 10, "1": 24, "2": 39, "3": 53, "4": 67, "5": 81, "6": 98, "7": 115, "8": 132, "9": 153, "10": 170, "11": 186, "12": 208, "13": 229, "14": 243, "15": 264, "16": 279, "17": 300, "18": 317, "19": 337, "20": 355, "21": 370, "22": 384, "23": 398, "24": 415, "25": 429}
---

**Dave Jones:** Now, I thought while we're on the topic, we might as well do some basic battery charger theory. So, here we go. Now, the first technique is a very basic one for charging these things. Nickel metal hydrides and NiCads are typically

**Dave Jones:** charged with a constant current. You can actually pulse the current as well, but it's but it's typically a constant current source. And what you can do, the first technique is a timer-based system. So, you just put the battery in and the

**Dave Jones:** microcontroller in there just times uh how long it's been in there charging and then shuts it off. And this is really totally inadequate except for the lowest charge currents because uh you don't know the state of this you

**Dave Jones:** don't know how much charge is already in this battery before you put it in the charger. Now, the two major types of rechargeables, as I said, are NiCad and nickel metal hydride. And I've drawn a charge uh charging graph here. This is a pretty

**Dave Jones:** standard chart you'll find. And this is the two different types. This is the NiCad curve and this is the nickel metal hydride curve. And what it is is it's the charge voltage because it's a constant current, the the voltage across

**Dave Jones:** the battery changes with charge. And this is a 100 0 to a 0 to 100% battery capacity. And this is uh the voltage across the cell when you pass the constant current charge through. And as you can see, they're two entirely

**Dave Jones:** different voltage profiles. So, uh the second technique for determining the end of charge is actually to measure the voltage. As you can see here, NiCad and nickel metal hydride, once they actually reach or just after actually, that's probably

**Dave Jones:** slightly out, just after they reach 100% capacity after you've charged them, then the voltage will actually peak and then it will actually start to drop again. And it's it's much more it's much a bigger drop on NiCads than it is

**Dave Jones:** on nickel metal hydride. I've probably drawn that exaggerated. It's probably not quite that sharp. Now, you've probably heard of negative whoop negative delta V um charge end of charge voltage detection and this is what it is. It's basically measures the change a

**Dave Jones:** negative change in voltage between here and here. So when it starts to go when it measure when the micro measures that the voltage actually starts to go negative i.e. delta a change in voltage delta means a change in voltage. So when you

**Dave Jones:** get a negative change in voltage, it knows, "Okay, the battery's full and I'll switch it off." So that's called negative delta V voltage detection. And it can also be what's called zero delta V which means it may not detect it going down. It may

**Dave Jones:** just just actually detect that it's flattened off like that over time. The third detection method for end of charge is measuring the temperature because NiCad and nickel metal hydride batteries, they both increase in temperature very sharply once once they get to 100% capacity as

**Dave Jones:** you can see here. Now, nickel metal hydride what's called an exothermic charging charging reaction. It means that they actually get hot during their entire charge cycle. Whereas NiCads over most of their range are actually what's called endothermic which means that they

**Dave Jones:** don't actually get hot during this charge. It's only once they get to the end of the charge when when they get build up inside, pressure build up, that that the NiCad actually gets hot as well. But, they both get hot near the

**Dave Jones:** end. So, you can actually use a temperature increase on the cell to detect when you've hit 100% battery capacity. Now, there are actually two different methods of doing temperature cut off. Now, the first one is called delta T.

**Dave Jones:** Okay, it's called delta T temperature sensing. And basically, at the start of the charging, it takes it takes a reading and then it measures the difference or the delta in the temperature over the time. So, it it'll, you know, once it's increased, you know,

**Dave Jones:** 15° or something like that, it'll switch off. Now, that isn't all that reliable in itself because once again, the ambient temperature can actually have an effect there. The second method of determining uh temperature change is what's called delta T on delta time.

**Dave Jones:** Okay, so it basically measures a change in temperature over a change in time. I E, it measures a slope. It actually measures a ramp like that. So, it this has less effect or ambient temperature has less effect in this

**Dave Jones:** technique because it's over a shorter time period like this. So, this slope here is not as steep as this slope here. I E, it changes X amount of T temperature over X amount of time. And this is a pretty

**Dave Jones:** reliable technique. And it's almost certainly what this Varta one is actually using along with delta uh, minus delta V uh, minus yeah, minus delta V voltage cutoff. Charging a battery is actually usually a three-step, uh, process. And the three

**Dave Jones:** steps are, one is the fast charge as we've explained. Uh, usually it's 1C, but this Varta one obviously uses 4C to get its 15 minutes. The second one is a top-up charge. So, when it's finished the fast charge, does a chop top-up at a

**Dave Jones:** current rate of C on 10 for, I don't know, 10, 20 minutes, something like that, just to top the battery up. And then, once it's done that, third one is it does a, uh, C on 300 um, charge rate, just a little

**Dave Jones:** tiny trickle charge for an indefinite period. It might be 24 hours or 12 hours or something like that. So, as you can see, this Varta charger obviously uses various techniques to, uh, to stop these batter- to stop destroying these

**Dave Jones:** batteries at this massive huge 4C charge rate. It's as you can as we saw, we took it apart, it's got individual contact, uh, temperature sensors on each cell. It's, um, all my it is all I can guarantee or it's also using, uh, minus

**Dave Jones:** delta V, uh, cutoff as well. And it's probably got a timer in there for good measure, just in case. It's 20 minutes. So, this thing's incredible. But, are you going to get those thousand recharges out of it at 4C?

**Dave Jones:** Not a chance.
