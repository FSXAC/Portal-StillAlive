from ascii_art import *

# lyrics downloaded also from https://combineoverwiki.net/wiki/Still_Alive

class TimedLyric:
    def __init__(self, text, duration=2, pause=0, ascii_art=None):
        self.text = text
        self.duration = duration
        self.pause = pause
        self.ascii_art = ascii_art
    
    def totalDuration(self):
        return self.duration + self.pause


still_alive_lyrics = [
    TimedLyric("<clear>", ascii_art=ascii_empty),
    TimedLyric("Forms FORM-29827281-12:\nTest Assessment Report\n\n", duration=7),
    TimedLyric("This was a triumph.", duration=2, pause=2),
    TimedLyric("I'm making a note here:"),
    TimedLyric("HUGE SUCCESS."),
    TimedLyric("It's hard to overstate"),
    TimedLyric("my satisfaction."),
    TimedLyric("Aperture Science", ascii_art=ascii_aperture),
    TimedLyric("We do what we must"),
    TimedLyric("because we can."),
    TimedLyric("For the good of all of us."),
    TimedLyric("Except the ones who are dead.\n", ascii_art=ascii_radiation),
    TimedLyric("But there's no sense crying"),
    TimedLyric("over every mistake."),
    TimedLyric("You just keep on trying"),
    TimedLyric("till you run out of cake."),
    TimedLyric("And the Science gets done.", ascii_art=ascii_atom),
    TimedLyric("And you make a neat gun."),
    TimedLyric("For the people who are", ascii_art=ascii_aperture),
    TimedLyric("still alive."),
    TimedLyric("<clear>"),
    # TimedLyric("<pause>"),

    TimedLyric("Forms FORM-55551-5:\nPersonnel File Addendum:\n\nDear <<Subject Name Here>>,\n\n"),
    TimedLyric("I'm not even angry."),
    TimedLyric("I'm being so sincere right now."),
    TimedLyric("Even though you broke my heart.", ascii_art=ascii_broken_heart),
    TimedLyric("And killed me."),
    TimedLyric("And tore me to pieces.", ascii_art=ascii_explosion),
    TimedLyric("And threw every piece into a fire.", ascii_art=ascii_fire),
    TimedLyric("As they burned it hurt because"),
    TimedLyric("I was so happy for you!", ascii_art=ascii_checkmark),
    TimedLyric("Now these points of data"),
    TimedLyric("make a beautiful line."),
    TimedLyric("And we're out of beta."),
    TimedLyric("We're releasing on time."),
    TimedLyric("So I'm GLaD. I got burned.", ascii_art=ascii_explosion),
    TimedLyric("Think of all the things we learned", ascii_art=ascii_atom),
    TimedLyric("for the people who are", ascii_art=ascii_aperture),
    TimedLyric("still alive."),
    TimedLyric("<clear>"),

    TimedLyric("Forms FORM-55551-6:\nPersonnel File Addendum Addendum:\n\nOne last thing:\n\n"),
    TimedLyric("Go ahead and leave me."),
    TimedLyric("I think I prefer to stay inside."),
    TimedLyric("Maybe you'll find someone else"),
    TimedLyric("to help you."),
    TimedLyric("Maybe Black Mesa...", ascii_art=ascii_black_mesa),
    TimedLyric("THAT WAS A JOKE. HA HA. FAT CHANCE."),
    TimedLyric("Anyway, this cake is great.", ascii_art=ascii_cake),
    TimedLyric("It's so delicious and moist."),
    TimedLyric("Look at me still talking", ascii_art=ascii_glados),
    TimedLyric("when there's Science to do.", ascii_art=ascii_radiation),
    TimedLyric("When I look out there,", ascii_art=ascii_aperture),
    TimedLyric("it makes me GLaD I'm not you."),
    TimedLyric("I've experiments to run.", ascii_art=ascii_atom),
    TimedLyric("There is research to be done.", ascii_art=ascii_explosion),
    TimedLyric("On the people who are", ascii_art=ascii_aperture),
    TimedLyric("still alive."),

    TimedLyric("<clear>"),
    TimedLyric("\n\n\n"),
    TimedLyric("PS: And believe me I am"),
    TimedLyric("still alive."),
    TimedLyric("PPS: I'm doing Science and I'm"),
    TimedLyric("still alive."),
    TimedLyric("PPPS: I feel FANTASTIC and I'm"),
    TimedLyric("still alive.\n"),
    TimedLyric("FINAL THOUGHT:\nWhile you're dying I'll be"),
    TimedLyric("still alive.\n"),
    TimedLyric("FINAL THOUGHT PS:\nAnd when you're dead I will be"),
    TimedLyric("still alive.\n"),
    TimedLyric("STILL ALIVE\n"),
    TimedLyric("Still alive.\n")
]