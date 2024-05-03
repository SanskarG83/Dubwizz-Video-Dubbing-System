def mlalgo(language):
    from transformers import pipeline, MBartForConditionalGeneration, MBart50TokenizerFast
    from datasets import Dataset
    from datasets import Audio
    import soundfile as sf
    import torch
    from aksharamukha import transliterate
    import final_video as final
    import os
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
        device=device,
    )

    ds = Dataset.from_dict({"audio": ["extracted\\audio_only.mp3"]}).cast_column("audio", Audio())
    sample = ds[0]["audio"]

    prediction = pipe(sample.copy(), batch_size=8)["text"]
    print(prediction)

    prediction = pipe(sample.copy(), batch_size=8, return_timestamps=False)

    print(prediction)
    English_text = str(prediction['text'])
    with open("Output\\eng_sub.txt", "w") as file:
        file.write(English_text)
    print("English Subtitle File Saved Successfully")

    # Language Translation - Text to Text

    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

    model_inputs = tokenizer(English_text, return_tensors="pt")

    if language == "hindi":
        tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
        )
    elif language == "bengali":
        tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["bn_IN"]
        )
    elif language == "tamil":
        tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"]
        )
    elif language == "telugu":
        tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["te_IN"]
        )
    elif language == "gujarati":
        tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"]
        )

    print(tokenizer.batch_decode(tokens, skip_special_tokens=True))

    trans_text = str(tokenizer.batch_decode(tokens, skip_special_tokens=True)[0])

    with open("Output\\trans_sub.txt", "w", encoding="utf-8") as file:
        file.write(trans_text)
    print("Translated Subtitle File Saved Successfully")
    # Text to Speech -

    model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                         model='silero_tts',
                                         language='indic',
                                         speaker='v4_indic')
    if language == "hindi":
        roman_text = transliterate.process('Devanagari', 'ISO', trans_text)
        audio = model.apply_tts(roman_text,
                                speaker='hindi_female')
    elif language == "bengali":
        roman_text = transliterate.process('Bengali', 'ISO', trans_text)
        audio = model.apply_tts(roman_text,
                                speaker='bengali_female')
    elif language == "tamil":
        roman_text = transliterate.process('Tamil', 'ISO', trans_text, pre_options=['TamilTranscribe'])
        audio = model.apply_tts(roman_text,
                                speaker='tamil_female')
    elif language == "telugu":
        roman_text = transliterate.process('Telugu', 'ISO', trans_text)
        audio = model.apply_tts(roman_text,
                                speaker='telugu_female')
    elif language == "gujarati":
        roman_text = transliterate.process('Gujarati', 'ISO', trans_text)
        audio = model.apply_tts(roman_text,
                                speaker='gujarati_female')

    output_path = 'Output\\translated_audio.mp3'
    sf.write(output_path, audio.squeeze().numpy(), 48000)

    video_file_path = "extracted\\video_without_audio.mp4"
    audio_file_path = "Output\\translated_audio.mp3"
    output_file_path = os.path.join("Final", "dubbed_video.mp4")

    final.combine_video_with_audio(video_file_path, audio_file_path, output_file_path)
