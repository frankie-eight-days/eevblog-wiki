---
video_id: v1BF9_a0_tA
title: EEVblog 1722 - Manufacturing Hardware War STORY
url: https://www.youtube.com/watch?v=v1BF9_a0_tA
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 29, "3": 42, "4": 56, "5": 71, "6": 85, "7": 99, "8": 113, "9": 127, "10": 141, "11": 156, "12": 169, "13": 182, "14": 191, "15": 204, "16": 219, "17": 232, "18": 244, "19": 256, "20": 266, "21": 281, "22": 298, "23": 310, "24": 321, "25": 334, "26": 350, "27": 364, "28": 377, "29": 390, "30": 403, "31": 416, "32": 429, "33": 445, "34": 460, "35": 473, "36": 486, "37": 500, "38": 511, "39": 524, "40": 536, "41": 551, "42": 564, "43": 578, "44": 593, "45": 606, "46": 620, "47": 635, "48": 647, "49": 658, "50": 669, "51": 682, "52": 695, "53": 710, "54": 723, "55": 738, "56": 751, "57": 761, "58": 771, "59": 783, "60": 796, "61": 810, "62": 824, "63": 838, "64": 849, "65": 868, "66": 882, "67": 895, "68": 911, "69": 926, "70": 940, "71": 952, "72": 970, "73": 982, "74": 996, "75": 1011, "76": 1024, "77": 1036, "78": 1047, "79": 1059, "80": 1071, "81": 1084, "82": 1098, "83": 1112, "84": 1127, "85": 1141, "86": 1159, "87": 1175, "88": 1189, "89": 1203, "90": 1217, "91": 1229, "92": 1240}
---

**Dave Jones:** Hi, it's industry story time because last month I was invited to give a uh short talk at the uh Sydney hardware uh meetup. It's the ASUS hardware meetup. It's on semi-regularly at different locations. It was really cool and

**Dave Jones:** they're up to their eighth uh Sydney hardware meetup. So, highly recommend you go along if you're in Sydney. It's really cool. Anyway, I'll link it in uh down below. So I was invited uh to give a just a short uh talk and just share an

**Dave Jones:** industry story at that event. Uh unfortunately it wasn't recorded at all so you had to be there but I've got the slides. Um there's not many of them but I thought I'd just go through and um tell that story again. The theme of it

**Dave Jones:** was hardware war stories. And of course the old adage is true hardware is hard. And me being an electronics design engineer, I used to work in the industry for a long time, I'd have lots of hardware, electronics, hardware war

**Dave Jones:** stories, but I thought I'd do something different and share um something that's not quite electronics, but still there's a good lesson in there. So, let's get into it. This one is how a rubber band cost a company millions of dollars and a

**Dave Jones:** lot of their uh goodwill reputation as well. So, let's get into it. I used to work at a company uh that developed underwater seismic uh exploration equipment for oil surveying. And this is basically um how it works. Here you've

**Dave Jones:** got a massive oil survey ship. We'll see that in a minute. Um and they tow these what are called towed array streamers behind them. And these can be five 10 kilometers long streamers, massive array. I'll show you that in a minute.

**Dave Jones:** And they contain hydrophones which are underwater microphones basically. And these thousands of these hydrophones being towed behind the ship and the ship just does a pattern in the ocean and like an and it maps a certain area and

**Dave Jones:** they've got a um shockwave source which are big like ram jets that actually generate a big pulse of energy into the low frequency energy into the water and it bounces down and it bounces through that sound energy bounces through all

**Dave Jones:** the you know the strata rock layers and everything. I'm not a geologist. And then based on what uh the sound energy actually um hits it actually uh reflects back and the reflections are picked up by the hydrophones and uh all this data

**Dave Jones:** is correlated, sampled in real time and then analyzed by supercomputers. Um oil surveying is one of the original uses for supercomputers to actually find oil. It's not quite an exact science. you got to hold your tongue at the right angle

**Dave Jones:** and you interpret these uh displays down here. But you know, you can get a reasonable confidence that uh you know there's oil in a certain location and that's where you drill your oil well through to uh find water or also you can

**Dave Jones:** do it for when an existing oil well is depleted. For example, you can go in and with more modern technology and more modern sensors and everything else, you can and more modern data processing, you can reanalyze old oil wells and go, "No,

**Dave Jones:** we think there's actually more down there. Um, we thought it was, you know, all dried up, but no, we can we can suck some more money out of that." By the way, back in the old days, um, they

**Dave Jones:** didn't have these uh big um air ramjets. They actually used to toss dynamite off the back end of the boat and that would generate the uh sound shock. But yeah, the whales just go and they still go at

**Dave Jones:** the um the sound of the air guns here. So yeah, it's not good. Not to mention the dolphins. So these ships are absolutely massive. They're like in fact this is um I believe is might currently still be. This is the ramiform Titan.

**Dave Jones:** This is a seismic survey vessel. And no, they haven't photoshopped off the back of the ship there. It's actually Hey, that's actually what it looks like. It's massive. This is the widest ship in the world. And they're used um they just as

**Dave Jones:** I said they just troll around the ocean in these zigzag patterns actually looking uh for oil. And these are absolutely massive. And here's a backend shot of it. And you can see that they have these cables coming out and these

**Dave Jones:** are the toad array streamers they're called. Back in the old days, there used to actually be um these streamers used to, you know, they're about yay diameter and they used to be uh filled with oil and the uh hydrophones would be sitting

**Dave Jones:** inside the oil, but they weren't very environmentally friendly because if you got any like tears or rips in them, which was uh quite common, then the oil would just leak into the ocean. It wasn't that great. So, they developed

**Dave Jones:** solid seismic streamers, which were basically just buoyant uh flotation material with a big core of cables going through them. So there was little to no oil. There's some oil in them as I'll talk about in a minute. But yeah, these

**Dave Jones:** ships are massive and they can tow up to some of the modern ships uh can tow up to 24 streamers wide. So 24 different arrays of streamers at 12 kilometers length each. And uh they actually uh branch out further apart than this.

**Dave Jones:** They've got like uh like guide veins out there that can actually, you know, pull the uh cables apart and then they actually sit, you know, just below the surface so that the waves aren't slapping on them because that would

**Dave Jones:** generate too much noise. So they're semi-boyant so that they actually just uh float below the surface so that they can use them in different uh sea states and they've got little guide veins on them underwater to sort of you know keep

**Dave Jones:** them at um a certain depth uh just below the water and then they'll have the big um ram air jets um off to the side as well generating the impulses. But these ships are absolutely massive. So on a

**Dave Jones:** large massive array you could have up to 10,000 different hydrophones in these. And yeah, that's a lot of uh real-time processing. And by the way, the uh frequency range we're talking about here in the seismic industry, 200 hertz was

**Dave Jones:** considered high frequency. So yeah, this was like DC to like a couple hundred hertz at most. So they're on the back deck of the ships like this in these big giant uh lengths. We used to manufacture these in both 100 meter lengths and 150

**Dave Jones:** m lengths. So, our our factory uh here in Sydney was like 180 m long, and we had gigantic benches where they'd actually uh manufacture these things. And you can see, you're probably going to have a hard time seeing the uh

**Dave Jones:** hydrophone modules, but they're like every couple of meters uh spaced here along like inside the cable. So, as I said, it contains a uh a core with all the cables. So, they put high voltage in at the boats because by the time it gets

**Dave Jones:** 10 km down the other end, they take a reasonable amount of power. You've got some of the lowest noise, highest end 24-bit analog digital uh converters optimized for that DC to couple hundred Hz bandwidth. There are analog devices

**Dave Jones:** and uh Cirrus Logic were two of the main uh providers back then if you're curious. You can probably go still find the uh data sheets for those. But um yeah, really ultra low noise um analog 24-bit ADCs in these. And these outer

**Dave Jones:** twisted pairs in here, they would actually connect to the hydrophones. The inner would be for power. some of the cables that we had fiber optics through them as well. And then there's Kevlar strengthening members and stuff like that in there. Um, and then they'd have

**Dave Jones:** the buoyant flotation material and a big uh poly put the kettle on um, you know, urethane kind of like outer protective uh, casing on them. Get on with the actual story, Dave. Okay. Well, here we go. So, these hydrophones are actually

**Dave Jones:** called benders because they're are like basically a uh a two plate curacitor. They're like a ceramic capacitor that um and they sort of bend when little, you know, you can't see it, but they physically uh bend when the sound

**Dave Jones:** pressure um hits them. So, they call them benders in the industry, but they're basically um you know, specialized ceramic capacitors. We used to have our own manufacturing facility to actually make these. And they sit in an oil filled packet. You know how I

**Dave Jones:** said they got rid of the oil filled streamers? That was all the way through. Um, now they're just in a module which we called a SIM module. But now there's only the oil um inside just that little uh hydrophone pocket like that just to

**Dave Jones:** couple the um sound energy from the outside into the hydrophone on the inside. You've got to have like an oil medium and that they used um isopar M. Um for the you chemists out there you can go look up the properties of isopar

**Dave Jones:** M. Please excuse the crudity of the model. Didn't have time to build it, scale or to paint it. I did find an original photo of one of the hydrophones. So, this is actually what um one of these modules actually look

**Dave Jones:** like. And you can see that they contain uh two metal um outer shells. So, two half outer shells like this. So, I've drawn those there, those metal outer shells. It's not the scale here, but um yeah. So, there's metal outer shells

**Dave Jones:** that you put on which would physically protect uh the hydrophones. And then there'd be two hydrophones, one top, one bottom, um, either side in here, and they'd just be in parallel. And then you can see that there's an outer, uh,

**Dave Jones:** sheath here, which is then glued on there, and it's, uh, and all that is filled up with oil. So, as I said, that's isopar Material um, inside there. So, yeah, that's basically we've just got a little oil filled pouch in there

**Dave Jones:** um, with our ceramic hydrophones um, inside and they got these little ports. You can see that tiny little port just in there where my cursor is. And that's where the uh pressure of the oil would go through to the hydrophone. You didn't

**Dave Jones:** need much. You only needed a tiny little uh hole in there for the uh pressure to get through, right? Cuz we're talking about like really low frequency um stuff here. Anyway, on to the actual war story. Okay, this was the late 1990s, I

**Dave Jones:** think it was, and there was big inrush of uh feds at the time to help improve manufacturing processes. there was you know lean manufacturing six sigma and kasin and continuous improvement which I've put up the top there so you know

**Dave Jones:** all and the employees would be sent on these courses about all these latest things about how to improve your manufacturing processes and ek out more profit and better uh performance and all that uh sort of thing and as it happens

**Dave Jones:** yeah one of these uh continuous improvement uh processes right we actually you know you look at all sorts of issues that you're having in in production. It can be electronics uh manufacturing. It can be like other related hardware like this. It can be

**Dave Jones:** manufacturing automotive. Can be manufacturing cars or widgets or whatever it is. It doesn't matter. You know, manufacturing is kind of like manufacturing. You have um similar sort of issues regardless of what uh you're actually making. So we were tasked to,

**Dave Jones:** you know, collate and look at all the issues we were having in production and see if we could find ways to improve, refine the manufacturing process and and things like that. And uh one of the big things with manufacturing this module

**Dave Jones:** here, you can see these wires coming out, but there's also wires inside and we've got these metal shells. So you got to sort of like shove the wires, you know, you push the hydrophone in. It's on little um O-ring uh mounts. you push

**Dave Jones:** it in and there's wires in there and then you've got to like tuck the wires away before you put the metal shells on. And we had sort of you know a small but significant um you know failure rate

**Dave Jones:** with these things by uh the wires that get pinched by the metal shells uh for example. And that that wasn't you know really optimal. We didn't want that to happen. So, um, somebody came up with the idea that, oh, we would actually,

**Dave Jones:** uh, use rubber bands to tie down the, you know, just to hold down the, uh, wires, just thin little, uh, rubber bands to hold down the wires in there before you put the metal shells on. And bingo, solved the problem of, you know,

**Dave Jones:** we basically eliminate and that and it worked. Spoiler alert, it worked. And we eliminated the problem of, you know, the wires getting pinched in in production. So, we went from a significant measurable um you know issue down to

**Dave Jones:** zero. And then we tested the hell out of this thing, right? Um because yeah, like when you introduce something a step into your manufacturing process, you really want to thoroughly test it to make sure that it's not a problem. And we

**Dave Jones:** thoroughly tested the hell out of this these things. The rubber bands made absolutely no difference at all. and all the engineering principles uh behind the acoustics of how all this worked. You know, it was basically guaranteed that these rubber bands couldn't cause any

**Dave Jones:** acoustic issues whatsoever. So, um yeah, we started to manufacture these. Everyone got a pat on the back and you know, Bob's your uncle, right? So, we're manufacturing these uh cables and we send them out and of course we're here

**Dave Jones:** in Australia, so they've got to be um shipped and they've got to be put onto these uh giant reels. They're smaller ones than these, but they get to the ship and then they join them and they put them on larger reels on the ship.

**Dave Jones:** But, you know, reels bigger than um I am um these gigantic reels and they got to be put on ships and they've got to be um sailed. In this particular case, it was to the North Atlantic. So, they got to

**Dave Jones:** be sailed to the, you know, the other side of the world basically. You know, it takes months to sort of get them out there, get them onto the ships and then uh actually deploy them on the ships. So, it was months and months passed by

**Dave Jones:** and we're still manufacturing all of these cables, right? Manufacturing all of these things, thousands of these things. They're very expensive cables. And what do you know? We started getting reports back from the customer once they got these on the boats, deployed them

**Dave Jones:** out on the ocean. And we're starting recording with these things and they're going, "Uh, something's not right." Like, the levels are down and like a lot of these things appear to be death. Like, they're just not working. whether

**Dave Jones:** the hydrophones broken or something like that. And we got started getting all these reports and because a lot of these are in parallel whether there was multiple strings in like a 150 m long uh streamer but um there were more

**Dave Jones:** hydrophones than there were individual strings which went to individual analog to digital converters. So, a lot of these hydrophones were in parallel and you know, it's really hard to tell like if there's one faulty um SIM module like

**Dave Jones:** this and and really one just one faulty SIM module doesn't you know it's neither here nor there, but they could start to see like an increase in the noise levels or I'm not sure of the exact mechanism um that they were able to detect this,

**Dave Jones:** but the performance wasn't there. Something had changed and we're racking our brains going it can't be the rubber bands. It's it's it's physically acoustically impossible. And then the penny dropped. Are there any chemists out there? Ah, you might be going, "Oh,

**Dave Jones:** I can see it." Leave it in the comments down below of what you think that the problem is. And it was certainly, of course, the rubber band that caused the problem. But we couldn't figure out how because we weren't seeing it in any of

**Dave Jones:** our um manufacturing back at home. But once they got on the boats out there, um, they were starting to see them. So, what did the issue turned out to be? Well, rubber bands. They contain rubber and I don't know, do they contain

**Dave Jones:** anything else? I'm not sure. Construction of rubber bands. Anyway, um, you know how I said they were filled with this isopm oil material? Well, if you immerse a rubber band in this isoparm oil for long enough and certain

**Dave Jones:** types of rubber bands, they will eventually absorb that oil and swell up. So, these rubber bands were actually swelling up and blocking the ports here. Sometimes it' be a port on one side, sometimes it'll be both ports and things

**Dave Jones:** like that. And this was happening um to a whole bunch of these streamers out in the field. But it would take months for that oil to actually seep in to the rubber bands and swell them up enough. And it depended on uh you know pot luck

**Dave Jones:** of where the operator cuz there was variability in where they put the uh rubber bands. You know, were they closer to the port over here? And you know, there wasn't much room inside uh this module. they could swell up in various

**Dave Jones:** ways and either block one or both ports causing um that hydrophone to be deaf. So yeah, oops. So once we realize that, that's obviously something we could uh fix immediately right on the production line then and there. I can't remember if we

**Dave Jones:** got rid of the rubber bands or changed the type or whatever, but you know, it it was basically an easy fix once we figure out that these rubber bands would eventually swell up over the months that it took to actually get them deployed to

**Dave Jones:** the customer out out on the back end of the boat. Um, but in the meantime, we had manufactured thousands of these streamers and that's were in various stages of being shipped and deployed and everything else. And as I said, these

**Dave Jones:** are like encased in this giganticund, you know, 50 meter long polyurethane jacket. There's no joins in them. They're they're like shoved. Like once we've manufactured these, then we had a giant machine like a you like big sausage machine to feed these um this

**Dave Jones:** big um 150 m long thing right through. So we had theseund, you know, big thick jackets like this. So, it was actually a two-step process to actually repairing these things in the field because having them shipped back to us, you know,

**Dave Jones:** shipping half a product this size halfway around the planet is just, you know, no, these had to be fixed on the back end of the boat. So, we had to send people out there to actually fix these things and and the um process was uh

**Dave Jones:** twofold. You know, how I said they're all in parallel and we couldn't quite figure out which one. Well, we had to uh develop test jigs that we would clamp over like with speakers, acoustic uh clamps that we would uh clamp over these

**Dave Jones:** things and then we'd individually excite each hydrophone and we can manually uh measure, you know, whether or not it was a problem coming out the uh back end. And then if that one proved to be faulty, then we had to come up with a

**Dave Jones:** process that was cutting open the jacket, peeling it back like this, and then physically, you know, taking off those shells and actually um, you know, just getting rid of the the rubber band, putting them back on and, you know,

**Dave Jones:** peeling the uh, big thick polyurethane jacket back on and then welding them back on and, you know, heat uh, welding them uh, back on. So we had to have these giant mold heaters that would uh you know so we had to have all these

**Dave Jones:** repair processes and this had to be done on the back deck of a giant boat out in the middle of the North Atlantic in various sea states up to seaate four or five or whatever and like yeah it it was

**Dave Jones:** not pretty um and it was a very expensive process and yeah it it cost millions of dollars and yeah the companies like cpped a bad reputation uh for these cables but they eventually fixed and everything was hunky dory. But

**Dave Jones:** um yeah, just be aware that making like one small change like that that you test thoroughly and by you know the laws of acoustics, this shouldn't not have caused a problem. And it didn't. But we didn't take into account the long-term

**Dave Jones:** effects of this uh and the rubber band would soak up the oil and block these ports because we just didn't test long enough. Um and maybe if we tested long enough we could have detected it in house but um then before they actually

**Dave Jones:** shipped out but um no that wasn't the case. So we were stuck with shipping you know repairing like thousands of these um hydrophones out in the um field. So yeah, very expensive oopsie mistake for just you know tweaking trying to tweak

**Dave Jones:** our manufacturing process even though we put best effort into uh you know determining that it wouldn't cause a problem it did and you know sometimes Murphy you're going to come a gutsa and um these sorts of things happen. So

**Dave Jones:** there you go. That's a very long short story of u not electronics hardware but physical manufacturing that uh you can really come a guts. So yeah just be aware of these you know continuous improvement lean manufacturing. So, next

**Dave Jones:** time you make a change to your production process, regardless of what it is, think about um any like long-term consequences. And you know, if if we had these sticking around for, you know, 2 or 3 months, maybe we would have um seen

**Dave Jones:** this problem in house before we shipped them. But, you know, that's a long time in the manufacturing uh business. So, and sometimes, no matter how careful you are, you're going to come a gutsa with something like this. And yeah,

**Dave Jones:** unfortunately just very difficult and expensive to repair, but it was doable in the end, but there you go. I hope you uh learned a lesson there about manufacturing. So, I hope you learned something from that. And if you did,

**Dave Jones:** give it a big thumbs up. And as always, discuss down below in the comments or over on the EV blog forum thread. And I'd love to hear both electronics war stories and which I've got a ton of um

**Dave Jones:** and also like things that aren't necessarily electronics related like this that you know a simple change can really cause you to come a gutsa. It's fascinating, huh? Catch you next time.
