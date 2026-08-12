---
video_id: M6ZVF8jeqcs
title: EEVBlog WebNX Data Center Server FIRE!
url: https://www.youtube.com/watch?v=M6ZVF8jeqcs
source: youtube-asr
---

**Dave Jones:** Hi, just a quick update a video because you might have noticed that uh what what what what the EEVblog website is down. That means the center of the universe is down, which is the EEVblog forum. Um everyone's getting withdrawal

**Dave Jones:** symptoms. They're having to check themselves into clinics and all sorts of things because um yeah, they can't get their fix of uh the EEVblog uh forum unfortunately and the website and my email has also uh been down since as of approximately uh

**Dave Jones:** the 4th of the 4th at uh 2100 hours. Uh it's been down for quite a few days now. What is it currently? It's the 6th of April, um almost midnight on the uh yeah, so almost the 7th of April now.

**Dave Jones:** So, it's been down for like 3 days or something. Um yeah, and it's kind of a big deal. So, I just wanted to uh update you on what's happening. Not that I know much. Uh we're waiting for it to come back because uh

**Dave Jones:** what happened is there was a fire basically at the uh data center in uh Ogden, Utah at Gorilla Servers, which is the company I use to host the dedicated servers uh for the EEVblog website, the EEVblog forum, EEVblog.org is also uh

**Dave Jones:** down where I do the podcast, uh host the podcast videos, like the streaming 720p podcast version and stuff like that. It's all down. Their entire Even their own website does not work. I'll refresh that now. Nope, gorillaservers.com is down. Um so, they do actually have an

**Dave Jones:** update uh here on WebNX. I guess it's one of their other companies that's still up cuz it's ironically hosted somewhere else. So, let's have a quick read of this. Now that we have a better understanding of what happened, we'd

**Dave Jones:** like to give everyone an update. One of our old generators that have has worked for years and was recently load tested had a mechanical failure and caught fire resulting in power being cut to our core routers and fire suppression system

**Dave Jones:** controlling the fire. So, I guess the automatic sprinklers and everything else or fire suppression. They probably might not use water, they might use, you know, some gas or some data centers, you know, fill up with inert gas and things like that which

**Dave Jones:** extinguish the fires. Not sure which. Unfortunately, the fire department opted to cut power to the rest of the building as a precaution even though the power systems were independent. So, it's even though this backup generator fire failed, the fire was controlled, this

**Dave Jones:** data center could have still operated including presumably my servers. So, yeah, they but the fire department just cut power to the whole complex. It's a massive complex in the middle of the desert somewhere. Yeah, we are currently waiting for an

**Dave Jones:** emergency inspector to arrive, give the all clear so I'm bringing back most of the servers in Ogden back online. Some servers will have an extended outages as may require rebuilds due to some water damage. Okay, it looks like they do have

**Dave Jones:** sprinkler system or that might have been the fire department, who knows. Whose builds have high probability that data is intact. We'd like to thank you for your patience. Blah blah blah blah blah. So, yeah, their latest update on Twitter they've yeah,

**Dave Jones:** current Gorilla Servers Inc. Host Fusion. Follow Host Fusion on Twitter. That's GNIF on the EV blog forum. He's the one who maintains the EV blog servers. And Gorilla Servers current updates project that close to 90 to 95% of all Gorilla Servers hardware

**Dave Jones:** make it bigger, experienced zero damage. What's the bet? Even money that the EV blog servers are the ones impacted. Anyway, electricians are working now to restore power to the Ogden, Utah data center and they're estimating power should have

**Dave Jones:** returned at approximately 3:00 p.m. MD MDT I think that's mountain time or something tomorrow. So, that time has passed but since then last night my emails started come back. So, the my email server I've got a cPanel email

**Dave Jones:** server which handles email and a bunch of other stuff. That's all working again and cuz if you don't know, we have three servers for the that handle all the EE V blog infrastructure. One is as I said the email server and the which handles

**Dave Jones:** some other stuff as well and also two redundant dedicated servers. These are all dedicated boxes. They aren't shared so I've got actually three dedicated boxes. They're Xeon something or other. Anyway, two redundant Xeon database servers which handles all of the forum

**Dave Jones:** and the WordPress website and all my online store and stuff like that. Yes, my online store's down. I might still be able to ship some stuff if you've got an order in because then it I use a third-party shipping system so the

**Dave Jones:** orders might have been automated I haven't checked today. We're going to ship some today but they should automatically have been imported in so hopefully those will still go out even though this is all down. So, yeah so I've got the so there are

**Dave Jones:** redundant servers so if one fails it takes the like the database is mirrored and shared and it's all complex Genefis set all this up. It's all you know advanced penguin stuff. I don't know too much about it but yeah so that's all

**Dave Jones:** safe and by the way all the data safe all the backups. If for some reason the server the data center has actually lost the data on the drives in the server machines we do have full daily backups in two separate

**Dave Jones:** locations professional backup services and at most we might and Genefis said that And he did check and it was during the backup time is when the whole thing went down. So at worst we're going to lose like a day's worth

**Dave Jones:** of posts on the forum or something like that if my server is one of the ones affected. So there you go, which Murphy I said like yeah, it's going to be back. It's interesting that my cPanel email server is back but the others

**Dave Jones:** aren't but they are on different subnets. It could be fine. There's good chance it's fine but they're within different subnets in the data center. So yeah, so they brought one subnet back up and the other ones yeah, they're just

**Dave Jones:** separate. So we we just don't know. We just got to sit back and wait. They have said that they can't uh like give dedicated you know say oh yeah, this client's servers will be back up and running or whatever time. But

**Dave Jones:** anyway, they are past the time when it's supposed to come back up and the website hasn't come back up yet. So we're just going to have to wait. I don't know how long it's going to be. So yeah, that raises some interesting

**Dave Jones:** questions and we just put up a dedicated GNF just got this dedicated page hosted somewhere else and redirected the DNS's. So at least it shows you something and this you'll get the updates. There's no more update. I don't think he's updating

**Dave Jones:** anything in the background. No. No, we're just going to have to wait. He's monitoring it and it'll eventually come back online but that raises some interesting questions. I know there's going to be 1 million responses down below of how we're doing it all wrong

**Dave Jones:** and we should be using a cloud infrastructure. We should be using a more reliable data center and come on, right? Fire in a data center, fire in a generator, this could have happened to any data center really and I guess you can make an

**Dave Jones:** argument that it should be on you know Amazon cloud or whatever but hasn't that gone down in the past? I mean it's just like Murphy's going to get you, right? We've had no issues with this current host for I don't know, I mean five plus

**Dave Jones:** years at least, I think. We've been on these dedicated boxes at Gorilla servers and we haven't had an issue apart from like technical stuff, you know, like it's yeah, it's not like they were unreliable. It's just other things

**Dave Jones:** sort of have taken the website down here or there for like, you know, hours or a day or something like that. But yeah, that wasn't really the servers their actual fault. So Anyway, yeah, I don't know. Flame away down

**Dave Jones:** below. Yeah, got caught with the pants down. Data is safe, but yeah, it's been out for three, probably four, could be longer days that everything's down. At least my email is back and I guess that's a lesson that I need to set up some sort

**Dave Jones:** of redundant email exchange server thingamabob. I do actually use Gmail for all of my Gmail's actually my interface for email. So if you send a email to david@eevblog.com, then it actually just gets forwarded into Gmail and it actually replies. I've

**Dave Jones:** got like the reply to section in there is david@eevblog.com. So you don't know that I'm actually reading all my email on Gmail. So it's mostly there, but anyway, it is back up, but yeah, cuz a lot of stuff was tied to

**Dave Jones:** david@eevblog.com, yeah, I couldn't do a lot of stuff. Like I couldn't get like do email confirmations for doing various online activities and stuff like that. So yeah, it's a bit I I Gmail's gone down before. So you know,

**Dave Jones:** yeah, it's Murphy's going to get you at the worst possible time it will happen. So I don't know. Yeah, everyone will flame away down below. Hey dumbasses Dave for using that, you know, just hosting it on a couple of little

**Dave Jones:** dedicated boxes in the middle of Utah somewhere. No, there's there's reasons why we do that. A lot of people ask why we don't host in Europe or something like that. The majority of uh the viewers and the forum users and stuff like that are sort

**Dave Jones:** of like US based. US is probably the best place to actually host it in terms of like latency and, you know, all that uh sort of stuff. So, you know, yeah, it could be hosted here in Australia, could

**Dave Jones:** be hosted in the EU, could be hosted in, you know, some little I don't know, tin pot island somewhere um in the Pacific or something, but I Yeah. Anyway, there you go. Just wanted to give you an update. Uh so, I can't do

**Dave Jones:** the Keysight uh drawing, by the way, because the forum's not available. I You know, I don't have ability to uh run my wobbulator program and all that, but I'll probably do uh the drawings for the other uh ones, probably today. So,

**Dave Jones:** yeah, anyway, there you go. Just wanted to give you an update. It's down, could be down for a while. I got no idea um if we do have to if my servers were impacted by the uh water damage or

**Dave Jones:** whatever and the hard drives were lost, yeah, we might lose like, you know, half a day or up to a day at most worth of uh forum posts or something like that. So, if that does happen, um sorry. It's uh

**Dave Jones:** yeah, there's probably reasons I think we did look at doing like a live database backup somewhere. We already run a redundant system. It's just that the whole data center has gone down. So, it's like, you know, so we just do a

**Dave Jones:** daily uh backup. So, yeah, we don't have a third off-site redundant live redundant synced database server. It's all complicated when you try to write to multiple databases at multiple times. We've actually had uh technical issues regarding on on the forum regarding

**Dave Jones:** actual uh the use of having the multiple databases cuz you got the sync issues with the I don't know the exact um you know, technical stuff behind it, but, you know, it can get complicated when you try and share all of your databases,

**Dave Jones:** you know, they're trying to all sync and be live and stuff like that. We have image problems on the forums for attachments, they weren't linking correctly and stuff like that. So, if all your databases aren't synced, um I'm

**Dave Jones:** sure Jaden if can inform people down below if you got technical questions about the whole thing, but there you go. Yep, still down. I don't know when it'll be back. Sorry, got no idea. Um we'll just have to wait like everyone else,

**Dave Jones:** but my email is back, david@evblog.com, so that allows me to do some stuff. Uh yeah. Flame away. Catch you next time.
