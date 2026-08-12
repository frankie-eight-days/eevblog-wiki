---
video_id: I0HOgcbtmws
title: Open Source Hardware Explained - EEVblog #195
url: https://www.youtube.com/watch?v=I0HOgcbtmws
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 34, "3": 52, "4": 78, "5": 98, "6": 117, "7": 135, "8": 151, "9": 165, "10": 179, "11": 196, "12": 212, "13": 223, "14": 240, "15": 256, "16": 270, "17": 284, "18": 302, "19": 315, "20": 334, "21": 350, "22": 362, "23": 377, "24": 392, "25": 409, "26": 424, "27": 442, "28": 453, "29": 471, "30": 486, "31": 501, "32": 513, "33": 529, "34": 539, "35": 554, "36": 571, "37": 590, "38": 604, "39": 621, "40": 633, "41": 649, "42": 664, "43": 680, "44": 695, "45": 709, "46": 723, "47": 736, "48": 751, "49": 768}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I thought I'd talk about open-source hardware or open hardware because there seems to be a lot of confusion out

**Dave Jones:** there, a lot of misinformation about exactly what open-source hardware is, what the definition of it is, when can you call your stuff open hardware, and what license should you use, and why you would do it. Why would you give your

**Dave Jones:** stuff away? Sounds ridiculous. Well, I thought I'd try and break it down for you. Here we go. So, what is open-source hardware? Well, the best example is the Arduino, as you're probably familiar with. It is the classic example of a successful

**Dave Jones:** open-source hardware project. And open-source hardware is kind of like uh open-source software, except with software, there's nothing tangible. There's nothing physical of actual worth. If you copy an open-source uh software product, then you get the exact functional product for free,

**Dave Jones:** completely for free, but open-source hardware doesn't work like that. This costs money to actually produce. It's about the design files to manufacture this. The information to manufacture this is free and open so that anyone can duplicate this hardware themselves if

**Dave Jones:** they don't want to buy it. That's basically what open-source hardware is. Remember, it's not free hardware, it's open hardware. Thankfully, there's actually now a formal definition of what open-source hardware is, and I'm going to link to the actual definition of it

**Dave Jones:** and it's got 12 different points. It sounds quite complex, quite involved, but I'm going to break it down to just two essential elements cuz I think that's all there is in open source hardware. It's very simple. Point number one, you have to give away

**Dave Jones:** all of the manufacturing and design files for this hardware to allow anyone to not only recreate the hardware, but to also change it and make derivative works from it. So, it's not just good enough to give away a PDF of the

**Dave Jones:** schematic and the Gerber files and that's it. That's not open hardware, it's not good enough. You have to give away and crucially, this is very important, you have to give away the original uh PCB and schematic files for your

**Dave Jones:** hardware and it includes the firmware as well to make it work and any necessary PC software to make it work and stuff like that. The bill of materials and anything else, block diagrams, as much documentation as you can give away to

**Dave Jones:** allow people to create and modify this without having to buy it. And just with those CAD files, they can be a real contentious issue cuz a lot of people claim that's not truly open open source hardware if you don't use open source

**Dave Jones:** EDA software tools. So, if you design your open source hardware project and you release it in say Altium Designer, which is a commercial product, no free thing available, then that's completely sucky, but probably still okay. If you release it in Eagle, it might be the

**Dave Jones:** next level. Once again, still a commercial software package, but at least a free version is available. That's kind of less sucky. And then, you get down to the point where, well, you use an open source tool and that's the

**Dave Jones:** true spirit of it, KiCad, gEDA, or one of the other open source CAD tools. Point number two, you have to give complete freedom to people to do whatever they like with the hardware and that includes to sell it and possibly

**Dave Jones:** even compete with you with the exact same product using the exact same files. You cannot restrict it to a non-commercial entity so that you're the only one who can make money from it. That's not open hardware. It's It's about the hardware

**Dave Jones:** being free and open for people to do whatever they want with it. You can't discriminate against people. You can't say, "I don't like Joe Bloggs, so I'm not going to let him use it." You can't do that. And you can't stop people from

**Dave Jones:** using the hardware in a way that you don't approve of. Somebody wants to use it in a nuclear bomb? Well, that's up to them. You can't stop them. Freedom. Now, when it comes to licensing your open source hardware product, there's a bunch

**Dave Jones:** of licenses available and I'll link to them. And what it essentially comes down to you though is that the license must meet the terms and conditions of the open source hardware definition. The official definition that's been defined not by

**Dave Jones:** some official group, but just by peers in the industry. They've got together and they've said, "This is what we think open source hardware should be and anyone who calls it open source hardware or open hardware should follow this

**Dave Jones:** definition. If you don't, don't call it open hardware. Call it something else." There's many licenses available. GPL is a popular one. CERN now have a new open source hardware license. Check it out. The very popular Creative Commons license is extremely popular, but beware

**Dave Jones:** of the non-commercial aspect of the license. You can't put that little clause which says non-commercial in there. If you do that, it ain't open hardware anymore. End of story. There's a bunch of licenses. Which one you actually choose doesn't really matter as

**Dave Jones:** long as you meet the spirit and the ethos of what open source hardware is about. You can even just completely give it away. You don't have to have a license. Public domain. Boom. Go. There's one important thing to remember

**Dave Jones:** with open hardware and that is if you take somebody's open hardware project and you modify it for your own purposes and then you go sell it, then that's fine. But you under uh then under an obligation to give that design back to

**Dave Jones:** the community under the same license that you got it from. So you have to share it. It's share-alike. So if you're using the Creative Commons license, you must use the share-alike license. And that helps build up knowledge and build

**Dave Jones:** up the product and everyone's work builds upon each other and we get better products in the open source community. Now even if somebody completely gives away their stuff under no license into the public domain, no strings attached, here it is, I give it to the world, then

**Dave Jones:** it's still common courtesy to acknowledge where you got it from. Give them some attribution. If you got this little bit of source code or this little uh circuit snippet from somebody, just acknowledge them. It's just common courtesy and it works both ways. If you

**Dave Jones:** do it for them, they'll do it for you, somebody else will do it for somebody else, etc. And it'll just be one nice big happy sharing community. Awesome. Group hug. So why the hell would anyone be stupid enough to give away their design? You

**Dave Jones:** spent a year working on your widget. You worked really hard. You set up an online shop. You're trying to sell it as a finished product or as a kit. You're trying to get into the business, trying to make some money, trying to get some

**Dave Jones:** fortune and glory. Why would you just give it away as open hardware? Oh, it's a very good question and there's several answers. First of all, while there might be some one hung low companies in China on eBay selling a clone of your product, and

**Dave Jones:** they might be taking some sales away from you, in general, it's not really a big deal because the people involved in the open source hardware community have the same ethos as you, and they would rather pay a little bit more and help

**Dave Jones:** you out, help give money to the original designer, get the original product, the original support, and things like that than buy it from the one hung low company in China. So, don't worry about it too much. You can still make your

**Dave Jones:** fortune and glory and release it as open hardware. And if you do want to protect your design just a little bit, you can do what the Arduino mob have done and you can trademark your name. Look, little TM

**Dave Jones:** next to it. It means nobody but the Arduino mob can use that name. Hence, ChipKit and Arduino this, Arduino that, okay? And you you can do that and you're still within the spirit of the open source hardware community, but I'd like to

**Dave Jones:** think that you probably don't even need to get a trademark. If you just say to people that, "Hey, I'd prefer it if you don't use that name." Or you take or if you want to spread it, then, you know,

**Dave Jones:** take off don't use my logo or my whatever. Okay? And most people will be happy to abide by that because it's a big sharing community. And those that don't abide by it, well, they'll probably end up getting a bad rep and

**Dave Jones:** sort of be, you know, shunned aside in the community. Second thing is, most of the open source hardware licenses have attribution clauses attached to them. So, your name will should always be attributed with that particular idea, that particular product, or whatever.

**Dave Jones:** And you become the industry expert on that product. And that can lead to not only glory, but it can lead to fortune as well because you People might approach you. Big companies might approach you because you're famous, because you designed X widget. So, they

**Dave Jones:** might hire you to design something similar for them or do other consulting work. You might be asked to speak somewhere, do whatever. There's lots of avenues to make your fortune and glory. Third, it can be that warm fuzzy feeling

**Dave Jones:** you get inside when you contribute something to the industry. And you get all this email, floods of email of people thanking you and helping you. People if you give to the open source hardware community, people will give back in terms of time. If you're not

**Dave Jones:** very If your widget or something needs a really nice custom case and you suck at designing CAD files, you might have somebody come up and say, "Hey, I like your product. I'll design you a case for free." Or something else. It's give and

**Dave Jones:** take. It's all part of the big wide community. That can be a really good thing to have. If you build up your name and rep in the industry, and of course it's understandable if you've worked hard on your little gadget, and you want

**Dave Jones:** to restrict people uh selling it and competing against you, well, that's just fine. It's your design. You have the freedom to do that. But just don't call it open hardware or open source hardware because people in the industry who

**Dave Jones:** support the actual definition of open source hardware, they'll come and wag their finger at you, and you'll get a bad rep. So, by all means, go on sell your product, but don't open hardware unless you meet the definition.

**Dave Jones:** There you have it. That's open source hardware in a nutshell. It's not as crazy as it might seem, and there can be some real big positive and long-lasting benefits to open sourcing your next project. So, why don't I give it a try?

**Dave Jones:** Set your next project free and see where it takes you. Now, open source hardware has actually been around for a long time, a hell of a long time. The concept has been around forever, but the definition is fairly new. It's only been

**Dave Jones:** ratified fairly recently as a general consensus in the industry. And not everyone necessarily agrees with it, but just be careful. If you are going to make the claim that your product is open hardware or open source hardware, same

**Dave Jones:** thing, then make sure it meets the definition. You don't want to piss off people who take this sort of thing and the definition very seriously. But essentially, it comes down to the spirit and the ethos of the whole open source

**Dave Jones:** hardware movement. And a lot of people can get really passionate and opinionated about this whole thing. Now, there's no doubt that the definition will change over time with how what happens in the industry and with community feedback. The whole thing was

**Dave Jones:** built on community feedback. So, if you've got feedback or some opinion on how open source source hardware should work, how, you know, if you don't like something in the definition, then well, leave some comments, contribute, leave some video responses, get your opinion

**Dave Jones:** out there and your voice heard. And you might just help shape the future of the open source hardware industry. Woo. See you.
