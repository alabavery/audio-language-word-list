import sys
import os
import json

import spanish.download_and_parse
import metadata_generator


class WordListGetter:
    
    def __init__(self, config, target_directory):
        self.config = config
        self.target_directory = target_directory

    def save(self):
        words, additional_metadata = self.config["getter"]()
        print("got words!", flush=True)
        metadata = metadata_generator.get_metadata(words)
        metadata.update(additional_metadata)

        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        metadata_file = os.path.join(self.target_directory, 'metadata.json')
        word_file = os.path.join(self.target_directory, 'words.json')

        with open(word_file, 'w+') as f:
            f.write(json.dumps(words))
        with open(metadata_file, 'w+') as f:
            f.write(json.dumps(metadata))


config = {
    "spanish": {
        "getter": spanish.download_and_parse.main,
    }
}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Must pass target directory argument.  Passed arguments:", str(sys.argv[1:]))
        sys.exit()

    language = os.environ.get('LANGUAGE')
    c = config.get(language)
    if not c:
        print("Must include one of the following languages as environmental LANGUAGE: ", str(config.keys()))
        print("You passed:", language)
        sys.exit()

    save_target_path = sys.argv[1]
    print("Language: {lang}; target_dir: {target_dir}".format(lang=language, target_dir=save_target_path), flush=True)
    
    wlg = WordListGetter(c, os.path.join(save_target_path, language))
    wlg.save()
    print("Successfully saved word list!")
