---
video_id: VnrtneFP_6A
title: eevBLAB #51- Industry Story - Design Deadlines & Unusual PCB Designs
url: https://www.youtube.com/watch?v=VnrtneFP_6A
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 49, "3": 70, "4": 92, "5": 113, "6": 129, "7": 143, "8": 164, "9": 185, "10": 202, "11": 219, "12": 231, "13": 248, "14": 262, "15": 283, "16": 301, "17": 324, "18": 343, "19": 365, "20": 383, "21": 402, "22": 419, "23": 435, "24": 450, "25": 465, "26": 479, "27": 495, "28": 510, "29": 530, "30": 541, "31": 559, "32": 581, "33": 598, "34": 614, "35": 634, "36": 652, "37": 668, "38": 681, "39": 699, "40": 716, "41": 727, "42": 745, "43": 762, "44": 780, "45": 796, "46": 811, "47": 827, "48": 841, "49": 861, "50": 882, "51": 896, "52": 919, "53": 938, "54": 952, "55": 968, "56": 982, "57": 996, "58": 1014, "59": 1030, "60": 1050, "61": 1070, "62": 1083, "63": 1100, "64": 1117, "65": 1133, "66": 1154, "67": 1169, "68": 1185, "69": 1204, "70": 1226, "71": 1243, "72": 1263, "73": 1282, "74": 1298, "75": 1310, "76": 1327, "77": 1345, "78": 1364, "79": 1377, "80": 1391}
---

**Dave Jones:** Hi, it's industry story time, because people say they like to hear industry stories, so I found this in the bunker the other day. Check it out. I've probably shown this before, somewhere, along the line, but anyway, I thought I'd tell you the story of this.

**Dave Jones:** What the hell is it, and how did it come to be? Because it's a rather interesting tale of a last-minute design scramble for a trade show. So, as you know, I used to work at Altium, so this is back in 2007. Now, we had already released the Altium NB2 nanoboard back in early 2007, I believe it was,

**Dave Jones:** and I'm not sure how long it was for sale at the time, but anyway, that was sort of like the previous year's big release, you know? So, it was a development board, because Altium were getting into FPGAs, that was their vision, and it was a development board that had plug-in FPGAs, you could get all different vendor FPGAs,

**Dave Jones:** and then all these peripheral boards that you could plug on and do different things, you know, audio, video, interfaces, HDMI, GSM, and IO, and all sorts of stuff. You could just plug in, had a little LCD on it, and everything else. And it was actually a ridiculously expensive development board.

**Dave Jones:** Here's a press release from September 9th, 2008. So this is a year later, when they decided to sell it via DigiKey. And they're at a price, $4,300, bargain price of $4,300. Although, it did actually come with the, like, a stripped out version of Altium design

**Dave Jones:** that allowed you to do all FPGAs and everything else, you got a license and all that sort of stuff. Famously turning the world of electronics design upside down, where PCB, the PCB module in Altium was optional extra. Yep, you bought the nanoboard, because that was Altium's vision,

**Dave Jones:** is that you wouldn't need to design your own boards. Why would you need to design your own boards? Because you could just use all these custom boards. This is the end of 2007. 2008's about to roll around, and the big conference in Silicon Valley was coming up,

**Dave Jones:** the big trade show, DesignCon 2008. And of course, Altium had to have the biggest and baddest stand there. And here it is, what it ultimately turned into, but we'll get into that. So they wanted something new to show off, and a new concept, you know, couldn't just show the nanoboard again.

**Dave Jones:** So they came up with the concept, I think probably Nick Martin, because he came up with all, you know, he drove everything at the time, CEO of, our founder and CEO, and came up with the idea for the industrial nanoboard, where, you know, the NB2 nanoboard was just a desktop development type thing.

**Dave Jones:** But of course, the vision was that you could buy all these off-the-shelf boards, you could develop it on your desktop version, and then just plug them into this industrial version, and just plug it on the wall. So the idea was that it would be more industrial-like,

**Dave Jones:** and here's a 3D model of it, and it had the same peripheral boards on here, so here we go, these peripheral boards, and it had the, where is it, you know, it had, it's like a more industrial type LCD on it, and stuff like that.

**Dave Jones:** And, but it was fully compatible with the desktop, so you could take the modules off there, whack them in, and it had like a bit, like a proper industrial enclosure with panels, you could get cables in and out of, and grommets and all that,

**Dave Jones:** you know, all that sort of jazz that was powered from, you know, external power supplies, like industrial power supplies, and stuff like that. And, you know, it was a decent idea. But the problem was, is that they came up with this idea in December 2007,

**Dave Jones:** and the DesignCon show, which they wanted to show this off at, was like the end of January, I think, or maybe like the 1st of February or something. But we had to get this done by, it was like, I don't know, early to mid-December at this point,

**Dave Jones:** and we had basically a month and a bit to get this all not only designed from scratch, but actually then manufactured, prototype manufactured, assembled enough that we had, could show off at the DesignCon booth. And who got stuck with the design of the PCB for this puppy?

**Dave Jones:** Not just one, but two different versions of it. And so this is what it turned out to be. But anyway, this was a very tight time frame to get all this done, with Christmas in there as well. Christmas and New Year's, when, you know, a lot of companies shut down,

**Dave Jones:** you can't get parts delivered, and, you know, all sorts of issues. But anyway, so I started frantically working on the design of the, this industrial nanoboard. And thankfully, the Altium design system was really good, because we already had, like, you know, a lot of the blocks, all the schematic blocks,

**Dave Jones:** and parts blocks, and everything else. So it came together rather quickly. But, you know, it was an entire design from scratch. And this is a, this is, what, an 8-layer jobby here. I won't go into too much detail. But anyway, I managed to get together this one,

**Dave Jones:** plus another version, which was basically the same thing, but it was, like, a different form factor. They wanted to have multiple form factors. So two boards, plus a display board, and everything else that had to all come together before the trade show. So I can, oh, there's a bug.

**Dave Jones:** It doesn't like that, does it? Oops. So this is the industrial nanoboard design that I came up with in consultation with the mechanical engineer at the time, who was designing all the enclosures, and case, and did all the, you know, 3D modeling stuff, and things like that.

**Dave Jones:** So I remember vividly working on Christmas Eve, and in the Altium building, there were only two people left, myself and Nick Martin, because Nick Martin was, like, always there. I think he lived there. So I went, oh, bugger this, it's Christmas Eve, I'll go back home and I'll work remotely,

**Dave Jones:** because we had, like, a remote desktop interface. It was really difficult for the time to do, but I used Altium at home, but I could, you know, get the files and everything remotely. So I thought I'd go home, finish, bugger off home, finish the design, and so it was, like,

**Dave Jones:** late at night on Christmas Eve, and I needed to order some parts so that we could have them from Farnell's, or wherever, or Digikey, or wherever, so that we could have the parts, you know, straight away. And I'd forgotten my company credit card.

**Dave Jones:** It was back at the office halfway across Sydney, so I thought, I wonder if Nick's still there. Nick will still be there, sure enough, contact him. Yep, he's still there. He went to the, this is, like, you know, midnight or something on Christmas Eve.

**Dave Jones:** It's just nuts. Anyway, so he goes over to my desk, gets me my, reads me my credit card numbers. Yay, we're saved, we're able to order the parts. So anyway, that was just nuts, like, on Christmas Eve. Anyway, I think we just got the parts

**Dave Jones:** before Christmas, or early New Year's, or something like that. Anyway, I was frantically finishing the design of these boards off, but then in, like, early to mid-January or something, we only got, like, a couple of weeks left, they're still designing the stands and everything else,

**Dave Jones:** and they got the idea for, you know, the slogan, seeing is believing, but touching is more fun. We had t-shirts with, like, all this, like, with this fun on the back. I've probably still got a bunch of t-shirts somewhere at home. Anyway, we already had the NV2 desktop,

**Dave Jones:** which we could show off as well, and we had the industrial nanoboard, and here it is. Here was the final solution down here in the two different form factors, and you could join them together. It was really quite neat from a mechanical aspect and stuff like that,

**Dave Jones:** but then they said, oh, they wanted to show a third step where, you know, you could do your own custom boards if you wanted to. So Nick said, you know, Dave, give me a custom board. Something that looks custom-y. And I went, well, what does that mean?

**Dave Jones:** Like, we've got no time left. Like, we've got, like, a day to do it or something like that. So I was scratching my head for a while, and, like, I think I maybe came up with a couple of ideas, and he didn't like them and stuff like that.

**Dave Jones:** And then I go, no, well, like, we've just got to, like, take the existing design. Don't have time to design something brand new. And so I came up with the idea to take the existing design and just make it look funky. So instead of outie and black, we'll make it red,

**Dave Jones:** and I decided to make it curved like this, right? And then add these big, like, shock mounts on here, like vibration, anti-vibration mounts. And it was just, like, one of the most bullshit ideas ever. But it was, like, you know, it looked kind of funky.

**Dave Jones:** And Nick loved it and said, yeah, let's go with that. So we had to, so I basically had the design. I just had to, you know, make it all funky and stuff like this. So I got this emergency rush assembled, like, I'm talking, like, 24-hour protos,

**Dave Jones:** as we did with the other ones. Eight-layer board, we got these turned in 24 hours. Don't ask the price. If you have to ask the price, you can't afford it, to get a board like this spun in 24 hours. So we got these made, and they look really funky,

**Dave Jones:** but then we had to get them assembled. And, of course, like, there's 0402, you know, lots of 0402 parts on there and stuff like that. And there's, you know, 600, 700-pin, 670-something-pin BGA and, you know, all sorts of stuff. So we could have done it by hand, but we actually decided,

**Dave Jones:** like, we needed a bunch of these. We needed, like, you know, six of them or something, half a dozen or something like that. So we rushed assembly job, once again, paying absolute top dollar. Because when you either go to a PCB house to get something like this 24-hour prototyped,

**Dave Jones:** or whether or not you go to an assembler and say, hey, I need my boards assembled today. Start programming the pick-and-place machine. I need this damn thing done. They'll go, sure, but we're going to charge, like, five times the normal price, or whatever it is.

**Dave Jones:** Because they have to then bump all the other jobs, and, well, you know, the other customers aren't going to be happy, so they want to be compensated for that. So it cost a lot of money. Anyway, we got these assembled, and we got them back in, like, a couple of days.

**Dave Jones:** Like, it was nuts. The timeline was just absolutely insane on this thing. And what do you know? All of the parts on here, like the, all of the, like, 0402s, where is it there? All the 0402s and stuff like that, they all tombstone.

**Dave Jones:** All the chips, well, not all of them, but yeah, I probably was. They all flipped up like this, because, as part of the industrial look and feel, I went for a double thickness board, so a 3.2 millimeter board instead of your standard 1.8.

**Dave Jones:** And it's an 8-layer board, it's got all ground planes all in there, so this actually retains a ton of heat when you put it through the reflow oven. You know, you do the pick and place, and then it goes along the conveyor belt,

**Dave Jones:** goes into the multi-stage reflow oven, and solders the parts on. And I think they goofed it up or something, and they didn't, they had the wrong temperature profile for it, like it was for a 1.6 millimeter board, and this thing retained all the heat much higher.

**Dave Jones:** So even though the surface mount components on here had thermal relieves, and we can see that, so even though all the parts had thermal relieves on them, and as you can see here, right, we shouldn't, they shouldn't have, you know, like, you know, tombstone, right?

**Dave Jones:** Because they're not directly connected to the ground plane, but because the board was so massive and had so much copper in it, it retained so much heat, and they goofed the profile, and it didn't cool down at the correct rate, and then the one pad cools down quicker than the other one,

**Dave Jones:** and then, whoop, it flips up. Anyway, screwed them all up, so there was a last minute frantic effort to go and rework all these 0402 parts to get them back down. Anyway, we finally got this done. We got them assembled, because they had to work.

**Dave Jones:** They wanted them on the stand to actually work, and ta-da! There's the final product working down there, and it was like a GSM, was it a GSM app? No, that one was just displaying a slideshow. But we needed it to actually do stuff,

**Dave Jones:** whereas the one up here had, like, a GSM module down in here, and you could, like, SMS a thing, and it would pop up, you know, it would pop up on the screen and stuff like that. So, yeah. So that was the, you know, the stand that they wanted to have,

**Dave Jones:** and we needed to set up multiple ones of this. But it wasn't over yet, of course. It was, once again, a frantic last minute effort to not only get all these designed, assembled, the software tested, the software written, the apps, you know, tested, and all that sort of stuff,

**Dave Jones:** and then the design people were working on these display boards and things like that for the stand, and, you know, how all that was going to go together. And the cases, these industrial-type cases here, we didn't have, like, the injection molding cases yet.

**Dave Jones:** These were just, like, prototypes. So I think they were all hand-finished out of fiberglass. They were all, like, hand-done. We didn't, like, some shop did it or something. So all these hand-done, they were really fragile, apparently, these hand-done fiberglass shells and everything. And, like, I think if you breathed on them,

**Dave Jones:** they would break or something like that. But we had to have something to show off at the DesignCon show, because it was the big show of the year, you know. And it was, you know, there's a lot of company prestige, and there's a lot of press around it,

**Dave Jones:** and, you know, things like that. So we got these fiberglass shells assembled. So they were extremely fragile, and we had to get them, I don't know where we had them made, but we had to get them shipped to Altium's headquarters at that time in Carlsbad, down near San Diego in California.

**Dave Jones:** And so we got them all rush-shipped there. So we had to all fly over there with our tested boards and everything else, but we had to, like, fit them inside these cases and everything. And I don't think they were painted or something. They weren't painted, and they weren't sanded down or something.

**Dave Jones:** So at the Altium HQ over there at Carlsbad, we had to, like, you know, sand them all down and finish and make them all look nice and, you know, ready for the show, install the boards and stuff like that. But as it turns out, they were too fragile to just, you know,

**Dave Jones:** throw in a crate and just ship them there, because, you know, these companies are notoriously bad at, like, handling this sort of stuff. So we had to get, and we had, like, dozens and dozens of these, and lots that we had to carefully pack into boxes

**Dave Jones:** so the boxes were big with all the bubble wrap. And there's no way we could get all this stuff on a plane or, you know, anything like that. So we thought, right, we'll hire a van. So we hired a van, stuffed it all full of, you know,

**Dave Jones:** full to the brim with all these boxes of all the trade show stuff. And myself and the mechanical engineer went, right, we have to get, like, there's a day left or something, and we've got to drive up to, from, like, basically San Diego

**Dave Jones:** up to Silicon Valley at the one convention center, wherever it was, the San Jose Convention Center, was it? And so we took a road trip up the, it was quite a nice road trip, actually, thanks for asking. And anyway, we managed to get there on time,

**Dave Jones:** and, but it wasn't over yet. We had to get all this sort of stuff assembled, tested on the trade show stand, and if you've ever done a trade show stand, you know it never is ever done early. So, like, the doors were open, like, 10 a.m.

**Dave Jones:** or something, and, like, 5 minutes to 10, we're under the benches, you know, wiring stuff up, still screwing things together and going, hope it all works, we power it all up, and, like, people are, we're still doing that as people are, like, walking onto the stand.

**Dave Jones:** But we got it done. So there you go, that was the, there it is, the custom nanoboard. And, like, here's, and there you go, there's Nick and former CEO at the time, Emma LaRusso. Yeah, that's another story. She didn't agree with the company vision,

**Dave Jones:** let's just put it that way. And, you know, it was fun. People were, there's, you know, just a, I don't know, a random person playing with the, playing with the board. And, you know, it was one of the demos that we had up

**Dave Jones:** because it looks funky on the screen and the 3D modeling. You know, back in 2008, you know, 2007, 2008, the 3D modeling thing was, you know, really innovative and novel and stuff like that. So we had our, trying to flog our $4,000 development board

**Dave Jones:** and these industrial enclosures, as you saw. But, and there's someone, I forget who that is, but just in the middle of setting up the stand. What was that packing up? I'm not sure. Anyway, we managed to get it done at the last minute.

**Dave Jones:** So it was frantic and I worked all over Christmas and New Year and, like, just absolutely flat out. I think I took, like, half of Christmas Day off with the family. That was frantic. And, yeah, I managed to get all the two different

**Dave Jones:** industrial designs done plus this shock. It was called the shock. It's, you know, the NB2 shock version. And it was complete wankery, right? But we just, like, we just needed something that looked custom. And everyone thought it was great. So, you know, yeah, anti-vibration feet.

**Dave Jones:** I thought that was a great idea. Blank PCB, whatever. Yeah, it worked and it wasn't much, you know, it's like an hour's design effort to actually design that when you already have the rest of it. You know, it's really, it's not hard at all.

**Dave Jones:** But, yeah, all that had to come together. Three different designs and, well, yeah, there was three or four different boards plus enclosure design and everything else in, like, it was probably a month, it was a month and a half tops. Absolutely crazy. But we managed to get it together

**Dave Jones:** and it all worked on the display stand and everyone was happy. But whatever happened to the industrial version? Well, I don't quite remember. But I'm not sure if we actually took any orders for it. But it just, I don't know, somehow just the concept died away.

**Dave Jones:** And we, I don't think we ever actually sold the industrial version. It was actually kind of neat. But once again, it was ridiculously expensive just like the NB2 Nanoboard, which was, like, $4,000. And when we eventually tried to sell it at DigiKey, even when we halved the price to, like, $2,000,

**Dave Jones:** it's still the world's most expensive development board and it didn't sell diddly squat. As was much discussed in the community, the Altium design community at the time and stuff like that. Eventually did come out with the NB3000, which was like a $300 development board,

**Dave Jones:** and that one actually sold in reasonable numbers. Oh, that was part of the turning the world of electronics design upside down when they made the PCB design module optional, extra, I think. Anyway, so there you go. That is the history of the... of this doodad.

**Dave Jones:** This funky little... But it really worked, and it was on the trade show. It was one of those last-minute scramble things. And if you ever get invited to be on a trade show stand, don't do it. Don't do it. It's... It's soul-destroying, I think.

**Dave Jones:** When you're on a trade show stand, you'll just be buggered by the end of it. By the way, I forgot to mention, during all of this, while I was staying at the Hilton in Carlsbad in California, near Altium HQ there, like, the first day,

**Dave Jones:** I got food poisoning. It was the worst food poisoning I've ever had in my entire life. So the rest of the two-week trip, or however long it was, I basically ate nothing. And when I got back, everyone just looked at me and went,

**Dave Jones:** what the hell happened to you? And it's like, yeah. I was... Almost didn't eat a thing for two weeks. It just... It was awful. So... Yeah, that wasn't a pleasant trip. After, you know, a frantic month of designing, all this sort of stuff.

**Dave Jones:** And these trade show stories, they're often always the same. I always have the belief that engineers do their absolute best when they have a real hard deadline. Like, you have to do it. That trade show's happening, we've booked the stand, and all the stuff is, you know,

**Dave Jones:** designed. We need the desktop, we need the industrial version working, we need this custom version working. It's all done. It has to be done. And engineers just magically get it done on time. It's amazing when you have a really strict deadline. And, you know,

**Dave Jones:** even though we had hiccups in assembly, and we had software hiccups, and I think the software was still being tweaked at like the last minute, even on the trade show stand, it was still being tweaked, and bugs being worked out, and, you know,

**Dave Jones:** all sorts of stuff like that. So, but it gets done. And it's amazing what you can do when you have a deadline. Anyway, I hope you enjoyed that story. If you please did, give it a thumbs up. And if you've got a frantic,

**Dave Jones:** last minute design story like that, leave it in the comments or over on the EEVblog forum. Catch you next time.
