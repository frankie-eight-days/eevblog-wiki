---
video_id: ewtdnzlv0Rg
title: EEVblog #1032 Part 2 - John Kenny Keysight Interview
url: https://www.youtube.com/watch?v=ewtdnzlv0Rg
source: youtube-asr
timestamps: {"0": 8, "1": 22, "2": 39, "3": 58, "4": 80, "5": 91, "6": 99, "7": 123, "8": 140, "9": 155, "10": 179, "11": 198, "12": 211, "13": 238, "14": 252, "15": 268, "16": 292, "17": 311, "18": 334, "19": 349, "20": 365, "21": 376, "22": 389, "23": 403, "24": 421, "25": 440, "26": 452, "27": 465, "28": 482, "29": 494, "30": 513, "31": 525, "32": 538, "33": 550, "34": 559, "35": 569, "36": 585, "37": 601, "38": 613, "39": 625, "40": 653, "41": 664, "42": 679, "43": 691, "44": 714, "45": 735, "46": 761, "47": 783, "48": 796, "49": 805, "50": 817, "51": 828, "52": 845, "53": 855, "54": 869, "55": 894, "56": 906, "57": 926, "58": 940, "59": 950, "60": 965, "61": 979, "62": 987, "63": 1005, "64": 1022, "65": 1036, "66": 1052, "67": 1064, "68": 1077, "69": 1088, "70": 1103, "71": 1116, "72": 1138, "73": 1157, "74": 1169, "75": 1182, "76": 1197, "77": 1211, "78": 1224, "79": 1239, "80": 1263, "81": 1289, "82": 1298, "83": 1316, "84": 1326, "85": 1337, "86": 1352, "87": 1363, "88": 1375, "89": 1389}
---

**Dave Jones:** Design tools. How have they changed over the years? From like '78 when you started, were you still doing the uh the the tape on the film? Yeah, we were using Rubylith and and board layout that way and then it it trimmed Doing it by hand?

**Dave Jones:** Doing it by hand with Rubylith and and the little coupons you put down for the Yes. Yeah, the for the IC for the DIP packages and stuff. Yeah. Yeah. And now it's all on on a computer and it's uh it does all design rule checking. You put in all your constraints, all your safety spacings, all your transmission lines, all your ampacities for all your tracks and it checks everything.

**Dave Jones:** But what have been the major advances in the development tool? There'd be one where you switch from the uh from the tape to a PC for laid out boards and then it happened in multiple steps. It went from the Rubylith to where you you you the one tool we had was you would draw everything in pencil and then use a giant digitizer.

**Dave Jones:** Right. To enter it. You'd still draw it in with pencil but then you digitize it into the computer. I don't Digitize it instead of Why? Cuz that was more efficient at the time? have the the graphics technology in the computers. It wasn't as far advanced to now where you can use a mouse and just click and and pop tracks in. But one of the the things I still to this day I'm still impressed by. You take this tool and you'll have say 20 traces that are

**Dave Jones:** minimum spaced and you have to get a 21st trace through. And you want it to go down the middle. Yeah. And you take your mouse and you drag it through the middle and all the other tracks they move out of the way. To this day I still get goosebumps watching it.

**Dave Jones:** It is magic. It still is. Cuz what that used to take before was Rip them all up. Well, you have to move this one, move this one, move this one and then you have enough space and run it through.

**Dave Jones:** And then oh, I have to run a 22nd and you have to do it all over again. It's just you know, the auto plow it's called. It's just Yeah. It's still scary cool. What tools are you using internally to develop products like this? What PCB tools? What simulation tools? What So that was actually PC tools one of the things that was interesting is we had different people in the company 10 years ago using different tools. But 80% of the company was using a tool called Design Architect. It was from Mentor

**Dave Jones:** Graphics. Oh, okay. Yeah. And that was a good tool, but it didn't serve everybody's needs the best. So today we're on their newer updated tool called Expedition. Yep. And DX Designer. And now we've pretty much gotten everybody 100% onto the same tool. And for someone like me whose job is to move designs from group to group, Mhm.

**Dave Jones:** that's invaluable because I can take a PC design, a circuit design, whatever it is that someone did and give it to someone else and it just works. We have a common core uh database for all our parts throughout the company with all the coupons for all the the parts. If anybody sets up a part, anybody else can just grab that part and drop it onto a board.

**Dave Jones:** Got it. And the layout tool actually has the full corporate database right in the schematic capture. So you can just say, I need a resistor 0.1% 5 ppm. It says, well, here's the eight different parts, different power levels. And you just grab it and drop it into your design. So it's our corporate uh tool group is really really amazing people. Um And that's all part of your efficiency job title. If I don't I don't in terms of Or is that a production?

**Dave Jones:** No, we We have a group. I'm not directly involved in that. I take no credit for the things they've done. They've done that without any of my help. Um They've just done an amazing job. It's really one of the enablers for us to get more efficiency though. I appreciate the fact that it's there. My job was to demand that we all use the same tool and get on board. And if there's a problem with you getting on board, I would help arrange training and and help people convert over to it their

**Dave Jones:** designs because trying to move We're still We have some older designs that I'm trying to leverage into new stuff. And if from the old tool, we have to do a what we call a Gerber copy where they put the Gerbers for the board layout and then trace all the new traces.

**Dave Jones:** Oh, no. Yeah. No, that's yep. But But you have to do that. Sometimes sometimes. Oh, well, I Right. Okay. Simulation is still not um common in in terms of a standard tool. We have different people like different simulation tools. We obviously sell you leave it up to the individual designer to use their tool of choice or Depends on what work you're doing. We make We make the premier RF design tool in Keysight that all the RF guys use and it's used universally by all those folks. You couldn't really do their job

**Dave Jones:** without it because it includes the board layout. They use a different board layout package for them because it includes the characteristics of the RF or the board's part of the circuit. And then the the rest of the the people use things like Cadence Allegro as used.

**Dave Jones:** A lot of people frankly use Tina and LT Spice for simple stuff cuz it's free and it's tied into the parts quickly. So you're just trying to do a simple wave filter or something like that. They'll just use that. Um one of the things that our our power group is actually really focused on is a tool called Saber by Synopsys.

**Dave Jones:** It's a very very powerful mixed signal simulator that can do the digital feedback and the analog interaction. Wow, that's powerful. It's a very expensive tool compared to some of the other simulators and it's more complicated to learn how to use, but when you're starting to do some of this mixed signal stuff, you really can't do it without it. It's essential. You can't do it. It would be impossible or it would just be so laborious that We've done it without it, but it's it's much more difficult.

**Dave Jones:** And it's it's a There's a couple of their simplest I think is one of the other big competitors for that. And of course MATLAB and Simulink. We do some stuff in MATLAB and Simulink as well. A lot of people use that, but for Saber, you can actually do the spice kind of things with digital feedback. All in all that's that's How would you even begin to program something like that? I don't know.

**Dave Jones:** That's crazy. And it's about 20K a seat per year. Wow, okay. The good news is because we have people all around the world, one seat serves multiple places. Oh, it does. Okay, right. So as long as I don't use it at the same time, you're good. You can transfer the license. We have a big operation in Penang and Penang is 12 hours different from the US. So depending on where you're in if you're in Colorado, it's I guess 10 hours, but it works out perfect that we

**Dave Jones:** can buy one license and get two views out of it. How How difficult is that time gap? Are you always flying there? Do you have Do you have people there working for you? And I spend I'd say four nights a week on teleconferences at 9:00 at night.

**Dave Jones:** four nights a week. Yeah. And But I get to get up late, so I don't have to get up early. Right. But not at We try to minimize the number of people have to do that because it is disruptive. Not everybody likes to I enjoy it. I do a lot of trips over there and I I run a couple projects over there for the low-cost power products.

**Dave Jones:** Um, I enjoy it very much. They're great group of people and I think for the longest time they were kind of treated like a little bit less. I don't think they ever deserved that, but, Yep. you know, that was our manufacturing manufacturing side.

**Dave Jones:** like it's it's it's the dirty part of engineering. And the fact the fact is they're critical for us to be effective is to meet our cost goals against some of these new competitors coming in. They're as strategically important as any part of our company.

**Dave Jones:** So, you mentioned tools before. You know, we really didn't touch upon firmware and software tools and one of the things that the company is really focusing on right now is standardizing on our software infrastructure Right. and our firmware infrastructure. So, we've been a Windows CE house for many years.

**Dave Jones:** I was going to ask about CE. Microsoft is sunsetting Windows CE. Ah, right. You know, I never heard of this before, but evidently Microsoft will not let us buy a bunch of licenses and keep shipping after the deadline. They will not let us ship the product after Wow, they will stop you from they'll We can't ship any product Wow.

**Dave Jones:** with Windows CE 6 after 2021. And we can't ship anything with Windows CE 7 after Doesn't this have Windows CE? Correct. Woah, what are you going to do? I can't tell you what I'm going to Okay, but Trust us that we're going to take care Well, one thing is we can currently We can switch to Windows CE 7, which is very similar to 6, okay?

**Dave Jones:** And we're looking at Oh, sorry. So, it's just a they're not discontinuing CE. It's a version difference. Right now, when they came out with Windows CE what say 8, it's not called 8. I think it's called something else, but it's different enough that we're not probably going to continue with that.

**Dave Jones:** We're going to do something different. Ah, you'll have to you think it's worthwhile to switch? Yes. Well, Microsoft does certain things really, really well. So, for For they know how to make a thumb drive driver, so it works with every thumb drive. They know how to do LAN, so it works really well.

**Dave Jones:** Yeah. But for us, what we found is that they're very inscrutable to get performance out of it. It's very large and bloated, and we don't have enough control. So, we're looking at alternatives that are more effective. Also, the processors today, when you buy them, don't come with Windows CE support. So, that costs us a very pretty penny to have support for Windows CE developed for these processors.

**Dave Jones:** Oh, you have to get them developed if you want to use a So, like for example, when you buy Windows CE support for a lot of the low-end embedded processors, it's mainly cuz we paid people like Adam Nail and others to do it, and then they get to sell it to other people.

**Dave Jones:** Ah, got it. We paid all the costs, and everybody else benefited. and they get the benefit. Not just Interesting. Um wow. Whereas today, if you get a processor, they all come with Linux support, for example. Got it. So, Linux is one of the things that we're looking at very seriously. There's a couple of other RTOSes that we're looking at for low-end products, but CE is we're looking at sunsetting that.

**Dave Jones:** It's just It's been a struggle all throughout. Like I said, there's been some good things and some not-so-good things. Um one of the things that we get a lot of negative feedback on is boot time. Yes. Yeah, it's it's important. Yeah.

**Dave Jones:** Um people accept it, but they don't like it. You know, and that's something CE has been very difficult to get good boot time. It's a differentiator. When I'm reviewing a product, if I'm reviewing a new scope and it boots up in 5 seconds, that's a wow factor.

**Dave Jones:** Yeah. Right? As opposed to analog. That's what you had. Yeah, yeah. Right. Yeah, exactly. On off and boom. It's good to go. Yep. Yep. Okay. So, you are focusing. There is some focus on that. There's absolutely some Yeah.

**Dave Jones:** focus on that. In fact, this team, when they developed this product, they took two of our best firmware guys, and they went off in a corner for 3 months, and they did a lot to optimize cuz it was over a minute when it was first developed.

**Dave Jones:** Well, yes, I remember. I got one of the early ones, I think, firmware releases, and it Yeah, and you halved it or something. Yeah. Yeah. That took two of our top firmware people like 3 months to do that.

**Dave Jones:** Really? easy. Um they could have done more, but it would require even more invasive change to the code, which would have raised a lot of risk. You can do what's called a hibernate mode and you basically take where the thing was at when you turn it off, copy it, and then reboot it like a like a laptop does. But Microsoft doesn't make it easy.

**Dave Jones:** Interesting. With Linux, do you uh use an industry build or do you find that you just have to maintain your own branch of it or something like that, so to speak? we're not we don't have any products out yet, I can't go into a lot of detail on that.

**Dave Jones:** if you had to if you had to, would if you see that You you want somebody who's going to be able to support that product and make sure that they take care of their part. And also there's some issues with licensing that you really need them to do that.

**Dave Jones:** Ah. Linux has got some strange copy issues with uh we have to be very careful about. Right. Interesting. Cuz open source code can be terrifying. You may have to publish all your code. Yeah. All your internal code, including your code.

**Dave Jones:** Including the product code. Every line of the product code. not doing that, obviously. Um but there have been some very famous situations. One of the most famous was um Linksys made a router. Yeah, it's right. and they used open source Linux, and they didn't realize that they had to publish it after it came out, and then they were forced to release all their internal code, and several people have made pretty good money coming up with modifications to their code, like OpenWRT and things like Yeah, that's right. Everyone's on that

**Dave Jones:** particular But and then it got so popular that they figured out, well, we'll make a a WRT54L, which had Linux in it so they could do that. Right. And they turned this a bad situation into a good thing.

**Dave Jones:** Into an actual product. Yeah. So Linux has got a lot of challenges with it that way. Uh there are ways through the forest, so to speak. Um it's got its own headaches. I mean, I don't think we're going to see quite the solidity of LAN and USB that Microsoft They they do more LAN and USB than anybody in the world.

**Dave Jones:** Right. Okay, cuz the PC is so many out there. Um it's going to be a challenge to go into new code space. There's things that were great, and we're going to have to make them better in this new solution, but there's other things that we're going to get when we change.

**Dave Jones:** One of the questions on the forum, a very good one. Back in the old days, when we were boys, um you used to get schematics. Mhm. In manuals. When did that trend happen in and why? Well, the biggest reason it happened was because products weren't comparable repairable at the component level by most people. When we went from through hole to surface mount was the first right.

**Dave Jones:** That's when it started to change. But the other place it started to change was when we realized people were copying our products. Ah, okay. Right. And literally you could go in and down to the component level troubleshoot. And it's we spent a lot of time and a lot of money creating very complex troubleshooting trees. We used to do things like signature analysis for the digital ICs. And you could repair a product with down to the part level.

**Dave Jones:** Today with ball grid arrays and fine pitch surface mount and and ROHS compatible solders, it's QFNs and things like that, you know, the the with the DFNs I should say where the leads are underneath the part. It's very difficult unless you have exotic repair equipment to repair parts. And we don't want to have to sell the parts. There's you can't buy some of these parts in low volume in less than 20 weeks. So But there's no obligation to sell the parts if you publish a schematic, is

**Dave Jones:** there? Well, for our customers we say it's supportable down to the component level, yes, we have to help them repair it. But why can't you just go, well, look, here's a schematic but it's it's as is. Or here's a part of a schematic, it's as is. Like we know support intended. Is that a legal thing or No, it's not a legal thing. It's a matter of creating something we think is good for our customers.

**Dave Jones:** Okay. And we think just throwing those stuff out there hurts our business, it hurts our customers because they're not getting enough guidance to be able to repair the product correctly. Got it. Right, so you think it could reflect on your reputation if you gave them the schematic and then hands off.

**Dave Jones:** Keep in mind I have to support the product everywhere in the world. We have we have support in every just about every country in the world. We are the most supported products in test and measurement around the world.

**Dave Jones:** You know, now we have to create those service manuals. we we used to translate them into multiple languages. Yeah. Okay, we had to support them. So when uh someone had a question about the schematic, they we had to answer the phone. And those costs took away from creating great products.

**Dave Jones:** Got it. And so few people today, you know, the the reliability of our products is much higher today than it was 20, 30 years ago. They don't fail as often and when they do fail, they don't have the facilities to repair them.

**Dave Jones:** Got it. much more difficult. So we don't even repair our products when they come back in many cases. We swap out a circuit And what it'll be board swap. I see. It's something everybody's changed, but you know, a lot of people complain about it because they want to repair it themselves and then I don't think they realize how much more difficult that actually is to do than they think.

**Dave Jones:** Yeah. And for the the small signal analog, if you're a trained analog engineer, I've repaired stuff without schematics. You know, you just look inside and see what's going on. you follow around and you sniff around and yep. Yep, you know, you can Yeah, follow your nose.

**Dave Jones:** or even shotgun a few parts, you can fix it. But some of the parts they're very specific, you know, selected for us and and we would have to sell them for you to repair it if you want those parts and that's very expensive to do and maintain for the huge volume of products that we make.

**Dave Jones:** What about just like theory of operation, block diagrams? We do provide some of that. You do you still providing some of that? Product to product, we do provide some theory of operation. Where we feel it benefits us in terms of creating a brand benefit where we feel explaining how we do things differently and it's good, it helps, but we we're not there to help them. We do get requests for example from a lot of our military customers demand that we provide support for repair.

**Dave Jones:** Interesting. Cuz they don't want to think about leaving their fac- their facility um and we try to work with those people specifically and we will actually provide internal documentation to key customers who make those kind of demands and we feel it's the right thing to do.

**Dave Jones:** But for general, we don't do it. How do you feel about the clones of your products? I mean, if you look at this, there's almost an exact clone from see like the the user interface. Yes. Like Edge, so much the performance of it, but well, they try and match, but the user interface is almost identical.

**Dave Jones:** Yes. What do you guys think about that? Do you just laugh and go, "Ha." No, we don't laugh. We're very upset. Oh, very upset. a lot of money and time to create this thing. A lot of the money and time today is in the user interface cuz it's one of the differentiators. And when someone copies it, they're stealing.

**Dave Jones:** Right. Okay? Yep. And we've learned, it's taken us a while to figure this out, but there's I mentioned this to Simon today at a breakfast, there are legal ways for us to protect ourselves. There's what's called a design patent.

**Dave Jones:** Yep. We're starting to use them more. You are? Yes. Well, a lot of people will be going, "Design patents?" You know. Design patents protect the way the front panel works. Yep. The way the product looks and feels. And they're actually created in China where a lot of the copying is going on, and they're very easy to prosecute.

**Dave Jones:** Right. Okay? And they're easy to prosecute in China? In China, yes. Really? I thought it was the opposite. No, China has recognized that in order to become a world-class uh economy, they've got to protect this. Interesting. We do copyright patents. We have for a long time.

**Dave Jones:** But you haven't done really design patents. So, when you did this, you didn't have a do a design patent on this. We didn't figure out that design patents were a valid thing to do until about 4 years ago.

**Dave Jones:** Interesting. Okay. So, it's a modern phenomenon, really. Well, or or you just didn't department Yeah. didn't want to do them because it wasn't effective until China passed the new design patent Got it. that they're now enforcing. And it's it's much less expensive to get a design patent than a regular patent. Both the cost of creating it and the cost of submitting it.

**Dave Jones:** Really? It's it's significantly different. Well, for a regular patent, you have to write a complete treatise on how the thing works. Right. Enough so someone else can easily copy it. Yep. And one of the challenges with a real with a not a real what do you call a the other type of patent that you're more familiar with, is that you're providing a primer for people to Yes.

**Dave Jones:** copy your design. And so therefore, one of the other challenges with a regular design a regular patent is what's called observability. If you can't observe and know for sure that they used that, you can't patent it. Cuz all you're doing is teaching them how to copy you, and you can't stop them cuz you can't prove it.

**Dave Jones:** You can't say, "I think you're stealing my thing, but I can't prove it. Uh-huh. So, we've actually we do patents where it's we it's fundamental to the feature of the product, but in many cases we don't. So, for example, our new Trueform function generators use some proprietary technology. We could not patent that because we would have shown you how to do it.

**Dave Jones:** Got it. So, you decide to keep it internally. It's effectively like a trade secret. Yeah, yeah. Okay? But, design Which is the opposite of a patent. You you either patent it or you trade secret it. No. Or or you open it.

**Dave Jones:** There's actually a few other things out there as tools for us, but the trade secret technically is supposed to be kept hidden even from people inside your company. Oh, okay. Interesting. for Coca-Cola. It has to be kept It has to be limited in who can get access to it.

**Dave Jones:** Okay. Is this for a legal reason or just because Oh, interesting. Otherwise, it's common knowledge throughout your company how to do it, then someone could leave And somebody leaves and takes it with you, and legally that's okay. That's okay. Yeah.

**Dave Jones:** Wow, okay. But, if you So, legally if you limited it within a certain team, and that person never worked in that team, and they went somewhere else, and somehow they got that knowledge, that's deemed to be stealing? Well, you think you think it out another way they can use it. Yeah.

**Dave Jones:** Right. eventually all trade secrets eventually know everybody knows what Coke's made out of now. They They hook up on one of these pieces of a what used to be Agilent. You can figure out it's got cloves and cinnamon and sugar and all those things, you know, it's not that hard to copy anymore.

**Dave Jones:** All right. Um that's the nature of trade secrets. They They slowly leak out. Yeah. Um but, all we're looking for is to keep people from rapidly copying our products. Mhm. So, a year after we we come out with a product, they've got an identical one, and of course our customers think we OEM'd it from them, which is the most insulting part of it, really. It's the exact opposite. They're stealing from us, and they think we're we're we're cheating and copying, you know, from them, which is not what we want to have

**Dave Jones:** happen. But, I have to ask about the Rigol thing. You guys were uh uh Rigol were the OEM for your scopes. Uh sorry, original design manufacturer. But, but you but you guys helped them technically I heard so the rumor goes.

**Dave Jones:** As in terms of design and manufacturing you helped them and have do you feel like you've created a monster or Well, a monster competitor or Well, I can only say that that that relationship is no longer It's it's no longer existing. Okay.

**Dave Jones:** That's all I can say about Okay. So, do you in retrospect we we all agree that we shouldn't have done what we did and we made other plans since then to do things in a different way. A better way and we're trying to different model towards with ODMs that's more effective.

**Dave Jones:** Right. So, you do work with ODMs still? What what products and can you I'm not obliged to Not obliged to say but some of them may not be key suppliers ODMs because it's it's a way for us to get more products out in less time.

**Dave Jones:** Of course. And in some cases they may have unique manufacturing technology for example for ultra low cost and it allows us to expand our scope and and get into more markets more quickly and that's something that sometimes is more important than doing it ourselves.

**Dave Jones:** Of course. Would you look at buying those companies? I don't do you guys buy many companies these days? telling Simon this morning we used to have rules when we were part of Agilent that we wouldn't buy anything smaller than a a half a billion dollars.

**Dave Jones:** Ah, interesting. So, there was a monetary figure of And the reason that was was because the cost of integrating the company in is fixed. Well, it doesn't matter if it's big or small you still have to take whatever system they have and convert it to your system. So, it cost almost as much to take a small company and bring it in as it does a big company.

**Dave Jones:** Right. And then when we realized that what that was doing and our competitors were not following this plan they were buying smaller companies Uh-huh. the we started to put much more demands on our acquisition team to be more effective in integrating into the these companies so they moved that line down because in some cases small companies have incredible technology and you don't want to OEM it from them you want to own them and keep it for yourself. So, we've purchased you know, Ixia we which is a

**Dave Jones:** big company we bought Signadyne small company And they have a key technology we need to be successful quickly, it's a great way to get going. But it puts pressure on your acquisition team to integrate their HR, their their finance model, their their benefits packages, the you know, in the case of Ixia we we bought Ixia and we're rapidly like moving people from facility to facility to cut our overhead costs without disrupting their development process. And that's something that we're very proud that that that transition is going much

**Dave Jones:** faster than it would have when we were part of Agilent, for example. Agilent they said it would take a year, it took two. Um something like Ixia I think they said it would take a year and now it's taking nine months.

**Dave Jones:** Okay, so you're moving in a towards a position where you can more cheaper and more readily acquire companies that have cool tech which you guys And smaller and smaller size. Well, now we're a pure TNM play and with TNM someone develops a new technology you've got to pay attention to that. You've got to be able to bring it into the fold.

**Dave Jones:** And in some cases there's a big company like Ixia who is, you know, the world leader in network security. And all of our products have LAN in them. And you heard about the shutdown in the US so where someone took over all the webcams.

**Dave Jones:** Yes, yeah, the webcams. Yeah, yeah. We can't tell our customers we didn't take care of that. So Ixia is a big part of our strategy to have the world's best internet security in all of our products and sell internet security technology as well.

**Dave Jones:** That's interesting cuz you don't want your multimeter to become machine. Fair enough, you know, not that there's huge volume these like there is webcams, but Right. still. Well, but it's also if you look at the the data the measurement data that's inside these things, they don't want that stuff leaking out.

**Dave Jones:** That's proprietary. That's company proprietary. If I had my multimeter and it was someone was spying inside Right, they could tell how many products you manufactured a day, for example, if they could crack that. And they don't want that information getting out.

**Dave Jones:** Yep. And there's a lot more to it, too. I mean, just going forward, internet security as the internet of things becomes pervasive is going to be more and more important to test internet security as well. Yep. So, we're paying attention.

**Dave Jones:** Is there a point to buying a company and leaving them alone? We've done that as well, but done that? less commonly. We're looking for a strategic fit that makes sense to make us a stronger overall company. Got it.

**Dave Jones:** I mean, we're not looking to just bring the cash that they make in. That's not the kind of acquisition we do very often at all, really. We're looking for things that enhance our overall company, that fit with everything else. So, leaving them alone, you know, if it's a segment of the market that's really independent, but we need to have an access to it, we might do that, but I haven't seen that yet.
