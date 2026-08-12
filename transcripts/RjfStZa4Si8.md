---
video_id: RjfStZa4Si8
title: AERL Battery Firmware Update
url: https://www.youtube.com/watch?v=RjfStZa4Si8
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 29, "3": 43, "4": 54, "5": 68, "6": 85, "7": 95, "8": 106, "9": 119, "10": 130, "11": 142, "12": 156, "13": 176, "14": 188, "15": 201, "16": 210, "17": 220, "18": 237, "19": 245, "20": 262, "21": 277, "22": 289}
---

**Dave Jones:** Hi, an update on the AIRL batteries here. I finally, well, we um Peter from AERL uh who remote desktopped in today um to fix that Raspberry Pi uh compute module that was on the uh you know that was on this board here.

**Dave Jones:** Anyway, uh we've updated all that. We installed the software remotely and finally got the thing working. So, rate my Bodgege setup. Uh we've got the finally got the gateway working here.

**Dave Jones:** Okay. But I've still got a problem with the Ethernet at home here. So uh temporarily we're um we're uh using an external 4G modem here for internet just for that.

**Dave Jones:** Just for that um because well it can't connect it. We do have Ethernet internally apparently on the uh CM4 module but uh yeah I haven't set that up yet.

**Dave Jones:** I'm not sure. I don't know. You'd probably have to put it on top. Wouldn't work with inside the metal cabinet. I don't know. Whatever. And because I've got my solar analytics thing bodgeged up here still, I haven't put it in a case or anything.

**Dave Jones:** That's my solar analytics which runs the 4 RS485 cable, not RS232, RS485 um into here. DI my inverter DI run the RS485 and the canvas on the same physical connector.

**Dave Jones:** So I've got to whack them in parallel and because I couldn't physically fit this double adapter into here whereas I could I originally had it down here but now I've got the gateway in there on the canvas.

**Dave Jones:** The gateway is on the canvas so I couldn't physically fit it in. So I had to get an inline joiner to bodgege that in. Um, so yeah, rape my setup.

**Dave Jones:** And because I haven't got a proper USB power adapter at the moment, I'm powering it from external DC, which comes from an external lab power supply. It's only drawing two watts.

**Dave Jones:** Um, so yeah. But anyway, uh, rate my bodgege setup out of 10, please. Um, how bodgeged is this setup? I I do I've got to win some award for this.

**Dave Jones:** Um, surely. So, um, yes, I'll just keep it like this. It works. Although, I'll fix the power adapter and I'll probably fix the Ethernet um thing as well. Yeah, something wrong with the Ethernet coming out to the lab here.

**Dave Jones:** No, it's not what killed that um CM4 compute module. I think it's just a DC toDC converter failure. Maybe triggered by an external USB or trying different USB sources and I don't know, maybe one of them took it out or something.

**Dave Jones:** But anyway, we finally got the thing working and all of the firmware has now been updated cuz I had very early firmware in mine. And uh this battery down here um you know it worked for a couple of months, but it actually uh like shut off and started flashing orange down here uh for a while.

**Dave Jones:** So I've actually had that out of action for a week or two, that uh battery. And um so we think it might be like a firmware compatibility, like a firmware um issue.

**Dave Jones:** So anyway, because I did buy um some extra batteries um for it after we got the regular ones installed, uh the original ones installed. So maybe there was a mismatch, but anyway, you can update the firmware all remotely.

**Dave Jones:** Peter's done that. It's updated all the firmware. I've got access to the new um cloudy gateway um thing, which allows me to like to see all the stats for the batteries and stuff like that.

**Dave Jones:** I probably have to do a separate uh video on that. I won't do it here. I won't edit that in here. But yeah, anyway, rate my bodgege setup. It's just Oh, it's terrible, Muriel.

**Dave Jones:** Um, but yeah, it does now work. So, yeah, bloody DI with their RS485 and can sharing the same connector and the gateway um the PCB on the gateway doesn't route all the connections over and you wouldn't expect it to.

**Dave Jones:** So that's why um this was this double adapter was working when I put it on this side of the gateway, but it went like the um before I didn't have the gateway.

**Dave Jones:** Sorry. Um and but once I put the gateway in series, it didn't work on the output side of the gateway because the internal pins, there's just two pins there for the RS485, uh weren't actually joined um through because that's a specific DI thing.

**Dave Jones:** That's not like an industry standard thing or whatever. So anyway, ah boy, they're back up and running now. Woohoo. So I'm back in business with the latest firmware cuz yeah, I had like very early firmware in these batteries.

**Dave Jones:** But finally, it's taken us a long time to sort out these problems cuz we were having all sorts of um issues caused by some things at my end basically.

**Dave Jones:** Anyway, fantastic rate my budge setup. Catch you next time.
