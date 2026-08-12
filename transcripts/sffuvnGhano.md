---
video_id: sffuvnGhano
title: EEVblog #975 - Human vs Autorouter
url: https://www.youtube.com/watch?v=sffuvnGhano
source: youtube-asr
---

**Dave Jones:** Hi, just a quick follow-up to my uh previous video which I'll link in down below if you haven't seen it where I basically uh took you as a walk through through the entire process of laying out this uh Nixie tube uh PCB that I've done

**Dave Jones:** here. And uh that was like an hour and 20 minutes worth and it was it seems very popular. But one of the uh common questions I got was a lot of people wanted to know uh what would the auto

**Dave Jones:** router produce? what this layout would look like if we actually let the Alium auto router run on this thing. And I thought, well, that's an interesting question. So, I thought we'd take a look at it. So, here is my manual uh layout.

**Dave Jones:** And it's it's fairly neat and tidy. It's not the most optimum uh optimal thing in the world, but uh you know, look, it's got the high voltage bus along the top there for the 160 volts or whatever. It's got the ground plane in there. It's

**Dave Jones:** got the um the serial clock lines, you know, going right through like that instead of hickledy pickledy all over the board. So, you know, there's a couple of, you know, nice manual routing uh touches in there. And as people will

**Dave Jones:** know, I'm not a big fan of auto routers. I don't suggest you use them, but there are times when selectively actually when I was a professional full-time PCB layout um engineer, I would often selectively use the auto router. So, I'd

**Dave Jones:** you know auto route certain parts of it. Never ever professional PCB designer does not auto route an entire board, but they use it selectively and sometimes you can spend hours or days setting up the auto router to do, you know,

**Dave Jones:** precisely what you wanted uh it to do and it can actually help in those regards. But people wanted to know what would happen if I just let the auto router rip on this board. And I thought, well, you know, that's interesting.

**Dave Jones:** Haven't used the auto alium auto router for years. This is the new the latest um Alium Designer 17 that I've got in installed here. The full package. This is not Alium Circuit Maker or Circuit Studio. It's a full professional Alium

**Dave Jones:** Designer. Now, Alium have never had the best auto router. Um the Citus auto router, I think they're still calling it. It's always been pretty me, you know, um it's hasn't got a lot of uh fans, but I thought, hey, we'd give it a

**Dave Jones:** rip. Um, so what I've done here is I've uh uh just made a duplicate of the board. So I haven't changed anything, but I've simply unouted everything. And that's what you can go. You can just go unoute all uh nets, and it just gets rid

**Dave Jones:** of everything. Um, and so that's what I've done. I've gotten rid of everything. So I'm actually going to let it do the whole kitten kaboodleoodle of the grounds, the power, everything. The grounds are going to be horrible. It's

**Dave Jones:** going to be ground traces everywhere. It's going to be a mess. But I thought we'd run it exactly the same circumstances and compare my manual route with the auto routed version. So let's give it a go. So the first thing

**Dave Jones:** we're going to want to do is go into uh route up here. Auto route. There we go. And uh we want to auto route all. Now I would love to uh simply exclude the uh you know the ground net or something

**Dave Jones:** like that. We might be able to do that. I haven't set up any net classes or anything like that. But anyway, we'll go into auto route all here. Um, now I've got my uh the rules I had before. 15

**Dave Jones:** thou clearance and uh 10 thou track. I've got my uh via set up exactly like I had it when I was doing the manual routing. And you can go in here and you can edit all of the rules. You know, you

**Dave Jones:** can go in there the routing via style and the clearance and all that uh sort of jazz. But I've um I've got that all um already set up as per my manual route. So it should be identical. And

**Dave Jones:** we've got several uh versions here, like several different uh pre-builtin algorithms. The default two-layer one, default two- layer with edge connectors, default multilayer, general orthogonal. Um we'll just go with the default two-layer board because that's exactly what we've got here. But yeah, you can

**Dave Jones:** go in and you can edit all sorts of stuff. Um you can lock any pre-outs uh down here that you uh might have had uh for example. So, if you already have partially routed the board, you don't want it to rip up your stuff and things

**Dave Jones:** like that. But, we're going to do the whole thing. So, here we go. I am going to run this entire auto route. Can I actually uh clear clear all messages? There we go. So, the messages up here um

**Dave Jones:** should show up while it's auto routing. So, let's just go ahead. We might be able to do some more optimized uh routes and stuff later, selective routing and things like that, but let's just go run it all and see what it gets. It'll might

**Dave Jones:** do a half reasonable job for a lot of stuff, but I expect the grounds to be awful, of course. Um, and uh, you know, probably traces running all over there. Maybe it won't even complete, uh, the route or whatever, but uh, we'll give it

**Dave Jones:** a go, shall we? So, here we go. Where are we? Default two-layer board route. All go. Silver Sovereign, go. There we go. Routing 81 of 237 connections routed. It's already at 50%. Um, is it really? Doesn't look like it, but uh you

**Dave Jones:** can see like grounds around here. You can see those like that. That's actually grounds. They're they're actually they're actually grounds. Look, it's doing a horrible job of this ground. Like it's just ah it's complete balls up, right? Um so you don't want it to

**Dave Jones:** route grounds. Typically, as you saw when I was doing my manual routing, you would only want it to uh you know, you leave the ground until last and then you flood fill that in later. You actually polygon that fill that in. So, it's not

**Dave Jones:** um helping that we're actually routing the grounds here. This is why you just never go route all on your board unless you absolutely have to have it done in five minutes and you just didn't give a rat's ass. Um then that's the only time

**Dave Jones:** that you would uh route all. So, you definitely wouldn't want to route your grounds, but power, of course. Yeah, you'd want it to route your power. And uh but you can see that trace going that that red one going here. This is this is

**Dave Jones:** all just ground. I mean, it's just like it's cutting off pads and doing whatnot. And it's not going to be great. But here we go. It's already got some contention up here. You might see some traces like overlapping each other. It'll tidy all

**Dave Jones:** that stuff up uh when it's done. But uh yeah, so now it's, you know, it started off all guns blazing and now it's uh it's really trying to figure it out. And you can see the uh rat's nest changing

**Dave Jones:** there. But you know, it's looking like if you take away the ground issue, it's looking like okay, you know, it's doing something. It's not going too horribly uh wrong at the moment, but uh it'll be interesting. Yeah, we definitely want to

**Dave Jones:** um set up, you know, you might want to set up net classes only do selected uh nets and things like that. You can like route an individual component for example um and stuff like that. So if ideally if I was setting up this and

**Dave Jones:** wanted it to do auto routing, I wouldn't include uh the uh ground of course. I probably wouldn't include the power. I'd probably route the power myself. I'd um actually uh pre-eroute the power and then I would just leave everything else

**Dave Jones:** on its own. Um but yeah, we're getting there. 207 of 238 connections. Uh starting layer pattern. So this is the general two layer algorithm it's using. And you know, you can set up Oh, by the way, I forgot to show you. There was um it's

**Dave Jones:** set up for automatic direction uh on both the positive bottom top and bottom layer, but uh with an emphasis on the vertical direction for the top layer, which is the red one here. And you'll notice that it's doing mostly vertical

**Dave Jones:** stuff with the red there in terms of like going to the Nixie Tube and stuff like that. And it's kind of doing more a horizontal emphasis on the bottom layer, which is the uh blue layer there. So apart from that uh red ground one we saw

**Dave Jones:** there, it's generally following those rules. So it's doing it, you know, in the same way I would have approached it uh manually and I did approach it manually routing this thing. The top layer I did most like vertical and then

**Dave Jones:** the bottom layer I kept for more horizontal uh type stuff. So here we go. It's struggling. It's struggling. I'm screen capturing. I've got an i7 760, you know, 3 and a half gig, you know, decent uh computer here doing this

**Dave Jones:** thing. Um, but you know, auto routing takes time. But hey, if it works for you, it can actually save you some time. And as I said, selectively auto routing stuff has worked in my professional uh experience laying out stuff. But I never

**Dave Jones:** would let it do this amount of, you know, a full board or anything like that. But hey, if you had to have this board out in five minutes, it it would work, right? It' kind of, you know, it's

**Dave Jones:** low frequency stuff. It'd be awful. You know, you wouldn't take pride in it. But if you just had to get something lashed together for a oneoff thing that you had to absolutely send away today, you know, or in the next couple of hours, yeah,

**Dave Jones:** you know, you might let it do this. And uh well, you probably have no choice, right? Because to manually route this might take, you know, 2 3 hours or something like that. and if you had to send it away uh with an hour's notice

**Dave Jones:** cuz then you'd miss the deadline on the PCB manufacturer and you wouldn't get a blah blah blah blah blah um then you know sometimes you may not have a choice or if you simply don't care trust me learn to care take some

**Dave Jones:** pride in your layout. It's an artwork. We're almost there. 227 of 238. And I may as well waffle on for the rest of it because we're we're getting there. And well, you know, it doesn't it's not like, you know, there's all

**Dave Jones:** garbage down in these dead spaces here. It's sort of, you know, said, okay, well, you know, I don't need to route ridiculous stuff all over here. And it's it's doing okay. Well, you know, this right angle crap in here, it might do a

**Dave Jones:** might do a cleanup uh pass at the end or something like that, but uh it's doing okay. any screen capture software is going to slow this uh down as well. Of course, it could easily double the time uh that it takes just because it's got

**Dave Jones:** to uh screen capture this whole thing in the background, but come on, you can do it. You can do it. Alium Citus auto router. I It's kind of fascinating to watch it go though. I do enjoy watching out auto routers do their thing and but

**Dave Jones:** no, there's all I'm always going to have an issue with it. Um, regardless of what you know what end result, there's always going to be something pretty horrid in there. But electrically, everything should be fine because it's going to meet the design

**Dave Jones:** rules, the clearance, the trace widths, everything else, and all the nets are going to be joined. Suppose sometimes it just will back itself into a corner because it doesn't know what it's doing. And, you know, it it's just given up

**Dave Jones:** ripping up uh traces and rerouting them. And it and you know there might be uh cuz this is a little bit tricky in terms of like cross tracing you know traces going off that way and this way and

**Dave Jones:** crossing and stuff like that. So it might uh not be able to complete a couple but uh here we go 231 of 238. So it's really taking its time with these last ones because of all the congested space in there. You know it's just to

**Dave Jones:** solve one now takes time. 232. There we go. Actually I'm I'm going to stop now. I'll come back when it's done. We are done. And routing finished with zero contentions, but it failed. There you go. It failed to complete six

**Dave Jones:** connections in 7 minutes and 41 seconds. And you can see the ones that it's actually failed to do. You can still see the whites rat nest here. So rat's nest. So look, I mean like like it didn't even

**Dave Jones:** try to get. Come on. I can I can see easily. My human mind can see where that's easily going. these two ones. It could easily go up here like this. And then look, they can even get Look, there's a direct path right up here.

**Dave Jones:** Right around here. Just move that a bit. And boom. Bob's your uncle. Look at that. I mean, it's ah like like that's too easy, right? And it said I couldn't complete that. And likewise this one here. Look, it couldn't figure

**Dave Jones:** out how to get this trace up here through here through here like this. Because this one, you can't fit two between these pads just because of the clear clearance rules. Anyway, even if you didn't have to, this one could have

**Dave Jones:** moved as you know, my human mind says, "Okay, look, this one instantly can move out here like this, even if we had to go through here." But it couldn't figure out how to get through there, get through there, shove this over a little

**Dave Jones:** bit, and then go connect there because it got caught on this via here, right? It just got completely caught and didn't want to. it determined that it had to move too much stuff and do too many things and make too many decisions to

**Dave Jones:** move that via up there, you know, uh like Yeah. whereas I just tidy that up in a minute or two, right? Um fixed as a you know, a human router. So like and and this one maybe you know this one,

**Dave Jones:** no, you drop a via down to the bottom. See this one here, right? I haven't even looked at the rest of it. this one here. I would immediately, how I'd fix this, immediately drop it here uh on the top

**Dave Jones:** side. Drop it down to the bottom side. You can see we can route this trace right up to here. Then I'd bring it to the top side again. Keep running the trace up here. And where does it have to

**Dave Jones:** go to? It's got to go to that one up there. Okay. So, I would have dropped it back down here because we're boxed in. We dropped it down here to the bottom layer. Take it up here and then take it

**Dave Jones:** to the top side again. And uh here. and we have to get it around to there. But even, you know, you drop it down again, another layer and take it across. I mean, you know, I could fix that in 10

**Dave Jones:** seconds, right? So, yeah. And look, it's, you know, it's left these horrible angles like this. I like I hate this. That's that's just an acid trap. um as they call it in the uh business when you put it into the um e acid etch bath then

**Dave Jones:** you know the acid can bubble around in there and it can ex etch away excess uh stuff on there. A professional PCB designer would not have a back angle like that. I mean 90° angles are generally frowned upon just because

**Dave Jones:** right even though you know this like acid traps generally aren't a big deal these days with modern uh etching techniques and stuff like that. They've done it down here as well, but you know, it's just like if you did that, if

**Dave Jones:** you're a professional designer and you submitted for designer review a board that looks like that, you know, you you just get laughed at or get the sack or something, you know, no professional designer is going to have angles like

**Dave Jones:** that in their board just because um yet this like it did it just fine. And where's Oh no, look. See, look at this. Two traces shorted overlapping each other. Ah, that shouldn't that have shown up as a contention or whatever?

**Dave Jones:** That's ridiculous, right? It's completely screwed up there. So, like down here as well. What the hell? Oh, sorry. That that's VCC. That that's the same net. Okay, but that's just like it's horrid, right? And and why is it

**Dave Jones:** determined that it needs two traces in here for the ground? I mean, that's just it's just ridiculous. And what's going on here with this angled trace like that? I mean, come on. It should have stuck. I'm I pretty sure I've got like

**Dave Jones:** it's done like you know the 45 uh degree angles and everything for most other stuff like some of it's not bad you know like you know these down here and stuff like it's it's doing a reasonable job but there's just a lot of messiness in

**Dave Jones:** there like yeah anyway and there's six routes it couldn't uh complete even though it's trivial um to see like this one here give me a break like instantly with like just a One second glance I can see that you can bring this trace up

**Dave Jones:** here like this. Bring it around outside here. Up. Hang on. Sorry. Yeah. Up around here like this. And bingo. Oh, and and back through here and to there. I mean that that was like like like a half second glance at that showed me

**Dave Jones:** where that route was obvious, you know? So bloody computers. Ah, I'm not worried about the uh the singularity. And of course, the other uh auto routing thing you can do is to route individual nets like this one that didn't uh complete

**Dave Jones:** for example. So you can just go uh auto route and then you can uh go individual net. So just one net at a time, you know, if there's one pain in the ass thing that you got to get from one side

**Dave Jones:** of the board to the other, then often it can be handy if it's a non-critical trace just to let the auto router do that. So we can give that a bell to see if it can uh see if it can do that.

**Dave Jones:** Thank you very much. And yep, it it did it, didn't it? There we go. It went down there with a horrible little right angle thing there and a little turd there and a you know, but then it jumped over to

**Dave Jones:** here and then it jumped over to there and down to there. But see, it did that. Why it couldn't do that as part of the auto router? Why it said this was the completed auto router board. Why it said

**Dave Jones:** it couldn't complete that un unoutable when it could easily just go ahead and do it as a single route. eh it's you know algorithm fail and there's a whole bunch of other auto routing uh stuff you can do uh you know areas rooms uh the

**Dave Jones:** net classes as we've taken a look at component classes and all sorts of stuff you can set up individual rules for each one and it can get quite complex as I said a professional using an auto a selective auto router on a really you

**Dave Jones:** know important complex uh board would you know spend many hours just you know setting up and make sure and they get the auto route to try it. They might even give it a couple of goes and stuff like that. Um to you know using

**Dave Jones:** different rules to you know see if they can get it to do it. But this is bloody mess. Don't like look at this. Look at this. Routed down to here. What the Yeah, they're the same net. Okay. So

**Dave Jones:** they're allowed to be on top of each other but Oh that's that's the clock line. Okay. So this is one of the clock lines. Look at this. So, you know, my nice one, for example, like you go over

**Dave Jones:** here, okay, select um well, hang on. Boom. And then tab. There we go. Like my one, you know, you saw that me route that in the video. You know, those nice two traces that you might route these before you actually start your auto

**Dave Jones:** route. Uh, for example, letting your auto route rip. And look what it's done. I mean, it's, you know, it of course you can force it to prioritize this and and stuff like that. You can get real complex with your rules and stuff like

**Dave Jones:** that. If you thought that trace was important, but look what it's done. It's gone up here. It's route switch back like that. Jeez, it's not a bloody railway layout. It's like this looks like a classic rail layout, not a bloody

**Dave Jones:** PCB auto route. Anyway, so what we'll do is we'll just unoute all and start again. Okay. So, what I'm going to do now is do that exact one again, but not route the ground in here. Now, Alium should make this easier. And

**Dave Jones:** maybe they have. I haven't been out using uh 17 for a while, so maybe there's a simpler way. But uh basically, we need to go into um classes here and we need to set up uh different net classes. So, what I've done is I've got

**Dave Jones:** all you know before like all by default every net goes to all nets and that's what we were routing before. Um but now I've set up all but ground. So I've put in every net in there except ground. So

**Dave Jones:** I've removed ground from there and ground just sits in its own uh net. So now we can actually instead of routing the entire board we can route just that class. All right. So here we go. Auto route and instead of all or individual

**Dave Jones:** net we'll route a net class and we can select all but ground. There it is. So, I'll select orbit ground and away she goes. And you notice, remember before it actually did the ground uh one first. It hasn't actually routed the ground. So,

**Dave Jones:** now it's doing the power because we want our 5V uh power cuz we don't this isn't a multi-layer board. We don't have our power planes and uh stuffs like that. So this this you know it might get to 100%

**Dave Jones:** uh completion now that we've actually uh you know taken out the grounds from this cuz we can fill in those later with polygon pore and uh you know tidy it up. So let's see what it does with just the

**Dave Jones:** main nets here and the VCC which I think is a you know so this is quite a re realistic scenario. If you asked me to auto route this board I had to do it in the next hour. This would probably be

**Dave Jones:** how I'd do it. So, I'll come back and we'll check out the end result. Now, I'm not sure why it keeps popping up with uh this. That's rather unusual. Does anyone know? Haven't encountered that before. But then again, I don't do much auto

**Dave Jones:** routing. And again, what's going on here? It's like, all right, this is getting ridiculous. This is getting unusable. It's almost as if it's popping up after each uh net is routed. That's just it's just nuts. The hell? No, it's just not

**Dave Jones:** incrementing at all now. It's still stuck on a net 170 of 238 and it just keeps popping up. It's just like what? I don't get it. Am I doing something stupid or is this thing just not working? No, I have to give up on

**Dave Jones:** this. It is not uh progressing beyond 170 of 238 connections. It seems to just be spinning its wheels on the exact same problem there. So, I'm I'm going to have to call that I'm going to have to call

**Dave Jones:** that quits. That's just nuts. Rounding finish with 11 contentions failed to complete 68 connections. Well, no [ __ ] Sherlock. Well, that didn't work at all. Yet, as far as I know, that is the way that you would do it.

**Dave Jones:** Um to, you know, to do everything but ground. You just auto route the net class and it should just do everything. I mean, can't even route that. Give me a break. Like, I No, it's it's crap. What? Anyway, like, you know,

**Dave Jones:** there's some probably some reasonable routes in there. If you had a look of them, you know, half of them might be, you know, re like this one here is quite reasonable what you do yourself kind of thing. But like, no. Like, that's a

**Dave Jones:** fail. Ridiculous. All right, let's just try another auto rounding technique. called selective uh auto routing where let's just select two components like this right and uh this would be quite uh you know common for a professional uh layout person to do this in a bit more

**Dave Jones:** detail setting with more strict rules and everything but let's give it a go. Okay, now what we got we can uh we can have just auto route the connections on the selected components or the connections between the selected

**Dave Jones:** components. So let's just do some between the selected components first. Once again using all the same rules that we've already been uh using. So let's give that a go. So it'll only route auto route those. There you go. And of course

**Dave Jones:** it didn't uh it didn't touch the uh uh you know it well it did the grounds between the pads there. So once again we had to we probably have to set up you know classes and all sorts of other

**Dave Jones:** things. it didn't let us exclude a class from just these two which is kind of you know annoying. Uh so we wanted to do that ideally we wanted to do that with a restriction on classes but anyway so

**Dave Jones:** we've individually routed that so let's actually undo that and it's done a I don't know you know half reasonable job there right for those few connections unoute all and let's try that again actually let's select those but let's

**Dave Jones:** auto route uh on selected components so it should also do the connections between this other chip over here as Well, and it'll do the clock lines between those two chips. Uh hopefully it should connect on selected components. So, let's try that. There we go. It's

**Dave Jones:** started to do this uh U2 chip here. See? So, we can just have it select those things. So, there's no reason why you can't go in there first and do like all of your clock line, for example. Put

**Dave Jones:** your clock line in there, put your ground, like, you know, stuff like power supply. You wouldn't auto route a power supply. you just you know put those traces in yourself, take at least a minimum of pride in your work there and

**Dave Jones:** of course you'd exclude grounds and then just you know like auto route just uh the logic connections. This is a classic why it's um important like if you got a really dense huge board with lots of you know digital logic and it's not

**Dave Jones:** particularly high speed there's not high-speed design rules and differential pairs and all the fancy fancy stuff right then you know often you just let it rip for example just let the file rip on uh you know a particular uh board if

**Dave Jones:** the signal integrity wasn't critical between two chips and things like that yeah just have at it the problem with doing selective routing like this um without having to have done, you know, pre- routes first and things like that

**Dave Jones:** is it's going to, you know, lock you in. It's going to block you in much further down the track when you start doing uh more routes and things like that. So, you know, that's why a good PCB uh

**Dave Jones:** layout person is worth their waiting gold because they'll be able to think, you know, halfway across the board ahead, you know, a thousand routes ahead and go, "Oh, I need to leave space for that." And you know, you don't have to

**Dave Jones:** dick around setting up rules. It's just all kept in your head and things like that as you s saw on my previous video. But of course, you know, it takes it does take more time to auto route uh

**Dave Jones:** sorry to manually route a board of course, but you're going to often get a much better job. But, you know, auto routers can be useful in selective uh scenarios and just getting something. As I said, if you need to needed to have

**Dave Jones:** something out the door, you know, it's 3:00 and you need to send out that file by 4:00, then you're not going to be manually routing the thing, uh, you just want to get something sent out, then, you know, you can auto route it and at

**Dave Jones:** least you'll have something um, you know, to build up, you know, mock up a prototype with and hopefully get the thing working. But yeah, they're not terrific. But Alium is not the best auto router um, algorithm out there. Not by

**Dave Jones:** far. In fact, some people consider it the worst or one of the worst auto routing um engines out there. So, yeah, all you auto routing fanboys, you know, flame away that, oh, Eagle's better or this is better or that's better. And of

**Dave Jones:** course, you know, you have to do exact sidebyside comparisons. I'd have to lay this out to do a real shootout between algorithms. It have to be laid out precisely on exactly the same grid components, all exactly the same

**Dave Jones:** footprints, everything with uh the exact same uh nets and layout, the exact same rules, everything else to you know it it's got to be apples 100% apples to apples or it's just not worth uh comparing auto routers really. So

**Dave Jones:** basically there you have it side by side an auto routed board fully auto routered board on the top there including all the grounds and uh the power and my manually routed uh board down the bottom here. And well it's not terrific of course um

**Dave Jones:** you know there's lots of horrid things in there. There's lots of stuff you got to tidy up and there's six missing nets which it couldn't do which were absolutely trivial which is uh should have been able to handle but you know

**Dave Jones:** you tweak the algorithms you know you maybe include some selective auto routing you probably can eventually massage it into doing a reasonable job like um you know a half competent uh uh manual route down the bottom here. But

**Dave Jones:** if we take a look at the bottom side here, you can see how, you know, I manual routing, I did very few on the bottom. I really tried to optimize everything on the one layer. Whereas the manual uh the auto router just went,

**Dave Jones:** "Hey, I've been given two layers. Let me add it." Even though I did try to prioritize the horizontal ones on the bottom layer and the vertical ones on the top, it didn't do nearly as thorough a job as I did uh manually here. So

**Dave Jones:** that's why you end up with all the crap on the bottom. And then if you tried to uh you know fill the tidy this up with the ground plane, go in there and select your uh ground for example and then uh

**Dave Jones:** you know get rid of all that and um yeah look it hasn't even routed grounds on these other chips. So you know that's just nuts. Um so you know if you wanted to ground fill that then there's nothing

**Dave Jones:** there's no space left to do it. You have via jumpers everywhere on your on your ground. So, it's it's not terrific. Auto routers aren't great. They are very very powerful tools used in the right hands under the right setup conditions, but

**Dave Jones:** you know, the myth of just being able to route your entire board unless it's ridiculously simple. You know, it's just going to produce a horrible result. So, there you go. I hope you like that little quick look at Alium auto router

**Dave Jones:** technology and on a you a fairly average double-sided uh board of sort of smallish uh complexity with a few little tricky uh cross routing stuff it had to deal with and yeah it didn't do a great job at all. Anyway, if you like the

**Dave Jones:** video, please give it a big thumbs up. Catch you next time and go on all you auto routing fanboys, have at it down below.
