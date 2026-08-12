---
video_id: ZA5vlDdpbkw
title: EEVblog #1105 - $100 Custom LCD Design - Part 3 (µSupply Part 18)
url: https://www.youtube.com/watch?v=ZA5vlDdpbkw
source: youtube-asr
timestamps: {"0": 1, "1": 23, "2": 39, "3": 50, "4": 62, "5": 75, "6": 89, "7": 98, "8": 113, "9": 131, "10": 148, "11": 165, "12": 177, "13": 196, "14": 211, "15": 225, "16": 235, "17": 248, "18": 266, "19": 283, "20": 296, "21": 305, "22": 322, "23": 337, "24": 352, "25": 362, "26": 383, "27": 399, "28": 418, "29": 431, "30": 445, "31": 457, "32": 465, "33": 484, "34": 500, "35": 511, "36": 519, "37": 530, "38": 541, "39": 554, "40": 564, "41": 574, "42": 587, "43": 598, "44": 610, "45": 627, "46": 643, "47": 654, "48": 674, "49": 686, "50": 701, "51": 724, "52": 748, "53": 766, "54": 783, "55": 794, "56": 804, "57": 826, "58": 837, "59": 853, "60": 863, "61": 879, "62": 890, "63": 910, "64": 927, "65": 938, "66": 956, "67": 967, "68": 973, "69": 983, "70": 994, "71": 1004, "72": 1024, "73": 1038, "74": 1050}
---

**Dave Jones:** Hi, welcome to part three in this custom LCD design tutorial and we have our finished product. Check this out. Now, if you haven't seen the two previous videos, I'll link them into the end and down below where we actually discuss designing this thing and all the aspects that go into that and we finally got our custom prototype delivered.

**Dave Jones:** This is the for the new micro supply project which we're slowly working on. Fully custom LCD from scratch and I think it cost a grand total of $138 US dollars for five of these.

**Dave Jones:** It was $100 $100 US dollars for tooling plus like $33 for courier delivery, but it did take them a couple of months. I know it's been three months since the last video.

**Dave Jones:** We just haven't had time to do this video. That's all, but yeah, they finally came through and we got five of these things and check it out. It looks like a bought one, doesn't it?

**Dave Jones:** And these are like supposed to be just like samples. They gave us our five of them, but this looks like any production LCD I've ever seen. I'll show you this up close for those who want to see the pin attachments down there.

**Dave Jones:** They They look glued in very nicely. I mean, nothing about this looks like it's you know, like a a prototype. You really wouldn't tell this apart from a production LCD really.

**Dave Jones:** So, I'm not sure of the exact steps, although there are a lot of steps and I'll put up a graphic of that of what goes into actually manufacturing these LCDs.

**Dave Jones:** There's just so many steps. It's crazy. I'm not sure, you know, at what liberties they take with those steps to get you these prototyping quote marks LCDs, but jeez, it looks pretty good.

**Dave Jones:** So, as seen in a previous video, this is the data sheet they gave us based on our original drawing and it looks like the real thing. It's not actually one to one scale there, but you know, it's got the bump on the end like that down there and you know, all the dimensions are absolutely bang on.

**Dave Jones:** No problems whatsoever. And for those playing along at home, here's all our specs. It's a positive mode super twist pneumatic 8th design for 8th duty cycle water bias 6:00 viewing angle, which if you don't know, this is the bottom of the LCD.

**Dave Jones:** So, the viewing angle is like it's not directly on its optimum viewing angle, sorry. Is like 6:00 is actually like looking down. Like if you've got the product flat on the bench, you're looking down like that as the camera would here.

**Dave Jones:** So, where basically I'm viewing this with the camera at the 6:00 angle. Operating temperature -10 to 50, good enough for Australia. Storage temp goes up to 60. Design for an operating voltage of 3.3 volts.

**Dave Jones:** Here's where we might have an issue, which we'll go into. Design for a 64 hertz frame frequency. The polarizer on the front is a transmissive type, I.E. you can actually see through the thing and it uses an adhesive type rather than I guess just like sandwich together and held together with the glue on the outside or something like that.

**Dave Jones:** So, anyway, they use adhesive down and the back polarizer is reflective cuz this is not designed for a back light at all. So, you know, I guess maybe you could edge light the thing if you wanted to, but back light wasn't a requirement for this thing.

**Dave Jones:** And of course, it's a pin based one and of course, we could order exactly the same LCD. Nothing would change if we wanted to use zebra strips, the conductive elastomer rubber with this thing.

**Dave Jones:** They would simply just leave off the pins and then the contacts would be on the bottom there and they would make contacts with your um conductive um zebra strip, and Bob's your uncle.

**Dave Jones:** So, I'm sure that we could uh change between a zebra contact one and a pin-based one with basically no change in spec. It'd be cheaper cuz then uh they wouldn't have to do the pins, but I haven't actually quoted that up.

**Dave Jones:** And of course, this is actually quite a complex LCD. It's got a bar graph, and you know, uh what is it? Two, four, uh five different um uh four-digit uh seven segment uh displays on it, and there's the uh segment and com how they actually join them all together inside um as we looked at in a previous video.

**Dave Jones:** And it basically uses uh eight commons and 32 uh pins on the thing. Doesn't necessarily use all of them in all uh circumstances. There's a couple of ones which aren't connected in here, but yeah, we basically needed an eight-common uh driver with the thing with a 32 segment.

**Dave Jones:** So, we decided to use a Holtek uh chipset, the Holtek um HT 1622 to drive this thing. I know what you're saying, "Shut up, Dave. Plug it in. Show us it working." Okay, well, here we go.

**Dave Jones:** We've just got a little uh test board here. Don't get excited. This is just a um a micro supply uh just a like a test bed that we can use.

**Dave Jones:** So, here we go. Let's plug it in. And tada! Look at that. Whoa! Like a bought one. Wow! And those segments look good, don't they? But, there's a bit of an issue.

**Dave Jones:** Let me show you. So, uh there we go. There's the digits up close, and that's from roughly the uh 6:00 viewing position, normal viewing position. That's from bang on uh 90° there.

**Dave Jones:** And uh sorry, uh we're getting a little bit of uh glare off the uh overhead lights there. But, it's not too shabby, is it? But, although that looks okay, there is a bit of an issue which with this which we only noticed when we uh started to use the thing.

**Dave Jones:** Let me actually switch it on here and we get our larger digits like that. And they look okay, but you can actually I'm not sure if this will show up on camera.

**Dave Jones:** I have to look at the edit later, but that V is not the best and you'll notice that when the digits change, they are a bit faded. There are some digits in there which do which are like not like the others and it's like a drive problem with the LCD.

**Dave Jones:** But, as I said uh we are using that Holtek HT1622 uh driver chip which is designed specifically for this. Um and there are no like uh software commands, like there's no uh you know, registers in there that we can screw up the bias voltage or anything like that.

**Dave Jones:** It's supposed to be able to handle this just fine. If you stare at it for a while, you might especially look if I go to a higher angle like this up here, like it works uh by the way, angle um you know, it's designed for 6:00 which is roughly about there, like straight on is there, so it looks really good.

**Dave Jones:** From the low angles like that, it really starts to fade out. So, it's it's by no means, you know, the world's best um LCD, but Oh, look, that one's not too That one's pretty good, isn't it?

**Dave Jones:** At that angle. Anyway, it could be you know, studio lights and stuff like that. But, anyway, if I tilt that up, so we're looking down on it, you can see that some of the segments just aren't as crisp as some of the others.

**Dave Jones:** And that includes the V, that segment there. So, I I suspect that they're all on a common. I'll have to double-check that. But, if they are, then we've just got something slightly out.

**Dave Jones:** And we contacted the manufacturer and they didn't uh know off the top of their head, of course, but they said, "Hey, you know, it could be just a drive voltage issue.

**Dave Jones:** So, try increasing the supply voltage to the chip." Now, our Holtek where we're using our Holtek chip at 3.3 V. We specified a 3.3 V nominal uh L you know, um supply voltage LCD, but it's just looks like maybe one of them is just, you know, slightly out.

**Dave Jones:** Pretty sure that's going to show up on camera. And of course, if you take it back to 90°, it looks fine and dandy. You can kind of just see it maybe on the uh ideal 6:00 angle there, but anyway, go that high angle.

**Dave Jones:** Yeah, so we might have to hack into this thing and increase out the supply voltage of our chip. It can actually go higher. So, yeah, it just wasn't quite as good as we're expecting.

**Dave Jones:** We don't know whether or not this is just a prototype um as we said, but of course, that's the idea of getting prototypes as you can see what the quality is going to look like.

**Dave Jones:** And you know, you wouldn't just go, "Oh, you know, she'll be right. It's only a prototype. It'll be better in production." No, you know, you want to solve this um uh problem now.

**Dave Jones:** So, anyway, might get in there and hack the voltage on there and uh increase it and see if it makes a difference on that uh they've got to be on the same common, surely.

**Dave Jones:** And sure enough, they are. Look at this. If we follow the money, follow the line down here, that connects to that segment there. And then, that goes it shows that it actually goes through the gap in there connects to this one.

**Dave Jones:** So, that segment, that segment is tied to that segment, which then goes around. And does it go to the V? I think it might go to the V. I think we have a winner.

**Dave Jones:** So, that common is, you know, there's some issue with that common. Now, whether or not it's the driver chip we've got shouldn't be. It's an industry standard driver chip.

**Dave Jones:** It's It's around a long time. Should be doing the business. There's no, you know, it's it's optimized for this kind of application. Um, you know, so I suspect it's more likely uh something to do with the design of the uh manufacturer of the uh LCD.

**Dave Jones:** It just doesn't, you know, they didn't optimize it right for the uh supply voltage. But I guess you could say, "What do we expect for like a 100 bucks tooling?"

**Dave Jones:** You know, for our five LCDs delivered or 138 US bucks delivered. Hm. Ridiculously cheap. And uh we got a pretty half-decent LCD out of it. I mean, it's absolutely phenomenal that they can do this for the price.

**Dave Jones:** They're obviously not making money on it. They're hoping for the big order. Well, gave it a bit of a clean up, but it's still there. But curiously, this segment, which is part of these, which I thought was dodgy before, faded before, is not faded anymore.

**Dave Jones:** So, I Anyway, all right. So, what I'm going to do is uh hook it up to an external supply. I've broken into a track underneath, which uh has the just the supply for the HT1622 LCD driver.

**Dave Jones:** And I've currently got it set to 3.3 volts, and I'll change it in uh 0.1 volt increments. So, I know I am viewing it from the ideal 6:00 uh angle here.

**Dave Jones:** But anyway, let's go down to 3.2. See what happens. Oh, there we go. 3.1. 3.1, it's fading. 3.0. Look at that. Hopeless. So, I'd expect 3.4 to be rock solid.

**Dave Jones:** Oh, there we go. 3.7 now. It's rock solid 4 volts. Oh, now we're starting to see some uh ghosting on the segments now. You don't want that. That's no good.

**Dave Jones:** So, that's at 4 volts. So, you definitely don't want to run it at 4. 3.8. 3.7. 3.6, 3.6 seems to be I'm going to say that's ideal. Look at that.

**Dave Jones:** Now we're looking down like that. That's 3.6 volts. 3.5 volts, sorry. That's 3.6. There you go. That's 3.5. 3.4 volts, and 3.3, and sure enough we have our ghost in segments or a faded segments, whatever you want to call it.

**Dave Jones:** And 3. Oh. 3.2, yeah, it's horrible. So, 3.1, 3.2, 3.3, and 3. 4. There you go. So, we only had to go up 100 millivolts to get rid of our problem, I think.

**Dave Jones:** Really? Oh, 3.4, I don't know. 3.5, I'd say to completely get rid of it, go up to 3.6. There you go. That's 3.6. So, yep. There you go. That's 3.6 volts.

**Dave Jones:** I like that. So, it looks like um it's even though we specified like a nominal 3.3 volt uh supply is what this thing's working at, and we I think we may have told them what hold what chipset we were using, I think.

**Dave Jones:** I can't can't recall exactly. Um but anyway, um yeah, they they designed it around all of our uh specs, which came from the data sheet from the Holtek device.

**Dave Jones:** So, all of this stuff down here, this all came from, you know, 1/8 duty quarter bias, um all that uh sort of jazz, 64 hertz frame frequency, uh voltage.

**Dave Jones:** That all came from the Holtek chipset itself. So, I can only presume that the LCD manufacturer um has, you know, the tolerances just like slightly off. What manufacturing step that would actually be that makes it out like that, I don't exactly know.

**Dave Jones:** We'll have to uh talk to them. Um so, there you go. I mean, it it's fixable. I mean, even if we had these in volume, you know, even if we push the button and ordered, you know, 1,000 or 10,000 of these, we could still run with this.

**Dave Jones:** Uh you know, we can modify the design to operate it from uh just the Holtek chipset from a higher voltage. That's no problem at all. Uh because the 3.3 V uh interface digital interface would uh still work cuz we've got CMOS voltage levels, so they'd be 0 and 3.3 V.

**Dave Jones:** So, even if we ran it from 3.6, it might even still work at 5. We might even still be able to interface uh with it still. So, um no problems in the logical level.

**Dave Jones:** We wouldn't need a logic level translator or anything like that. Um you just need to run it at a higher voltage. Now, whether or not this problem would have been fixed in the production ones, well, you know, you wouldn't want to take the risk, would you?

**Dave Jones:** That's the whole idea of getting these prototypes, so you can see stuff like this. I'm kind of glad that we had an issue with our bargain basement um $100 100 US dollars for five LCDs.

**Dave Jones:** Um that's the tooling charge, that's everything, and uh 30 bucks courier to get it here. Um it's it's basically, you know, it's it's peanuts. It really is. Although, it did take a couple of months, but you expect that when you're paying like that ridiculously low rate.

**Dave Jones:** That's just crazy low. So, anyway, um yeah. We'll talk to the LCD manufacturer. I might do a follow-up video, or I'll just follow up on the uh EEVblog forum with comments or something like that, but 3.6 I reckon that's the go.

**Dave Jones:** And that's quite a nice LCD. There you go. So, that is that's the part three in how to design your own custom LCD. It's not that hard. It wouldn't necessarily be this cheap for you and me.

**Dave Jones:** We found a very cheap manufacturer. We won't say who it is. But they they look, you know, quite reputable and large-ish. So, you know, it's not like some, you know, someone's kitchen.

**Dave Jones:** So, it's not like someone's kitchen table in in Shenzhen or something like that or the back room at the Shenzhen markets. So, this was quite a large LCD company doing this.

**Dave Jones:** But yeah, I mean, I guess you might get what you pay for in this case. You know, they sort of it's a one of these 100 buck prototype jobs.

**Dave Jones:** We'll just slap it together, you know, she'll be right, no worries. So, it's you know, it's hard to say where the issue is, but I'm very impressed with that.

**Dave Jones:** For a fully custom LCD like that for five of of course we we had to sort of not promise them, but we had to give them a ballpark of, you know, look, we're serious and we're thinking about making thousands of these things.

**Dave Jones:** So, you know, we might order, you know, 5,000 LCDs or something like that in the future and sort of yeah. They were happy to give us these prototypes for 100 bucks.

**Dave Jones:** So, I hope the takeaway from this little video series for you is that hey, it's not that difficult or expensive to custom design your own LCD. You probably won't might not be able to get it for this price, but you know, typical prices might be, you know, two $300 or something like that for prototype LCDs.

**Dave Jones:** And if you only want, you know, like a few dozen of them or something like that, then it's even a viable option at that sort of price. It could make or break your a for example, and it makes your product look custom and professional, doesn't it?

**Dave Jones:** I really like it. Winner winner, chicken dinner. So anyway, if you like that video, please give it a big thumbs up as always, and discuss below either in YouTube comments or on the EEVblog forum.

**Dave Jones:** Hope you found it interesting. Catch you next time.
