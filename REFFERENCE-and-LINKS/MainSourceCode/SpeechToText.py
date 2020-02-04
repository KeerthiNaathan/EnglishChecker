import speech_recognition as sr
import enchant


###############################################

def checker(audio_file_s):
    audio_file = sr.AudioFile(audio_file_s)
    r = sr.Recognizer()
    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    value = r.recognize_google(audio)
    print(f'AUDIO to TEXT : {value}')
    words = str(value).split()

    enc = enchant.Dict('en_US')
    english_words = 0

    for i in words:
        val = enc.check(i)
        if val:
            english_words += 1

    print(f'total English words you speak today : {english_words}\n'
          f'total Words do you speak today : {len(words)}')

if __name__ == '__main__':
    checker('Sample2.wav')