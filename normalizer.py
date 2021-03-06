from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

import_sound = ""
export_sound = "normalized_" + import_sound

sound = AudioSegment.from_file(import_sound, "mp3")
normalized_sound = match_target_amplitude(sound, -20.0)
normalized_sound.export(export_sound, format="mp3")

print("Done!")

