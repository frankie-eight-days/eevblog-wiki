---
video_id: 1q2rnKExMiY
title: EEVBlog #263 - Extech LP100 Laser Test Probes
url: https://www.youtube.com/watch?v=1q2rnKExMiY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 39, "3": 57, "4": 72, "5": 96, "6": 108, "7": 123, "8": 144, "9": 163, "10": 188, "11": 203, "12": 220, "13": 241, "14": 268, "15": 282, "16": 295, "17": 315, "18": 332, "19": 350, "20": 364}
---

**Dave Jones:** Hi, I got a press release yesterday from Extech, because I follow Extech's stuff. And this thing popped up, and it was rather bizarre, unusual. I've never seen anything like this before. So I thought I'd just mention it. It's a... well, here it is.

**Dave Jones:** Extech adds safety to high voltage testing with the first ever laser non-contact laser test probes. Go figure. And it says here, the new LP100 series laser probes leverage existing laser voltage probe designs with voltage and timing waveform acquisition technology previously only available at the scale intended

**Dave Jones:** for flip chip integrated circuit analysis. I had no idea you could even measure voltage at a distance with a laser. Go figure. And in addition to some marketing blah blah bullshit they've got in here, it says one laser acquires waveforms from the electrical source while the other laser creates a reference

**Dave Jones:** to eliminate unwanted noise from the signal data that is acquired. And if you take a look at the photo here, it actually shows a red laser coming out, but it actually says in here that it's infrared. So they've obviously got like a dual laser,

**Dave Jones:** just like those laser thermometer things work, you've got to have a visible red laser to actually show your target that you're actually targeting on. So the red laser does nothing, but it would have another, presumably have another infrared laser in there, separate die or something like that, laser die, one for measurement and one for actually aligning

**Dave Jones:** to show what you're actually targeting. Because if you couldn't see it, then you'd just be pointing it in the air and you wouldn't, you know, if it's a couple of feet away, five, six feet away, you wouldn't be able to know exactly what you're targeting.

**Dave Jones:** Phew! Anyway, I have no idea how this thing works at all. I haven't got a clue. But thankfully, the new EEVblog apprentice, Phil, has a PhD in laser physics, and he's tried to figure out exactly how it works, and he may have cracked it.

**Dave Jones:** Maybe. Thumbs up. Let's go, Phil. All right, Phil, you reckon you cracked it? What's going on? They don't give us enough, give us a lot of detail. Phil's voice is a little bit better, by the way. It's getting better. If you heard it last time, he had an operation, it's getting there.

**Dave Jones:** So they don't give us a lot of detail, except that they're using two lasers for noise reduction and that, but it still doesn't explain how they do it. What I think they could be doing is possibly using the Faraday effect, Faraday rotation through an air space.

**Dave Jones:** So they have their laser, which is a polarised laser, travelling through an air space. It has some dielectric strength, and if you apply a high magnetic field to that, you get a rotation of that polarisation. Because I spoke to Extech, and they said that it does have a maximum distance, of course, of a couple of feet.

**Dave Jones:** You wouldn't get much, because the magnetic field strength would drop off very quickly. You'd only have a small interaction length, so you wouldn't be able to get too far away from it. Closer you can get would be better, but there'd be an optimum distance.

**Dave Jones:** Because it's designed for high voltage, this only works at, Extech told me it only, gave me a quick email, they didn't know all the technical details, but it only works at like hundreds of thousands of volts. It's designed for high voltage. Yeah, so you'd need a really high voltage, and you'd still only get a small rotation in the polarisation

**Dave Jones:** due to this Faraday effect. So what they're probably doing there is they're just shining their laser at their wire with the magnetic field. It could be a bus bar, or it could be anything. Yeah, high voltage stuff. And the laser would get modulated passing through the field,

**Dave Jones:** and you'd get a small rotation in the polarisation. So when it came back, you would have a polarisation sensitive detector, which would have some relations like this. So as you increase the rotation, your sensitivity decreases quite dramatically. So you'd be able to get an indication of how much field strength you've passed through.

**Dave Jones:** Yep. And then get your measurement from that. And that's how they would get it for DC as well as AC. As well as AC, yeah. Yep, got it. So you don't necessarily need a current on your wire. Just electrostatic field would probably be enough.

**Dave Jones:** So it's similar to how the voltage detection sticks. You'd be very close to it, yeah. Because they can work with no current flying through. Right. That's what I think they could be doing. Right. But you'd have to have a look at the patents or something.

**Dave Jones:** Yeah, exactly. They've got some magic going on there. Have to do a search on the pads. Right. So it's something to do with Faraday rotation through the air. So the angle of rotation is directly proportional to the Verde constant for air, which is how susceptible it is to be affected by a magnetic field.

**Dave Jones:** Right. The magnetic field itself and the distance that it travels in that field. So you'd have that maximum distance here, and you'd be able to extract out your field strength, and from there you'd be able to get the voltage on the wire. Neat.

**Dave Jones:** It's quite nice. So it's plausible. Plausible. Yeah, we don't have a MythBuster-style one where we actually chisel it out or something like that. It is plausible. Yeah. All right. Well, I'm going to have to get one. They're going to have to send it to me.

**Dave Jones:** We'll do a tear-down and some tests. But, yeah, I'll have to find some real high-voltage, high-energy stuff to work on, but I'm sure that's not a problem. Nice. Thanks, Phil. Nice. See, your PhD, it did come in useful. You didn't waste it. Finally.

**Dave Jones:** Finally. Awesome. Catch you next time. Bye. Bye. Bye.
