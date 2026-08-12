---
video_id: 6JhK8iCQuqI
title: EEVblog 1746 - The 555 is 55 Years Old!
url: https://www.youtube.com/watch?v=6JhK8iCQuqI
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 47, "3": 71, "4": 100, "5": 134, "6": 163, "7": 183, "8": 215, "9": 235, "10": 261, "11": 292, "12": 327, "13": 355}
---

**Dave Jones:** Hi, probably the most classic chip in all of electronics history, the triple five, the 555 timer, is 55 years old this year, or thereabouts. So, we're going to celebrate this milestone by releasing this video on May the 5th.

**Dave Jones:** Let's call it from here on out International Triple Five Timer Day. And yes, I'm probably going to release this at 5:55 p.m. today. And hopefully this video is going to be five minutes and 55 seconds long. So, a brief history, the triple five was developed in 1971 famously by the legend Hans Camenzind, who was actually a contractor at Signetics at the time. So, this was originally a Signetics product. He was full-time there, but he wasn't that happy, so he went to be in a contract. He was getting

**Dave Jones:** paid a pittance, but he had this idea for a timer chip, because I guess there weren't any timer chips available back then. And that was based on a circuit that he had for uh some PLL, some phase-locked loops he was working on the time. That was the uh timer source for the PLL. So, he took that idea, told Signetics about it, "Hey, I want to make this timer chip." Apparently, a lot of the management said, "Well, what do you want a timer chip for?" But, marketing

**Dave Jones:** said, "Oh, yeah, I think we can sell a timer chip." So, he was working for a pittance at the time in a back alley uh shop that is still there. It's a real estate agent now, apparently. So, sometime in mid-1971, he uh taped out the first version of the triple five timer. And back then, there were no CAD tools. You have to uh like hand cut uh the rubylith material for the mask and everything. Anyway, it worked, but that original version actually needed nine pins. So, he

**Dave Jones:** redesigned it, and in October 1971, we get what we know and love today, the eight-pin DIP triple five timer, the classic. And the design of it basically hasn't changed since, although there's a new CMOS variant of it which gets around some current shoot limitations on the bipolar output and a current consumption. But anyway, it's still going strong and still selling in the squillions 55 years later. It's available from everyone. In fact, they Signetics actually didn't bother to patent the thing back then. So, in 1972, there were

**Dave Jones:** already a dozen different suppliers of the 555 timer. Oops. But that led to its popularity and is still used in absolutely everything. You can even get a space-rated variant of it. So, it started being shipped and cloned in early 1972. And I dug out of my archives the first mention of it that I can find in Electronics Australia, November 1972. So, even before the internet, this thing had already made it to Australia and was being advertised.

**Dave Jones:** Look at this, the timer of a thousand and one uses. And this is an ad from Signetics. And look, even like in the year of its release, they're talking about being a true standard. Um it's and a thousand and one uses. Even back then, they're talking about this thing being an industry standard and the timer chip.

**Dave Jones:** It's just unbelievable. Anyway, this was the local dealer in Australia. So, I just find that amazing. By the year of its release, it was already they're pushing it marketing were pushing it as the standard chip. Uh cheapest chips down here, rock bottom cost. But the marketing just didn't die out. Everyone started using it and it became the de facto industry standard timer almost right away. And the marketing manager at Signetics, Art Fury, he's the one who actually named it 555. And yes, I don't care what anyone says, the five 3.5 K

**Dave Jones:** resistors in the circuit, that's not a coincidence, damn it. Oh, look, Australia actually used to make 7400 series chips right here by Philips. Unbelievable. What happened? Behold my killer one-shot circuit. I've got a classic triple five one-shot uh timer.

**Dave Jones:** I've got an indicator LED on the output here and I've got a capacitor which will trigger the thing when it immediately turns on and I've got an RC time constant here of around about 5 seconds. So, the LED, once we apply power, should turn on for about 5 seconds and then well, after that, um I'm not sure. We may only get one shot at this. I'm powering it from 15 volts.

**Dave Jones:** Uh here we go. Still in the business. No worries. Woah. 330 milliamps. Um almost 5 watts. Oh, oh, oh, no, it's turning off flashing circuit. Um and uh yeah, it went to zero. Uh so, let me just uh turn the power off here and uh see if we can repower that, shall we? Will it work again?

**Dave Jones:** Uh no. It's dead. Can we have a hearty salute for that triple five timer? It worked a treat for 5 seconds. It did its job, damn it. So, here's the Dave CAD schematic for my killer one-shot. It's a standard uh one-shot timer, but instead of having the uh timing resistor between pins seven and eight, I've actually tied pins seven and eight together and put the timing resistor here. And then our timing RC circuit charges straight away like this and as soon as it reaches the threshold voltage, that uh 2/3 point, uh

**Dave Jones:** the discharge transistor open collector jobby turns on and wah, wah, wah, wah, dead crowbar short right down to ground. Anyway, try it at home. The killer one-shot. Win or win it, chicken dinner. Catch you next time.

**Dave Jones:** >> Mhm.
