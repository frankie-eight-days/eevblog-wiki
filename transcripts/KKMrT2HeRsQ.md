---
video_id: KKMrT2HeRsQ
title: EEVblog 1589 - CCD Scanner Array
url: https://www.youtube.com/watch?v=KKMrT2HeRsQ
source: youtube-asr
---

**Dave Jones:** Hi, just a quick follow-up video to my facts teardown, the dumpster facts I got. I forgot to I was going to include this in the video, I completely forgot. So, here's a separate video looking at the linear scan head inside this

**Dave Jones:** fax machine um scanner copier. Now, this is interesting. The scanner head, this is module in here, and I noticed a little drop-down latch there. So, if you push it push it like that, it drops out. Isn't that neat? There you go. So, there's the

**Dave Jones:** there's the sensor head. That's just it comes out nicely, and it's got an illumination array in there, and and the actual linear scan head itself. So, oh, we could have a look at that under the microscope. Now, this is only a monochrome unit, so

**Dave Jones:** this is not a color. I don't know how many gray scales it's got effect effectively. Um but let's let's have a look at how this head works, cuz it normally like it sits like that just had a couple of glue

**Dave Jones:** points there, which I've broken, and it's basically got a bit of glass on top. Okay? It's got I'll show you inside better in a minute, because you can't see often see through the glass there, but you can see that

**Dave Jones:** there's some sort of array in there, okay? And there's some sort of like you know, larger sections, and that would be to the let the light through. So, if we actually flip this PCB off like this, you can see

**Dave Jones:** that we've got two parts to it well, essentially three parts to this. One is these little channel things, right? They actually go down, and they've got a window, which then goes down onto the paper. Cuz when you're scanning, of course, it's you know, it's

**Dave Jones:** completely dark in there, so you've got to illuminate the page, and you've got to do it, you know, consistently right across the board. Illumination is um like 90% of it, really. Um if you don't get the illumination right, you're going to

**Dave Jones:** screw it up. So, what they're doing, as you can see down here, they've got little LEDs down there, little LEDs. A lot of people complain when I call it LED. Here in Australia, it's LED. It's not LED. When I was a boy. Anyway, um yeah, so

**Dave Jones:** let's let's let's take a look at the PCB down here first. Okay, so you can see uh So, I've got my Tagarno microscope here. We've got 40 times magnification, but we will go under the better Olympus microscope later. And you

**Dave Jones:** can see that is a little LED there. So, LEDs spaced at um various intervals, and they would simply light up through these uh channels here, and then light up the page through that. So, they're just all in series there, are they? Just like a

**Dave Jones:** regular LED strip uh kind of thing. They've probably got a constant you know, maybe a constant current driver there, something like that. So, that's the connector there. So, that's driving all that. And then, we've got whatever that is. I don't know

**Dave Jones:** what that is. Maybe that's a light sensor? Perhaps? I don't know. I don't know. If you know what that is, leave it in the comments down below, cuz I can't see any like, you know, there it is there. Does it actually like

**Dave Jones:** can't see how it connects or anything. So, I'm not sure what's doing there. That's not That's not the sensing array. The sensing array is, of course, all of these little tiny bits down here. You can see them, and

**Dave Jones:** I'll show you under to microscope at the in a minute, but that's obviously the pitch between those will be the resolution of this thing. So, this is a line sensor array, of course. Um so, it's a CCD sensor array, and it's got

**Dave Jones:** like one line. So, it might have I don't know, 4,000 of these little sensing CCD elements here, 4,000 of them by one. So, even though it looks like it might have maybe two, one above the other, um that's not that's not how it's going to

**Dave Jones:** work. There's just going to be a sensing element there, and then you can see circuitry on the uh silicon above that. So, if we get it out, it's all about exposure, really. There we go. If I turn that down, yeah,

**Dave Jones:** so we can see the bond wires going over to the various pads and whatnot. That's interesting, huh? And it looks like they've got the lucky major groups. It looks like cuz you can kind of sort of see that they're split

**Dave Jones:** there. There seems to be like some split in it. So, it looks like it's coupled I don't know if that's like cuz they would like they would shift these out, of course. They would they would have like there'll be one big latch line that goes

**Dave Jones:** latch all of them all at once. And then uh either shift them all out, and then the stepper motor, of course, moves the head across a tiny one uh pixel forward, and then latch, scan the entire array, shift it out, shift the data out. And I

**Dave Jones:** don't know, it might be 8-bits per pixel or something like that. So, you know, there's a fair bit of data. Multiply that by however many pixels, you know, however many thousands of pixels across. There's a lot of data that has to be

**Dave Jones:** shifted out quite quick from this linear scan head here. And yeah, and so, they only need one pixel wide, and then of course, that's why the scan head goes across the And if you've ever tried to stick your head in there when when it's

**Dave Jones:** doing it, um it's really bright. And it it just scans across, and yeah, so it's got that little stepper motor that goes step step step step. Although, it does it so fast that it appears as low as like a a really uh smooth sweep across,

**Dave Jones:** but it's actually a essentially a stepper motor in there that just steps at once and then boop. Um and reads out all the data. So, that's really cool. Huh? So, there you go. So, that's the array head. So, yeah, I don't know what that's

**Dave Jones:** doing. I I Yeah, I'm going to presume maybe and like a light sensor or something. Now, this is interesting. This they've got these things here. And these look like LEDs, right? They look like LEDs, but there's not, right? There's nothing connecting

**Dave Jones:** these at all, right? There's no electrical connection to these. They They just sit in there. So, they I guess they appear to be some sort of like lens kind of thing, but the pitch of those doesn't match up with the massively fine

**Dave Jones:** pitch that's along the actual silicon sensor head there, right? That's embedded on the die there. I mean, you know, you can't It's hard to see there. Like it's, you know, well over an order of magnitude difference in the pitch

**Dave Jones:** between, you know, these and between the array elements and those um lenses up there. So, they're not They're not LEDs. So, yeah, I these don't seem to be LEDs, right? Because these ones out here they're your LEDs, right? The little bond wires go

**Dave Jones:** into them. So, yeah, I'm not sure how that's actually working. There, I don't know. If you got any thoughts, leave it in the comments down below, but you can see by the yellow there that it's actually these are

**Dave Jones:** actually um see-through. They're little see-through like windows, lenses, something like that. And the reason that they're yellow is cuz I've got a yellow Post-it note under it. Trust me, I can I can see through that. If I take away

**Dave Jones:** the post-it note, yeah, there you know, you can actually see through them. So, that is rather interesting. They're like little little bubble lenses at a way greater pitch than the sensing array. There There we go. You can see that.

**Dave Jones:** Interesting, huh? So, don't quite know how that works. And they do actually line up. So, these LEDs down here, these are these are going to line up with these big channels down here. Okay, so obviously those LEDs just like

**Dave Jones:** you know, flood fill light in there and then it just goes on the angled plastic and then it lights up the paper through the bottom like that. And then it looks like the sensor array actually does sort of like flip up over

**Dave Jones:** onto that bubble lens array. So, eh, it's interesting. I would have thought that that would distort it in some way. Yeah, I don't know my optics. Maybe they Maybe they do that for some sort of like optical reason. Like I I

**Dave Jones:** couldn't even pull out the words off the couldn't even pull out some wank words off the top of my head. But, you know, refraction and all sorts of you know, optical type things. Optical's not my field. So, I can't even pull out some

**Dave Jones:** wank words there. But, you know what I mean, hopefully. So, but but that's interesting. Is it not? Um, that they have just sort of like an array. I don't know if they're curved or what cuz they're actually embedded. Can I

**Dave Jones:** actually get that out? Hold on to your hat. I got the plastic out. Now, it's not going to fall out. But, I would have thought that would distort the image. And that seems to be the only way that light's getting through to the

**Dave Jones:** sensor. So, that's interesting. So, it must you know, some more patenting or you know, something something like that. Perhaps. Oh, look at that. Got it. Here you go. So, we've got the glass plate. And then we got that. It's

**Dave Jones:** quite thick, isn't it? Look. Okay. So, it's kind of like an optical zebra strip. If that's like for want of a better word. That's how I would describe it, like an optical zebra strip. And they're like staggered there. Yeah, if you know

**Dave Jones:** the name for that, I'm going to call that like an optical zebra strip. Because that that is fascinating. And that's really thick. That's like 5 mm thick. And it's just like like light pipes. Just like staggered light pipes like

**Dave Jones:** that. But the sensor array is like an order of magnitude greater pitch than that. So, I would have thought, you know, the little breaks in there would have like distorted your image or something, but I don't know. Please, optical experts,

**Dave Jones:** leave it in the comments down below. A huge 5-mm optical zebra strip light pipey thing. And that's the lens array that goes over your optical sensor strip like that. So, once again, once So, that kind of lines up for those

**Dave Jones:** being some sort of light sensor, perhaps. Just a, you know, uh just to detect that the light's there and it's all even and I don't know, maybe it can do some calibration adjustment for based on the light output

**Dave Jones:** or something like that, perhaps, for each individual section. But you'd have to do it on like a whole section basis, cuz it looks like they only I know, they've probably got two. They're It's an odd pitch. They don't seem to have

**Dave Jones:** two of those per thing over here. So, I don't I don't know. Not quite sure what's going on there. Anyway, let's go over the microscope and uh see if we can see down at the individual um sensor and silicon uh circuitry level.

**Dave Jones:** And if I get that array under my Olympus microscope here, you can actually see that they're all they're all absolutely identical, these individual uh this is 400 times mag, I I think. Yes, I think I've got that right. Uh

**Dave Jones:** and you can see that they're all identical. There's no There's no filter. It doesn't appear to be any sort of filter on any of them. Sorry, my stage is a bit how you doing here. There you go. If you

**Dave Jones:** want to decode that, knock yourself out. They look absolutely identical. But there you go. Um so, the difference between the the pitch between those is going to be the resolution of the uh scanner. Obviously. So, it's a you know, however

**Dave Jones:** many pixels wide by one pixel in this particular case. That's the actual That's the actual sensing element. I can take it back to 200 times. Yeah, so there's a bond wire up the top there, for example. And got some extra circuitry up the top,

**Dave Jones:** whatever that's doing. Scroll across there. Yeah, you can see one of the bond wires. So, nothing else doing there. Take that back to 100 times. There you go. 200 and 400 times mag. Slightly off there. It's not the world's best microscope,

**Dave Jones:** although it is quite capable. So, it's interesting that There looks like there's a little array just above the the sensing element there. There looks like there's a little array. Is that some sort of like buffer array or something like that? I I don't know. If

**Dave Jones:** you know your semiconductor layout, um please leave it in the comments down below. So, that's interesting, is it not? Um yeah, there doesn't uh seem to be any extra, uh, you know, filter or anything over the top of those elements, which makes

**Dave Jones:** sense. They're just relying on all the external, uh, parts of that. This is just a linear sensor array, and how many, like, levels that's got, how many bits, um, I don't know. How many, uh, gray scales, essentially, cuz this is

**Dave Jones:** not a color sensor, so you don't see any There's no RGB array. If this was a color sensor, you'd probably have three separate elements in there, each with its own RGB filter over the uh, top. You'd have like three in a line or three

**Dave Jones:** next to each other, or however it, uh, works. But, of course, this is a fax machine. This is not a full-on color copier, so this is a, uh, just a monochrome, uh, laser printer and fax, uh, machine and scanner, so it's not

**Dave Jones:** going to, um, scan in color. So, that's why we get an array and we don't see any, uh, filter elements at all. But, anyway, that's that's really cool, huh? So, if you like that, give it a big thumbs up. As always, discuss down

**Dave Jones:** below. Catch you next time.
