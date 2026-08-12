---
video_id: 4Lh4Re68Ox0
title: eevBLAB #50 - Great Idea At The Wrong Time!
url: https://www.youtube.com/watch?v=4Lh4Re68Ox0
source: youtube-asr
---

**Dave Jones:** Hi, let me tell you a story about a good idea at the wrong time and how I tried to patent it. So, the story starts in early 2007. I was at the gym doing my workout as I do. I'm a

**Dave Jones:** bit of a gym junkie and I actually have um qualifications in the field. I'm actually a qualified fitness instructor, although I've never really taught any classes or done any personal training. I am actually qualified. Anyway, I was at

**Dave Jones:** the gym and back in the day, back in 2007, what's that? Uh 11 years ago now. Um you know, everyone had these newfangled iPody things. They'd been around for a while, but like everyone had an iPod. Hardly anyone was using their phone to

**Dave Jones:** listen to music, right? It was very popular. And I thought, you know, like in a sometimes I had my notebook for my workout and stuff like that. Usually I do classes, but anyway, I was doing my own workout and it's sort of, you know,

**Dave Jones:** occasionally like had a notebook of, you know, like exercises and stuff I was going to do, how many sets, how many reps of what exercise and stuff like that. So, I got to thinking, everyone's got these iPod things. What if I

**Dave Jones:** actually had the instructions in my ear? That sounds like a good idea, right? But, you know, how can I do that, right? Yeah, I could use like a voice recorder and actually record it and stuff like that, but I thought, "Hey, wouldn't it

**Dave Jones:** be cool? Like everyone's like listening to music while they're working out. What if they could actually get instructions at the same time?" Aha, the light bulb went off. So, that's when I came up with the idea for this,

**Dave Jones:** which is still there. Dates from You can see the date at the bottom to February 14th of 2007. Pod Sweat, I called it um because like iPod and sweating sounded like a good name. Anyway, I came up with I what I thought was a really

**Dave Jones:** novel idea and I think it well, it was and hence the point of this video. It was a really good idea at the time. It was just really bad timing. So, let me go into it. I wrote this in I wrote the program on in

**Dave Jones:** short order in Visual Basic. Don't know I think it was VB6 was it at the time? And basically what it did is it was a program. You would Here it is how it works is that it Yeah, that's a screenshot

**Dave Jones:** from the program. Here we go. So, we have this program here which no longer works. It needs, you know, some old like old DLLs and stuff like that. Couldn't be around with it trying to get it working on a modern Windows 10

**Dave Jones:** machine. Anyway, I can probably download it somewhere. Anyway, it basically this was the main screen and it would like allow you to put in like your weights and your reps and do like in frequency and and it would auto

**Dave Jones:** increment your weights and your reps like every second or third day or so or a second or third workout or something like that. And but the Anyway, it was it was like a Windows program that allowed you to do

**Dave Jones:** this. But the the magic in this is that my program would actually modify the tags inside MP3 files. Cuz if you're not aware MP3 files actually have like a like a tag at the beginning that has all this meta information, you

**Dave Jones:** know, the song title, you know, how it can pop up on your iPod or your iPhone or whatever you're using these days, your car radio, whatever. It pops up with the song and all that sort of stuff. All that information is embedded

**Dave Jones:** in tags in the MP3 file. And I won't go deep into details. I can put links in if you want to go check it out. Anyway, what it did is actually embedded the exercise information into those MP3 tags. So, on your iPod, when you

**Dave Jones:** actually loaded it up, it would show you the the exercises that you had to do, how many reps, how many and all that sort of stuff. But not only that, the program actually embedded a voice at the start of

**Dave Jones:** each MP3. So you didn't even have to look at the screen. So if you had like one of those small iPods that didn't really have the screen or was inconvenient, was in your pocket, you didn't want to look at it, it would

**Dave Jones:** actually tell you in your ear before your favorite song came on what your exercises you had to do. And then you do your exercises to your favorite song. Then next song come on, you do that and then give you that announcement. And the

**Dave Jones:** way it did this is one of the you could actually choose the voice. One of them was Microsoft Sam. If hands up if you remember Microsoft Sam. Anyway, that really wasn't good enough, but of course Microsoft Sam computer generated voices

**Dave Jones:** are really shitty, right? So I Here's the actual all the source code and stuff like that. I used the LAME encoder and you know, cuz that was that was the encoder back then to generate like I think I I can't remember how I

**Dave Jones:** joined the MP3 files together. Anyway, I you know, I put a lot of work into this program and learning about the intricacies of MP3 files and tags and how to join MP3 files to you know, concatenate audio and stuff like that.

**Dave Jones:** Anyway, I wanted a human voice and of course my voice is crap, right? So I wonder I do a radio show and make a living from this. So what I did is I actually got Mrs. E Vblog to record Here

**Dave Jones:** we go, 44 kHz 16-bit mono. All of these different wave files are there must have been more than exercise names, yeah. All these exercise names. So all these different exercises I got her to actually record these. So if we go in

**Dave Jones:** here, here we go, play that again. Alternate dumbbell curls. So, bent knee flat bench leg raises.

**Dave Jones:** Arm blaster curls. And So, and then I got her to record all these numbers like, you know, from 1 to 10 and then multiples. So, 30. So, 30 and then say, you know, 2,000. 2,000. So, if you wanted the number, you know,

**Dave Jones:** 2,031, then the software would convert that number into it would know that it needs 2,000 the word 2,000, you know, and 30 and 1. And it would join all those audio clips together and then it would encode those into an MP3 file and then it would

**Dave Jones:** concatenate the MP3 files along with the exercise name and everything else. So, we actually had a you know, a human voice at the start of every track. And anyway, I thought that was a really cool idea. I thought like I I looked around

**Dave Jones:** like this had never been done before, right? So, I thought it would take the world by storm, you know, like how many people are exercising and want a a thing on that worked with not only iPods but worked with any MP3 player. Didn't

**Dave Jones:** matter what it was, iPod, one of the you know, the I I had a Creative Zen or whatever it was, tiny little single double A triple A thing or whatever or it could be could have been your phone

**Dave Jones:** at the time, for example. But unfortunately, this was February 14th, 2007. So, I thought this was a fantastic idea. I told my brother-in-law Phil about it who you might have you seen on the blog before, you might know he's a patent

**Dave Jones:** attorney and at the time he was like he had just started being a patent attorney and you know, wanted the experience and stuff like that. So, he said, "We can patent this. We can Let me Let me patent

**Dave Jones:** Let me write up the patent for this, okay?" So, that's what he did. He wrote up the patent. It's like huge, right? Well, no, the patent's not big. This is like all the email correspondence, you know, and all the other stuff. Anyway,

**Dave Jones:** um yeah, I actually filed a provisional patent for this. And of course, he did it for free, so it didn't cost me anything to have the patent drafted, which would normally be many thousands of dollars. Could even, you know, three

**Dave Jones:** two three thousand dollars depending on how much time that they spend. Could be a lot more than that. Um actually, not only doing the investigation to see if it's a viable patent idea, which Phil did the searches, and he had shown me,

**Dave Jones:** "Yeah, this is like Yeah, this would probably get granted, you know, and you could own the market for embedding uh for putting exercise information in MP3 files." And I thought, "That's a killer." So, you know, even though I'm

**Dave Jones:** not a big fan of patents, I do actually technically have one from a former company that I have for underwater um acoustic type stuff. I'm a co- names co- on the patent, you know, co-patent holder on that. I got paid by $1

**Dave Jones:** from the company at the time. They had to pay me $1. So, the you know, sign the rights over to the company and stuff like that. Uh I remember I went out and bought half a muffin. Muffins were $2 at the at the

**Dave Jones:** company canteen. And for my $1, I put in chipped in an extra dollar, and I had my the half a muffin tasted great. Anyway, so I thought this was a great idea. I'd get a patent, and he did it for free,

**Dave Jones:** and I think it cost me 80 Yeah, I've got the receipt in here. I think it cost 80 bucks to get the uh provisional patent application. And what you do in that instance for a provisional patent application, it

**Dave Jones:** means like you just put it in early, and from that date it it was at the time, I believe. Don't know if it's changed now. And this is for Australia. It might be different in other countries, but from

**Dave Jones:** that date when you file the provisional patent application, you don't have to pay as much to actually uh put that in, but then from that date you have a year to decide whether or not you want to apply for a full patent. And at the

**Dave Jones:** time, you know, a full patent's like the time. It's probably more now, and that didn't cover all the countries I wanted in. So, it was a lot of money. So, I thought, "Oh, look, let's just put in a provisional patent. 80 bucks, it's

**Dave Jones:** nothing, right? Might as well put in, and then I'll see if the program becomes popular and whether or not, you know, I want to spend the full money on the full patent." So, yeah, we got our provisional patent back in March 2007.

**Dave Jones:** Beauty. So, I thought, "Hey, you know, if there's a chance these patents going to get granted, it's kind of cool. It's novel. I think it has really wide uh appeal. Who knows? It might be uh you know, the idea might be worth something

**Dave Jones:** um down the track." So, I actually released my uh program. I got some beta testers and and stuff like that. You could download it on my website. It was all free. So, I was just going to give it away, and you

**Dave Jones:** know, maybe I'd have like a paid uh version down the track and uh stuff like that. I think I might have even Yeah, I was working on like a pro version, like a paid uh version which had extra stuff or

**Dave Jones:** something like that. Anyway, so it was all looking pretty cool until ta-da! June 29th, 2007. There it is. The date that will live in infamy when the iPhone was released. And of course, the big thing about the iPhone uh was that not that it was a

**Dave Jones:** good phone or wh- whatever. Like, who cares, right? So, it was just another phone. But, it had apps. Well, I'm not sure that like the apps really I don't think they had the apps at the time, but they were all they only

**Dave Jones:** had the Apple apps. Like, you couldn't actually design your own apps and stuff like that. That might have come a year later. I don't know. I had don't don't have the info. Don't quote me on that, but I don't think that the apps were

**Dave Jones:** available straight away. You know, like everyone's writing an app these days, right? And back then, right? You got to remember this is 2007. Apps basically weren't around as we know them today. You know, they don't have your million

**Dave Jones:** different apps that do absolutely everything. So, that's why it was a Windows program. It was embedded in the MP3s. There was really no way to run an app. I just, you know, wasn't a thing back then. The technology didn't really

**Dave Jones:** exist. And it didn't really exist for another couple of years before apps would really take on not only on the iPhones, but also, you know, but then Android would come up and other phones and stuff would have apps and things

**Dave Jones:** like that. So, anyway, um it it came to the 12-month point in like, um you know, March 2008. And Phil hassled me, "Dave, you do you want to pay the five or six grand or whatever and get the full

**Dave Jones:** patent application for this thing?" So, yeah, you know, the program, like people were using it and stuff like that, but it really wasn't uh catching on all that much. And then these I I realized I sensed that these apps were going to be

**Dave Jones:** a huge thing, right? Not only on iPhones, but on every phone. Like, you know, smartphones had started and that was, you know, the what made a smartphone really were the apps that you could download for it. And I could see

**Dave Jones:** that, you know, people aren't going to be carrying two devices. These modern smartphones, uh as I Were they even called smartphones back then? I don't know. Anyway, I thought, you know, like no, people are probably going to be They

**Dave Jones:** don't want to carry two devices. They don't want an iPod and an iPhone or a you know, some other phone. They're just going to listen to the music on their phone. And if they got the phone, they've probably got

**Dave Jones:** a well, they have the ability to download apps. And I saw that, you know, apps would would totally dominate this thing. And really, yeah, my idea as a as it was that I thought, um yeah, didn't really have a future in the app side of

**Dave Jones:** things. So, it still could have been used in an app in terms of uh embedding exercise music in an MP3 file, and I don't know, maybe I could have made a fortune from it, but I don't know. At the time, I decided

**Dave Jones:** that uh yeah, it really wasn't worth the $5,000 at least. Um I couldn't see my return on investment on that thing, and I decided nah, let it lapse. So, anyway, there you go. I could have owned the patent on

**Dave Jones:** uh putting exercise information inside an MP3 file, but whether or not that would have been used in apps down, I don't know. If you're I don't use exercise apps, so if you do use exercise apps, let me know. See if

**Dave Jones:** anyone's using my technology that I invented in 2007. Are they embedding voices into and mixing them with the MP3 files? Cuz I'd have to read the whole patent, the exact wording of the patent again, and see exactly what I was uh

**Dave Jones:** claiming. So, you know, it's it's very specific wording. It's It's not that hard to get around patents if you know what you're doing, especially if you're a big company and things like that, but And so, you got to be, you know, very

**Dave Jones:** like it goes on and on. There's like like I don't know, 24 claims. Like No, there's more. There's like 30 claims or other things. I don't know. I don't know whether or not it would have been uh granted. You don't know until you go

**Dave Jones:** through, and you spend a couple of years and wait um and things like that, and here's the uh and here's some jazzy diagrams to Typical patent stuff, you know, the flowchart of how it works and things I love it. Look at all that. Like that's

**Dave Jones:** that's just pure wankery, you know. Anyway, that's what uh patent attorneys do. They just, you know, turn your good idea into gibberish and useless, you know, incomprehensible diagrams and stuff like that. But, yeah, basically, um whether or not it would have been

**Dave Jones:** like worth anything, I think it probably would have been easy to uh avoid it um in terms of like an app avoiding it in terms of uh it just like it just speaks it speaks it directly. It interrupts your audio stream and just

**Dave Jones:** boom, you know, you're not joining them, you're not doing it, saving as an MP3, and and you know, doing stuff like that. So, it it probably would have been easy for any app to overcome this patent, but you just never know. And then, of

**Dave Jones:** course, if uh some company did actually uh like technically I what I thought would have been violating my uh patent even if it was granted, what am I going to do about it? Like, I'm a one-man band. A typical to win a

**Dave Jones:** patent case costs several million dollars minimum. Like, it's not like you can do it for you can go to your local lawyer and say, "Hey, I'm going to sue him for patent infringement." And it's going to cost you 10 grand, 50 grand,

**Dave Jones:** 100 grand, 200 grand, half a million. Pah, nah. That'll just buy you lunch with the partners. No, forget it. Um it's going going to cost you a couple of million bucks to win. Of course, you can try and and then it becomes the whole

**Dave Jones:** patent thing. If you can, you know, try and uh tell them, "Hey, look, I've I've got this. I'm threatening to sue you." You know, you can send them a cease and desist letter or whatever. "You're violating my patent." They just might

**Dave Jones:** go, "Screw you." You know, especially if it's a big company. Ha, sue us. And what do you Yeah, you just have to walk away with your tail between your legs. So, the idea of the patent actually being worth anything would have been

**Dave Jones:** from the point of view of a company going, "Oh, this is rock solid. You know, this is like we can't get around this. This guy owns this technology." And you'd have to, you know, hope that uh some biggie buys out your patent or

**Dave Jones:** licenses or whatever and I I really didn't see see that happening. So, yeah. Just didn't seem worth it. So, yeah. Could have been rich, but most likely not. Anyway, if you've got an interesting uh similar story about a patent, something

**Dave Jones:** you tried to patent and it was just or maybe an idea for the uh you know, a good idea at the wrong time, let us know in the comments. So, anyway, hope you enjoyed that little story. Let me know your comments down

**Dave Jones:** below. Catch you next time.
