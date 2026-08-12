---
video_id: eRtO3EZK_Cc
title: EEVblog #301 - LTspice Temperature Sweep Tutorial
url: https://www.youtube.com/watch?v=eRtO3EZK_Cc
source: youtube-asr
timestamps: {"0": 1, "1": 22, "2": 39, "3": 55, "4": 73, "5": 89, "6": 107, "7": 121, "8": 136, "9": 153, "10": 171, "11": 185, "12": 206, "13": 221, "14": 234, "15": 257, "16": 275, "17": 291, "18": 305, "19": 316, "20": 333, "21": 349, "22": 361, "23": 375, "24": 389, "25": 406, "26": 420, "27": 436, "28": 454, "29": 472, "30": 484, "31": 501, "32": 514, "33": 533, "34": 552, "35": 574, "36": 588, "37": 605, "38": 623, "39": 639, "40": 651, "41": 668, "42": 683, "43": 697, "44": 710, "45": 725, "46": 740, "47": 758, "48": 774, "49": 790, "50": 804, "51": 824, "52": 839, "53": 860, "54": 875, "55": 889, "56": 902, "57": 919, "58": 939, "59": 959, "60": 978, "61": 993, "62": 1014, "63": 1031, "64": 1043, "65": 1060, "66": 1074}
---

**Dave Jones:** Hi, I thought I'd just run you through a quick little tutorial here in LTspice showing you a very valuable technique called temperature sweeps. And that's analyzing your circuit not just in the regular domains but over temperature variations. And it's not really obvious

**Dave Jones:** how to do this in LTspice unless you're familiar with the spice commands and things like that. It's much easier in other circuit simulation tools. They might have a menu option or some other option to do temperature sweeping. It's really obvious but

**Dave Jones:** it's not so obvious in LTspice. So but it's really very easy and it's built in there. You just don't know it. So let's run through it. And temperature sweeping your circuit simulation can be a very valuable technique to see how your

**Dave Jones:** circuit is going to perform over a real world temperature variation or a semi circuit simulator temperature variation. It's going to be fairly close in most cases and it's a step which a lot of people simply forget to do. They will

**Dave Jones:** simulate their circuit and it works just fine but then when they build it up they find that oh it's not working as they intended because the temperature variation has changed and every component has regardless of what the component is has some sort of

**Dave Jones:** temperature coefficient. So it's parameters, its value will change with temperature and there's a way to simulate this. Now using LTspice of course it's my favorite circuit simulator tool. It's free and it's not the easiest to use though. I've

**Dave Jones:** done a few little tutorials here and there on it. So we'll learn how to do temperature variation in this one. And as far as I know there's nothing in the tool, you know, the menus or anything like that, the simulation

**Dave Jones:** commands and stuff like that to do a temperature variation. So, how do you do it? Good question. Well, the circuit we're going to use here is a very simple two-transistor constant current circuit and you may have seen this before or you

**Dave Jones:** may have seen a variation with Q2 transistor here replaced with two series diodes. It really doesn't make much difference. You can use either. And what it does is it basically sets up a constant current through R1 here, through this transistor Q1,

**Dave Jones:** based on the base-emitter voltage of the transistor and the and the source here, in this case Q2 or two series diodes. You may have also seen one with an LED in here as well. That can be used as well cuz all you need is

**Dave Jones:** anything that generates a constant voltage greater than the base-emitter drop of Q1. So, anything here like an LED which might have, say, a 1.8 V drop for a red LED, will set up a constant current through here. But, as you should

**Dave Jones:** know, the base-emitter voltage will change with temperature. And we're going to find out how much by doing a temperature parameter sweep in LTSpice. So, let's go. First thing we'll do here is we'll run a regular simu- transient simulation here and

**Dave Jones:** let's set it up so that our stop time is 1 second and we've got starts at zero seconds and we'll have a time step of 1 millisecond. So, we'll get 1,000 points there and it puts our SPICE command down

**Dave Jones:** here and we'll add a SPICE command later to do the temperature sweep in. So, this is probably if you've used LTSpice or any other circuit simulator with transient response, this is what we'll do. So, we'll go up here and we'll run

**Dave Jones:** it. And it's running and then we can see our constant current through R1 here and there it is. It's 6.1 milliamps, which is not surprising at roundabout 0.6 volts um base emitter drop uh basically and where uh divided by 100 ohms is 6.1 milliamps and

**Dave Jones:** that isn't really going to change uh much at all with this voltage is with the supply voltage up here because it's a constant current generator. That's what it's designed to do, generate a constant current through R1 regardless of

**Dave Jones:** the voltage here. So, we can go in there and we can modify that and we can call that say 20 volts, okay? And we can run that again and bingo, there it is. It's still that 6.1 milliamps. It hasn't varied at all. Now,

**Dave Jones:** I might as well show you uh before I show you the temperature parameter sweep, let's go for a basic parameter sweep. You notice how I manually changed that uh V2 voltage there from uh 10 volts to 20 volts and we ran the

**Dave Jones:** simulation again. Well, what if you wanted to do sweep that value across? So, the way we do this is we go into V2 here and instead of putting that value in there like we did before, we put in a

**Dave Jones:** curly bracket and that indicates to uh the spice engine to LTSpice that this is going to be a parameter which we're going to modify when it's running the circuit simulation and we can give this a label and we can call this say V in

**Dave Jones:** like this and we close it with a curly bracket like that and now we can actually use a spice directive, a spice command and we go up here, this little tab up here called spice directive. We go in and we can use a command which is

**Dave Jones:** called a dot step command. And then we want to tell it and use another command that we want to step the parameter. So, we use param like this and then we give it the label we just gave it, which is V

**Dave Jones:** in. And then we use another command called list. I know it sounds complicated, but you know, it's once you learn this once, it's pretty easy to do. And then that just tells us that tells the engine that we're going to list some

**Dave Jones:** values here that we want to sweep through. So, we want 1 2 3 4 5 6 7 8 9 10. And you can put in as many as you want. So, it'll sweep through. So, that command is to step through the parameter

**Dave Jones:** V in with a list of values 1 2 3 4 5 6 7 8 9 10. Simple. And then that puts that command onto your schematic there and you can now run this simulation and it should, in theory, if we measure the

**Dave Jones:** voltage here, bingo. Look, it's now stepped it. I know these scales are slightly off, but that is cuz that's that auto scale uh function, but that is 1 2 3 4 5 6 7 8 9 10 V there. So, circuit simulation has

**Dave Jones:** gone through and done this transient response um with 1,000 steps. It's done it 10 different times for all of those values. And we can now look at the variation in this uh look at the variation in the constant

**Dave Jones:** current here for this V2 varying from 1 V through to 10. And you see that it's pretty darn close. Look, it's 6.10 you know, third decimal place there. It changes a little bit. So, that's a really pretty good constant current

**Dave Jones:** circuit at one temperature because it's only simulating this at one nominal temperature, which is nominally room temperature. So, that's called parameter sweeping, and you can not only do that for voltage, you can do it for any parameter in any circuit component. So,

**Dave Jones:** this resistor here, you could sweep use that exact same command to sweep through, say, this this resistor. You could change the value from 1K up to 100K or something like that. And you could uh these transistors here, you

**Dave Jones:** could go in and you can change any one of the parameters in there using that parameter command. But, we want to do a temperature sweep. So, we do exactly the same thing. We put in our SPICE directive, and we go .step, and then we

**Dave Jones:** want to put in instead of param, we don't want to change the parameter, we want to use we want to sweep the global temperature in the circuit. So, you use the command temp, and then we want to list them again, and let's say we want

**Dave Jones:** to list go from 0 5 10 15 20 25 30 35 40 45 and 50. We want to sweep from 0 through to 50° C. We just put that in there like this. That's our SPICE command, our SPICE

**Dave Jones:** directive, and we go ahead and run that. And wow, look. We've got a spread of parameters here. Let's go in and check it out. We've got our current through here. Uh-huh, look at this. Over temperature, you'll see that the temperature ch- as the

**Dave Jones:** temperature changes by each 5°, it jumps from 5.67 mA, 5.76, and it spreads by the almost like 1 mA there. So, you know, that's a fair error to go from 5.6 mA to 6.6 mA over a 50° temperature range, and you wouldn't have

**Dave Jones:** known this unless you did a temperature parameter sweep. Now, there's actually an easier way than just doing this list. If you want to say you want to do 1° steps from 0 to 50, you don't actually have to type in 1

**Dave Jones:** 2 3 4 5 right up to 50. You can actually go in there and you can modify this and instead of putting list, you can just leave out the list command and you can put 0 50 and then the step value. So, it will

**Dave Jones:** you're telling the engine now to go to step from 0 to 50 with an increment of one. So, there's only three parameters there. So, we do that and we execute our There it is. Bang, it's running through 50 different transient simulations there

**Dave Jones:** of our It's exactly the same before except we've got greater resolution. And you can see those values change. Magic. Now, at this point, I know what you're thinking. Can we actually combine more than one parameter sweep at the

**Dave Jones:** same time? Can we sweep V2 over here at the same time as we sweep the temperature? Well, you bet we can. Well, we can't do it at the same time, but it will but we can make it step through as

**Dave Jones:** many parameters as we like. So, in this case, I'm going to combine the two exact things we've done before, our spice directive here, which is our set temp from 0 to 50 in 5° steps and also we're going to step our parameter V in from 1

**Dave Jones:** to 10 in 1-V steps. So, what it's going to do is it's going to run through this transient response not just 10 times here, but it's going to do it 10 times for each one of these 10 times here. So,

**Dave Jones:** let's give that a go. Let's run that. Oh, by the way, I've changed changed my transient time to be a 10-ms uh just so the simulation uh is a bit shorter, but it's going to be no difference. So, let's run that and

**Dave Jones:** bingo, what do we get? You see it ran through it ran through like 100 times to give us all these responses. Now, you're probably we're looking at the current through R1 here. We can look at the VN value up here. You can see it step from

**Dave Jones:** 1 V through the 10 V, but let's look at how our constant current load here changes over temperature. Now, that looks just like before, but let's zoom in here and you'll notice, if you can just see that, that with each one of

**Dave Jones:** these lines, there is a slight variation with all the other lines. So, let's see if we can actually zoom into this bit here and see if we can see the variation. Look at that. So, there you go. For each one of those temperature

**Dave Jones:** steps, we have an input voltage step like this and you can see the minute change. We're only talking, you know, 6.508 mA up to 6.51 mA. Not much change at all, you know, you're only talking 10 microamps, 20

**Dave Jones:** microamps change based on that voltage at that particular temperature. So, that's how it works. So, you can see the minor variations in each one of those and you can do that for sweeping as many parameters as you like. So, as you saw,

**Dave Jones:** that can be a very powerful tool. We're just getting simple flat uh curves there. When you do a more complex circuit, maybe you're sweeping like a band pass filter or something magical like that and you're sweeping responses, you can combine them all with all the

**Dave Jones:** different types of um analysis functions you've got in a spice tool, can be very, very powerful and I won't go through it. I encourage you to go and experiment on your own. Now, um let's do a simple let's uh change this circuit just out of

**Dave Jones:** curiosity. Let's uh do an LED. Add an LED in here and see what happens. See if that's any better than our two transistor circuit. So, we pick a new diode Nichia. There we go. We've got a Nichia. I have no idea what an NSCW100

**Dave Jones:** Nichia LED is, but there's all of the spice values in there, 30 milliamps. I thought, yeah, okay, let's just pick that as a typical diode. You'd have to have a look at the data sheet, but let's do that.

**Dave Jones:** Uh run that simulation again and see what we get here. Wow, let's have a look in here. Wow, look at that. That's quite That's a quite a substantial variation. You're talking 12.5 milliamps there. From 12.5 milliamps to 14.5

**Dave Jones:** milliamps. Now, let's go back to our dual transistor configuration for a second and instead of having our fixed 3.3 volts here like we did before powering this, I'm actually going to take this from the input from the input supply

**Dave Jones:** voltage V2 here. And I've just run the simulation again, exactly the same parameters as before, but look at the quite the spread in variation. You notice how we had like before we had like just you know, a single line with

**Dave Jones:** the temperature variations very clumped together. You know, they've got a much wider spread like that because the VIN is changing, it's changing this current through R2 here. We can actually get a spread of that and you can actually see

**Dave Jones:** that that current changing through R2 as V2 gets stepped here. So, V2 gets stepped. I've set it from 3 volts through to 10 volts. So, it gets stepped 3 4 5 6 7 8 9 10 volts. You can see and

**Dave Jones:** in between those you have the individual temperature variations. So, going back and looking at our two transistor constant current source here, it's quite crude, uses jelly bean 2N3904s. How good is it? Well, using a constant V1 here, if you we can see the result

**Dave Jones:** over a 50° C range, it's about a 15% change over a 50° C rise. So, that's a a roundabout 0.3% per degrees C. Is that any good? Well, if we take a look at the classic LM334 constant current source

**Dave Jones:** chip, then it has essentially the same temperature coefficient. It's got around approximately 0.33% per degree C temperature dependence. So, there you go. It's as good as an LM334 basically. I rather like it. It's neat. Let's just try one other totally

**Dave Jones:** different example. Here, I've got a Colpitts oscillator which comes with the as an example, comes with the LTSpice circuit. I've added my It doesn't normally do the temperature variation, but I've added my spice directive here, step temp from 0 to 50,

**Dave Jones:** 5° steps. Let's run it. Look at that. Beautiful. Look at all the temperature variations in there. Fantastic. And you can almost get works of art with these things. I It's almost, you know, it's almost art what you can actually

**Dave Jones:** make with the results from these parametric sweeps and temperature sweeps. Good stuff. So, I hope you enjoyed that. I hope you found it interesting in how easy it is to do temperature parameter sweeps or any parameter sweeps in LTSpice because it's

**Dave Jones:** a shame that it's not immediately obvious how to do it. They don't have like a menu option in here in simulate. It would have been nice if, you know, somehow they hadn't, you know, an option in here to sweep and to do like a

**Dave Jones:** temperature and automatically added that command. I know it's not much, but it just would have been easier for beginners to find that. Otherwise, it's just buried away as a regular spice command. And if you don't know your spice commands to do temperature

**Dave Jones:** sweeping, then well, you'll be sitting here looking through all the menus scratching your head. So, I encourage you to have a play around with temperature sweeping next time you simulate your circuit. It's a very powerful and essential tool. I hope you

**Dave Jones:** liked it. And if you liked the video, please give it a big thumbs up. Catch you next time.
