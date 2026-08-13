---
video_id: jYJz1QlPagM
title: TEST: Constant Qp Test - Using VBR
url: https://www.youtube.com/watch?v=jYJz1QlPagM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 40, "3": 60, "4": 80, "5": 96, "6": 116, "7": 128, "8": 144, "9": 156, "10": 168, "11": 188, "12": 208, "13": 224, "14": 240, "15": 256, "16": 272, "17": 288, "18": 308, "19": 324, "20": 336, "21": 352, "22": 368, "23": 384, "24": 400, "25": 412, "26": 428, "27": 440, "28": 460}
---

**Dave Jones:** Hi, this is just a test video because what I'm going to do here, you're actually going to see this video twice. It's the exact same video uploaded twice to my EEVblog2 channel and to all my alternative platforms because what I'm testing here is that when I render my files,

**Dave Jones:** I go in here, here's my latest Solar Robo's video not yet released, and if I go in here and render as okay, when I actually render this, I actually depending on the type of content it uses I generally, like for this screen capture one, I'll typically do

**Dave Jones:** 1080p, 30 frames per second because that's what I record at and 8 megabits per second and if we go in here and we customize the template here, I'm using Vegas here, please don't mention any other editors, just don't waste my time, please. Anyway, I do, so I use the

**Dave Jones:** NVENC encoder, which is the NVIDIA encoder and I encode it at a variable bitrate here and I in this particular case, I have 8 megabits, which is I think the recommended bitrate for YouTube with a maximum of 20, so it'll be an average bit, so by the time it finishes, it should be an average

**Dave Jones:** bitrate of like 8 megabits per second. And then various other ones, of course, you know, if I'm doing like, if I'm rendering like 4K, for example, like a teardown video, I'll do like 24 megabits per second average, which again is what YouTube recommend.

**Dave Jones:** But I'll use the variable bitrate. Now, what I want to actually do is I want to now experiment with rendering videos in, and I'll explain why in a second, rendering videos in a constant quality mode because yes, I use Handbrake for my, I'm aware of Handbrake and I use

**Dave Jones:** constant quality mode in Handbrake, but that's only for my podcast version. I don't want to do a multi-step process before I upload to YouTube, so I want to just output from Vegas, but I want to use a constant quality mode to get the

**Dave Jones:** file size down. So I'm using the exact same settings as before, but I'm going into constant QP mode here, which is constant quality mode, basically. So basically there is no minimum, maximum bitrate, it like just adjusts the bitrate. Well, actually I don't know

**Dave Jones:** if that's actually the case. I don't know what the average, no it can't be, because the file size is different, trust me. So the file size, I've tested this, and the file size is very different. The file size is much smaller, depends on

**Dave Jones:** the content, but it's much smaller than it is with constant quality mode, which is what I get with Handbrake. Anyway, so I want to experiment with that. So basically it's constantly changing the bitrate depending on the amount of changing information in the video.

**Dave Jones:** So if I've got a mostly static image like this, these screen captures, these actually compress quite well even with standard variable bitrate down to like small file sizes, because there's not much changing on the screen, so it doesn't need to push up that higher bitrate.

**Dave Jones:** It's just my little talking head down here, and there's no like shaky cam footage or anything like that, it's crisp, clean, unchanging background here, right? So that's really good for the compression algorithm. So screen captures actually compress really low in file size. So the problem is, this is not a problem for YouTube, okay?

**Dave Jones:** For years I haven't worried, I used to worry about file size. Here's all my original files going back almost to number one. I do have number one somewhere, but anyway. Let's go right to the bottom. Here we go. So here's my recent ones, okay?

**Dave Jones:** And I've done some tests here, you can see how I did my regular 8 megabits per second output and it was 174 meg here. I did the exact same video again and it was only 44 meg. This is like just an example, like 3 minute

**Dave Jones:** render. So it was much smaller file size, but I can't really pick the difference. So once again, I've just, here's my files, like some big ones, like this compact portable teardown, but that's 4K. Right? That's like 6.5 gigabytes, right? That is a lot.

**Dave Jones:** You know, it's quite large. And mail bag, like even though that's only 1080p, but that's over 6 gig again, because it's like an hour long and stuff like that. But even, you know, why are these pins short at 1.5 meg? Like a battery

**Dave Jones:** leakage? Was that a screen? Oh no, that was just a very short one. But you know, my file sizes are right up there. Now the problem with this is, as I said, not for YouTube. Nobody has any problem playing back on YouTube. But all of my alternative platforms,

**Dave Jones:** Odyssey for example, I just hit 50,000 subscribers on Odyssey, thank you very much. And BitChute and Utreon and Vimeo and others, right? I get these systems to automatically pull my videos from YouTube. And if I upload to YouTube in a really high quality large file

**Dave Jones:** format, I don't know if it's pulling the exact file, but it seems to be pulling very large files. Now normally, of course, what Odyssey slash library, for example, recommend is of course to use Handbrake before you upload. But I don't have that option because I want it to

**Dave Jones:** automatically pull my videos. Because it'll pull in the video, the thumbnail, the description, the links, the keywords. It just pulls in everything and makes it easy. I don't want to have to be uploading the same different file to like you know, half a dozen different platforms that I'm on.

**Dave Jones:** It's stupid. So I figure if I can get my file size down that I upload to YouTube that I used to do back in the old days when it actually mattered, when upload bandwidth was a problem, right? I'd make more small files as small

**Dave Jones:** as possible so that I could upload in a reasonable time. But now upload speed is just, you know, it's practically instant here. I've got like a, what is it? 250 meg upload? Meg bits upload? So it's not a problem. It's really quick. And of course no storage problems on YouTube

**Dave Jones:** or playback problems. But on places like Odyssey that have a buffering problem, it's a real issue. So I'm going to do this exact same file, I'm going to render it twice, and I'm going to use one, it'll be labeled in the description, and one will be constant

**Dave Jones:** quality, one will be just my regular outputting variable bitrate. Because I want to test if that exact same file uploaded in two different files, one will be smaller, constant quality but smaller, uploaded to YouTube, if they actually pull into Odyssey and other platforms

**Dave Jones:** at a different file size, right? So and Odyssey tells you what the file size is, because you can just download the file from Odyssey, right? You don't, like, it has a direct link there to do it. It tells you what the file size

**Dave Jones:** is. So this is just a test to check whether or not YouTube reprocesses it, does whatever, and I'm going to end up with exactly the same file size result, in which case, well, there's no point me doing this constant quality thing. I might as well upload the best quality possible to YouTube and be done with it.

**Dave Jones:** Or whether or not it'll download quicker. So I actually don't know. I hope it does. So this is a test. I'll let you know, or you can look at the comments down below, or have a look for yourself. The file size, see if it's any different.

**Dave Jones:** Go to my Odyssey channel, link down below, and see if the file size is different between these two videos. If it is, I'll upload in constant quality from now on. So there you go. I'll start a render. So I'll drop this into the timeline, this video, and then I'll render it.

**Dave Jones:** Catch you next time.
