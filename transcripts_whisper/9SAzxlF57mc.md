---
video_id: 9SAzxlF57mc
title: EEVblog #1120 - How To Understand Polarised Light
url: https://www.youtube.com/watch?v=9SAzxlF57mc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 35, "3": 53, "4": 64, "5": 83, "6": 103, "7": 116, "8": 130, "9": 140, "10": 154, "11": 167, "12": 182, "13": 197, "14": 219, "15": 237, "16": 248, "17": 267, "18": 282, "19": 299, "20": 313, "21": 335, "22": 347, "23": 364, "24": 381, "25": 398, "26": 412, "27": 425, "28": 445, "29": 461, "30": 478, "31": 498, "32": 512, "33": 524, "34": 539, "35": 552, "36": 565, "37": 583, "38": 595, "39": 607, "40": 624, "41": 639, "42": 651, "43": 663, "44": 678, "45": 694, "46": 707, "47": 724, "48": 738, "49": 753, "50": 765, "51": 776, "52": 789, "53": 809, "54": 827, "55": 846, "56": 857, "57": 870, "58": 886, "59": 905, "60": 919, "61": 934, "62": 949, "63": 962, "64": 979, "65": 990, "66": 1003, "67": 1016, "68": 1029, "69": 1045, "70": 1058, "71": 1070, "72": 1082, "73": 1097, "74": 1114, "75": 1129, "76": 1144, "77": 1159, "78": 1177, "79": 1192, "80": 1207, "81": 1220, "82": 1231, "83": 1245, "84": 1260, "85": 1276, "86": 1292, "87": 1309}
---

**Dave Jones:** And I'm here with Gav, the mechatronics guy. You've seen Gav before, and he's going to show us what he's been working on. My obsession recently has been polarised light, and I've been off and on this one for a couple of years. So, I've been playing around with polarised light and I really, really love it, and it's a really interesting kind of...

**Dave Jones:** Polarised light is all around us, and we can't see it, and that frustrates me. I think it's rude. So, this is a modification I made of something made by David Prucci, who won the Hackaday Prize a couple of years ago for the Dolpi polarisation camera.

**Dave Jones:** And it's using some LCD shutters that I've modified and put extra layers on. These are LCDs from shutter glasses, like 3D... Oh, sorry, so they're one plane. One pixel, and you can kind of model them as a voltage-controlled wave plate, but we'll get to that later.

**Dave Jones:** But if we... I don't know if we can shoot through here and look at the tables. We'll try it. Let's give it a go. So, this is just an ordinary scene with some tables, and if we put this in front... They're pulsating. And it's not...

**Dave Jones:** We're not looking at particular mirrors or anything. This is just sheen on just a plastic table or grass that's a little bit damp, or these tiles. And it's totally changing the polarisation, having done that bounce from the sky to us. And in the same way, everything we look at is slightly not quite perfectly polarised,

**Dave Jones:** so we get information there that we just totally can't see normally. And our second example for that is if we look through the circular one. So, the circular one's not really doing much. You can see a little bit of a flash there. That might be more to my device being a little bit imperfect about the rotations around the sphere it's doing.

**Dave Jones:** But if we go and look at the table... So, if we look at the stuff on the table... We can see one of the lenses is... Why is it not flashing? It wasn't flashing before when I was looking through it. There we go.

**Dave Jones:** Oh, there we go. Because you're alternating the... That's it. Right-hand circular, left-hand circular, right-left, right-left, right-left. And that's how the 3D cinema works. Nice. It's got to do that, you know, like 40 times a second or whatever. There's different ways... People know the light can be polarised,

**Dave Jones:** but there's actually really different ways that it can be polarised. So, if you can see the light does stuff to electromagnetic... Let's say electric field. And if it's coming in, it could grab a charged particle and kind of move it up and down.

**Dave Jones:** And if it's moving up and down, we'll call that vertically polarised. And if it's left-right, we'll call it horizontally polarised. But you could just as easily have it diagonal, so 45 degrees, or anti-diagonal, minus 45 degrees. But it's also possible if you've got something that's got a horizontal and a vertical component

**Dave Jones:** and they're a little bit out of phase, that you'll have something that produces circular polarisation. So, right-hand circular polarisation, left-hand circular polarisation. If you sort of think about all the ways these can come together, there's a model called the Poincaré sphere from Mr Poincaré.

**Dave Jones:** And here's a tangible version I built of it. This is to get it straight in my head that, you know, what's going on and what do optical components do to this. So, for example, you can have light that's perfectly horizontally polarised, and that'd be this point on the sphere.

**Dave Jones:** Or it could be perfectly vertically polarised, and that'd be that point on the sphere. And what a lot of complex optical things do, like waveplates and linear filters and sugar rotators and Faraday rotators and things like that do, is actually just a rotation on this sphere.

**Dave Jones:** So, as an example, if I get a waveplate and I drop it on there, what that actually does, this can convert horizontal light into circular light. So, if I start off horizontal and I put my waveplate at 45 degrees, then that would turn horizontal light into right-hand circular polarised light.

**Dave Jones:** And it would turn vertical light into left-hand circular polarised light. So, this is just a way to visualise the rotational aspects of the light. And this might seem a little bit weird, why I'd want to do this, because it's pretty straightforward if you're just looking at one element of a filter.

**Dave Jones:** But when you're looking at a whole bunch of filters or a whole complex optical system, suddenly it gets very complex quickly. And I wanted something to just tangibly show me what was going on. And so that's a waveplate, so that's one common optical component.

**Dave Jones:** Another thing you can have is if you put sugar and you shoot light through a sugar water solution, it's actually going to do a rotation around this axis. And ordinary biological sugar that we're sort of used to is all right-handed sugar. So, it actually does a right-handed rotation, which is doing that around the city.

**Dave Jones:** So, horizontal light through a sufficient thickness of sugar water would become diagonal light. So, you just have to dissolve it in water and that's enough to do it? Yeah. And you could tell the difference between lab-synthesised sugar and biological sugar because the lab-synthesised one's going to have an equal mix of left and right-handed.

**Dave Jones:** And on average, it's going to do nothing. Right. Oh, I get it. Right. So, it has no aspect to it. No net rotation. But here's the interesting thing. You could make right-hand sugar in a lab, but you'd have to have something that was already right-handed

**Dave Jones:** or of one particular handedness as a catalyst. You couldn't start from nothing and get a net asymmetry in the amount of handedness there. You'd have to use some catalyst which is already, or some runaway reaction, and then it'd be a 50-50 crapshoot of which handedness you got.

**Dave Jones:** Interesting. So, what is the raw sugar if you just got it out of the cane? Just out of the cane? Right-handed. Right-handed sugar. Right-handed sucrose is levosucrose. Levodextrose? Sorry. Dextrose. That's why it's called dextrose. It's dexter. It's dextrose, yes. Right. And artificial would be levodextrose, L-dextrose, whatever.

**Dave Jones:** The chemist is probably going to call me out on that, but it's close enough. And in the same way as the sugar does a rotation, you can make a Faraday rotator, which is, Ben Crow's now made this with olive oil and a solenoid,

**Dave Jones:** and you can change the direction of the applied field, same axis, and it'll do the same rotation. But that one, because you can flip the magnetic field, you can actually make it go in the other direction. So, these are three models of what three common things you might find in a lab

**Dave Jones:** due to the polarisation of light. I made another model of this conserved quantity, because the amount of horizontalness squared plus the amount of diagonal squared plus the amount of right-handedness squared equals one, which is why it's a sphere, which is why it's this conserved quantity.

**Dave Jones:** So, unless you have a filter that throws away amplitude, you're not actually going to do anything to the amplitude there, it's just going to be conserved. There's a mathematician who's called this set of things SO3, special orthogonal group three. But every filter is going to have attenuation.

**Dave Jones:** A teeny little bit of attenuation. Okay, so that doesn't matter too much. In this, a wave plate, a Faraday rotator and a sugar rotator, you can all find kind of close to ideal versions of those that don't throw any amplitude away. Something like a polarising filter, on the other hand,

**Dave Jones:** will throw away 50% of the light. And that's kind of just going smoosh to one side of the sphere. Is it, it throws away 50%? Is that an inherent? An inherent nature of everything that comes out is, I think it's the likelihood that it'll get through

**Dave Jones:** is the cosine squared of the angle, something like that. Got it. Yeah. Now, this is the Poincaré sphere, which is for polarisations of light. And I made a similar model called the Bloch sphere here. And this is another structure, which is SO3. It's a conserved quantity under rotation.

**Dave Jones:** And this is a qubit. So this is a qubit with a zero state, a one state. And because probability amplitudes are complex numbers, I won't get into that, but they're a complex thing. You can have a plus, a minus, a plus I, and a minus I as the four combinations there.

**Dave Jones:** And these are actually kind of equivalent to each other under certain circumstances. And it actually makes a lot of sense if you're thinking about doing quantum computing with photons, because a photon is often called a flying qubit. So that's the Bloch sphere. And that was the background of sort of thinking about

**Dave Jones:** these quantities and working with them. But what the wave plate does is really cool because it's doing this rotation there. And there's a device called a polarisation controller that looks like this. So it's three wave plates, one after the other. Oh, should I explain about what a wave plate is?

**Dave Jones:** Yes, please. Yeah, yeah. I should explain what a wave plate is. So if you get like a mineral like calcite, it's, what do you call it, anisotropic. It's different. It has a preferred direction of, like the crystal structure is aligned in one direction,

**Dave Jones:** which means that it kind of, because it's more dense going this way than this way, it has a slightly different speed of light going this, for like going polarised this way versus like polarised this way. And if you were to cut a calcite crystal

**Dave Jones:** to a certain thickness, then the light that's coming in, say it was diagonally polarised, that's got a little bit of a component in the vertical and a little bit of a component in the horizontal. So those two things go through the crystal. One of them, they're split into two different ways to traverse.

**Dave Jones:** They're on two travelators and one travelator is going faster than the other. So by the time the crowd recombines, there's a phase shift between those two waves and you're horizontal and vertical are now out of phase and your diagonally polarised light is now doing a circular.

**Dave Jones:** So you can use a wave plate, usually a quarter wave plate is the most common one and that'll convert linear light into circular light. And this is actually what frustrating is because if you say to a lot of physicists like, what does a wave plate do?

**Dave Jones:** And they go, a wave plate converts linear light to circular light. It's like, no, it doesn't, it really doesn't. It can, but if we jump back to the block sphere, the Poincaré sphere. So this is most definitely converting, say vertical light into right-hand circular polarised light

**Dave Jones:** if we do that, right? But what if I put in light that was diagonally polarised? It's not going to do squat because its axis is lined up with the axis of the wave plate. And so there's actually always going to be two points

**Dave Jones:** where it does absolutely nothing and it'll convert and it does kind of lesser conversion. So if you had a little bit diagonally polarised and a little, but mostly diagonally and a little bit vertically polarised and you need a rotation, it'll be still mostly diagonal,

**Dave Jones:** but it'll just be a little bit right-hand circular polarised. So it'd be elliptical. And so it's like, I really wanted something to visualise what's actually going on with this. Because if you jump back to that polarisation controller, actually these things are really cool.

**Dave Jones:** The actual implementation of this, you usually achieve this in a lab. Dave, I don't know if you can do like a Google image search and throw a photo on top of that. I'll try. If you look at a polarisation controller, it's just you feed in a single mode optical fibre through coils.

**Dave Jones:** And because you're coiling it up and it's just stressing it a little bit, it's affecting the polarisation. So all you do, it's just a fibre going through a loop and then another loop and another loop. And it's stressing the fibre a little bit

**Dave Jones:** and affecting the polarisation the same way that the crystal does. And so all you do is you rotate the paddles around. It's just three paddles and you just go swivel, swivel, swivel. And you can turn any polarisation state into any other polarisation state.

**Dave Jones:** I've seen them. You can actually buy them and they physically rotate. They physically move. It's just ordinary fibre. Single mode optical fibre? Right. Any single mode fibre will do. Any single mode fibre that you stress, I believe, will do that. I don't think it has to be polarisation maintaining fibre or anything.

**Dave Jones:** I think it can't be polarisation maintaining fibre. Do you know the magic about what single mode fibre is? You're going to tell us. So if this... If I go over here, is that all right? Yeah. So these tiles over here, if this was a canal

**Dave Jones:** and we had waves coming along through there, because this canal is like really, really wide, it could support waves going this way, but it's wide enough that it could slightly support waves going that way. So you could have any pulse that came through here

**Dave Jones:** would kind of be reflected more than once. And there are multiple possible ways for the amplitude coming in to get to the amplitude coming out. But if you make the channel narrow enough, like this grating drain here, so that it's much smaller than the wavelength of light,

**Dave Jones:** it's not just hard, it's impossible for light waves to exist at that dimension. There are no modes that support oscillation. So the only way that this grating could possibly oscillate would be straight down the bore, meaning that single pulse in, single pulse out,

**Dave Jones:** and you get the minimum amount of broadening that you can possibly get compared to something much, much wider going on. And the advantage of multimode, though, is that you can send... is that you can make use of those different... You can do that with single mode as well.

**Dave Jones:** You can do that with single mode as well. You can send multiple wavelengths down there. The difference is how much each pulse, each perfectly narrow pulse will be smeared out. Remind me to tell you about Bragg gratings and fibre couplers and how they make them.

**Dave Jones:** And it's basically just doing terrible things to a fibre until the signal meter goes, whoop, whoop. And, yeah, just like heating the fibre up until two layers are kind of cross-coupling. And then it's like, yep, done that. All right, call that one done.

**Dave Jones:** Next one, put the next one in the rig, yeah. Back to the fibre controller. So the fibre controller is really cool because with three quarter-wave plates, three things that are doing a 90-degree rotation on this sphere, you can turn any input polarisation state

**Dave Jones:** into any other polarisation state. So if you wanted to turn diagonal into 67.2 degrees polarisation, you could do that quite easily just by manipulating those three paddles. I wanted a tangible model of that. So actually, first of all, this is what I made for the half-wave plate.

**Dave Jones:** So a half-wave plate is doing a 180 rotation on the sphere. And that's really useful because right-hand circular would convert to left-hand circular polarisation. So what this is, is our input coordinate frame. And you can see you've got vertical, horizontal, anti-diagonal, diagonal, right-hand circular.

**Dave Jones:** And this is the output one. And you can see that right-hand is always turned into left-hand. And depending on what angle you put the fast axis of your wave plate, you can just do whatever you like with the polarisation. So this is a tangible model of an actual half-wave plate

**Dave Jones:** you could get in a lab. And that's really cool, but I wanted to go a little bit beyond that and do any-to-any mapping and see if I could get something tangible that you could play with. There is a point to this in the end

**Dave Jones:** of what you're actually doing this all for. So let's just say that. I don't know if you want to later on. I'll show you the shutter thing and you can start with that. And then, yeah. So this is three quarter-wave plates joined together

**Dave Jones:** in a physical model. And basically, I just choose what I want my task to be, how I want to convert between these coordinate systems. Say I want to go, I want anti-diagonal to go to vertical. And I can just kind of turn it until that happens.

**Dave Jones:** And actually, I've switched right and left polarisation. So I'd have to play around with it a little bit more until. What can I do with that? That is great. With some judicious playing around, you can make anything happen. And so this is a model of using those three plates

**Dave Jones:** to do anything-to-anything. And I've actually. Are there any other physical models like this, like educational models? This is precisely why I made it. I wanted to make something that you could play with because it's like. Because otherwise, you're just moving three paddles around

**Dave Jones:** and it's totally unintuitive as to what's actually happening. Whereas this is, maybe it's not the easiest to work with, but it's actual, very tangible. And you can see what it physically means at each stage of the process. And I've actually done. I took a random task of turning polarisation

**Dave Jones:** into another polarisation on my website and manually manipulated it until I got it lined up as I wanted. Then noted the angles of the wave plates. Did the Muller calculus on that, which is like four by four matrix operations, multiplying three of them together,

**Dave Jones:** then putting a four vector in as the input and then looking at the output. And I got the right answer. I got like within a few percent of the right answer. So I'm super happy with that. For laser cut wood and hastily assembled,

**Dave Jones:** not quite 90 degree bent aluminium, that's not too bad. This is how they would have done it before computers came along. This is how you, this is how you did algebra, like algebra, like you draw. You didn't just, before you had digital computers,

**Dave Jones:** you didn't just pack up and go home. You had to do it. Yeah, you built or drew something to model it. This is totally different than my original idea. I originally had it as a linked thing that was more like a pan and tilt unit.

**Dave Jones:** And I realised that I had the arrangement backwards. So this is like 10 o'clock at night and I'm like, stuff it, just do simple stuff. And so I like laser cut really simple ones as examples and then just like hot glue them together

**Dave Jones:** and did enough of them that I was satisfied that this relationship with the gears should work. And then started, I'm like, because at 1030 at night, I'm not really thinking on cylinders. And it's like, all right, how can I trade off effort for thinking?

**Dave Jones:** And let's just laser cut it and hot glue it together until I'm sure that I'm not fooling myself what the result is. So that's, yeah. What is the end goal? So the end goal of all of these things that I've been playing around with is,

**Dave Jones:** following on from David's work with the polarisation cameras, I really wanna make a camera that will take a full picture of an image and for every pixel in that image, give a sphere breakdown of where it is. Because every pixel has a different story to tell

**Dave Jones:** about its polarisations and it's maybe it reflected off the table or maybe it's off the sky and the sky polarises light subtly differently. And is it strongly polarised? In which case it's right on the edge of the sphere. Is it weakly polarised? In which case it's much closer to the origin

**Dave Jones:** and the rotations don't really affect it that much. So there's all this information there which is kind of hidden in our just everyday view of things. And I really, really, really wanna get a camera that can just capture that and so I can actually start seeing that.

**Dave Jones:** And you think you can do it on an individual pixel level? Yes, absolutely, absolutely. By having movable filters and things like that and taking multiple images and then calculating to get back to the original states. As part of this, I built an optical table

**Dave Jones:** that can rotate filters around and characterise materials and I'm trying to bootstrap up from the ground up how much can I get without any known lab grade stuff? And I'm slowly getting there but an interesting thing has been I can figure out what vertical polarisation is

**Dave Jones:** and what horizontal polarisation is based on how light reflects off the surface of water or some known surface. But the difference between right hand circular and left hand circular is actually really, really hard because I need a wave plate that I know which axis is the fast axis

**Dave Jones:** and which axis is the slow axis. Otherwise, it's like if I have this on the sphere, what this does is completely different if the axis is lined up that way than if the axis is lined up that way. Right and left is gonna be completely symmetrical

**Dave Jones:** if I don't know which way it is. I can tell the difference but I don't know which one is truly right handed. In an absolute sense. In an absolute sense. So these things are, according to the Real 3D website and other places, the left lens is left circularly polarised

**Dave Jones:** and the right lens is right circularly polarised. That tells me everything right. No, because there's two conventions that are about equally popular of whether light is coming from the source or towards the observer as to whether it's the left or right according to that.

**Dave Jones:** So I still don't know. So I'm slowly building some stuff to figure that out and get my quest for left from right happening. And that's gonna rely on having, I've made some stuff out of, I've made my own ROM, Frenzel's ROM, which is how Mr Frenzel originally,

**Dave Jones:** Frenel, Frenel, originally converted it. The trouble is I've laser cut the acrylic and I've got it polished but I've introduced so much heat stress from the laser cutting that it's now completely birefringent and overwhelming. So I'm now trying to anneal the acrylic back to being optically perfect

**Dave Jones:** and that's an ongoing project. No, wouldn't you start the process again? No, no, no. I wouldn't, sorry. I wouldn't start from scratch because if I want to shape the, if I want to shape the acrylic with a laser, I'm gonna introduce stress or if I use a saw,

**Dave Jones:** I'm gonna introduce some stresses as well and heating up. And so what I need to do is make it the shape that I want and then anneal it back to being completely unstressed. And I've done some experiments and like heated it up to 90 degrees,

**Dave Jones:** which is just under glass transition temperature, held it for several hours and brought it back down at no more than 10 degrees per hour. And I've massively reduced the amount of stress but it's still not to zero yet. So I'm getting there. That's my quest for left from right

**Dave Jones:** via annealing acrylic. And yeah. That's great. Because I don't have any lab grade stuff that I can just look up the calibration sheet and go, oh, that's the fast axis and that's the slow axis. So yeah. Can you buy them? You can. You absolutely can.

**Dave Jones:** But at this point, it was like a challenge of how much can I, how can I do from first principles? Are there any animals out there that are sensitive to polarized light? Have they evolved? Is there any advantage to that? And so the mantis shrimp,

**Dave Jones:** I believe, can see in circularly polarized light. There's a bunch of other underwater ones. A cuttlefish, I think, can also do it. A lot of beetles have carapaces on the back of the beetle that are preferentially right circularly polarized instead of left. And they think it's like a signal

**Dave Jones:** to the same species to not. So if my playing around with the acrylic and the ROM and stuff didn't work, my backup plan was to go to the museum with the glasses and look at beetles and figure out whether the beetle was brighter in this eye or in this eye.

**Dave Jones:** So beetles as an ISO standard calibration object. The ISO beetle. All right. Thank you very much, Gav. That's hugely fascinating. Good luck with the project. Maybe we can do a follow-up. Yeah, yeah. I'll show you the optical table at some stage. Awesome. Because that'll be open source

**Dave Jones:** for CNC-controlled filter rotators. Fantastic. Thanks, Gav.
