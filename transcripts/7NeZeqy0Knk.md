---
video_id: 7NeZeqy0Knk
title: EEVblog 1697 - What's Up With Different Brand Op-Amps?
url: https://www.youtube.com/watch?v=7NeZeqy0Knk
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 29, "3": 34, "4": 49, "5": 57, "6": 73, "7": 85, "8": 93, "9": 103, "10": 120, "11": 130, "12": 144, "13": 155, "14": 163, "15": 176, "16": 200, "17": 206, "18": 217, "19": 226, "20": 237, "21": 245, "22": 255, "23": 270, "24": 278, "25": 290, "26": 298, "27": 314, "28": 328, "29": 348, "30": 358, "31": 373, "32": 381, "33": 394, "34": 407, "35": 419, "36": 435, "37": 459, "38": 472, "39": 488, "40": 496, "41": 505, "42": 517, "43": 537, "44": 550, "45": 559, "46": 569, "47": 580, "48": 588, "49": 610, "50": 620, "51": 633, "52": 650, "53": 663, "54": 678, "55": 690, "56": 699, "57": 709, "58": 718, "59": 735, "60": 745, "61": 768, "62": 780, "63": 790, "64": 810, "65": 823, "66": 836, "67": 846, "68": 858, "69": 874, "70": 884, "71": 901, "72": 910, "73": 918, "74": 933, "75": 942, "76": 957, "77": 969, "78": 983, "79": 992, "80": 1001, "81": 1011, "82": 1030, "83": 1038, "84": 1056, "85": 1069, "86": 1081, "87": 1091, "88": 1105}
---

**Dave Jones:** Hi, it's forum question time and I thought this was interesting enough to do a dedicated detailed video on here. And thank you very much Gamelot on the EV blog forum super contributor.

**Dave Jones:** It all happens over on the EV blog forum. If you're not a member, um it relates to my latest review and teardown video of the Uni-T UDP6731 power supply and I did a follow-up video on the EV blog two channel about that as well.

**Dave Jones:** Like have I been done it cuz they sent me a new one. Anyway, if you haven't seen it, I'll link it in. So Gamelot's referring to the teardown photos.

**Dave Jones:** We'll take a look at it in a minute because I had an issue with the this power supply just in one particular listener mode and they've fixed that and we're kind of still left wondering well, what was the actual fault that actually caused that cuz Uni-T didn't know.

**Dave Jones:** They just said it was faulty and they sent me another one and sure enough it works. Anyway, I'll link in that second channel video. So Gamelot's question is in reference to that, I believe.

**Dave Jones:** Why do they use two different types of LM358 from different manufacturers on the same board? Actually, great question. So this is my detailed answer to it. So let's take a look at the board inside in question.

**Dave Jones:** This is the controller board inside just of on its own board here vertical riser board. There's several reasons why you might do that because the main board looks like this and it's just like one big thing like that.

**Dave Jones:** And if you try and put a like this is all in the bottom side the through hole hole side on the other side has like all the big through hole components on it.

**Dave Jones:** The big pass transistors, the heat sinks and big capacitors and everything else. So you know, to try and cram all the control circuitry on the bottom side, you've got this double sided load thing.

**Dave Jones:** It's not the best idea. So you actually find this a very common inside switch mode power supplies, lab supplies like this one or commercial uh, ones or whatever. Um, I've done tons of tear downs, and you've no doubt seen these little vertical riser boards.

**Dave Jones:** And the reason for it is because you can put all of the, uh, control circuits, as you can see, like there's like different op amps here, here, here, here, and there.

**Dave Jones:** They're near identical, but there's some differences, uh, between them. That's an op07 precision op amp there. And then they've got the switching, uh, controller over here. And the reason you'd put these on one board is not only to free up, um, space from like the main board over here.

**Dave Jones:** It it just means that you can actually test this board separately. So, you can design automated test jigs where you just plug this in, because it's just got the pin header, um, on the bottom here and over here, I think.

**Dave Jones:** Uh, where you can just plug it in, and, you know, you can do all your detailed testing, and a pass fail, and stuff like that. And that's what this little mark here, somebody's marked that with a pen like that.

**Dave Jones:** And that's just to indicate that this one has, uh, passed testing. And for something like a power supply like this, and, you know, any sort of switching supply, you know, all the all the magic sort of like happening on this board.

**Dave Jones:** It's also in software as well. But all the analog magic, right, all the control loops and everything, are basically happening on, uh, this board. So, if anything goes wrong with that, and you want to like, tweak it a bit later, you want to modify the board a bit, it's just easier to modify a smaller plug-in board like this than it is to, uh, like just re-spin the entire huge board

**Dave Jones:** like this. So, all of your stuff that you think might change, or you might want to tweak, you might want to test separately, you put it on a daughter board like that.

**Dave Jones:** Anyway, that's just a little aside on why they did that. Anyway, the question asked, why are they different brands of LM358 chip? And you can see LM358 there. That's an ST.

**Dave Jones:** You can see, right? One of the big huge names. That's an ST jobby, right? One of the big reputable manufacturers. Got another one down here. They're from an identical batch.

**Dave Jones:** M, uh, what is it what is that? MZ207. So, that'll would like a batch code, thing, that you know, whatever that means. Every manufacturer has a different way of doing their batch code.

**Dave Jones:** You have to read the data sheet or sometimes it's not even in the data sheet. You get what you get and you don't get upset. But yeah, they're basically from they would be from the same reel.

**Dave Jones:** They'd be on the same physical reel that you put on the pick and place machine. But look, this is also an LM358. It's from a company called Arts Chip.

**Dave Jones:** Have you heard of Arts Chip before? PROBABLY NOT. RIGHT? Because the LM358 is what's called a jelly bean component. So I've done videos on jelly bean op amps. And look in the thumbnail, LM358.

**Dave Jones:** Because it is one of the jelly bean op amps. Anyway, great series if you haven't seen it. If you want me to continue this series, I've done regulators, bipolar transistors, comparators, and op amps.

**Dave Jones:** So let me know if you want that to continue. Anyway, I'll link in that video if you haven't seen it. A jelly bean component is basically one that is has been around forever.

**Dave Jones:** I'm talking 40, 50 years, right? Like the LM358 has. I don't know when it was introduced offhand, but it's probably in that video. Right? It's been around for a long time.

**Dave Jones:** It's available everywhere. It is cheap as chips. Pun intended, I'm here a week. And it's available from dozens and dozens of different manufacturers. How many manufacturers? Let's go over to Digi-Key and search for LM 358.

**Dave Jones:** And look, all these different manufacturers. 3PE, Diodes Incorporated, Evo, never heard of them. You know, all your old school ones, Fairchild, NatSemi, On Semi. And then there's Road, and then there's a Shenzhen one, ST Micro of course, TI, UMW, never heard of them.

**Dave Jones:** Teijing. And then if you go over to a Asian, you know, the Asian Asian equivalent to these catalog supplies, LCSC. Then you got 3PE, Cosign, Chip Nobo, Diodes, so that'd be Diodes Inc, Doway, Elect Super, Fushan, Blue Rocket Electric, Co GA, right?

**Dave Jones:** All of these different manufacturers, look at them, right? And then you're you know, mixing your STs and your TIs, your big Western names that you're familiar with and your on semis and whatnot.

**Dave Jones:** But they're available from dozens and dozens and different Even this LCSC doesn't list this Arts chip. So you go over to the Arts chip website and sure enough, they make like tons of different analoggy stuff, right?

**Dave Jones:** And these are the op amps they make and sure enough the LM358 is one of them and we can pull up a data sheet on that and we can pull up an ST data sheet here.

**Dave Jones:** But basically, what that jelly bean component means is that you select that component cuz you just want a very basic op amp function. So what choosing a jelly bean component for your design means is that you're basically don't care too much what the specs are.

**Dave Jones:** You're choosing that jelly bean part because it's available from dozens of different manufacturers. So when you go to manufacture your product, oh, you're not hit with some supply chain crisis where you can't get it because you're fixed locked into one manufacturer.

**Dave Jones:** You pick it because A, there's tons of different manufacturers available, so you're guaranteed to get this part forever and also longevity of production. They've been selling it for 50 years, they're not going to suddenly stop, right?

**Dave Jones:** And then the next one is you don't really care too much about the specs. You don't need high bandwidth, you don't need high precision and low offset and low noise and you know, all the other bells and whistles because there's literally what, thousands of different types of op amps out there to pick from.

**Dave Jones:** The reason you're picking an LM358 is just cuz you need a jelly bean op amp to do a basic op amp function and nothing more. So pretty much, if you're doing a design and you care which brand LM358 or which brand jelly bean component, be it a 75 7805 voltage regulator or a comparator, you know, LM339 comparator or something like that.

**Dave Jones:** If you care about the exact brand that goes in there, because one is slightly different like lower offset voltage than the other, then you're doing your design wrong. The reason you pick these jelly bean components is because you shouldn't care.

**Dave Jones:** Your design shouldn't care. So, I am not the least bit surprised to see different brand LM358s on there because it shouldn't matter a rat's ass whether or not you use an Alt's chip or an ST or any other one hung low brand component on there.

**Dave Jones:** Doesn't matter at all. And if you're serious about manufacturing your product, you're going to have a detailed bill of materials. This is the bill of materials for my micro controller.

**Dave Jones:** This is actually from the assembler that I used to use to manufacture my micro controller. Yeah, everyone keeps asking am I going to bring it back? I don't know.

**Dave Jones:** Anyway, we'll see. I don't have a specific example here, but this is how you would basically do it. You would have the part number that you want, you would have the manufacturer, you would have the description, you know, the designator and everything.

**Dave Jones:** And then you would have the supplier that you're getting it from and the supplier's actual part number or manufacturer specific part number on there. And then you do this again for supply number two, supply number three, supply number four, supply number five, and you can go as long as you want for something like an LM358.

**Dave Jones:** I don't have anything that generic on here. The only one was actually this LMV321. Where I'll link in the video. I haven't watched it in a long time, but I did actually come when I changed the brand on this.

**Dave Jones:** That's not quite a jelly bean op amp, but I thought it was jelly bean-ish enough that I could change it. And like get it from a different manufacturer. And it turns out no.

**Dave Jones:** I come a gutser on that one and that caused an issue. I've done a whole video on that. But anyway, the whole point is that you can have multiple suppliers in here.

**Dave Jones:** And then if you're a big company like Uni TR for example, they're going to have like a purchasing manager, a purchasing team whose their job is to go out and find the cheapest supplier for these parts.

**Dave Jones:** Hopefully, they get it from a legitimate source, right? So, you tell them where to get it from. Um this is part of you know, the the the designer has to do this, right?

**Dave Jones:** The designer is basically going to do the bill of materials cuz they're the ones who know the specifications for the components and they've looked at the data sheets and they've evaluated all they've physically tested that part and they know it's good and then they can it can go into the official bill of materials and you can have multiple supplies in there and then the purchasing officer's job, their job is to go out and purchase

**Dave Jones:** that exact part number there from whichever reputable supplier they can get it from and you know, hopefully they don't screw that up. Um but then they'll have multiple choices in there for a lot of the parts that are jelly bean.

**Dave Jones:** Of course, you know, usually when you're building some product, you usually you have to specify in a single source part. You can't get around that. The holy grail of any design is to have multiple supplies for absolutely everything.

**Dave Jones:** Something like, you know, like your passive components, your resistors, your transistors and stuff like that in most cases, they're going to be fairly generic jelly jelly bean. But because my micro controller was very precise, for example, and I like bought high precision components, some of those resistors were several dollars each, right?

**Dave Jones:** So, I would actually specify, "Oh, I want a Susuma resistors here. I want this exact tolerance." And only if they can't get it, would the manufacturer or supplier come back to me and say, "Hey, I can't get this one.

**Dave Jones:** Is this substitute okay?" And then you'd you know, you might test it, you look at the data sheets, compare and you go, "Yeah, okay, that's okay. Add it to your supplier list in here." But yeah, this is how and when you're serious about manufacturing products, you're going to have multiple supplies in here.

**Dave Jones:** The bill of materials, very important. But that still doesn't explain on this one board how these multiple brand chips ended up on there. Well, that's It's easy to explain.

**Dave Jones:** When you're getting your PCB manufactured at the assembler, they're going to have these massive pick and place machines like this Yamaha jobbie here, and you can see the feeders here, right?

**Dave Jones:** They They're on big carts. So, all of your reels of components Your components come on reels of like, you know, 1,000 3,000 op amps or something like that will come on one reel.

**Dave Jones:** So, each one of your parts on here each one of these like the op amp These are 10K resistors here, these capacitors here, this diode here, this um LED here, right?

**Dave Jones:** All these different components, they're all going to be on separate reels, and they have to be loaded into um these, you know? So, if you have a look here, you can see that the reels are loaded in there, and they go in, and the machine might have, you know, a big machine might have like 60 feeders, 100 feeders.

**Dave Jones:** They might have feeders on the other side as well. So, you know, there's ones hidden on the other side that you can't see. So, they might have like four of these carts that you can wheel in and out.

**Dave Jones:** And when you're doing high-volume manufacture, it's, you know, delicate dance of getting these pick and place machines to not only to work optimally, but also efficient flow. So, depending on how many components, you know, like each board has, you have to sort of program in all all your reels into the machine to actually have redundancy in the there so you don't run out.

**Dave Jones:** This say the op 07 here, okay? That's There's only one of those on the board, and there's only one of the and there's two of these OP2202s here, for example.

**Dave Jones:** So, if you're manufacturing a run of a thousand of these boards, and say there's a thousand of these SO8 chips per reel, for example, then you're going to need one entire reel just for that.

**Dave Jones:** You're going to need two reels installed for this part, right? Two different reels, and you're going to need three reels in loaded into the machine for the LM358. Otherwise, you're you're to run out halfway during your like you you run and and your machines are typically in a huge line like this, okay?

**Dave Jones:** And you can put multiple pick and place machines in series like this. This a line here has like three physical pick and place machines all in series. So, this could have, you know, 300 feeders or something like that, right?

**Dave Jones:** It can have a lot of feeders, but but some boards have a lot of parts on them. So, you have to load up all of these machines. And sometimes you'll load up one one machine with just passive components like your resistors, your capacitors, your diodes, transistors, or whatever.

**Dave Jones:** And and the next machine you might have your specific, you know, really expensive ICs that you can't afford to waste and and things like that. And so, you can load up machines all in different ways.

**Dave Jones:** But this is all up to the assembler and how they want to do things most optimally. But basically, yeah, you you're going to use three times as many LM358s as you are OP07s over here.

**Dave Jones:** So, you've got to put more reels in that machine. And because, you know, you're manufacturing thousands, tens of thousands, sometimes hundreds of thousands, or millions of these boards, you have to keep feeding in all these reels cuz these machines can spit out these boards pretty quick.

**Dave Jones:** So, you're constantly feeding these reels in multiple times a day, and you're getting from different sources. Your supplier number one might have run out that you had on your bill of materials, so they get it from supplier number two.

**Dave Jones:** And you know, it it doesn't matter. If you've put that into your bill of materials that you can use any one of those suppliers, then really you have no guarantee which reel the assembler is going to insert in here because to them it's exactly the same part.

**Dave Jones:** When your purchasing people send all the reels to the assembler, all the assembler can do often the parts supply, you know, they can do the parts supply for you, order them all.

**Dave Jones:** Then they're going to put their barcodes on there, and that barcode for this reel of Arts chip LM358 is going to be exactly the same barcode as this these ST ones.

**Dave Jones:** So, to the assemblers, it makes absolutely no difference whatsoever. This is an identical part. And that is how we've ended up with multiple LM358s on the one board, which you might think that's weird.

**Dave Jones:** What's going on there? Are they You know, that it does this do something that has a slightly different spec to this one? No, it shouldn't. If they've designed it that way, then they've designed it very badly.

**Dave Jones:** Because the LM358 is not a is a jelly bean part and it's not a precision part and you just don't get you should not care about the specifications. So, that's why it's just this is just an assembly house thing.

**Dave Jones:** They've they've treated that as exactly the same part and it's going to pass with flying colors. And I've done a video on that like I visited the local nest, which is an alarm manufacturer here in Australia and this is their pick and place line.

**Dave Jones:** You can see that they've got multiple Yamaha machines and then it goes into well, and that that detracts like that and the boards just go through all these multiple machines like this to load up and you can have probably reels on the other side as well.

**Dave Jones:** You can see the reels loaded into the feeders. These are the feeders that you plug in. Right, this one has 50. I think yeah, 50 or 48 or 50 feeders or something like that.

**Dave Jones:** Might include some on the other side as well. You can see how it goes through the multiple machines, then it goes into your reflow oven here and there might be optical inspection at the end and things like that.

**Dave Jones:** So, yeah, I'll link in that video if you haven't seen it, but that's a typical, you know, a smallish {slash} medium scale you know, pick and place manufacturing line.

**Dave Jones:** Now, we won't go through the specifications in details here, but suffice it to say that you can go download these data sheets for yourself. I'll actually link them in directly and you can compare the ST to the arts chip one over here and the offset voltages, you know, it's it's like very average as I said, yeah, like the slight differences.

**Dave Jones:** This one might be typical at two for example for just the basic grade that doesn't, you know, if you put A on the end, that can actually be better.

**Dave Jones:** And you know, max of seven over here and this has a max of nine over here for the full range, for example. But as I said, if your design if you're worrying about these specs in your design, then you shouldn't be using a jelly bean component like this op amp.

**Dave Jones:** You should be choosing a specific op amp with specific specifications to meet your need. That's why you can find thousands of different types of op amps. You would not choose a jelly bean if you really cared about any of these specs.

**Dave Jones:** You might slightly care cuz it has like the voltage, you know, the wide voltage range required or something like that. But beyond that, you probably don't care. You just go, "Oh, yeah, you know, 10 millivolts of offset, she'll be right.

**Dave Jones:** No worries." Um and yeah, you just don't care. So that's why I'm absolutely sure that Unity, the designers of this do not care whether or not it's an Arts chip or it's an ST jobby.

**Dave Jones:** And that's how they ended up on there. So anyway, if you found that interesting, please give it a big thumbs up. As always, discuss down below in the EVBlog forum, of course, where there's tens of thousands of us over there um chatting about every minute detail about everything possible.

**Dave Jones:** It's fantastic resource. Biggest on the interwebs. Catch you next time.
