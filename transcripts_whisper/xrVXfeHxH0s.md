---
video_id: xrVXfeHxH0s
title: EEVblog 1648 - USB Battery Bank mAh Capacity ratings are a LIE!
url: https://www.youtube.com/watch?v=xrVXfeHxH0s
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 42, "3": 65, "4": 86, "5": 104, "6": 135, "7": 152, "8": 170}
---

**Dave Jones:** Hi, this is just a quick video explaining the difference between input-referred and output-referred specifications. In particular, in this example, when it comes to these portable battery packs, this is a 20,000 mAh battery pack. Now, mAh is actually not the correct way to compare battery capacities because mAh is a charge, it's not an energy.

**Dave Jones:** So, even though it's got battery energy here, 20,000 mAh, but it actually gives you a watt-hour figure. Now, that is what you're supposed to use to compare battery packs. So, it's 77 watt-hours because it's based on, that mAh capacity is based on a voltage.

**Dave Jones:** In this particular case, 3.85 volts there. So, this battery pack is supposed to have a capacity of 77 watt-hours. Well, I actually measured it with a constant current load here, and you can see I was having a load of 5 watts. Here, constant, it took a long time to actually do this, 12 hours actually, and it's 61 point, well, it's actually 61.8 watt-hours there.

**Dave Jones:** Well under the 77 watt-hour spec. What's going on? Well, the problem here is the marketing department, that 20,000 mAh capacity is what's called input-referred. And what that means is that here is the battery bank here. It has the battery, the actual battery inside here, and then a DC-to-DC converter to drive that.

**Dave Jones:** Now, the battery inside may indeed have a watt-hour capacity of 77 watt-hours, so it may actually meet that spec. But they don't tell you that this is what is called input-referred, because it's coming from the input, i.e. the battery. You can also call it battery-referred if you want to.

**Dave Jones:** It's not output-referred, which is what we measured with this thing, the 61.8 watt-hours here. So, the input-referred figure does not include the efficiency. Of the DC-to-DC converter, so 61.8 watt-hours into 77 watt-hours, that is an 80% efficient DC-to-DC converter. So, just be aware of this when you're comparing battery banks like this, or a ton of other products out there where they don't include the efficiency of any power supply.

**Dave Jones:** They give you the input-referred, when really what you care about as a consumer is how much energy can it deliver to my load. So, if you're comparing batteries with just the input-referred figures, then it doesn't include the efficiency of the DC-to-DC converter. So, one of them might be way more efficient than another product,

**Dave Jones:** but you wouldn't know unless you actually test it output-referred like we did with this load here. So, yeah, just be aware of marketing departments just having a wank and doing input-referred and not output-referred. Whenever you want to compare two systems, make sure you're comparing an output-referred figure.

**Dave Jones:** So, I hope you found that useful. If you did, please give it a big thumbs up and don't forget to subscribe. and comment down below. Catch you next time.
