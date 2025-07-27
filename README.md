# Inspiration

You have been called by your teacher to solve a question on the board, while the truth is you've not been paying attention and have no idea how to even start. You give your friend and awkard stare, but turns out he knows what to do and tries to help you by mouthing the words without making sound and getting caught. But there's a catch, you couldn't understand and made a dumb decision to write whatever you could make up from the lipsing... You failed that class terribly and were very embarrased.

Well, what happened can't be undone, but to prevent it from happening in future, me and my partner decided to make a tool that can read lips. Although it won't be ethical to do such activities in the classroom, we've decided to make a slight diversion and think how it can help society in a good way!

Our app will be able to create live transcripts from just lipsing, and this will be able to help a lot of people with hearing disabilities.

# What it does

(What we wanted to do) App can generate transcripts from reading lips.
(What we could have progress) Detect if someone is trying to speak and the visemes they spoke.

# How we built it

We used OpenCV and MediaPipe in Python, used some maths of ratio and proportion and some constants later, we can detect sylables (a few atleast)

# Challenges we ran into

Apparently, apart from using python, these kind of projects are new to us, so it was a hardship, but to make the progress we have done so far, we took a lot of thinking, analysing information about how we speak, association between shape of mouth, teeth, and tongue with sound produced and trying to replicate sounds in a weird way (just for research to see if we make any break-through, spoilers - we didn't, so far atleast).

# Accomplishments that we're proud of

- Detection of lips
- Detection of speaking or not
- Detection of syllable
(Basically every milestone possible)

# What we learned

How we talk is complicated, but with enough efforts and studies it is possible to make a lips reader.

# What's next for Syllable Detection

Convert it to Lips Reader

# Requirements

- `Python 3.10` (higher versions may not be compatible)

# Run The Project

```sh
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

