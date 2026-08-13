---
video_id: DvFBnB2ws6c
title: Getting ChatGPT AI to Code a Youtube Video Uploader - Part 1
url: https://www.youtube.com/watch?v=DvFBnB2ws6c
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 30, "3": 49, "4": 66, "5": 88, "6": 105, "7": 121, "8": 144, "9": 161, "10": 174, "11": 188, "12": 208, "13": 222, "14": 243, "15": 254, "16": 270, "17": 284, "18": 299, "19": 313, "20": 327, "21": 343, "22": 359, "23": 375, "24": 391, "25": 405, "26": 421, "27": 437, "28": 454, "29": 466, "30": 483, "31": 499, "32": 517, "33": 533, "34": 551, "35": 571, "36": 601, "37": 614, "38": 629, "39": 647, "40": 664, "41": 681, "42": 696, "43": 711, "44": 732, "45": 754, "46": 770, "47": 787, "48": 810, "49": 832, "50": 852, "51": 869, "52": 886, "53": 902, "54": 919, "55": 937, "56": 957, "57": 987, "58": 1000, "59": 1016, "60": 1029, "61": 1043, "62": 1056, "63": 1072, "64": 1089, "65": 1105, "66": 1128, "67": 1154, "68": 1176, "69": 1196, "70": 1217, "71": 1233, "72": 1252, "73": 1264, "74": 1280, "75": 1298, "76": 1314, "77": 1333, "78": 1360, "79": 1379}
---

**Dave Jones:** Hi! As a lot of you might know, I'm not just on YouTube. I'm on many different platforms. I always have been. In fact, I've been one of the pioneers on virtually every video platform that's come out. I'm on Odyssey, still got 72,000 followers there.

**Dave Jones:** I'm on Rumble over here, even though I don't use Rumble, I've got 1,500 followers there. My videos are on there. Of course, I'm big on X. I'm posting natively on X. I was one of the first to do that. So all my videos are native on there.

**Dave Jones:** And then I'm on Facebook as well. How many? 24,000 followers on Facebook. I post natively on Facebook. And I've got my own website, EEVblog.com, where you'll find my latest videos as well. I used to put Odyssey links in here, but I've gone back to putting YouTube links in there.

**Dave Jones:** But anyway, you can go in there and you can watch the videos directly on the website. And I even upload, ever since video number one, I've uploaded every single video to my own dedicated server. I've got my own box that does this, and you can just, in 720p,

**Dave Jones:** usually not in HD, let alone 4K. But 720p versions are available here, on my own website. I've got them all the way down here. Do we have number one? Yes, we've got EEVblog number one, right up there. So that's on EEVblog.org. And this, of course, worked well for a few different platforms like Odyssey and Rumble and BitChute

**Dave Jones:** that supported automatic upload from YouTube. They would automatically pull in your latest video for you. But YouTube broke the tools. They took their bat and ball and they went home. And according to Rumble here, it was like a year ago now that they actually broke the tools,

**Dave Jones:** they broke the toys, for the automated uploads for these sites. So my last one on Rumble, because I don't use it, I haven't been manually uploading there. It died about a year ago. It was actually automatically uploading both my second channel videos and my main channel videos.

**Dave Jones:** It was actually automatically uploading them there. But yeah, it stopped. But Odyssey, they found a workaround for YouTube breaking the tools, and that worked up until recently. But back on November 7th, 2024, Odyssey said, look, please upload your videos manually now, because YouTube broke their sync tool.

**Dave Jones:** Now, YouTube has recently implemented additional anti-competitive measures that limit our ability to automatically sync videos from YouTube to Odyssey for creators who have opted in the service. These changes make it increasingly challenging for us to maintain automatic syncing. While we cannot specify timelines, likely YouTube syncing may eventually be discontinued.

**Dave Jones:** In light of this, we strongly recommend you manually direct upload. Now, I was, because I'm one of the top channels on Odyssey, and one of the founding members, they actually, they did find a workaround for this, but it wouldn't work for all the channels.

**Dave Jones:** So there were only a few select channels, and mine was one of them, that they continued, that they could continue auto-uploading. So that was working for a while after YouTube broke the toys, but now, it's only recently, it's, all of a sudden, it's stopped working.

**Dave Jones:** So I've got to manually upload to Odyssey now. So this is getting rather annoying. So the only one that seems to now automatically upload is BitChute, and BitChute sucks. So, I don't use BitChute, I just, like, it really sucks bad. But all the others, Facebook, X, Rumble, Odyssey,

**Dave Jones:** I've got to upload onto these platforms manually, let alone my own server as well, let alone YouTube. So, you know, I'm uploading to more than half a dozen, every time I make a video, I've got to upload to, like, half a dozen different places manually.

**Dave Jones:** And for years, donkey's years, I've been asking around, surely somebody has written a tool to actually automatically upload via the APIs, because these platforms have APIs, via the APIs to upload to all the different channels. Surely every video creator wants that. Any video creator is not on every platform is just,

**Dave Jones:** well, I don't know what you're thinking. Because, well, even if you have to upload manually, you should at least have one backup platform, goodness sake. So as far as I'm aware, nobody's ever written this tool. A few people over the years have contacted me and said,

**Dave Jones:** hey, I can write that, I'm working on it, and I never hear back from them. So I decided, hey, use AI. So I'm not a good coder myself, but AI can apparently code. I've done videos on that. So I thought that I would actually ask ChatGPT,

**Dave Jones:** can you create a Windows programmer script, purpose of which is for a video creator to upload a video file to YouTube, other video hosts and playstorms, Odyssey, Rumble, et cetera, and WordPress. The user would be prompted for the file name, preferably drag and drop,

**Dave Jones:** because I've got like a handbrake script, which I wrote, that I just transcode, I just drag and drop my file onto that, and it creates the 720p podcast version, which I upload, and also the raw files for my camera. I've also got batch programs that I just drag,

**Dave Jones:** entire subdirectories even, into there, and it'll transcode all the files for my camera and make them smaller, so I don't have to archive them all anyway. So I've got like automated command line scripts for that. And yes, it can. It can create it.

**Dave Jones:** So here we go. I won't go into all the details here, but, you know, it claims it can be able to do it. It'll have, you know, error logs. It says it can use the APIs for direct uploading stuff. WordPress uses a REST API.

**Dave Jones:** I don't know what that is, but it claims it can be able to do it, and this is how it's going to implement it. It would use Python for the back end, using Tkinter for GUI. I don't know what that is. PythonTube, Google Auth,

**Dave Jones:** and YouTube upload for YouTube, API integrations with requests for Odyssey, Rumble, YouTube, and Selenium or automated browser interactions for BitChute. But I don't, I'm probably not going to do BitChute. I will start by creating a basic version of the program in Python. Would you like a GUI version,

**Dave Jones:** easier for users, or a command line version? I don't want that GUI rubbish, so command line is fine. And I ask, could the command line version do video file drag and drop? Yes, it can. So it claims to be able to do all this sort of stuff.

**Dave Jones:** Like, I just take my finished video file that I've edited, drag it onto this Python script, and it should, in theory, automatically upload to all the platforms. That's the plan anyway. Would you like me to start coding this? Ask if it can add support for X, Facebook, and Instagram.

**Dave Jones:** Yes, it can add that. And then it goes on and tells you how it's going to do it, and next steps, and all this sort of stuff. Yes, please create this command line version using the config file for user platform settings. So all the API settings,

**Dave Jones:** put those in a separate command file, and I asked it to go do it. And sure enough, here's the code. It actually created this here. And I'll move my ugly mug out of the way here, because, look, you can refine and debug on the spot

**Dave Jones:** using Canvas. I assume we're already in Canvas. So, got it. Yes, so it adds this code here, and every time you tell it to make changes, it actually just goes over the same code and then modifies it. It's really quite cool. But I know that every script kiddie out there

**Dave Jones:** already knows this, because they're already using AI for bloody everything these days. But anyway, I'm not that used to it, and I don't know Python. I can understand what's going on here, but I don't know the syntax or anything like that. So I don't know if any of this is actually legit stuff.

**Dave Jones:** Anyway, so I said, yes, please actually create it, and it actually created it. Sorry, I don't have the old code that it actually made. So I asked it to add user input for keywords, because I forgot about keywords, and I asked it to remove bit chutes,

**Dave Jones:** so I removed bit chute from the code. And then there does not appear to be any API call code in this script. It just had API. Sorry, I don't have the old code, because it's already overwritten it. It had just call API, call YouTube API,

**Dave Jones:** and there was actually no code there. So I don't know why it didn't do that on the first draft. I don't know. And it went, you're right. The script contains placeholders, but doesn't have actual ATI calls implemented. After I said that, it actually just automatically redid the code,

**Dave Jones:** and you can physically watch it go through line by line and change it, and it added all of the, presumably, yeah, this is the upload to YouTube part, and this is where it calls the YouTube build developer key. All right, so it pulls the API key

**Dave Jones:** from the config.json file, for example. And then it hadn't added all the platforms there, like Facebook was missing, so I just said add Facebook, and sure enough, it just added the extra Facebook, and then X wasn't there, so I said add video to X,

**Dave Jones:** and sure enough, it just added in the X code there, and here we are. Now, so yeah, I don't know if this works yet. I haven't actually tried it. It looks like it might attempt to do something, although it doesn't. I noticed up here that the config file, config.json,

**Dave Jones:** it'll print an error message if there's no file, but then it doesn't tell you the syntax for the file, so I'm going to ask it to add. Can you add help syntax for the config.json file so the user, probably don't have to explain this,

**Dave Jones:** so the user knows what syntax to use. And editing, editing, editing, come on, Mr. AI, here it goes, and it should change this config help. Your API key, right, right, so it's just YouTube API key first, WordPress API key, cool, cool bananas. Okay, using the following format print config help,

**Dave Jones:** so it's just going to print that. Cool. So it just added some extra little nice help there. Neat. So I guess what I'm going, like, I don't know. I'd have to go through this line by line and figure out if there's anything else missing.

**Dave Jones:** I mean, you Python coders out there are probably going, oh, this is missing, this is missing, this is missing. But I can come back later. So I think what I'm going to do is just, you know, I just highlight this, save it all to a Python file,

**Dave Jones:** and I guess I just try and drag a video onto it and see if it works. I'll get back to you. Okay, so I just saved that text to uploader.ph, and I put a shortcut on the desktop here. So I should, I guess, be able to just drag in a file

**Dave Jones:** and it calls Python and just runs it. Let's try it. It'll give me the error message there's no config file because I haven't actually done that yet, but we'll see what happens. Okay, I just drag a random file into here. Well, no. Something happened too quick there.

**Dave Jones:** So I just tell it, add a pause before the program exits because, yeah, you want to be able to see what it was spitting out before that script ended. So it'll go through, and yeah, once that's finished I will save that again, try it again.

**Dave Jones:** It's actually pretty slow, I guess, like in terms of doing this. If you have to make one minor change like I do because I just don't know the syntax, I'm sure it was trivial just to add a pause in there, but I didn't know how to do it.

**Dave Jones:** So how did it actually input? Input, press enter to exit. Right, okay, so I didn't actually know that. So that's, yeah, all right, so let's copy that in there and see what's what. All right, so let's try that again, shall we? Oh, no.

**Dave Jones:** No, I've got Python installed. Everyone out there is just screaming. We're going, Dave, you dumbass. I don't know anything about this stuff. So can I just run upload a py, like that? No, line 6 in module import request, module not found, no module named requests.

**Dave Jones:** Okay, so we have our first bug, have we? So I assume traceback, I assume it's loaded Python, right, because it knows it's associated py files with Python, so I assume it's called it. And line 6 in module import request, okay. So let's go up here to line 6, import requests.

**Dave Jones:** Okay, I have no idea where import requests is. I don't know. Is that needed? Is that a mistake? It's a good thing I have an AI robot helper, isn't it? I get an error in line 6, import requests. Why? The input suggests that the request library

**Dave Jones:** is not installed in your Python environment. You fix this by installing a pip install requests. Okay, right. What is bash? If you're using a virtual environment, insure after install, try running the script again. Okay, pip install requests. Pip install requests. Is that it?

**Dave Jones:** There you go. It's downloading. Cool. Cool bananas. Let's run it again. Upload a .py. Now it's an error in line 7. Module not found error, no module named Google applicant. Sorry, applicant. Google API client. I'm seeing those mixed up there. My mind was assuming.

**Dave Jones:** Error in line 7. This is a good thing about this. You can just ask the AI bot for help. No module indicates that Google API client is not installed in your Python. Ah, you can fix it. Right. I should ask it. Is there anything else that I have to install?

**Dave Jones:** Because this could go on forever. Google API Python client install. Okay, cool. Cool. That looks like it's working. Bingo. Upload a .py. Oh, look. Yay. It got past it and it's giving me the help. Config file missing. Please create a config file JSON using the following format.

**Dave Jones:** Right. So you have to actually, so it looks like the text has to include YouTube and then API key and then, you know, so you've got to put your API key within that string there. So it's got to actually contain that. So cool bananas.

**Dave Jones:** We're getting there. Okay, so I've created my config.json file. Now I have to go get, I have to go to each of these platforms and get the API keys. So I'll start out with my second channel or I've got actually a couple of channels I've got nothing on.

**Dave Jones:** So I can try those out as dummy channels and see if it uploads. Hmm. But I can ask it, where do I find my YouTube API key? Because, I don't know, I just have to type that into Google anyway because I can't remember.

**Dave Jones:** I think I got it at one point, but, you know, I can never remember where that sort of stuff is. Google Cloud Console. Okay. Select a project. Create a new project. Project name. Okay, yeah. I thought it was something like that. Enable YouTube data API version 3.

**Dave Jones:** Blah, blah, blah. God. God. Okay. Right. But it's good. It gives you the help. Great. Wow, this is not bloody easy, is it? It's so complicated. There's so much crap that you can integrate with. I guess, you know, they've got so many tools and whatnot,

**Dave Jones:** but, oh man. YouTube data API version 3. Access to YouTube data. Okay. Enable. Create credentials, I guess. YouTube data API. This wasn't as easy as the AI made out. Am I doing it wrong? Probably. No, this seems kind of wrong, doesn't it? Oh, no.

**Dave Jones:** Here I am. Create credentials. Okay. Right. Create credentials API key. Okay. Creating an API key. I won't show it, obviously. Uploader.pi. Okay. Uploader. Right. Yes. Uploader. Okay. Slash. H. Title. Description. Keywords. Thumbnail. Video path. Following arguments required. Video path. Okay. Because I didn't drag in a video to it.

**Dave Jones:** So, let me try that. Okay. Drag in a video file. And, what? What happened there? I blinked. Ah. It flashed up. It was on my other monitor. So, I did capture it. It said, uploading to YouTube. And then it just, um. I've got to add.

**Dave Jones:** It's going. I've got to add a link. I've got to add a link. I've got to add a link. I've got to add a link. I've got to add a link. It's going. I've got to add, like, pauses, to that. So. Maybe it's uploading in the background, but it didn't prompt me for the title or whatever,

**Dave Jones:** which is what it was supposed to do. So, it's failed on that. It was supposed to. The whole idea was drag in a file. And then, you know, it prompt me to type in the description and everything else. Um. So, it does the command.

**Dave Jones:** It looks like it might do that on the command line. But I don't want to do that. I've got, like, a text box that I can, you know, type in the description with, and the title and stuff. And I'm not sure which channel it actually, um, uploaded it might be attempting to upload

**Dave Jones:** to as well. I don't know where my API credentials didn't seem to point to a channel, so. I don't know how that works. I just know it. There's going to be a thousand people in the comments telling me how to do this. And they'll all say something different.

**Dave Jones:** So I asked it. It did not prompt me for the title, description, and keywords. Why? The script is current. It automatically uploaded the code. It automatically adds and modifies the code. I guess you can tell it to undo the last thing. Um. But it's automatically updating the code, even though I didn't really ask it to.

**Dave Jones:** I was just asking why. If these arguments are not provided, it defaults to using the file name as the title. Yeah. Right. Okay. So it, I checked my YouTube. It wasn't uploading anything. Um. So. Solution. Prompt for user input. I will update the script to prompt the user for missing values if they're not provided

**Dave Jones:** by command line arguments. Yes. But it didn't ask me. It just went ahead and did it. And it's not exactly the quickest thing, um, out there either. I know it's amazing what it's actually doing. It's suddenly only 80 lines? It was like 130 lines or something before.

**Dave Jones:** What's going on? Muler. Bueller. Bueller. Okay. So it's passing arguments here. Fair enough. And if the argument doesn't, right. Prompt for missing imports. Okay. So it's added that. I'm sure it was like 130 lines. Like. No. Look. Look there. No. The code is missing.

**Dave Jones:** The code is missing for all of the upload to YouTube things. It's just gone. It's just gone. The code was there. And that, like, those functions were there. All the functions for uploading seem to have vanished. Vanished? Vanished. All the functions for uploading seem to have vanished.

**Dave Jones:** What the heck? What does that have to say for itself? It looks like the upload functions were removed. When I updated the script to, oh, restore the up, yes, please. Dumbass AI. Why would it actually remove? Hands up if you actually use this on a daily basis for coding, because this would be so

**Dave Jones:** frustrating. Well, the speed of it's faster than what a coder could do. But if it's just going to remove stuff like that, that's just ridiculous. I know that GitHub doesn't, it has its own AI co-creator, and I've heard good things about that and stuff like that, but I have no idea how that works.

**Dave Jones:** And other AIs might work better than ChatGPT, but I'm using the latest 4.0. It is the latest, isn't it? Yes. Great for most questions. It's painfully putting them back. It's got to redo the whole thing each time, and then it hallucinates that it forgets that

**Dave Jones:** you, as AIs do, AIs hallucinate, and they'll never get rid of that, because they're trained on humans, and humans hallucinate. So that's why AIs hallucinate, and you'll never get rid of it. You can't just hard-code that. You can't just beat it out of it.

**Dave Jones:** But yeah, it's just totally forgotten that it had those things, and wow, that's not very good, is it? But anyway, it's still doing it quicker than I can do it, because I don't know how to code in Python. Or use the APIs. You know, you have to read the API documentation for each one, and it's like, you know, that's

**Dave Jones:** the advantage of AI, is it can just go out and get this sort of information. And you can probably just, you know, instead of writing the whole program, if you just need to know the API information, you don't have to go out and try and find it, you can

**Dave Jones:** just ask the API, give me this short routine, that, you know, and then you can just cut and paste that into your code. So anyway, oh, it's still going. There we go. All right, I'm going to drag my file in, I'm going to upload it, ta-da, there you go, enter

**Dave Jones:** video title, upload test, enter video description, upload test, test. It still doesn't, oh, it's, yeah, see, it said upload into YouTube, I miss what it said after that. It had an extra line, because before it only said upload into YouTube, but it had an extra

**Dave Jones:** line after that, so I don't know what that was. Once again, I have to add, like, a pause in there. So I can do that manually, there you go, press enter to exit, I'll just add that, and I'll just do it again. Did it not like my file?

**Dave Jones:** No. My command line box popped up in the other window, and it just didn't do anything this time, so what? So the only other print thing after that was YouTube upload complete video ID, so I guess it printed that, but why doesn't it like input, press enter to exit, because it did that down

**Dave Jones:** here, input, press enter to exit. I'll try another file. No. Unfortunately, I've run out of time for right now, so I'm going to annoy absolutely everyone by uploading this half-arsed attempt at writing, well, getting AI to write an automated script that will accept a drag-and-drop file and then upload to multiple platforms.

**Dave Jones:** And you watch, people just go crazy in the comments down below, go ahead, go ahead, bonus fun for everyone, grab your popcorn. So whether or not I just have to massage it a little bit with my tongue at the right angle or not, I don't know, but yeah, I'll get back to you.

**Dave Jones:** Work in progress. Catch you next time.
