---
video_id: c_ZhkT2E7Fw
title: EEVblog #122 - Renesas RX Design Contest Announcement
url: https://www.youtube.com/watch?v=c_ZhkT2E7Fw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 27, "2": 48, "3": 78, "4": 103, "5": 122, "6": 141, "7": 173, "8": 189, "9": 208, "10": 230, "11": 243, "12": 263, "13": 283, "14": 303, "15": 326, "16": 344, "17": 361, "18": 382, "19": 401, "20": 433, "21": 463, "22": 480, "23": 501, "24": 520, "25": 541, "26": 563, "27": 582, "28": 600, "29": 616, "30": 632, "31": 647, "32": 667, "33": 681, "34": 694}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. We're going to announce and launch our RX design contest tonight. In fact, right now it's the official launch. It's one of the biggest and best contests we've ever done.

**Dave Jones:** It's going to be global. We're going to have Europe and parts of Asia participate in this contest. And what's interesting is, for the first time, our alliance partners are joining me and supporting and sponsoring this contest. I'm very proud of having the support of these alliance partners.

**Dave Jones:** And what does this partnership or sponsorship by these great alliance partners mean? It means that together, Renesas and its partners, we have put up $110,000 in cash and prizes for the winners. That's amazing. You know, recently, at DHC Boston, one of our competitors announced a contest and I think it was $15,000.

**Dave Jones:** $15,000, so you can compare it. It's amazing. $110,000 in cash and prizes. And it's going to be distributed for a very limited number of opportunities. Of course, the awards, first and foremost, will be based on technical merit, originality. They have to be useful.

**Dave Jones:** You know, like those beer mugs we had last time with the LED lights going on? Very useful. They have to be cost-effective. And, you know, these days, documentation, if you want to use video or any type of good-quality documentation will also be important.

**Dave Jones:** And most of all, we're going to use public input for voting. So it's going to be online, it's going to be, you know, using social media, it's going to be public input as well. You will have, or the contestants will have until March 4th, 2011, to submit your design.

**Dave Jones:** And we will do the final judging live at the upcoming Embedded Systems Conference in San Jose. Which is, they call it the Spring ESC 2011. Now, for us to enable you to submit those original and useful designs, we would have to allocate 1,003 Renaissance Rose kits for the RX-661.

**Dave Jones:** So, you know, we're really going to enable a lot of people to try to participate in this contest for the $110,000 cash prizes. Now, to talk about this board, we have a special guest here, Maury Wright. Most of you know him as Dr.

**Dave Jones:** Michael on our Renaissance Rose blog page. He's here to share with you the importance of this board. Please welcome Maury Wright. Thank you. My name is Maury Wright. Dr. Michael has been through most of this week. He's been very gratifying to those of you who have been asking about the effect Dr.

**Dave Jones:** Michael has had on Renaissance Rose. And I appreciate you reading the blog. I'm really excited about the contest. I'm excited about the RX architecture in general. It's been a lot of fun for the past six months. Getting a chance to investigate the RX architecture and to write about it on a regular basis.

**Dave Jones:** And now, I'm excited about the opportunity to participate in the judging and to continue the Dr. Michael blog. And among other things, cover the progression of the contest. And I want to talk a little bit about the board, which you see on the screen.

**Dave Jones:** I think this is just an outstanding platform for a contest. The contestants will probably, for the most part, get their hands on the RX-661 microphone for the very first time. With the full complement of communication and peripherals such as Ethernet, USB, and CAN.

**Dave Jones:** But the platform is way more than that. It has a host of other good stuff on the board for third parties. For analog devices, we have three MIMS sensors. A three-axis accelerometer. A digital thermometer. A microphone. There's a fantastic graphics display you see there.

**Dave Jones:** It's pretty small, but it's amazing how much you can put on that graphics display. There's also a flash device. There's an Ethernet by the National Semiconductor. And great remote support from Sega. So, it's a platform that I think will allow the contestants to really come up with compelling applications for it.

**Dave Jones:** And something I really look forward to testing. I'd also like to just mention the demonstrations that come to the board. I think those demonstrations will both help the design contest entrants jumpstart their project and probably will inspire ideas. For example, there is a motor control demonstration that comes with the kit.

**Dave Jones:** And that motor control demonstration uses that circular area of LEDs that you see to simulate the different phases of a motor drive. So, I look forward to seeing how creative all you can be. And to participate in the judging. And also to model and put forth.

**Dave Jones:** Now, I want to introduce another engineer that's going to be involved in the process as well. You may have seen him around here with his camera this week. You probably know him best for his presence on the internet. He's E.E.B. Block. Please welcome Dave Jones.

**Dave Jones:** Hi, I'm Dave Jones. I'm with E.E.B. Block. And my secret talent has been unusual. Every week I educate and entertain those like me on YouTube. And trust me, that takes a lot of talent. Roll the tape. Let's blow some shit up. Alrighty, look at that.

**Dave Jones:** Check out the input circuitry. Oh, isn't that sex? On a stick. Why? They probably went back to their cubicles and just started bashing their heads against the decks. Yes, it wins the E.E.B. Block Retardant product of the week award. This is actually real.

**Dave Jones:** Maybe I'm lying. Look, watch this. Oh, jeez. No, go away. I'm a professional design engineer. I don't need design advice. It's all over the shop. It's messy. I don't like it. It sucks. Let's have some fun. Woo! Oh, silly old springing sound in that way.

**Dave Jones:** You guessed it. Fantastic new technology that can make it work. Well, I smell bullshit. One person, one hobbyist, one hacker, one maker can change the world. Thank you. I can't believe I'm talking about my own stuff. That's terrible. I've never seen myself with such a big screen.

**Dave Jones:** I'm so used to watching myself on YouTube. On a tiny little YouTube screen. I don't have any speech prepared today. I've lost the cuff. As I already introduced myself, my name's David Jones. I'm the host of the Electronics Engineering Video Blog. If you don't know the accent,

**Dave Jones:** I am Australian, from Sydney. I'm not from Zealand or England, so please don't get us hooked up. And I basically do a weekly electronics engineering show, which should be of interest to most electronics engineers out there. If you like my style, that's pretty much a summary of some of the wacky stuff I get up to.

**Dave Jones:** I do product reviews, product teardowns, design tutorials, and I like to rant about bad product design. Basically, if something's crap, I call it crap. That's something I enjoy doing. So, if you want to see the show, it's only a week from any of these Microsoft conferences.

**Dave Jones:** I'll do one for myself, if I can get away with that. Now, our apprentices have asked me to be involved in the RX Design Contest. I've got one here, and I'm super excited, really. This is a great design contest. I've been involved in a lot of design contests over the years,

**Dave Jones:** both entering and watching. And there's even Microsoft in the audience, who's won a previous design contest. And a lot of them are pretty lame. They've got, you know, $5,000 total prize money. We're talking $110,000. It's massive. I've never seen a design contest this big.

**Dave Jones:** I'm excited from that respect. And also, there are just so many prizes involved. Really, it's just unbelievable. If you don't win a prize in this, I mean, you can always get something for a leg flasher. There's that many prizes involved. It's not just one major prize.

**Dave Jones:** So, it's fantastic. Now, I'm going to be involved in this several ways. The first way is, I'll meet a judge at ESC, along with Darth Maury, who introduced me, along with several others here as well. And our job is to, I guess, go by the contest rules.

**Dave Jones:** But I do like stuff that's cool. So, if you design something cool, that doesn't quite meet the criteria, it's going to get up there. So, guys, make some cool stuff, okay? I'm going to be dealing with this. The amount of power on this RX4 is phenomenal.

**Dave Jones:** The amount of features that you can get, all the stuff built in that Maury went over, it's just incredible. So, you can do anything. You can imagine with it. Now, so, I'll be a judge at ESC. I will also have a regular video involved.

**Dave Jones:** It will be both on the EEV blog and on the rest of the rules site as the contest goes along. I'll be tearing down the board and doing some, probably, some exams and showing you how it works and giving you ideas and things like that.

**Dave Jones:** And I'll certainly, I'll most likely be talking, I'll most likely be reviewing some of the entries. So, if they don't work well, you might just give them a serve. So, make sure they're interesting, make sure they're creative, make sure they're cool. And have some fun with this RX Design Contest.

**Dave Jones:** And I'd like to thank everyone who's been involved with this because it really is fantastic. So, get to work, guys. Get one of these. It's free. Can you believe it? If you haven't picked one up, okay, see one of the Renesas people. I'm sure they can hook you up

**Dave Jones:** if you want. It's got 99 bucks written on the back. There it is. 99 US. You don't have to buy it. You can give it away. It's unbelievable. So, enter the contest and I hope you do well. Thank you. Thank you a lot.

**Dave Jones:** Thank you.
