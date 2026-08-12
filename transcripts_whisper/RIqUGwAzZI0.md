---
video_id: RIqUGwAzZI0
title: OpenROV - Open Source Underwater Robot - Sydney Maker Faire 2013
url: https://www.youtube.com/watch?v=RIqUGwAzZI0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 42, "3": 55, "4": 81, "5": 101, "6": 128, "7": 146, "8": 156, "9": 174, "10": 191, "11": 208, "12": 224, "13": 242, "14": 265, "15": 281, "16": 296, "17": 314, "18": 331, "19": 348, "20": 366, "21": 386}
---

**Dave Jones:** We've got Dominic, and he's from Open ROV, and he's going to tell us about this beastie. That's an Open ROV. It's a remote operated vehicle. It's an open source underwater robot, or rather right now, remote operated vehicle. It's not autonomous yet. Yep. We're getting at the point.

**Dave Jones:** We're selling kits through the shop in the US. Sell about 870 US dollars right now. Yep. Remote control through your laptop. So you have a webcam, you have lights, you have three props. We had the unit going down to 90 meters successfully. Is it wired or wireless?

**Dave Jones:** Wired. So it's wired. Yeah. Right. You don't get any wireless. Wireless. I was going to say wireless is going to die at about half a meter or something. Yeah. Not even. You get telemetry probably, but you cannot get video. Yeah. No, no, no.

**Dave Jones:** You definitely wouldn't get video. You get very low board rate telemetry, maybe. Yeah. So we bound to a tether, but we use HomePod adapters to facilitate communication. So the same stuff you use in your mains at home to connect two rooms. We have that one, and it runs on 100 meter, 200 meter cables.

**Dave Jones:** Pretty good bandwidth. Yeah. Fantastic. So you can get video and what sort of telemetry data do you get out of it? We get depth, time, pressure, temperature, compass heading, and it has a nice great CBUS connection. So you can add all the sensors.

**Dave Jones:** Some people talk about salinity sensors and things like that. So it's an extendable platform and it's all open source. You just go and download the data source and extend it yourself and add your own sensor. Got it. And how buoyant is it? Like it normally floats and then how much pressure is required to get it

**Dave Jones:** under and down to depth or is it neutrally buoyant or? Yeah, it is neutrally buoyant. It is neutrally designed to be neutral. Yeah. Right. So in saltwater, it's slightly positive. Right. But you can add some more washers or some screws to make it a bit heavier to compensate for whatever

**Dave Jones:** environment you use. But you'd probably want it to be slightly positively buoyant because if it fails, you want it to float to the surface, right? Yeah. Eventually. Well, there's still the tether. And then the tether, you just pull it up. You can actually pull it up.

**Dave Jones:** So the cable's anchored on there as well. Has it got a mechanical stiffener in there as well in the anchor cable, in the cable? No. So as it comes from the kit, it's just the cable, the two-wire cable. I've seen people talking about putting like fishing line on it.

**Dave Jones:** They armor it in some way too. To, yeah, strengthen it. The thing is you can't get it too stiff, otherwise it won't move enough, or the raft uses too much power to move the cable around. Oh, got it. Of course. Yeah. Yeah. And then as well, you can't use a tether that is too buoyant,

**Dave Jones:** otherwise it pulls the rice up or too heavy, it pulls it down. Yep. Yep. So it's a bit the right approach to find. Got it. And so we use the top propeller here to control the, whoop, there it is. Yep. It's controlled and we're getting video.

**Dave Jones:** There we go, we're getting video out of it. Ta-da, that's me. Yeah. Fantastic. So we're getting live video. Yep. Out of that thing. And it's got a camera in it, so there's the camera in the front. Can that tilt up and down by the looks of it?

**Dave Jones:** It can. It can. There we go. So that tilts up and down. Yep, up. Nice. Yep. Excellent. It's got the LED lights, of course. And the batteries are in. These are in the cylindrical bottom parts there. And where's the forward and backward propellers?

**Dave Jones:** They're on the back. They're on the back. There they are. Neat. Woo hoo. Of course. Very nice. Good one then. Excellent. How's the, would it be better to have like a, actually have some propellers on the front and the back in like, would it go forward, would it tilt and tip?

**Dave Jones:** Is that an issue when it... Um, it is a little bit. It's, when you see, see the videos of, of the ROF, when you power it on, it is kind of... I was gonna say the tilt forward and it... It, it kind of goes, goes a bit up, not up, but, but, uh, starts to rise.

**Dave Jones:** Um, might be better to have one on the front, but it's gonna be more difficult to balance it out and stuff. Got it. Uh, and the more, the more cables you run through, the more troubles you get with, with... Of course. ...sealing everything.

**Dave Jones:** Yep. Um, so with the E-PROPS, we, we're fairly good right now. Mm-hmm. Um, someone started to build like little, little wings on the side to make it more stable. Yep. And he, he had some great results with that. So... Nice. And it's, as it's open source, he pushed the stuff, uh, on his GitHub repository and, uh...

**Dave Jones:** Fantastic. ...he takes from that. And what's the main, what's the main controller in there? Uh, the main controller is a BeagleBone Black. Okay. Uh, in combination with an Arduino. So we have an 18-megachip on there, um, and it communicates with the BeagleBone Black through

**Dave Jones:** serial connection. Uh, why, why the two separate processors? Um, because the Arduino is more suited to control stuff like, um... Of course, yeah. ...like speed controllers and servos. You can do the same thing with the BeagleBone Black. Mm-hmm. You need to do a little bit more.

**Dave Jones:** And Arduino is very common in... Of course. ...projects like this. Yep. Um, on the BeagleBone Black... ...we run a Ubuntu, uh, customized for us, um, and run a Node.js server. Mm-hmm. So the, the whole front end and the server back end is written in JavaScript.

**Dave Jones:** Got it. Um, and just the communications with sensors and, uh, the, the motors is done in Arduino Secrets Plus. Excellent. Well done. So, what's the kit worth? About $800 or something you said? Um, $858.70 US dollars at the moment. Nice. Yeah. I like it.

**Dave Jones:** And, uh, yeah, if anyone wants to build one here, we might get, uh, a bulk order getting together at one point. So, uh, get excited. Excellent. Great. Thank you very much, Dominic. Thank you.
