---
video_id: gO7hdxyCNCA
title: EEVblog 1721 - RIP Arduino (New T&C Deep Dive)
url: https://www.youtube.com/watch?v=gO7hdxyCNCA
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 36, "3": 50, "4": 67, "5": 88, "6": 102, "7": 113, "8": 128, "9": 142, "10": 156, "11": 169, "12": 180, "13": 191, "14": 208, "15": 221, "16": 238, "17": 256, "18": 268, "19": 281, "20": 296, "21": 311, "22": 324, "23": 339, "24": 350, "25": 364, "26": 376, "27": 388, "28": 404, "29": 423, "30": 444, "31": 457, "32": 471, "33": 485, "34": 503, "35": 519, "36": 532, "37": 548, "38": 565, "39": 581, "40": 596, "41": 609, "42": 624, "43": 637, "44": 652, "45": 667, "46": 680, "47": 698, "48": 710, "49": 725, "50": 743, "51": 762, "52": 774, "53": 792, "54": 805, "55": 821, "56": 836, "57": 847}
---

**Dave Jones:** Hi, you've probably heard the news about 6 weeks ago that Qualcomm acquired Arduino. Yes, completely gobbled up that bastion of open-source hardware that was Arduino. So, I and almost everyone else in the industry predicted, well, once that takeover happens, that big

**Dave Jones:** corporate buyout happens, it's basically just downhill from there. It's not a matter of if, but when Arduino just simply vanishes into the ether. And I predicted on Twitter that once the corporate suits want their KPIs, their key performance indicators,

**Dave Jones:** I gave it a bit about probably 12 months tops before they start to go, "This ain't working. We're not making money from this thing." And probably turn into a subscription model or some other rubbish like that. And in

**Dave Jones:** a few years time, it'll just vanish into the ether. Poof. But, of course, Arduino is open-source, so it can actually be forked. And we'll talk about that at the end of this. Now, it's unknown what Qualcomm actually paid for Arduino, but

**Dave Jones:** my guess is it's probably in the quarter of a billion dollars, i.e., $250 million range plus. Why? Because we know that Arduino have taken $53 million in two rounds of venture capital. And that's from the likes of Renesas, uh Bosch, and CVP Capital,

**Dave Jones:** and Andreesen Horowitz something like that. So, they've raised a lot of money. And those seed investors are not going to sell out for anything less than a decent multiple of the money that they put in. So, 53 million bucks worth of

**Dave Jones:** income, I reckon it's at least 250 million bucks, at least, they paid for this. If you've got any other guess what it might be, leave it in the comments down below, but I reckon it's at least quarter of a billion. And basically,

**Dave Jones:** they only make their income from two things, either hardware or like software services. Um And basically, hardware services, there's data out there that show that's like the vast majority of their income. And there's sales figures out there of like a million to two

**Dave Jones:** million a year or something like that, if I recall correctly. And basically, yeah, no, they're not going to be making their money back, especially given that people have gone, "Oh, Arduino's bought out. Why am I going to now support this

**Dave Jones:** big huge corporation, Qualcomm, when I can just buy a clone Arduino board? So, what's the point?" So, all that goodwill is just going to go down the toilet. So, there's no way they're going to make money with this thing. And yeah, as I

**Dave Jones:** said, 12 months' time, when the KPIs come in and they realize they're not making money from this, they'll try and tighten the screws in. They'll bring in the subscription goblins. And well, that's not going to work either. And

**Dave Jones:** eventually, no, it's all going to go bust. They'll just write it off on tax. Anyway, there's been some talk today about them making some big changes to the terms and conditions on the website. So, I thought we'd have a look at it.

**Dave Jones:** It's not going to be an absolutely 100% comprehensive look, cuz it's like a 40-page terms and conditions. But I'll I'll see if I can find some highlights here. So, what I've got on the left-hand side here is the brand new terms and

**Dave Jones:** conditions here, live on their website, updated October 29th, 2025. So, it's actually been updated a while ago. So, that was only a couple of weeks after they acquired them. So, anyway, on the right-hand side here, I've got a

**Dave Jones:** September 12th edition of the terms and conditions before they were bought out. But it's actually not September 12th. If you have a look here, it was updated November 26th, 2024. So, that's the last time they updated them. So, we'll use

**Dave Jones:** that as a comparison before and after. The very first thing they've got here is important notice regarding arbitration. This is all the latest uh fed with uh big companies like this. It basically means that well, your options of suing

**Dave Jones:** them if it came down to that is limited. Basically, it gives up your right to a jury trial class collective aggregate representation or consolidated actions or proceedings. So, anyway, um there was something about that in the previous uh things. So, yeah, but it's just

**Dave Jones:** changed. I guess it's worse. I don't know. You'd have to ask one of those legal channels. But here's a big update which wasn't in the previous terms and conditions. Basically, if you're under 18 years of age and well, Arduino was

**Dave Jones:** designed for entry-level hobbyists. So, a huge part of that market will be under eight people under 18 years of age. They're basically saying bugger off, we don't want you and you we're going to give you a limited account. If you are

**Dave Jones:** under 18 during the registration process, you'll be required to provide uh date of birth and otherwise confirm your age. If you are under 18, the account will be restricted to a junior account. What restrictions that has, I don't know. And if they become aware

**Dave Jones:** that uh anyone using it like a normal account is under 18 years of age, uh they're just going to ban your account. Great. Thanks. And in the previous terms and conditions, the word age doesn't even appear. So, yeah, that's a new one.

**Dave Jones:** Now, one of the big concerns was about uh reverse engineering content. And that's of course um not supported by the open source ethos. Um this is the whole point of open source hardware and software is that you're supposed to be

**Dave Jones:** able to reverse engineer things, figure out how they work. And here it is. Um 8.2, user shall not translate, decompile, or reverse engineer the platform, engage in any other activity designed to identify the algorithms and logic of the platform's operations

**Dave Jones:** unless expressly allowed by Arduino or by applicable license agreements, or extract or make copies of the information contained in the platform, blah blah blah, make derivative works from the platform, reuse the platform, making any other use of the platform

**Dave Jones:** other than as set forth in the terms permitted by applicable law. That sounds really bad, but as it turns out, that wasn't added by Qualcomm. This is not a change, it was always in there. Here it is, 6.2 instead of 8.2. It's basically

**Dave Jones:** word for word, the user is prohibited, the user shall not. That's pretty much the only difference, I think. Haven't checked it word for word, but yeah, it was already there. So, it's not like they've gone suddenly changed direction

**Dave Jones:** and said, "Oh, you can't reverse engineer anything." Apparently, that was always there. I don't know when Arduino put that in, but yeah, it's there. So, maybe it's some catch-all clause for, I don't know, you don't want to reverse engineer their

**Dave Jones:** website or something like that, perhaps. But yeah, it was always there. So, that rumor is busted. And here's a big change, publishing content on their website, you'll see that basically, you give them anything you upload to the website, you give them a perpetual,

**Dave Jones:** irrevocable license to use that forever. Whereas, the previous one, perpetual, but revocable. So, you had the option in the previous Arduino terms and conditions, you could delete your account, for example, and actually revoke the stuff that you've uploaded to them. So, they've changed

**Dave Jones:** that to revocable to irrevocable. Oops. And here's another worrying one, Arduino services. So, if you use the Arduino platform and services and the code and everything else for your open source hardware project, then they can revoke, they can revoke your ability to

**Dave Jones:** do that, which could, I don't know, your project or something like that. I don't know how that relates if you then publish it on GitHub or whatever. Can they revoke your ability to, like, publish it elsewhere or something

**Dave Jones:** like that? And there was no mention of revocable under the previous one. So, they could potentially pull the plug on your project, I guess. I don't know. Once again, it's legalese, you know, only you know, you've got to battle it

**Dave Jones:** out lawyer versus lawyer to try and figure out what it actually means in the end. But, yeah, doesn't sound good, does it? So, if you're looking to design a product you know, which you might turn into a marketable product, we'll talk about

**Dave Jones:** that in a minute, then do you trust using the Arduino site and services and code and whatever if it's revocable? I don't know, sounds a bit dodgy to me and it just erodes trust in the whole open source system. Like,

**Dave Jones:** why would you touch them? And another concerning one, they've changed this user's duties here and look at this, user will use the site and platform in accordance with these terms and conditions. But, specifically, the user undertakes not to use the platform

**Dave Jones:** to develop competitive services including to create or incorporate other data sets correlated to Arduino to be used for a service which is similar or identical to the services.

**Dave Jones:** Like, it's supposed to be open source hardware and open source software, right? I guess the whole point is that you can fork it and now they're saying you potentially can't we don't want you to fork it. I don't know. Whereas previously, that

**Dave Jones:** first point was just transfer or resell the services or premium services and the right to the platform to others. Well, that's fair enough. So, there's some legalese wording there that they've specifically changed there. So, that's a worry. I don't know, you know, it

**Dave Jones:** requires a lawyer to delve into the details, but doesn't sound promising. And there's other concerning ones like you cannot export any information outside the platform except for those cases expressly permitted by the terms and conditions, but that was there

**Dave Jones:** previously. So, yeah, I don't know. Not probably not too much to worry about there. But, you'll notice that under here there's a couple of more very large points that weren't there in the previous version. So, you can't sell,

**Dave Jones:** export, re-export, transfer, or otherwise make available, or enable access to the platform side of service directly or indirectly. Blah, blah, blah, blah, blah, and all that use the platform side of services identify or provide evidence to support any

**Dave Jones:** potential patent infringement. So, they've added patents. They're They're protecting their ass, or trying to protect their ass some way there. I don't know. Legalese. But, yeah, the lawyers are on the case. They're They're earning their coin here. They've added a

**Dave Jones:** lot of stuff. And you'll notice how the old terms and conditions just jumped onto use of the services and premium services here. But, in the new one, they've added a whole new section four, which is export and trade controls

**Dave Jones:** compliance. And, well, yeah, I don't know. Read that to your heart's content. But, it's just more things to be worried about if you're, once again, using anything to do with Arduino. Uh well, anything to use with like their website

**Dave Jones:** or services, code, whatever it is, then um yeah, you've just got to be aware of this. That there's all sorts of export restrictions. A lot of lot of it's like to foreign you know, countries that are unfriendly to the US and all that sort

**Dave Jones:** of jazz. But, still, you know, they've added a lot of stuff in there. And this one sounds concerning. Should the platform or services allow the downloading of specific content, the download of a copy, unless otherwise indicated, shall be only used on one

**Dave Jones:** computer device for personal and not for commercial use. Um that sounds dodgy until you actually realize that, well, the old license uh terms and conditions had exactly the same things. I don't know what that's about. And this changes section has been

**Dave Jones:** expanded a lot, whereas previously it was just changes to the agreement was just the one section here reserves the right to modify the agreement publishing the new version on the site. You know, that's all standard stuff, but here

**Dave Jones:** Arduino reserves the right to change, suspend, or discontinue any service. However, if users pay for a premium service, Arduino will provide for the term specified. That means, well, if we shut this whole dog and pony show down in 2 years, then

**Dave Jones:** well, tough titties. And you'll only get 30 days notice. Great. And you can't sue them either. If you're, you know, base your widget design on anything Arduino base that requires on their products or services, if they shut down, well, that's it, but

**Dave Jones:** that's pretty standard stuff. Moderation and content restrictions imposed on user seems to be quite similar to what they had previously, so nothing major there, I don't think. But having said that, yeah, they can like suspend your account for whatever reason, so good luck with

**Dave Jones:** that. They've added an indemnification clause. That's pretty standard. That was not in the previous one really, so but yeah, as you can see, they're we're up to section 21 now, and they've added a lot of stuff, whereas the previous one

**Dave Jones:** only had like 13, 14 dispute resolution. Once you after 14 here, um that was it. Bob's your uncle there, but this one, yeah, just, you know, these arbitrary these binding arbitration things and trial by jury and all that sort of

**Dave Jones:** stuff. They've added a lot of dog and pony legal show here, so do you say specific obligations? I got no idea what that is. That's an EU thing, is it? I don't know. Anyway, as you can see, they

**Dave Jones:** have changed a lot of stuff and it's almost certainly not for the better. But of course I saw all this coming a mile away and I am the owner of libre duino.org. There's nothing there at the moment and

**Dave Jones:** I have no plans to use it personally, but if somebody out there has some really good plans to use such a domain then well, let me know and I can transfer it over. Anyway, if you found that useful and if you found anything

**Dave Jones:** else specific in here that wasn't in the previous version of the leave leave the direct links to these two so that you can compare them yourself. You could even probably use some automated AI thing to compare them or something if

**Dave Jones:** you really want. Yeah, let us know in the comments down below or over on the EEVblog forum but yeah, Arduino I think it's circling the drain. Wah wah wah. Catch you next time.
