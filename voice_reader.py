import pyttsx3

class VoiceReader():
    def __init__(self) -> None:
        self.mouth = pyttsx3.init()

        self.defaultSettings()

    def defaultSettings(self) -> None:
        self.mouth.setProperty("rate", 130)

        for voice in self.mouth.getProperty("voices"):
            if voice.id.split("\\")[-1] == "MSTTS_V110_viVN_An":
                self.mouth.setProperty("voice", voice.id)

    def changeRate(self, rate: int) -> None:
        self.mouth.setProperty("rate", rate)

    def changeVoice(self, voice: str) -> None:
        self.mouth.setProperty("voice", voice)

    def getListOfVoices(self) -> list:
        listOfVoices = []

        for nameOfVoice in self.mouth.getProperty("voices"):
            listOfVoices.append(nameOfVoice.id.split("\\")[-1])

        return listOfVoices

    def speak(self, text: str) -> None:
        self.mouth.say(text)
        self.mouth.runAndWait()