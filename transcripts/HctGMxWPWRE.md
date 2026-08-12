---
video_id: HctGMxWPWRE
title: Deye Hybrid Inverter Time Sync Issue UPDATE + Battery News
url: https://www.youtube.com/watch?v=HctGMxWPWRE
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 34, "3": 50, "4": 67, "5": 82, "6": 98, "7": 113, "8": 127, "9": 142, "10": 158, "11": 172, "12": 188, "13": 199, "14": 211, "15": 225, "16": 239, "17": 254, "18": 269, "19": 282, "20": 296, "21": 311, "22": 324, "23": 334, "24": 347, "25": 362, "26": 376, "27": 388}
---

**Dave Jones:** Hi, just an update on my DI uh hybrid inverter here. I solved the uh issue with the clock or mostly. Um I've installed I found I finally found it and installed the Wi-Fi uh dongle there as you can see. Um instead of the RS232

**Dave Jones:** going to my Solar Assistant Raspberry Pi. Um and I've managed to fix it. So, I've now got um RS485 go into the uh Raspberry Pi. Sorry, you probably can't see the screen. It's just horrible out here. Don't know what

**Dave Jones:** that's like. But uh anyway, um yeah, so the Raspberry Pi running solar assistant is now on RS485 link. I had to get the uh cable for that because it's a shared RS485 and CAM bus. The CAM bus goes off to the battery.

**Dave Jones:** Anyway, um so I've now got the Wi-Fi dongle. I'm now um hooked into the the DI cloud thing or whatever it is. Anyway, um with that, it now does do the time sync. I'm still losing the time like 10 minutes per day, but it is now

**Dave Jones:** reyncing. So, I've got the time sync option uh set on this thing, but there's still a problem in that yes, it does drift 10 minutes per day, but it only syncs. And I've confirmed this with DI, the design of this thing. Yeah, not sure

**Dave Jones:** if you can see that again, but when you hit that time sync function up there, um it only syncs it only resyncs when the internal clock in this thing is uh plus or minus 5 minutes from the network

**Dave Jones:** time. So, this thing still drifts well minus 5 minutes. Yes, is it minus? Yes, minus 5 minutes a day. It loses 5 minutes a day. Um, so yeah, it can still be out by plus minus 5 minutes. That's

**Dave Jones:** the design of this heap of crap. It's unbelievable. But and hey, at least my timers now work. So I've got free power available from 11:00 a.m. to 2:00 p.m. And I set it for like 5 minutes. So 11

**Dave Jones:** minutes past 5 and 11 minutes 2 just in case and 5 minutes to 2:00 just in case um to, you know, cater for the error in this thing. But oh, what a heap of crap really. Um, this DI has been. It's just

**Dave Jones:** unbelievable. Anyway, it is now connected to the Wi-Fi. Um, and it is time syncing, but yeah, five plus - 5 minutes a day is the design of this turd. Unbelievable. Anyway, um, it has basically fixed my problem. I do now at

**Dave Jones:** least it now keeps time relatively close and I can actually get my free power time window uh during the day to charge the battery regardless of the weather. So anyway, that's the update. And there's my Raspberry Pi running the uh

**Dave Jones:** solar assistant uh thing. And yes, I do have uh the Hoy Miles um uh thing. Well, like a wireless adapter thing. Um, and I can actually connect to my inverter up there, but I haven't like reinstalled the old one to see if I can like re

**Dave Jones:** flash it or do whatever. Anyway, uh that that's powered from my uh Yeti 400 uh battery here just next to it. Um so yeah, I need to get a case for this. It's just bodgeged in. But anyway, I do

**Dave Jones:** now have I got the official CAN um adapter cable for it because it only uses the two pins because that RJ11 connector on the DI, it actually has two buses. It's got uh the CAN and uh uh the

**Dave Jones:** CAN bus and well, it's actually got two RS485 buses and it's only using uh two wires. So, I've actually um just connected that on. I didn't have to run a new cable. I ran the existing cable cuz I think this one is the Yeah, this

**Dave Jones:** is the cable coming in from the DI Hybrid and it's running all pairs in there. Um I I won't disconnect it, but yeah, it's it's running all the pairs, but the CAN uh that goes to the Raspberry Pi is only tapping off two of

**Dave Jones:** the pins. And thoughtfully, ARL designed this thing so that it wasn't um it doesn't connect the can the other pins and that it doesn't need to. So, they're just floating there. So, I can actually just tap off parallel. So I can just uh

**Dave Jones:** bodgege parallel using an adapter like this uh to go off to my solar assistant for those unused can lines. So I didn't have to run an extra cable from my DI. So yeah, thanks very much Peter from AERL for designing that thing. Right. So

**Dave Jones:** yeah, it just didn't um tap into the other lines that didn't need to. So, um, yeah. So, the, uh, DI hybrid inverter talks to here via the CAN lines, which are which use a different pair in there to the RS485,

**Dave Jones:** which uses a different pair. And then that just now goes off to my solar assistant. So, there you go. That's the update for the dodgy uh, DI hybrid inverter. Don't touch the things. They're awful. Um, had so many issues.

**Dave Jones:** But anyway, technically, it's kind of sort of fixed my problem. Um, and this battery, by the way, I um I will actually be moving this outside um because we actually need the room in the garage. Um so yeah, I'll be and I'll

**Dave Jones:** probably be expanding this battery system as well. Um cuz the government is money printer go and um yeah, I'm I'm probably going to um expand the battery on this thing. So yeah, stay tuned for that. Um but we'll

**Dave Jones:** see what happens there. But yeah, um I'm going to I'm going to have to I'm going want to keep this rack, of course, because it's the purpose-designed rack for it, but I want to move this entire thing outside. So, I need an outdoor

**Dave Jones:** weather uh cabinet. So, I want to put this cabinet inside another weather cabinet. So, if you've got any good um links to um good outdoor weather cabinets I can use, uh leave it in the comments down below. But anyway, that's

**Dave Jones:** the plan. Um and yeah, I'm back in business uh charging this battery during the day. um during that threehour free window. And uh yeah, fantastic. But I can only charge at the maximum 5 kilowatt. So I can only get a maximum 15

**Dave Jones:** kilwatt hours per day. And this is a 25 kWh uh battery. I've still got room for one more down there. Um yeah, this is a 25 kWh battery, but I at least I can get 15 kwatt hours per day for free from the

**Dave Jones:** grid because we've got too much excess solar on our grid. So, yeah, I'm going to use it uh using that time window. So, that's what it's currently uh doing. It's not 11:00 a.m. yet, but it'll kick in and uh regardless of what the sun's

**Dave Jones:** doing, I can get at least 15 kilowatt hours per day from this thing, which should last me basically overnight if we don't do anything drastic. So, there's the update. Catch you next time.
