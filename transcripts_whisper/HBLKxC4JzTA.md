---
video_id: HBLKxC4JzTA
title: Space Electronics Circuit Protection
url: https://www.youtube.com/watch?v=HBLKxC4JzTA
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 44, "3": 69, "4": 88, "5": 98, "6": 113, "7": 133, "8": 148, "9": 164, "10": 178, "11": 197, "12": 215, "13": 228, "14": 248, "15": 268, "16": 287, "17": 312, "18": 337, "19": 354, "20": 365}
---

**Dave Jones:** Note to myself during editing, this is the clip that goes into the electronics section, just so I know. All right, circuit protection. How do you protect this thing? Because we'll do another video on radiation where you can get SCR latch-up, which is probably the worst possible condition.

**Dave Jones:** How is it fused? Do you have resettable fuses? How do you deal with latch-up? Yeah, so for example, with latch-up, for example, there are some pretty nice chips which can actually completely deal with it. Oh, are there? Yeah. What is it? FD2020, for example?

**Dave Jones:** Oh, okay. Something like this. Right. So you've got some dedicated hardware in there to prevent SCR latch-up. Yeah, so those are really kind of useful for detecting high transients beyond QR. Yeah, so you don't get transient spikes, because that's what SCR latch-up will do is basically shorts out your rail, if you don't know, shorts out your voltage rail, so you'll get this large spike that is not part of normal things.

**Dave Jones:** Yeah, so the thing is that, for example, the chip is really nice. It's actually, it waits for, what was it, like, I think one millisecond, and then it's... Right, and it kills power straight away. Yeah. Yep. So that's pretty neat, for example. Bypassing, pain in the ass, because bypassing on your power supply...

**Dave Jones:** If you've switched off your power, if you've got a lot of bypassing there, there's a lot of energy stored in those caps. They can still continue to dump the energy. Yeah, but this is also... So where do you put these chips? Do you put them after the bypassing?

**Dave Jones:** Yeah, yeah, definitely. Right. Exactly, otherwise you're screwed. Yeah, yeah, yeah, no, no. Trap for young players, folks. Don't put your bypassing after you. Yep. Yeah, no, you have to do that, yeah. But it's also, you know, pulling it to a crown, so not just letting it float.

**Dave Jones:** Oh, okay. Oh, it pulls it. Right, got it. So it protects it that way. What about just general? Fusing, resettable pulley switches, all that sort of jazz? Yeah, so we did some experimentation with pulley switches in the past, for example, for our motors, and that wasn't the best idea.

**Dave Jones:** Why not? Do tell. Yeah, because the thing is that, you know, when you're driving motors, then the spikes are significantly higher than you expect. And so if you apply your voltage meter and you look at the current and you say, it's like, oh, okay, this is just about 1 amp, so it will take us...

**Dave Jones:** It's like a 3 amp fuse, and then you're like, it kicked in unexpectedly, let's put it this way. Unexpectedly, yeah, transients are a big problem. Measuring your current transients, you need specialized test gear to do it. You can't just, you know, whacking your amp meter and, you know, hope it goes up there.

**Dave Jones:** Even an analog one, which, you know, your needle can't move fast enough to, you know. This is how I cut my microcurrent. And it's even, it's not fast enough sometimes, 500 kilohertz, 300 kilohertz bandwidth, you know, sometimes you can get really short current spikes that can...

**Dave Jones:** Really ruin your day. Yeah, so we're running at a pulse modulation frequency of about 64 kilohertz with the motors. Oh, okay, right. Is that synchronous to anything else, so you don't get radio interference and stuff like that? No, you just don't care, because the motor controllers are out here and you don't care.

**Dave Jones:** This is one of the significant advantages of having them outside here, you know. Physically separate. So, you know, the thing is that this is aluminum, so it's really well sheeted, and yeah, this makes it much easier. It makes it much easier. The question really is, it's about which parts do you want to shut off?

**Dave Jones:** So, where you have to, you know, if something goes wrong, what is your failure state, you know? You don't want to kill everything. You don't want to kill your radio. Yeah, exactly. If one motor goes, you don't want to kill your radio. You want to be able to still change it, right?

**Dave Jones:** Exactly. Yeah, so this is, for example, one of the questions that you have to deal with when you're saying, okay, let's make three CPUs. For example, for the lender, you know, this, you might think that, oh, let's, for the ones that is controlling the engines, we definitely need to have three of them.

**Dave Jones:** And then you realize this gets really tricky, because if you just do, you know, majority voting of the signal that controls the pulses for the thrusters, for example, they might be shorter than what you need. So, this is where it gets, where adding redundancy gets very tricky, and you need to deal with.

**Dave Jones:** And so, for some points, we just say, okay, for example, with the thrusters, we just have one single board computer that does the control of all the thrusters. Right. And it's a single point of failure. Yep. And we are accepting it, because we don't have the engineering capacity and the energy to do it the easy way.

**Dave Jones:** So, it was a case of rover first, worry about lander second. Yeah, yeah, yeah. Right? It was. Essentially, yeah. Yeah. Another thing is that the rover is. It's very easy to test. You can take it to a playground. Yeah, it's very easy. But with a lander, it's really hard to test it, because the thrusters that you have don't actually work on Earth in an oxygen environment.

**Dave Jones:** They are made for vacuum. And they don't have the ability to lift the lander at a 1G gravity. They are designed to avoid enough lift for 1.6 gravity. So, all of that together makes the. So, we are developing the lander, a pretty big challenge that we wanted to address in the latest part where we went, where we were sure what the requirements are.

**Dave Jones:** And you've got solid funding to. Oh, yeah, and the funding is also interesting. Because lander is not sexy. Nobody, look, we've got a lander. Oh, it's kind of sexy. You know, but come on, you can't sell that to Audi. They don't want a lander.

**Dave Jones:** No, give us the rover. We want our logo on a rover, you know. So, yeah, the rover is something that people can relate more to. They can relate more to it. It's better. And it's fun. Come on, the rover is more fun than the lander.

**Dave Jones:** Yeah, yeah, I agree.
