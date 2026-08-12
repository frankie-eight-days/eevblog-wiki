---
video_id: Q2rvAoO-MIA
title: EEVblog #1035 - Flaming DIY Power Supply!
url: https://www.youtube.com/watch?v=Q2rvAoO-MIA
source: youtube-asr
---

**Dave Jones:** All right, time to bring out the big guns, the Xantrex. I don't know Have I done a teardown of this one? I'm not sure. Anyway, the Xantrex XFR 300-4-300 V, 4 A. That's 1,200 W for those playing along at home. I set

**Dave Jones:** it to 55 V because, well, 55 sounds like a good number and we've got some quiescent current and it's working. There you go. We have the magic smoke. The magic smoke has escaped. Holy crap. Quick, smoke alarm. Cover it up. Cover it up.

**Dave Jones:** Glove. Glove. Glove. Well, that ended very badly. Um the magic smoke escaped. I don't know what the hell went wrong. I was just feeding 55 V into it and uh it Woo. Still smoking. It is still smoke I don't know if you

**Dave Jones:** can see it. There's still smoke coming out. Damn. Yep, she's still wafting out. There you go, you can see it. Ah. Love the smell of a burnt power supply in the morning. It's still smoking. It's still coming out of the vent.

**Dave Jones:** This is hilarious. I was just sitting here, didn't even have a load actually hooked up on the thing and what what what what And I've actually got this uh sitting right down near the inlet of my um carbon air purifier system here and I

**Dave Jones:** still having a hard time getting the smell out of the lab. Uh I do I've been gone for I just went away for half an hour, came back and still not great. Hi. Well, I was going to do video. In

**Dave Jones:** fact, I shot a lot of intro material for this RD Tech What is it? DPS 5020 power supply module that you've seen in previous videos, which I'll link in at the end of this video and also down below. And

**Dave Jones:** the designer of these modules, Glenn from RD Tech, who sells these on AliExpress, he's the designer and manufacturer of these. And he saw my video, liked it, and kindly sent me this very nice case for it, which I

**Dave Jones:** mentioned in the previous video. It's 20 $24 for the case including all of the fan and the switch and the binding posts and everything else and the wires and the whole kit and caboodle, this board up here, which is a fan controller

**Dave Jones:** board and everything else. And kindly sent this DPS 5020 power supply, which is a 50-V output 20-A 1000-W module in this tiny little thing. But you seen in previous video that these are very efficient, like over 95% efficient. But still, even at 1 kW

**Dave Jones:** claimed output power, then well, that's like 50 W in that tiny little heatsink and everything else. So, I was going to do a video. I built this. I got time-lapse footage of building everything else. Going to do a little

**Dave Jones:** review of this thing. And I built it up and hooked it up to my Xantrex power supply here and the magic smoke escaped as you saw all the drama at the start. So, let's obviously Yeah, it's not going to work

**Dave Jones:** anymore. And that's probably it for the review unless I can repair it. So let's take a look at what went wrong. What I think happened, I didn't have the camera running at the time unfortunately when it went bang,

**Dave Jones:** but I didn't have a load on the thing. I was feeding it with 55 volts on the input. It has an input voltage range up to 60 volts, so I wasn't even at the maximum and I just pressed the voltage

**Dave Jones:** button here and I started adjusting the voltage up and I just went all the way with the DJ right up and then all of a sudden it just went poof and it went and things started catching on fire. Smoke

**Dave Jones:** billowed out of the thing. There was literally something on fire in here. So let's take a look at what went wrong. Now just in case somebody asked, some people might think well I don't have any rubber feet on this thing. Metal on top

**Dave Jones:** of metal here, maybe there's some sort of earthing issue and that's what shorted out. No, it's not that because the output of the Xantrex power supply is floating. Didn't have a it's not mains referenced at all. So it's

**Dave Jones:** definitely not something to do with that. It's something into it must be something internal in the power supply because I like these Xantrexes are bulletproof. These are the ducks guts in the industry and I don't and it still

**Dave Jones:** works. I don't think there's anything wrong there at all. It's still still hunky-dory cuz you can't kill these things. So yeah and I briefly saw this voltage when I turned this up, briefly saw and I went bang and I looked down here and

**Dave Jones:** this had actually dropped down to zero. So I think it had hit its 4 amp I can't remember what I had the current limit set to it the time, but it goes up to 4 amps. Obviously just dumped all the

**Dave Jones:** power cuz this has a 1200 watt capability. So this is a really high power supply. It can deliver a lot of oopsie into there if something goes wrong. All right, so let's have a look here and see if we can uh see what's gone wrong.

**Dave Jones:** First thing you do, of course, we well, use all your senses. We smelt it, we saw it, it was uh smoking, and uh now we're going to check visually, like, you know, none of the caps have exploded, like,

**Dave Jones:** there's nothing around like the MOSFETs. Nothing seems to be blowing except ta-da! Look at that. Under the board obviously, um there's flames. That is clearly flame type uh you know, to produce so much uh smoke. It might like and it kept

**Dave Jones:** on producing the smoke. It wasn't just puff of smoke then gone. Like, a component caught on fire under this thing. So, let's take that off and uh see what's on the bottom. Let's just get all the connections off there. We'll

**Dave Jones:** flip it out and Oh! Goneski. Wow, look at that. What was there? Are there any components on the bottom? Um I'm going to have to check the previous video where I think I briefly showed the bottom of this thing. Uh my first guess

**Dave Jones:** would be They're They're the two pads. That's the negative pad. That's the positive pad. I had no load connected to this thing at all. It just went poof when it went up near uh towards full scale, 50 volts. So, maybe there was a

**Dave Jones:** cap under there that uh was Would there be like a ceramic cap that caught fire? We've seen that in uh the NES uh video that we uh saw a long time ago, which I might have to link in. Oh, there's the

**Dave Jones:** There's a trace under there. Um yeah, let me have a look at the old footage. Um see if I can get a uh picture of what was actually there. Must have been something. Otherwise, like, what's causing the short? And sure enough, yep,

**Dave Jones:** here's a uh screen capture from the previous video. Luckily, I did uh actually capture the components on the in that video and sure enough, there are two capacitors under there. Looks like only one was fitted though. What is it?

**Dave Jones:** C34 there. It's a quite large ceramic cap and that has clearly caught on fire here. Um, and it's just like it's completely gone. Like it is vaporized, but it actually caught on fire just like that nest one that we saw before. And the

**Dave Jones:** problem with these are ceramic problem with ceramic caps is when they fail, they fail usually fail short. So, if you want the utmost in reliability from a design, you might put say two of them in series. Yes, you have

**Dave Jones:** the capacitance, but then if one of them breaks down for whatever reason, it's a manufacturing problem, it's an over voltage stresses issue, whatever, then it's covered by the other one in series with it. So, it's not a problem. One of

**Dave Jones:** them's short, one of them's just an open cap. So, you just lose half your capacitance. It's not a problem, but given that we only had the one capacitor across here, either it was a wrong rated part, I it wasn't rated

**Dave Jones:** for 50 volts. You know, it was like a 25 volt cap and it went poof because this thing it only failed when I turned that I don't know exactly what voltage it got to, but I think it was getting pretty

**Dave Jones:** close. It was going up to like 30, 40 volts or something and maybe like when it topped out, something's gone wrong. So, either they've got the wrong stress component in there or it's just a faulty cap. It happens, you know, they got it

**Dave Jones:** from the One Hung Lo company at their stand at the Shenzhen market that morning and there's going to be like a manufacturing bell curve of these things. You're just going to get a certain number of defects which as I said fail short and that's

**Dave Jones:** what's happened here. It just caught on fire and because I think the default I haven't hadn't I just powered it on factory fresh module. Probably by default is set to like what what was it? The 20 amp current limit or whatever,

**Dave Jones:** and it just delivered all that power to the output cuz this thing's capable of delivering a kilowatt. Remember that. So, if you got something shorted on the output, 20 amps flowing through that cap, it's going to catch on fire, and

**Dave Jones:** that's what's happened here. So, the only question there is why it failed. Um so, I can I can clean this up, have an attempt to clean it up, and uh power this puppy back on. Uh are there any uh

**Dave Jones:** like are there any protection fuses anywhere around, you know? I don't know. Nothing else looks uh smoked. So, everything looks pretty intact. Um so, I think that's all it did, and it did the power supply did its job. It delivered

**Dave Jones:** that maximum like 1 kW uh output, that 1,000 W output into that load. It was just dumping as much power as the capacitor was saying, "Give me give me give me more power. I want to catch on fire." And uh the power supply said,

**Dave Jones:** "Yeah, no worries. Here you go. Have all the power you want." What what what what magic smoke escaped. Well, there you go. There's the aftermath of that. Wow. That poor cap that used to live in there is uh now

**Dave Jones:** dead. It looks like um the cap was soldered directly across the two pins, and that's got big thermal sinks with the pins for this thing and all the copper around there. So, they would have had to dump a lot of heat

**Dave Jones:** into that cap, poor old cap, to actually get that on the output. So, that's a bad design decision because you want those caps to be, you know, reflowed. Well, in this case, it's the only component on the bottom, is it? So, probably hand

**Dave Jones:** soldered, but you don't want to put it directly on those large mass components like that. It's almost as if it's an afterthought, like they just didn't uh design it and oops, you know, we need this extra bigger cap on there. That's

**Dave Jones:** probably why the other one wasn't fitted. Would be my guess, but yeah. So, it could have done some damage to the cap, which then caused premature failure, even if it was aspect correctly. Wow, that really is quite amazing. You can see the charring of the

**Dave Jones:** fiberglass in there. Ah. Wow, I was just trying to solder that and look what happened to the pin. The pin just like sheared off in half. It was weakened by the heat of the fire. Wow. So, what value

**Dave Jones:** capacitor was actually here? Well, Glenn will have to tell us that. I'm sure he'll respond and tell us what the issue is here. But if, say for example, you go to Digi-Key and you search for ceramic capacitors, multi-layer ceramic

**Dave Jones:** capacitors above 50 V cuz you don't want to use a 50 V. This is 0 to 50 V output. So, you wouldn't choose a 50 V rated part for this particular case. So, it'd have to be 63 V, 80 V,

**Dave Jones:** 100 V, or, you know, one of those preferred values, voltage values over 50 V. If you have a look at Digi-Key, it's basically got to be something under 10 microfarads, probably 1 microfarad or something like that cuz you

**Dave Jones:** the higher you get in capacitance in multi-layer ceramic capacitors at that particular high voltage, which is quite an unusually high voltage for a ceramic capacitor, they're either like specially manufactured, they're a special physical size, or they're like in like a a little

**Dave Jones:** lead frame stacked array, which is rather interesting. I'll show you that here. So, it's probably like in the case size we saw like you know a 1206 type size package or you know something a bit larger than that then well you know it's

**Dave Jones:** probably a microfarad. All right so I've cleaned it up I haven't added a cap on the bottom cuz I don't have any readily available high voltage caps. I could put two in series but whatever we it burned through a sense line coming

**Dave Jones:** back you can see that the two sense lines there coming back so sense in the voltage directly on the output. I've just added a 200 volt 22 mic cap much larger value than what was there before but doesn't matter that will just get us

**Dave Jones:** up and running it probably work fine without a cap but we'll just add something there. So let's power it on this time external supply just to limit the potential damage that can happen here. So let's give it a whirl.

**Dave Jones:** All right so I got a 40 volt input half amp current limit so let's switch that on and it's booting. It's booting it still works. Look at that. It's alive. Beautiful let's actually see if it outputs a voltage. Oh sorry the output has to be

**Dave Jones:** on but no look at that it reset. No. No that's one sick puppy. It's set to 10 volts at 20 amp current limit. Let's go I set. So let's turn the current limit right down there and let's turn the output on. So we got

**Dave Jones:** 10 volts at you know 1 amp on the output no no load at all and uh Whoop no 7 no 7.2 volts not. She's gonsky and it's reading an amp Um, 8 W, there's not nothing on the output.

**Dave Jones:** Not Hang on. Think I can smell something again. Hmm. This ain't good. Oh, yeah. I mean, like, you know, it's drawing 1. You know, 1.9 W quiescent um with nothing on. And if we switch that output uh that output on again, whoa. Yep, no. It

**Dave Jones:** was drawing like 10 plus W up there. No, it's one one sick puppy. Yeah, it's actually drawing 17 W. Yes. So, um that is one sick puppy. Um, I don't think I'm going to try and uh trouble shoot that without a schematic.

**Dave Jones:** Um, I think she's Well, we could, you know, I could try and trace it out, reverse engineer it, but I'm not going to do that right now. It's like uh 10:30 um at night, and uh I need to edit this

**Dave Jones:** video and uh get it up and go home. So, Mrs. EVBlog doesn't get too upset that I work too much. Hmm. Yeah, for those who want to see what's under the heat sink, got ourselves a uh seal pad there.

**Dave Jones:** Trademark. Um Oh, there we go. Hey, is that There you go. Um let me get those under the uh microscope and see if I can get a part number. And we've got ourselves uh four N-channel MOSFETs. These are Alpha

**Dave Jones:** Omega. I love that uh uh company name. Um terrific. These are D2810. That one's upside down, so all the electrons are falling out. So, that was uh what our problem was, clearly. Um but, there are They look like They're

**Dave Jones:** certainly not from the same same batch, are they? They're uh They're quite different, but yeah, we've got four of those there. 80 V uh 40 A N-channel MOSFETs. So, fairly you know, fairly grunty little beasts. And also under here, um that's obviously not a

**Dave Jones:** switching converter. You can uh switching controller cuz I it's got a designated Q, which is a transistor, and it's got your three pins tied together here or four pins tied together over there, and that's your gate down in

**Dave Jones:** there. Your classic MOSFET configuration. Once again, Alpha Omega. Um, AO 42 uh 64. And this is a 60 V 12 amp job in series with, mind you, a polyfuse. Look at that. Poly put the kettle on. So, what

**Dave Jones:** that one's actually doing, I don't really know. Um, cuz it's not the switching controller. Our main switching controller is the XL 7005. I believe we saw that last time on the modules. We've just got some input transistors over

**Dave Jones:** here. And so, that's coupled with the TL 594, the classic PWM uh controller in there. And then we've just got the quad op amp up there. And all together, it's actually quite a complex beast. I'd love to see the full schematic of it. Reverse

**Dave Jones:** engineering this is quite possible, but it's quite a task. So, I'll leave that to someone else to do. I'm not sure if Glenn wants to share the schematic with us, but yeah, like there seems to be no other

**Dave Jones:** damage though, but well, physical damage, but obviously electrically something else is gonski. So, there you have it. That was supposed to be a review video on the DPS 5020 and the nice little case it comes in and everything else, but in the end it was a

**Dave Jones:** complete balls up, and it's just like bad luck that I got a unit that possibly had a damaged cap. I don't Once I As I said before, I don't know if it's like under spec or something like that,

**Dave Jones:** whether or not it was soldering damage, whether or not it was just unlucky that that ceramic cap failed. You know, infant mortality component infant mortality is a thing and they often fail short and catch a light like that. Not particularly common, but it

**Dave Jones:** does actually happen. Sure enough, it happened to me. Sometimes you get lucky. I'm off to buy a lottery ticket. Catch you next time.
