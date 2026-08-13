---
video_id: kCtGoymiShU
title: Deye Hybrid Inverter Gen Port Troubleshooting
url: https://www.youtube.com/watch?v=kCtGoymiShU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 46, "3": 70, "4": 91, "5": 112, "6": 126, "7": 146, "8": 167, "9": 184, "10": 203, "11": 220, "12": 235, "13": 254, "14": 269, "15": 286, "16": 305, "17": 324}
---

**Dave Jones:** Hi, I'm trying to get to the bottom of this mysterious DI 84 watt power consumption, which happens 24-7, regardless of what I do when I switch on the microinverter input on the generator port. So, I'll measure the current clamp, right? This is coming from the battery.

**Dave Jones:** And, look at this, right? It's 1.15 amps there, and I've actually verified that with another current clamp. At a current voltage of... current voltage? Get it? I'm here all week. A current voltage of 53.6 volts there, that doesn't equal the 84 watts. And let me show you.

**Dave Jones:** Okay, what I've done is I've actually isolated the inverter. It's nighttime here, obviously. So I've isolated the AC side, which is that one there, okay? And I've also isolated the new microinverter, which is that one there. So I switched both those off. So the DI inverter is being powered just from the battery.

**Dave Jones:** There's no other source, and you can see it's showing off-grid there, and it's still showing 5 watts, 4 watts from the microinverter on the gen port, but that's just a residual error. There's nothing doing there, but it's still reporting the 84 watts. So there's nowhere else for the current to go.

**Dave Jones:** Like, that 84, I reckon's got to be some sort of furphy. And it makes no difference if I switch the microinverter off. So it's not the Hoy-Miles microinverter consuming 84 watts quiescent standby at night. It's not that. It's happening, if it is real, it's happening inside the DI,

**Dave Jones:** because it's not going back out to the grid. It's got absolutely nowhere to go. So, yeah. I can only presume that this thing is taking, well, 65 watts or thereabouts. So I don't know where the 84 is coming from. It makes no sense whatsoever.

**Dave Jones:** I don't get it. So I think it's some sort of furphy. Arrgh! Thoughts and comments down below. Now I'll switch the AC grid side back on. I don't think it's connected yet, but it takes like a minute to reconnect. But all of that power is still coming from the battery,

**Dave Jones:** so I'm going to wait for that grid to reconnect and see if that actually, if the residual, there it goes, it dropped. So the grid is reconnected. There you go. That's what I thought would happen, okay, because I had the grid isolated. So the DI microinverter is completely isolated from other power sources,

**Dave Jones:** except for the battery, and when that happens, it drew about 1.15 amps-ish there, which is around about, that battery voltage is around about 60-odd watts. So it's definitely not the 84, and it's definitely not on the generator port, because I've got nothing on the generator port.

**Dave Jones:** I've disconnected the Hoyle-Myles microinverter. So now obviously most of the power for the DI box is coming from the grid side now, because the grid side is reconnected now. So now there's only a little piddly bit coming from the battery. I don't know, that's just to power some internal circuitry in there,

**Dave Jones:** so that's not much, right? That's bugger all. In terms of watts, just to power the input circuitry, whatever that is, in the DI for the battery there. So it's just some residual stuff there. So that's interesting, huh? And this is real-time updating, okay?

**Dave Jones:** During none of this has any of that 84 watts changed, whether or not I connect the Hoyle-Myles microinverter to the gen port or I don't, whether I disconnect or disconnect the grid. The only thing left to do is to actually physically switch it off,

**Dave Jones:** change the work mode, and see what happens. Actually switch it off back to not a microinverter thing, and that should drop to zero then. So if I change that auxiliary input, the microinverter, okay, I'm going to convert it back to generator input like this,

**Dave Jones:** and if I save that, if we go back out there and we go right down to the bottom, I think we might find generator power zero. So it's now dropped back to zero. So I reckon there's something really, really sus going on there.

**Dave Jones:** Yep, yep, there it is. It just dropped right back to, well, it will, I think. Should drop back to zero. It shows zero on the other page. I'm not sure why the scale hasn't moved there. I've got one minute update. Let me try and refresh that.

**Dave Jones:** Yeah, zero. There you go. After a refresh. So there you go. When you switch it to microinverter input, there's a mysterious 84 watts there. I've got no idea. I have asked DI, but they haven't really responded yet. So yeah, I think it's a furphy.

**Dave Jones:** I don't think there's actually like 84 watts actually going anywhere. I think there's just 60-odd watts for the actual DI thing itself. So that kind of makes sense, I guess. Seems a bit high, but, you know, at least it's something. But yeah, it's definitely not the microinverter or something else.

**Dave Jones:** So I get, well, I don't know, it might chew extra power because it's got to switch on the microinverter output to keep on the gen port to keep it going. But I don't know. I don't get it. Yeah, it's weird. Another DI quirk.
