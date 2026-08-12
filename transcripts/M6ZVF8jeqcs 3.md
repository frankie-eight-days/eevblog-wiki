---
video_id: M6ZVF8jeqcs
title: EEVBlog WebNX Data Center Server FIRE!
url: https://www.youtube.com/watch?v=M6ZVF8jeqcs
source: youtube-asr
timestamps: {"0": 2, "1": 15, "2": 38, "3": 50, "4": 59, "5": 88, "6": 102, "7": 112, "8": 126, "9": 139, "10": 161, "11": 176, "12": 186, "13": 200, "14": 223, "15": 234, "16": 253, "17": 269, "18": 286, "19": 297, "20": 316, "21": 326, "22": 349, "23": 361, "24": 375, "25": 385, "26": 399, "27": 415, "28": 423, "29": 435, "30": 452, "31": 462, "32": 476, "33": 487, "34": 501, "35": 516, "36": 529, "37": 542, "38": 563, "39": 574, "40": 585, "41": 607, "42": 622, "43": 642, "44": 653, "45": 667, "46": 690, "47": 696, "48": 705, "49": 715}
---

**Dave Jones:** Hi, just a quick update a video because you might have noticed that uh what what what what the EEVblog website is down. That means the center of the universe is down, which is the EEVblog forum.

**Dave Jones:** Um everyone's getting withdrawal symptoms. They're having to check themselves into clinics and all sorts of things because um yeah, they can't get their fix of uh the EEVblog uh forum unfortunately and the website and my email has also uh been down since as of approximately uh the 4th of the 4th at uh 2100 hours.

**Dave Jones:** Uh it's been down for quite a few days now. What is it currently? It's the 6th of April, um almost midnight on the uh yeah, so almost the 7th of April now.

**Dave Jones:** So, it's been down for like 3 days or something. Um yeah, and it's kind of a big deal. So, I just wanted to uh update you on what's happening.

**Dave Jones:** Not that I know much. Uh we're waiting for it to come back because uh what happened is there was a fire basically at the uh data center in uh Ogden, Utah at Gorilla Servers, which is the company I use to host the dedicated servers uh for the EEVblog website, the EEVblog forum, EEVblog.org is also uh down where I do the podcast, uh host the podcast videos, like the streaming 720p

**Dave Jones:** podcast version and stuff like that. It's all down. Their entire Even their own website does not work. I'll refresh that now. Nope, gorillaservers.com is down. Um so, they do actually have an update uh here on WebNX.

**Dave Jones:** I guess it's one of their other companies that's still up cuz it's ironically hosted somewhere else. So, let's have a quick read of this. Now that we have a better understanding of what happened, we'd like to give everyone an update.

**Dave Jones:** One of our old generators that have has worked for years and was recently load tested had a mechanical failure and caught fire resulting in power being cut to our core routers and fire suppression system controlling the fire.

**Dave Jones:** So, I guess the automatic sprinklers and everything else or fire suppression. They probably might not use water, they might use, you know, some gas or some data centers, you know, fill up with inert gas and things like that which extinguish the fires.

**Dave Jones:** Not sure which. Unfortunately, the fire department opted to cut power to the rest of the building as a precaution even though the power systems were independent. So, it's even though this backup generator fire failed, the fire was controlled, this data center could have still operated including presumably my servers.

**Dave Jones:** So, yeah, they but the fire department just cut power to the whole complex. It's a massive complex in the middle of the desert somewhere. Yeah, we are currently waiting for an emergency inspector to arrive, give the all clear so I'm bringing back most of the servers in Ogden back online.

**Dave Jones:** Some servers will have an extended outages as may require rebuilds due to some water damage. Okay, it looks like they do have sprinkler system or that might have been the fire department, who knows.

**Dave Jones:** Whose builds have high probability that data is intact. We'd like to thank you for your patience. Blah blah blah blah blah. So, yeah, their latest update on Twitter they've yeah, current Gorilla Servers Inc.

**Dave Jones:** Host Fusion. Follow Host Fusion on Twitter. That's GNIF on the EV blog forum. He's the one who maintains the EV blog servers. And Gorilla Servers current updates project that close to 90 to 95% of all Gorilla Servers hardware make it bigger, experienced zero damage.

**Dave Jones:** What's the bet? Even money that the EV blog servers are the ones impacted. Anyway, electricians are working now to restore power to the Ogden, Utah data center and they're estimating power should have returned at approximately 3:00 p.m.

**Dave Jones:** MD MDT I think that's mountain time or something tomorrow. So, that time has passed but since then last night my emails started come back. So, the my email server I've got a cPanel email server which handles email and a bunch of other stuff.

**Dave Jones:** That's all working again and cuz if you don't know, we have three servers for the that handle all the EE V blog infrastructure. One is as I said the email server and the which handles some other stuff as well and also two redundant dedicated servers.

**Dave Jones:** These are all dedicated boxes. They aren't shared so I've got actually three dedicated boxes. They're Xeon something or other. Anyway, two redundant Xeon database servers which handles all of the forum and the WordPress website and all my online store and stuff like that.

**Dave Jones:** Yes, my online store's down. I might still be able to ship some stuff if you've got an order in because then it I use a third-party shipping system so the orders might have been automated I haven't checked today.

**Dave Jones:** We're going to ship some today but they should automatically have been imported in so hopefully those will still go out even though this is all down. So, yeah so I've got the so there are redundant servers so if one fails it takes the like the database is mirrored and shared and it's all complex Genefis set all this up.

**Dave Jones:** It's all you know advanced penguin stuff. I don't know too much about it but yeah so that's all safe and by the way all the data safe all the backups.

**Dave Jones:** If for some reason the server the data center has actually lost the data on the drives in the server machines we do have full daily backups in two separate locations professional backup services and at most we might and Genefis said that And he did check and it was during the backup time is when the whole thing went down.

**Dave Jones:** So at worst we're going to lose like a day's worth of posts on the forum or something like that if my server is one of the ones affected. So there you go, which Murphy I said like yeah, it's going to be back.

**Dave Jones:** It's interesting that my cPanel email server is back but the others aren't but they are on different subnets. It could be fine. There's good chance it's fine but they're within different subnets in the data center.

**Dave Jones:** So yeah, so they brought one subnet back up and the other ones yeah, they're just separate. So we we just don't know. We just got to sit back and wait.

**Dave Jones:** They have said that they can't uh like give dedicated you know say oh yeah, this client's servers will be back up and running or whatever time. But anyway, they are past the time when it's supposed to come back up and the website hasn't come back up yet.

**Dave Jones:** So we're just going to have to wait. I don't know how long it's going to be. So yeah, that raises some interesting questions and we just put up a dedicated GNF just got this dedicated page hosted somewhere else and redirected the DNS's.

**Dave Jones:** So at least it shows you something and this you'll get the updates. There's no more update. I don't think he's updating anything in the background. No. No, we're just going to have to wait.

**Dave Jones:** He's monitoring it and it'll eventually come back online but that raises some interesting questions. I know there's going to be 1 million responses down below of how we're doing it all wrong and we should be using a cloud infrastructure.

**Dave Jones:** We should be using a more reliable data center and come on, right? Fire in a data center, fire in a generator, this could have happened to any data center really and I guess you can make an argument that it should be on you know Amazon cloud or whatever but hasn't that gone down in the past?

**Dave Jones:** I mean it's just like Murphy's going to get you, right? We've had no issues with this current host for I don't know, I mean five plus years at least, I think.

**Dave Jones:** We've been on these dedicated boxes at Gorilla servers and we haven't had an issue apart from like technical stuff, you know, like it's yeah, it's not like they were unreliable.

**Dave Jones:** It's just other things sort of have taken the website down here or there for like, you know, hours or a day or something like that. But yeah, that wasn't really the servers their actual fault.

**Dave Jones:** So Anyway, yeah, I don't know. Flame away down below. Yeah, got caught with the pants down. Data is safe, but yeah, it's been out for three, probably four, could be longer days that everything's down.

**Dave Jones:** At least my email is back and I guess that's a lesson that I need to set up some sort of redundant email exchange server thingamabob. I do actually use Gmail for all of my Gmail's actually my interface for email.

**Dave Jones:** So if you send a email to david@eevblog.com, then it actually just gets forwarded into Gmail and it actually replies. I've got like the reply to section in there is david@eevblog.com.

**Dave Jones:** So you don't know that I'm actually reading all my email on Gmail. So it's mostly there, but anyway, it is back up, but yeah, cuz a lot of stuff was tied to david@eevblog.com, yeah, I couldn't do a lot of stuff.

**Dave Jones:** Like I couldn't get like do email confirmations for doing various online activities and stuff like that. So yeah, it's a bit I I Gmail's gone down before. So you know, yeah, it's Murphy's going to get you at the worst possible time it will happen.

**Dave Jones:** So I don't know. Yeah, everyone will flame away down below. Hey dumbasses Dave for using that, you know, just hosting it on a couple of little dedicated boxes in the middle of Utah somewhere.

**Dave Jones:** No, there's there's reasons why we do that. A lot of people ask why we don't host in Europe or something like that. The majority of uh the viewers and the forum users and stuff like that are sort of like US based.

**Dave Jones:** US is probably the best place to actually host it in terms of like latency and, you know, all that uh sort of stuff. So, you know, yeah, it could be hosted here in Australia, could be hosted in the EU, could be hosted in, you know, some little I don't know, tin pot island somewhere um in the Pacific or something, but I Yeah.

**Dave Jones:** Anyway, there you go. Just wanted to give you an update. Uh so, I can't do the Keysight uh drawing, by the way, because the forum's not available. I You know, I don't have ability to uh run my wobbulator program and all that, but I'll probably do uh the drawings for the other uh ones, probably today.

**Dave Jones:** So, yeah, anyway, there you go. Just wanted to give you an update. It's down, could be down for a while. I got no idea um if we do have to if my servers were impacted by the uh water damage or whatever and the hard drives were lost, yeah, we might lose like, you know, half a day or up to a day at most worth of uh forum posts or something like that.

**Dave Jones:** So, if that does happen, um sorry. It's uh yeah, there's probably reasons I think we did look at doing like a live database backup somewhere. We already run a redundant system.

**Dave Jones:** It's just that the whole data center has gone down. So, it's like, you know, so we just do a daily uh backup. So, yeah, we don't have a third off-site redundant live redundant synced database server.

**Dave Jones:** It's all complicated when you try to write to multiple databases at multiple times. We've actually had uh technical issues regarding on on the forum regarding actual uh the use of having the multiple databases cuz you got the sync issues with the I don't know the exact um you know, technical stuff behind it, but, you know, it can get complicated when you try and share all of your databases,

**Dave Jones:** you know, they're trying to all sync and be live and stuff like that. We have image problems on the forums for attachments, they weren't linking correctly and stuff like that.

**Dave Jones:** So, if all your databases aren't synced, um I'm sure Jaden if can inform people down below if you got technical questions about the whole thing, but there you go.

**Dave Jones:** Yep, still down. I don't know when it'll be back. Sorry, got no idea. Um we'll just have to wait like everyone else, but my email is back, david@evblog.com, so that allows me to do some stuff.

**Dave Jones:** Uh yeah. Flame away. Catch you next time.
