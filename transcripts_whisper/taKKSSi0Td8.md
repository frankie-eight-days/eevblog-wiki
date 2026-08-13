---
video_id: taKKSSi0Td8
title: Synology NAS FAIL Adventure
url: https://www.youtube.com/watch?v=taKKSSi0Td8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 39, "3": 54, "4": 75, "5": 90, "6": 106, "7": 125, "8": 140, "9": 155, "10": 170, "11": 183, "12": 199, "13": 213, "14": 227, "15": 245, "16": 263, "17": 278, "18": 293, "19": 310, "20": 324, "21": 337, "22": 351, "23": 362, "24": 381, "25": 400, "26": 423, "27": 442, "28": 464, "29": 478, "30": 498, "31": 512, "32": 530, "33": 548, "34": 567, "35": 583, "36": 601, "37": 613, "38": 627, "39": 640, "40": 654, "41": 664, "42": 680, "43": 695, "44": 707, "45": 720, "46": 731, "47": 744, "48": 758, "49": 772}
---

**Dave Jones:** Hi. Yes, it is fail time on the Synology NAS, the DS418 here. Now, if you've been watching for a while on my second channel, I'll link it in if you haven't seen it, one of the drives in my four-drive NAS array here failed almost three years ago now.

**Dave Jones:** It was disk number three, and that was, you know, your traditional disk failure. They, you know, because they're up, they're running 24-7 and, you know, they eventually fail, and that's why you have a redundant drive. So I've got four 6-terabyte drives in here,

**Dave Jones:** so you get one is a redundant array, one is a redundant disk. So I've got 18 terabytes total here, and I do all my video editing on this, and it normally sits down in the dungeon, and I've got my 1-gig ethernet going down there,

**Dave Jones:** and all the, I do direct editing straight from this, no problems whatsoever. So yeah, that fire three years ago, the disk three just failed, and it started beeping, and the disk three lead went to orange here or something, and, you know, easy. Okay, you remove the drive, you know, and plug in a new one, hot swap,

**Dave Jones:** and then it rebuilds, it takes a day to rebuild the array. Bob's your uncle, right? I've had no problems since then. But last night, I was editing my video, and I've been fighting this problem for the last 24 hours, and I'll see if I can take you through the whole thing.

**Dave Jones:** Anyway, I did have a, I originally put a thread on Twitter, and then I moved it to Reddit, and people were helping me out there, because this is quite an unusual fault, right? So I was editing my video, and all of a sudden it started freezing and stuttering,

**Dave Jones:** and then I just couldn't edit my videos anymore. And then I discovered that the Windows share, like, subdirectory for all the, all my, you know, all my video, all my project files are on here, everything's on here, right? And I found that I couldn't access any of those whatsoever.

**Dave Jones:** And one of the unusual symptoms was, was that while I could actually get into the login in this, in the, like, the local IP address login, it had, like, it had actually take time to, like, you put in the local IP, it would take time, and it eventually, though,

**Dave Jones:** eventually, it would actually load up the login screen, okay? But when I, you know, put in my username and password to log into this thing, it said, okay, process impending login or whatever, and it would just sit there forever. I could not log into the thing.

**Dave Jones:** So I went down to the dungeon to take a look at the physical drive, and everything was hunky-dory. Status LED was green. All the disk LEDs here were green. But one thing I didn't notice at the time is that disk one was, you know, flickering just a little bit,

**Dave Jones:** but I thought that was just, like, normal, you know, normal operation. It was, you know, trying to do its reading or whatever. So no problem, but everything was green. Everything was green. So I thought, oh, haven't got any disk failures. What's going on?

**Dave Jones:** So some people said I should try to SSH into this thing. I tried that. No, couldn't do it. Exactly the same problem. I was getting error messages telling me, like, I couldn't log into this thing. And then, of course, the next thing you do is, well, try to turn it off and on again.

**Dave Jones:** Hello, IT. And so I tried to switch it off. So you hold it down, and, you know, normally the power LED flashes, and it shuts down after 10 seconds or whatever, you know, 30 seconds or whatever. But it didn't. It would not shut down.

**Dave Jones:** It would just continually flash the power LED. So if I left it for, like, an hour, the thing wouldn't shut down at all. So I eventually went, oh, screw this. I'm doing a hard power reboot. So I do a hard power reboot, and it comes back up,

**Dave Jones:** and eventually, it took a while, but eventually, same thing. All five status LED green. All four drive things are green. And I had the same login problem. The screen would show up, which means that the processor in here was working. It was generating that login page that, you know,

**Dave Jones:** it was rendering that login page and everything. But it was incredibly slow. And then it just simply would not log in at all. So I'm like, what the hell's going on? I'm thinking, oh, okay, maybe a power supply issue, but that kind of doesn't, you know, because it uses one of these external power brick things.

**Dave Jones:** But that doesn't explain why it would, like, have a proper login thing, and all the LEDs are green, and, like, at least, like, it was like the processor was doing something. And then, of course, I thought about the C2000 bug. I'm not sure that that's a problem with this one,

**Dave Jones:** but that was a problem where it just wouldn't boot up at all, whereas mine was booting up to at least five green LEDs here. So, yeah, it was kind of all unusual. Anyway, I have a spare power brick somewhere, but I couldn't find it, of course, bloody Murphy.

**Dave Jones:** So I couldn't test that at all. So the next thing is I brought it up here to lab, and I threatened it with physical violence. So I plugged it in to my local Ethernet here, and I used findsynology.com, which is a thing which, like, finds your drive locally or whatever.

**Dave Jones:** It's a little script that finds it because it might have been a new IP or whatever. So it found it, it detected it, and it tried to take me to the login screen, but it wouldn't. It wouldn't. It wouldn't load at all. And, like, what's going on?

**Dave Jones:** So that's when I noticed that disk one here was... it was green, but it was, like, flashing a bit, and the other ones were solid, like they're doing now. You know, they might flash, you know, really, like, well, occasionally you just saw it then,

**Dave Jones:** but disk one was, like, flashing a little bit more than the others. So I thought, okay, and my spidey sense was telling me that disk one might be dodgy. Anyway, so I took all the drives out, and then I repowered the thing cold.

**Dave Jones:** I booted the thing up, and I found that it booted up, and it went to orange, of course, which is to expect when you have no drives or whatever, and it's not set up. So I managed to boot it up. So what I did is I put all the drives back in.

**Dave Jones:** I think I just hot-swapped them back in. And then I used find-synology.com again, and it found the IP address, and it then... rather than take me to the login screen, though, it took me to, like, the factory-fresh welcome. You know, prepare to set up your Synology drive.

**Dave Jones:** And it's like, oh, what the? What the? Like, these were my, like, proper drives in the correct slots and everything. And, like, I'm going, well, I don't really want to proceed with that. So, um, yeah, nah. So what I did then is I pulled that maybe-suspect drive one out here.

**Dave Jones:** So what I did then is I pulled that maybe-suspect disk one over here, and then all the other three drives started going flishy-flash, flishy-flash, and you know, doing their thing, like, aha, this drive was causing the processor in here to sort of lock up, like it was waiting for a response from it,

**Dave Jones:** and it just couldn't do it. But why it was still showing green and everything, I don't know. But that seemed to be the culprit. Once I actually removed that first disk one over here, then these disks started doing their business. So I cold-powered the whole thing, and I put drive one back in,

**Dave Jones:** cold-powered the whole thing again, and then eventually, I waited some time, and eventually I finally got to the traditional status of orange status LED here, which means something's wrong, and an orange disk one LED, so disk one is failed. But, then, I still couldn't log in.

**Dave Jones:** So I used for, you know, that IP address that findsynology.com gave me, and it would not have a login screen. There was no login screen. So then I was able to pull disk one out, and eventually, I waited, I actually went home, and I came back in the morning,

**Dave Jones:** and I was able to access my files, no problem whatsoever. All my Windows shares were back, everything's hunky-dory. But then, yes, there's another struggle. I used that IP address that findsynology.com gave me, says it has detected it, and here's the IP address, and the port and everything, Bob's your uncle,

**Dave Jones:** log in, but I get no login screen. No login screen at all, right? It's just like, can't find it, or whatever. So I'm going, oh, what the hell, but I can access all my files. So the RAID was back up and running, and it was just in a degraded state,

**Dave Jones:** so I had no backup drive now, but I could access all my files, because I still had three good working ones. So, yeah, I couldn't log in. And then I discovered that findsynology.com was give, even though it detected it, it was giving me the wrong IP address.

**Dave Jones:** I went back to the original IP address I had when I had it downstairs, and bingo, Bob's your uncle, there's the login page, super quick, log in, boom, and I'm back. So, oh, that's like, unbelievable, unbelievable. So anyway, I'll take you over to the login screen now,

**Dave Jones:** and you can have a look. Alright, you can see here from the system log here that there were read errors on the internal disk, and sure enough, disk 1 there. But why this thing, like, just seemed to lock up, or go incredibly slowly, at least render a login screen,

**Dave Jones:** but it is still display, like a green indicator for LED 1? Like, that really sucks. And now it says there's a file system error was discovered, do you want to reboot and run a file system check? I guess I should do that. Could take a while, so I'll probably do that first,

**Dave Jones:** and then I will go into the recovery thing for the actual drive. So, yeah, it's in a degraded state here, Synology drive degraded, available slots. So as soon as I whack that other one in, it's just your regular thing, when your drive fails,

**Dave Jones:** you just put in a brand new drive, which I do have. I ordered a spare way back. Yeah, so I've got a spare one there, just sitting, waiting for this to happen. So, yeah, hopefully it's still good. It's been sitting there for a couple of years,

**Dave Jones:** but it should be good to go. So yeah, I'll whack that in, and so I'll run that, system check, and then I'll do that. But yeah, bloody Synology. Why would it, like, continue to operate like that? And, like, just because, okay, the drive's got,

**Dave Jones:** once it got a bad read error, right? It should have shown up yellow. It should have gone yellow. Okay, degraded state, warning. And it said it failed to send an email. Apparently I can send emails to me, and it couldn't do it for some reason.

**Dave Jones:** I don't know, have to check on that. But yeah, it should beep, and it should, you know, at least turn the status thing orange, so that you can see that something's wrong, and then it should not hang up. There should be, like, a timeout thing on that drive.

**Dave Jones:** It shouldn't, you know, yeah, okay, the drive is completely screwed up, and is, like, hanging there, and it's waiting for a response from it. I presume it's something like that, and it just never got it. There should be some sort of timeout there,

**Dave Jones:** and then just ignore that drive, and say, hey, there's something wrong with that drive. Replace it. And, nah, but it doesn't do it. And I know, go ahead, in the comments down below, go, you've got to use TrueNAS. You've got to use a DB and Linux environment in TrueNAS,

**Dave Jones:** and you'll never get this problem. Go ahead. Go ahead. Go. Go. Do it. You know you want to. And then there's the other type of person in the comments down below, so I have to use comment voice. Dave, didn't you know that NASs aren't true backups?

**Dave Jones:** So you've got to have a proper backup solution. Well, go ahead. Write that down below. I know you want to as well. Get it out of your system. Get it out. No, this is my working drive. I do not use this as a backup.

**Dave Jones:** I actually have an automatic cloud backup, so I wasn't worried about losing any data on this. Would be a complete pain in the ass if this NAS went down. It'd take me a long, laborious process to get all the data back, download it from the cloud,

**Dave Jones:** and write it on new drives, and do whatever, right? It'd be a long and expensive process, but I could still do it, so I wasn't worried about losing data on it. It's just losing daily, like, downtime like this. I've basically lost a day's work on this.

**Dave Jones:** I was supposed to have a video finished and released yesterday, and now it's like, ah, I just got back in from a fire alarm. So, you know, what turns out, that was a fake. It wasn't a fire alarm. It turns out it was a glass breakage alarm

**Dave Jones:** on the front door of the building, because I went down to the fire panel, and I had a look, and that actually had proper status, and it told me that it was a glass breakage alarm in the foyer, and sure enough, these guys, they're working on the foyer doors,

**Dave Jones:** because they were broken down somehow, so they were repairing them, and they must have tripped the glass breakage sensor on there, and the whole building gets evacuated. So that's my day, and then I got the bloody appointment at 12 o'clock, and then I got this,

**Dave Jones:** and then that, and oh, God, and then, oh, isn't tomorrow a public holiday? No, not for me. Anyway, catch you next time.
