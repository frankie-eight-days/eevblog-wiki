---
video_id: KMHnkjWP1yU
title: Remove Green Screen Background using GIMP
url: https://www.youtube.com/watch?v=KMHnkjWP1yU
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 62, "3": 91, "4": 121, "5": 150, "6": 179, "7": 199, "8": 231, "9": 263, "10": 281, "11": 293, "12": 320, "13": 333}
---

**Dave Jones:** Hi, I'm just going to show you how to remove a green screen background, which is what I've got here. This is how I'm doing this video, a green screen background from an image using so that you can create a transparent PNG file that you can then overlay and in my particular case use as a thumbnail. So, let's go because it's not at all obvious how to do this in Yeah, yeah, I know Photoshop. I don't have an Adobe account. I don't use Photoshop. So, I'm using So,

**Dave Jones:** let's drag in an image which I want to remove the green screen background of. This is me doing a big loser pose here. So, I actually So, how do we remove this green screen background? Right, first step is to go in here and right click on the image here and you've got to add an alpha channel. If you don't, then you don't have the transparency layer that you need and you'll just get like a white screen background. So, or whatever the background color happens to be. So,

**Dave Jones:** we've added our add alpha channel down here. Then, we want to go up to here and we want to use what's called the fuzzy select tool and select by color. So, we right click on that to give us the option select by color like this. And now, this is actually an interesting image because we're trying to remove the green screen and you can see how it's not very it's not perfectly evenly lit, okay? So, it's it's probably not going to do it in the one hit. And also, we've

**Dave Jones:** got a green PCB in here, which makes it a bit trickier. Now, if the green PCB actually really matched the green background, we'd have a bit of trouble and we'd probably have to use some different methods to certainly have to use different methods to do that. But anyway, we want to set the threshold down here. Now, I'll show you if I set the threshold to say 30 like this. This is the detection threshold where it detects the color. Now, what we do is we simply click on the background here,

**Dave Jones:** okay, and it's selected. You can see how it's selected my outline reasonably well, okay, cuz there's a decent contrast in there, but it's got all this crap up here like this, and it's got all crap down here like this, and it didn't quite get inside here like this. So, and you can see that it's actually selected some of the PCB as well. So, you don't want that PCB uh that green PCB to or what green object, whatever it is, um to be included in that threshold. So, 30 is

**Dave Jones:** a bit high. So, let's drop it down to 20 threshold, and let's do that again. So, we just uh left click in here, okay, and you'll notice how it now hasn't selected any of the PCB in here. So, you know we've got the right threshold. Now, what we do now, because we couldn't can't just get rid of it like this, it'll be crap. If we just go hit delete key like that, we're left with like just like half and half pizza here, right? That's no good whatsoever. So, we have to hold

**Dave Jones:** down shift, and then click in here, and we can get more of the even color. So, it just adds that, and up where around here, just shift click again, and it's got rid of that. Shift click again, and keep shift left clicking until all of it's gone away. And does that look pretty good?

**Dave Jones:** Now, uh the problem is we can't go too low on the threshold here, otherwise we'll end up with a a green fuzz. So, you notice that we have actually some green around there left. And the thickness of that will be dependent upon the threshold. So, if we didn't if we went too low there, it would just get thicker and thicker and thicker green outlines. So, a threshold in 20 in this particular case is a reasonable compromise between getting like a green little tinge around the outside of your

**Dave Jones:** image, and not selecting this green PCB in here. So, yeah, anyway, so that looks pretty good to me. So, all we're going to do is hit the delete key now, and bingo, we've removed our background. And you know you've got the alpha channel, the transparent background, cuz you end up with this checkered pattern like this. And then all we want to do is go export as, and then PNG image, export like that. And then we'll just leave those as default. You can muck around with those if you want. But we've

**Dave Jones:** exported that, and now I'll actually show you how I'm going to include this. Now, I'm inside of Vegas, which is my video editing tool. This is where I'm going to use the image, but you can use it however you like. I've dragged it in here, so we've got you can see we've got the checkered background.

**Dave Jones:** So, it's the transparent overlay, and bingo, you can see that I just dragged that over, and I could just save that as a thumbnail if I want that to be the thumbnail. You know, if I want this to be the thumbnail, it it doesn't matter.

**Dave Jones:** I can like export that as the image for whatever I want. So, there you go, I can overlay it like that, and you can see the green tinge now. You can see the green tinge outline. So, yeah, it's it's a bit of a trade-off there, but anyway, there you go. That is how you remove a green screen background in And it's easy when you have one It doesn't have to be green. It can just be any one consistent It can be a white wall, whatever it is, but then of course, you

**Dave Jones:** know, my pasty white skin would be a problem, etc. So, it just has to be a different color to whatever it is that you know, your foreground image. So, don't wear a green shirt. Anyway, found that useful, give it a big thumbs up.

**Dave Jones:** Catch you next time.
