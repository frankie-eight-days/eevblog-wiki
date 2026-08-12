---
video_id: xo4sojpJIBI
title: EEVblog #1170 - TRUE Mystery Teardown! (not even Dave knows)
url: https://www.youtube.com/watch?v=xo4sojpJIBI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 27, "2": 43, "3": 82, "4": 93, "5": 122, "6": 146, "7": 169, "8": 174, "9": 176, "10": 200, "11": 218, "12": 242, "13": 260, "14": 274, "15": 290, "16": 320, "17": 320, "18": 350, "19": 350, "20": 380, "21": 410, "22": 410, "23": 448, "24": 476, "25": 496, "26": 521, "27": 550, "28": 570, "29": 586, "30": 586, "31": 589, "32": 589, "33": 677, "34": 699, "35": 719, "36": 748, "37": 767, "38": 777, "39": 797, "40": 821, "41": 842, "42": 859, "43": 881, "44": 886, "45": 894, "46": 914, "47": 930, "48": 949, "49": 967, "50": 995, "51": 1007, "52": 1023}
---

**Dave Jones:** Hi, it's time for another mystery teardown. And when I say mystery teardown, I really mean it, because I have no idea what this is until we actually tear it down. I found this in that big dumpster raid, which I'll link in at the end and down below if you haven't seen it, with a whole bunch of stuff in a dumpster from a mysterious technology company that I'm not allowed to mention.

**Dave Jones:** Anyway, this looks like a powerpoint, and it is a regular, oh, it's a 15 amp jobby, by the way. It's got the larger earth pin here. It's physically longer than the regular 10 amp one, so that's like the industrial 15 amp outlet. So, anyway, it looks like a regular powerpoint, but, like, where does the mains go in?

**Dave Jones:** Where's Wally? Where's Wally? I guess the mains goes in through a little... Mini-B connector, does it? And some other... Is that a micro-USB? Mini-B and a micro-USB. Um, so, like, what the? What the? Like, I... If it was something that took the mains as an input and then outputted something, like it measured something or outputted something, then it wouldn't be in this form factor.

**Dave Jones:** You wouldn't plug a male-powered male pin into a female receptacle. So, what on earth is it doing? Well, only one way to find out is to tear it down. So, if we rip the back off here, there's actually a battery door in this.

**Dave Jones:** So, it's actually battery-powered. So, oops, that just comes right off. And we have a little hobby lithium battery in here, one of these nanotech jobs. That looks a bit puffy, doesn't it? Hmm, anyway. Anyway, 7.4-volt job to sell this side up. There you go, thank you.

**Dave Jones:** Nice label in there. Ooh, dangerous voltages inside, do not open. It's okay, I'm a professional. Return to Platypus Instruments for repair. Platypus Instruments, I love. Look at this, I love the logo. That logo is just fantastic. See the platypus, his little eyes, and the little bill, surrounded by an ohm symbol.

**Dave Jones:** It's great. Anyway, Platypus Instruments, don't go look them up now, because it might be a spoiler for you if you want to try and figure this out from the teardown. But this is a specialized instrument. The company only makes, as far as I know, they only made this, and it came out in mid-2017, so it hasn't been out very long.

**Dave Jones:** So, obviously, the company who I got this from didn't need it anymore, and they tossed it in the dumpster, or it got thrown out, wet accident. So, obviously, the company who I got this from didn't need it anymore, and they tossed it in the dumpster, or it got thrown out, wet accident.

**Dave Jones:** So, obviously, the company who I got this from didn't need it anymore, and they tossed it in the dumpster, or it got thrown out, wet accident. So, obviously, the company who I got this from didn't need it anymore, and they tossed it in the dumpster, or it got thrown out, wet accident.

**Dave Jones:** Whatever it was, or it doesn't work, who knows? But, yeah, it's a specialized bit of test equipment, believe it or not. Well, it's actually test equipment to test test equipment. Can you figure it out yet? So, obviously, we've got a lithium ion battery input here, reset button.

**Dave Jones:** We've got a programming port there, and dangerous voltages inside. So, let's crack it open. So, let's crack it open. So, let's crack it open. So, let's crack it open. So, let's crack it open. All right, let's have a look inside. Ta-da, look at that, there's one big ass cap.

**Dave Jones:** And of course, yes, it does actually output, ooh, the Pi 3 version, 3.3, March 2017, there you go. So, it was actually released in mid-2017, and we've got a couple of leads there, too, by the way. the way, which is quite nice because they've used the existing holes on the, these are normally the

**Dave Jones:** screw holes that you, you know, put into the screw into the plate in the wall. They've actually used those screw holes as little lead. They've got little reverse leads on there. Anyway, that's pretty cool. So we've got a big ass cap on there and got a couple of, a couple of tranny, that looks

**Dave Jones:** like a, some sort of, oh no, worth electronic components. Yep, is that a custom tranny or off the shelf? Anyway, got a couple of chokes in here and geez, there's not much else, is there? So, actually, there's a fair bit on the bottom and that's where all the goodness is.

**Dave Jones:** Let me get that out. Actually, the first interesting thing to note here is, look at this micro switch. This is actually, looks like it's a safety micro switch. It's a safety micro switch interlock because it was normally pressing against the back of this plate.

**Dave Jones:** So, it's designed to detect when we've actually removed the board from there. And if you have a look where it's connected over to here, it looks like it's connected to some big beefy part of the, obviously, some sort of power supply system. So, it's designed to maybe shut it off or maybe even discharge this huge, oh, Rubicon.

**Dave Jones:** Nice, 450 volt, 220 micro farad cap. So, yeah, maybe some sort of safety interlock to, you know, if people do take it apart to prevent, well, to think you'd discharge the cap anyway, wouldn't you though? But, I don't know. So, I'll briefly explain what it looks like we've got here.

**Dave Jones:** You'll notice like we've got different blocks all around here. They seem to be sort of separate functions. So, what we've got down here, this section, it's a little bit mysterious. You know, it's got a power tranny there and what a couple of optos.

**Dave Jones:** And this is actually an LM358. So, like, and there's nothing on the backside, by the way. So, almost all the circuitries on the top side except for these transformers and the cap and this power resistor here. So, that's an op amp and just something else.

**Dave Jones:** This section here, this is actually a PIC 12F series micro. And these two chips here, are actually half bridge drivers. So, that's what these two power MOSFETs are here for. And we've got a diode up there. And that ties in with this. So, is that a common mode choke or a transformer?

**Dave Jones:** I'm not sure what's doing there. You'd have to look at the configuration anyway. So, that's got the 400 volt huge cap on there. So, obviously, this section here is tied into the half bridge drivers here with the MOSFETs. And then here's our output here, by the way.

**Dave Jones:** This is our mains output. And it is actually an output. It's not an input. You don't plug anything into it like mains into a female socket. That's not how it works. So, it actually outputs stuff. And this section up here, we've got another PIC micro.

**Dave Jones:** That's the programming port, of course. We've got a fuse in there. We've got a big shunt resistor up there. And this is a, you know, really schmicko MOSFET. And another grunty looking MOSFET here, which seems to be driving this transformer here from Worth.

**Dave Jones:** And then the output side of this goes over to here. Oh, look. There's some traces tapping off over to here. So, that's probably doing some sort of measurement functionality. It's probably not driving anything, is it? I don't think so. I think it might be tapping off there and measuring.

**Dave Jones:** And then the output of that is obviously tied in somehow into our mains output here. And on this section over here, classic 34063. I've done a whole video on that, I'm sure, way back in the day. Buck boost converter. So, yeah, look. Nice big 270 ohm power resistors

**Dave Jones:** there. Aren't they nice? And, well, what is this thing? Have you figured it out yet? Hmm. I might let the original designer tell you. Roll the videotape. Hello and welcome to Platypus Instruments. What I'm about to share with you may be an interest for you in your personal safety, your business productivity increase, and efficiencies.

**Dave Jones:** We have patented a pocket inverter, which we use for full trip time testing portable RCDs. The inverter is 240 volt, 50 hertz, pure sine wave, earth neutral bonded, is a very safe form of isolated power supply, and also contains a 360 volt DC outlet for voltage

**Dave Jones:** proving. The inverter totally eliminates the requirement to connect the mains power and its hazards, totally eliminates the requirement of isolation from the main power supply. And, of course, if you have a portable appliance tester with RCD facilities, even if you have an isolation

**Dave Jones:** transformer, you still need power. And some portable appliance testers cannot do 250 volt IR testing, so they have to do leakage testing. The inverter meets all those requirements. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments.

**Dave Jones:** Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments.

**Dave Jones:** Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Thank you very much, Trev, from Platypus Instruments. Somewhere here in Sydney, I believe. And it's actually hard to find information on this thing, because all they've got is a Facebook page like this.

**Dave Jones:** They did have a website, but it's Gonski, as in, like, the domain is gone. And it seems to be like a startup thing that they started, and there's videos talking about it. I think this is like the investment guy, or not investment, like, advisement, like startup advisor guy or something like that.

**Dave Jones:** Please, Trev, if you have any questions, please let me know. Please, Trev, if you have any questions, please let me know. Please, Trev, if you have any questions, please let me know. I thought I'd do a little spiel on that, and I happen to have my brother-in-law, Phil, who is a patent attorney here, and at the time, he was just hanging out at the lab the other night, and I shot a video all about patents, and it ended up being a half-hour thing.

**Dave Jones:** So I won't go through that. I'll link it in at the end and down below. I highly recommend you watch it to know all about the difference in everything to do with patents. Anyway, it was fantastic. So here is a diagram for it.

**Dave Jones:** Sorry, that's the crudity that it comes with. Anyway, it's got a battery charger in here, of course. Those were the extra connections you saw on the battery there. They were the inner cell taps, of course, to balance charge the lithium. There's a low-voltage microprocessor in here, so that would be the one on the high side.

**Dave Jones:** There's a PIC-R16F series on the high side, and there's a DC-to-DC converter here, and this is the isolation transformer, that custom-worth. Isolation transformer that we saw, and then there's a regulator here, and there's also got that PIC-12F series micro. It's the high-voltage microprocessor.

**Dave Jones:** The microprocessor, of course, doesn't work at high voltage. It's still a 3.3 or a 5-volt microcontroller, but its ground is floating at 240 somewhere, you know, on 240 volts. So it's totally isolated from the other microprocessor over here. So there you go, and there's the H-bridge output filter.

**Dave Jones:** So, of course, we had a half-bridge driver, but we had two of those chips, and four and two transistors per half-bridge. So we've got a full H-bridge driver, and that generates our sine wave, and it can measure back. So, Bob's your uncle. That's it.

**Dave Jones:** It's, you know, it's pretty simple. And, oh, I have to link in the patent at the end, and it goes through the background of the invention and stuff like that. Phil says that this... This is a bargain basement patent. It's not very long.

**Dave Jones:** It's not... He didn't do it himself, but, yeah, it's not hugely comprehensive, but it gives you some detail. There you go, 60 kilohertz PWM, and the high-voltage cap is, of course, charged to 400 volts DC, sustains large voltages, short-term transient output load currents as required for loads.

**Dave Jones:** The high-voltage CPU includes a frequency reference from which the 50-60 hertz output for the PWM is defined, the PID control loop that stabilizes the output voltage, H-bridge over-current protection, supplementing the protection inherent in the analog design of the bridge. In addition to the analog bias voltage removal circuits described above to protect the MOSFETs, oh, we missed that,

**Dave Jones:** it also monitors the current flowing through the JFETs, since the microprocessor is the source of the switching bias voltage signals. By detecting the overload condition, it can reduce the magnitude of the commanded output to reduce the transient currents present. The output regulation... is performed by the PID algorithm.

**Dave Jones:** There you go. Via the isolation transformer 22, it wasn't labeled, there were no enunciators on the diagram. So, the CPU generates bursts of 35 kilohertz signal to measure the impedance presented by switch 31. There you go, that's interesting. Nice, that's like a, like an ESR measurement, like you'll, um, do measure ESR of capacities, you'll do that at 100 kilohertz, typically.

**Dave Jones:** In this case, the 35 kilohertz to measure the impedance, and the switch, excellent. A high impedance presented by the switch 31, there you go, that's interesting. Nice, that's like a, like an ESR measurement, like you'll, um, do measure ESR of capacities, you'll do that at 100 kilohertz, typically.

**Dave Jones:** In this case, the 35 kilohertz to measure the impedance, and the switch, excellent. A high impedance presented by the series resonance circuit, I won't go through the whole details of how this whole thing works, you can argue it out in the comments, in discussing the comments.

**Dave Jones:** Conversely, a closed switch presents low impedance, removes the need for a separate power switch, and presents the user with a familiar GPO on/off switch, which also serves the additional, traditional function of high voltage AC switching. Thus, the low voltage CPU 16 is able to sense the state of power switch 31 and GPO 30 on the other side of the galvanic isolation barrier.

**Dave Jones:** Nice! It's capable of... delivering 20 watts of sinusoidal 240 volts to the load indefinitely. Well, that little battery's not going to last too long at 20 watts, is it? Or 500 watts for short, tens of milliseconds duration, cater high peak currents and deviance for the device under test.

**Dave Jones:** Well, I thought it was only for testing the portable appliance tester. Maybe I don't know the details of exactly what tests the portable appliance tester does, and we won't go into that, but yeah, suffice it to say, there was obviously a requirement to have short-term high-current, high-power pulse capability.

**Dave Jones:** Of course, here in Australia, we use the MEN system, the Multiple Earth Neutral Bonded System. It just goes through the conventional approach to testing RCDs and stuff like that. There are the claims for the patent. So, there you go. That's all there is to it.

**Dave Jones:** A neat little bit of niche test gear. Nice. All right. Let's see if this works. I'll power it up with an external 7.4 volt supply. So, give it a bell. Switch. Off. On. Nah. Sorry. I'm not going to troubleshoot that. But anyway, I hope you enjoyed that little mystery teardown

**Dave Jones:** for this really niche little bit of equipment that's actually designed and engineered really quite well. I really like it. And I think it's going to do it for a specific purpose. It does its job, and it looks like it would do it superbly.

**Dave Jones:** So, I'm not sure what, if Platypus Instruments are still going, can you still buy it? I don't know what the deal is. But, yeah, great example of a niche product. So, if you like the video, please give it a big thumbs up. And, as always, you can discuss down below in the forum.

**Dave Jones:** And, if you want to talk about this, I guess you can email Trev. His email was in the video there. Go for it. I'm sure he'll happily answer all your questions. Catch you next time.
