---
video_id: 3hHG_WcJtQo
title: Solis Cloud & Battery Charge Timer
url: https://www.youtube.com/watch?v=3hHG_WcJtQo
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 29, "3": 48, "4": 65, "5": 79, "6": 91, "7": 104, "8": 118, "9": 130, "10": 144, "11": 156, "12": 170, "13": 181, "14": 195, "15": 208, "16": 220, "17": 231, "18": 247, "19": 261, "20": 277, "21": 291, "22": 306, "23": 322, "24": 340, "25": 359, "26": 374, "27": 387, "28": 401, "29": 419, "30": 432, "31": 443, "32": 458, "33": 471, "34": 484, "35": 501, "36": 516}
---

**Dave Jones:** Hi, first look at my new Solace inverter Solace Cloud thing. I've got the thing installed, commissioned, and connected via the Wi-Fi dongle thing, which plugs into the bottom of the USB port, and it's connected to my home network,

**Dave Jones:** so I can access this anywhere in the world now. So, let's just have a look at here cuz I was trying to debug a problem, which it I still currently have. Trust me, it was working a minute ago, but I'll show

**Dave Jones:** you why it's not working in a minute. I wanted it's currently 12:30 p.m., so it's within my 3-hour free charging window. So, obviously, I want to charge my new 75-kW hour battery home storage battery. I want to use as much energy. I want to

**Dave Jones:** charge the EV and also the home storage battery during that free 3-hour window, which apparently they just announced a few days ago that they're going to offer to everyone now. Everyone in Australia, regardless your energy retailer, is supposed to now

**Dave Jones:** have an option for if if you want to join, like they have to have a plan option where there's a 3-hour energy window per day cuz we've just got too much solar here in Australia. So, yeah, we have to use it

**Dave Jones:** because when we installed all the solar here, it didn't have the ability to curtail it and switch it off and stuff. So, anyway, so they want people to use it. So, I want to charge that. So, here's the display. It's pretty groovy

**Dave Jones:** here. So, I've got my PV up it the sun just peeked out at the moment. I've got the AC coupling that'll be coming from the Enphase system, but I think that's just the residual from the Enphase system. I'm not sure. I still haven't

**Dave Jones:** figured out the gen port, which is connected to my two-panel Hoymiles microinverters. Still haven't figured that out, but I think anyway, AC coupling, I think that's coming from the Enphase system or the residual of it. The battery, of course, uh, whether or

**Dave Jones:** not it's it's doing nothing at the moment, actually. Um, and we might see why in a minute. Um, and the grid there's 2 kW coming in from the grid. Um, that's interesting because the battery's shut off for some reason,

**Dave Jones:** anyway. The grid load here, um, is um, we're charging the EV at the moment. So, this is on the So, that will show up as grid load here and the backup load is the rest of the house. So, um,

**Dave Jones:** family's home at the moment, so they're taking 3.8 kW in the house. So, you know, they're probably I don't know, they might have an aircon or something like that. That's more than normal. Mrs. EV blog could be cooking something or

**Dave Jones:** thing things like that. Anyway, now I thought I had set up the, uh, timer uh, the charge timer for the battery cuz it's got two charge timers where during that window it should start charging full charging the battery and it wasn't.

**Dave Jones:** So, I've trying to find it where that was in the cloud and why that wasn't working. I finally found it. I looked at the tutorial video on the Solis YouTube channel, but it was out of date. So, it

**Dave Jones:** was like 2 years ago and it looks and feels different. So, I'll show you where to change the, um, charge timer. So, let's go into device over here. You have to go into device and we've got our inverter and you can like the data data

**Dave Jones:** logger is like that Wi-Fi, uh, adaptery, um, thing they call it the data logger. Um, and so we need to go into the inverter here and if we go into the inverter that just gives us a similar display over here, but it gives us some

**Dave Jones:** graphs and we can, you know, do some fancy graphing and stuff. Haven't really played around with that, uh, at all yet, but, um, we go up to inverter control, this button up here, inverter control. So, let's go into that and it was not

**Dave Jones:** obvious where the charge timer was. It was supposed to be here. It'd be so nice if it was just here like charge timer, please. And that's what it was in the old version of software, but they changed it. So, we have to go into, I

**Dave Jones:** think, storage mode. Twiddle your thumbs. Takes a bit of time to update. Come on, you can do it. And it's down here, charge and discharge slot. They call it a slot. So, uh whatever. So, we can go in here and we

**Dave Jones:** can view what it's currently um at or we can uh set it. I do actually want to change it because I've been fiddling with it um just before I started this video. So, we've got two uh charge timers and I originally

**Dave Jones:** from here it is, charge timer one from 11:00 a.m. I originally had that set to uh 2:00 p.m. So, let's actually well, I can't type that. So, we'll change that to 2:00 and 150 amps. 150 amps at um 53

**Dave Jones:** volts like nominal battery battery voltage. That's around about the 8 kW um limit there. So, I would just set uh a normal 150 amps. And I originally, I think why it wasn't working today is because this was set, the state

**Dave Jones:** of charge was set to 21% and the battery is already higher than that. The battery is at currently 50 60% or something. Um so, yeah. It wasn't going to charge. So, I've set that to a 100% and so, if the battery is

**Dave Jones:** not 100% during that free 3-hour window, say that three times quickly. Free 3-hour window. It'll charge the battery and if it's even at 99%, it'll still actually charge it. And I want to disable I was just mucking around with this charge timer

**Dave Jones:** slot two. So, I'm going to disable that and um that should work. There is a time period conflict. Oh god, what? But but it's disabled. Is that a That's that's a bug, right? It's it's disabled. There should be no

**Dave Jones:** conflict whatsoever. There should be none. So, 0000. Okay. Right. Yeah. Small bug there. Command successful. There we go. RS485 command. Boom. Boom. Boom. Look at that. Shows you the actual command sent. By the looks of it, is that the actual

**Dave Jones:** That's the actual RS485 command sent. That's useful, I guess. So, um now unfortunately, it won't up- I I did this before and it didn't update live. So, I'm going to have to probably wait a bit, maybe like there's a 5-minute

**Dave Jones:** window where it updates or something. But yeah, it I immediately changed it before and it didn't um reflect here, but trust me but just before I started shooting the video, it was actually charging at like 7 and 1/2

**Dave Jones:** 8 kW or something like that. So, I'll pause this and I'll get back to you when it's actually working. Ah, there you go. Yeah, that only took like less than 5 minutes or something and it's updated again and now we're charging.

**Dave Jones:** Ta-da! At 8 kW there. So, I'm using my uh free 3-hour window and we've got 4.7 from the solar. Uh we've got some AC coupled stuff as well and uh the EV still charging there. Now we're pulling 11 kW from the grid. Beauty um because

**Dave Jones:** it's free. I don't pay for it. Uh it's coming from everyone else's solar at the moment as well as mine, uh of course. So, this uh Solis system in terms of usability and setting up, it's not easy. It's

**Dave Jones:** probably not for your average Joe. It's not like a Tesla system or something like that even though I've never used one. I have seen, you know, apparently it's pretty easy. But yeah, it looks like I can do stuff. So, winner winner

**Dave Jones:** chicken dinner. I can do that remotely. I I still don't really understand the AC coupled thing and cuz there's no like other gen port option or something like that that I can find yet. I don't know. If you know how exactly I'm doing

**Dave Jones:** that, leave it in the comments down below. But yeah, it's a bit weird how they've implemented uh the AC couple was tied to some other optional something and I I didn't like the way that was um set up. That could actually be coming

**Dave Jones:** from in like the actual gen port, but if it is, then I don't Well, I want that, but I also want the AC coupled to come from the Enphase system as well. So, I haven't still haven't verified that that

**Dave Jones:** is 100% operational yet. But anyway, it's good enough for Australia. I'm charging my battery. It's currently at 51% of my 75 kWh there and it's charging at uh 8 8 kW. Beautiful. Look at that. Um the inverter will be getting a bit

**Dave Jones:** warm, but that's why it's got a fan on it, right? How How long it lasts? I don't know. Heard good things about the Solis. They're pretty reasonable apparently, so we'll see. But there you go. That is just like a sort of first day update.

**Dave Jones:** I'm still troubleshooting. I'm still learning this whole thing and but I seem to have nailed the timer anyway. Beauty. Catch you next time.
