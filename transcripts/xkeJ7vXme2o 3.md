---
video_id: xkeJ7vXme2o
title: Laugh as Dave FAILS to Install pfSense
url: https://www.youtube.com/watch?v=xkeJ7vXme2o
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 26, "3": 40, "4": 55, "5": 68, "6": 81, "7": 95, "8": 108, "9": 121, "10": 134, "11": 148, "12": 158, "13": 172, "14": 183, "15": 198, "16": 214, "17": 236, "18": 253, "19": 266, "20": 278, "21": 292, "22": 310, "23": 327, "24": 340, "25": 361, "26": 380, "27": 397, "28": 413, "29": 431, "30": 452, "31": 468, "32": 484, "33": 500, "34": 521, "35": 540, "36": 555, "37": 569, "38": 582, "39": 601, "40": 621, "41": 634, "42": 659}
---

**Dave Jones:** Hi, I'm going to be doing some penguiny stuff today. And you know what an absolute guru I am with penguin computer stuff. Um, I'm going to be repurposing this uh BeeLink, which you've seen in the mailbag, the EQI12.

**Dave Jones:** I do have a lower power one. It's like an N150 uh processor one, but I can't find it. It's here somewhere. So, anyway, I'll use this. I think this is an Intel i5 uh jobby. Pretty powerful little beast. Don't need this much

**Dave Jones:** power. But what I'm going to do today is I'm going to install uh PF Sense on this, which is a firewall, and I'm also going to use it as a VPN as well. So, um I probably won't show you all the

**Dave Jones:** details of setting this up, but I thought I'd give it a go. So, I have been assured that PFSense is the duck's guts, and it's going to uh provide me with more better security and also VPN, uh capability as well for my entire lab.

**Dave Jones:** So, um, yeah, I've downloaded PFSense onto a stick here, uh, using Baliner Etcher because I'm such a PC guru. I know how to do this. And this is what I've currently got at the moment. I've got my fiber to the premises. Fiber

**Dave Jones:** comes straight in. I've got my NBN uh modem thing here, which has four ports on it, but I'm only using one. And that goes into my uh Wi-Fi routery uh thing that is very ancient. Um, so yeah, sec

**Dave Jones:** security vulnerabilities there. Um, and then that goes into a dumpster um, TPLink uh, switch here, 16 channel switch, which then goes out to all the ports, including my uh, NAS as well. And I edit all my videos from my NAS.

**Dave Jones:** Actually, people think, you need a solid state drive, really fast solid state drive on your machine you're editing on. No, I edit all my videos, including 4K, directly from the spinning NAS. None of that solid state rubbish spinning NAS

**Dave Jones:** here. Um, then I've got various PCs, including my editing PC and my lab PC and my shipping PC and other stuff. Um, and then I've got things connected up to the uh Wi-Fi. And I'm only using one output from the Wi-Fi router here. And

**Dave Jones:** then I've got that going 100 meters down into the basement into my dungeon. Um, I've got another uh switch down there. I've also got another Wi-Fi access uh point down there. And I've got various uh uh things. I got a backup PC down

**Dave Jones:** there and other things connected up down in my dungeon. So, what I'm going to do is I'm going to put uh this new PFSense box between the uh modem here and uh then and and the switch. So, my Wi-Fi

**Dave Jones:** router I'm going to move um over to one of the ports on the uh switch that has been recommended uh because I don't want that in the way. I just want that to be like an access point uh thing. And then

**Dave Jones:** the PFSense box uh that will handle the uh DHCP stuff. And I've been assured that this is the ducks cuts from a security point of view. So, let's power this thing up and uh see I've I've got Windows 11 on

**Dave Jones:** here, but uh we're going to install uh a Penguin on here using I think PFSense uses uh the Penguin, doesn't it? And we're going to uh install that. So, I'll get back to you. So, going to the bias

**Dave Jones:** going to change my boot order uh priority here. So, option number one, let's boot from my USB device. It's found it. SanDisk partition one. All right, no worries. And after that, we just do number two as the Windows boot

**Dave Jones:** manager there. So, let's give that a B. Save and exit. Rebooting. Ah, boom. Straight in. There you go. Jeez, that was quick, wasn't it? Damn. Um, yeah. Okay. I've never done this before, but I'm an absolute guru at PC stuff, as

**Dave Jones:** everyone knows, so I totally know what I'm doing. Uh, and copyright trademark notices. Uh yeah. Okay. Fir firmware error. ACPI could not resolve symbol blah blah found blah blah firmware error blah blah. Whoa. So I pressed enter. Install pfSense. I got past that. Rescue

**Dave Jones:** shell. No. Install pfsense. What are the advanced options? Um yeah it keeps telling me that. So that could be a a boot thing. Bias thing. Continue installation. Save options. Uh yeah. Back. Okay. So, install pfSense. Um, yeah, that's just annoying

**Dave Jones:** because it just overlays that error there. But anyway, set up the network to continue. Setting up the network to continue the installation. At the moment, I've just got it connected uh to one of the ports on my uh uh switch

**Dave Jones:** here. So, I don't know if that's correct or whether or not I need to plug it directly into Whoa. Or whether or not I need to plug it directly into the modem. Maybe I should plug it directly into the

**Dave Jones:** modem, I'm thinking. H. So, I haven't shown it here, but uh this new uh PC I've connected directly to the modem over there just in case uh it needs that. So, can I bloody get rid of this? Just choose. Okay. Continue. Proceed

**Dave Jones:** with the installation. DHCP. No, I want the DHCP to be going on in here, but I assume I can change this all. Ah. Oh, hang on. No. Oh. Oh, I'm down. I'm down here in the prompt. Uh, mouse doesn't work. Okay. Oh, an

**Dave Jones:** installation step has been aborted. Would you like to restart the installation? Yes, restart. I'm down on the prompt now. Oh, this is ridiculous. I'll get back to you. Well, I just rebooted and started again. And I have to select the WAN interface, which is

**Dave Jones:** the wide area network, which connects to the modem. But I've got two Ethernet ports on this thing, which is what you need. Um but I don't know which one's actually what. So both of them just say no carrier.

**Dave Jones:** All right. So it said something about ACPI. Auto configuration is disabled. Enable hibernation. Enables or disability to hibernate. Uh no I don't. I want to disable hibernation. I suspect sleep state. Suspend RAM. Suspend disabled. Don't want any of that because I want this

**Dave Jones:** thing to run all the time. And I guess auto configuration enabled. Oh, okay. It was just suspend auto configuration enabled. I'll try that. Well, that didn't fix it. I'll set it to manual and that disable thing. Well, that's a nope.

**Dave Jones:** Exact same error. So, it doesn't I mean, that's what it says. Firmware error ACPI. So, I have no idea what that is. Uh something get I don't know. Um, yep. Yep. No idea, but it's just turned up the same error. So, I guess my dad box

**Dave Jones:** isn't um like out of the box compatible with uh the free BSD that uh this thing runs on. So, okay, I speed ran the uh thing before it Oh, popped up with an error message. Cannot reach the neck 8

**Dave Jones:** servers. Uh yeah. Okay, wonderful. I changed the Ethernet socket on the front and it looks like I'm getting active now. So I can choose that RE1. So proceed with the installation I guess and now it should find the server

**Dave Jones:** because there is Oh uh none do not assign the LAN interface, right? No, because we were RE1. RE1 had the connection. So do not assign the LAN interface. LAN RE1 active. Uh, please confirm the interface assignment to continue. Well, that's got active,

**Dave Jones:** right? So, we want that. And let's see if we can contact the servers now. Bloody cloud rubbish. Oh, yeah. This do not have a Yes. Plus subscription. I don't want that. Um, install CE. Yes. So, I want the uh Yes. I think C is

**Dave Jones:** community edition or something, I think. So, yes, I want install C. I don't want the plus. I don't want to purchase anything. I want the freebie. Proceed with the installation. Continue. File systems are recommended default. GPT partition scheme. Okay. Proceed with the

**Dave Jones:** installation. Uhhuh. Stripe. Stripe. No redundancy. Uh, yeah, whatever. Select the disk. Yep, that's the one. I want to override my Windows. Last chance. Are you sure you want to destroy the current Windows 11? Yes, I wish to destroy it.

**Dave Jones:** Committing the changes. All right. So, yeah, this message is just annoying. It's not stopping me do anything. Current stable version. Uh, yes. Yes. Current stable version. Oh, hang on. Whoa. Yes. Current stable version. Yes. Finally. Here we go. We're in like

**Dave Jones:** Flynn. I think 17 meg. Is that all? What? Hang on. This process will require 64 meg more space. Ah, why? I thought it was going to nuke the solid state drive. There's nothing there. I can't see under it cuz the bloody error

**Dave Jones:** messages. If there's anything under that, I just have to wait, I guess. Um, should have Yeah, updating. Yep. Okay. No, it's going. I don't know why it said it will require more space. Process require 100. Ah, okay. It looks like

**Dave Jones:** it's Yep. Right. Everything it needs to download. It just tells you it it's an incremental thing. It tells you it needs Okay, it needs another 121 meg. It's got that because it's nuking the drive, which is one gig drive or something. So,

**Dave Jones:** yeah. All right, I'll get back to you. Looks like it's working. Whoa. I think we're done. PFSense post installation setup done. It looks like there's a button there. I guess I just hit that. Installation complete. Would you like to

**Dave Jones:** reboot the install system now? Reboot. Woohoo. Winner winner chicken dinner. Um, yep. Yep, it's rebooting. So, yeah, this has been a little bit frustrating, but ultimately got through it. Okay. Well, it just booted. There was multi-user. I don't know. Single user,

**Dave Jones:** multi-user. Got no idea. What? Launch shell selector configuration. Install. I just installed the bloody thing. Oh, I'm a dumbass. It was still booting from the USB stick. So, all right. There you go. That's a pebbc. Yep. Yep. That's a Dave brain

**Dave Jones:** fart there. Well, there there you go. So, we're booting from the disk now. I still did not see that boot screen whether or not it was single user, multi-user, whatever the options starting device manager. Okay, we're good to go. Yeah, remember to use your

**Dave Jones:** remove your USB stick after installation. Unbelievable. Oh, hang on. We've got this ACPI error again. A bought in method due to previous error. Wow. when DHCP6. Nope. No. It's just the same error message over and over again. It's not going to boot.

**Dave Jones:** Unbelievable. I'm um giving up for now. Catch you next time.
