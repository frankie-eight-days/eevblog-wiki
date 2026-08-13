---
video_id: fpstmpm_rFM
title: EEVblog #1032 Part 3 - John Kenny Keysight Interview
url: https://www.youtube.com/watch?v=fpstmpm_rFM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 34, "3": 49, "4": 65, "5": 82, "6": 94, "7": 104, "8": 118, "9": 128, "10": 141, "11": 154, "12": 169, "13": 181, "14": 192, "15": 201, "16": 213, "17": 225, "18": 239, "19": 258, "20": 273, "21": 285, "22": 303, "23": 319, "24": 331, "25": 354, "26": 367, "27": 382, "28": 395, "29": 411, "30": 429, "31": 442, "32": 457, "33": 470, "34": 484, "35": 504, "36": 517, "37": 535, "38": 556, "39": 568, "40": 580, "41": 601, "42": 613, "43": 629, "44": 646, "45": 659, "46": 671, "47": 684, "48": 707, "49": 722, "50": 738, "51": 754, "52": 770, "53": 785, "54": 805, "55": 821, "56": 833, "57": 846, "58": 861, "59": 879, "60": 892, "61": 908, "62": 923, "63": 939, "64": 953, "65": 969, "66": 984, "67": 998, "68": 1013, "69": 1031, "70": 1049, "71": 1066, "72": 1078, "73": 1093, "74": 1107, "75": 1121, "76": 1135, "77": 1148, "78": 1164, "79": 1187, "80": 1201, "81": 1217, "82": 1236, "83": 1250, "84": 1265, "85": 1283, "86": 1301, "87": 1320, "88": 1334, "89": 1349, "90": 1363, "91": 1375, "92": 1393, "93": 1406, "94": 1418, "95": 1430, "96": 1449, "97": 1461, "98": 1475, "99": 1487, "100": 1501, "101": 1517, "102": 1529, "103": 1541, "104": 1553, "105": 1571, "106": 1583, "107": 1595, "108": 1609, "109": 1621, "110": 1633, "111": 1645, "112": 1657, "113": 1673, "114": 1687, "115": 1703, "116": 1717, "117": 1731, "118": 1741, "119": 1757, "120": 1773, "121": 1791, "122": 1801, "123": 1817, "124": 1827, "125": 1837, "126": 1847, "127": 1861, "128": 1875, "129": 1891, "130": 1905, "131": 1919, "132": 1931}
---

**Dave Jones:** Back to the design of these sorts of things, how big's your design team on metres? It varies. Something like a metre might be ten or twelve people, you know, three or four analogue engineers, one or two mechanical engineers and three or four firmware and maybe

**Dave Jones:** a software person. Oh, firmware and software are different. Absolutely. Oh, like software, like as in PC software you're talking about? PC software and then there's this kind of bridge gap where you have the web browser technology which is sort of a hybrid between those two.

**Dave Jones:** Ah, okay, right, interesting. And software is one of the areas that we're investing in more heavily than any other area. We just started a new centre in Atlanta, in Atlanta, Georgia and we've started a relationship with Georgia Tech and we're growing a huge software centre there to expand our standard

**Dave Jones:** software across all of our products. Got it. Because software, not everybody wants a front panel and when you do more sophisticated solution oriented measurements that have multiple pieces of equipment, you know, the front panel's not enough. Yeah. So you take a pixie system, there's no front panels and you're solving a much larger

**Dave Jones:** problem. You need software to make that really fly. Is every product going towards web browser, like a web page built in, what's the correct term? LXI requires you to have some sort of a presence on the web. Right, it does. So, because now you can go in and you can access the web page for the instrument.

**Dave Jones:** Right. So now you can control it at a basic level. One of the things that I'm working on actively is if you go through all the different products that look the same and you look at their web presence, what they come up with, it varies

**Dave Jones:** on product to product because this design team thinks this is what the web should look like and this design team thinks this is what the web should look like and this design team doesn't have enough money so they did the minimum necessary and it's not good for our

**Dave Jones:** customers. Yeah. Okay. We've had cases where we went overboard and spent over a million, two million dollars on our web interface. Wow. Yeah. And it's amazing, but we could have done it with a software package for a third of the cost. Got it.

**Dave Jones:** The only reason they like it in the web is that the field engineers don't have to install the software before they demo it for the customers. Correct. They can just go on their phone and go straight to the web address. Yeah, that's not a reason to spend two million dollars.

**Dave Jones:** Yeah. Okay. And the problem is everybody thought the web was going to not have to be updated. The web was always going to stay the same. Well, you can't get Java, can you? You can't get Flash, can you? So it hasn't worked out to be as good and it's evolving just like every other part of

**Dave Jones:** the PC is evolving. Yep. So it hasn't been this zero maintenance thing we thought it was going to be. So we're pulling the web back to more of a common level that's going to be more standardized across our products and more rapid for us to deploy more easily.

**Dave Jones:** Still give you the local control over the web, which people want, but not as full blown as some products have done. And it's not as stripped down, which is not good enough for some other products. I mean, one product we make, the web control consists of a window you can type Skippy commands.

**Dave Jones:** Yep. That's not very useful. That's, well, it's, yeah. It meets the LXI standard. The hardcore guys cheer, but yeah, apart from that. Well, we still, that's an easy thing to integrate, but that's all the integrating, you know. Right. It meets the LXI standard, but that's about it.

**Dave Jones:** Most of our products we're trying to standardize on, it's where you have a view at the front panel and you can press buttons and the display looks just like the front panel. And that turns out to be, for most people, they just want to remotely control the product

**Dave Jones:** and verify that it's doing what they expect it to do. So that's what they expect. They expect to see something like that in the future. Well, no, there's a group of people who want it, because the web is a giant CRT, you can

**Dave Jones:** do much more than you do on a limited size front panel. And you can even add additional level, high-level constructs that you wouldn't put in the product because it was hard to use on a small display. That's the area that I think there's more debate, can we do more of that?

**Dave Jones:** And my feeling is, from an efficiency standpoint, let's get everything common and then let's move the whole thing as a phalanx forward and make it better, more efficiently. Instead, we have some groups going all the way to here, some groups going to here.

**Dave Jones:** It just doesn't lend itself toward efficiency. What really frustrates me is, we have a concept, the name that Ron came up with in the management staff called One Keysight. We want our customers to have a consistent One Keysight experience across all of our

**Dave Jones:** products. That's as important as any one product. So we're really trying to... We're a bit cynical, us engineers in the market, in that we think that's a bit, you know, that's a bit corporate-y, silly. But if it wasn't there, you'd probably miss it.

**Dave Jones:** It's probably under-appreciated by us engineers. I think most people, if you talk to them, if they own an Apple product, Apple's the master of that one Apple, if you will, that they have that consistent... Now, that doesn't mean Apple's perfect. There's lots of areas that there's issues with Apple's implementation, but for the most

**Dave Jones:** part, it makes people brand loyal and they do have a consistency and a quality to the experience that they're very big on. I'm not saying that we're trying to clone Apple, but we are trying to take some of that same shared experience and make it more consistent.

**Dave Jones:** So we'll find this user interface on most of your benchtop products like this? We have a box coming your way with the new E36-3, 11, 12, or 13, I don't know which one they're going to send you. And there are screens on that that are identical to the screens on this.

**Dave Jones:** For things like setting up the LAN, things for setting up the file manager, you know, why have different experience on each one? It's a file manager, you know? And that's something as an example, but we literally have four or five different implementations on this exact screen because it was developed here versus here versus here.

**Dave Jones:** That's not acceptable anymore. We're paying for something three times. I know, of course. Yeah, that's crazy. And our customers hate that. Yeah. They learn how one works. No, I don't. Yeah, I want to be able to use the same. I expect the same interface.

**Dave Jones:** And you're not getting it today. Yes. But that's being worked on. Absolutely. Excellent. How quickly can you spin fixed firmware issues and things? If someone reports a firmware issue on a product, what's the mechanism to fixing that? If a firmware issue comes up, the hard part is getting it to the people who can fix it.

**Dave Jones:** Because we're a big company, it typically goes to our support group. The first thing they have to go is to evaluate if it's truly a mistake. And sometimes that communication takes a while. This is not the customer who wants to just sit on the phone on hold waiting for the support

**Dave Jones:** person to describe it and document it. That can take the longest amount of time. When it gets to the design team, depending on how hard it is to fix the bug, that can take a couple days. It can take a couple weeks. If it's a case of a memory overflow that only happens on a rare occasion, that's the hardest

**Dave Jones:** thing to catch. That might take two, three, four weeks to catch it with its pants down, so to speak. Once you find it, it takes very little time to fix it. And then it takes typically a week or two to guarantee that we didn't break something

**Dave Jones:** else. We do exhaustive testing before we ship a firmware update out. The worst thing you can do is fix it and bring something else. That delays us getting out there. We have very, very thorough regression testing. Even that doesn't have perfect coverage, so we'll pass it around to other people to make

**Dave Jones:** sure we didn't break something else in the process. Is that an automated testing? Do you have automated tools in place to exercise all these functions remotely and just go through every possible combination of implementation? We do for the buses, all the different buses, GPIB, LAN, USB.

**Dave Jones:** Front panel is very difficult to automate. You can use vision. Yeah, but you can push the buttons from the LXI. You can push the buttons, but you actually have to look at the spot, you have to look at it. And with vision systems, it's very complex and time-consuming to program vision systems

**Dave Jones:** to simulate all that stuff and catch it. Okay, so it's different. Someone still has to look at how is it different and figure out what that means. There's no artificial intelligence to make all that happen. Front panels are probably the biggest headache when it comes to automated testing and catching

**Dave Jones:** things. But the bus stuff is much more amenable to automation. Also though, a voltmeter, you're measuring voltage. We have to make special fixtures that feed different reference signals in of different types. And actually the hardest one, believe it or not, to write regression is power products

**Dave Jones:** because you have both sourcing and loading and measurement and different types of sequencing. So for example, most of our power products have the ability to put out sequences with different time delays and all that, so that can get very complicated in regression testing.

**Dave Jones:** So the 3458A, there's rumours that maybe a new one's in the works. Are you still going for those sort of, you know, the top of the line Cal Lab type instruments? Is that still on key sites? The 3458A is one of the most revered products in our history.

**Dave Jones:** Today it has not been eclipsed by anybody for absolute performance. We know that's really important and we will not let our customers down. Okay. That's about all I can say. It's being worked on. I didn't say that. It's being considered. We will not let our customers down.

**Dave Jones:** You will not let your customers down. Well done. All right, with old products like that, I mean, how long has that one been around? As long as the 34401, they were released within a few years of each other, mid-80s, late 80s. Yeah, 20, 30 years.

**Dave Jones:** It's been a while. Wow. Do you, have you lost, I mean, clearly you're going to lose talent if people know, like, at a high, at such high end, there's so much subtle magic in there that, So I actually managed the two guys working on that the first time we tried to do a replacement on it.

**Dave Jones:** And it was fascinating for me to learn the kind of subtleties they have to go through on that. And I learned a great deal about, you know, high-end voltmeters, managing those two guys. Both those two guys are still with the company. They're still with the company.

**Dave Jones:** Now, the four guys, the four horsemen that developed the original 58, none of those four guys are still with the company. One of those four guys is one of our biggest competitors that makes TMS. Right. And he's an amazing engineer that we lost.

**Dave Jones:** We were very unhappy that he went to the dark side. And he's still developing with them. He's still doing quite a lot of good things for them. The 58 has some of the most challenging aspects to it, the subtleties of that. One of our R&D managers who was running the group at the time came over,

**Dave Jones:** the four guys were still with the company, had a handkerchief laying over the circuit board when he was testing it. He says, why are you doing it? He says, because the subtle differences in the air temperature going over some of the parts were moving a tenth of a degree and it showed up as noise.

**Dave Jones:** You could see it. You could see it. You could see the fluttering of the air on top of the parts. It was changing the DC measures. So is it hard to say you've still got some talent? Oh, yeah. Well, the R&D manager that managed those four guys is still with us.

**Dave Jones:** All right. And he's busy, and has been busy, training a younger guy. He's been there 15, 18 years. He developed the 34. Oh, I was going to say, yes, some of them apparently went into this. Yes. And both of those guys are still with us and we're looking at how we can take that to the next level.

**Dave Jones:** Kind of do it even higher. We have a 7.5 digit model now and the 7.5 is very close to 58 performance. Wow. I mean, in some areas. We know some of the stuff we'd have to do to upgrade it to that next level.

**Dave Jones:** So we came very close to having a completely new 58 design. But part of the challenge with our old management team was they said, you're just replacing the revenue we had before. There's no growth in that. There's no new profit in that. And we were part of the life sciences cash cow.

**Dave Jones:** They didn't want to spend money. Now that we're a test and measurement company exclusively, there's a lot more willingness to be having a premier product in our catalog that we understand. Got it. And that's one of the great things about being a pure test and measurement company,

**Dave Jones:** is we're much more focused on what matters. The reference inside this and others, are they getting difficult to get? No. No? So that's an interesting story. The reference that's inside the 3458 was developed by us 30 years ago. And we came to the conclusion that we're not the right people to make it.

**Dave Jones:** So we gave the design to linear technology. This is the RTZ1000? Correct. OK, you guys developed it. We developed it and we gave it to them. We have a big burning system in our factory that we mount them in little boards and we burn them in.

**Dave Jones:** And we sell graded versions of it for better results. Now the 7.5 digit on this one uses the RTZ1000. It's one of the things that allows us to get to 7.5 digits because of the drift. This doesn't have all the hooks that a 58 has.

**Dave Jones:** It doesn't have the level of A-Cal. It doesn't have the AC measurement technology that's unique on the 58. All of that stuff is more straightforward. We had already started to work on redesigning that. And stay tuned. We're in the process of looking at how to take things to the next level.

**Dave Jones:** But there's still a lot of new measurement technology that can be done. A voltmeter is a fundamental building block for a lot of what we call synthetic measurement technology. And we're looking for how we can grow into other measurements. One of our competitors down in Texas does a great job.

**Dave Jones:** All they do is synthetic measurements. Their granularity is a little card about this big. They pop into a frame. We have focused on the standalone. They've focused on that. There's a significant opportunity in that area for us. And we think you're going to see more of that over time.

**Dave Jones:** Interesting. What sort of volumes would those high-end instruments sell at? I wouldn't imagine there's... How much would they have to sell for to make it worthwhile? All the years and years of developing such a high-end product with such a limited market. Which is basically Cal Labs.

**Dave Jones:** It's not as limited as you think. One of the bigger opportunities for the 58... It's kind of surprising. When you look at high-volume consumer products, throughput is a huge factor for these people. The voltmeter, even if it's a $10,000 box like the 58,

**Dave Jones:** it's the cheapest piece of equipment in the rack. You start putting a spec in or a high-end scope, something like that, it's $30,000, $40,000. And you've got material handling equipment trying to move this stuff in and test it in a few seconds. You put an 8.5-digit voltmeter in that system,

**Dave Jones:** you don't have to change ranges ever and you still get an accurate reading. So it's much faster test throughput. Much faster test throughput. You don't have to change ranges. You can lock it on a 100-volt range no matter what signal comes in, you get an accurate reading.

**Dave Jones:** On a 6.5, you might have to change ranges. And that takes time. And it slows down your product. That's right. We have some people using the 58 for its throughput benefits. We have other people who build large multi-base systems. They put a 58 at the bottom of the rack

**Dave Jones:** because they want the system to be robust. And we sell into military aerospace. It's a very popular configuration. So it's not all just CalLabs. In fact, frankly, CalLabs, we've lost a lot of that business to our big competitor in Everett. Got it. They've really taken over a lot of the Cal.

**Dave Jones:** They're really focused on Cal as a big deal. We get less of that than we used to get for sure. And these other things, this kind of transfer standard where they mount it in the rack, they just calibrate the 58, and it calibrates everything else.

**Dave Jones:** Got it. And because it's so accurate, that works. You might have one of these. They might have some pixie cards, some other things, a function generator. The 58 has incredible RMS AC measurements. It can verify all those things in the rack. They just route everything through it.

**Dave Jones:** It does a confidence check and a calibration. And it's less expensive and smaller than the other competitor's product. Can we expect to see an 8.5-digit bench one like this rather than a rack? I mean, if there's benefits to throughput, I mean, 7.5 digits is almost there.

**Dave Jones:** But if you can get the extra... I don't know exactly what would do that. Might matter. That's an interesting question. I don't know if there's as much benefit to having it on a bench where you're dealing with data on the front panel. Right, yeah.

**Dave Jones:** It's more automated system rack stuff. Again, the AC measurement technology in the 58 is something that has a lot of benefit in a standalone like this. That kind of technology for it. But the pure 8.5-digitness, there was a lot of debate to do a 7.5-digitness format.

**Dave Jones:** Okay, interesting. We fought that battle over and over and finally people said, how much will we get out of it? They said, the technology is so common, we think we can do it fairly quickly. It's one of the tricks. If you can make the effort low,

**Dave Jones:** people stop arguing with you. When they have a 58 replacement, they really argue down to the bone and it took a lot less time because they planned for it. Oh, so when you're first designing this, you thought maybe we might do a 7.5

**Dave Jones:** or did that come later? They knew the 7.5 was on the roadmap. We knew it was coming. They didn't lay out all at one time but still because we had the front panel and we had all the other pieces, they could do it with a lot less resources.

**Dave Jones:** So instead of having a team of 12, I think it was a team of 4. And Yemi did it 10% of his time engineering the 7.5 digit measurement solution. Everything else is the same. So it was a lot quicker, a lot smaller project team

**Dave Jones:** and there's a follow-on and even all the marketing literature and documentation was reusable. All the screens are the same. So the firmware was minimal change. Got it. Do you laugh at the competition that try and do 6.5 digits and their specs aren't even close?

**Dave Jones:** We never laugh at anybody. Do you remember the Chinese competitors getting there? I think the biggest mistake we make is to ever underestimate our competitors. You were talking about this this morning. In the US, Toyota and Honda came into the US market with terrible, terrible inexpensive cars.

**Dave Jones:** So did Hyundai. And of course now they produce the most reliable. And they're the largest selling car in the world. Hyundai is the fastest growing car company in the world. Ignoring your competitors, big or small, is always a mistake. Being arrogant was a big mistake we made for many years.

**Dave Jones:** And it's something that will not be repeated if a few of us have anything to say about it. You don't get to be the best and then get arrogant. You won't stay the best for very long. One of the things I really was happy to

**Dave Jones:** be able to do this with you is to kind of shift in how people learn about products. One of the things I tell people so for example, we developed the 36, 311, 12 and 13. I recommended that all the projects on the project team

**Dave Jones:** go to your blog and read about all the things you did on Google and everybody else. All the criticism, all the vitriol. But all the things they get right too. I always tell people, I don't want to know what they got wrong. I want to know what they got right.

**Dave Jones:** I want to learn what they figured out that I can use. Steve Jobs said art is steel. I look at something, what you provide to the industry is much like a movie critic. You save me from watching bad movies. At the same time,

**Dave Jones:** you teach me what to look for and what the craft of a great movie is. We really appreciate what you bring to the market and the fact is you're much more accessible than those millions of customers that you represent. It's something that as we've tapped in more to social media

**Dave Jones:** we think that you are really a valuable resource for all of us in the test and measurement industry. You make our industry a better industry for it. You are an objective purveyor of how good products are. I think you're going to make all of our products better.

**Dave Jones:** You're going to make their products better and you're going to make our products better. That's the intention. That's something that I think is really exciting and a little scary too because we don't have any control over it. From that standpoint, it can be a little frightening.

**Dave Jones:** I did not come to this today without a little trepidation. You've got to take the hits. If your product fails, the Mina for example, you remember the 1272 meter and there were soldering issues and they've gone through. I like to think that people value

**Dave Jones:** the response that you give. If you just ignore it, they're not going to give. Say, hey, we admit it's a problem, we're working on it. Everyone's going to think better of the company. There's an old cliche that it isn't what you do when you fall down

**Dave Jones:** it's what you do when you get up. To us, what you bring to the market is really an invaluable resource that makes us better. You can harness that and get a perspective because when you say what you say, if your readers don't agree with you,

**Dave Jones:** we read that too. It really helps us create a perspective that would be very difficult for us to get any other way. You're actively looking to be on the forums and in an official company? We have all of our project team members I demand that they read all your forum stuff

**Dave Jones:** on all the products that compare to our products. We also buy all of our competitors' products and tear them down. First, we evaluate them in a black box way and we've instituted a practice where each of the engineers on the project has one of our competitors' products

**Dave Jones:** and they actually have to use it during the project on the bench. Every few months, we sit down and say, what do you feel now? Some things that they got really right we try to incorporate them in our product and we try to say, how can we do it better?

**Dave Jones:** What don't you like about it? Did we end up tripping into that and doing it the same way? Let's move the bar up. I think you've helped make that possible. Fantastic. That's how we're going to stay ahead. We have some interesting stuff in all the different products.

**Dave Jones:** One of the ones I find the most amazing is what we call Trueform. Trueform is really a trade secret that I can talk around without giving the trade secret. If you look at a traditional DDS style function generator, DDS is great because it's cheap

**Dave Jones:** but it's got all sorts of problems. It's got jitter, it doesn't work well for other types of square waves, for example. Square waves are horrendous with jitter in DDS technology. Trueform has allowed us to dramatically simplify the structure of a function generator. I don't know if you're aware,

**Dave Jones:** they would not generate square waves with a DAC. They would generate a triangle wave and they would run that into a comparator. No, no, no. You would have a limited two or three different slew rates and you would have a 10% minimum duty cycle.

**Dave Jones:** Now with Trueform, you can get less than 1% duty cycle and you can get infinitely variable slew rates. That makes the product so much more usable on your bench. We're actually looking at how can we take that technology and integrate it in more and more

**Dave Jones:** products because it is so, so much better for testing and use. It's one of those things that when we first did it, we learned about it from the RF guys because they're trying to create spectral purity with their waveform generators and that's what they focused on.

**Dave Jones:** This is one of these that I didn't get involved in but it kind of showed what could happen. One of our guys from the team that develops function generators actually went to California to our RF site and learned about it at a lunchtime conversation.

**Dave Jones:** Right. He was smart enough to realize what it could mean for function generators and brought it back. It takes a ton more FPGA. In fact, in our 120 MHz part, we actually had to do the waveform in pipeline in 4 paths because FPGAs don't want to run past

**Dave Jones:** about 250 MHz. We couldn't afford an ASIC because the volume on the high performance one is lower so he actually figured out a way to pipeline the whole thing in 4 paths and then mix them all together with a delay line at the end.

**Dave Jones:** It gives us just an incredible benefit and some of our competitors have picked up a little bit. I was going to say, Siglin they do one that they claim is innovative. Is that just a copy? No, it's not a copy because there's nothing to copy.

**Dave Jones:** We don't tell you what we did. But the intention is that they copied it. What they've done is a much simpler version that is not as sophisticated. It's a good solution. It's not as good as what we've done. This allows you to generate small

**Dave Jones:** duty cycles in a large memory. What Siglin has done I believe is just basic interpolation. What we've done is much more sophisticated than interpolation. It's much lower distortion, much lower jitter, much more fine grain. And we're not telling them what we did because once we tell them, they can do it too.

**Dave Jones:** Although it was interesting, like I said, in the high frequency function area, once they knew how to do it because they did it on the lower frequency one it's just one path. The hard part was putting it in a giant FPGA and figuring out how to do 4 paths

**Dave Jones:** in parallel and line them up at the end. That was really pretty tricky stuff. But that's the kind of stuff when you say digital, I don't think we've even really come close to fully fleshing out all the things we can do digitally to make test and measurement equipment

**Dave Jones:** even better. I mean, I think the scopes that they're doing spec-ans now, that's an example where they say, hey, what's the difference? And we're doing more and more and more of those kind of things. What you're going to see next is you're going to see where, if you have

**Dave Jones:** 2 voltmeters in a function, you have a low frequency network analyzer. Yes, that's right. But you can't do that today very well. No, it's a bit clunky. You can't synchronize the 3. But there's no reason you can't. In PXE you can do it, but then you don't have

**Dave Jones:** the positive user interface. You don't have it all linked together. So there's a lot more to come. How would you link them in a technical aspect? Would you link them through the network interface or does it have to have a dedicated physical digital port in between?

**Dave Jones:** We developed a technology called IEEE 1588 many years ago. We actually developed it in our labs and then gave it out to the world for free like we did with GPIB. 1588 is time sync over land. Right. And it's used for video. It's used in everybody's house.

**Dave Jones:** They don't realize it. It's used for how they do streaming video in your Apple TV and stuff and how they distribute streaming video in the cable companies. And Keysight? Agilent? It was developed as, I think, Hewlett Packard. Oh, that was HP. It's been around a long time.

**Dave Jones:** Wow. It was one of those deals when we did GPIB you have to pay a dollar to get a license I didn't know you were out there. I was a little bit miffed when I found out how much we gave way on it, but it's now built into all the

**Dave Jones:** microprocessors and layout stuff. We've developed a method to take it a step further. We combine it with an FPGA and we can get Pico second level synchronization with 1588. Over the network? Over the network. Wow. Okay. How do you get Pico's... Is that another trade secret and you're not going to tell us?

**Dave Jones:** It's another trade secret. Damn it. I can't tell you. But it's pretty amazing stuff that the labs guys have come up with. The problem with 1588 is if we just put it in our products and told you, you figure it out, it would be so complex they couldn't.

**Dave Jones:** It's really difficult. So you need the application layer to do it? You need the application layer to do it and frankly one of our weaknesses as a company is our software has not been up to snuff. Hence your new... Right, so now we're renewing our focus on software

**Dave Jones:** and really putting a lot of money and time into software so we can start getting out some of these higher level solution focused. The big term in the company today is solutions not hardware. Got it. Software not just hardware. It's hardware, software and people make solutions

**Dave Jones:** and that's really what it's all about. That's what I was doing the other day I was characterizing the power supply on the bench and I wrote them all down by hand because I couldn't be bothered figuring out how to automate them. They've all got

**Dave Jones:** LXI connectivity and everything else. I'm not going to... But if there was a solution that I could just download from the website, oh, just tie these together and it just worked, yeah, I would have used it. It's going to take us a while to fully

**Dave Jones:** flesh out that outcome but that's the path we're on. There's no question about it. That's really where we're going because that's the kind of problems that people face today. They don't have time to figure this stuff out. You know, you look at the emergence of IoT

**Dave Jones:** and 5G and some of these new emerging technologies, there's going to be more electronics in everything you own. I mean, everywhere you turn, from when you walk in the room, the lights turn on because there's a sensor that senses you coming in and

**Dave Jones:** all that, that's just the beginning. There's so much more that's coming with all these new emerging technologies and they just don't have the time to do it the old-fashioned way. And they're often non-engineers doing design. That's a really good point. They're gluing together Arduinos

**Dave Jones:** or Raspberry Pis and stuff like that. And they're doing amazing stuff because they're using all this off-the-shelf hardware and software. But how do you characterize that stuff in more complex ways and that's really the challenge for us is to create higher-level integrated solutions

**Dave Jones:** with multiple boxes to make it happen. And it's a huge challenge because it forces us to stop being little sites that develop independent products and start creating one key site. And that's why our management team has really shifted investment focus dramatically toward the software, toward the solution side.

**Dave Jones:** Even to the point of how we market and sell our products, we now have what we call solution teams and centers of excellence. And I'm responsible for a third of the company as the technical side of centers of excellence. And my boss is the manager for all this group.

**Dave Jones:** And we have four solution teams tied to key industries. So we have one automotive and energy group. We have one general purpose and education group. We have a wafer test, semiconductor test and board test. And those groups just focus on solutions in those industries.

**Dave Jones:** And automotive is I think one of the most fascinating ones because let's face it ten years from now you're going to be reading a book where the car takes you where you want to go. That's only a matter of time until that self-driving vehicle.

**Dave Jones:** And the technical challenges behind autonomous vehicles are just, it's off the charts crazy. Google and other people are doing these self-driving vehicles that they map everything out. You know what they're finding out? They're finding out that it don't work so good. When it's raining, when there's

**Dave Jones:** construction, solving those problems is incredibly difficult. And relying on networks to go back to central computers. I was driving across Sydney now that Sydney is impossible to drive in at the best of times. Which is terrible. But I was driving home at night

**Dave Jones:** it was torrential pouring rain and it was construction everywhere. They're chopping and changing lanes on a daily basis. And I went no, like this is just a nightmare from a self-driving car point of view. It's just terrible. And they know that. But they still, this is an

**Dave Jones:** enabler for them to sell you an even more expensive car or even, you're going to rent time on a car. The car is going to get so expensive we're not going to own them. How do you feel about a car that the other guy didn't put air in his tires?

**Dave Jones:** When you're driving at 200 miles an hour in an autonomous driving lane. So a lot of things are going to change in ways that I don't think people are ready yet for. The technology that's going to emerge, because that's what people want, is going to be crazy.

**Dave Jones:** Do you think it's going to take longer than most people think? Because everyone's talking, oh yeah it's going to be here like that. I think in limited areas it's going to be sooner but I think it's going to take longer to get all the

**Dave Jones:** bugs worked out. One of the things they're talking about now is that they probably have to put transducers in the road. Oh yeah, now once you get to that level it's... Well they're going to turn, the HOV lanes are going to become auto driving lanes.

**Dave Jones:** That's going to be the first place they're saying you're going to see it. They're going to repurpose the HOV lanes and you're going to pull into like a gating area with an entrance ramp. The car is going to stop and then it's going

**Dave Jones:** to pop you in it. Right. You're going to be tailgating the car. Got it. Right. So you break the wind barrier so you get efficiency at higher speeds. It'll be like airplane crashes. When an accident happens a lot of people are going to die but it'll happen very infrequently.

**Dave Jones:** Very infrequently, exactly. That's going to be one of the most amazing transformations that's going to change everything we know but even the way that electronics is in our lives, one of the things that we've been looking at is counterfeiting. Right. You know, Ray-Ban sunglasses.

**Dave Jones:** Oh yeah, yeah. 60% of all Ray-Bans are counterfeit. Wow. So they're talking about putting electronic chips in every pair so that they can tell if it's counterfeit. Yep. But then they can just copy that as well. It gets harder. They're trying to be one step ahead.

**Dave Jones:** That's right. Yeah. Is there a point where that one step ahead thing just, you may as well, you're better off giving up and just figuring out a better way to do it? Well, how do you feel about taking medicine when it's fake? Yeah, no.

**Dave Jones:** Let them give up, right? No, no. It's true, well played. Pacemakers. Right. I don't need an artificial pacemaker, but it's fake. Yeah, okay. You know, so there's some security issues that you may not want to ever see a fake, but there's problems in that area too with drugs

**Dave Jones:** and food and, you know, they're talking about putting, you're going to get meat and it's going to have a tracer in the meat. And you're going to swallow it and you're going to take it out the other way and that's what's going to happen.

**Dave Jones:** It's insane. Yeah.
