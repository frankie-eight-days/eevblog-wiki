---
video_id: HJVy8LAI_Bc
title: EEVblog 1535 - DeepPCB AI AutoRouting FAIL!
url: https://www.youtube.com/watch?v=HJVy8LAI_Bc
source: youtube-asr
---

**Dave Jones:** Hi, back in video number 975 6 years ago. Whoa, I'm I did a very popular video where I pitted my PCB routing skills against Altium's auto router to see which one could do a better result on my Nixie tube project

**Dave Jones:** which was like a most like five or six part video series. If you haven't seen it where I did design this Nixie tube project for my YouTube silver award thing. Anyway, link it down both link it down below if

**Dave Jones:** you haven't seen it and TLDR is that nah, the auto router was yeah, nah. It was no. I was you know, I don't want to brag, but I was much better than the auto router. Now, as a former

**Dave Jones:** professional PCB design engineer who did routing every single day like for decades. Yeah, auto routing is actually useful, but as I've said many times before when discussing auto routers is that it actually it sometimes takes more time to set up the auto router properly

**Dave Jones:** all the parameters that go into, you know, all the constraints and parameters behind auto routing before you hit the auto router button. You can't just place your components and just hit the auto router and and magic happens. That just no, it doesn't work. Auto

**Dave Jones:** routers are actually incredibly useful for lots of in especially the more complex a PCB gets like, you know, a motherboards and things like that, you know, incredibly complex things usually not going to 100% hand route those. You'll probably like set up a lot of

**Dave Jones:** constraints, but you'll spend you could spend a week setting up constraints before you hit that auto router button and then it can actually produce really good results. But anyway, in this particular example which was a double-sided board here.

**Dave Jones:** Yeah, the one on the top is the auto router result. The one on the bottom is mine. So, yeah, anyway, you can check that out. There's the bottom, there's the top. I've put in a nice ground fill and everything else. Anyway, yeah, the

**Dave Jones:** Altium auto router didn't do a very good job, but it can if you set it up and constrain it correctly. But, a lot of people, for quite a few years now, in fact, I checked my emails, someone sent

**Dave Jones:** me this in 2019. There's a There's an AI cuz AI is all the rage. This is company called Deep PCB who have an AI auto router. Now, there's nothing new about supposedly magic auto routing, you know, AI technology. It's

**Dave Jones:** been going back many, many decades. Neural net routing was all the rage in the '80s and '90s and stuff like that. And there was They had fuzzy logic and they had all sorts of right Every manufacturer had their own, you know,

**Dave Jones:** trademark flavor of auto router. That's sort of like, you know, pretended to be machine learning AI and all that sort of stuff. But, of course, AI these days it's pretty advanced as I've done videos on. So, I thought I'd try this. So, this

**Dave Jones:** Deep PCB, people have been asking me to give this a go. So, I thought I would take the exact same file out of this that I used for this example, so that we'll have a comparison with my routing with the Altium

**Dave Jones:** routing with the Altium auto routing, and then try this AI. Still beta version 1.000. So, I I don't know what they've been doing for like 4 years or whatever, but some people say it's pretty good, others go, "Meh." Now, of course, the big thing

**Dave Jones:** with auto routing, one of the big things, is placement. As I've said before, PCB layout is like 90% placement. Getting the placement right. Now, as I've already placed these components, what I'm going to do is take the existing board file, I'm just going to

**Dave Jones:** unroute it. So, it's reasonably good placement and done by a verified human, Um, I thought we just load that in there and see if it can order out. Pure AI-powered cloud-native PCB routing, design complex boards in less than 24

**Dave Jones:** hours. So, I can't do this live right now. I think I have to like wait a day. Um, and it's free for two-layer uh boards, I believe, cuz it's still in beta or whatever. Upload your board. Um, our fully automated, no human in the

**Dave Jones:** loop cloud platform gets to work as soon as it receives your .dsn PCB file. No time wasted. Distributed machine learning. Our beta release covers the following features routing for printed circuit boards up to 150 pairs. Two layers is currently available. I'm not

**Dave Jones:** sure what the 150 pairs is. Is that like controlled impedance pairs? Um, I I'm not sure what the deal is. Um, all our sole boards are DRC uh checked, fully compatible with KiCad. Uh, leverages innovative Instadeep AI technology

**Dave Jones:** combined with powerful GPUs and cloud infrastructure to offer the first pure AI PCB routing engine. Results in 24 hours, not weeks or months. Uh, save time, accelerates. Well, if it's a two-layer board, like it's not going to take you weeks or months to lay

**Dave Jones:** out the board usually, unless it's an absolutely massive board. Your questions answered. Are you Are you doing this manually? I would bet you have humans in the loop. Actually, DeepPCB is fully automated tool currently in beta. Automation possible thanks to reinforcement

**Dave Jones:** learning and AI technology particularly suited to decision-making problems, board games such as chess or go, logistics, mobility, or PCB routing. Instadeep. So, there you go. Anyway, I will I'll link it in down below. Apparently, there's no humans in the

**Dave Jones:** loop. So, apparently, all it supports is a .dsn uh file. So, that's an OrCAD uh Spectra file. So, um unfortunately, my um Altium license, and yes, I know the irony of this, it has expired. And yeah, they won't give me another one just for

**Dave Jones:** like educational use or whatever. So, anyway, I can't export my original uh project here. But, thank you very much. uh a couple of people I asked on Twitter. Couple of people uh did that. They unrouted it for me, saved it as a

**Dave Jones:** uh DSN file, and well, we're going to give it a whirl. All right, so let's drag over open the DSN file, submit, and apparently it will display like a preview image or something. Price, free. Thank you. Number of layers, uh number

**Dave Jones:** of air wires, 238. Number of pins, 363. Uh I can't even get board information. Yeah, I can't get anything. Anyway, um I presume it'll do the full thing. I hope it's within the constraints. Um it's not a huge board. So, let's

**Dave Jones:** confirm. Okay, free. Uh done. Order placed successfully. My board. So, I can view it, presumably. Board processing. Okay. Um I'll get back to you. It's It's running. It's doing its business. Will it actually Will this be a like a live

**Dave Jones:** update? That'd be really cool. I think But of course, you don't want to sit there watching the AI do it, do you? Uh you know, you just want to like send me an email when it's done. Please. Routing

**Dave Jones:** from empty board. Yeah, it knows there's no uh traces there. I haven't told it anything about ground planes or anything like that. Whether or not it actually is smart enough to like whack down a ground plane under all that. Not that it's

**Dave Jones:** needed on something like this. It's just You know, it it it's just the done thing. It's the vibe. Think cuz this is a Nixie tube project that you know, you know, reasonably high voltage DC stuff. So, clearance is important. So, once

**Dave Jones:** again, all that clearance sort of stuff would be part of your manual uh constraints when you're uh set up constraints for your auto router. Auto router. There you go. Completed in 4 minutes. What? It's 4 No, it's still

**Dave Jones:** running. I was excited there. It looks like it's done 117. Yeah. There you go. It changed from 117 to Oh, look. Look. It's doing it. It's doing it live. I thought this would be like a 24-hour thing. Look, it's got these uh Yeah,

**Dave Jones:** yeah, you can see my cursor there. It's got like nine right angle traces coming out. That's just a no-no, okay? That's what the Altium auto router did, but I don't know if this is like an intermediate route or it's a final route

**Dave Jones:** or anything like that. Now, look, I'm going to forgive anything to do with like clearance constraints for for the high voltage, you know, part of it. So, I'm you know, I'm just going to ignore that. But, look at this look at

**Dave Jones:** these traces up here, okay? It's just It's just a why why not continue that across there and go down? So, let's go to my board over here and it was obvious that this like common, right, high voltage anode I

**Dave Jones:** think it is like a line. That's a common thing for all of those displays. So, any human, right, would would would know like you kind of route that first, right? A, it's a high voltage line, so you like snake it around the outside, so

**Dave Jones:** it's got a clearance from everything else and it goes to these dropper resistors down in here like this, okay? And then it's common to all of them. So, like that was one of the first things that I routed as a human, right? And and

**Dave Jones:** then it's No, but this thing, right, it's got it's dropped vias down there, right? Oh, no. Oh, this is this is terrible, Muriel. Whether or not I assume it's a rip up retry like algorithm as it's called. That's the industry term for when if you

**Dave Jones:** get sort of like locked in it's going to change when you get like locked in sort of like constrained in you might have to rip up some traces and it can't figure out any way inside it has to rip

**Dave Jones:** up some traces and then retry again. Yeah, it is definitely rip rip up and retry. It it definitely changed. I was just explaining how it put a via in there and and jumped over that that high voltage line over there and

**Dave Jones:** it's just ripped up that and completely redone it. See, but it it doesn't know cuz we haven't told it, but you know, this is what these are the things humans know, right? And the And the AI can't possibly know that cuz it

**Dave Jones:** doesn't have any schematic information. It's got no knowledge of what the circuit's doing or anything like that. It's just routing. So, you know, once again, this is where like you could you could utilize a tool like this and you could partially route a

**Dave Jones:** board. Like all the important stuff, you could route and then the unimportant stuff, you just let the auto router rip. And as a professional PCB designer, that's what I've done countless times before. It's like I've got all this

**Dave Jones:** digital crap and I've got to route, you know, a thousand traces. And like and they're just like low frequency stuff. It doesn't matter. They're just all, you know, or whatever or you're routing like big buses or something like that. And

**Dave Jones:** you can just let it do all that sort of like unimportant stuff. But the important stuff, you've got to do yourself and set as a priority. So, I I guess I can't blame it. I I can't blame it for not getting that. But it's

**Dave Jones:** doing this live. This is pretty cool. Doesn't look like it's going to be any better than the Altium auto router, which is the one up the top here. But yeah, once again, like all the traces up the top here, it's done a

**Dave Jones:** similar sort of thing. Like it's just No. Yeah, it's just like taking them through the middle of the pins instead of like taking it right around the outside. And that's what a human would have done. That's why mine looks much

**Dave Jones:** cleaner. And And then the top side of mine just looks cleaner. It just looks like a more human result. Anyway, we can actually like just accept current solution, I guess, if you're happy with Oh, right. Stop. I'm happy with that. Don't rip up any

**Dave Jones:** more. Once again, I I didn't expect this to work. It's exactly It It produced the exact or it's producing the exact result I expected, which is kind of like just all over the shop. It just looks like it's auto routed. Nah, AI's not helping

**Dave Jones:** here. Once again, like keep out layers. Like I didn't do any keep out layers. Anyway, you can see I'll turn the wires off there and you can see that it shows the net There we go. And you can see

**Dave Jones:** how, you know, like the placement is ideal for this like each segment has its own chip or or two chips actually, which go to those two, those two, those two like, you know, so nothing's Not much is like crisscrossing across the board and

**Dave Jones:** stuff like that. There are a few things like there's a few common control lines down here. It's a big shift register if you don't know. It's basically, you know, data in and data out and just drivers for the high voltage Nixie

**Dave Jones:** common drain drivers for the high voltage Nixie displays here and uh Bob's your uncle, but unless it's absolutely uncritical and you really don't care, um you know, but have some pride in your PCB layout, please, from an old school

**Dave Jones:** PCB designer. Have some pride and don't do like have traces coming out of Look at this. Look at this one coming back in and just going And then it's coming along and then it's going and going up at this angle. No. No. Oh

**Dave Jones:** god, look look look look at this one up here with this big jaggy like that. Oh, this is terrible. It's having a red hot go, but you know, you know, it's our situation has not improved. This This trace is going up and way. Now

**Dave Jones:** look at this. It's going all the way This is trace here. It's going around here. It's dropping down a via there. It's going on the red layer up the top. Hopefully you can see that. My cursor is bigger on the screen. And then this goes

**Dave Jones:** around around here and then all the way back down to here like it's going all the way up around this side of the board and then all the way back. No, it's it's gotten it's gotten rid of that now. This

**Dave Jones:** is its rip up retry thing and obviously realized that was dumb. This this jaggy on the bottom still down here and I just Yeah, no. I'm I'm just going to have to wait. Now you can see up the top right

**Dave Jones:** here. This is actually solution 16. So is it gone through like 16 complete No, it it it it wouldn't be complete in like 16 16 rip up retry efforts cuz some I know some traces like this Jaggy over

**Dave Jones:** here. This is not changed in several iterations now. So yeah, um it looks like it's just it's going through all these solutions. How it comes upon the best one I don't the AI determines what is the best one? Anyway, let's

**Dave Jones:** let's cast final judgment over the final board once it's done. But we have actually a verified that there's no point sitting here watching it do its business. Although you can get a good idea that uh oh no, I should have

**Dave Jones:** constrained it better. For example, I don't want it doing that sort of stuff and oh, I forgot to constrain it here and here and you know, I probably should have put my ground plane down first. I should have laid down these high

**Dave Jones:** priority traces first and things like that and now you can get an idea of where it's goofing up. So this is actually a really good interface. I like it. Okay, it's been going 2 hours and 9 minutes now and

**Dave Jones:** it's still only up to 100 whoa whoa oh look you can actually choose a solution. Whoa, that's pretty cool. Just discovered that. So it's routed 196 out of 238 connections. So it's it's creeping towards there and yeah, nah, it's still a yeah, nah. All

**Dave Jones:** right, I left it running overnight. It looks like it's locked up. It hasn't gone anywhere. It's exactly the same as it was you saw in the previous clip solution 48 at 2 hours and 9 minutes. It's just it's just died there. So it

**Dave Jones:** looks like it actually died before I actually recorded the previous clip cuz I came back at night and recorded that one and it I think it had already frozen. It's it's I've emailed support. See what happens. Well, it's 24 hours later and

**Dave Jones:** it did actually Well, it says it succeeded here. It took 1 day and 3 minutes. So, I guess they're you know, pretty spot-on with their 24-hour claim. But, uh yeah, look, the solution here is Sorry, I can't see it. It's only gotten

**Dave Jones:** down to 48 there. It's exactly where we were before. And, it's only routed 196 of 238 connections. Now, I haven't heard back from Deep PCB about what happened here, but it obviously froze on that 48th solution there and it just it looks like

**Dave Jones:** it's either refused to go any further cuz I don't know, backed itself into a corner or something or whether or not we reached the limitation of how many nets it can do or whatever. But, anyway, um we've got the results here and

**Dave Jones:** yeah, no. It's crap. All right. So, what I've got here is both the top layer and the bottom layer uh with the old Deep PCB auto routed up the top and my manual uh route down the bottom. So, this is uh

**Dave Jones:** this is DaveCAD versus AI up here. And, no. No, no, no, no, no. This thing has no clue how to route a double-sided PCB. One of the golden rules for or even multi-layer uh PCBs uh it Take any of

**Dave Jones:** the old-school boards. I've shown this before. Let me get it again. Okay, here's an old-school PCB. Okay, with through-hole parts. But, stick with me, okay? You'll notice all the traces on the bottom there. Most of them are going

**Dave Jones:** left and right, horizontal, like that. And, if you have a look at the top, they're going they'll actually be going vertical. I know it's not, you know, clear in there, but that's how you route a board because you don't want to be

**Dave Jones:** caught. The first thing when you're laying out a double-sided board like this generally is that you You want things going higgledy-piggledy, okay? This way, this way, you know, crisscross, cuz then you just run out of room completely and you have to add a

**Dave Jones:** ton of vias. Now, look at my board here, right? What I tried to do is I tried to route almost everything as a first pass on the top layer or the bottom layer, just on one layer. And in this

**Dave Jones:** particular case, I made sure that the two chips associated with the display are placed near, so that and in fact, I even rotated the parts so that they were in the correct orientation. You can watch my I've done a full layout video

**Dave Jones:** of how I laid out this board. And you can see all these traces feed in nicely into here. And you'll notice it's the same thing here. It's the same thing here. Same thing here, here, right? Every display like this. This is the

**Dave Jones:** what a human would do. It prioritizes uh groupings of components. That's another layout technique. You place components near each other that are supposed to be part of the group, and this is how you're you're you're synergy with your schematic uh when you

**Dave Jones:** draw your schematic. Parts that are supposed to be close together, you make sure they're physically close together on the board as well. And then you're going to have the shortest routing path like this. But you'll notice that they, you know, look,

**Dave Jones:** they've done a couple of lines here which are prioritized, but look at how Look at how this was easily routed like this. I just manually routed all these around and it was, you know, look, they're almost lined up perfectly to

**Dave Jones:** route them through like that. And they just they just haven't done that, right? Oh, look, they managed to get one which went all the way over there, but that's like No. And look, in the end, it actually didn't route these nets at all.

**Dave Jones:** You'll notice that these were part of the nets that were that was my first priority when I routed this board is to make sure those segments are there and then I can do the with the dig, you know, the

**Dave Jones:** um, interconnections between the chips like layer maybe on like a horizontal layer like this, but they've just gone higgledy-piggledy everywhere, okay? And next up, just just look at some of the stupid stuff they've done here. This is just nutso, right? Go in here. Look,

**Dave Jones:** what is this, right? What is this? Why have we got two v- like like why is that going like what is this going around to there? Just route it into there for goodness sake, right? It's an absolute joke. Another one, just coming 45° out

**Dave Jones:** of here. It's That's just stupid. No, you drop that straight down to there. And having these just like go into the corner, but no, you have it coming out and then you branch up like that out and you branch over like that. Oh, come on,

**Dave Jones:** seriously? And what the heck's going on over here? Look, it's That's going into there. It's like they they haven't treated it as like the one physical net. Like they've just, you know, treated it as different routing paths to take. This is just terrible,

**Dave Jones:** absolute amateur hour, right? I got No, it's got no idea how to prioritize and route a double a simple double-sided PCB. And look at the bottom here, right? As a human laying out a board, right? You try and like get it all on the one

**Dave Jones:** layer and then the stuff that you can't put on the one layer, you would put on the bottom cuz then you'll have them you'll be able to maximize your ground planes, you'll be able to get your power around and, you know, uh, stuff like

**Dave Jones:** that. So, you notice I don't actually have that many like traces on here. Really, it's just actually joining some chips together and going horizontal, um, like that, basically. And as you saw, all my uh, top layer is just all vertical stuff,

**Dave Jones:** mostly vertical stuff. You know, there's a couple of horizontal here that joins some of the, uh, like the common, uh, clock pin or whatever it was, uh, down here. But, you know, that's about it. I mean, this thing has no clue.

**Dave Jones:** To be fair though, of course, it it it didn't know our intention, but even then just some of the stuff it's doing is just is just awful. Look at this, right? It's just jagging off there. Why not just go like that, right? It's just end

**Dave Jones:** this. Just branching off there like that. It's just no, absolutely awful. And it knows, right, that all these resistors should be connected like this, okay? And this is what I've done on my board down here. You can see I've just

**Dave Jones:** joined them all together as a priority. Not cuz it doesn't know it's a high voltage trace and all that sort of stuff, right? And then like it comes down here like this and then branches up and then whoop, wiggles back like that

**Dave Jones:** down and around. And it's like, what? And then they've like caught themselves in a corner here. No. No, no, no, no, no. And there's more weirdness happening around here and here. What's going on there? That's just dumb. Oh, and then

**Dave Jones:** this going up like that and then down. Oh, it's just it's awful. Now, to be fair, the Altium one I guess is not a huge amount better. There's some, you know, stuff around here. You'll have to go watch my uh previous uh video. It's

**Dave Jones:** got some reverse jaggies in there and, you know, some weird branch offs and a maybe a little overlap in there. Sorry, I can't uh zoom in on this. Don't have the original file to hand. Um it's yeah, but no, like it is certainly it's

**Dave Jones:** it's no better than a traditional auto router like this. It's just no. So, yeah, I'm very disappointed by this AI. It is just really dumb auto router stuff. There's nothing AI about it at all. There's no like it like it learns

**Dave Jones:** from its own routes. That's why it does it like multiple times or something. I would have like expected multiple times for it to figure out, oh look, there's some association, some, you know, grouping associates, some tight association over here. And if I go into

**Dave Jones:** the individual traces, we might actually be able to see, um, you know, like some issues where like it it just plainly has no clue what it's doing. It hasn't learned It looks like it hasn't learned a thing. So, I can't see any advantage to using

**Dave Jones:** this over, you know, a traditional auto router, which is based on decades and decades of refinement for various algorithms. And you can set it up with tell it different algorithms, how many layer board you want, do you want, you

**Dave Jones:** know, horizontal, vertical priority, and you know, all sorts of different algorithms you can actually select in any good auto router. You can actually select an optimal algorithm for it. But, yeah, this thing's just it's it's terrible, Muriel. That's

**Dave Jones:** that's a complete and epic fail. And did it just give up and couldn't complete some of the routes even though they're like really obvious stuff, like, you know, going through here, like this. I mean, like it's just, you know, it's

**Dave Jones:** they're taking one trace through there, and that just chopped off everything else, right? And like a human's just going to know this stuff. Even if the human auto router, and this is quite common in the industry, actually, where you just have

**Dave Jones:** a PCB layout person. They didn't design the schematic. They've got no idea. They might even have no idea what the thing does. I know a lot of superb, um, old school PCB designers who come from a drafting background. They've got

**Dave Jones:** no idea about electronics, but they can see when you have the rats nest, they can see the groupings up here, like this. Like So, deep PCB AI, huge thumbs down. I expected better. It's it no, no, I wouldn't bother using it.

**Dave Jones:** Yeah, just go back to your traditional auto router and just let it loose on very specific requirements that you got you know a board like this you take some pride in your work lay it out yourself and it can be you know quite

**Dave Jones:** nice like this with minimal you know number of traces on the bottom going higgledy-piggledy and then you got priority to your high voltage higher priority traces like the high voltage one and other you know stuff you can set up as a priority but anyway and

**Dave Jones:** now I I expected better than that for a machine learning system that's supposed to learn from all those more 48 passes it did and it still couldn't figure out priority of stuff so very poor anyway if you found that video

**Dave Jones:** interesting please give it a big thumbs up as always discuss it down below and over on the EV blog forum and catch me on all my alternative channels I'm on the Odyssey's I'm on the Utreons I'm on the bitchutes I'm on the rumbles I'm on

**Dave Jones:** the no no I think I'll stop being on daily motion anyway I'm everywhere even on the EV blog.com old school you can get the RSS podcast feed of this thing which comes video comes directly from my own server been doing that forever

**Dave Jones:** catch you next time
