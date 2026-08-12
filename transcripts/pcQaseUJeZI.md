---
video_id: pcQaseUJeZI
title: EEVblog #871 - Find Aliens With Your Raspberry Pi!
url: https://www.youtube.com/watch?v=pcQaseUJeZI
source: youtube-asr
---

**Dave Jones:** Hi. How many of you have one of these lying around? A Raspberry Pi, be it an original Raspberry Pi, Raspberry Pi 2 like I've got here, or whatever the latest flavor is. I bet there's a lot of people out there who bought one of these

**Dave Jones:** things because, hey, it's a cool little Linux computer, you know, and it's super duper cheap. But there's probably a lot of these lying around doing nothing, just going to waste. So, I thought that was a bit of a shame. myself thought,

**Dave Jones:** hm, I've got a couple of these lying around the lab. What can I do with them? Can I do anything useful? I know. Let's look for aliens. Why? Because aliens. Let's go. I've got a Raspberry Pi 2. I've got it all hooked up. Let's

**Dave Jones:** see if we can find ourselves some aliens. Beauty. As you might know, the Raspberry Pi 2 I've got here uses a fairly powerful Broadcom ARM processor. Um, and this particular one actually has four cores and it works uh close to one

**Dave Jones:** gig or thereabouts. So, it's a pretty powerful beast. Not in terms not really, you know, like PC powerful, but in terms of uh power per watt, i.e. MIPS per watt, processing power per watt, it's a pretty decent device. So, I thought we'd

**Dave Jones:** uh see how well this thing does with boink. What's boink? Let's find out. And for those curious to know how I'm going to do this, I'm actually taking the HDMI video output of the Raspberry Pi here. I'm feeding it through my AVA Media Live

**Dave Jones:** Gamer Portable. So, that captures the um the HDMI signal. I've got myself a uh mic plugged into this thing. So, let's go straight to the video capture. Beauty. Now, before we get into STI, aliens, boink, and of all people, Paul

**Dave Jones:** Horowits, I thought we'd uh just fix something really annoying here. You'll notice a black border around the screen here. This is not a problem with my um screen capture. This is actually an out of the box problem with the Raspberry Pi

**Dave Jones:** or more specifically the uh Noob version at least of the uh Raspian OS that um I'm running here. So, it's I need to fix it. It's bugging me. Now, this is actually a problem with overcanning designed for TVs and things

**Dave Jones:** like that. And we can fix that by going into the uh boot operating system and the config txt file here. Now, if you take a look at the settings here, we've got overcan things. These are commented out, but there are default settings for

**Dave Jones:** overcan. And overcan's actually turned on by default. And this is an old uh style thing designed to um fix problems with, you know, old TV sets and and monitors and things like that. But modern LCDs and and monitors and TVs,

**Dave Jones:** you don't need this. So, I don't know why it's turned on by default. It's just really annoying. Anyway, we can fix it. So, it seems I can't use the uh editor that comes with uh the Raspberry Pi to

**Dave Jones:** do that. It won't let me save the file. So, that's interesting. So, we can use the command line uh pseudo nano boot/config txt. I know you want to get to the aliens. I know. I know. But let's go down here and let's uh disable

**Dave Jones:** overcan, shall we? There we go. So, let's reboot this puppy and uh see if we can fix it. And twiddling thumbs. Oh, pretty. I have no idea what any of that does. H. Ah, that's much better. Now, we can

**Dave Jones:** get back to aliens. Now, how we're going to use our Raspberry Pi to search for aliens is to use the Seti at home system. Now, this is not uh new. It started in about 1999. Uh, coincidentally, um, sadly, Prince just

**Dave Jones:** died today. So, yeah, let's party like it's 1999. Let's go crazy. Find some aliens, shall we? Um, it was an initiative uh to uh try and utilize people's uh home computers that were just sitting there basically doing nothing most of

**Dave Jones:** the time. all that CPU horsepower sitting there doing nothing, just idling away, waiting for you to do your word processor or surf the web or something like that and all that processing power going to waste. So why not use it to

**Dave Jones:** actually do some science and process uh data because SEI requires massive amounts of uh data to be processed, massive bandwidths of data to search for all the different frequency bins and FFTs and do everything else. So they thought hey if we can probably get you

**Dave Jones:** know 50,000 computers or something like that at the time uh then it could you know really have a very significant impact on the science of actually searching for uh signals. So, so they developed software called Boink. Yes, that's how you pronounce it, I believe.

**Dave Jones:** Uh, it stands for the Berkeley Open Infrastructure for Network Computing. And, uh, what it is is a program that, uh, just ties all of all computers together and shares processing tasks between them. You know, that it'll send you a little chunk of data to uh, play

**Dave Jones:** with and then you use your idle time on your computer to solve it and then sends the result uh, back. But it's not just for it started out just a SETI but now Boink actually supports a whole host of

**Dave Jones:** different uh science uh projects which we might have a quick look at uh later but you can contribute to dozens and dozens of different scientific endeavors with the Boink uh software. It's available for Windows. It's available for um Unix and Mac and also for your

**Dave Jones:** phone as well. for your Android uh phone, you can get an app, so when your phone's doing nothing, it can do some processing as well. And uh the the thing is they've just released the latest version of it. And the latest version

**Dave Jones:** release uh includes support for the Raspberry Pi for ARM uh processors. In fact, it's not just for the Raspberry Pi. should in theory work on many different ARM embedded ARM platforms if it uses a specific uh type of uh

**Dave Jones:** interface which the Raspberry uh Pi you know software type interface which the Ras Raspberry Pi does. Now, I've always been interested in the SEDI uh at home thing, the search for extraterrestrial intelligence, but I never uh got around

**Dave Jones:** to really trying it. But I was spurred on after watching this uh Paul Horowitz, yes, of art of electronics uh fame. He's actually one of the pioneering researchers on SETI. Not many uh people know that, although it's in the back

**Dave Jones:** blur of the book, I think. Um and he's gave a great fantastic talk at Google about SETI research old computers and and calc and ballpark back of the envelope calculations. It's brilliant. Just watch it. I'll link it in down

**Dave Jones:** below. Uh we what we need to do is we need to download and install the one for um on the Raspberry Pi. So we're going to open a terminal window here and we have to do some fancy fancy commands,

**Dave Jones:** but uh we can install it. I've already installed the software on here. I've already actually created a setiat at home account on my Windows PC. I just did that first. You don't I don't believe you have to do it in this

**Dave Jones:** particular order. You can just do it on the uh Raspberry Pi, but just be aware that I've already created account. So, I have login credentials on the STI at home uh network. So, what we want to do is we actually want to install the Boink

**Dave Jones:** uh client software. This will install as a uh demon on the Ras on the Linux on the Raspberry Pi. By the way, I'm using uh Raspian uh the Raspian Noob install, the latest one available today. I don't know what uh version it is. And we do

**Dave Jones:** this using the uh pseudoapp get install boink client command. It'll go away and automatically find that. So if we type that in, it'll download. It's reading the package download. It's installing and after there will be used re preconfiguring package blah blah blah.

**Dave Jones:** And it should ask us are we sure? No. Come on. Come on. You can do it. So there you have it. It's installed the uh Boink client. No problems at all. So that will automatically load and read the uh configure the Boink configuration

**Dave Jones:** file and for the SETI at home project and for any other scientific projects you want to run on here as well. It doesn't, as I said, doesn't have to be uh seti at home, but that's what we're running today. Now we want to actually

**Dave Jones:** do exactly the same thing again, but we don't want to install the Boink client. We want to install Boink. And this installs the boink guey manager uh software which we can play around with at a guey uh level which is just nice to

**Dave Jones:** be able to change settings and things like that. So I'll install that one as well. Twiddle our thumbs and we'll come back. Doesn't take long. Do you want to continue? You bet your ass I want to continue. Sixmeg. Jeez. When I was a

**Dave Jones:** boy, let's go crazy. And we're done. Now, for all you uh command line afficionados, we can actually go in and use the command line to do everything. So, we can use the boink uh command command line uh program and we can

**Dave Jones:** install uh projects or what you know in this case set at home and we can attach projects and we can do all sorts of stuff. We can set up all our parameters and do everything else but eh that's

**Dave Jones:** just nah too hard. So, let's go in here and we should find that now over here in system tools, we've got the boink manager. Beautiful. Let's load that up. And just as a little aside, if you want to find out what temperature your

**Dave Jones:** Raspberry Pi process is running at, you can do that at 37.9°. But we're doing, you can see the processing uh bar up here. We're doing bugger all because we're just running the goo. We're only like using a couple

**Dave Jones:** of percent of our processor. But when we run uh the Boink software, it can be up to 100%. We can set how much of the processor we utilize, and the processor might get a bit warm. And here's our boink manager. And

**Dave Jones:** I've already uh because I've already got an account attached, um it looks like it automatically even though I reinstalled the software, it did go back to where I came from. So obviously uninstalling the thing didn't get rid of uh some things.

**Dave Jones:** So, I am actually um still attached here. So, let me kill that and we'll do it from scratch. But first, one thing we want to do is run the CPU benchmarks to actually find out how fast uh Boink

**Dave Jones:** thinks that uh this Raspberry Pi actually is. And you run it and you think it's nowhere, but you have to actually go over here into the event log to actually uh find the results. It's currently running the CPU benchmarks and

**Dave Jones:** it'll do floating point tests. It'll do integer test and give you a result in uh MIPS, dry stones, you know, all your standard uh benchmarking uh stuff. I'm not sure of the exact um algorithm it's actually using there, but it'll give us

**Dave Jones:** a figure of how fast this Raspberry Pi is. And then we can compare it with my uh dual Xeon desktop PC. And here it is, 292 floatingoint MIPS uh Wheatston per CPU. But remember, we've actually got four CPUs, and you saw before how we

**Dave Jones:** actually had four tasks running at once. So, it's actually going to run one task per CPU. And it's got 1161 energy MIPS um dry stones per CPU. And this is drastically less than what I get on my uh 12 core dual processor Xeon machine.

**Dave Jones:** But that's to be expected. This thing's drawing bug raw power and my Xeon processor is drawing a ton of power. But hey, if it's it's all about the processing power per watt essentially. So what we want to do is go in here and

**Dave Jones:** add a project. So and here's all the different uh projects I told you about that you can get with boink asteroids at home searching. That's not playing asteroids again. That's actually processing searching for aststeroids. The asteroids um the atlas uh thing for the CERN large

**Dave Jones:** headdrawn collider you can do some processing for that. citizen science grid um high energy physics. You can do climate prediction modeling and stuff like that for global warming and other stuff. You can do you know mathematics nerds um do various things cosmology at

**Dave Jones:** home, Einstein at home which is a gravitational wave detector and you can like be involved in not just one you can actually be you know you can dedicate one CPU per uh task if you wanted to you know if you're a fan of uh all these

**Dave Jones:** things but look how many different things you can do it's just absolutely incredible. So, we're going to choose uh STI at home. Uh and cuz we want to find aliens. Yeah, absolutely. It's going to happen one day. I think we're going to

**Dave Jones:** find something. So, anyway, uh yes, I'm an existing user, so I will go in there and uh set up my account, but you can actually create a new account here. No problems at all. So, if we can There you

**Dave Jones:** go. Project added. Click to finish. And that's it. Bingo. We've got steadyi at home and it's essentially ready to go. As you can see, our processor bar at the top only drawing 2% because we haven't actually um started this thing yet cuz

**Dave Jones:** it's in suspend mode here for the activity. But if we just go run, bingo. And now our processor should or it's got to download the tasks and things like that first. So let's go in and have a look at the tasks here. And uh so it

**Dave Jones:** might take some time to actually uh configure the thing. That's why it's only drawing like a quarter because it's only running one task on one core here. So we need to uh set this up. I think it could take actually some time to do

**Dave Jones:** that. And we can actually go into tools and computing preferences here. And we can set up all how much uh processor power we actually use. And it's very powerful. You can only run it on certain uh times and dates and things like that.

**Dave Jones:** uh when you can set it to slow down or disable when you run applica, you know, when you're running applications. So, it'll only do processing when you're idle. It's incredibly powerful this Boink software. My hats off to the um

**Dave Jones:** people who uh wrote this thing. It's incred you know, while while the computer don't run it while the computer is on batteries and all that, you know, computing allowed while it's on batteries and all that sort of stuff

**Dave Jones:** while computer is in use. While uh GPU is in use, that's for, you know, PCs and things like that. So while processor is usage is less than 25%. All that sort of jazz fantastic. And then you can set if you've got if

**Dave Jones:** you live in a shitty country well great country like Australia which has shitty internet then uh and you've got uh bandwidth caps as almost every plan internet plan in Australia does whether it's mobile home broadband whatever they've got. Even at my lab here paying

**Dave Jones:** 400 bucks a month for my internet here for my 20meg 20meg connection. I'm limited to like I think it's 500 gig per month. So, you know, it can add up. Do the math in terms of uh bandwidth. The

**Dave Jones:** bandwidth requirements of this thing is reasonably small. But if you leave it running 24/7, even you know 50 or 100 uh kilobytes per second, running 24/7 can chew large amounts of uh bandwidth. So, just be careful there. Now, we can set

**Dave Jones:** up how much disc and memory it uses. use at most uh one gig of uh disc space on the Raspberry. I wouldn't use it m well maybe if you're dedicating your Raspberry Pi just to doing this. You can

**Dave Jones:** set up and use as much as you want but you know you might only set one gig or something like that use at most 9% of total disc space etc etc but uh and then you can exclude applications so you can

**Dave Jones:** stop it working when applications boot and all sorts of stuff. It's great. And if you actually hit the uh preferences button down here, it takes you over to the uh STI at home uh website where you've actually created uh an account

**Dave Jones:** and you can actually set up global things for the computers, all of the different computers on your network and things like that. So I can uh this is my um actual account here and I can uh set things up. So I can go in here and check

**Dave Jones:** it out. Here we go. Let's have a look. and we can go into uh computers on this account and we can have a look and these are the different computers that I've got running. This is the Raspberry Pi

**Dave Jones:** that we've set up. There's my um lab machine that I my dual zeon uh machine here. And that's I've had I've only had that running basically uh for yesterday. And I've already accumulated um a total credit of 3,799, which is, you know, it's getting

**Dave Jones:** there. Not bad for a day's use. And I've only got that set to like 20% of my uh process in idle or something like that. That's my Android uh phone down here. So, uh, once again, it hasn't actually

**Dave Jones:** completed a task yet. So, I only installed that one, uh, last night and had it running overnight, but it hasn't finished a task. This is my other laptop at home. Once again, I've only set these up last night, but our Raspberry Pi

**Dave Jones:** hasn't earned any credit yet, but it is processing in the background. It tells us it uses an ARM. It's got four uh, processes, last accessed, all that sort of stuff. It's fantastic. And then we can have a look at the individual tasks

**Dave Jones:** that this thing is scheduled for. So, these are the tasks. So, I'm not sure. I don't think it's actually, as I said, it hasn't Oh, yeah. There we go. It showed up. Okay. It just took some time for

**Dave Jones:** these extra tasks to actually show up. So, we're 02% of this task now. And we have a deadline of the 14th of June uh to finish this task by. We've been allocated this task. Our little Raspberry Pi has been allocated this.

**Dave Jones:** And if it doesn't finish, then I don't know, you might get penalized in terms of um your ranking and stuff like that on the STI network and stuff like that. But we have that time to do it. I think

**Dave Jones:** it'll do it. We're already up to 0.9%. I think we'll be there by the 14th of June. No worries whatsoever. And there you go. We've got four different tasks running on four different cores on our Raspberry Pi. Our Raspberry Pi. And

**Dave Jones:** you'll notice we're now up to 100% up here. So, our Raspberry Pi might get a little bit slow. So, we might want to knock that processing power back to 90% or something just so we can do some things in the background. But as you can

**Dave Jones:** see, it does still the browser still works and everything like that even with 100% CPU utilization that we're actually seeing up there. So that's actually very impressive on the part of the uh Raspberry Pi. It's not a fast um you

**Dave Jones:** know computer by any uh means, but uh it it still does the business. So it works really well. Tada. We are now searching for aliens using our Raspberry Pi. Maxing it out. I'll just sit here and wait for the signal to come through.

**Dave Jones:** Yeah, feel like Jodie Foster contact. Now, unfortunately, the Boink build for the Raspberry Pi uh does not include the graphics. Normally, we could actually select a task here and we could hit this show graphics button like this, and it

**Dave Jones:** pops up with all the funky stuff like we get on the uh desktop and other uh versions. So, unfortunately, they haven't included that. They just I guess they just decided that you know um it was they haven't tested it yet. I

**Dave Jones:** actually talked to the guys on the forum who were actually developing this and did the Raspberry Pi uh version. By the way, there is an excellent community over here which uh and message board and forum and everything else and they

**Dave Jones:** helped me. So, thank you very much getting this thing up and uh running. Had a little bit of uh issue at first, but it's it is actually as easy as I've uh shown here. And I'm just on my

**Dave Jones:** desktop here, which is a dual processor Xeon machine you've seen before. This is one I do all my video rendering on. It's got like 128 gigs of RAM, and it's absolutely uh crazy. It does actually support 24 virtual uh cores, but I've

**Dave Jones:** actually restricted it to to the 12 physical cores, six per uh processor. And you can see that's actually running 12 tasks here. And as I mentioned before, there is some funky graphics, which automatically installs as your screen saver, by the way, which is uh

**Dave Jones:** fantastic. So, I can choose this task here. And let me drag it in. And this is what it looks like. This is what it looks like. Isn't that funky? You can get different uh types of screens. Hang on. Wait. Wait for it. Wait for it. You

**Dave Jones:** can, you know, you can pan it around and stuff like that. But it's great. Here we go. So, it's it's doing the frequency bins a resolution of 89.4 hertz. I don't know how to stop it um spinning actually. Um 20 resolution 22 hertz and

**Dave Jones:** things like that. It's It is fantastic. Base frequency 6.75 gig. There you go. This is uh this data was recorded at the Greenbank uh telescope receiver 4_6. And it's got all the when the data was actually recorded, January 16th. So,

**Dave Jones:** we're uh processing all this data. So, it's searching for pulses, triplets, Doppler, drift rate, and it's I you can sit and watch this all day. So, we're almost done. So, we're almost going to get credit on our thing there.

**Dave Jones:** So, I I just love that. I just love that feature. It's just absolutely terrific. So, that uh that graphic feature. It's sad it's not on the uh Raspberry uh Pi, though. So, um yeah, I don't know. Hassle the guys on the forum and maybe

**Dave Jones:** they'll uh include it. It's like a library. The library file isn't there. It hasn't been tested. It's not included in the build and uh stuff like that. So, yep, we are almost done. And we can show all the tasks. You can actually show the

**Dave Jones:** tasks that these are the tasks that are upcoming ones that are being assigned. And this one actually is set to use my GPU. So I've got a a Radeon R290. I think it is graphics card in here. Fairly uh fairly decent uh graphics card

**Dave Jones:** in the thing. And yeah, these are all the tasks which are lined up for the thing. But uh that's brilliant. So this is screaming through them. Let's do a little bit of a uh a power comparison, MIPS per watt comparison, shall we? Wow.

**Dave Jones:** Check it out. That's incredible. 370 watts that's drawing on 100% uh utilization almost, you know, practically 100% utilization on all those 12 cores of my dual Zeon processor. But that includes all the computer overhead as well, the hard

**Dave Jones:** drives, all that uh sort of jazz as well. But still, that is what the system takes. 370 W. Here's the power consumption of the Raspberry Pi. Cranking all four uh cores at 100%. There you go. We're, you know, what is it? Let's say

**Dave Jones:** 2.3 watt. Uh 2. It's jumping around. I'm going to say, let's say 2.3 for argument sake. So, have a very quick look at the numbers here. The Raspberry Pi 2 of course was uh had a much lower uh MIPS

**Dave Jones:** per watt in both floating point and integer but it drew much much less power 75 watts per core compared to 30.8 watts per core. But of course the Xeon is cores are faster. But if you actually um do the numbers and calculate the MIPS

**Dave Jones:** per watt, the Raspberry Pi 2 is five to eight times more efficient than the Xeon processors. And that's that's pretty incredible. You know, that is a lot. So, if you were going to do this sort of thing, you wouldn't use these uh Xeon

**Dave Jones:** processors. So, of course, this is just based on the uh you know, the benchmark uh you know, floating point and integer um uh calculations, but you know, that's a decent ballpark. You can work with five to eight times more efficient

**Dave Jones:** Raspberry Pi. So, hey, build a Raspberry Pi cluster. Go for it. It's better than this dual processor Zeon. Okay, so the Intel Xeon's not exactly known as an efficient uh processor. So, you know, maybe that's not a fair uh comparison.

**Dave Jones:** Might be fairer to compare it with say a modern Core i7 which are, you know, quite efficient in especially compared to the uh Xeons, I'm led to believe. But if anyone's got any uh data on that, comparing the uh Raspberry Pi 2 to the

**Dave Jones:** i7s, I'd like to see it posted down below. So, there you have it. We're using our Raspberry Pi for something useful, doing scientific research. This is awesome rather than just flashing a stupid lead or something like that. Well, that's okay for, you know, just

**Dave Jones:** having a play around. But yeah, I like this. I think my next step is uh going to have to create like a Raspberry Pi cluster. And you know, how many of these things will I need? And I don't know. I

**Dave Jones:** could I like I could probably run set one up as a separate board, like a separate computer in each one, whether that's the most efficient way to do it or whether or not there are ways to uh you know, a lot of people are building

**Dave Jones:** these Raspberry Pi cluster supercomputers and things like that. And there's software I believe that ties them all together and treats them as like a thousand core machine. So technically it might only show up as one computer. So I'm not sure which way

**Dave Jones:** would actually be better uh to run. If you've got any info on that, please leave it in the uh comments down below. But you can certainly hook, you know, just sit a thousand of these in a rack, power them up, hook up a thousand

**Dave Jones:** Ethernet cables, and Bob's your uncle and uh configure each one as a separate computer on the STI network. But yeah, the Raspberry Pi isn't that powerful on its own, but hey, MIPS per watt, pretty decent. And by the way, all the settings

**Dave Jones:** that we actually do in here, all the properties and everything else, uh, processing power, all that sort of stuff, uh, will automatically save to a config file. And that config file be will be read by the, uh, demon that

**Dave Jones:** automatically loads, uh, when we restart the Raspberry Pi every time. So, we don't actually have to run this uh boink manager here. It'll the Raspberry Pi will just automatically boot up and you'll see the 100% processing up here

**Dave Jones:** when you restarted. My hats off to everyone at STI at home and I'll link in another video to the creator of um STI at home down below. It's an excellent YouTube interview uh with him. So, watch that uh down below. Highly recommend it.

**Dave Jones:** So, there you have it. That's how to use your Raspberry Pi to search for aliens or do any other uh scientific research. I highly recommend it if you got one lying around. Then um just set it up and

**Dave Jones:** just leave it running in the background. It takes bugger or power really in the scheme of things and it just feels good knowing that you're actually contributing to uh you know proper scientific research beauty. Anyway, if you want to discuss it, Eevee blog

**Dave Jones:** forum, all that sort of stuff link down below and we know they're out there. It's just a matter of listening. Catch you next time. Hi, this is the new Raspberry Pi 2 just released very recently and a user

**Dave Jones:** by the name of Peter Onion discovered something very interesting with this board. Let's take a photo of this lovely little board with a camera with a Zenon photo flash on it. Here we go. Oops. Look what happened. We have

**Dave Jones:** just reset. not only reset our board, but we've um actually locked it up. It is no longer working at all. To get it working again, we have to repower the thing. What's going on? Well, it's actually pretty darn obvious.
