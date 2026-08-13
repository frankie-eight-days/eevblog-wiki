---
video_id: 0U8he-5Bqtw
title: EEVblog #965 - The (Autodesk) Eagle Has Crashed
url: https://www.youtube.com/watch?v=0U8he-5Bqtw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 53, "4": 65, "5": 81, "6": 93, "7": 117, "8": 141, "9": 157, "10": 177, "11": 193, "12": 213, "13": 233, "14": 245, "15": 265, "16": 285, "17": 301, "18": 317, "19": 333, "20": 349, "21": 367, "22": 383, "23": 399, "24": 415, "25": 427, "26": 443, "27": 459, "28": 475, "29": 495, "30": 511, "31": 523, "32": 535, "33": 555, "34": 571, "35": 591, "36": 611, "37": 627, "38": 647, "39": 659, "40": 675, "41": 691, "42": 707, "43": 723, "44": 743, "45": 755, "46": 771, "47": 787, "48": 807, "49": 827, "50": 843, "51": 855, "52": 871, "53": 887, "54": 903, "55": 923, "56": 939, "57": 959, "58": 975, "59": 991, "60": 1007, "61": 1023}
---

**Dave Jones:** Hi. Do you remember the big news about six months ago in July 2016, when Autodesk bought CADsoft Eagle, the Eagle PCB CAD program. They actually bought it from Farnells, and Farnells bought it, bought CADsoft Eagle a couple of years before that. And everyone was kind of worried about what was going to happen and things like that.

**Dave Jones:** And Artifruit did an interview with the head of the new electronics division at Autodesk, who coincidentally is a former Altium colleague of mine, and it was all, you know, sounded pretty good, reassuring, things like that. But people were still getting a little bit

**Dave Jones:** of the heebie-jeebies, wondering about what the future would hold. Now, one of the major concerns was that they would switch over to a subscription based model and or cloud based software, because Eagle has always been a perpetual license, i.e. you buy it, one off

**Dave Jones:** cost, and they give you a license key code, you've got the executable, that's it. You don't need to ping back to the server or do anything else. You can still use it in 20, 30 years time if you've still got the hardware to run it.

**Dave Jones:** And of course, having the finely honed bullshit detector that I do, I read their complete non-answer to this question, called them out, and they said they should have just been honest and said it's going to cloud and subscription based. But sure enough, they

**Dave Jones:** responded and said, hey, Dave, it's not going subscription. So there, smiley, at this stage it isn't anywhere on my roadmap. Thought about it, decided against it. Can't say that we will never in the life of the product do that. No, of course not.

**Dave Jones:** That would be, at best, unfair at worst, dishonest. But I have so many things that are more pressing. So there you go. Very reassuring from just six months ago, it's not going to subscription based. Yeah. You guessed it. Yep. I called it. Or at least half of it.

**Dave Jones:** They went to subscription based pricing today. But they, hey, they haven't gone to cloud yet. But hey, I'm sure it's not Matt's fault. I mean, he works for Autodesk. Autodesk are huge big corporate, big company mentality, and I think the majority or most of their other products are also

**Dave Jones:** subscription type based services. So it was obvious they were going to do this. And it's so funny, just a few days ago on the EEVblog forum when they're talking about the new version of software that they're going to release, which they just did with this new license feature, you guys

**Dave Jones:** have no idea the awesome that is about to drop. Yeah, they dropped one, all right. It's a big stinky one. And, of course, changing owners seems to erase company memory very, very quickly. Here's a post from two years ago when they introduced version

**Dave Jones:** 7. And what do you know? They introduced a new license management feature. With the release of Eagle version 7, Catsoft Computer introduced a new license management system for Eagle in order to better protect our intellectual property and offer more flexibility and control to customers with multi-user licenses on a

**Dave Jones:** network. During the two weeks since the launch of Eagle version 7, we've been listening carefully to your constructive feedback and concerns about the new license management technology and have decided to remove the license management features. And with version 7.1 they caved in, listened to all the complaints

**Dave Jones:** and they dropped it. But, yeah, two years later, new managements come in and, yeah, they haven't learnt the same lesson, but maybe they're about to. And they're not beating around the bush either. Here's a post from George Garcia who works for Autodesk on the Autodesk

**Dave Jones:** forums, the Eagle forums. As it stands now, if you are not on subscription, you won't be able to use Eagle version 8 or any other version that may come out in the future. Behaves like an electric bill. If you don't pay the power, get shut off.

**Dave Jones:** At this point in time, and under this licensing mechanism, there is no solution for off-network machines, i.e. ones disconnected from the interwebs. There are other schemes at Autodesk that do allow off-network licenses, but Eagle currently does not have them. I'll be making our management aware of this full threat and see what improvements can be made.

**Dave Jones:** You think? Autodesk is full subscription going forward and this position is non-negotiable. I know that for a lot of you this is not good news. You think again? But there's not much that can be done about it. I'm truly sorry, guys. Yeah, I'm sorry too, George, but yep, I

**Dave Jones:** think you're going to get a fair bit of backlash from this one. And predictably, the campers aren't happy. They've been angry all day over it. Bye-bye, Eagle. Purge Eagle, install KiCad. And there's no shortage of people saying it's a complete showstopper for them.

**Dave Jones:** Eagle is dead to me. This is a no-go. This totally kills it for me. It just goes on and on. And there's even a user who's got 30 professional licenses and well, they're not going to upgrade. They're going to stick with version 7.

**Dave Jones:** And also, predictably, there are calls everywhere to switch to KiCad open-source software, all that sort of stuff. And somebody even came up with the excellent idea down the bottom there to give his entire team a 2K bonus to learn KiCad and make a tax-deductible

**Dave Jones:** donation to the free and open-source community. Love it. But there's some good news. The free version of Eagle, which of course made it the de facto industry standard in the open-source hardware community, is still free, which is great. In fact, they've increased the capabilities

**Dave Jones:** of the free version, I believe. But the downside? Yeah. You need an Autodesk account to download it or to upgrade a future version. D'oh! And of course, you might say, Dave, what's the big deal? You know, everyone, everything's going to this subscription model.

**Dave Jones:** Well, yeah, that's true. And I personally use a lot of subscription stuff, and I don't have too much of a problem with this personally. But the problem is, a lot of people do. Not only on principle, but for the work environment and their

**Dave Jones:** workflow. And Eagle recognized this a couple of years back when they admitted here, we understand that for a large group of customers, the current license management is causing limitations or simply not usable in your current workflow. I've worked at companies where you are cut off

**Dave Jones:** from the internet. You are firewalled from the internet. And if your software has to go back to the internet periodically to check your license, then it is simply an unusable product. Like, based on company procedures, you simply cannot use it. Or for those who want to, let's say, you want

**Dave Jones:** to, you know, you're going on a plane trip. You know, you're going, for me, it takes me 24 hours to get, 30 hours to get to the other side of the planet. You know, I want to be able to use something standalone. If you're sitting on a beach for a couple

**Dave Jones:** of weeks, if you've gone out back, whatever, you know, if you're disconnected or got unreliable internet, you don't want to be tied into it. But as a consolation, they have actually thought of this. Here's a post from Matt on the forum. If you lose your network connection, the software has a 14-day

**Dave Jones:** heartbeat that will enable you to work offline for 14 days. I know some folks would prefer to never have to connect, but this is required to support their monthly subscription model. And we'll get into the prices in a minute, because they've changed over and, well, they

**Dave Jones:** want people to be able to have the flexibility to rent monthly. And fair enough. But that's then now locked them into this 14-day online subscription heartbeat requirement. And it's just going to be a complete showstopper for people, either due to serious requirements or just on principle.

**Dave Jones:** The biggest problem with not having a perpetual license option, a standalone license option, is you don't have the ability to, when you make your CAD files for a particular product, then just like zip and archive the software, the license keys, everything. A lot of companies and people

**Dave Jones:** take complete snapshots of their hard drive and back those up so that they can instantly come back in 10, 15 years time when the customer has to upgrade the product or the customer needs some support or something like that. You've got to change it and you can just get back up and running with the

**Dave Jones:** thing. But now with this online licensing, you don't have that standalone license key that you can then zip up and archive and then just get up and running later. If you come back in 10 years time, hey, the company may not be there, but hey, it's Autodesk.

**Dave Jones:** Okay, the product may not be there anymore, but hey, okay, it's Autodesk. Or your license for that particular version that you have may not exist, but hey, it's Autodesk. Or you might be able to buy the latest license for the latest version, but then you've got problems with that.

**Dave Jones:** Your old files may not be compatible. It could be some bug, quirk, you can't load it in. That's why people take snapshots of their entire development systems. Anyone who's really serious about long-term maintainability, either just because or because you have contractual requirements. I've worked in large companies where we're

**Dave Jones:** contractually obligated to provide support for 10 or 20 years or whatever, and you can't do that with this type of subscription model CAD tool. And well, that's the thing. These companies just don't get it. CAD software is not like your regular consumer software.

**Dave Jones:** It's almost a religion. I know it is like that with, you know, some other consumer type software, but this is a tool for professionals that invest their entire career sometimes learning how to use this tool, and when you try and change it on them, they don't change the way it works.

**Dave Jones:** Operates the entire subscription model. You turn it on its head and you're going to get this backlash. It's just people will just get angry on principle, let alone due to practical requirements. They really are going to be in for a hard time here, and they learned this two years ago

**Dave Jones:** and they're probably going to learn the exact same lesson yet again. Now, of course, Eagle aren't the only ones to change things up like this. Outium, for example, are famous, infamous, for turning the world of electronics design upside down and changing the way they do things.

**Dave Jones:** Their models, their pricing, their licensing, the features they're going to focus on, everything else. And they specialized in shooting themselves in the foot at every available opportunity. But hey, the customers stuck around because A, they're loyal, they're tied into the software, and there wasn't really any serious competition

**Dave Jones:** in the sort of price point that Outium were operating at. But this is different for Eagle. Just look at all the people saying, well, I'm going to go to KiCad, I'm going to go to DipTrace, I'm going to go to, you know, insert one here

**Dave Jones:** the new Circuit Studio has a, Outium have a standalone license, for example. Eagle just aren't in the same position as, say, someone like Outium was when they make these big changes. There are so many other options. Most of their, majority of their business

**Dave Jones:** is going to be that, you know, small hobbyist, hacker, maker you know, one man band, you know, five person company or whatever. They have doing smallish type stuff. No real serious professional companies out there, you know, using Eagle. You don't see it in the job requirements

**Dave Jones:** of professional companies and stuff like that. These are people who can switch much easier. And this backlash is real. Like they need to take this serious. They may not survive well, they'll survive as a company, but they may not survive this intact in terms of their reputation.

**Dave Jones:** They're going to lose a lot of business over this. And there's been some talk about how it's actually can be potentially more expensive now as well. And that's a yes and a no. Let's take a look at the new pricing model. So now they've got two versions instead of three.

**Dave Jones:** Eagle Standard and Eagle Premium. Eagle Standard, $15 if you just want the monthly thing or $100 a year if you want to go for the yearly option. And the Eagle Premium is $65 a month or $500 a year. So if we take a look at their original prices on the left hand side

**Dave Jones:** here, you can see that they actually have three standards. Eagle Light, Eagle Standard and Eagle Professional. They've gotten rid of Eagle Light and they've only got the Eagle Standard now. But Eagle Standard has changed. You can see how it used to have six layers

**Dave Jones:** there with 160x100mm routing area. Well now it's only two layers for that $10 a month or $100 a year. So that has changed fairly significantly. So if you just want to jump up to like a four layer board, they don't really have that option anymore.

**Dave Jones:** You've got to go up to the Premium. So in that sort of case yes, it's more expensive if you had that limited routing size and the four layer or six layer requirement. But I've always thought that this was really completely stupid. I mean, why would you pay

**Dave Jones:** $500 or $820 if you want the auto router for a lousy 160x100mm routing area? It is just ridiculous. If you want a single layer board with one part on it that's 161mm you've got to jump up to the before. You had to jump up to

**Dave Jones:** the $1100 model. But now it's actually cheaper to go pro on the Eagle Premium here. It's only now $500 a year. So it's more than half. It used to be $1145 and now it's only $500. So I think overall more people are going to win out on this pricing

**Dave Jones:** structure. So I don't quite know why there's a bit of an uproar over the pricing here. Maybe if you're stuck in that mid airy-fairy area, yeah, okay, fair enough. But no, I think it's much better now. But the good news is that you can now actually

**Dave Jones:** just rent it for a month. If you want that 16 layers unlimited board area size, rent it for a month and Bob's your uncle, right? You can, I guess, you can always go back to your previous subscription, you know, your lower subscription model.

**Dave Jones:** And Altium were going to do this with Circuit Maker originally. And I thought, I actually saw this before they released, and I thought that was the subscription, like the monthly subscription, being able to rent certain features, that's actually quite valuable. So I think that's

**Dave Jones:** kind of a good move, but of course that's pushed them into that license checking online requirement. You can't have that standalone license. And that's the big bugbear here, is that most people are up in an uproar because they just don't have that standalone

**Dave Jones:** perpetual license. That's the real killer here. But hey, also on the positive side, Autodesk takeover has meant that they're actually finally adding all these new features. I mean, they got BGA fan out, and they're adding different new routing engines and all sorts of stuff that they're adding in.

**Dave Jones:** So that's, you know, that's terrific. But yeah, I can understand why there's a big uproar over this thing. And to completely flip your pricing model, especially so soon, like six months or less after buying the company, they must have made this decision, you know, a month or two back, only to

**Dave Jones:** be able to roll it out now. And they flipped on that. They did a complete U-turn on that pretty darn quickly. You know, they were promised basically back at the start that, no, we've investigated, no, we're not going to the subscription model. So you think, okay, maybe a couple of years

**Dave Jones:** down the track they might change their mind. But no, flip-flop, after less than half a year. Ridiculous. Anyway, I can understand the uproar, and they need to fix this. It's just ridiculous. They need to have that stand-alone license option. Otherwise, it's, as I said before, it's easy, relatively easy for people

**Dave Jones:** to leave from Eagle, because it doesn't have that, you know, locked-in structure that, you know, your other higher-end packages have. There's too many other options. So, yeah, I don't like it at all. Speaking of options, if you did want to switch over to KiCad, then my

**Dave Jones:** esteemed Ampower co-host, Chris Gammel, who runs Contextual Electronics, said he would kill a puppy if I didn't recommend Contextual Electronics over here in his Get Into Blinky program, where you can learn KiCad and all that sort of stuff. So, yeah, we don't want to kill a puppy.

**Dave Jones:** So, yeah. Check it out. So, yep, Autodesk and Eagle, they've really opened a big can of worms here, and they're copping a lot of flack over it. And I think, you know, rightly so. I think they need to sort this mess out, and they recognized it two years ago, and they're gonna

**Dave Jones:** look like they're making the same mistake again. They don't quite understand the intricacies of the CAD market and the user base. But anyway, let us know what you think. If you've got opinions on this, would you dare touch subscription CAD software like this?

**Dave Jones:** And if so, tell us why. Is it principle or do you have, you know, some requirement that, you know, really makes this a showstopper for you? Leave it in the YouTube comments or on the eeveelook forum down below. Catch you next time.
