---
video_id: f496QtJDgzc
title: EEVblog #1300 - "Parts Per" Notation EXPLAINED
url: https://www.youtube.com/watch?v=f496QtJDgzc
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 15, "2": 30, "3": 60, "4": 90, "5": 102, "6": 119, "7": 131, "8": 149, "9": 179, "10": 193, "11": 211, "12": 229, "13": 246, "14": 268, "15": 287, "16": 307, "17": 326, "18": 345, "19": 368, "20": 385, "21": 400, "22": 416, "23": 434, "24": 448, "25": 464, "26": 484, "27": 500, "28": 517, "29": 533, "30": 548, "31": 565}
---

**Dave Jones:** Hi, in a previous video looking at this power supply, when I was going through the specs in here, just yapping away, talking about various parameters in here, I missed something, and you can easily cut my guts around here. Let's actually have a look at the output tolerance here, i.e.

**Dave Jones:** what is the basic specification for this power supply. Now, I'll give you like two seconds to have a look at this and then tell me what the voltage spec is. There it is. Voltage. Ta-da, we're back. What was it? Well, if you said it was plus minus 2%, you're wrong.

**Dave Jones:** It's actually 0.2%. What's going on? Well, it has to do with this little weird thing in here. This is not actually plus minus 2%. It's plus minus 2 per mil. What is per mil? Let's find out. So what is this per mil? Well, don't be surprised if you've never heard it before, because it's quite uncommon, especially in various parts of the world, various countries and various engineering and other disciplines, as we'll go into.

**Dave Jones:** But I bet you have heard of it in several respects. Per mil actually comes from the Latin. It means in each thousand or per thousand, basically. And it's written in various ways. It could be per mil, M-I-L. We'll get into that. You've almost seen it.

**Dave Jones:** You've certainly heard that before, especially on the EEV blog. Or it could be one word per mil, or it could have two L's without the E and all sorts of variations. But I believe the correct one is M-I-L-L-E. So what is it exactly?

**Dave Jones:** Well, this is where we have to get into parts per notation. You've heard this before. Parts per thousand, parts per hundred, parts per million, as we'll get into. And per mil is what's called parts per thousand, i.e. one part in a thousand. Now, you've certainly heard of the percentage sign.

**Dave Jones:** You're familiar with this. You use it every day in general life and engineering as well. That's actually parts per hundred, i.e. one part in a hundred. One percent is one one hundredth of whatever thing you're talking about. And per mil is no different.

**Dave Jones:** It's just parts per thousand. One part in one thousand of whatever you happen to be talking about. So in the power supply we saw, it was plus minus. Plus two, not percent, it's per mil. So plus minus two per mil is the correct way to say it, basically.

**Dave Jones:** And instead of it being, if this extra little O wasn't there, it is an O. It's not actually a zero. It's like an actual O. It's a circle. It's plus minus two. It's not plus minus two percent. But instead of parts per hundred, parts per thousand, we have to shift the decimal place one.

**Dave Jones:** So plus minus two percent, but when you add that extra O in there, it's per mil. So it's actually plus minus 0.2 percent if you want to convert it back to percent. And you do because you're more familiar with percents. Although you could work in per mils, but I don't think anyone does.

**Dave Jones:** Leave it in the comments down below if you do. I'm sure some specific industries do, but anyway, 0.2 percent like that is you're more familiar with. That's the general accuracy of that power supply. So why did they use per mil? I don't know.

**Dave Jones:** The engineer who wrote that manual, they were familiar with mils. Maybe coming from China, I've rarely seen this. It's very rare that I see this in the engineering electronics industry in terms of specifications and stuff like this. So it's real easy to miss and real easy to misinterpret, but you can easily convert between per thousand and per hundred.

**Dave Jones:** Just shift the decimal place. Make sure you do it in the right direction though. So if you want to do the working in this particular case, highly recommend you do just so you don't goof it unless because you rarely encounter this sort of stuff.

**Dave Jones:** Unless you do it all the time, you'll probably come a gutter real easy. So plus minus two on one thousand because it's per parts per thousand. So it's two parts per thousand like this, and that is equivalent to 0.2 on 100. So that's how you get your...

**Dave Jones:** 0.2% because it's parts per hundred. So where have you almost certainly seen and heard this before without knowing it was actually per mil with the double L-E like this? Well, on the EEV blog here, anytime I do a PCB video because I'm old school, I work in mils or thousand.

**Dave Jones:** Remember, PCB is one thousandth of an inch is equal to one mil. In this particular case, it's spelt with the M-I single L. But you could actually say it's M-I double L-E effectively. One one thousandth of an inch. You'll also get that in machining, mechanical engineering, of course.

**Dave Jones:** It's usually when you refer to inches. We don't usually say, you know, like a thou or a mil related to millimeters. That's just you just use millimeters or micrometers, microns. So where else have you heard of this parts per notation? Well, in engineering electronics, you've almost certainly seen PPM.

**Dave Jones:** Or parts per million. It's another per notation. And you could, in theory, I guess, write it with an extra three O's on the end of that. So four O's. But I've never seen that. Leave it in the comments down below if you've ever seen that.

**Dave Jones:** It's simply people just write it as PPM like that. Parts per million. And you'll get that in data sheets for crystal oscillators, for example. The accuracy of crystal oscillators. The accuracy of crystal oscillators. Generally defined in parts per million. You know, a couple of parts per million for a regular crystal down to like 0.1 parts per million for a more stable like ovenized oscillator or something like that.

**Dave Jones:** Or even lower. And you'll get that in your high end like six, seven and a half digit or eight and a half digit multimeters. So typically specify the accuracy in parts per million instead of percent or per mil in this weird ass case of this power supply that we looked at today.

**Dave Jones:** Now, there's actually one. More obscure one that's between these in here. We don't just jump from parts per thousand to parts per million. There's one that's actually not a per thing. It's actually called a basis point. And you've almost certainly heard this before.

**Dave Jones:** If you watch the news, financial news in particular, about how they've reduced or reduced these days. But trust me, they can actually go back up the interest rates. The interest rates are dropped by 50 basis points. What does that mean? Well, it's actually parts.

**Dave Jones:** Per 10,000. That's why it has an extra O on here. So it's just it's the percentage sign in per 100 with an extra O parts per thousand with an extra O again for parts per 10,000. So you hear in the financial news that they've dropped the interest rates by 50 basis points.

**Dave Jones:** Well, that's 50 on 10,000, which get your calculator out or just do it in your head is 0.5%. That's why the interest rate drops by 0.5% in real terms. But the financial people like to use it. They use basis points. I don't know.

**Dave Jones:** Sounds fancy. It's just parts per 10,000. So there you go. I hope you found that interesting. A lot of people will not have heard this. Even if you've been in engineering for a long time, you could easily never have come across this extra O in here like this or parts per thousand.

**Dave Jones:** You almost certainly heard of parts per thousand, you know, or even parts per 10,000. But did you know that's a basis point or parts per million? You know that one, you're familiar with it and percent. You may have never heard of it. You may have never really heard of a percent just expressed as parts per hundred, but obviously that's what it implies.

**Dave Jones:** You just, you know, everyone just instinctively is taught and understands percentages, but there you go, per mil, it's fascinating. So just watch your extra O's in here. When you're scanning a data sheet or something like that, you can really come and go. It's very easy to miss something like that.

**Dave Jones:** I did when I first looked through that data sheet for that power supply. I thought that was two. I thought, geez, that's pretty horrible spec. No, it's actually, I didn't see the extra O in there. And there's other like more obscure variations. Go look up per myriad, for example.

**Dave Jones:** There's like, leave it in the comments down below. If in your industry, do you have, or have you seen, or do you use on a regular basis, some like obscure thing like per mil or something like this. So have you seen this extra parts per notation with these extra O's in here like this?

**Dave Jones:** It is used in some like obscure fields. And things like that. So please, in the comments down below, it'd be interesting to find out where people use these more obscure ratios, because these aren't units, by the way, this does not, it doesn't imply any units at all.

**Dave Jones:** It's could be per, you know, parts per thousand could be parts per thousand of anything, of any unit. So I hope you found that interesting and useful. If you did, please give it a big thumbs up. And as always, subscribe over there, click the notification bell thing, so you get alerted to all my new videos.

**Dave Jones:** And as always, comment down below. Or over on the EUVblog forum, or on my library channel, catch you next time. Thank you.
