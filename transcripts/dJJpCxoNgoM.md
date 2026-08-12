---
video_id: dJJpCxoNgoM
title: My Automated Handbrake Video Conversion Batch File Script
url: https://www.youtube.com/watch?v=dJJpCxoNgoM
source: youtube-asr
timestamps: {"0": 0, "1": 30, "2": 39, "3": 60, "4": 83, "5": 112, "6": 123, "7": 139, "8": 152, "9": 164, "10": 187, "11": 204, "12": 218, "13": 232, "14": 239, "15": 256, "16": 263, "17": 281, "18": 295, "19": 308, "20": 323, "21": 331, "22": 342, "23": 357, "24": 371, "25": 390, "26": 403, "27": 416, "28": 428, "29": 444, "30": 462, "31": 472, "32": 484, "33": 495, "34": 509, "35": 518, "36": 530, "37": 540, "38": 555, "39": 563, "40": 574, "41": 585, "42": 601, "43": 613, "44": 627, "45": 636, "46": 648, "47": 664, "48": 676, "49": 691, "50": 704, "51": 719, "52": 732, "53": 744, "54": 765, "55": 777, "56": 791, "57": 800, "58": 817, "59": 828, "60": 855, "61": 865, "62": 881, "63": 891, "64": 903, "65": 917, "66": 930, "67": 941, "68": 949, "69": 958}
---

**Dave Jones:** Hi, I just want to do show you my transcoding process with HandBrake cuz I'm actually in the middle at the moment. I'm on my to go on a microscope streaming machine here and I've put in my old Nvidia RTX 2060 card into here and what I'm doing is I'm leaving this machine actually running now transcoding all of my original video files or not all of them cuz I

**Dave Jones:** The thing is I've been saving every single video that comes out of my camera every single raw file the raw video files I have saved those ever since video number one, right?

**Dave Jones:** So we're talking a lot of videos. Now in more recent years, of course, I've switched over to 4K video for a lot for a lot of my videos for teardowns for example, always shoot them in 4K, but even the 1080p stuff is like quite high bit rate stuff coming out of the camera and the raw files.

**Dave Jones:** Now probably for the last 6 months. I don't know how many videos. I don't know exactly when I change, but I've been transcoding them before I edit them, but that's only for the more recent videos for all of the all of my backlog of all all my videos I have edited the raw video files and I've kept those raw video files, but now the high bit rate

**Dave Jones:** stuff the 4K I'm ready to actually clear off my NAS drive and actually archive another group of videos. I've got you know, like 500 maybe 500 videos or something last 500 or so I'm looking to archive those onto hard drives and get them off my NAS and my NAS is backed up to an online cloud storage thing as well, but you know, I want to like periodically once I get

**Dave Jones:** enough of them. I like to fill them up dedicated hard drives to get two different hard drives two different hard drives of two different brands, and I duplicate the contents on there and then I erase them from my network array storage.

**Dave Jones:** Now, this is different to the the actual rendered files which I upload to YouTube. I keep those as well, but they're quite a lot smaller than what the all the raw original files are.

**Dave Jones:** So, they're not a file storage problem. So, you can see here that I'm actually running HandBrake script. So, I'm you can see here I'm transcoding this is a 1080p file here.

**Dave Jones:** And can I No, I can't highlight. Oh, yeah. Yeah, I can highlight that. See? So, this is a So, this is the output geometry. So, the input geometry here, this is my Apollo 50th video that it just happens to be running at the moment.

**Dave Jones:** That's 24 megabit bit rate, 8-bit H.264, and that's 60 frames per second there. And and I'm transcoding that basically the H.265. So, yeah, there it is there. H.265. I'm using the GPU, the NVEnc, and with a constant quality factor of 26.

**Dave Jones:** So, I find 26 is pretty much ideal for 4K, and it's it's more than good enough for 1080p content as well. Although, really I could do say 20 usually do about 23 constant quality factor for 1080p content.

**Dave Jones:** But, in this particular case, this is just storage of the old video raw video files. Constant quality factor of 26 is more than good enough. So, yeah, I'm I've got this script, and I'll show you the script in a minute.

**Dave Jones:** So, I'm busily transcoding like 8,000 video files or something like that. I'm doing it in batch of batches of 100 videos. And let me actually go Yeah, so I've actually got You can see up here on this on my desktop here.

**Dave Jones:** Yeah, you can see this. I've got a batch file. And this is how, like a Windows uh DOS batch file, all right? So, this is how I uh transcode my card.

**Dave Jones:** As soon as I shoot a video, I take the um the clips file from that card, and I just drag and drop it onto my batch file here. And then in the process and hand I've written a script that HandBrake then just uh goes in the background and and does all this uh transcoding.

**Dave Jones:** And now I've got this set up so that on this machine here, which I can just leave running for days and days and days, it'll transcode all my files for me.

**Dave Jones:** Uh this is my NAS uh drive here, and you can see that these are all These are all my raw videos, right? These are Look, right? I I Last time I did it was So, my last hard drive backup was 1175, video number 1175.

**Dave Jones:** But 1176 onwards, right through 1176, right? Right through right through right through What am I up to? 1560 something at the moment, right? So, I've got to do all the I've got to do all these files, right?

**Dave Jones:** 1460 60 I'm getting there. And custom LCD design, quantum computer, you haven't seen that one yet. And uh yeah, so I'm now I'm saving those to my local C drive here.

**Dave Jones:** And you can see video temp, and I've done uh 1200. It's in the middle of For some reason, it's not doing them in alphabetical order. It's got 1230, and then it jumps to 1288, but it's going to do them all.

**Dave Jones:** And you can see that HandBrake is doing about 330 frames per second. It's usually about 360 370 frames per second. Maybe it's cuz I'm screen capturing uh at the moment.

**Dave Jones:** So, that's uh taking some resources here. But um Oh, why is that not Why is it stopped? Oh, cuz I interacted Oh, I physically clicked on it, so I stopped it.

**Dave Jones:** Uh oops. There you go. I didn't know that. It paused. Anyway, um yeah, so I'm transcoding all these files. So, what it does is the script's smart. It actually takes all of It knows the subdirectories, and it does all the videos in the subdirectory.

**Dave Jones:** So, I can see uh roughly I'm getting about a 70% reduction. So, it's reducing my file size by about a third. So, let's take um for example, let's take this uh What is it?

**Dave Jones:** Um D cell battery scam 1200, right? That is uh What is it? Um two two gig. There you go. So, but if we go up to here, my original raw 1200, let's go up to 1200.

**Dave Jones:** Da da da da da da And where is it? 1200 D cell battery scam. So, it went from 5.4 GB down to 2 gig. So, quite a sizable reduction there.

**Dave Jones:** So, that's why I'm running this transcoding uh process. So, but like I said, I do actually run this process on all of my uh more recent uh videos. But, I haven't been doing it for that long, maybe 6 months or something.

**Dave Jones:** So, I'm not exactly sure when I started there. But, anyway, um yeah, it's just sitting in the background. So, let me show you the script that I've got. Um cuz it And I did actually have to I put this on Twitter, and it's quite interesting.

**Dave Jones:** I actually had forgotten how I wrote this script. It was donkeys years ago. Donkeys years ago. I think I like cludged some code from somewhere, some examples from somewhere, and I I cludged it together, but it never handled subdirectories properly.

**Dave Jones:** Um or it did, but it only handled one subdirectory, and it wouldn't create the subdirectories. And then when you dragged multiple subdirectories in, it wouldn't handle that. So, I actually asked um Chat GPT uh to fix it to fix it for me, and it did.

**Dave Jones:** It did. It actually I'll I'll try and insert I'll try and edit it in here. Um and it actually fixed it for me. So, this is um So, this is like you can see my old code uh well, yeah.

**Dave Jones:** No, the the old code is basically this, right? The old code is basically this here, but it it added in this loop thing with this So, this makes a new subdirectory.

**Dave Jones:** So, because of course, when you drag in a whole bunch of subdirectories. So, what I'm doing at the moment is I'm grabbing like, you know, a hundred of these subdirectories, right?

**Dave Jones:** I won't actually drag it now cuz it'll start another process. Um it'll actually physically start another HandBrake process. So, I can do like multiple ones at the same time, but you're not getting any speed increase cuz it's just sharing the GPU resources.

**Dave Jones:** Anyway, so I just drag in like a hundred subdirectories. That that'll be like you know, 5,000 files or something, right? 5,000 video files. I just drag them in there.

**Dave Jones:** And um it it just handles it all. It's really cool, right? So, this is my um script. Oh, actually I'll probably I don't know. I can leave it down in the comments down below, but you can see it here.

**Dave Jones:** If you want to do it uh for yourself, it's really good. Um so, yeah. I'm just running uh the hand the command line version of HandBrake here. I'm just uh and you can see it's just putting it on my local D drive.

**Dave Jones:** So, I sort of like hard hard coded that um in there, right? And it's running the NVEnc uh H.265 encoder. Quality factor 26. Uh that's all audio encoder um a AAC.

**Dave Jones:** Uh verbose just puts all the crap on the screen um there we which I kind of like. Um CFR's constant uh frame rate and it just matches the frame rate.

**Dave Jones:** So, if you feed in 50 frames 50 or 60 frames per second, you get 50 60 frames per second out, but I can change that using the command line options to anything uh that I want.

**Dave Jones:** I've even got other like on my main machine desktop machine, I've got like a dozen different batch files set up for different things for doing, you know, for sizing uh 4K down to 1080p, for example, and other stuff.

**Dave Jones:** So, changing frame rates and uh for my podcast version, my 720p podcast version, I've got one specifically uh for that. So, as soon as I finish rendering a video, I take my 4K or 1080p content, I drag it onto a specific uh batch file that I've got.

**Dave Jones:** That creates my uh podcast version. So, so I just got ChatGPT to add in this rem this uh loop thing. Look, it's even putting comments, rem, you know, rem, which is short for remark.

**Dave Jones:** Um you know, old school DOS batch stuff, and it works. It works really well, and as I said, like, it's processing now tens of thousands of video files, all in sequence.

**Dave Jones:** So, it'll just do it one it's just doing one file at the moment, and look, it's just about to finish. Boom, it loads in another. You can see where it actually got it from.

**Dave Jones:** This is the Unity UPO 3000 teardown, for example, and see and see is the uh clip 16 MPEG-4, which came Oh, that was quick. Right. And some will be 4K, like, this is 60 frames per second.

**Dave Jones:** So, I don't know why I was shooting 60 frames per second teardown for. Uh that's a bit dumb. I usually I shoot 30 frames per second now. Um so, this might this was obviously on an older uh camera, or I changed uh settings or whatnot.

**Dave Jones:** But, yeah, I just wanted to show you the batch file. So, I'm just uh transcoding all these to make them about 1/3 the size they were before. This is just for backup archive purposes, and this is not the videos I upload to YouTube.

**Dave Jones:** Again, this is just keeping all my old raw files, and I've got a whole stack of hard drives, which I keep them all on. But, the more modern ones, 4K content, high bit rate stuff, you know, it it you don't fit many videos onto like a 2 TB hard drive for example.

**Dave Jones:** Like you might fit, you know, 50 videos on there. I don't I don't know exactly, right? Well, I can go in here, right? Here's the note. Here's the Here's the raw files.

**Dave Jones:** Let's take a, you know, a 4K Aha, 4K content. Here you go, my ultrasound teardown video 13 14 for example, right? So, you know, it's like 1.5 gig, you know, just for one clip cuz I start and stop my camera.

**Dave Jones:** Like every time I change angles or, you know, start and stop talking, I start and stop a clip. So, a teardown like that, it's got 75 clips, right? 75 clips.

**Dave Jones:** For a teardown, that's that's typical. You know, a typical video might have 50. Like a typical teardown might have 50 videos or something like that and these have These are images like, you know, screen captures and stuff like that, so overlay um stuff.

**Dave Jones:** And the interesting thing about HandBrake, I believe I tweeted this. I didn't know this, but if you've got a text file for example, so if if one of my videos actually contains a text file, like just a TXT file, it'll actually convert HandBrake will convert that text file into a a scrolling video.

**Dave Jones:** Into a little scrolling video. And it does the same with images, too. It actually converts them to video. So, this script, it doesn't look for just video files. It'll look for any file which it knows and it'll convert it into a video file.

**Dave Jones:** So, if there's just an image, you know, this script will actually um just it'll generate a little short little, you know, uh video clip or something. Like short, like really I don't know how long it actually is, but quite short stuff.

**Dave Jones:** So, in fact, we might be able to go and see that. Yeah, here it is here, right? Here So, here's the DEERCEL battery scam here, right? And it's actually create image one, image two, image three, right?

**Dave Jones:** So, it's actually created. Will we see Do No, I can't play that. But, yeah, it's it's actually converted some images into tiny It's only 270 bytes, right? But, it converts it into tiny little And And the thumbnail there, it converted the thumbnail.

**Dave Jones:** So, I don't know how that works. But, yeah. Um yeah, HandBrake can do things like convert text into scrolling text. It's actually really quite cool. So, yeah. Anyway, there you go.

**Dave Jones:** That's my uh batch file. That's my uh magic HandBrake batch file, which I do a ton of different stuff with. This is why I'm obsessed with HandBrake, cuz it's got the command line version, and I can just drag entire subdirectories, or in this case, a selection of like a hundred different subdirectories of all my raw videos, 10,000 video files, one drag, walk away, and then it generates um it

**Dave Jones:** it generates all these um So, this subdirectory was empty before, and where Where did we start at? I don't know, 12. We were up to something 31? Was it up to 31 before?

**Dave Jones:** So, oh, I might still be Is it still working on that? Don't know. Since I've been shooting this video. But, oh, and the reason I'm not doing this on my main machine with my new 4060 uh GPU card is cuz there's, you know, it's about 30% quicker, maybe.

**Dave Jones:** Um but, this thing does like for 1080p, it's doing like 370 odd frames per second. It does like 470, 480, or something on the uh 4060. But, I don't want to leave my main machine running.

**Dave Jones:** I can just leave this running in the corner here. I can just leave it for days and days and days, and everything's hunky-dory. Um So, yeah, I'm just uh doing them in batches of a hundred at the moment.

**Dave Jones:** So, then I can Once I've done this, I will actually um once it's finished, this lot here, I will then drag those back to my uh NAS drive, and overwrite um all of those original video files on there.

**Dave Jones:** Um and I've double-checked that it's all hunky-dory. It's all good. I trust in the process, I trust in the HandBrake and the script and yeah, it's all good and I get a 70% reduction.

**Dave Jones:** Or thereabouts in uh my content, which is really good. So, yeah, pretty happy with that. So, there you go. That's my magical HandBrake script. I use it for a ton of uh stuff.

**Dave Jones:** It's really useful. I love the command line version of uh HandBrake. Those batch file experts, "Oh, you're doing it all wrong." I don't know. I just cobbled this together donkey's years ago.

**Dave Jones:** I've been using this for like a decade now or something. I've been using it for a long time. Um so, yeah, it's really cool. Anyway, if you like that video, give it a big thumbs up.

**Dave Jones:** As always, thoughts and comments down below. Catch you next time.
