---
video_id: YhXueY3FW6s
title: EEVblog #524 - Vignetting on a Cathode Ray Tube
url: https://www.youtube.com/watch?v=YhXueY3FW6s
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 53, "4": 70, "5": 86, "6": 102, "7": 119, "8": 143, "9": 159, "10": 171, "11": 191, "12": 208, "13": 228, "14": 248, "15": 264, "16": 280, "17": 292, "18": 308, "19": 325, "20": 345, "21": 361, "22": 377, "23": 397, "24": 413, "25": 434, "26": 450, "27": 474, "28": 494, "29": 515, "30": 535, "31": 551, "32": 567, "33": 583, "34": 595, "35": 615, "36": 631, "37": 648, "38": 664, "39": 680, "40": 696, "41": 712, "42": 729, "43": 745, "44": 761, "45": 777, "46": 798, "47": 814, "48": 830, "49": 850, "50": 866, "51": 878, "52": 899, "53": 919, "54": 931, "55": 955, "56": 976, "57": 992, "58": 1008}
---

**Dave Jones:** Hi, just a quick follow-up video on this classic Hewlett-Packard 35660A dynamic signal analyzer, or FFT analyzer, as they're known in the trade. And if you haven't watched the previous repair video of this, it'll be linked in down below, so please watch that first.

**Dave Jones:** Now, one thing that was noted in the previous video is we've got rounding on the CRT display here. Look at these dark round patches on there like that. And anyone in the photography or video industry will know that as a Vignetting effect around the outside.

**Dave Jones:** Now, what is causing this? Now, you know, there were quite a few people who said, oh, there's a, you know, a circular mask on the front of the CRT like that, and that's what's causing it. You've got to shrink the display and all that

**Dave Jones:** sort of stuff. Well, no, that's not the case. Trust me, this is the proper size for the screen. I've used it before. It is actually a rectangular front. It's nothing to do with any sort of circular masking there whatsoever. But the reason for this is very

**Dave Jones:** obvious, but to understand it, I think we should go to the whiteboard. But just a quick little note on why you might see this screen pulse in a little bit, the variation in the brightness. Well, that's to do with the update, the scan update rate

**Dave Jones:** of this ancient CRT display. And my camera, my camera is currently shooting this at 25 frames per second. Alright, I've set the camera to now 1 12th of a second, so 12 updates per second, and you'll notice we don't get the flicker anymore, but look at that.

**Dave Jones:** You don't, you get blurring in my hand as I move it around. That's because well, you know, we're only updating that 12 times per second. I can set it as low as 6. I'm using manual shutter priority here. And that's 1 6th of a second.

**Dave Jones:** And you'll notice, of course, no more flickering, of course, because we get that persistence of vision update, but this is really slow. And this is the maximum shutter speed of 1,200 times per second, and look at that. I mean, you know, it's going to be really weird in a minute now, but sorry for anyone

**Dave Jones:** having epileptic fits or something. Should have put a warning on the video. Anyway, I just thought I'd throw that in there, because that's interesting to know. If you're ever shooting video of any CRT displays, be they television, old computer, you know, retro computer monitors, or something like that,

**Dave Jones:** you've got to use, if you don't want that flicker to show up, it could be it depends on the rate of course, you might just get lucky, but generally you want a camera with shutter priority mode. And here we go. How a CRT works.

**Dave Jones:** And this is probably almost very familiar to most of you, I'm sure, but we'll just go through it. Now, as you know, CRT screen, it's an evacuated tube like this. In this case, it's not a round tube on the front. A lot of the old oscilloscopes back in the old days, yes, they actually used to be round front

**Dave Jones:** tubes on them. If you've seen those real ancient valve-based crows, cathode ray oscilloscopes. Well, this one's not, of course, as you saw, it's like a square front on it, but then it tapers off into a round neck. This is the neck part of the tube down in here.

**Dave Jones:** And basically, how a CRT works, it's got a heater in here, it heats up the cathode, which generates electrons, which are then accelerated in a beam via the high voltage anode here, and that's that little strange plug you see attached to the side of the CRT, and it's often, as you

**Dave Jones:** saw inside the DSA, it's got a protective shield over the wiring. That's the real high voltage stuff. You know, that's the 5, 10, 15, 20 kilovolts stuff. You know, so you really don't want to be touching that, but then that inside generates the potential difference between the cathode and the anode to accelerate the electrons

**Dave Jones:** as a beam via this, and then we have a focusing coil here. In this case, it's an electronic focusing coil. It allows you to adjust, as it says, the focus of the beam, the narrowness of the beam in there. And if you, and if that's all you had,

**Dave Jones:** then you would see a very bright dot right in the centre of the screen on the front. And of course the front of the screen inside has a phosphor coating. This is only a mono CRT. I won't, of course, go into colour, which is different, well, it's

**Dave Jones:** similar. It's got three different beams. Well, let's not go there. It gets a bit complicated. Let's stick with the mono one. So, if that's all we had, the heater, the cathode, the anode, the high voltage potential difference, the phosphor on the front, and the

**Dave Jones:** even without a focusing coil, you'd still get a dot on the front of the screen there. But of course, what we need to form a raster image like this with a horizontal scan like this. As you know, a CRT is scanned in lines,

**Dave Jones:** horizontal and then a vertical number of lines like that. This DSA works no different whatsoever. It's scanning like that. And the way they do that is with deflection coils, because this electron beam can be deflected with a magnetic field. And that's all they have.

**Dave Jones:** They have four coils here. Please excuse the crudity of my 3D model here. I'm not very good at drawing this sort of stuff, but anyway, it'll do. Basically we have wide deflection plates on the top and bottom, or deflection plates, deflection coils. They're implemented as coils inside the unit, as you'll

**Dave Jones:** actually see. But they've got one on the top and bottom, and one on the side for the X. So when you energize the X coils here, you can make the beam sweep across the front of the CRT like that. And likewise with Y, you can select which line

**Dave Jones:** you want, and of course you can turn the beam off and on very quickly. So you can actually generate individual dots, and then you can build up a dot matrix rastered screen like that. So that's all there is to it. Pretty simple. But what's causing the vignetting on the screen?

**Dave Jones:** As you saw, we were getting dark patches, dark corners on the screen like it was some circular, you know, like there was some circular mask on the front of the screen. And what is the only circular thing inside this thing? It's not the front of the screen,

**Dave Jones:** because it's like rectangular. It's the neck here. The neck is circular. So what we've got, if these are, now I've got a side view of the CRT, and if these are the deflection coils here, the X and Y, the Y is on top

**Dave Jones:** there, and the X is on this side and the far side there. Now normally this deflection coil is pushed right up against the neck of the CRT here. So let's actually draw that as if that was the case. Okay? If it was like that, please excuse the

**Dave Jones:** crudity of that, it's right up against the neck like that. And of course, this is the point where the electron beam actually bends. So if we've got our electron beam coming through here like this, it's at this point that it's going to bend like that and

**Dave Jones:** go up and hit the screen up here, like this. And if it's right up against the neck, then there's nothing in the way to display the full screen of this thing like this. But if this deflection system is moved backwards along the neck like that, which will represent, which

**Dave Jones:** we can show you right now, like this, let's say it's like that, if it's moved back along there, then what happens? The beam comes through here and then it tries to bend too early, and it hits some of it, the outer part of it hits

**Dave Jones:** the corners like that, and what does that turn into on the front of the screen? If this is the front of the screen like this, you get an image that is, you know, perfect in the center but then has these rounded corners on them because it is getting, the beam

**Dave Jones:** is hitting the internal edge of the CRT there. So you're getting these rounded corners. And that's what's happening here. The deflection coils are too far back on the neck like that. Very simple. There's no real other explanation for it. So yesterday when I was doing

**Dave Jones:** the preliminary repair on the scope, I did actually push that forward because that's the obvious reason for it, but it didn't budge. So, and I couldn't because it had all the shielding all over the CRT, I couldn't see that it was directly up against the neck, and I thought it was, but obviously

**Dave Jones:** it's too far back on the neck. I've gotta use more force, use a bigger hammer, get a bit medieval, and give this thing a bit of percussive maintenance. And there's lots more advanced stuff which goes into these CRTs as well. You saw those little permanent, those four little permanent

**Dave Jones:** magnets sort of, you know, arranged in various locations. There's various techniques, there's various patterns on that sort of thing for actually optimizing the screen, the roundness of the screen, and the geometry of the image and all that sort of stuff. Bit of black magic goes into that.

**Dave Jones:** But we won't try and explain that today because we don't have the full info. And yes, as it turns out, I just applied a bit more force on this thing and I was able to move it back in there. So that looks like it's the issue.

**Dave Jones:** Now that looks pretty much that feels like it's now all the way in. To really see that, I'd have to take the metal shield off, which I don't particularly want to do, but I believe that really feels like it's in there now. So there was just something

**Dave Jones:** maybe stuck on the side of that, which meant that when I pushed it forward in the previous video, I thought it was in, but it wasn't. So I'm absolutely certain that's what was causing the vignetting that we saw on the front of the

**Dave Jones:** CRT in there. But we can actually play around with that and experiment and see that we'll get, as we move this entire deflection assembly back and forth, we'll be able to see that we can change the amount of vignetting on the front of the CRT.

**Dave Jones:** And of course we can rotate this entire assembly as well, which then gave us the rotation issue which we got before, but yeah, basically we just want to move it back and forth on that neck, and we should be able to see this.

**Dave Jones:** And by the way, yes, this is all powered off, and it is safe, once it's all powered off and discharged, then to go in there and sort of, you know, play with this assembly. But you don't want to be dicking around with this when the thing's live, that's for sure.

**Dave Jones:** Unless you absolutely know what you're doing. Anyway, what we've got here is our 4 wires. They're our deflection coil assembly, one for the X, one for the Y coil up in there, which it goes through all the bobbin. I won't, I don't know, I might take this shield off

**Dave Jones:** maybe if it's relatively easy. But you'll notice that there was no focusing coil which we saw on there. There actually is, but it's inside. And it's coming up, you can see the focus pot down here, there's the focus pot, and it looks like we've got the focus wires coming up down into the

**Dave Jones:** neck board here, and then they've got extra pins on there which then go through, so they're going to have the focus coil on the inside of the tube instead of on the outside, like we showed simplistically on the whiteboard. And bingo! As we expected, once we pushed

**Dave Jones:** that deflection coil all the way forward, right at the base of the neck, ta-da! There's our test pattern, no problems whatsoever. Beauty. Let's see if we can make it come back. I've just moved it a tad back here, I think the rotation's slightly off, so we might see a little bit of rotation there,

**Dave Jones:** but let's have a go. And there we go, it wasn't quite as far back as what it was originally, and you can see it just starting to appear on the corners there, because that electron beam is hitting the inside of that CRT tube

**Dave Jones:** there. Bingo! Fixed! I'll just push that back and screw that back into place, and Bob's your uncle. And by the way, this front panel mesh here, as several people pointed out, is actually a screening mesh to stop any of the CRT scanning frequencies escaping from this thing.

**Dave Jones:** And as we saw in the previous video, the shielding on this system, the way they've designed the shielding is absolutely incredible. Belt and braces stuff, because this is a really, you know, precision bit of kit down in the low frequency range. So the scan frequency of this CRT,

**Dave Jones:** you know, however many tens of kilohertz it is, it's going to be in that range, is smack in the middle of the DC to 100 kilohertz measurement range of this thing. So you're really, you know, that's a really vital part of getting, you know, the noise floor and the

**Dave Jones:** performance out of this instrument. Now you may actually be wondering, well, where is the ground connection for this metal mesh screen? By the way, it's just like your microwave oven, for example, except that's stopping 2.45 gigahertz. This one's stopping low frequency stuff. But to do that, it's got to be grounded in some way.

**Dave Jones:** And there's no grounding connection on there, really. But this the plastic, what you might think is a plastic front panel in here, it's not. Check it out. Nickel screened. Look at that. They have got, it's all conductive. So, and of course, this goes back

**Dave Jones:** to this metal tab which is connected onto the chassis, and everything's just fine. So they've really gone to town on the shielding of this thing. But not surprising considering the precision instrument that it is. It's really designed for low noise, low signal level, and they just can't tolerate any

**Dave Jones:** lack of shielding whatsoever. So of course they just went completely belt and braces on the thing. Nickel screened all the plastic in the front, the shielding on the CRT which keeps it out, all the, you know, triple screening in here, all of the design of the chassis.

**Dave Jones:** This ridiculous, you know, like just even the front, the gold on the front plate there, and the shielding, huge shielding box on the input and source terminals. Then they've got the shielding inside these individual cans, and then they'd be shielded again, and they're probably using

**Dave Jones:** screened reed relays in there for the switching, and oh, goodness. Woo! Talking about shielding the lily, but that's what you get in a high performance, high priced instrument like this. And can we actually measure that noise? Oh, you bet we can. All you need is a scope probe, put it up

**Dave Jones:** to the front there, and just the pickup on the probe is enough to get the noise there. And if you take that off you don't get nearly as much, because you've got some extended metal in there acting as an antenna. But there you go, that's a rather effective antenna.

**Dave Jones:** We've got the vertical rate here, 56.1 hertz. There it is. So that's our vertical scan, and then if we zoom in on the scope, you'll notice this higher frequency stuff. And that there is about 4 divisions there, and we're 10 microseconds per division, 40 microseconds,

**Dave Jones:** that's 25 kilohertz. That's the horizontal scan rate. So there you go. We can easily pick up that. And in a high precision measurement environment, which these DSAs are specifically designed for, that sort of noise can really kill you. And of course we can make that go away with the magic

**Dave Jones:** screen inside here. So here's our probe, there it is. It's picking up all that junk. You put this in front of it, and the tabs on there are connecting through to the metal case on the back, which is actually screened, as you can see, very, well, it's

**Dave Jones:** probably there, but it's probably going to be very low. It's going to be very effective. Look at that! Ah, yeah, I can't even get that. That's just other crap in the air. Bloody ripper! What a bobby dazzler, this one. Really like it. Hope you liked the video.

**Dave Jones:** Catch you next time.
