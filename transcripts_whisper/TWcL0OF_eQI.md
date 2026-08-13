---
video_id: TWcL0OF_eQI
title: EEVblog #754 - Altium Circuit Maker First Impressions
url: https://www.youtube.com/watch?v=TWcL0OF_eQI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 36, "3": 54, "4": 80, "5": 100, "6": 115, "7": 130, "8": 152, "9": 168, "10": 188, "11": 203, "12": 218, "13": 233, "14": 250, "15": 263, "16": 285, "17": 307, "18": 320, "19": 341, "20": 359, "21": 376, "22": 397, "23": 418, "24": 435, "25": 455, "26": 472, "27": 495, "28": 512, "29": 531, "30": 550, "31": 566, "32": 583, "33": 599, "34": 615, "35": 630, "36": 652, "37": 667, "38": 685, "39": 703, "40": 726, "41": 746, "42": 769, "43": 789, "44": 803, "45": 822, "46": 843, "47": 861, "48": 879, "49": 896, "50": 925, "51": 953, "52": 977, "53": 994, "54": 1010, "55": 1028, "56": 1048, "57": 1068, "58": 1085, "59": 1102, "60": 1121, "61": 1134, "62": 1149, "63": 1164, "64": 1177, "65": 1197, "66": 1214, "67": 1230, "68": 1248, "69": 1267, "70": 1280, "71": 1297, "72": 1315, "73": 1330, "74": 1343, "75": 1361, "76": 1377, "77": 1396, "78": 1414, "79": 1431, "80": 1446, "81": 1460, "82": 1474, "83": 1487, "84": 1504, "85": 1521, "86": 1537, "87": 1555, "88": 1571, "89": 1584, "90": 1601, "91": 1615, "92": 1631, "93": 1646, "94": 1664, "95": 1679, "96": 1696, "97": 1709, "98": 1725, "99": 1741, "100": 1755, "101": 1769, "102": 1784, "103": 1798, "104": 1816, "105": 1831, "106": 1846, "107": 1862, "108": 1877, "109": 1890, "110": 1908, "111": 1930, "112": 1943, "113": 1959, "114": 1973, "115": 1991, "116": 2011, "117": 2025, "118": 2043, "119": 2061, "120": 2077, "121": 2091, "122": 2106, "123": 2123, "124": 2138, "125": 2152, "126": 2165, "127": 2183, "128": 2197, "129": 2213, "130": 2232, "131": 2248, "132": 2264, "133": 2278, "134": 2291, "135": 2305, "136": 2317, "137": 2336, "138": 2352, "139": 2368, "140": 2381, "141": 2397, "142": 2413, "143": 2427, "144": 2442, "145": 2460, "146": 2475, "147": 2489, "148": 2507, "149": 2523, "150": 2541, "151": 2556, "152": 2571, "153": 2588, "154": 2604, "155": 2622, "156": 2640, "157": 2656, "158": 2671, "159": 2689, "160": 2707, "161": 2720, "162": 2737, "163": 2753}
---

**Dave Jones:** Hi, I've had a lot of requests for this video to take a look at the new Altium Circuit Maker software that hasn't actually been released yet, but it is in open public beta, so you can actually download the thing and check it out and actually use it for yourself.

**Dave Jones:** But yes, it is still in beta, so bear that in mind. Now, as many of you will know, I used to work at Altium. I worked there for about four years, but I've been using Altium slash ProTel since about the mid to late 1980s, so I'm a longtime loyal user of it.

**Dave Jones:** And just like every single loyal Altium customer, I have a love-hate relationship with them. And yes, I did do that video about what they should do when they release this free version, so let's take a look at what they've done, shall we? By the way, if you haven't seen my previous video, linked in down below.

**Dave Jones:** Now, first of all, Circuit Maker Altium have actually bought back an old product which they bought. They used to sell a product called Circuit Maker 2000, and I actually liked Circuit Maker 2000. It had quite a good simulator in it, and I used it for quite some time as a simulator, but no, the new Circuit Maker has absolutely nothing to do and shares no code with the original Circuit Maker 2000.

**Dave Jones:** And while Circuit Maker does share code from the full Altium Designer product, it is actually a completely different beast. Now, my biggest recommendation is that they should have a completely free version, just like Eagle do. Well, they have a limited restricted version, and just like many other companies out there, have a free version of the tool.

**Dave Jones:** Have they done that? You bet your ass they've done that. In fact, they've gone a lot further than what I thought they would, and they've released everything for free. This is not a crippled version, there's no layer limits, there's no size limits, there's no limitations whatsoever.

**Dave Jones:** It's a full, like professional level, although that remains to be seen, PCB level package with no limitations whatsoever. Except for a couple of little gotchas which we're going to take a look at, but you do get everything. It's a fully functional tool, not crippled at all.

**Dave Jones:** Awesome, got to give them huge props for that, big thumbs up. This is different to what I originally got as a preview back before they started doing anything public with it. Well, their original intention was to have, just like Eagle, to have a crippled free version of the software.

**Dave Jones:** And you could actually pay some money to like, you know, for example, upgrade it to four layers or eight layers. You could pay a small amount of money, it was, you know, like sub $50 or something like that, to increase the size of the board, for example, the number of nets or whatever.

**Dave Jones:** They hadn't actually finalized it, but that was their original approach to actually doing CircuitMaker, which didn't have a name back then, but they completely abandoned this and went, well, if we're going to make it free, we're going to make everything free. So they've given you the whole thing, no strings attached.

**Dave Jones:** Now, whilst I did really think that their original concept for having a free version, plus some really realistic, affordable paid options to increase the capability of their product, I thought they were on an absolute winner there, and they would have taken the market by storm.

**Dave Jones:** But I can understand why they've gone for the completely free approach and given it away. Now, here is the big trap with this thing. Yes, it is a professional PCB design tool. Yes, it is completely free. They don't charge you for anything at all.

**Dave Jones:** There are no optional extras to buy on this thing. But the catch is, while it's a program which runs local on your machine, it is cloud and community based. That is their focus. They want to develop a, have a free PCB design tool

**Dave Jones:** that the entire open source hardware community can get behind and use. And, well, okay, it's a very noble cause. And I've got to give them props and huge thumbs up for attempting to do this. It's awesome. And just before we have a play around with it in general,

**Dave Jones:** I thought I'd just go through a list of pros and cons up front here that I've basically found in my initial impression of this thing. The main one is, of course, it is completely free. There are no layer restrictions, size restrictions, anything else.

**Dave Jones:** It is a full professional PCB package. It's got the, you know, the famous Altium 3D view and all that sort of stuff. It's, you know, basically as, pretty much as fully functional as the regular Altium software. It may not be as productive as the regular Altium designer software,

**Dave Jones:** but it is basically, uses a majority of Altium's advanced PCB design technology. So it's fantastic. No limitations there whatsoever. And it's got collaboration tools as well, which I'll go into so you can set up teams and things like that and have multiple people working on your projects and stuff like that.

**Dave Jones:** So I can go into my project here and I can add people to my team and they can see my projects and have multiple people. That's actually great for open source hardware projects, which it's like community-based projects, which this thing is specifically targeting.

**Dave Jones:** It's got version control and forking. It uses Altium's own online Git type, you know, repository with releases and you can fork it and, you know, do all that sort of jazz. I don't believe it's compatible with like Git or anything, other third-party version control tools.

**Dave Jones:** I think it's all just Altium built in. So it's a community-based tool and it can import a few different formats, but the two important ones are Altium and also DXF, which is rather important for loading in things. As we'll see later, I've loaded in the Arduino UNO files here

**Dave Jones:** directly from the board and it hasn't done a terrific job, but it has worked, like it didn't throw up any errors, so it at least gets you started. So that's awesome that it can import Eagle and a few older Altium designer formats. And here are the downsides to it.

**Dave Jones:** It requires an internet connection to make the thing work. You cannot start the thing or otherwise work on your projects without an internet connection. That may be a showstopper for a lot of people right there. So if I actually try to start CircuitMaker, it will load.

**Dave Jones:** Here we go. But look, I can't see without an internet connection. I've physically pulled the ethernet plug from my internet connection and look, we just can't do anything. I can't see any of my projects, can't see my account, can't see, can't do a damn thing.

**Dave Jones:** So much for being able to work on a plane or a bus or something like that. That's a killer. The next major disadvantage, of course, being cloud-based like this, you can only save your files on the cloud. Now granted, it does actually save the actual, look,

**Dave Jones:** the .sketch.files and things like that locally. So, you know, they are technically there. But yeah, so you can back them up yourself if you really wanted to. But essentially, it doesn't let you work from these local files. And the other thing is it uses a completely different file format

**Dave Jones:** to Altium Designer. And you cannot import Altium Designer or Circuit Studio files. So yeah, they'll probably, they might add that in the future. You know, it just seems stupid that you can't do that. But I can't. I would have loved to have loaded in some of my big Altium Designer

**Dave Jones:** projects that I've got, but I can't do it. It just doesn't support their own other products. Unbelievable. Now because this is a completely free tool designed for online collaborative open source hardware projects for the, you know, maker community, etc, etc. They pretty much are forcing you to make all of your projects and files public.

**Dave Jones:** And I thought this was a really horrible limitation at first, but it turns out it's not. It's actually better than what you think. Because if you go in here and you actually start a new project. So let's go in here and new project.

**Dave Jones:** And we actually get the choice to actually do a sandbox project, i.e. keep it all private. And I believe that you can, I haven't tested this yet, but you can collaborate with other people privately on that project. And if you've only got one or two projects,

**Dave Jones:** then you don't have to share any of your information with the public at all. You can keep them private forever. So that is good. But they only allow you two sandbox projects, and you can't do any, i.e. sandbox being private projects. You can think of them like that.

**Dave Jones:** You can't do any more than that. If you want to do that, then you have to release one of your sandbox projects to the public, and you can only work on two private projects at a time. It's actually not a bad limitation, given the market that they're trying to reach here.

**Dave Jones:** So it would have been absolutely horrible if you had to make every crap edit and everything you did public before you actually released the project. That would have been awful. But they've thought about it, and that actually works reasonably well. So I think that's not a bad compromise.

**Dave Jones:** So, for example, I've got two projects, which is an Arduino Uno that I imported from Eagle Files, and I have actually released that publicly. But I've got a test project here, which is also an Arduino Uno thing, but I haven't released that. So if I right-click on here,

**Dave Jones:** you'll see that I can actually commit the project to the version control tool, or I can actually release it. And when you do that, that's when you actually, I believe, even commit makes it public. But I have tested that other people, whilst they can see my project,

**Dave Jones:** and they can see the name of my project, they can see that I've started a project called Test Project, like this. Anyone in the public can see it. They can't actually see any of my design files until I actually go in there and commit and release them.

**Dave Jones:** So it's mostly private, not 100%, because people, you know, if your title up here is very descriptive, if you're Super Secret Project, then, well, if people are following you, then they can see that name as public, even before you release the project. And whilst I understand why they've changed the user interface

**Dave Jones:** to this ribbon format, people either love it or hate it, I can understand that because Altium Designer is not exactly the most beginner-friendly package out there. It's super powerful, but I, you know, I think this one will be easier to operate for beginners.

**Dave Jones:** But that's hard, you know, for me, because I've been using Altium Designer since, you know, the 1980s when it was ProTool. But here's the most annoying thing for an experienced Altium user like me, is that not only is the user interface changed, but it still actually looks, you know,

**Dave Jones:** it's still quite familiar to me. That's okay. The thing that really bugs me is that they've gotten rid of all the shortcuts. If I'm in the PCB and I go P for place, like, no, it goes up the project here. Oh, unbelievable. Why did they have to take out the key?

**Dave Jones:** Shortcuts like that. They've had the same key shortcuts since their original ProTool for DOS product in 1985, or whatever it was. Unbelievable. I think I know the reason is because they don't want to make this tool too productive. So, you know, that's one of the big differentiators between this one.

**Dave Jones:** Yes, it's a full-featured, you know, professional-type tool, but it's not as hugely productive as the proper, you know, full $8,000 or whatever it costs these days Altium Designer tool. But, you know, come on. That's just stupid. I mean, it doesn't help people when they start out with CircuitMaker like this

**Dave Jones:** and then move up to Altium Designer. Oh, so frustrating. Calm down, Dave. Calm down. It's a free tool. Just deep breaths in and out. But here's where I think the wheels have really fallen off the billy cart with this idea. And while CircuitMaker standalone, I think, is, you know,

**Dave Jones:** it's a great concept and they're doing the right things here. They've just killed you right at the step where let's say you've used CircuitMaker, you know, to work on your projects, and now you're working on something bigger. Well, you want to keep more than two projects private

**Dave Jones:** and you want to be able to work on files locally, for example. You're on a plane, a train, or whatever, or you just have a shitty internet connection or whatever. What do you have to do? Well, instead of giving you like a pay $100, couple hundred bucks even,

**Dave Jones:** I don't know, I'd happily pay a couple hundred bucks for the ability to work on projects locally, for example, something like that. No, what they force you to use, they've now got another new program, confusingly called CircuitStudio. Okay, so they've got Altium Designer as their flagship product,

**Dave Jones:** then they've got CircuitStudio, and then they've got CircuitMaker. And CircuitStudio, well, it uses a similar ribbon system to CircuitMaker. Once again, it's different to Altium Designer, so you're not stepping up to Altium Designer, you're sort of like stepping up halfway to CircuitStudio. Well, that might be okay, right?

**Dave Jones:** But how much does it cost? They've teamed up with Element14, haven't they? The makers of Eagle, because they own Eagle. And Element14 clearly want Eagle to be like the low-end, hobbyist crap product. And I've heard that they're actually laying off staff at Eagle.

**Dave Jones:** I don't know if that's true. There's a rumor going around that that's the case, so they probably won't phase it out anytime soon. But yeah, they've teamed up with Altium. I'm not sure who contacted who first. But anyway, Element14 is now where you buy CircuitStudio

**Dave Jones:** from this mid-range package. Okay, great. How much does it cost? Tell us the price, son. Well, let's go in here. Stand-alone license plus one-year subscription. Oh yeah, you've got to buy the subscription just like Altium Designer. How much? Hold on to your hats.

**Dave Jones:** Hold on to your hats. $3,573.55 before tax. That's Yankee. Is that Yankee dollars? Yep, that's Yankee dollars. Unbelievable. So you've got to step from the free tool up to $3,500. What the plus? And to keep the thing maintained and, you know, bug fixes and all that,

**Dave Jones:** it's $591 a year after that to continue. That's maybe okay-ish. But, like, it's $3,500. It's in this no-man's land, this dead zone pricing band between free and Altium Designer. They needed, like, a $300, couple hundred dollar option, maybe even $500 option for people to use CircuitMaker locally.

**Dave Jones:** Why have this middle-of-the-range CircuitStudio? Unbelievable. I reckon they've just completely screwed up here with their product, you know, differentiation between the different products. There's no need for this CircuitStudio. I haven't tried it, granted, but just the pricing of it. It's just... D'oh! D'oh!

**Dave Jones:** Fail. I don't reckon it'll sell at all. So what the hell are Element14 and Altium playing at here? I mean, well, Element14, I can only think, well, they must want to have a tool to step people up, be able to sell a tool to step people up from Eagle.

**Dave Jones:** So in that case, well, they probably don't plan on putting much effort into Eagle anymore if, you know, that's just going to be some low-cost, you know, hobbyist kind of thing, and we'd much rather have people sell Altium Designer. But it's very interesting to note, and perhaps telling,

**Dave Jones:** that Element14's competitors, Mouser and DigiKey, have done the same thing. Look at this. DigiKey have now teamed up with Mentor Graphics, and they're offering Designer Schematic and Designer Layout, some cut-down thing with 1,500 connections. How much is the unlimited connection one? Let's have a look.

**Dave Jones:** I haven't actually looked at it. $499! There you go. Look at that. That's just for the Schematic, and the layout is unlimited connections, so $500. And $800, you know, it's, hey, a cheaper solution than what bloody Circus Studio is from Element14, that's for sure.

**Dave Jones:** And Mouser, yet another competitor to DigiKey and Element14, they're offering National Instruments MultiSim. This is like a fairly highly regarded simulator, but it does PCB design and BOM and stuff like that. You can download it for free, features, completely free, blah, blah, blah, free, free, free.

**Dave Jones:** Oh, goodness. I don't know. Try it if you dare. So, you know, they're playing Me Too, and they have to have something, and they asked Altium, and Altium went, oh, yeah, we can just repackage CircuitMaker and call it Circuit Studio and charge $3,500 for it.

**Dave Jones:** How does that sound? Woo-hoo! Everybody happy! So anyway, it is what it is. We have CircuitMaker, and it is free, so that is awesome. Let's not complain, shall we? So the way it works, like all this over here, this panel, this projects panel,

**Dave Jones:** looks exactly like Altium Designer, but as I said, this ribbon layout up the top here, completely changed. And it all starts with, ironically, this start page here. And this is what you get when you load up the program, or you can go back here at any time from wherever you are.

**Dave Jones:** And it lists, like, popular projects, the ones that have been committed, things like that. You can follow people. These are my projects here. I've only created two of them. You can make a new one here. You can search for components. I haven't actually tried that.

**Dave Jones:** And here's the forum activity, and it is tied into the forum, which still uses the bloody Morphic forum engine. Anyway, yes, they do have a forum over there. It's not hugely active, but there are a lot of people there who will answer your questions,

**Dave Jones:** including the Altium people. So, yeah, these are my ones that people have replied to threads I've done, and things like that. You can send messages to people. And it all starts from here. So we can do a new project, or we can do recent projects down here.

**Dave Jones:** Now, down here in extensions, they do actually still have the purchased option here. They don't have anything for you to purchase, but obviously they've got the facility in place, so if they wanted to do things like, okay, local saving or something like that,

**Dave Jones:** maybe they can add that as a purchased option. And updates are fairly seamless. Installation worked no problems for me. A few people reported issues, but it's about a 300 meg download or something. I just updated again, and it downloaded 300 meg again. By the way, I've got a pretty fast rock-solid connection here.

**Dave Jones:** I've got 20 megabits upload and 20 megabits download direct fiber connection. So, yeah, it's a rock-solid internet connection. So, unfortunately, I can't test it with a dodgy internet connection to see how slow it is. Now, if I do actually type a number into this lookup components here,

**Dave Jones:** it searches, it searches, and it finds various parts. Now, by the way, Altium have teamed up with Octopart. So they're using the Octopart database and back engine and all that sort of jazz to get price and, you know, supplier information and all that sort of thing.

**Dave Jones:** Now, unfortunately, one of the problems here is that... Oops, it just... Libraries, there we go. Here's the libraries breakout. And, like, how do I scroll this? Like, all this pricing data is down here, but, like, how do I... Like, it's just not... My screen is not big enough.

**Dave Jones:** I've got a full HD 1920 by 1080 screen, you know. Granted, I've used bigger ones with Altium Designer before when I was using it professionally, of course. But, yeah, they just haven't... Like, how do I get to my data down here? It's just chopped off.

**Dave Jones:** I mean, this is like a very typical size screen your average user is going to have, and you can't see all the information. Then, okay, assuming that we've, you know, found a part that we like or whatever, then we can right-click on that.

**Dave Jones:** Whoops. And then we can either place that directly on our schematic sheet. We can build a new custom component, or we can edit this, build new versions. Add to favorites library, and stuff like that. Here's our component detail. Here we go. See, that's the thing with this internet.

**Dave Jones:** It seems to take... A lot of things in here seem to take a while. Anyway, I know it's downloading data from the Octopart engine and all that sort of stuff. Anyway, look, we do have stock. Look, there's people who have these things in stock, non-authorized ones,

**Dave Jones:** DigiKey, blah, blah, blah, tell you the price, how much stock you got. I mean, fantastic. It looks like Audium's teamed up with Braintree. They're in Essex in the UK, and they've got this bomb management, bomb analyzer, all this sort of stuff, and distributors.

**Dave Jones:** So I'm not sure whether or not that has anything to do with Octopart, but they were supposed to be using the Octopart backend for that, so I'm not exactly sure what's going on there. But anyway, it's tied into all these different third-party backend databases.

**Dave Jones:** And this is why they've got ShowingSiva.com down here in the parts library, and that's why if you go over to the libraries panels, the actual library is called Siva. So that is what looks like Audium are pinning all their hopes on, is that all of your library components, all the parts,

**Dave Jones:** you don't get access to the regular Audium Designer libraries, which is, you know, they've got hundreds and hundreds of thousands of parts. It's actually, you know, it's not bad at all, but they don't give you that in the CircuitMaker one. They've gone for this third-party company called Siva,

**Dave Jones:** which ties into the Octopart. Well, that's what it originally was. Maybe they've changed over to Siva. I'm not sure. Anyway, you know, I don't know anything about Siva. I haven't really looked at it, but this is where all of the component, your standard built-in component libraries are coming from.

**Dave Jones:** Now, one thing I'd love to see is in the schematic here, being able to right-click on the part, and then actually go to that page that we saw before with all that information. Sure, we can go down to properties here, and it pulls up like an Audium, almost an identical Audium Designer info panel.

**Dave Jones:** So this is intimately familiar to me, and we can edit the pins, and we can see the parametric information and stuff like that. But, like, where is the ability just to jump over to that Siva page that we saw before? Because the beautiful thing about all this community parts thing is,

**Dave Jones:** well, this is not a good example, but it will show you how many projects it's used in, which projects it's used in, what revision the part is, things like that. So you can see how popular the part is, and I'm not sure if you can actually sort by popularity of parts,

**Dave Jones:** or it shows the most popular part and things like that first. And when you've got a community component database like this, you can do all sorts of powerful stuff like that. So, you know, you can say, oh yeah, the Arduino people used that particular part.

**Dave Jones:** Oh yeah, I can trust that, must be a winner. They've made, you know, 100,000 of those boards, no worries. Now the general responsiveness of the schematic is okay, when you're just, you know, panning around and doing the usual stuff, no problems at all.

**Dave Jones:** But I've encountered, like, that one popped up instantly, but I have encountered, like, lag and things like that. Now, there's one thing that I really like. If I leave my cursor over here, over a component, it pops up with a supply chain insight,

**Dave Jones:** which is some of that information, some of the information we saw on that component, that library page before we got from that SEVA website. So that's really quite nice. But look, I don't know why there's no, like, right-click option to call that up.

**Dave Jones:** Why do I have to, like, I didn't even know. I just found this by just leaving my cursor there. Like, you know, where is it? Where is this supply chain insight up here? I don't get it. You know, look, it's not up in view, libraries, it's not any part of that, right?

**Dave Jones:** So, like, what the hell? You know, these, like, magic stuff like that, just hidden. I've just got to leave my cursor there. Why can't I right-click? Crazy. And one of the things with this ribbon interface up the top, while it looks, like, you know, kind of jazzy,

**Dave Jones:** but look at how much vertical room of your real estate you're losing to this ribbon frame up here. It's just crazy. No wonder we can't see everything in the bloody libraries panel, because it's all taken by this stupid ribbons thing. When this thing pops out, it should, like, use all of your available screen.

**Dave Jones:** But no, look, there's no ribbons and there's no options in here. But still, it's just, like, completely wasted space. Terrible. And all of your project options stuff, well, this is, you know, straight out of Outium Designer, if you've used it before. It's, you know, it's exactly the same.

**Dave Jones:** So it's very clear that they've just taken Outium Designer and they've, you know, whacked on this ribbon interface, shoehorned it in, you know, all this, like, you know, made a few changes over here, but they've kept all the projects and all sorts of other stuff.

**Dave Jones:** And all the menus are basically exactly as you see on Outium Designer. But, hey, that's not surprising, you know. They didn't actually develop this from scratch. And it's got some of Outium Designer's more advanced functionality, as they promise, and things like PCB pin swapping, for example.

**Dave Jones:** So we can go in there and configure our pin swap data for, you know, very handy for FPGAs and other types of pin swappable micros and things like that. And over on the PCB side of things, yeah, once again, it works exactly like Outium Designer.

**Dave Jones:** We're actually, by default, in single layer. Well, not by default, by what this library was loaded as. In single layer mode here. And, of course, we can just hit the three button to go into Outium's famous 3D view, which is, you know, fantastic.

**Dave Jones:** And we can do lots of... So a couple of, like, the zero key and things like that still work from Outium Designer. We can do stuff like, you know, fly inside the board. Sorry, I'm doing this with my mouse. I don't have my space navigator that I was used to

**Dave Jones:** when I was working at Outium. But we can fly inside the board, under the part, and things like that. So, you know, fantastic. Just hit two or three key. It's one of the most powerful features of Outium Designer. Not just to see, like, the 3D components like this

**Dave Jones:** and things like that, but just to see the bare board. Even if you don't have the 3D component information on there, being able to see a solder mask and everything else, fantastic. And it's nice that you can actually take your board and export that as a step file, too,

**Dave Jones:** for your, you know, to put in some other 3D package. Terrific. And, yeah, everything's just like Outium Designer. I feel completely at home. It works the same way. It's just that they have this ribbon interface. Once again, look, pissing away all the space up here.

**Dave Jones:** They could have made these icons smaller. Anyway, yeah, you know, we can do the assembler's drawings, pick and place files, MC drill files, print, everything else. It's exactly the same. It's exactly the same menu. You get in the full version of Outium Designer,

**Dave Jones:** so we can go in there. We can choose our layers, for example, our top overlay, and our top and bottom layers, and our bottom overlay. We can generate our Gerber files, and off we go. Bob's your uncle. So here's our generated Gerber files.

**Dave Jones:** Unfortunately, one big thing that they have removed and grrr, is Gerber viewing. Look, you can't actually view these Gerber files, whereas before you could use the rather crude internal Gerber viewer in Outium Designer. So here's the top layer, and if we click on that,

**Dave Jones:** yeah, there's a Gerber file viewed as text. Thank you very much. You want to read the matrix? Now, the thing I'm actually amazed about is, like, when you go into here and you look at all the community designs, I found this Arduino one I'll look at in a second,

**Dave Jones:** but I just, like, put five stars on here, and it's automatically appeared to the top, okay? But, like, where are all the huge, big reference designs? Why don't they load? You know, they've got nanoboards that, you know, I designed when I was there.

**Dave Jones:** They're massive, big, like, eight-layer boards, big reference designs. I had 12-layer boards and things like that. I'd love to be able to load in and show you, and why they don't have, you know, a really fantastic example. You know, they should have, like, you know,

**Dave Jones:** Primo examples here or whatever. Look at here. You know, we can do a big 16-layer board with BGAs and coming out our Wazoo and everything else, and it's just not there. I mean, granted, this is not a release, right? This is a beta, so maybe they'll,

**Dave Jones:** hopefully they'll add some sort of stuff, and this is, like, the most complex project I could find that somebody had uploaded, browsing through, like, three or four pages worth of projects. So it's an Arduino Due that they've, if I'm pronouncing that correctly, that they've imported from Eagle,

**Dave Jones:** and that looks like it does the business. Yeah, there are a few issues with the imports, but as I said, you know, it gets you the basics anyway. Like, you know, nobody's, like, gone through and tidied that up. I had a few issues with the PCB and things like that,

**Dave Jones:** but if you need to import projects, yeah, it's not going to be seamless, but it can do the business. So, of course, it's got all that lovely interactive multi-routing and things like that. This won't be the world's best example, but I can go in here and I can go interactive multi-routing

**Dave Jones:** on these three pads. I haven't set up all my routing rules and things like that, but, you know, it'll, and you can set for push and shove. You can see the traces down there, just push and shove around and things like that. So it's got all the usual powerful routing capabilities

**Dave Jones:** of Altium Designer. I love it. It's fantastic and it's free. So this video is already long enough. I won't go through and show you what Altium Designer's like, but yeah, it, from what I've, you know, I've only played with this thing for a little bit,

**Dave Jones:** but it does look like it has most of the capability, all the good stuff in Altium Designer, in the full, like, you know, $8,000 package that everyone knows and loves or has a love-hate relationship with. It depends on which way you look at it.

**Dave Jones:** You know, multi push and shove auto routing, interactive differential pair auto routing, the BGA, the pin swapping, and all sorts of stuff like that. It looks like it's the full-on package. It's just that they've, the only way that they've sort of dumbed it down

**Dave Jones:** is to add in the sort of, you know, online-only, internet-only cloud capabilities and stuff like that. Hey, you know, fantastic. I'll take that for free. Thank you very much. Unbelievable. So, you know, great thing, and the 3D view has always been one of Altium's strong points.

**Dave Jones:** I know a lot of other packages have caught up to that now, but even if you don't, as I said, even if you don't do the 3D models and things like that, it shows you, you know, whizzy-wig. What you see is what you're going to get

**Dave Jones:** from your PCB manufacturer. There's your solder mask expansion, things like that. You can actually go into the board if you're that keen, and, you know, fly around, and it's, yeah, it's just terrific stuff. And you get all this in the free version of CircuitMaker.

**Dave Jones:** You know, wow. My hat's off to them. Fantastic. Now, of course, I would expect bugs in this, but because it's based on, it looks like it's, you know, like the complete Altium Designer back-end and things like that, it seems to look, work, and feel,

**Dave Jones:** almost all the menu options are identical. In fact, it's sort of like only the ribbon kind of interface, which has changed all the menus. Everything else is exactly Altium Designer, taking out a few things I take for granted regularly using Altium Designer, like the hotkeys and the Gerber viewer,

**Dave Jones:** the simple internal Gerber viewer, for example. But, oh, jeez, no problems whatsoever. I mean, you know, yeah, Altium always has bugs, always had. They're famous for their bugs, but, yeah, anyway, it's still a kick-ass package, and this CircuitMaker, I'm sure, even though I haven't fully used it in anger yet,

**Dave Jones:** I think it will be pretty much as good as Altium Designer, because it's basically, it's going to be like the same code. I'm not sure how they handle it at a project management code similarity point of view, where any updates in Altium Designer

**Dave Jones:** automatically get pushed through to CircuitMaker or vice versa, but, yeah, it's pretty impressive. So, actually, moving up from CircuitMaker into, well, Circuit Studio is going to be the same as CircuitMaker, except it allows you to do all the local stuff, I believe, but moving from CircuitMaker

**Dave Jones:** up to the full professional Altium Designer shouldn't be that hard at all, and, of course, I'm completely familiar with this. I can, you know, lay out boards fairly quickly straight away, because it effectively is Altium Designer, just with a little bit easier to use user interface,

**Dave Jones:** although I think they, you know, they're wasting a lot of space up there. Space is always, real estate, screen real estate's always been an issue with Altium Designer, and, yeah, this new ribbon layout doesn't, doesn't help matters at all, but, oh, I feel so at home.

**Dave Jones:** I love it. But, of course, because it is based on Altium Designer, well, you've got, you know, what, 25 years worth of, oh, maybe not 25 years, but, you know, since when did they release the first Windows version? I don't know, but there's just, like, you know,

**Dave Jones:** so much legacy in the menu options and things like that, so Altium's famous for having lots of duplicate functions all over the place, and, you know, lots of things, different options scattered in nonsensical areas, and, you know, things like that, and that carries over into Circuit Maker,

**Dave Jones:** so while it looks a bit easier with the ribbon thing up the top, it's, you know, not quite as user-friendly as it could be, that's for sure, and there's been some talk that you can't create your own components from scratch. Well, that is not true.

**Dave Jones:** You just go into your panel over here, you right-click, and you just go Build New Custom Component, and off you go. Bingo. And this will certainly not be a component creation tutorial by any means, but, yeah, here you go. You can add the new schematic symbol,

**Dave Jones:** you can add your own footprint, and you can add your own simulation model as well. No problem whatsoever. So the interface is exactly like Altium Designer, except, as I said, I don't have the bloody hotkeys, which is really annoying, but I can just place my rectangle.

**Dave Jones:** I created that in, like, you know, 10 seconds. Bingo. Easy. And it automatically showed up here in your models. Yes, I know. I've put pin 0 in there. I was just automatically repeating. And we can go in and do exactly the same thing

**Dave Jones:** with the PCB footprint as well. So, oh, I can't do place. Oh. Anyway, we can place our pad 0. 1, 2, 3, 4. Yeah, right. 5, 6, 7, 8. There you go. There's our Dave's dodgy component. And if we go over here as a created node,

**Dave Jones:** we might have to just give that a little save. And it should pop up over here. Bingo. There's our component. We can go through and add. Like we regularly do, you can, you know, add a 3D model and all that sort of jazz.

**Dave Jones:** So no problems whatsoever. Although it seems like you can't change this weird-ass, you know, auto-generated number up here. So I'm not sure what the hell's going on there. But anyway, I guess you've got to have a unique part. This is a unique name.

**Dave Jones:** This is part of the, you know, the community aspect to it. And when you go in and start your new project, like if you want to, somebody's already used Proto. We know if you want to, or somebody's Transmitator. Transmitator? Transmitator? Anyway, you can't use any project name

**Dave Jones:** that anyone else has used. So, you know, if you put, if you've already used a Test Project, well, you can't use Test Project. You might have to use Test Project 592 and add your age or something like that. It's like getting a bloody Gmail address.

**Dave Jones:** Although the only thing I'm unsure of is actually now how to call up, search for and call up that part. I gave it the name EEVblog Test Part, and I can't find anything in the regular Place Part section, and I can't find anything in the library,

**Dave Jones:** the SIVA library. So I'm not sure how it actually adds them to, or if it adds them to SIVA, or whether or not it's stored locally or something. I haven't. It's not over in my favorites, so I haven't exactly figured out the full component management yet.

**Dave Jones:** But you can certainly create your own symbols. Not a problem. Well, there you go. I think I'm actually going to call it quits there. This video is long enough. It was just like a brief look and sort of like my first impressions of CircuitMaker here,

**Dave Jones:** and I started out being, you know, so excited I did that video telling Altium how not to screw it up because Altium is famous for shooting themselves in the foot and screwing things up. And I was, you know, and then I saw like the preview release

**Dave Jones:** and they talked about the community staff, and I thought, yeah, okay, yeah, okay. But I really was quite excited when they told me that they, you know, had the low-cost model and they could add things on. I thought they were headed in the right direction.

**Dave Jones:** Everything was terrific. And then rumor came out that they, yeah, had completely gone away from that. It's now completely free, but it's now fully online and everything else. And I just went groan and sort of gave up for it on a while. But now I'm on the lookout to,

**Dave Jones:** for a new package, and I am definitely going to try CircuitMaker because it basically is Altium Designer, which both myself and David too here in the lab, he's familiar with as well, and we can collaborate on designs and it's free. We can do unlimited size designs,

**Dave Jones:** as many layers, as much complexity as we want, and we can make them publicly available because we plan on doing open source hardware. So it's not a problem. And it's a reasonable limitation to have like the two free things, but I really think that they need to offer

**Dave Jones:** that local saving option. If your internet connection goes down, it looks like you are screwed or if you've got a poor internet connection, you're screwed. You know, I'm kind of a bit used to that, all my emails online and I use, you know,

**Dave Jones:** Google Docs and things like that for stuff and so I'm used to that sort of thing. So I'm tentatively going to, you know, I'm a bit nervous about trusting everything online like that, but the options are compelling. This is the full, basically you're getting

**Dave Jones:** almost all of Altium Designer for free. It's incredible. And I think that it ultimately might be very powerful with the community stuff and things like that. This is only a beta. Altium are after feedback, so if you've got feedback on this, install it.

**Dave Jones:** It's free. No catches. Try it out. Yeah, I was skeptical, but the more I think about it, the more I use it. I've only used it for an hour or two, so I haven't got really in-depth to it yet. I need to start a full project from scratch

**Dave Jones:** and the whole design cycle, everything else. But I'm pretty certain that they're not going to go and offer a local option for this because that's what Circuit Studio is for, and that's why you've got to pay $3,500 for it. So if they went and added

**Dave Jones:** like even a $500 option for Circuit Maker here to save everything locally and work without the internet, then, well, why would you buy Circuit Studio? You wouldn't. You'd be nuts to pay $3,500, so they've got to protect that market now that they've made that commitment

**Dave Jones:** to or, you know, the agreement with Element 14. They're just locked into it. It's not like they can just go and can that thing. That'd be embarrassing, although I think they should. I think they should. That would be the sensible, just admit, no, sorry,

**Dave Jones:** Circuit Studio, that was just at that sort of price point, just a dumb idea. Or just lower the price of Circuit Studio, you know, make it $1,000 or something like that. You know, heck, I wouldn't even go and personally buy it at $1,000,

**Dave Jones:** you know. So, but, nah, $3,500, it's just, nah, it's going to fail. So my verdict at this stage, although I don't think it's the right direction that I wanted it to go in, I'm not going to, you know, kick sand in their face

**Dave Jones:** because this, it looks really good and I'm quite excited to have most of Altium Designer for free and I think the limitations are probably quite reasonable. So, yeah, I've got to give it a, I've got to give it a thumbs up and I recommend people go and

**Dave Jones:** try it because all that power in there for free, but hey, I understand if it's a showstopper with the internet connection or whatever or you really need multiple projects for, for, you know, a private and things like that, then, well, there's, you know,

**Dave Jones:** hey, sorry, you're just going to have to go and try it. Not for everyone, but, geez, imagine if everyone had it and they need to work on the community tools and the libraries and the aspects of it and things like that, but, initial first reaction is

**Dave Jones:** it's a, it's, I think it's going to be successful. I really do. Circuit Studio, I think, is just going to fail. It's, it's just priced in the wrong market. Maybe if it was a thousand dollars it'd be successful, but because it's like three and a half thousand dollars

**Dave Jones:** plus maintenance and things like that, nah, that's just going to fail. No one's going to go for that. They're all just going to go right up to the full-blown Altium designer, I think, anyway, but, hey, I could be wrong, but, yeah, that's the impression I'm getting,

**Dave Jones:** but I need to give Circuit Studio a go, but Circuit Studio is effectively, from what I understand, Circuit Maker, just with, like, local saving options and all that, not, you know, not locked to the internet. So, yeah, Circuit Maker, just charged a reasonable price,

**Dave Jones:** maybe left out things like auto routing or, you know, some of the interactive auto routing, perhaps the multi, you know, just left out a few things that, you know, would have sweetened the deal, but, hey, you can't complain when it's all for nicks.

**Dave Jones:** Unbelievable. So, yeah, I'm rather excited to have Altium Designer for free. And one really important thing to note is that there is no, you know, commercial clause to this. You can, ah, use this for any commercial project you like. It doesn't matter. There is no restriction.

**Dave Jones:** It is free, gratis. Just go and use it. Adds Altium's gift to the open source hardware, you know, slash hacker maker movement. For people to use this thing, sure, they want everyone to collaborate and all the rest of it, maybe they can make money

**Dave Jones:** somewhere on some optional extras or maybe just, I get people to upgrade to the previous version, but yeah, it's a big move on their part by just making everything completely free. And that's just, that is brilliant. Yeah, they have crippled it and if your

**Dave Jones:** workflow doesn't support the crippled nature of the fixed internet connection requirement, then, well, sorry, but, yeah, if you can handle it, this could be the package of choice. Anyway, I recommend you try it out. I've only tried it out for a few hours.

**Dave Jones:** In this, and, because we, yes, I am working on the microsupply and other projects as well, along with Dave too here, and we'll both be using CircuitMaker and looking forward to the collaborative functions and the release management and all that sort of stuff

**Dave Jones:** and no doubt I'll be doing more videos and probably tutorial videos and things like that in due course because I think I've found my package. I'll give it a go anyway. It might come back to bite me out here. Might cancel this damn thing

**Dave Jones:** in a couple of years when they change direction again. Who knows? I, yeah, I wouldn't put it past them but, anyway, we'll cross that bridge if we ever get to it. So, yeah, sorry this wasn't an in-depth look because I've literally only used it

**Dave Jones:** for like an hour just bummed around but, yeah, I like it. I think it's got a winner written all over it. So, there you go. The link is in the description down below if you want to discuss it. Jump on over to the

**Dave Jones:** EEVblog forum. Catch you next time. Ooh, wish I had my space navigator. I could do this, you know, really nicely.
