---
video_id: 3hHG_WcJtQo
title: Solis Cloud & Battery Charge Timer
url: https://www.youtube.com/watch?v=3hHG_WcJtQo
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 29, "3": 47, "4": 59, "5": 76, "6": 87, "7": 102, "8": 116, "9": 127, "10": 142, "11": 151, "12": 170, "13": 179, "14": 188, "15": 200, "16": 209, "17": 220, "18": 229, "19": 241, "20": 255, "21": 268, "22": 284, "23": 294, "24": 311, "25": 322, "26": 338, "27": 353, "28": 367, "29": 387, "30": 401, "31": 414, "32": 424, "33": 437, "34": 454, "35": 469, "36": 480, "37": 495, "38": 507, "39": 516}
---

**Dave Jones:** Hi, first look at my new Solace inverter Solace Cloud thing. I've got the thing installed, commissioned, and connected via the Wi-Fi dongle thing, which plugs into the bottom of the USB port, and it's connected to my home network, so I can access this anywhere in the world now.

**Dave Jones:** So, let's just have a look at here cuz I was trying to debug a problem, which it I still currently have. Trust me, it was working a minute ago, but I'll show you why it's not working in a minute.

**Dave Jones:** I wanted it's currently 12:30 p.m., so it's within my 3-hour free charging window. So, obviously, I want to charge my new 75-kW hour battery home storage battery. I want to use as much energy.

**Dave Jones:** I want to charge the EV and also the home storage battery during that free 3-hour window, which apparently they just announced a few days ago that they're going to offer to everyone now.

**Dave Jones:** Everyone in Australia, regardless your energy retailer, is supposed to now have an option for if if you want to join, like they have to have a plan option where there's a 3-hour energy window per day cuz we've just got too much solar here in Australia.

**Dave Jones:** So, yeah, we have to use it because when we installed all the solar here, it didn't have the ability to curtail it and switch it off and stuff. So, anyway, so they want people to use it.

**Dave Jones:** So, I want to charge that. So, here's the display. It's pretty groovy here. So, I've got my PV up it the sun just peeked out at the moment. I've got the AC coupling that'll be coming from the Enphase system, but I think that's just the residual from the Enphase system.

**Dave Jones:** I'm not sure. I still haven't figured out the gen port, which is connected to my two-panel Hoymiles microinverters. Still haven't figured that out, but I think anyway, AC coupling, I think that's coming from the Enphase system or the residual of it.

**Dave Jones:** The battery, of course, uh, whether or not it's it's doing nothing at the moment, actually. Um, and we might see why in a minute. Um, and the grid there's 2 kW coming in from the grid.

**Dave Jones:** Um, that's interesting because the battery's shut off for some reason, anyway. The grid load here, um, is um, we're charging the EV at the moment. So, this is on the So, that will show up as grid load here and the backup load is the rest of the house.

**Dave Jones:** So, um, family's home at the moment, so they're taking 3.8 kW in the house. So, you know, they're probably I don't know, they might have an aircon or something like that.

**Dave Jones:** That's more than normal. Mrs. EV blog could be cooking something or thing things like that. Anyway, now I thought I had set up the, uh, timer uh, the charge timer for the battery cuz it's got two charge timers where during that window it should start charging full charging the battery and it wasn't.

**Dave Jones:** So, I've trying to find it where that was in the cloud and why that wasn't working. I finally found it. I looked at the tutorial video on the Solis YouTube channel, but it was out of date.

**Dave Jones:** So, it was like 2 years ago and it looks and feels different. So, I'll show you where to change the, um, charge timer. So, let's go into device over here.

**Dave Jones:** You have to go into device and we've got our inverter and you can like the data data logger is like that Wi-Fi, uh, adaptery, um, thing they call it the data logger.

**Dave Jones:** Um, and so we need to go into the inverter here and if we go into the inverter that just gives us a similar display over here, but it gives us some graphs and we can, you know, do some fancy graphing and stuff.

**Dave Jones:** Haven't really played around with that, uh, at all yet, but, um, we go up to inverter control, this button up here, inverter control. So, let's go into that and it was not obvious where the charge timer was.

**Dave Jones:** It was supposed to be here. It'd be so nice if it was just here like charge timer, please. And that's what it was in the old version of software, but they changed it.

**Dave Jones:** So, we have to go into, I think, storage mode. Twiddle your thumbs. Takes a bit of time to update. Come on, you can do it. And it's down here, charge and discharge slot.

**Dave Jones:** They call it a slot. So, uh whatever. So, we can go in here and we can view what it's currently um at or we can uh set it. I do actually want to change it because I've been fiddling with it um just before I started this video.

**Dave Jones:** So, we've got two uh charge timers and I originally from here it is, charge timer one from 11:00 a.m. I originally had that set to uh 2:00 p.m. So, let's actually well, I can't type that.

**Dave Jones:** So, we'll change that to 2:00 and 150 amps. 150 amps at um 53 volts like nominal battery battery voltage. That's around about the 8 kW um limit there. So, I would just set uh a normal 150 amps.

**Dave Jones:** And I originally, I think why it wasn't working today is because this was set, the state of charge was set to 21% and the battery is already higher than that.

**Dave Jones:** The battery is at currently 50 60% or something. Um so, yeah. It wasn't going to charge. So, I've set that to a 100% and so, if the battery is not 100% during that free 3-hour window, say that three times quickly.

**Dave Jones:** Free 3-hour window. It'll charge the battery and if it's even at 99%, it'll still actually charge it. And I want to disable I was just mucking around with this charge timer slot two.

**Dave Jones:** So, I'm going to disable that and um that should work. There is a time period conflict. Oh god, what? But but it's disabled. Is that a That's that's a bug, right?

**Dave Jones:** It's it's disabled. There should be no conflict whatsoever. There should be none. So, 0000. Okay. Right. Yeah. Small bug there. Command successful. There we go. RS485 command. Boom. Boom.

**Dave Jones:** Boom. Look at that. Shows you the actual command sent. By the looks of it, is that the actual That's the actual RS485 command sent. That's useful, I guess. So, um now unfortunately, it won't up- I I did this before and it didn't update live.

**Dave Jones:** So, I'm going to have to probably wait a bit, maybe like there's a 5-minute window where it updates or something. But yeah, it I immediately changed it before and it didn't um reflect here, but trust me but just before I started shooting the video, it was actually charging at like 7 and 1/2 8 kW or something like that.

**Dave Jones:** So, I'll pause this and I'll get back to you when it's actually working. Ah, there you go. Yeah, that only took like less than 5 minutes or something and it's updated again and now we're charging.

**Dave Jones:** Ta-da! At 8 kW there. So, I'm using my uh free 3-hour window and we've got 4.7 from the solar. Uh we've got some AC coupled stuff as well and uh the EV still charging there.

**Dave Jones:** Now we're pulling 11 kW from the grid. Beauty um because it's free. I don't pay for it. Uh it's coming from everyone else's solar at the moment as well as mine, uh of course.

**Dave Jones:** So, this uh Solis system in terms of usability and setting up, it's not easy. It's probably not for your average Joe. It's not like a Tesla system or something like that even though I've never used one.

**Dave Jones:** I have seen, you know, apparently it's pretty easy. But yeah, it looks like I can do stuff. So, winner winner chicken dinner. I can do that remotely. I I still don't really understand the AC coupled thing and cuz there's no like other gen port option or something like that that I can find yet.

**Dave Jones:** I don't know. If you know how exactly I'm doing that, leave it in the comments down below. But yeah, it's a bit weird how they've implemented uh the AC couple was tied to some other optional something and I I didn't like the way that was um set up.

**Dave Jones:** That could actually be coming from in like the actual gen port, but if it is, then I don't Well, I want that, but I also want the AC coupled to come from the Enphase system as well.

**Dave Jones:** So, I haven't still haven't verified that that is 100% operational yet. But anyway, it's good enough for Australia. I'm charging my battery. It's currently at 51% of my 75 kWh there and it's charging at uh 8 8 kW.

**Dave Jones:** Beautiful. Look at that. Um the inverter will be getting a bit warm, but that's why it's got a fan on it, right? How How long it lasts? I don't know.

**Dave Jones:** Heard good things about the Solis. They're pretty reasonable apparently, so we'll see. But there you go. That is just like a sort of first day update. I'm still troubleshooting.

**Dave Jones:** I'm still learning this whole thing and but I seem to have nailed the timer anyway. Beauty. Catch you next time.
