---
video_id: -ON1AdmAMOY
title: Vintage Tek Museum: Curve Bug Signal Debugger
url: https://www.youtube.com/watch?v=-ON1AdmAMOY
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 26, "3": 38, "4": 51, "5": 66, "6": 82, "7": 93, "8": 113, "9": 126, "10": 140, "11": 153, "12": 169, "13": 182, "14": 196, "15": 211, "16": 227, "17": 243, "18": 256, "19": 270, "20": 284, "21": 297, "22": 312, "23": 325, "24": 338, "25": 352, "26": 367, "27": 379, "28": 392, "29": 407, "30": 420, "31": 433, "32": 447, "33": 461, "34": 478, "35": 487, "36": 502, "37": 518, "38": 535, "39": 551, "40": 564, "41": 574, "42": 584, "43": 595, "44": 610, "45": 621}
---

**Dave Jones:** It's Oh, vintage tech museum. OH, IT'S THE CURVE BUG. OH, IT'S A curve tracer. It's a curve tracer. WE CAN GET OUT OUR OLD school Tektronix analog oscilloscope. Oh, touch nodes in the circuit and get a heuristic feel for the

**Dave Jones:** characteristics of that node. Oh, yes, it comes from the Huntron. The Huntron tracker was big when I was a kid. Um, that was all the that was all the rage with all the repairs um with the repair techs out there. The curve

**Dave Jones:** bugger allows the simultaneous display of two comparable curves so you can AB compare a good unit with a bad. So, if you've got a good if you've got a faulty unit, you've you're repairing faulty PCB you're repairing. If you've got a known

**Dave Jones:** good one, you can compare the waveforms on both of them. So, you get two probes and you go probe this point and you go how different are the two waveforms? And then you can um know Oh, okay, so you

**Dave Jones:** can localize the fault to that specific part of the circuit. The museum is only asking for 40 bucks for the curve bug. Bargain. Modestly priced. Yes, it is. Um, there you go. It's from the vintage tech museum. Fantastic. Uh, personally um

**Dave Jones:** Bob. Yeah, Bob Pucket. There you go. Bob Pucket. Good on you, Bob. Uncle Bob. Personally, I'm a retired R&D engineer who has a blast restoring old Tektronix gear for the museum. It's fun to go to schools with our exhibits and play Mr.

**Dave Jones:** Wizard a bit. Awesome. >> It's very compact for what it does. I'd expect something a bit bigger for analyzing. >> Yeah, I mean it's it's tiny. Well, no, it doesn't analyze it doesn't do any smarts. You've got to

**Dave Jones:** Yeah. So, this is actually what I thought it was initially. It's a curve tracer, but it's basically a two-channel curve tracer with uh selectable source resistances so that you can test and compare in-circuit uh components unpowered, of course. Um, so that's why

**Dave Jones:** it's got two channels. It's got the one comp port and the two channels here. So, this uh curve tracer is also known as like a component tester in old school analog oscilloscope. Sorry, none of my analog oscilloscopes actually have the

**Dave Jones:** component tester function in there, but a lot of old school ones did. They'd have um banana jacks on the front that would allow you to connect hook up components and test resistors, capacitors, diodes, everything else. And you'd get different patterns on the

**Dave Jones:** screen, which we're going to see uh shortly once I hook it up to the uh PC. And that's how these old school component testers work, but they were only single channel just to test components. This one has two channels

**Dave Jones:** effectively doing uh the same thing. Here's um diagram of what it's essentially doing. It's just a signal generator with a DC bias I'll mention in a minute that outputs through two different resistor values, and you can change that in the software, so you can

**Dave Jones:** drive different currents into your unpowered board. It must be unpowered or unpowered boards, your eye board, your golden board as it's called in the industry. Um if you've ever been in the repair trade or something like that, you

**Dave Jones:** might have what's called a golden board, which is a known working perfect board that will you you will compare signals against when you're actually repairing and troubleshooting a the same product. And this is what this allows this thing

**Dave Jones:** to do. So, anyway, I'm going to probe it with the old school analog scope. Note where the ground is here. So, let's get that right on that graticule there. They should be identical. And you'll see that it goes up about .6 volts or thereabouts

**Dave Jones:** and down to minus one to almost minus three volts there. Um and we're one volt per division there. And both channels will be identical in this regard. And then they've just got an ADC in there. It's an ARM Cortex um M0 or whatever. And we

**Dave Jones:** get two different currents out of here. One is a microamps through a 4.5 K source resistor and another is 30 microamps through a 100 K source resistor. So, using this triangle wave generator through a source resistor, we're able to

**Dave Jones:** actually measure the component under test. So, let's install the software and give it a whirl. We'll download and install this. It's only available for Windows by the looks of it, but well, that's okay for me. It may not be

**Dave Jones:** for you, but anyway, so let's install that. No worries. Got an old school installer. Not a problem. We've just got the flat lines like this and apparently I think you press the space bar go yeah, into weak. You see the word weak there. Yes.

**Dave Jones:** So, it's got weak mode up here. As I said, that goes through a 100 K source resistor and you'll just get a different well, operating current through your device under test that you're actually doing. So, sometimes depends on the

**Dave Jones:** which circuit node you're actually connected to whether or not you need to use weak mode or I guess full mode or whatever with the 4.7 K or whatever source resistor. So, we can show we can show both and we can and when we move

**Dave Jones:** the cursor around there, we get the individual value, but I'm going to use my fingers. Here you go. Wee! A circle is a capacitor. So, I'm primarily capacitive, but I'm going to have some there's going to be some parallel

**Dave Jones:** resistance in there as well. If I do the other channel, there we go. If I hold calm and do Hang on, I've got to use the same fingers. Look. All right, so we're comparing the two circuits like that.

**Dave Jones:** All right, so if I release the pressure on one finger, you can see it varies like that. So, you can see how it's actually doing a comparison test between you know, this finger which is it's going to be

**Dave Jones:** just going to have a different parallel resistance on there. A higher parallel resistance, less pressure I put on there, but when I do two, both very similar. There you go. Can I wet my fingers? Wow, LOOK AT THAT.

**Dave Jones:** BOBBY does that. Anyway, the point of you saw that um it had a lower negative voltage uh minus three or thereabouts volts as opposed to part plus point six volts. The reason for that and the reason and the uh way

**Dave Jones:** that this thing works is when you're probing a powered off circuit node, most modern circuits, they're all you know chippies, right? The chippies connected to every node. So, the inputs and outputs on a modern, you know, CMOS or

**Dave Jones:** whatever um technology uh you know, component is, whether or not it's a processor and op-amp analog thing, whatever it is. The pins on that chip that are in that circuit node, there might be other passive components around, but the pins on that chip

**Dave Jones:** usually will have input like a diode protection, for example, they'll have reverse bias diode protections. And that's what this negative voltage can do. It can actually switch on those nodes in the circuit. So, it's able to use like essentially test the chip as

**Dave Jones:** well. It doesn't test the functionality of the chip, but it can test that, you know, the input is not, you know, shorted out or something like that. Um by turning on all those diodes. Oh, look at that. That's That's so much fun. I

**Dave Jones:** love it. So, if I get my reference capacity here, so we've got a perfect perfect capacitor. Oh, come on. They're not the correct pin sp- Oh, they're not the standard pin spacing. I'm going to have to budge it a bit. So,

**Dave Jones:** it's supposed to be a perfect circle, but she ain't. I'm not sure why. Should be. And then the other one will be that as well. And if I hook up a resistor, it's going to be a straight line. Ta-da! Just happens

**Dave Jones:** to be 120 ohms, 1 K ohm, for example, as we go up in value. And if I go up to, you know, 100 K, for example, there we go. And one one meg, it's going to get progressively completely flat. That's

**Dave Jones:** like 13 meg. And in higher power mode, 1K 2K like that. So, that's pretty cool. So, let's probe a point in a circuit happens to be for a old school watcher, you might remember. Yes, this was the drop

**Dave Jones:** tested at at the dam at the famous dam. So, I'm just going to Sorry, I can't show you this at the same time, but I'll just I have no idea where I'm probing. Go Okay, I'm going to probe across a

**Dave Jones:** diode A and that's what we get in circuit. There we go. I was wondering why we weren't getting the characteristic response. That's better. We're starting to see our diode characteristic curve there. And if I change the polarity No, it's the same because they're just

**Dave Jones:** back-to-back diodes. There's another in circuit diode. There you go. That's a better diode response. And we'd expect that to change in the other polarity and we could do you can see the knee. So, we're going to see that knee there and when

**Dave Jones:** you change that polarity, you get the diode junction like that. Cool, huh? Oh, I just figured that out. It cycles between weak single trace mode, normal dual weak and then normal single trace mode. Okay, that is not a

**Dave Jones:** bug. Finally figured it out. Dumb ass Dave. It's good to have both on there. Um so, what you can This is like really quick. It works perfect, does exactly what you want. It's no fluff, doesn't do anything else. It just does what it says on the

**Dave Jones:** box. And I think that is great. You could use something like this this circuit tracer for characterizing that golden board as I told you about. You know, it's a known good board. It's the perfect board. We're going to compare

**Dave Jones:** all other boards against and then you can go through and trace important points in the circuit and you can get screen captures of them and you can post these in the service manual or whatever. So, you can have in your service manual.

**Dave Jones:** Okay, probe this point which is a little curve bug here and uh make sure that you get it matches this waveform, you know, roughly. Um and if it does, it's good to go. Go on to the next one, and then go

**Dave Jones:** around and uh probe your circuit, and you can have you can document all this sort of stuff. And for a lot of cases, this is very important to actually do this. I know a lot of people say, "Oh, I

**Dave Jones:** don't provide service information anymore." Well, when you're designing like industrial products and things like that, it's still a huge thing. Unfortunately, not that uh common on consumer stuff these days, but there you go. That is the curve bug. That is very cool. I like

**Dave Jones:** that. And what is it? I think it's 40 bucks on the website. Bargain. That's absolutely fantastic. I'll link it in down below. Thanks, guys, for sending that in. The Vintage Tech Museum. Have to visit one day. Next time I'm in the

**Dave Jones:** US, definitely. Catch you next time.
