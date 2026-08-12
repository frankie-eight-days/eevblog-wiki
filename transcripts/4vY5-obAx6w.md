---
video_id: 4vY5-obAx6w
title: Deye Hybrid Solar Inverter RTC FAIL!
url: https://www.youtube.com/watch?v=4vY5-obAx6w
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 35, "3": 59, "4": 69, "5": 81, "6": 94, "7": 110, "8": 122, "9": 151, "10": 167, "11": 175, "12": 191, "13": 206, "14": 223, "15": 235, "16": 245, "17": 258, "18": 272, "19": 286, "20": 298, "21": 313, "22": 326, "23": 337, "24": 345, "25": 357, "26": 371, "27": 391, "28": 401, "29": 411, "30": 421, "31": 435, "32": 446, "33": 462}
---

**Dave Jones:** Hi, it's time for another problem with my DIY hybrid solar inverter here. Um yes, again. And this one is really freaking annoying. It's practically a showstopper at the moment um because I just changed my electricity plan and I've now got uh three uh free free hours completely free hours per day of electricity from the grid.

**Dave Jones:** So, I thought, "Aha, this thing has timers built into it. We can go into here. We can go into system work mode like this." And you'll notice it's got timers.

**Dave Jones:** So, from 11:00 a.m. at the timer system in this is a ridiculously confusing. Anyway, um I I did get it to work and at just after 11:00 a.m. it switches on and charges uh the battery in this thing at the full 5 kW uh power during those um three three free hours three free hours say that three times quickly.

**Dave Jones:** Um yeah, during this three-hour window that I've got free power um I charge this battery at 5 kW regardless of what the solar is doing. And that's absolutely fantastic.

**Dave Jones:** So, it means regardless of the weather, regardless of the season, or whatever, I should always have a full battery at night that'll last me all night. So, you know, uh pretty much regardless of what I do.

**Dave Jones:** Absolutely fantastic. The problem is though um go out here, I set the time on this thing like the date and time. There it is. I set it only a couple of days ago and it's 9:08 a.m.

**Dave Jones:** But look at my watch. It ain't 9:08 a.m. It is 5 minutes to 10:00. It's lost like over 40 minutes in like well I think it might have been 3 days I set the Anyway, it's losing like 10 15 minutes per day per day.

**Dave Jones:** And uh for those who think, "Oh, it might be um like you've got your 50 60 hertz setting wrong or something like that. No, it's not the 50 60 hertz grid setting.

**Dave Jones:** I've got that actually set and it does actually have a time sync function in here, but that's only if you have it internet connected via the Wi-Fi dongle thing and I don't have that because it hooks onto the RS232 port and I'm using the RS232 port for my Raspberry Pi based solar assistant and that does not have the ability to send a command or a time sync to this DI unit.

**Dave Jones:** If it did, that would solve all my problems, but yeah, I am completely screwed. This thing is losing many minutes per day and there's nothing I can do about it apart from actually come out here and physically like reset the time like almost every day.

**Dave Jones:** Because if I was only losing a minute per day, I could come out every couple of weeks or something and do it, but no, we're I'm losing 10 15 minutes per day.

**Dave Jones:** Well, the first thing DI said is hook on the Wi-Fi dongle and get an RS485 cable for your solar assistant. So, I've ordered an RS485 cable. They're bloody expensive.

**Dave Jones:** Could have made one up myself, but whatever. Anyway, 485 cable for my Raspberry Pi I could free up the RS232 port for that stupid Wi-Fi dongle. I didn't want to internet internet connect this thing, but anyway, that's a step, but I can't seem to find that Wi-Fi dongle.

**Dave Jones:** I think it came with the unit, but I'm not 100% sure. Anyway, I'm still looking for that. What a pain. So, yeah, I'm just losing time and this thing if you look at my teardown does actually have a crystal a 32 kilo 32.768 kilohertz watch crystal on it.

**Dave Jones:** So, I don't know what's going on there and it has an RTC chip. So, I don't know what the heck is going on, but anyway, um yeah, DIY seemed to think, "Oh, this is just normal.

**Dave Jones:** Just internet connect the thing and set that um time sync function." I don't want to set the bloody time sync function. That's ridiculous. It should be able to with any crystal at all.

**Dave Jones:** Um regardless of temperature variation, it should be able to keep like, you know, at least a minute per month or something like that at worst case. So, this is just nuts.

**Dave Jones:** So, yeah, I basically it's rendered this thing useless. And the solar assistance system, it does actually have the ability to um like change work modes based on its own timer and stuff like that, but um it doesn't uh but I have not been able to get that to work.

**Dave Jones:** I don't think it works at all um in in the way I want it to like set the charge mode. I can turn the charge mode off and on, but it still needs these internal timers in here to actually needs those internal timers to actually do that.

**Dave Jones:** Um so, yeah, it's like so, I can switch it off and on. I can switch that um I can switch the charge mode off and on, but not but it doesn't override these if you get what I mean.

**Dave Jones:** So, um yeah, I'm stuck at the moment. And then they offered, "Oh, we can replace your entire front panel board for you. That'll fix it." And it's like if you've seen my teardown, you know to replace the front panel board, you've got to take out all the guts in this thing.

**Dave Jones:** And it's almost not quite a destructive process, but oh my goodness, it ain't pretty. So, there's no way I'm going to do that. And then they finally said, "Look, uh we can offer you an entirely new unit." But yeah, okay, thanks, great.

**Dave Jones:** Um but there's a lot of work to actually physically replace this thing. So, anyway, I'm going to eventually try the RS485 um thing on this once I get the cable.

**Dave Jones:** And hopefully they can maybe they can send me a new dongle thing for it or something. Um that's way cheaper for them. But yeah, pain in the ass this thing.

**Dave Jones:** Unbelievable. Like something simple like that that they can't even get right. But like the the time of day, the time of day. 9:13. So, I've got to go in there and I've got to set that back again to What is it?

**Dave Jones:** It's Yeah, it is now 10:00 a.m. It is now 10:00 a.m. So, got to adjust that. And we're back. Whoop. In fact, I'll put the couple of I'll put a 5 minutes ahead.

**Dave Jones:** There you go. Cuz it's just going to It's just going to lose time anyway. Unbelievable. Now, the only thing I can think of is that I'll I'll put up a a screenshot here of uh from my solar assistant how the the 50 Hz mains, which this thing measures, there is actually these skips every now and then like you know, like half a dozen times a day.

**Dave Jones:** Maybe very short skips. And I'm not sure my I'm pretty sure it's not my mains doing that. So, I think it's the actual DI whatever measurement system in the DI inverter is doing that.

**Dave Jones:** Now, if that's some how causing it to skip, I don't see how when you've got a proper RTC chip it it physically has supposed to have an RTC chip in there.

**Dave Jones:** So, I I don't know, but anyway, that's at least something to go on. But anyway, they don't seem to think that's a thing. But they seem to think I just have a faulty board.

**Dave Jones:** Okay. Thanks. Anyway, they didn't make it easy to bloody change the board in this thing. If this front panel, like if this entire front panel just came off and I could swing out and replace the board, easy.

**Dave Jones:** 5-minute job. No worries. But unfortunately, no. No, you've got to dig out all the internals and unroute all the cables and connectors and everything else inside just to get at that front panel board.

**Dave Jones:** So, unfortunately, they didn't think about that from a replacement point of view. So, it's either a terrible design or I don't know. My crystals failed somehow. Like it's off by a huge amount.

**Dave Jones:** I don't know. Leave it in the comments down below if you've ever had that sort of error on a crystal RTC. Unbelievable. This thing's no end of trouble. Catch you next time.
