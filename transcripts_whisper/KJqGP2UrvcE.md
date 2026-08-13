---
video_id: KJqGP2UrvcE
title: Synology RAID Setup
url: https://www.youtube.com/watch?v=KJqGP2UrvcE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 57, "4": 77, "5": 102, "6": 118, "7": 134, "8": 154, "9": 170, "10": 186, "11": 203, "12": 223, "13": 247, "14": 267, "15": 296, "16": 317, "17": 337, "18": 349, "19": 365, "20": 381, "21": 401, "22": 422, "23": 438, "24": 458, "25": 474, "26": 494, "27": 518, "28": 530, "29": 551, "30": 567, "31": 587, "32": 603, "33": 628, "34": 644, "35": 664, "36": 688, "37": 709, "38": 733, "39": 762, "40": 787, "41": 807, "42": 831, "43": 857, "44": 877, "45": 905, "46": 929, "47": 949, "48": 986, "49": 1006, "50": 1035, "51": 1059, "52": 1075, "53": 1107, "54": 1131, "55": 1160, "56": 1180, "57": 1209, "58": 1237, "59": 1266, "60": 1290, "61": 1306, "62": 1326, "63": 1346, "64": 1375, "65": 1403, "66": 1415, "67": 1432, "68": 1456, "69": 1468, "70": 1500, "71": 1528, "72": 1557, "73": 1585, "74": 1606, "75": 1638, "76": 1659, "77": 1691, "78": 1707, "79": 1727, "80": 1744, "81": 1768, "82": 1788, "83": 1808, "84": 1833}
---

**Dave Jones:** Check. Checkity-doo-dah. Am I up? Yes, I think I'm up. Just thought I'd record this. I don't know. Why not? Got nothing better to do. Yes, I do. Anyway, I just got one of these new Synology, what is it? A DS418 RAID drive. Wasn't particularly cheap.

**Dave Jones:** I could have got a cheaper solution, but I also could have got a much more expensive solution. Anyway, let's get started. Anyway, I thought I'd set it up, because I've got an older Netgear. It's a ReadyNAS Duo V2 and it's been okay. I've got two 2GB hard drives in there

**Dave Jones:** set up as a RAID 1 configuration, and it's worked okay, but recently it's not mapping properly. It's not mapping as a drive, and it's old, it's not supported anymore. I don't know, Netgear just dropped support for it. I don't know how old it is.

**Dave Jones:** Anyway, it's a ReadyNAS Duo V2. I don't think it's the one with the Intel processor. There's one with and without. I don't know. Whatever. Anyway, I thought I would get a Synology 4 drive RAID system, mostly to store all my working stuff on.

**Dave Jones:** And yeah, I thought at the moment I've only got two 6GB, gigabyte, it keeps saying gigabyte. David keeps laughing at me over there. I'm old school. Two 6TB Western Digital RAID drives. Not the RAID Pro, just the regular RAID. Don't need the Pro I don't think.

**Dave Jones:** Anyway, I thought I'd just set it up here. Came in a box with just instructions to turn it on. I don't know, I haven't used Synology before, but quite a lot of people tell me, yeah, you know, it's one of the ones to get along

**Dave Jones:** with QNAS or something as another brand. Either of those are fine. And of course there'll be the fanboys out there, what did you buy that heap of crap for? Use FreeNAS and use all those dumpster PCs and set up FreeNAS. No. I don't want another stinking hot power hungry

**Dave Jones:** space hogging PC here. I just want something that just sits here, it's nice and quiet, it's energy efficient, just does its job in the background, dedicated, the right tool for the job, beauty. Alright, so anyway, so it's expandable, so I've got the two 6GB, I'm going to

**Dave Jones:** set them up and I'm going to use the, I can't remember what it's called, we'll find out in a second, the Synology's own RAID system, instead of the traditional RAID 1, RAID Xeon, all that sort of stuff. It's more flexible, apparently, and everyone recommends

**Dave Jones:** it, so I'm going to use that. And so when I install more drives later, it should just add on, it should just work. So let's set it up, it's detected, I've plugged it into my LAN, into my router, I've got a 1GB LAN router-y thing, modem-y thing.

**Dave Jones:** So let's go set up. And it took like 30 seconds or a minute for it to, like it was booting, the power LED was flashing, but now I'm getting a flashing status light, and two greens on disk 1 and disk 2. Install Disk Station Manager.

**Dave Jones:** DSM is the operating system running. Install the latest DSM for new features. It's out of the box, but yeah, okay. Install now. All data on the hard disk will be removed during installation. Whoa, that's a bit mean. I understand. Okay, because they're brand new drives, that's

**Dave Jones:** okay. Could take a while. Anyway, I'm not going to edit this, this is just a crap second channel video. My camera wasn't horizontal, it was disturbing me. A lot of people ask, where do they get the cool poster in the background? Yes, it is freaking awesome.

**Dave Jones:** Just search for Chart of Electromagnetic Spectrum poster, and you'll get it. It's on a Flickr account from, who did it? Bell, was it Bell Labs or somebody? They're the ones who scanned it in. Anyway, it's available in high res, that you can print on an A0 like this one.

**Dave Jones:** And it's beautiful. It's beautiful. So yep. We were 10 minutes. Please do not turn off the power during the procedure. Geez, I should have done a live show. I should have streamed this live. Anyway, ooh, I haven't seen 192.168.20 before. That's new. I don't know, is that a thing now?

**Dave Jones:** .37? Colon 5000? I don't know. Whatever. As long as it works and keeps on working and I don't lose mapping and all that sort of stuff. So what is Disk Manager? Disk Station Manager, it obviously installs on the drives. Oh yeah, okay, it's formatting system petition.

**Dave Jones:** But I thought, you know, it hasn't asked me what format I want yet, what sort of configuration I want. I guess it has its own low-level thing. Right? I don't know, I'm kind of trusted. I liked the RAID 1 stuff, because it was like,

**Dave Jones:** if the whole thing just shat itself, you could take the drive out and you could just read it in another machine. You know, you could read one of the drives and they were identical mirror images of it. This one you sort of have to trust the RAID.

**Dave Jones:** You know, I don't know. Yeah, if it fails, that's the idea. You've got one disk, I'm going to have at least single disk redundancy on this. You can configure it so you can have multiple disk redundancy, but I don't maybe you want that if you've got, you know, 8 or 16

**Dave Jones:** array ones which you can buy, you know, big huge monster ones. But I don't need anything like that. It's good enough. I'll probably still store most of my RAW footage, because I keep all my RAW footage. I've currently got 3 or is it 4

**Dave Jones:** 2TB drives with all my, I think it's 3. 3 2TB, here it is, look. You know, like yeah, that's it. I haven't put them away yet. But yeah, I just store them on, you know, that's RAW from video 950 onwards, and then I've got another one that has

**Dave Jones:** 9, what is it, you know, up to 950 from 600 to 950 or something, however much fits on a 2TB drive. And I always get two different types. So I've got a Seagate and I've got a Western Digital. And they just contain identical stuff, and then I keep

**Dave Jones:** them at different locations. Although obviously not with this one. But that's the idea, is that two different brands, so if there's some sort of hardware fault with one of them, then I can, you know, some sort of systemic hardware problem, then it shouldn't

**Dave Jones:** affect the other one. You know, it's more, it's unlikely to affect the other one. So, there you go. Yeah, it's not perfect. I mean, no backup thing is perfect. This Synology one should be able to sync, also sync cloud backup, if I want

**Dave Jones:** cloud backup to my Backblaze system, which I use for just backing up my local drives here in this machine. I back them up, but they don't actually back up the drives, they just back up the files. They don't actually back the drives up.

**Dave Jones:** Like, as in like a mirror image type thing. So, it's kind of annoying, especially your boot drive. It's just kind of annoying. I thought Backblaze did that originally, but it doesn't. Anyway, in approximately 10 minutes, please do not turn off the power during this procedure.

**Dave Jones:** Gee. Eat my lunch or something. It's almost lunchtime. Geez. So yeah, it's a raid. I know, like, I see all these people, you know, every time I talk about raid, oh yeah, I've got a 8 disk raid array with 8 disks of 8 terabytes each or something.

**Dave Jones:** And it's like, God, what are you doing? You know, I'm a professional video blogger storing all my raw footage, and I'm just dicking around with a little pissant 2 drive 6 terabyte thing, you know. And it does the job. And they're like $5,000.

**Dave Jones:** People think nothing of spending $5,000 on a, you know, $3,000 or $5,000 on a raid system. It's like, wow. Okay. But yeah, I didn't skimp this time. I bought, you know, I upgraded, I got the 4 drive, well, for me I didn't skimp.

**Dave Jones:** I got the 4 drive 1, so it's expandable. I got the proper red raid drive arrays, whereas before I've never used those. I've always just had you know, generic consumer crap. I didn't get the pro, because I was a bit tight ass. The pro is apparently the same, but

**Dave Jones:** just a bit faster or something. Which probably isn't a big deal. I think, yeah, I think the regular Western Digital red drive I've got is fast enough for the throughput of this DS418 raid drive anyway. So buying the pro and putting it in here

**Dave Jones:** wouldn't have helped much. I think there might be some longer term reliability things with the pro. I'm not sure. What are they filled with? Maybe some special type of nitrogen pixie dust, you know. Or something. Make some special, here we go, restarting your disk station.

**Dave Jones:** What? It's not going to take 10 minutes to, really? It's going to take 10 minutes to restart? Oh man. That's hopeless. Terrible mural. The power LED's flashing. It's just like all the other LED's have gone off. Status, disk 1, disk 2, and they're

**Dave Jones:** I don't know if I should touch it. Probably shouldn't, right? It's flashing its blue power LED like it was booting. So maybe, yeah, it must be doing something in the background. I better not touch it. I don't want to record for another 10 minutes.

**Dave Jones:** I'm going to do something else. More productive. Anyway, yeah, maybe I'll come back. In that case I've got to edit this video. Dammit. Yeah, I'm not waiting here for 10 minutes. If it was live then I could at least interact with people, but it's not live, so

**Dave Jones:** there you go. Boo. Boo hoo. Alright, I'll be back. Oh no, I can pause it! Hang on! I can pause it! Pause local recording. Ha ha! Yay, XSplit! Awesome function, I hardly ever use it. There you go. Now we're resumed. It didn't take 10 minutes.

**Dave Jones:** Create your administrator account. Low info will be used to manage your Synology DS418. Okay. Oh, it's password strength. Oh, minimum password. Exclude name and description of user from minimum password length 6. Good, I hope they don't force you to use all the mixer characters and all that sort of bullshit.

**Dave Jones:** Um... Should I share the network location of your disk station with Synology to help you easily reach your disk station in the local network via findSynology.com? I don't see any advantage to doing that. Like, I know where it is, it's right here. It's plugged into my computer.

**Dave Jones:** Um, no. Okay, server name. Ooh, okay. I'll set this up and get back to you. Congratulations, you have set up the administrator account. Please complete the following steps. Install the latest DSM version automatically. Install the important updates of DSM automatically. Typically fixes for security vulnerabilities.

**Dave Jones:** Yeah, well that sounds good. Install the latest, oh, important updates, download the DSM updates and install them manually. I guess the first option, right? Install the latest DSM automatically. Let it do its thing. Okay, so install the latest DSM version automatically every Monday and Thursday at 1 o'clock.

**Dave Jones:** Whatever. Yeah, that's fine, yes. It is set for 1. Yeah, it's set for 1am. Yep, yep, it's, yep, that's a 24 hour clock. So Monday and Thursday, fine. Run smart test to check the health of my hard drives periodically, because that sounds good.

**Dave Jones:** Will be tested to perform, yep, extended test will be performed once every month. Oh yeah, why not? Enable bad sector warning for drives. Oh yeah, that sounds alright. And then 50 bad sectors. Yeah, why not? Why not? Quick setup, quick connect. Without port forwarding.

**Dave Jones:** Do I want to set up, create a quick connect ID with new Synology account? I can use it from home. That sounds good. That sounds good. I'll set this up and get back to you. Install Synology's recommended packages. These packages will help you get started with DSM effortlessly.

**Dave Jones:** Hyperbackup, cloud station server, media server. I don't want all that crap, really. I don't do the media server thing. I don't play video, I don't stream videos from it, like, I don't, I just use it to store my working files and stuff. So I don't,

**Dave Jones:** I can download those later, surely. So what's download station? Download station sounds alright. Cloud station server. Yeah, David's looking for me. What's Synology cloud station server? I'm on download station still. What's download station? Download station is something that allows you to download files from the internet

**Dave Jones:** through FTP, HTTP, etc. On the device itself. That sounds alright, yeah. Seems like that's what it means, yeah. Okay, yeah, alright, I'm going to install that. Ah. You can download torrents into it. Oh, hang on, it looks like I've got to install them all?

**Dave Jones:** I don't know. By confirming you agree to be bound by the terms of service. Bloody hell. You're saying don't use it to download illegal stuff. Right, yeah. Alright, well, it looks like you've got to, let's take the quick guided tour of DSM. Oh, no, I'm not sending

**Dave Jones:** anonymous statistical data. No. Quick guided tour. Access all built-in and installed packages from the main menu. Alright. Ah. Yeah. Yeah. Discover more applications at package centre. Control panel. File station. ... There we go. Good. System health. Your disk station is working well. Well, I'd hope so.

**Dave Jones:** Just installed it. Uptime. 40% of the CPU. Oh no, it just went down. And the LAN. Alright. Comprehensive. Is that good? Is that like real data? Or is that just simulated? Did not automatically launch DSM help at every login. Yeah, I don't need

**Dave Jones:** help at every login. Media service successfully installed. Download station successfully installed. ... Okay. It's doing stuff. It's doing stuff. Right. Okay. All I wanted to do was appear as a drive on Windows, you know. That's it. I don't really care about the back end stuff.

**Dave Jones:** Right. DSM help. DSM get started with DSM. Learn how to implement essential DSM features. Nah. Okay, it's still installing packages in the background, that's why it's spiking. Yeah, this must be real, this must be real data. Your disk station is working well. I'm so pleased.

**Dave Jones:** I hope that, like, LAN IP address stays static or whatever. I don't know. Like, I know you can, like, fix that sort of stuff in the router and ... Oh, okay. Hyper backup. All the packages are ... Does that mean it still has one left to install?

**Dave Jones:** Probably. File station. There you go. All right. File station. Yes, I'm a dummy. I have not used a Synology thing before. Cloud station. All right. Home. Individual at volume one. 5.41 terabytes. Hey! Where's the rest? 6 terabyte drive. Photo, video. Like, I don't

**Dave Jones:** categorize my things into things like that. I have my own directory names. I mean, you know. Cloud station. List of ... right. SynRAID. Like, do I have to use these subdirectories? Surely not. Upload. Skip. Overwrite. Right. Okay, just very basic. A web-based thing.

**Dave Jones:** So I can get in via this, presumably. Shared links. Mount list. Mount remote folder. All right. And settings. Enable file station log. Oh, that'll grow, won't it? Enable drag-and-drop between browsers. Enable smart drag-and-drop. Why wouldn't they enable those by default? Mount connection. Shared

**Dave Jones:** links. Administrators. Administrators. Remote folder. Virtual drive. Okay, so I can set up users. That's cool. No speed limit. Nah. Ah, plain text. All right, yeah, whatever. Oh, well, that's boring, isn't it? Now what do I do? Like, how do I access my Synology drive as a...

**Dave Jones:** like, where does it like, which format am I in? Which RAID configuration? They said I could choose this and stuff. Resource monitor. Storage manager. Probably storage manager. Sounds like the go. Yeah, here we go. Now we're talking. Let's get rid of that rubbish.

**Dave Jones:** All right. Volume 1. Used up 1%. Disk group. Right. There we go. Normal. 5.5 terabytes. Health info. Yep, I'm sure they're healthy. 30 degrees. I can hardly hear it too. Hang on. Yeah, it's pretty silent. It's got two big fans on the back of it.

**Dave Jones:** Pretty happy with that. I think it was like 26 dB or something. 26 dBA was the noise level. So, all right. I have no idea what iSCSI is. Intelligent SCSI. Intelligent SCSI. There is no iSCSI thing. Okay. That makes sense. There are no disk groups in your system.

**Dave Jones:** What's a disk group? Volume. RAID type. SHR. RAID type. Ah, yes. Oh, yes. Synology Hybrid RAID. That's it. That's the acronym. Yes, so by default it used that. That's what I wanted. Synology Hybrid RAID. With data protection of one disk fault tolerance. Yes, so if one of these disks fail, I presume the red light will come on, and then I just swap it.

**Dave Jones:** Because it's failed. Put a new one in. And after re-syncing and re-doing everything, it should come good again. Because the odds of two failing at the same time, jeez, you'd have to have a lightning strike or something. You know? Like, you'd have to be really smart.

**Dave Jones:** You'd have to be really serious. Optimizing file system. Yep. Shut down or reboot it now. Thank you. Jeez, well that was pretty quick and easy. And I guess that's done. That's done. All I need to do now is see if I can access

**Dave Jones:** this puppy via if I go to network, there's a media, it's showing up as a media device. Other devices. Yeah, a Synology RAID. If I double-click on it. Oh, there we go. Yeah, it pops up. Okay, so I double-click on it, it goes to the IP address

**Dave Jones:** of where I was before. And it's shown up as a media device, so presumably I can... No, that's the same thing. All right, now I've got to figure out how to map it as a drive, because that's what I want to do. I want to map it as a

**Dave Jones:** Windows drive. Huh. Open media player, create shortcut, view device web page. Welcome to media play, no. That's Windows is treating it as a media player. I don't care about that. All right, I'm going to have to get back to you. It's working. It's set up as the Synology Hybrid RAID, which is what I wanted.

**Dave Jones:** One disk fault tolerance, it's all raring to go. I'll try and figure this out. It's not obvious. Like, it probably is to those who have set it up, and you're all probably laughing at me. I don't care. I haven't done this before. Hmm.

**Dave Jones:** All right, I'll get back to you. All right, here we go. Store files to Synology NAS from a Windows PC within the local network. That's what I want to do. Why doesn't it do this by default? I don't know. Like, how else would you use it?

**Dave Jones:** Okay, I can maybe drag things as a media device or something, but like I don't know. It's designed to make storage easier. It's designed to make storing and sharing files within your local network quick and simple. Well no, it's not, because you didn't offer to map my drive when you

**Dave Jones:** set this thing up. Allowing you to directly access files in the system without going through the hassle of logging into DSM every time. Yeah, why would anyone want to log into DSM? That's just dumb. With Windows Explorer, just like any other network drives.

**Dave Jones:** Of course! Why this is not default? I don't know. Open a Windows Explorer window and go to computer. Okay. Hang on. Computer? No, I don't have computer. I've got this PC. This must be old. This is not the new Windows 10, is it?

**Dave Jones:** Anyway, computer. Map network drive. Of course! I know that. Network and sharing center. View device website. Add devices and printers. No, I don't connect with No, I don't have that. Hang on. This PC. Map network drive. Ha! There it is. Yeah, sorry. It's obvious.

**Dave Jones:** Yeah, I knew that. I've done that once before. Map network drive. Drive letter. Okay, I'm going to... X. X sounds good. It's the X files. The X files. Example. Connect folder. Specify the drive letter folder you would like to connect, and the folder

**Dave Jones:** you want to connect to. Well, browse. It's not showing up as a network device. No, I can only... No! It's not showing up. There's only other computers on the network. Map network drive. No. It's not showing up. I won't show you the list, but it's not showing up.

**Dave Jones:** There's two other computers in this lab, and it's not showing up as either one of those. Diskstation. No, there is no option to get diskstation. That's a fail. That's a fail. Enter admin password. Fine. But it's not showing up on my list of...

**Dave Jones:** on my list of devices. Nah, epic fail. What's going on? I'll get back to you. Check it out. This is really interesting. Look at this. Right? It shows up here. EvlogSyn RAID. Okay? And there's the files. Okay, I can actually just drag and drop stuff to them now, presumably.

**Dave Jones:** That's fine. Which shows up under this PC, but then it doesn't show up under this side list here. The back... I've got another RAID system, which isn't connected at the moment. That's the Netgear one. And it shows up, but EvlogSyn RAID does not show up.

**Dave Jones:** Wow. And I can't map that. I can't, like, it's not like, you know, and if I map network drive, right? Map network drive, it doesn't show up in the list here. Nuts. Reconnect at signup. I've tried typing in manually. Doesn't work. Should I create a folder?

**Dave Jones:** No. Okay. I think what I have to do is type this in manually. I haven't tried it yet, but I think EvlogSyn RAID doesn't work on its own, because it can't connect to the root. So it's got to connect to, let's try slash video.

**Dave Jones:** Right? So let's try, I don't know, let's give that Y drive, for example. Finish. Attempting to connect. Hey! Now we're in. Alright. But that wasn't obvious. Like, it doesn't tell you, the help doesn't tell you to do that. In fact, it tells you, well,

**Dave Jones:** it doesn't tell you that diskstation is the name of the device. Oh no! Yes it does. For example, if the server name of your Synology NAS is diskstation and the name of your shared folder is share1, nah. It's there. I didn't read the instructions.

**Dave Jones:** Oh! And oh! That was embarrassing, wasn't it? Okay. Yeah, I kind of done this before on the Netgear one. It did the same thing. You've got to create the directories you want, the shared directories you want inside the disk manager thing, the Synology disk manager, and then

**Dave Jones:** use those as mappings for individual drives. So I've already got video so I could have like, you know, documents or something, you know, like, or whatever. Anyway, so yeah, we've got, where is it? Controlled file station. Here it is. Yeah. So we've created, yeah, music, photos, and videos.

**Dave Jones:** Right? And we can create a new folder. Okay. That's where we have to map it. Um, alright. Fine. But it's ridiculous, because I've got oh no, no, no, I'll drag it. Nah, it's okay. I've already stored my stuff in slash video subdirectory, so I thought it'd be

**Dave Jones:** slash, thought it'd be video, video, but it won't be. It'll just be video. So, okay. Alright. I'm good. So there you go. That's setting up a Synology RAID system. That was pretty easy once you know and if you actually follow the bloody read stupid instructions, as I am

**Dave Jones:** famously known for not doing. So there you go. Alright. That's it. Tell me below that I'm a dickhead because I don't read stuff, and that I'm a dickhead for buying a Synology RAID. Go for it. Catch you next time.
