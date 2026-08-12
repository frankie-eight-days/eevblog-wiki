---
video_id: 2zGisPMNstI
title: EEVblog #552 - DFM Automated PCB Panel Testing
url: https://www.youtube.com/watch?v=2zGisPMNstI
source: youtube-asr
---

**Dave Jones:** Hi. Previously, I've done a video on design for manufacturing your circuit board, i.e., how to mount it in a panel such as this for production. And I'll link that in down below. It's been incredibly popular, one of my most

**Dave Jones:** popular videos. But so this is a kind of a follow-up to that in how to add some automated test functionality to your particular panel to help in testing your final product. Because what people will do with their panels if they're you

**Dave Jones:** know, a beginner or they're being lazy or they're not doing a huge run and they don't want to invest in an automated test system. That typically they'll put it in a panel like this. This is pretty essential for when you're getting your

**Dave Jones:** boards manufactured, especially for small boards like this. So when it goes through the pick and place machine, instead of just manufacturing one tiny board at a time like that, you can actually pick and place all the parts at

**Dave Jones:** once. So there's real big advantages to doing that. And most people do that if they're going for any sort of reasonable quantity, putting them through a pick and place machine. But often unless you're doing you know, tens of

**Dave Jones:** thousands or hundreds of thousands, you don't often invest in an automated test system to actually plug onto the thing. But as we'll see today, even for my micro current, I'm doing a new version of this. I thought I'd just add a test

**Dave Jones:** connector on the side of my panel here just to help out and just you know, smooth that testing process. Even though I'm not making tens of thousands of these things, um it really is simple to add just some basic features to your

**Dave Jones:** panel just to simplify your testing. So let's go. Now here's an example of an ATE connector, automated test equipment connector, designed into a commercial product. And this is something that I worked on a few years back. And you'll

**Dave Jones:** see that on the edge of the product here, which is actually hidden normally hidden to the user by way of uh know, uh mounting rails and things like that. You don't ordinarily see this, but it's got a card edge PCI connector built into

**Dave Jones:** there. Yes, it's the same PCI connector uh you'll find in your PC. Now, the good thing about uh PCI connectors is that, you know, they're standardized, they're good for a large number of insertions in terms of uh you know, the test

**Dave Jones:** connector. If you're testing thousands of these boards, you don't want to have to replace your connectors all the time. And we'll uh see that in a minute. And the other good thing about a large PCI connector like this, it has a lot of

**Dave Jones:** connections. It's got all those on the bottom as well. So, and you can transfer power and lots and lots of data and test signals. And that's exactly what happened on this particular product. We sort of uh in the design process of the

**Dave Jones:** product, routed out all of these signals out of here, sort of you know, in parallel with all sorts of other stuff. And there were dedicated IO pins coming from the processor and FPGA to uh enable this functionality, which was designed

**Dave Jones:** into the product from day one. Now, of course, we could have just used a you know, 0.1 in header or something like that. And that's okay if your board is designed to be uh you know, it is is not

**Dave Jones:** going to be visible to the public, then that's fine. You can design it in. But the thing about uh header connectors and other off-board interconnect connectors is that you've got to physically plug a cable into them. And that's a step that can go

**Dave Jones:** wrong. You can bend pins, it's messy, it takes time. So, this card edge PCI connector, what this allowed us to do is actually mount this board on a sliding rail system. And here's one that I uh hand-built. You just uh slide the board

**Dave Jones:** on top, and then uh with a big handle on the side, just push it into a uh purpose-designed uh test jig board on the side there with the PCI connector mounted on it. and that works really well. It's very quick, it's very simple

**Dave Jones:** and these card edge connectors here, you don't need a really hard gold plating on these like you would on a normal expansion card for example cuz this is only designed to be used once during the manufacturing test and then that's it.

**Dave Jones:** This connector is never used again. So you wouldn't be wasting your money on hard gold edge plating on those connectors there. So here's the automated test board I designed for this thing and I've taped up a few things

**Dave Jones:** just to protect the innocent here and basically it had a processing module on here so it had its own local processing and it was designed to basically perform most of the testing in combination with a test special test script which was

**Dave Jones:** downloaded to the product under test that plugged in. So I had one big main board here which mounted on the chassis. I just got some mounting points because you don't make many of these. You don't really, you know, this is not like a

**Dave Jones:** product. You might make say five or 10 of these for a large production run or something like that. You'll test, you know, you'll have five or 10 operators or something like that testing boards as they come off the production line. So

**Dave Jones:** that's about the number we had here and it's got various programming interfaces, you know, power off on. It's just powered from an external plug pack or its own local regulation. And down the bottom here, it's most interestingly it has all of the

**Dave Jones:** pass fail functionality down here. So all the different tests which were stepped through and some, you know, some spare just in case at the end of it and it's got pass fail LEDs for each one. So these would all be populated, you know,

**Dave Jones:** red LEDs for fail, green LEDs for pass. So however many minutes it took it would just tick through each test and you'd see each LED come up red or green after you press the test button. It basically handled everything. There's a switch on

**Dave Jones:** here to apply power to the device under test. Here Here's the test interface connectors over here. We'll take a look at how it can measure the board current as well. You can see a current shunt resistor. Oh, sorry, that's a That's a

**Dave Jones:** poly switch to protect the board from any overload. Then it's got a current sense resistor, little current sense amplifier, so it can actually measure the current. That's all part of the test as well. It's going to have a little LCD on here.

**Dave Jones:** So, you know, just a two line by 16 character thing so that you can get status. That's pretty handy. And as I mentioned before, the number of insertions. Because these test jigs have a finite lifetime of the test connector

**Dave Jones:** over here, you basically look at the data sheet for your connector and it might say 1,000 mating cycles, right? So, you would maybe you wouldn't go that far. You might go, "Okay, I'm going to set it to 500." So, this would just be

**Dave Jones:** one of those little LCD counter modules that every time a board is tested, just increments that counter by one. And then once it gets to a set number, then you can you know, stop it to testing or you can warn the

**Dave Jones:** operator or whatever to change this test board. And the test interface boards over here, here we go, just start pointing basically converts that PCI connector on the side to 0.1 inch ribbon headers, which then connect over to the

**Dave Jones:** main board here. So, it allows you to mount this test interface board test connector board vertically so that you know, on that sliding test jig I had there. And then just easily connect over to the 0.1 inch header connectors. And

**Dave Jones:** there's a test board which we plugged into the product under test to enable some loopbacks and other functionality. But that's just an example of a typical automated test jig for a specific product. And if you're serious about production of any product, then an

**Dave Jones:** automated uh, system like this is absolutely vital to ensure that, you know, speedy and quick testing of your product under test. Especially, you know, you're trying to build a low-cost product, for example, you don't want to manufacture your product for 100 bucks,

**Dave Jones:** and then it costs you $100 in time to test the thing. Um, you know, even at cheaper labor rates, if there's a lot of testing that needs to be done for the thing, then or you even 10 bucks worth

**Dave Jones:** of testing, you want to minimize that time. So, if you design testing into your product to begin with, or into your production panel, then that can really help a lot. In this case, it wasn't a production panel, it was the

**Dave Jones:** finished board. So, with my previous microcurrent design, I've done videos, which I link in down below, of me actually, uh, testing this thing, and it was quite time-consuming, cuz yeah, I produced it on a panel like this, which

**Dave Jones:** is efficient for manufacturing, of course. Uh, 5 by 2, 10 boards total. But, you know, I'm lowering my costs there, but in terms of testing, these things had to be individually broken out of here, and then tested at the

**Dave Jones:** individual board level, after inserting the battery on the back for each one, for example, and then you've got to operate it, then you've got to plug all the leads in and out. In this case, I've only got a small number of connections

**Dave Jones:** to at the top, two at the bottom here, but even that would be a pain in the ass to plug leads in, those four leads, and you've got to do it if each unit. So, that's why I've shown this in a previous

**Dave Jones:** video, where I designed this little, uh, test jig, where I could just take my finished board, and just plug it on top like that, hold it down, and then, uh, run the test, and that was it. It was,

**Dave Jones:** you know, reasonably efficient, but, uh, still, I had to go through and manually flick the switches on each one, and it didn't allow me to, uh, you know, test, uh, some things, cuz it was powered from the battery under test, and things like

**Dave Jones:** that. So, it was okay, that really reduced my production time, but, uh, considering I'm doing a new version of this board, I would like to design a bit of functionality into this panel so that I can possibly test all 10 at once while

**Dave Jones:** they're in the panel and without having to plug the power into each particular one because you may like there's nothing worse than if you're not shipping this product because it contains the lithium battery then nothing worse than having

**Dave Jones:** to insert the battery, do the test, and then remove the battery again before you ship the product. What a pain in the ass. You're just wasting time and money. So, what I'm going to do is integrate some functionality into this panel so

**Dave Jones:** and into my individual bare board so that I can do you know, not quite test 10 at once. It's not going to be that automated. I'm not going to go to town on this thing for various reasons, but

**Dave Jones:** just allow me to speed up the production a little bit more over this dinky chitten test jig I've got here. So, remember when you get a panel manufactured like this, a panel is just part of the PCB. So, you can put traces,

**Dave Jones:** you can even put circuitry, connectors, and all sorts of stuff on here outside your product and you can get signals on and off your board, but in this particular case, I didn't. I actually V-grooved these old boards here and if

**Dave Jones:** you do V-grooving, yeah, it's cheap and simple. You can just snap off your boards and everything, but you can't route signals across here either top or bottom because that V-groove, that just you know, the wheel comes along and just

**Dave Jones:** saws out all of your traces. They'd be cut. So, we have to convert this thing to having breakout tabs. And here's not quite my finished product, but it has got the breakout tabs like this. So, even though there's you know, there's

**Dave Jones:** not much room in there, I can actually route out a trace or two top and bottom side of the board out of these little tabs here. So, as you can see, there's not much room in here, but there

**Dave Jones:** certainly is enough room to route it, route out a single you know, 10-mil trace or something out of there and then down both top and bottom side. But, because this is a front panel board, you know, the look and feel of this thing is

**Dave Jones:** quite important. So, it's not like I can bring a via up here and then, you know, route out a signal top side like that. It's just going to ruin the look and, you know, finish of the front panel of

**Dave Jones:** the product. So, um on this particular design, I am limited to the four corners on the bottom. Now, I could add extra breakout tab here, for example, but once again, that doesn't cut out very nicely. I'd have to do some mouse bites in

**Dave Jones:** there, as they're called, and sort of dig into the product a bit. And you just don't get a nice smooth finish. But, on the corners like this, when I break them out with a pair of side cutters, it

**Dave Jones:** works really well. So, you know, just for functionality uh and and appearance's sake, I'm going to limit myself to just four tabs on the corners on the bottom side. So, that means I'm probably only going to be able to get

**Dave Jones:** out like a single trace on there. I don't want to push my luck. So, I'm pretty much limited to four traces coming in and out of each particular board in this case. Now, one thing you have to be careful of is that these

**Dave Jones:** routing paths here aren't exactly uh precise. So, while you can actually define them as precise, but typically the manufacturer will use whatever routing bit uh you know, it might be 2.4 mm standard routing size. In my case, I

**Dave Jones:** do know that. So, I have route So, I have specified this channel as 2.4 mm as wide. So, I I'm confident in how much space I have in there for a trace. And really, you know, it shouldn't eat it,

**Dave Jones:** but just be aware that there is uh quite some manufacturing tolerance in there. It may not be exactly as you specify, unless you really hand hold your uh bare board manufacturer to get it right. You know, if you start pushing two and three

**Dave Jones:** traces down there, you know, 5-mil or something like that traces, you can be in trouble. Just be aware of that. Last thing you want is for the routing tool to come along here and just, you know, that trace being right on the edge and

**Dave Jones:** just tear it off or drill all the way through it. And if you are going to be a rebel and put like several traces through here, generally you'd only put one trace through each mouse bite. If you did a mouse bite,

**Dave Jones:** you'd have a couple of little or you'd put multiple vias along there, little holes so that you could actually cut it out. You might put one trace between there, but if you're really desperate, you might try and squeeze in two traces

**Dave Jones:** in there. Just be careful of that because if you then get in there with your side cutters and cut it off, you can accidentally short out your tracks and that can ruin your day. So, let's have a look at my new circuit here and

**Dave Jones:** see what test functionality I can include in this thing. Now, I wouldn't mind basically being able to replace the battery here so I can power the board, all the boards, all 10 boards on that panel. Of course, mandatory I have to

**Dave Jones:** measure the output voltage here and I've got my input current over here. So, you know, really ideally I'd want six connections like this so I can inject a test current, measure the output voltage and also power the thing under test cuz

**Dave Jones:** remember that I've got a battery load detection system here so I'd want to It'd be nice to be able to test that for example. So, you know, feed in like 3 V and make sure the LED lights drop it

**Dave Jones:** down to 2.65 V under the 2.7 V limit and ensure that the LED goes out. Things like that. So, really I need six connections, but as I said, I've only got four there so I'm a bit limited into

**Dave Jones:** what I can do. Now, of course, it My first thought was of course, well, I can hook the current in series of all the boards so I can feed in one constant current source and then loop through series like this all of the 10

**Dave Jones:** boards on the particular panel. But, unfortunately, because of the common output ground here, you can't I can't just do that. This is not a floating cut current input. So, unfortunately, that plan, unless I want to my test board to be able that plugs into

**Dave Jones:** this panel to be able to switch current into each board separately. So, that's you know, that's a bit messy. So, I especially at the low currents we're talking about switching the low currents and things like that. And you know, I

**Dave Jones:** would I would do that. I would have be testing all six things like this and have a nice current switching system if I was manufacturing tens of thousands of these things and you know, I wanted to do it properly. But, really, this is

**Dave Jones:** just like a quick and dirty thing to you know, I might only be manufacturing a hundreds or a couple of thousand of these things. So, I don't want to go to town on this and gild the lily. So, what I'll do is I'll just tap

**Dave Jones:** the output voltage that's mandatory and I'll power the board. So, there you go. I've got my four connections, positive, negative, power the board. So, the one voltage will go in parallel to all 10 boards and then the output voltage, of

**Dave Jones:** course, the common's all the same, but then I need to tap out the 10 10 boards on the panel, so 10 individual output voltages here. And then, I can just run around and plug in. So, when I plugged

**Dave Jones:** my test connector into this panel, I just run around and then plug the test current into each one. Yeah, it's a manual work with a cable, but hey, you know, it's good enough. It's still going to take save a lot of time

**Dave Jones:** over this clunky thing. So, that will be the plan. I'll have a test connector on the side of the board here and I'll route out the output voltage signals through the tabs up here and all the way around the outside of my panel back to

**Dave Jones:** this one, you know, large 15 or 20 pin test connector over here. And then, that'll feed it allow me to feed in the voltage, power up all these boards without having to plug the batteries on the back. I can test the low battery

**Dave Jones:** voltage here, and I can also then just go around with the cable and go boop boop boop boop. Like it literally will be that quick. Just touch it on like that, and I'll have some red green LEDs on my board just like I did over here on

**Dave Jones:** this board here. I'll just have a whole bunch of like 10 red green LEDs, which will just uh pass fail the current into the board like this. Easy. So, I've just done a quick Dave CAD noodle here of what my test board will

**Dave Jones:** be. It'll have like a 14-way test connector here. I need 13 connections, so just make a 14 or 15-way just a 0.1 inch header, for example. Then it's got ground, reference ground, and those 10 output voltages from the 10 individual

**Dave Jones:** boards. And then they just go into a window detector here, which then lights up a, you know, a red green light based on a reference voltage for a particular known test current. You know, it might generate, you know, one for a

**Dave Jones:** nominal like 1 V output or something. So, that might be a 1 V reference voltage. Of course, it's going to be a plus minus because it's a window detector. So, there'll be the tolerance in there of, you know, 0.05%

**Dave Jones:** or something like that. I would set it to whatever tolerance I require for testing. So, this would be a, you know, a real expensive voltage reference, real expensive precision resistors on here. But because you only have to make one of

**Dave Jones:** these boards, you know, not a big deal. And then that reference voltage can also be used to generate a constant current source as well. So, I probably don't even need to use an external my Keithley constant current sources

**Dave Jones:** anymore. I can sort of build this in and calibrate this thing, and you could have trim pots on this board, and you could, you know, test it and trim it perfectly cuz I only need one board. It's not too

**Dave Jones:** hard. and then I can generate the test currencies, go off to banana jacks, and then as I said, I can just, you know, walk around, bang, bang, bang, bang, and then the LEDs light up on the 10 channels. I can have a selectable 3-V

**Dave Jones:** and 2.6-V voltage source to detect my low battery there. And that's pretty much all there is to it, although I might also want in here, for example, I might want to add in a little up a little current sense

**Dave Jones:** shunt, and, you know, then I can measure the test current as I switch on the individual board. So, I can go around, you know, switch one board on, and it'll be 1-mA current, for example. I can even have like a panel meter on the board as

**Dave Jones:** I did for that other ATE board I showed, you know, switch it on, you're going to get, you know, 1-mA current draw plus or minus something. You'll get, you know, switch the next one on in parallel or switch that one back off, and you can

**Dave Jones:** measure the total current to make sure there's no overloads on there. I don't know if I do that. It's not, you know, really a big deal cuz if you get your output voltages, pretty much there's going to be

**Dave Jones:** no overload conditions with such a simple circuit like this, but there you go, very easy test board. You just build one of those, and bingo, you can install You can either do it in house, which I may do for some, or then I might give

**Dave Jones:** this test board once I manufacture it to the subcontract assembler, then get them to test the boards as soon as they come off the the production line, and then you do some test documentation to go along with this to just explain

**Dave Jones:** step-by-step clearly to the operators how to test these boards and what to look for. But, as I said, if I was really going to town and doing this professionally for, you know, tens of thousands or hundreds of thousands of boards, I'd, you know,

**Dave Jones:** I'd automate this. I'd ensure that I could feed the test current into the test connector, and I'd have automated switching on here. I'd have a microcontroller and a test button which sort of ran through an automated sequence of tests and then just gave one

**Dave Jones:** big pass fail on there. And the other thing you want is when you got your 10 LEDs here switching on, you want to give those a number and of course you want to have an associated number printed on

**Dave Jones:** your panel so you know exactly which board failed lights up. So to begin you'd you know put a silk screen label there, you know, 1 2 3 4 5 etc. Then you take off some solder mask there so that

**Dave Jones:** you can mark it with uh you know a red marker pen or something like that that that board's failed or you know they could come along with one of the you know a red dot sticker or something like that. Not very

**Dave Jones:** visible on a red board but you know each test house has their own way of doing that. And on a fully automated jig of course, you would probably break out the connectors as well like this so that you

**Dave Jones:** could automate those cuz there's nothing worse than having to go along and manually flicking switches for various ranges and and testing like that. So if you're really serious, you'd probably route out all those so that you could automate it with relays or solid state

**Dave Jones:** switches or something like that. All right, let's actually take a quick look at my board here and just see what I'm going to do. I'm not actually going to go through the detail. I'll just show you before and after basically. I've got

**Dave Jones:** my schematic here. I know that I want four test signals, two from the battery here and two from the voltage output over here. So let's take a look at my bare board. What I need to do is route

**Dave Jones:** some traces on my bare board through to those through to the corners out here because this is just the individual board. I haven't panelized it yet but I still need to route traces on my individual board. Now this will vary how

**Dave Jones:** you exactly do this will vary totally depending on which PCB package you have and how it supports panelization of your board. This is Altium Designer that I'm using here so other packages will vary and there are multiple ways to do it

**Dave Jones:** within here, but anyway, here's my bottom layer here. Here's my battery positive and negative terminals down here. So, what I've done is I've routed this trace out here down to this bottom right-hand corner down here, and I haven't I deliberately haven't

**Dave Jones:** taken it all the way to the edge like that. If I just want to get a single board manufactured, then I can you know, then that's just going to work fine. But then I'll bring my trace in here on the panel side, and

**Dave Jones:** that'll just automatically join up as we'll see in a minute. And then I've got my other one over here routed down here to the bottom right-hand side. So, that's easy. And then my output signals were really easy cuz they they were my two terminal

**Dave Jones:** binding posts up here. So, I just routed those out to the corners, and I've just got them going out. So, they're my four test signals. And as I said, nothing on the top layer because that's going to be

**Dave Jones:** my visual you know, thing. I don't I you know, I don't want to ruin that at all in terms of uh you know, spoiling the look and feel of my front panel board. So, it'll just be on the bottom there. So, anyway, if we go

**Dave Jones:** over to our panel, let's take a look here. Now, here is my panel board, and it's flipped. Sorry about that. I'll just flip it back. And this is how I've done it. 5 by 2. I could have made a larger panel, but hey,

**Dave Jones:** 10's a nice round number. Nice little compact board. It's going to fit with any manufacturer. And basically, I've done a video on this before. So, I won't go into the details, but I've just specified my routing path here

**Dave Jones:** basically. And that's a 2.4 mm route, and then I've just stopped short there, and I just put a manual note on there to let the bare board manufacturer know that they are to route out that. And to them, it's pretty obvious what to

**Dave Jones:** actually do. I don't have to give any additional notes. They just, you know, are so used to these sort of things. It's really obvious. And uh of course, this actually panelizes this thing for me. It's a penalization routine

**Dave Jones:** inside here. So, it just duplicates my single board uh 10 times. But, if you got a package that doesn't support that, then you would have to manually cut and place. But, anyway, um so that is my bare board without any test

**Dave Jones:** functionality at all. Of course, I've got my fiducials down here and my tooling holes as well. They're important, as I've mentioned in previous videos. But, now here's one I've prepared earlier. This has my test connector on the side here. So,

**Dave Jones:** what I've done is I've just got a a 15-way or 14-way uh .1-in right-angle pin header here, which they'll uh solder on at the assembly stage. It doesn't, you know, cost a huge amount just to hand solder that that connector on. And

**Dave Jones:** I've basically got traces running out the tops and bottom corners and these balls to line up with the other traces. So, let's go to the bottom layer here. I just switch that on. And I've got the trace just coming through the little

**Dave Jones:** breakout tab there and just going in here. So, when I generate the Gerbers, it'll automatically join up with the existing trace in here. So, I've just got that a separate trace going to the output, the positive output connector of

**Dave Jones:** each board like that. And then the negative one, I've just got that going to the top layer and that's just a common trace on the top layer there. So, that Yeah, there we go. And on the top, of course, I've numbered them as well, 5

**Dave Jones:** 4 3 2 1. I've removed some solder mask there just so that you could write something there easily with a marker. And I've done that for all of these boards. And I've brought all those signals back to the test connector. The

**Dave Jones:** battery here, these two pins here, are just going parallel to uh here we go, down to the bottom corner. I've done exactly the same thing down here as I did before. I just have the trace going through there and the

**Dave Jones:** positive or negative, I think it is, trace going through the other side. And that's it. That's how I've added some production functionality to my otherwise wasted panel cuz usually a panel all it's there for is just a physical

**Dave Jones:** mounting frame which is some you know, tooling holes just to hold the board in place inside the pick and place machine and the fiducials visual alignment fiducials to line up the pick and place head and that's all it is, but we have

**Dave Jones:** actually added some stuff and if I wanted to, I could add active circuitry onto this panel no problems at all. And now I haven't gone to the effort to produce a separate schematic for this panel, but if you are really doing it

**Dave Jones:** seriously and you want to design real check. So I can't design real check this panel board because it's so simple. I don't really have to. The risk of me goofing something up is quite low although Murphy's law, you know how it goes, but

**Dave Jones:** anyway, if you want to design real check that, you'd typically have a schematic associated that and there's various ways to do that. So you would have individual board schematics and then a panel level schematic as well if you're really going

**Dave Jones:** to town on this thing, but that's all there is to it. So my test board will just mate with a female header over on this side and bang, it plugs in the side and now I can power all those boards at once and also access

**Dave Jones:** the output test signals. And here are the generated Gerber files which I've done earlier. I could have done it just live, but let's zoom in on this sucker and see what we get here. Now as you can see, when I zoom it up, when I zoom in,

**Dave Jones:** something's going on there. Oh, something buggy there. Now try like you can't see the routing paths here, but as you can see it's now these traces are now joined up on my board. So the panel ones have just

**Dave Jones:** automatically, because I've overlaid them one on top of the other, automatically just joined up at the Gerber layer like that. So, now my Gerber is just fine and dandy. I think that artifact might be my screen capture program doing something. I don't know.

**Dave Jones:** Um but, yeah, all those traces now joined in there, and I've got a full production test uh production-ready panel. Fantastic. So, there you go. That's just uh several simple options for production testing a panelized product like this. Very simple

**Dave Jones:** to implement. Just, you know, something basic like this that can really pay dividends come test time. So, I hope you enjoyed that. And as I said before, all of the previous videos which are related to this will be linked in

**Dave Jones:** down below. So, be sure to check those out if you haven't done that already. And if you want to discuss this, best place to do it is over on the EE blog forum, because the new YouTube comment system sucks ass. Catch you next time.
